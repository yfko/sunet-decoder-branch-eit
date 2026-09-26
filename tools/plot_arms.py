"""Generate PlotNeuralNet .tex for each of the six ablation arms.

    python3 tools/plot_arms.py            # writes figures/tex/arm_*.tex

Driven by tools/arch_spec.json, which is itself dumped from the live models in
tools/arms.py — so the channel counts and split points in the figure cannot
drift away from the code that is actually trained.

To render:  bash tools/build_figures.sh     (TinyTeX is installed at
~/Library/TinyTeX; the script handles the space-in-path problem).

Follows the idiom of PlotNeuralNet/pyexamples/unet.py so the output sits beside
the existing Fig. 3 rather than looking like a different tool made it.
"""

from __future__ import annotations

import json
import math
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.append(str(HERE / "PlotNeuralNet"))
from pycore.tikzeng import (                     # noqa: E402
    to_head, to_cor, to_begin, to_end, to_generate,
    to_ConvConvRelu, to_Pool, to_UnPool, to_ConvSoftMax,
    to_connection, to_skip,
)

# spatial edge of the drawn box at each depth (64, 32, 16, 8, 4 px feature maps)
SIZE = [40, 32, 25, 16, 8]


def skip_below(of, to, pos=-0.35):
    """Mirror of tikzeng.to_skip that routes the connection UNDER the figure.

    to_skip interpolates south->north at pos=1.25, i.e. above the block. With
    two decoders both fed by the same encoder, sending all eight skips over the
    top produces a thicket that crosses every box. The lower branch uses this
    instead, so the two bundles never meet."""
    return (f"\n\\path ({of}-southeast) -- ({of}-northeast) "
            f"coordinate[pos={pos}] ({of}-bot) ;\n"
            f"\\path ({to}-south)  -- ({to}-north)  "
            f"coordinate[pos={pos}] ({to}-bot) ;\n"
            f"\\draw [copyconnection]  ({of}-southeast)\n"
            f"-- node {{\\copymidarrow}}({of}-bot)\n"
            f"-- node {{\\copymidarrow}}({to}-bot)\n"
            f"-- node {{\\copymidarrow}} ({to}-south);\n")


def wid(ch: int) -> float:
    """Drawn thickness from channel count, on PlotNeuralNet's own scale.

    Floored at 32 channels rather than extrapolating down: at the original
    scale a 32-channel block came out 0.85 thick and its two xlabel numbers
    printed on top of each other."""
    return round(1.6 + 1.0 * math.log2(max(ch, 32) / 32), 2)


def encoder(spec):
    """Shared contracting path. Identical in every arm."""
    out, prev = [], None
    for d, ch in enumerate(spec["enc"]):
        s = SIZE[d]
        out.append(to_ConvConvRelu(
            name=f"ccr_e{d}", s_filer=64 >> d, n_filer=(ch, ch),
            offset="(0,0,0)" if prev is None else "(1.1,0,0)",
            to="(0,0,0)" if prev is None else f"({prev}-east)",
            width=(wid(ch), wid(ch)), height=s, depth=s))
        out.append(to_Pool(name=f"pool_e{d}", offset="(0,0,0)",
                           to=f"(ccr_e{d}-east)",
                           width=1, height=s * 0.8, depth=s * 0.8, opacity=0.5))
        if prev is not None:
            out.append(to_connection(prev, f"ccr_e{d}"))
        prev = f"pool_e{d}"
    return out, prev


def bottleneck(spec, prev):
    ch, s = spec["bottleneck"], SIZE[4]
    out = [to_ConvConvRelu(name="ccr_bn", s_filer=4, n_filer=(ch, ch),
                           offset="(1.8,0,0)", to=f"({prev}-east)",
                           width=(wid(ch), wid(ch)), height=s, depth=s,
                           caption="Bottleneck"),
           to_connection(prev, "ccr_bn")]
    return out, "ccr_bn"


def decoder(widths, prev, tag, y=0.0, first_offset=2.0, skip_from=None,
            side="above"):
    """One ascending path. `y` shifts the whole chain so two branches can run
    in parallel without colliding; `skip_from` names the encoder blocks whose
    skip connections feed it."""
    out = []
    for i, ch in enumerate(widths):
        d = len(SIZE) - 2 - i            # 3, 2, 1, 0 for a four-stage decoder
        s = SIZE[d]
        off = f"({first_offset},{y},0)" if i == 0 else "(1.6,0,0)"
        out.append(to_UnPool(name=f"unpool_{tag}{i}", offset=off,
                             to=f"({prev}-east)",
                             width=1, height=s * 0.8, depth=s * 0.8, opacity=0.5))
        out.append(to_ConvConvRelu(
            name=f"ccr_{tag}{i}", s_filer=64 >> d, n_filer=(ch, ch),
            offset="(0,0,0)", to=f"(unpool_{tag}{i}-east)",
            width=(wid(ch), wid(ch)), height=s, depth=s))
        out.append(to_connection(prev, f"unpool_{tag}{i}"))
        if skip_from is not None:
            out.append(to_skip(of=f"ccr_e{d}", to=f"ccr_{tag}{i}", pos=1.25)
                       if side == "above"
                       else skip_below(f"ccr_e{d}", f"ccr_{tag}{i}"))
        prev = f"ccr_{tag}{i}"
    return out, prev


def head(prev, name, caption, y=0.0):
    return [to_ConvSoftMax(name=name, s_filer=64, offset=f"(1.0,{y},0)",
                           to=f"({prev}-east)", width=1, height=SIZE[0],
                           depth=SIZE[0], caption=caption),
            to_connection(prev, name)]


def build(arm: str, spec: dict):
    arch = [to_head(str(HERE / "PlotNeuralNet")), to_cor(), to_begin()]
    enc, prev = encoder(spec)
    arch += enc
    bn, prev = bottleneck(spec, prev)
    arch += bn

    if arm in ("A", "B", "B_wide"):
        dec, last = decoder(spec["dec"], prev, "d", skip_from=True)
        arch += dec
        if spec["heads"] == 1:
            arch += head(last, "out_lung", "lung")
        else:
            arch += head(last, "out_lung", "lung", y=3.2)
            arch += head(last, "out_heart", "heart", y=-3.2)

    elif arm in ("C", "C_wide"):
        trunk, last = decoder(spec["trunk"], prev, "t", skip_from=True)
        arch += trunk
        # two short private tails, offset above and below the shared trunk
        for tag, cap, y, side in (("l", "lung", 5.5, "above"),
                                  ("r", "heart", -5.5, "below")):
            tail, tlast = decoder([spec["tail"]], last, tag, y=y,
                                  first_offset=1.8, skip_from=True, side=side)
            arch += tail
            arch += head(tlast, f"out_{cap}", cap)

    else:  # D — two complete private decoders from the bottleneck
        for tag, cap, y, widths, side in (
                ("l", "lung",  7.0, spec["dec_l"], "above"),
                ("r", "heart", -7.0, spec["dec_r"], "below")):
            dec, last = decoder(widths, prev, tag, y=y, skip_from=True,
                                side=side)
            arch += dec
            arch += head(last, f"out_{cap}", cap)

    arch.append(to_end())
    return arch


def main():
    spec = json.loads((HERE / "arch_spec.json").read_text())
    outdir = HERE.parent / "figures" / "tex"
    outdir.mkdir(parents=True, exist_ok=True)
    for arm in ("A", "B", "B_wide", "C", "C_wide", "D"):
        f = outdir / f"arm_{arm}.tex"
        to_generate(build(arm, spec[arm]), str(f))
        print(f"{arm:8s} -> {f.relative_to(HERE.parent)}  "
              f"({spec[arm]['params']:,} params)")
    print(f"\n{len(list(outdir.glob('*.tex')))} files in {outdir}")
    print("render with: bash tools/build_figures.sh")


if __name__ == "__main__":
    main()
