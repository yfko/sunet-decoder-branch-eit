"""H3: does the branching advantage grow as SNR falls?

    python3 tools/h3_snr.py --results results_v2_snr60 ... --snr 60 50 40 30 20

PREREGISTRATION_HEART.md section 3 registers the rule verbatim:

    confirmed if  the paired difference (D - B_wide) at the LOWEST SNR level
                  exceeds that at the HIGHEST, with a 95% bootstrap CI on the
                  difference-of-differences excluding zero
    falsified if  the CI contains zero, or the ordering is reversed

The bootstrap resamples SEEDS, not images: seeds are the unit of replication in
this design, and the same 58 seeds appear at every SNR level, so the level-to-
level comparison is paired within seed and the resample must preserve that.

This computes the registered statistic and nothing else. It does not search over
levels for the largest gap -- the two levels tested are fixed by the rule as the
extremes of the registered sweep.
"""
from __future__ import annotations

import argparse
import csv
import math
from collections import defaultdict
from pathlib import Path

import numpy as np

SEEDS = list(range(58))    # registered n = 58


def per_seed(results_dir: Path, arm: str, channel: str) -> np.ndarray:
    """Mean DSC per seed for one arm, in registered seed order."""
    got: dict[int, float] = {}
    with open(results_dir / "per_seed.csv") as fh:
        for r in csv.DictReader(fh):
            if r["arm"] == arm and r["channel"] == channel:
                got[int(r["seed"])] = float(r["dsc"])
    missing = [s for s in SEEDS if s not in got]
    if missing:
        raise SystemExit(f"{results_dir}: arm {arm} missing seeds {missing}")
    return np.array([got[s] for s in SEEDS])


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--results", nargs="+", required=True, type=Path,
                    help="one results dir per SNR level, same order as --snr")
    ap.add_argument("--snr", nargs="+", required=True, type=float)
    ap.add_argument("--treat", default="D")
    ap.add_argument("--control", default="B_wide")
    ap.add_argument("--channel", default="heart", choices=["heart", "lung"],
                    help="heart is the registered primary endpoint. lung is the\n"
                         "discriminating control: if branching helps the lung\n"
                         "channel equally at low SNR, the effect is general noise\n"
                         "robustness, not the claimed protection of the weak component.")
    ap.add_argument("--n-boot", type=int, default=100000)
    ap.add_argument("--seed", type=int, default=20260904)
    a = ap.parse_args()
    if len(a.results) != len(a.snr):
        raise SystemExit("--results and --snr must have the same length")

    delta = {}
    print(f"=== {a.channel} DSC, {a.treat} - {a.control}, per SNR level ===")
    print(f"{'SNR':>6s} {a.control:>10s} {a.treat:>10s} {'diff':>10s} "
          f"{'SD_diff':>9s} {'dz':>7s}")
    for snr, d in sorted(zip(a.snr, a.results), key=lambda t: -t[0]):
        t, c = per_seed(d, a.treat, a.channel), per_seed(d, a.control, a.channel)
        df = t - c
        delta[snr] = df
        print(f"{snr:6.0f} {c.mean():10.5f} {t.mean():10.5f} {df.mean():+10.5f} "
              f"{df.std(ddof=1):9.5f} {df.mean()/df.std(ddof=1):+7.3f}")

    lo_snr, hi_snr = min(a.snr), max(a.snr)
    d_lo, d_hi = delta[lo_snr], delta[hi_snr]
    dod = d_lo - d_hi                      # paired within seed
    obs = dod.mean()

    rng = np.random.default_rng(a.seed)
    idx = rng.integers(0, len(SEEDS), (a.n_boot, len(SEEDS)))
    bs = dod[idx].mean(axis=1)
    lo, hi = np.percentile(bs, [2.5, 97.5])

    label = ("H3, registered rule" if a.channel == "heart"
             else "lung channel -- NOT H3; the discriminating control")
    print(f"\n=== {label} ===")
    print(f"  difference-of-differences  D({lo_snr:.0f} dB) - D({hi_snr:.0f} dB)"
          f" = {obs:+.5f} DSC  ({obs*100:+.3f} points)")
    print(f"  95% bootstrap CI over {len(SEEDS)} seeds  "
          f"[{lo:+.5f}, {hi:+.5f}]  ({a.n_boot:,} resamples)")

    grew = obs > 0
    excl = (lo > 0) or (hi < 0)
    if a.channel != "heart":
        print("  Lung is not an H3 endpoint. Read it against the heart result:\n"
              "  a comparable lung growth means the low-SNR effect is general\n"
              "  noise robustness, NOT protection of the suppressed component.")
    elif grew and excl:
        print("  VERDICT: H3 CONFIRMED -- the advantage grows as SNR falls.")
    elif not grew:
        print("  VERDICT: H3 FALSIFIED -- ordering reversed "
              "(the difference does not grow as SNR falls).")
    else:
        print("  VERDICT: H3 FALSIFIED -- 95% CI contains zero.")
    print("\nWhichever way this falls, it is the finding. Report it as it is.")


if __name__ == "__main__":
    main()
