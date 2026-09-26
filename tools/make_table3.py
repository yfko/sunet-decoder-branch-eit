"""Table 3 for the core paper: the registered addendum contrast (D vs B_wide trained and
evaluated at 20 dB) beside the evaluation-only contrast for 40 dB-trained models and the
registered 40 dB primary. Every cell comes from results/manuscript_numbers.json
(tools/verify_manuscript_numbers.py) and results/geom_bootstrap.json -- never typed.

    python3 tools/make_table3.py
"""
import json
from pathlib import Path

N = json.load(open("results/manuscript_numbers.json"))
G = json.load(open("results/geom_bootstrap.json"))["results"]

rows = [
    ("40 dB", "40 dB", "H1 (registered primary)", N["40dB_D_minus_Bwide_heart"], G["results_v2_fix"]),
    ("40 dB", "20 dB", "H3 low end (evaluation only)", N["sweep_20dB_heart"], G["results_v2_snr20_heart_fix"]),
    ("20 dB", "20 dB", "H5 (registered addendum)", N["H5_20train_20eval_heart"], G["results_20db_fix"]),
]

def ci(v): return f"[{v[0]:+.3f}, {v[1]:+.3f}]"
def rule(c):
    return "confirmed" if (c["mean_pts"] > c["control_seed_sd_pts"] and c["wilcoxon_p"] < 0.05) else "falsified"
def p(c): return "<0.0001" if c["wilcoxon_p"] < 1e-4 else f"{c['wilcoxon_p']:.4f}"

hdr = ["Trained", "Evaluated", "Contrast", "B_wide heart DSC (mean ± SD)", "D heart DSC (mean ± SD)",
       "D − B_wide, pts [95% CI, seeds]", "[95% CI, geometries]", "dz", "Wilcoxon W", "p", "Floor (B_wide seed SD), pts", "Seeds D > B_wide", "Rule"]
md = ["| " + " | ".join(hdr) + " |", "|" + "---|" * len(hdr)]
tex = []
for tr, ev, name, c, g in rows:
    verdict = rule(c) if name.startswith(("H1", "H5")) else "— (no rule)"
    cells = [tr, ev, name, f"{c['B_wide_mean']:.4f} ± {c['B_wide_sd']:.4f}", f"{c['D_mean']:.4f} ± {c['D_sd']:.4f}",
             f"{c['mean_pts']:+.3f} {ci(c['ci95_pts'])}", ci(g["geometry_ci"]), f"{c['dz']:+.2f}",
             f"{c['wilcoxon_W']:.0f}", p(c), f"{c['control_seed_sd_pts']:.3f}", f"{c['wins']}/{c['n']}", verdict]
    md.append("| " + " | ".join(cells) + " |")
    tex.append(" & ".join(x.replace("±", r"$\pm$").replace("−", "$-$").replace("<", "$<$").replace("_", r"\_") for x in cells) + r" \\")

gap = N["H5_gap_20in20_minus_20in40"]; rec = N["H5_absolute_recovery"]
note = (f"Registered H5 rule: Δ_20|20 must exceed B_wide's seed-to-seed SD at 20|20 AND Wilcoxon p < 0.05. "
        f"Secondary, reported not tested: Δ_20|20 − Δ_20|40 = {gap['mean_pts']:+.3f} pts {ci(gap['ci95_pts'])} (seeds resampled in pairs), "
        f"a {gap['shrink_factor']:.1f}-fold shrinkage. Retraining at 20 dB raised B_wide's heart DSC by {rec['Bwide_gain_pts']:.1f} pts and D's by {rec['D_gain_pts']:.1f} pts. "
        f"Lung channel at 20|20: Δ = {N['H5_20train_20eval_lung']['mean_pts']:+.3f} pts {ci(N['H5_20train_20eval_lung']['ci95_pts'])}, p = {N['H5_20train_20eval_lung']['wilcoxon_p']:.4f}. "
        f"Geometry-level CIs resample the 360 test frames (100,000 resamples); seed-level CIs resample the 58 seeds.")
Path("results/tables/table3_retrained_20db.md").write_text("\n".join(md) + "\n\n" + note + "\n")
Path("results/tables/table3_retrained_20db.tex").write_text(
    "\\begin{table*}[t]\n\\caption{The registered addendum contrast (D vs B\\_wide trained and evaluated at 20~dB) beside the evaluation-only 20~dB contrast for 40~dB-trained models and the registered 40~dB primary. Heart channel, 58 seeds per arm.}\n"
    "\\label{tab:retrained}\n\\centering\\small\n\\begin{tabular}{" + "l" * len(hdr) + "}\n\\hline\n" + " & ".join(h.replace("_", r"\_").replace("±", r"$\pm$").replace("−", "$-$") for h in hdr) + r" \\" + "\n\\hline\n"
    + "\n".join(tex) + "\n\\hline\n\\end{tabular}\n\\end{table*}\n")
print("\n".join(md)); print(); print(note)
