"""Geometry-level bootstrap of D - B_wide (PREREGISTRATION_HEART.md section 9.4).

    python3 tools/geom_bootstrap.py results_v2_fix results_v2_snr20_heart_fix results_20db_fix

The registered intervals resample SEEDS: every seed is scored on the same 360
test geometries, so those intervals describe training-run variability only.
This script resamples TEST GEOMETRIES instead: for each bootstrap draw it takes
360 frames with replacement, averages each seed's per-frame Dice over the drawn
frames, forms the paired D - B_wide difference per seed, and takes the mean over
seeds. The interval therefore describes variability across phantoms for the
mean-over-seeds contrast. Both intervals are reported side by side in the
manuscript; neither replaces the registered rule, which is defined on seeds.

Reads per_image.csv (written by tools/evaluate.py on the machine that scored the
runs). Column names are detected: an arm column, a seed column, a channel
column, an image-index column (idx / image / frame / i) and a dsc column.
"""
import csv, json, sys
from collections import defaultdict
from pathlib import Path

import numpy as np

N_BOOT, SEED = 100_000, 20260923


def load(d: Path, ch="heart"):
    rows = list(csv.DictReader(open(d / "per_image.csv")))
    cols = rows[0].keys()
    idx_col = next((c for c in ("index", "idx", "image", "frame", "i", "img") if c in cols), None)
    if idx_col is None:
        raise SystemExit(f"{d}/per_image.csv: no frame-index column among {sorted(cols)}")
    per = defaultdict(dict)          # (arm, seed) -> {idx: dsc}
    for r in rows:
        if r["channel"] != ch: continue
        per[(r["arm"], int(r["seed"]))][int(r[idx_col])] = float(r["dsc"])
    return per


def contrast(per, treat="D", ctrl="B_wide"):
    seeds = sorted({s for a, s in per if a == treat} & {s for a, s in per if a == ctrl})
    frames = sorted(per[(treat, seeds[0])].keys())
    T = np.array([[per[(treat, s)][f] for f in frames] for s in seeds])   # seeds × frames
    C = np.array([[per[(ctrl, s)][f] for f in frames] for s in seeds])
    return T, C, seeds, frames


def main():
    rng = np.random.default_rng(SEED)
    out = {}
    for arg in sys.argv[1:]:
        d = Path(arg)
        if not (d / "per_image.csv").exists():
            print(f"{d}: no per_image.csv, skipped"); continue
        T, C, seeds, frames = contrast(load(d))
        nS, nF = T.shape
        point = float((T.mean(1) - C.mean(1)).mean() * 100)
        # geometry bootstrap
        idx = rng.integers(0, nF, size=(N_BOOT, nF))
        boot = np.empty(N_BOOT)
        for b in range(N_BOOT):
            j = idx[b]
            boot[b] = (T[:, j].mean(1) - C[:, j].mean(1)).mean() * 100
        glo, ghi = np.percentile(boot, [2.5, 97.5])
        # seed bootstrap for side-by-side
        dseed = (T.mean(1) - C.mean(1)) * 100
        sidx = rng.integers(0, nS, size=(N_BOOT, nS))
        slo, shi = np.percentile(dseed[sidx].mean(1), [2.5, 97.5])
        out[d.name] = dict(n_seeds=nS, n_frames=nF, diff_pts=point,
                           geometry_ci=[float(glo), float(ghi)], seed_ci=[float(slo), float(shi)])
        print(f"{d.name}: D-B_wide {point:+.3f} pts | geometry CI [{glo:+.3f}, {ghi:+.3f}] | seed CI [{slo:+.3f}, {shi:+.3f}]  ({nS} seeds × {nF} frames)")
    Path("results").mkdir(exist_ok=True)
    json.dump(dict(n_boot=N_BOOT, rng_seed=SEED, results=out), open("results/geom_bootstrap.json", "w"), indent=2)
    print("wrote results/geom_bootstrap.json")


if __name__ == "__main__":
    main()
