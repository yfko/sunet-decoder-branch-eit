"""Five U-Net arms for the divided-branch study.

The arms differ ONLY in decoder topology and width. Encoder, block structure,
skip connections, normalisation and initialisation are shared, so any measured
difference is attributable to the decoder.

    A       1 decoder, base width, 1 output (lung)          historical baseline
    B       1 decoder, base width, 2 outputs                multi-task, no branch
    B_wide  1 decoder, widened to D's parameter count       CAPACITY CONTROL
    C       2 decoders, split at the last block, 2 outputs  late branch
    D       2 decoders, split at the bottleneck, 2 outputs  early branch

The primary contrast is D vs B_wide: same parameters, same supervision, the
only difference is whether the decoder is split. See
Nov142025/ARS_Review_2026-08-27/09_Step3_Training_Protocol.md section 1.

Outputs are linear (no sigmoid). The targets are GREIT reconstructions whose
values reach -75; a sigmoid cannot represent them. The previous implementation
used sigmoid + binary cross-entropy against continuous targets.
"""

from __future__ import annotations

import torch
import torch.nn as nn

__all__ = ["build_arm", "ARMS", "count_params", "match_width"]

ARMS = ("A", "B", "B_wide", "C", "D", "C_wide")


def _block(cin: int, cout: int) -> nn.Sequential:
    """Two 3x3 convolutions, the U-Net unit. BatchNorm added for seed stability;
    it is present in every arm, so it cannot favour one."""
    return nn.Sequential(
        nn.Conv2d(cin, cout, 3, padding=1, bias=False),
        nn.BatchNorm2d(cout),
        nn.ReLU(inplace=True),
        nn.Conv2d(cout, cout, 3, padding=1, bias=False),
        nn.BatchNorm2d(cout),
        nn.ReLU(inplace=True),
    )


class _Encoder(nn.Module):
    """Shared contracting path. Identical in every arm."""

    def __init__(self, cin: int = 1, base: int = 32, depth: int = 4):
        super().__init__()
        self.depth = depth
        chans = [base * 2**i for i in range(depth)]
        self.blocks = nn.ModuleList()
        c = cin
        for ch in chans:
            self.blocks.append(_block(c, ch))
            c = ch
        self.pool = nn.MaxPool2d(2)
        self.bottleneck = _block(c, c * 2)
        self.skip_chans = chans          # fine -> coarse
        self.bott_chans = c * 2

    def forward(self, x):
        skips = []
        for blk in self.blocks:
            x = blk(x)
            skips.append(x)
            x = self.pool(x)
        x = self.bottleneck(x)
        return x, skips


class _DecoderStage(nn.Module):
    """One upsample + skip-concat + conv block."""

    def __init__(self, cin: int, cskip: int, cout: int):
        super().__init__()
        self.up = nn.ConvTranspose2d(cin, cout, 2, stride=2)
        self.blk = _block(cout + cskip, cout)

    def forward(self, x, skip):
        x = self.up(x)
        return self.blk(torch.cat([x, skip], dim=1))


class _Decoder(nn.Module):
    """Full expanding path. `split_at` marks how many stages are *private* to
    this decoder when it is used as a branch; the module itself is agnostic."""

    def __init__(self, bott: int, skips: list[int], width_mult: float = 1.0,
                 n_out: int = 1, stages: int | None = None,
                 cin_override: int | None = None):
        super().__init__()
        skips_rev = list(reversed(skips))                # coarse -> fine
        widths = [max(8, int(round(s * width_mult / 8)) * 8) for s in skips_rev]
        self.stages = nn.ModuleList()
        c = cin_override if cin_override is not None else bott
        n = len(skips_rev) if stages is None else stages
        for i in range(n):
            self.stages.append(_DecoderStage(c, skips_rev[i], widths[i]))
            c = widths[i]
        self.out_ch = c
        self.head = nn.Conv2d(c, n_out, 1) if n_out else None

    def forward(self, x, skips_rev, start: int = 0):
        for i, st in enumerate(self.stages):
            x = st(x, skips_rev[start + i])
        return self.head(x) if self.head is not None else x


class UNetArm(nn.Module):
    """One arm. `arm` selects the decoder topology."""

    def __init__(self, arm: str, base: int = 32, depth: int = 4,
                 width_mult: float = 1.0):
        super().__init__()
        if arm not in ARMS:
            raise ValueError(f"unknown arm {arm!r}; expected one of {ARMS}")
        self.arm = arm
        self.enc = _Encoder(1, base, depth)
        b, sk = self.enc.bott_chans, self.enc.skip_chans

        if arm == "A":
            self.dec = _Decoder(b, sk, 1.0, n_out=1)
        elif arm == "B":
            self.dec = _Decoder(b, sk, 1.0, n_out=2)
        elif arm == "B_wide":
            self.dec = _Decoder(b, sk, width_mult, n_out=2)
        elif arm in ("C", "C_wide"):
            # Shared trunk for all but the final stage, then two private tails.
            wm = width_mult if arm == "C_wide" else 1.0
            self.trunk = _Decoder(b, sk, wm, n_out=0, stages=depth - 1)
            tail_in, tail_skip = self.trunk.out_ch, sk[0]
            tw = max(8, int(round(sk[0] * wm / 8)) * 8)
            self.tail_l = nn.Sequential()
            self.tail_l.add_module("st", _DecoderStage(tail_in, tail_skip, tw))
            self.tail_r = nn.Sequential()
            self.tail_r.add_module("st", _DecoderStage(tail_in, tail_skip, tw))
            self.head_l = nn.Conv2d(tw, 1, 1)
            self.head_r = nn.Conv2d(tw, 1, 1)
        elif arm == "D":
            # Two complete private decoders from the bottleneck.
            self.dec_l = _Decoder(b, sk, 1.0, n_out=1)
            self.dec_r = _Decoder(b, sk, 1.0, n_out=1)

    def forward(self, x):
        z, skips = self.enc(x)
        skips_rev = list(reversed(skips))
        if self.arm in ("A", "B", "B_wide"):
            return self.dec(z, skips_rev)
        if self.arm in ("C", "C_wide"):
            h = self.trunk(z, skips_rev)
            last = skips_rev[-1]
            l = self.head_l(self.tail_l.st(h, last))
            r = self.head_r(self.tail_r.st(h, last))
            return torch.cat([l, r], dim=1)
        l = self.dec_l(z, skips_rev)
        r = self.dec_r(z, skips_rev)
        return torch.cat([l, r], dim=1)


def count_params(m: nn.Module) -> int:
    return sum(p.numel() for p in m.parameters() if p.requires_grad)


def match_width(target_arm: str, control_arm: str, base: int = 32,
                depth: int = 4, tol: float = 0.01,
                lo: float = 1.0, hi: float = 3.0, iters: int = 40):
    """Find width_mult so that `control_arm` matches `target_arm` in parameters.

    Bisection on a monotone quantity; returns (width_mult, n_target, n_control).
    Widening is quantised to multiples of 8 channels, so an exact match is not
    always reachable -- report the residual rather than pretending it is zero.
    """
    n_target = count_params(UNetArm(target_arm, base, depth))
    best = None
    for _ in range(iters):
        mid = (lo + hi) / 2
        n_ctrl = count_params(UNetArm(control_arm, base, depth, width_mult=mid))
        rel = (n_ctrl - n_target) / n_target
        if best is None or abs(rel) < abs(best[2]):
            best = (mid, n_ctrl, rel)
        if abs(rel) <= tol:
            break
        if n_ctrl < n_target:
            lo = mid
        else:
            hi = mid
    return best[0], n_target, best[1]


def build_arm(arm: str, base: int = 32, depth: int = 4,
              width_mult: float | None = None) -> UNetArm:
    """Construct an arm. For the width-matched controls, `width_mult` is solved
    for automatically unless given explicitly."""
    if width_mult is None and arm in ("B_wide", "C_wide"):
        ref = "D"
        width_mult, _, _ = match_width(ref, arm, base, depth)
    return UNetArm(arm, base, depth, width_mult or 1.0)


if __name__ == "__main__":
    # Parameter table -- print this into the paper. The capacity claim is only
    # as good as these numbers, so they belong in the manuscript, not a footnote.
    print(f"{'arm':8s} {'width_mult':>10s} {'params':>12s}")
    for a in ARMS:
        wm = None
        if a in ("B_wide", "C_wide"):
            wm, n_t, n_c = match_width("D" if a == "B_wide" else "D", a)
        m = build_arm(a, width_mult=wm)
        print(f"{a:8s} {(wm or 1.0):10.4f} {count_params(m):12,d}")
