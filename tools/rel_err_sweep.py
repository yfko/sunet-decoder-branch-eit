"""Relative error reduction of D over B_wide at every SNR level, both channels.

    python3 tools/rel_err_sweep.py

Why this exists (plan-stage stress test, 2026-09-22): the raw-point sweep shows
a step between 40 and 30 dB, but DSC is bounded above and the two arms sit at
0.966-0.969 for 60/50/40 dB, so a reviewer can read the flat top as ceiling
compression rather than an onset. Dividing each seed's paired difference by the
control arm's own error at that level removes the ceiling. The 20 dB value of
this quantity is already reported (RESULTS_STUDY2.md section 4, fig_snr_sweep
panel b); this script reports it at every level so the shape can be judged with
the ceiling taken out.

Definition, identical to make_fig_snr.py panel (b), per seed s and level L:

    rel_s(L) = ( DSC_D,s(L) - DSC_Bwide,s(L) ) / ( 1 - DSC_Bwide,s(L) )

reported as mean over the 58 registered seeds with a 95% percentile bootstrap
CI over seeds (seeds are the unit of replication; resampling preserves the
within-seed pairing across arms). Not a registered analysis: descriptive.
"""
from __future__ import annotations

import argparse
import csv
import json
from pathlib import Path

import numpy as np

SEEDS = list(range(58))
LEVELS = [60, 50, 40, 35, 30, 25, 20]   # 35/25 added 2026-09-24 per PREREGISTRATION_HEART.md section 9.3 (descriptive)


def per_seed(results_dir: Path, arm: str, channel: str) -> np.ndarray:
    got: dict[int, float] = {}
    with open(results_dir / "per_seed.csv") as fh:
        for r in csv.DictReader(fh):
            if r["arm"] == arm and r["channel"] == channel:
                got[int(r["seed"])] = float(r["dsc"])
    missing = [s for s in SEEDS if s not in got]
    if missing:
        raise SystemExit(f"{results_dir}: arm {arm} missing seeds {missing}")
    return np.array([got[s] for s in SEEDS])


def boot_ci(v: np.ndarray, rng: np.random.Generator, n_boot: int) -> tuple[float, float]:
    idx = rng.integers(0, len(v), size=(n_boot, len(v)))
    means = v[idx].mean(axis=1)
    return float(np.percentile(means, 2.5)), float(np.percentile(means, 97.5))


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--pattern", default="results_v2_snr{L}_heart_fix",
                    help="results dir per level; {L} is replaced by the SNR")
    ap.add_argument("--treat", default="D")
    ap.add_argument("--control", default="B_wide")
    ap.add_argument("--n-boot", type=int, default=100000)
    ap.add_argument("--seed", type=int, default=20260922)
    ap.add_argument("--out", type=Path, default=Path("results_v2_rel_err_sweep"))
    a = ap.parse_args()

    rng = np.random.default_rng(a.seed)
    rows = []
    for ch in ("heart", "lung"):
        for L in LEVELS:
            d = Path(a.pattern.format(L=L))
            t, c = per_seed(d, a.treat, ch), per_seed(d, a.control, ch)
            raw = (t - c) * 100                       # DSC points
            rel = (t - c) / (1 - c) * 100             # % of control's own error
            rlo, rhi = boot_ci(raw, rng, a.n_boot)
            lo, hi = boot_ci(rel, rng, a.n_boot)
            rows.append(dict(channel=ch, snr_db=L, n=len(SEEDS),
                             control_mean_dsc=float(c.mean()),
                             control_error_pts=float((1 - c).mean() * 100),
                             raw_diff_pts=float(raw.mean()), raw_ci_lo=rlo, raw_ci_hi=rhi,
                             rel_err_reduction_pct=float(rel.mean()), rel_ci_lo=lo, rel_ci_hi=hi,
                             seeds_positive=int((rel > 0).sum())))

    a.out.mkdir(exist_ok=True)
    with open(a.out / "rel_err_sweep.csv", "w", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=list(rows[0]))
        w.writeheader(); w.writerows(rows)
    with open(a.out / "rel_err_sweep.json", "w") as fh:
        json.dump(dict(definition="(D - B_wide) / (1 - B_wide) per seed, mean over seeds, "
                                  "95% percentile bootstrap over seeds",
                       treat=a.treat, control=a.control, n_boot=a.n_boot,
                       rng_seed=a.seed, source_pattern=a.pattern, rows=rows), fh, indent=2)

    # Markdown table, every number computed above and none typed
    lines = ["| channel | SNR | B_wide DSC | B_wide error (pts) | D − B_wide (pts) [95% CI] "
             "| relative error reduction (%) [95% CI] | seeds > 0 |",
             "|---|---|---|---|---|---|---|"]
    for r in rows:
        lines.append(f"| {r['channel']} | {r['snr_db']} dB | {r['control_mean_dsc']:.4f} | "
                     f"{r['control_error_pts']:.2f} | {r['raw_diff_pts']:+.3f} "
                     f"[{r['raw_ci_lo']:+.3f}, {r['raw_ci_hi']:+.3f}] | "
                     f"{r['rel_err_reduction_pct']:+.2f} [{r['rel_ci_lo']:+.2f}, {r['rel_ci_hi']:+.2f}] "
                     f"| {r['seeds_positive']}/{r['n']} |")
    (a.out / "rel_err_sweep.md").write_text("\n".join(lines) + "\n")
    print("\n".join(lines))


if __name__ == "__main__":
    main()
