"""Dump a few model predictions, so the paper can show what the networks output.

    python3 tools/dump_preds.py --out preds.npz            # 40 dB and 20 dB
    python3 tools/dump_preds.py --out preds.npz --seeds 0 1 2

Run on the machine that holds the weights. Every figure so far shows the DATA
(inputs, targets) and the STATISTICS, but no segmentation paper should ship
without showing what the model actually produced -- and both referees complained
that the figures do not explain themselves.

This writes a small file (a few MB) so it can be carried back for plotting,
rather than moving 12.5 GB of checkpoints.

The normalisation is the one the models were trained under: recomputed from the
training split of the file passed in, exactly as tools/evaluate.py does. Nothing
here re-derives a scale of its own.
"""
from __future__ import annotations

import argparse
from pathlib import Path

import numpy as np
import torch

import sys
sys.path.insert(0, str(Path(__file__).resolve().parent))
from arms import build_arm                         # noqa: E402
from train_arms import load_dataset, normalise     # noqa: E402

ARMS = ["B_wide", "D"]          # the primary contrast
QA = 0.25


def qa_mask(img, fov):
    a = np.abs(img) * fov
    m = a.max()
    return a > QA * m if m > 0 else np.zeros_like(a, bool)


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--sweep", type=Path, default=Path.home() / "work/sunet_sweep")
    ap.add_argument("--runs", type=Path, default=Path("runs"))
    ap.add_argument("--levels", nargs="+", type=int, default=[40, 20])
    ap.add_argument("--seeds", nargs="+", type=int, default=[0])
    ap.add_argument("--n-images", type=int, default=6)
    ap.add_argument("--out", type=Path, required=True)
    a = ap.parse_args()

    dev = ("cuda" if torch.cuda.is_available()
           else "mps" if torch.backends.mps.is_available() else "cpu")
    out: dict[str, np.ndarray] = {}

    for lv in a.levels:
        data = a.sweep / f"v2_snr{lv}/dataset.mat"
        mixed, lung, heart, idx, fov = load_dataset(data)
        mu, sd, (mn, ln, hn) = normalise(mixed[idx["train"]], fov, mixed, lung, heart)
        print(f"{lv} dB: mu {mu!r} sd {sd!r}")
        test = idx["test"][: a.n_images]
        out[f"input_{lv}"] = mn[test]
        out[f"true_lung_{lv}"] = ln[test]
        out[f"true_heart_{lv}"] = hn[test]
        out["fov"] = fov
        out["test_idx"] = np.array(test)

        x = torch.from_numpy(mn[test]).unsqueeze(1).to(dev)
        for arm in ARMS:
            for seed in a.seeds:
                ckpt = a.runs / f"{arm}_seed{seed}.pt"
                if not ckpt.exists():
                    raise SystemExit(f"missing {ckpt}")
                model = build_arm(arm).to(dev)
                model.load_state_dict(torch.load(ckpt, map_location=dev))
                model.eval()
                with torch.no_grad():
                    y = model(x).cpu().numpy()
                out[f"pred_{arm}_s{seed}_{lv}"] = y
                d_l = np.mean([_dsc(qa_mask(y[i, 0], fov), qa_mask(ln[t], fov))
                               for i, t in enumerate(test)])
                d_h = np.mean([_dsc(qa_mask(y[i, 1], fov), qa_mask(hn[t], fov))
                               for i, t in enumerate(test)])
                print(f"  {arm:7s} seed{seed}  lung {d_l:.4f}  heart {d_h:.4f}")

    np.savez_compressed(a.out, **out)
    print(f"\nwrote {a.out}  {a.out.stat().st_size/1e6:.1f} MB")


def _dsc(p, g):
    s = p.sum() + g.sum()
    return 1.0 if s == 0 else 2.0 * (p & g).sum() / s


if __name__ == "__main__":
    main()
