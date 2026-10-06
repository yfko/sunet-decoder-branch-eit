"""Tables 1 and 2 for the core paper, generated from per_seed.csv -- never typed.

    python3 tools/make_tables.py

Table 1: the five arms at the registered 40 dB (results_v2_fix), heart and lung
         DSC, each arm against B_wide (the capacity-matched control), with the
         registered H1 rule's two conditions shown as numbers.
Table 2: the registered SNR sweep (results_v2_snr{60..20}_heart_fix), D - B_wide
         per level in DSC points and as a fraction of B_wide's own error
         (results_v2_rel_err_sweep, tools/rel_err_sweep.py), both channels.

Outputs Markdown and LaTeX (booktabs) to results/tables/. Every cell is computed
here from the CSVs; MANUSCRIPT_RULES R10c requires the manuscript's numbers to
be traceable to output files, and this file is that trace.

Statistics match tools/evaluate.py: Wilcoxon signed-rank (scipy) on the paired
seeds, Cohen's dz = mean/SD of the paired differences, 95% percentile bootstrap
over seeds (figstyle.boot_ci: 100,000 resamples, rng seed 20260904).
"""
import sys
sys.path.insert(0, "tools")

import csv
import json
from pathlib import Path

import numpy as np
from scipy.stats import wilcoxon

from figstyle import ARMS, PARAMS, boot_ci, per_seed

OUT = Path("results/tables")
OUT.mkdir(parents=True, exist_ok=True)
LV = [60, 50, 40, 35, 30, 25, 20]   # 35/25 added 2026-09-24 per PREREGISTRATION_HEART.md section 9.3 (descriptive)
DECODER = {"B": "1, two heads", "B_wide": "1, widened ×1.5312",
           "C": "2, split at last block", "C_wide": "2, split at last block, widened",
           "D": "2, split at bottleneck"}


def contrast(t: np.ndarray, c: np.ndarray) -> dict:
    d = (t - c) * 100                       # DSC points
    lo, hi = boot_ci(d)
    p = float(wilcoxon(t, c).pvalue) if not np.allclose(d, 0) else 1.0
    return dict(diff=float(d.mean()), lo=lo, hi=hi, p=p,
                dz=float(d.mean() / d.std(ddof=1)), wins=int((d > 0).sum()), n=len(d))


# ---------------------------------------------------------------- Table 1
rows1 = []
ctrl = {ch: per_seed("results_v2_fix", "B_wide", ch) for ch in ("heart", "lung")}
floor_pts = float(ctrl["heart"].std(ddof=1) * 100)   # the registered H1 floor
for arm in ARMS:
    r = {"arm": arm, "decoder": DECODER[arm], "params": PARAMS[arm]}
    for ch in ("heart", "lung"):
        v = per_seed("results_v2_fix", arm, ch)
        r[f"{ch}_mean"], r[f"{ch}_sd"] = float(v.mean()), float(v.std(ddof=1))
        r[f"{ch}_vs"] = contrast(v, ctrl[ch]) if arm != "B_wide" else None
    rows1.append(r)
dB = contrast(per_seed("results_v2_fix", "D", "heart"), per_seed("results_v2_fix", "B", "heart"))
dBw = next(r for r in rows1 if r["arm"] == "D")["heart_vs"]


def ci(c, pts=True):
    return f"{c['diff']:+.3f} [{c['lo']:+.3f}, {c['hi']:+.3f}]" if c else "—  (control)"


md1 = ["| Arm | Decoder | Parameters | Heart DSC (mean ± SD) | Heart Δ vs B_wide, pts [95% CI] | Wilcoxon p | dz | Lung DSC (mean ± SD) | Lung Δ vs B_wide, pts [95% CI] |",
       "|---|---|---|---|---|---|---|---|---|"]
tex1 = [r"\begin{table*}[t]", r"\centering",
        r"\caption{Five arms at the registered 40~dB (58 seeds per arm, test split). $\Delta$ is each arm minus B\_wide, the capacity-matched control, in DSC percentage points with 95\% percentile bootstrap CIs over seeds; $p$ is the Wilcoxon signed-rank test over paired seeds; $d_z$ is Cohen's $d_z$.}",
        r"\label{tab:arms40}", r"\begin{tabular}{llrcccccc}", r"\toprule",
        r"Arm & Decoder & Parameters & Heart DSC & Heart $\Delta$ [95\% CI] & $p$ & $d_z$ & Lung DSC & Lung $\Delta$ [95\% CI] \\", r"\midrule"]
for r in rows1:
    h, l = r["heart_vs"], r["lung_vs"]
    md1.append(f"| {r['arm']} | {r['decoder']} | {r['params']:,} | {r['heart_mean']:.4f} ± {r['heart_sd']:.4f} | {ci(h)} | "
               f"{h['p']:.3f} | {h['dz']:+.2f} | {r['lung_mean']:.4f} ± {r['lung_sd']:.4f} | {ci(l)} |"
               if h else
               f"| {r['arm']} | {r['decoder']} | {r['params']:,} | {r['heart_mean']:.4f} ± {r['heart_sd']:.4f} | — (control) | — | — | {r['lung_mean']:.4f} ± {r['lung_sd']:.4f} | — (control) |")
    PM = r"$\pm$"
    arm_tex, dec_tex = r["arm"].replace("_", r"\_"), r["decoder"].replace("×", r"$\times$")
    hcell = (f"{h['diff']:+.3f} [{h['lo']:+.3f}, {h['hi']:+.3f}] & {h['p']:.3f} & {h['dz']:+.2f}"
             if h else "--- (control) & --- & ---")
    lcell = (f"{l['diff']:+.3f} [{l['lo']:+.3f}, {l['hi']:+.3f}]" if l else "--- (control)")
    tex1.append(f"{arm_tex} & {dec_tex} & {r['params']:,} & {r['heart_mean']:.4f} {PM} {r['heart_sd']:.4f} & {hcell}"
                f" & {r['lung_mean']:.4f} {PM} {r['lung_sd']:.4f} & {lcell} " + r"\\")
note1 = (f"Registered H1 rule: D − B_wide (heart) must exceed B_wide's seed-to-seed SD, {floor_pts:.3f} pts, "
         f"AND Wilcoxon p < 0.05. Observed {dBw['diff']:+.3f} pts, p = {dBw['p']:.3f}; D wins on {dBw['wins']}/{dBw['n']} seeds. "
         f"D − B (heart): {dB['diff']:+.3f} [{dB['lo']:+.3f}, {dB['hi']:+.3f}], p = {dB['p']:.3f}.")
md1 += ["", note1]
tex1 += [r"\bottomrule", r"\end{tabular}", r"\begin{tablenotes}\small\item " + note1.replace("_", r"\_").replace("−", "$-$") + r"\end{tablenotes}", r"\end{table*}"]
(OUT / "table1_arms_40db.md").write_text("\n".join(md1) + "\n")
(OUT / "table1_arms_40db.tex").write_text("\n".join(tex1) + "\n")

# ---------------------------------------------------------------- Table 2
rel = {(r["channel"], int(r["snr_db"])): r for r in csv.DictReader(open("results_v2_rel_err_sweep/rel_err_sweep.csv"))}
rows2 = []
for ch in ("heart", "lung"):
    for L in LV:
        d = f"results_v2_snr{L}_heart_fix"
        t, c = per_seed(d, "D", ch), per_seed(d, "B_wide", ch)
        k = contrast(t, c); rr = rel[(ch, L)]
        rows2.append(dict(channel=ch, snr=L, ctrl=float(c.mean()), treat=float(t.mean()), **k,
                          rel=float(rr["rel_err_reduction_pct"]), rlo=float(rr["rel_ci_lo"]), rhi=float(rr["rel_ci_hi"])))
h20 = per_seed("results_v2_snr20_heart_fix", "D", "heart") - per_seed("results_v2_snr20_heart_fix", "B_wide", "heart")
h60 = per_seed("results_v2_snr60_heart_fix", "D", "heart") - per_seed("results_v2_snr60_heart_fix", "B_wide", "heart")
dod = (h20 - h60) * 100; dlo, dhi = boot_ci(dod)

md2 = ["| Channel | SNR (dB) | B_wide DSC | D DSC | D − B_wide, pts [95% CI] | dz | Wilcoxon p | Relative error reduction, % [95% CI] | Seeds D > B_wide |",
       "|---|---|---|---|---|---|---|---|---|"]
tex2 = [r"\begin{table*}[t]", r"\centering",
        r"\caption{The registered SNR sweep: models trained once at 40~dB and evaluated at seven measurement-noise levels (58 seeds); 35 and 25~dB were added by the registered addendum and are descriptive. Relative error reduction is each seed's $(\mathrm{D}-\mathrm{B\_wide})/(1-\mathrm{B\_wide})$, i.e.\ the gain as a fraction of the control arm's own remaining error, which removes the DSC ceiling; it was not pre-specified and is descriptive.}",
        r"\label{tab:sweep}", r"\begin{tabular}{llcccccccc}", r"\toprule",
        r"Channel & SNR (dB) & B\_wide DSC & D DSC & D $-$ B\_wide, pts [95\% CI] & $d_z$ & $p$ & Rel.\ error reduction, \% [95\% CI] & Seeds D $>$ B\_wide \\", r"\midrule"]
for r in rows2:
    md2.append(f"| {r['channel']} | {r['snr']} | {r['ctrl']:.4f} | {r['treat']:.4f} | {r['diff']:+.3f} [{r['lo']:+.3f}, {r['hi']:+.3f}] | "
               f"{r['dz']:+.2f} | {r['p']:.4f} | {r['rel']:+.2f} [{r['rlo']:+.2f}, {r['rhi']:+.2f}] | {r['wins']}/{r['n']} |")
    tex2.append(f"{r['channel']} & {r['snr']} & {r['ctrl']:.4f} & {r['treat']:.4f} & {r['diff']:+.3f} [{r['lo']:+.3f}, {r['hi']:+.3f}] & "
                f"{r['dz']:+.2f} & {r['p']:.4f} & {r['rel']:+.2f} [{r['rlo']:+.2f}, {r['rhi']:+.2f}] & {r['wins']}/{r['n']} \\\\")
    if r["snr"] == 20 and r["channel"] == "heart":
        tex2.append(r"\midrule")
note2 = (f"Registered H3 statistic (heart): D(20 dB) − D(60 dB) = {dod.mean():+.3f} pts, 95% CI [{dlo:+.3f}, {dhi:+.3f}]. "
         "Lung relative values at high SNR divide by a control error of under 0.7 pts and are not interpretable as harm; all three CIs contain zero.")
md2 += ["", note2]
tex2 += [r"\bottomrule", r"\end{tabular}", r"\begin{tablenotes}\small\item " + note2.replace("−", "$-$") + r"\end{tablenotes}", r"\end{table*}"]
(OUT / "table2_snr_sweep.md").write_text("\n".join(md2) + "\n")
(OUT / "table2_snr_sweep.tex").write_text("\n".join(tex2) + "\n")

json.dump(dict(table1=rows1, table1_notes=dict(floor_pts=floor_pts, D_minus_B=dB, D_minus_Bwide=dBw),
               table2=rows2, h3=dict(dod=float(dod.mean()), lo=dlo, hi=dhi),
               boot="figstyle.boot_ci 100000 resamples seed 20260904", test="scipy wilcoxon two-sided"),
          open(OUT / "tables.json", "w"), indent=2)
print("\n".join(md1)); print(); print("\n".join(md2))
print(f"\nwrote {OUT}/table1_arms_40db.{{md,tex}}, table2_snr_sweep.{{md,tex}}, tables.json")
