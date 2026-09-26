"""Re-derive every manuscript number that is not already printed by make_tables.py
(MANUSCRIPT_RULES R10c). Reads per_seed.csv files only; writes
results/manuscript_numbers.json. Never typed, never copied from a draft.

    python3 tools/verify_manuscript_numbers.py
"""
import json, sys
from pathlib import Path
import numpy as np
from scipy.stats import wilcoxon, spearmanr

sys.path.insert(0, str(Path(__file__).parent))
from figstyle import per_seed, boot_ci, _IDX58  # same 100,000 seed-resamples as Tables 1/2

OUT = Path("results/manuscript_numbers.json")
out = {}

def contrast(d_dir, arm_a="D", arm_b="B_wide", ch="heart"):
    a = per_seed(d_dir, arm_a, ch); b = per_seed(d_dir, arm_b, ch)
    diff = (a - b) * 100.0
    lo, hi = boot_ci(diff)
    w = wilcoxon(a, b, method="auto")  # n=58 > 50 -> normal approximation, continuity correction
    ties = int(np.sum(diff == 0))
    return {
        "mean_pts": float(diff.mean()), "median_pts": float(np.median(diff)),
        "ci95_pts": [float(lo), float(hi)],
        "dz": float(diff.mean() / diff.std(ddof=1)),
        "wilcoxon_W": float(w.statistic), "wilcoxon_p": float(w.pvalue), "ties": ties,
        "control_seed_sd_pts": float(b.std(ddof=1) * 100.0),
        "wins": int(np.sum(diff > 0)), "n": int(len(diff)),
        f"{arm_b}_mean": float(b.mean()), f"{arm_b}_sd": float(b.std(ddof=1)),
        f"{arm_a}_mean": float(a.mean()), f"{arm_a}_sd": float(a.std(ddof=1)),
        "min_pts": float(diff.min()), "max_pts": float(diff.max()),
    }

# --- 40 dB primary (H1, H2, D-B) and every sweep level, heart and lung
out["40dB_D_minus_Bwide_heart"] = contrast("results_v2_fix")
out["40dB_D_minus_Cwide_heart"] = contrast("results_v2_fix", "D", "C_wide")
out["40dB_D_minus_B_heart"] = contrast("results_v2_fix", "D", "B")
for lvl in (60, 50, 40, 35, 30, 25, 20):
    for ch in ("heart", "lung"):
        out[f"sweep_{lvl}dB_{ch}"] = contrast(f"results_v2_snr{lvl}_heart_fix", ch=ch)

# --- H5: trained and evaluated at 20 dB
out["H5_20train_20eval_heart"] = contrast("results_20db_fix")
out["H5_20train_20eval_lung"] = contrast("results_20db_fix", ch="lung")

# --- secondary (registered "reported, not tested"): Delta_20|20 minus Delta_20|40, seeds resampled in pairs
d2020 = (per_seed("results_20db_fix", "D", "heart") - per_seed("results_20db_fix", "B_wide", "heart")) * 100
d2040 = (per_seed("results_v2_snr20_heart_fix", "D", "heart") - per_seed("results_v2_snr20_heart_fix", "B_wide", "heart")) * 100
gap = d2020 - d2040
lo, hi = boot_ci(gap)
out["H5_gap_20in20_minus_20in40"] = {"mean_pts": float(gap.mean()), "ci95_pts": [float(lo), float(hi)],
                                     "shrink_factor": float(d2040.mean() / d2020.mean())}
out["H5_absolute_recovery"] = {
    "Bwide_heart_20eval_40train": float(per_seed("results_v2_snr20_heart_fix", "B_wide", "heart").mean()),
    "Bwide_heart_20eval_20train": float(per_seed("results_20db_fix", "B_wide", "heart").mean()),
    "D_heart_20eval_40train": float(per_seed("results_v2_snr20_heart_fix", "D", "heart").mean()),
    "D_heart_20eval_20train": float(per_seed("results_20db_fix", "D", "heart").mean()),
}
out["H5_absolute_recovery"]["Bwide_gain_pts"] = (out["H5_absolute_recovery"]["Bwide_heart_20eval_20train"] - out["H5_absolute_recovery"]["Bwide_heart_20eval_40train"]) * 100
out["H5_absolute_recovery"]["D_gain_pts"] = (out["H5_absolute_recovery"]["D_heart_20eval_20train"] - out["H5_absolute_recovery"]["D_heart_20eval_40train"]) * 100

# --- H3 statistic and the 50 dB anchor
d60 = (per_seed("results_v2_snr60_heart_fix", "D", "heart") - per_seed("results_v2_snr60_heart_fix", "B_wide", "heart")) * 100
d50 = (per_seed("results_v2_snr50_heart_fix", "D", "heart") - per_seed("results_v2_snr50_heart_fix", "B_wide", "heart")) * 100
d40 = (per_seed("results_v2_snr40_heart_fix", "D", "heart") - per_seed("results_v2_snr40_heart_fix", "B_wide", "heart")) * 100
d30 = (per_seed("results_v2_snr30_heart_fix", "D", "heart") - per_seed("results_v2_snr30_heart_fix", "B_wide", "heart")) * 100
for name, anchor in (("H3_D20_minus_D60", d60), ("H3_D20_minus_D50", d50)):
    dd = d2040 - anchor; lo, hi = boot_ci(dd)
    out[name] = {"mean_pts": float(dd.mean()), "ci95_pts": [float(lo), float(hi)]}
l60 = (per_seed("results_v2_snr60_heart_fix", "D", "lung") - per_seed("results_v2_snr60_heart_fix", "B_wide", "lung")) * 100
l20 = (per_seed("results_v2_snr20_heart_fix", "D", "lung") - per_seed("results_v2_snr20_heart_fix", "B_wide", "lung")) * 100
dd = l20 - l60; lo, hi = boot_ci(dd)
out["H3_lung_D20_minus_D60"] = {"mean_pts": float(dd.mean()), "ci95_pts": [float(lo), float(hi)]}

# --- seed-level structure and 20 dB robustness
rho, p = spearmanr(d40, d2040)
out["spearman_40_vs_20"] = {"rho": float(rho), "p": float(p)}
out["slope_positive_seeds_40_to_20"] = int(np.sum(d2040 - d40 > 0))
order = np.argsort(-d2040)
out["20dB_drop_top3_mean_pts"] = float(np.delete(d2040, order[:3]).mean())
out["rise_40_to_30_pts"] = float(d30.mean() - d40.mean())
out["high_snr_mean_spread_pts"] = float(max(d60.mean(), d50.mean(), d40.mean()) - min(d60.mean(), d50.mean(), d40.mean()))
out["Bwide_heart_loss_60_to_20_pts"] = float((per_seed("results_v2_snr60_heart_fix", "B_wide", "heart").mean() - per_seed("results_v2_snr20_heart_fix", "B_wide", "heart").mean()) * 100)
out["Bwide_heart_loss_40_to_20_pts"] = float((per_seed("results_v2_snr40_heart_fix", "B_wide", "heart").mean() - per_seed("results_v2_snr20_heart_fix", "B_wide", "heart").mean()) * 100)
out["D_heart_loss_60_to_20_pts"] = float((per_seed("results_v2_snr60_heart_fix", "D", "heart").mean() - per_seed("results_v2_snr20_heart_fix", "D", "heart").mean()) * 100)
out["Bwide_lung_loss_40_to_20_pts"] = float((per_seed("results_v2_snr40_heart_fix", "B_wide", "lung").mean() - per_seed("results_v2_snr20_heart_fix", "B_wide", "lung").mean()) * 100)

# --- relative error reduction at 20 dB, heart minus lung (post hoc, Section 3.4)
def relerr(d_dir, ch):
    a = per_seed(d_dir, "D", ch); b = per_seed(d_dir, "B_wide", ch)
    return (a - b) / (1 - b) * 100
rh = relerr("results_v2_snr20_heart_fix", "heart"); rl = relerr("results_v2_snr20_heart_fix", "lung")
lo, hi = boot_ci(rh - rl)
out["relerr_20dB_heart_minus_lung_pp"] = {"mean": float((rh - rl).mean()), "ci95": [float(lo), float(hi)],
                                          "heart_mean": float(rh.mean()), "lung_mean": float(rl.mean())}
lo, hi = boot_ci(d2040 - l20)
out["raw_20dB_heart_minus_lung_pts"] = {"mean": float((d2040 - l20).mean()), "ci95": [float(lo), float(hi)]}

# --- onset thresholds computed, not typed (FIGURES.md 2026-09-24 rule)
levels = [60, 50, 40, 35, 30, 25, 20]
rel = {}
for lvl in levels:
    r = relerr(f"results_v2_snr{lvl}_heart_fix", "heart"); lo, hi = boot_ci(r)
    rel[lvl] = {"mean": float(r.mean()), "ci95": [float(lo), float(hi)]}
out["relerr_heart_by_level"] = rel
detect = next(l for l in levels if rel[l]["ci95"][0] > 0)
floor_cross = next(l for l in levels if out[f"sweep_{l}dB_heart"]["mean_pts"] > out[f"sweep_{l}dB_heart"]["control_seed_sd_pts"] and out[f"sweep_{l}dB_heart"]["wilcoxon_p"] < 0.05)
out["onset"] = {"first_level_relerr_ci_excludes_zero": detect, "first_level_clearing_H1_form_rule": floor_cross,
                "dz_max_level": max(levels, key=lambda l: out[f"sweep_{l}dB_heart"]["dz"])}

OUT.write_text(json.dumps(out, indent=1))
print(json.dumps(out, indent=1))
