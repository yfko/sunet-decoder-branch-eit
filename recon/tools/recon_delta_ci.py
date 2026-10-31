"""RECON revision round 1 (2026-10-10, panel REV-14 / REV-4 / REV-12): per-cell statistics on the paired
D - B_wide heart-DSC difference that RESULTS_RECON.md did not report, from per_seed.csv only.

    python3 tools/recon_delta_ci.py --results results_recon --runmeta <dir with runs_*/ *_seed*.json> \
        --out results_recon/recon_delta_ci.json

For every tested cell (R1 x2, GREIT diagonal 30 and 58, M1 x3, M1' x3): mean Delta, SD of the thirty paired
differences, 95% percentile bootstrap CI on Delta (100,000 resamples, seed 20260904, seeds resampled, the
same procedure as R3 in tools/recon_results.py), Wilcoxon W (sum of positive ranks, scipy `wilcoxon`
statistic under the registered call: two-sided, normal approximation, continuity correction, zero
differences handled by scipy's default 'wilcox' zero_method), the number of exact zero differences and of
tied absolute differences.  For the six R3 cells: SD of the per-seed difference of differences and the
difference of differences detectable with 80% power at n = 30 (paired t approximation, dz = 0.53), which
is the achieved-sensitivity figure REV-4 asked for; the same for E1.  Epoch counts and wall-clock minutes
per arm per row from the training metadata (REV-12 / REV-14). No registered verdict is touched; this file
adds columns, it changes none.
"""
from __future__ import annotations
import argparse, csv, json, sys
from pathlib import Path
import numpy as np
from scipy.stats import wilcoxon, rankdata
sys.path.insert(0, str(Path(__file__).parent))
from recon_results import load, boot, SEEDS, RECON  # noqa

DZ80 = 0.53  # paired, two-sided alpha 0.05, n = 30: dz for 80% power (t approximation)

def cell_stats(R, cell, B, S, seeds=SEEDS):
    d, b = load(R, cell, "D", "heart", seeds), load(R, cell, "B_wide", "heart", seeds)
    diff = d - b
    w = wilcoxon(d, b, correction=True, method="approx")
    nz = diff[diff != 0]
    ranks = rankdata(np.abs(nz))
    ties = int(len(ranks) - len(np.unique(ranks)))
    lo, hi = boot(diff, B, S)
    return {"n": len(seeds), "delta_mean": float(diff.mean()), "delta_sd": float(diff.std(ddof=1)),
            "delta_ci95": [lo, hi], "wilcoxon_W": float(w.statistic), "p_wilcoxon": float(w.pvalue),
            "zero_differences": int((diff == 0).sum()), "tied_abs_differences": ties,
            "B_wide_sd_floor": float(b.std(ddof=1)), "seeds_D_gt_B": int((diff > 0).sum())}

def dod_stats(R, x, y, suffix, B, S):
    dxx = load(R, f"{x}__{x}", "D", "heart") - load(R, f"{x}__{x}", "B_wide", "heart")
    dxy = load(R, f"{x}__{y}{suffix}", "D", "heart") - load(R, f"{x}__{y}{suffix}", "B_wide", "heart")
    dod = dxy - dxx
    sd = float(dod.std(ddof=1))
    return {"dod_mean": float(dod.mean()), "dod_sd": sd, "dod_ci95": list(boot(dod, B, S)),
            "mde_80pct_power_n30_points": sd * DZ80 * 100, "realised_dz": float(dod.mean() / sd)}

def epochs(runmeta: Path, row: str, seeds=SEEDS):
    out = {}
    for arm in ("D", "B_wide"):
        ep, mn, best = [], [], []
        for s in seeds:
            f = runmeta / row / f"{arm}_seed{s}.json"
            if not f.exists():
                continue
            m = json.loads(f.read_text()); ep.append(m["epochs_run"]); best.append(m["best_epoch"]); mn.append(m["minutes"])
        if ep:
            out[arm] = {"n_runs": len(ep), "epochs_run_median": float(np.median(ep)), "epochs_run_min": int(min(ep)), "epochs_run_max": int(max(ep)),
                        "best_epoch_median": float(np.median(best)), "minutes_median": float(np.median(mn)), "minutes_total": float(sum(mn))}
    return out

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--results", type=Path, default=Path("results_recon"))
    ap.add_argument("--runmeta", type=Path, required=True)
    ap.add_argument("--out", type=Path, default=Path("results_recon/recon_delta_ci.json"))
    ap.add_argument("--n-boot", type=int, default=100000); ap.add_argument("--seed", type=int, default=20260904)
    a = ap.parse_args(); R, B, S = a.results, a.n_boot, a.seed
    res = {"n_boot": B, "boot_seed": S, "dz_80pct_power_n30": DZ80, "tested_cells": {}, "R3_dod": {}, "E1_dod": {}, "training": {}}
    cells = {"R1-GN": "gn__gn", "R1-BP": "bp__bp", "GREIT-diag-30": "greit__greit",
             "M1-(MIXED->GREIT)": "mixed__greit", "M1-(MIXED->GN)": "mixed__gn", "M1-(MIXED->BP)": "mixed__bp",
             "M1'-(MIXED-PS->GREIT)": "mixedps__greit", "M1'-(MIXED-PS->GN)": "mixedps__gn", "M1'-(MIXED-PS->BP)": "mixedps__bp"}
    for k, c in cells.items():
        res["tested_cells"][k] = {"cell": c, **cell_stats(R, c, B, S)}
    from recon_results import all_seeds
    g58 = all_seeds(R, "greit__greit")
    res["tested_cells"]["GREIT-diag-58"] = {"cell": "greit__greit", **cell_stats(R, "greit__greit", B, S, seeds=g58)}
    for x in RECON:
        for y in RECON:
            if x == y: continue
            res["R3_dod"][f"R3-({x.upper()}->{y.upper()})"] = dod_stats(R, x, y, "", B, S)
            res["E1_dod"][f"E1-({x.upper()}->{y.upper()})"] = dod_stats(R, x, y, "_e1", B, S)
    for row in ("runs_20db", "runs_recon_gn", "runs_recon_bp", "runs_recon_mixed", "runs_recon_mixed_ps"):
        res["training"][row] = epochs(a.runmeta, row)
    a.out.write_text(json.dumps(res, indent=1)); print("wrote", a.out)
    for k, v in res["tested_cells"].items():
        print(f"{k:24s} n={v['n']:2d} Δ {v['delta_mean']*100:+.3f} [{v['delta_ci95'][0]*100:+.3f}, {v['delta_ci95'][1]*100:+.3f}] sd_diff {v['delta_sd']*100:.3f} W {v['wilcoxon_W']:.1f} p {v['p_wilcoxon']:.2g} zeros {v['zero_differences']} ties {v['tied_abs_differences']} D>B {v['seeds_D_gt_B']}")
    for k, v in res["R3_dod"].items():
        print(f"{k:18s} dod {v['dod_mean']*100:+.3f} sd {v['dod_sd']*100:.2f} MDE80 {v['mde_80pct_power_n30_points']:.2f} dz {v['realised_dz']:+.2f}")
    for k, v in res["E1_dod"].items():
        print(f"{k:18s} dod {v['dod_mean']*100:+.3f} sd {v['dod_sd']*100:.2f} MDE80 {v['mde_80pct_power_n30_points']:.2f} dz {v['realised_dz']:+.2f}")
    for row, v in res["training"].items():
        for arm, e in v.items():
            print(f"{row:20s} {arm:7s} n {e['n_runs']} epochs med {e['epochs_run_median']:.0f} [{e['epochs_run_min']}-{e['epochs_run_max']}] best med {e['best_epoch_median']:.0f} min med {e['minutes_median']:.0f} total {e['minutes_total']/60:.1f} h")
if __name__ == "__main__":
    main()
