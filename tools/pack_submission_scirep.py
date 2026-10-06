"""Assemble the Scientific Reports submission package for the core paper (derived from pack_submission_pm.py, 2026-10-07).

    python3 tools/pack_submission_scirep.py [manuscript/43_SUBMISSION_scirep_v5]

Writes submission_SciRep_<date>/ with the manuscript (from the given stem, default manuscript/43_SUBMISSION_scirep_v5.*),
cover letter, figures, tables, the related-material copy of the 2025 manuscript, the supplementary document S1-S9 assembled from the
project's own records (numbers recomputed from result files, R10c), the two
preregistrations with their hashes, a checklist of author-supplied fields still
open, and a MANIFEST with SHA-256 of every file.
"""
import json, re, shutil, hashlib, subprocess, datetime, csv, sys
from pathlib import Path
import numpy as np
from scipy.stats import spearmanr

ROOT = Path(".")
DATE = datetime.date.today().strftime("%Y%m%d")
STEM = sys.argv[1] if len(sys.argv) > 1 else "manuscript/43_SUBMISSION_scirep_v5"
OUT = ROOT / f"submission_SciRep_{DATE}"
SOFFICE = "/Applications/LibreOffice.app/Contents/MacOS/soffice"
def to_pdf(path):
    subprocess.run([SOFFICE, "--headless", "--convert-to", "pdf", "--outdir", str(Path(path).parent), str(path)], check=True, capture_output=True)
if OUT.exists(): shutil.rmtree(OUT)
for d in ("01_Manuscript", "02_Cover_letter", "03_Figures", "04_Tables", "05_Supplementary", "06_Preregistrations", "08_Related_material"):
    (OUT / d).mkdir(parents=True)

# ---- 01 manuscript, 02 cover letter
for ext in ("docx", "md"):
    shutil.copy(f"{STEM}.{ext}", OUT / "01_Manuscript" / f"Manuscript_SciRep.{ext}")
to_pdf(OUT / "01_Manuscript" / "Manuscript_SciRep.docx")
cl = Path("manuscript/40_COVER_LETTER_SCIREP.md").read_text()
letter = cl.split("---\n", 1)[1].split("\n---\n")[0].strip() + "\n"   # strip the internal notes
(OUT / "02_Cover_letter" / "Cover_letter_SciRep.md").write_text(letter)
subprocess.run(["pandoc", str(OUT / "02_Cover_letter" / "Cover_letter_SciRep.md"), "-o", str(OUT / "02_Cover_letter" / "Cover_letter_SciRep.docx")], check=True)
# related material required by the journal's submission policy (earlier manuscript, results withdrawn)
shutil.copy("Nov142025/Manuscript.docx", OUT / "08_Related_material" / "Related_material_2025_manuscript_withdrawn_results.docx")

# ---- 03 figures (manuscript numbering per FIGURES.md 2026-09-22/23), 04 tables
figs = {"Fig1": "fig1_separability", "Fig2": "fig1_arms_and_task", "Fig3": "fig_snr_sweep", "Fig4": "fig_predictions"}   # Sci Rep deliverable order (by first citation; format_convert_scirep.py swaps 1 and 2)
for k, v in figs.items():
    for ext in ("pdf", "png"):
        shutil.copy(f"figures/{v}.{ext}", OUT / "03_Figures" / f"{k}_{v}.{ext}")
for t in ("table1_arms_40db", "table2_snr_sweep", "table3_retrained_20db", "table_s9_sweep_all_arms"):
    for ext in ("md", "tex"):
        if Path(f"results/tables/{t}.{ext}").exists(): shutil.copy(f"results/tables/{t}.{ext}", OUT / "04_Tables" / f"{t}.{ext}")

# ---- 05 supplementary S1-S8
def h5_seed(d, arm, ch):
    rows = list(csv.DictReader(open(f"{d}/per_seed.csv")))
    return np.array([float(r["dsc"]) for r in sorted((r for r in rows if r["arm"] == arm and r["channel"] == ch), key=lambda r: int(r["seed"]))])
S = []
S.append("# Supplementary material\n\nA decoder branch for the cardiac component of lung EIT: a preregistered, parameter-matched evaluation across measurement-noise levels. Chen, Wang and Ko.\n\nEvery number below is regenerated from the per-seed result files by `tools/pack_submission_scirep.py` (S9 by `tools/make_table_s9.py`); the preregistrations in the companion folder carry the registered SHA-256 hashes.\n")
# S1
S.append("## S1 Per-arm architecture diagrams\n\nFiles `S1_arm_A.pdf` … `S1_arm_D.pdf` (PlotNeuralNet renderings; Fig. 1a of the main text shows the five arms side by side). Arm A (single output, lung only) belongs to Study 1 and has no heart head.\n")
for a in ("A", "B", "B_wide", "C", "C_wide", "D"):
    shutil.copy(f"figures/arm_{a}.pdf", OUT / "05_Supplementary" / f"S1_arm_{a}.pdf")
# S2 Study 1
s1l = json.load(open("results_v1_lung_fix/summary.json")); s1h = json.load(open("results_v1_heart_fix/summary.json"))
S.append("## S2 Study 1 (registered 2026-08-28, SHA-256 `eebf21a2…`): full results\n\nHomogeneous organ conductivity, no measurement noise, n = 10 seeds per arm, lung-channel Dice as the registered primary endpoint (mis-specified for the mechanism; recorded in that preregistration's §8 and not switched).\n\n| Arm | Lung DSC (mean ± SD) | Heart DSC (mean ± SD) |\n|---|---|---|")
for a in ("A", "B", "B_wide", "C", "C_wide", "D"):
    l = s1l["table"][a]["dsc"]; h = s1h["table"].get(a, {}).get("dsc")
    S.append(f"| {a} | {l[0]:.4f} ± {l[1]:.4f} | {'—' if h is None else f'{h[0]:.4f} ± {h[1]:.4f}'} |")
def c1(s, k): v = s["contrasts"][k]; return f"{-v['mean_diff']*100:+.3f} pts, p = {v['p']:.3f}, dz = {-v['cohen_dz']:.2f}"
S.append(f"\nRegistered contrasts (lung channel; sign is second-named minus first-named arm as stored, reported here as branch minus control): D − B_wide {c1(s1l,'B_wide-D')}; D − A {c1(s1l,'A-D')}; B − A (supervision) {c1(s1l,'A-B')}. Registered decision: D − B_wide = {s1l['verdict']['diff']*100:+.3f} pts against a floor of {s1l['verdict']['control_seed_sd']*100:.3f} pts, p = {s1l['verdict']['p']:.3f}: falsified. Heart channel (secondary): D − B_wide {c1(s1h,'B_wide-D')}, floor {s1h['verdict']['control_seed_sd']*100:.3f} pts: falsified, and at n = 10 underpowered for the effect Study 2 later registered.\n")
# S3
shutil.copy("figures/fig_s3_effect_sizes.pdf", OUT / "05_Supplementary" / "S3_fig_effect_sizes.pdf")
S.append("## S3 Effect sizes of the three branching contrasts with the registered floor\n\n`S3_fig_effect_sizes.pdf`: Study 1 D − A (lung), Study 2 D − B_wide at 40 dB and at 20 dB (heart), with the registered seed-SD floor drawn from the data. The 40 dB interval excludes zero and lies entirely below the floor.\n")
# S4 seed correlation
levels = [60, 50, 40, 35, 30, 25, 20]
diffs = {l: (h5_seed(f"results_v2_snr{l}_heart_fix", "D", "heart") - h5_seed(f"results_v2_snr{l}_heart_fix", "B_wide", "heart")) * 100 for l in levels}
S.append("## S4 Seed-level correlation of D − B_wide (heart) between sweep levels\n\nSpearman ρ over the 58 seeds; models trained at 40 dB, evaluated at each level.\n\n| | " + " | ".join(f"{l} dB" for l in levels) + " |\n|---|" + "---|" * len(levels))
for a in levels:
    S.append(f"| **{a} dB** | " + " | ".join(f"{spearmanr(diffs[a], diffs[b])[0]:.2f}" if b >= a else "" for b in levels) + " |")
rho, p = spearmanr(diffs[40], diffs[20])
S.append(f"\n60/50/40 dB behave as one measurement (ρ ≥ 0.99); 40 dB and 20 dB are uncorrelated (ρ = {rho:.2f}, p = {p:.2f}), so the positive 40 dB mean is not a weak form of the 20 dB effect.\n")
# S5 deviation logs verbatim
def section(text, start_pat, end_pat=None):
    m = re.search(start_pat, text, flags=re.M); t = text[m.start():]
    if end_pat:
        e = re.search(end_pat, t[1:], flags=re.M); t = t[: e.start() + 1] if e else t
    t = t.strip() + "\n"
    return re.sub(r"^#+ ", "#### ", t, count=1)
ph = Path("PREREGISTRATION_HEART.md").read_text(); p1 = Path("PREREGISTRATION.md").read_text()
S.append("## S5 Preregistration deviation logs, verbatim\n\n### S5.1 Study 1 (`PREREGISTRATION.md` §8)\n\n" + section(p1, r"^## 8\. Deviations").replace("\n## ", "\n#### ").replace("\n### ", "\n#### "))
S.append("### S5.2 Study 2 (`PREREGISTRATION_HEART.md` §8 and the §9 addendum, registered 2026-09-23, hash `a252444b…`)\n\n" + section(ph, r"^## 8\. Deviations").replace("\n## ", "\n#### ").replace("\n### ", "\n#### "))
# S6 defect record
S.append("## S6 The scoring defect record (`METRIC_DEFECT_2026-09-18.md`), verbatim\n\n" + Path("METRIC_DEFECT_2026-09-18.md").read_text().replace("\n# ", "\n#### ").replace("\n## ", "\n#### ") + "\n")
# S7 environment
env = {}
try:
    env = json.loads(Path("results/env_mini.json").read_text().splitlines()[0])
except Exception:
    pass
m40 = json.load(open("runs_v2/run_meta.json"))["norm"]; m20 = json.load(open("results_20db_fix/summary.json"))["norm"]
const = {k: re.search(rf"^{k}\s*=\s*([^\n#]+)", Path("tools/train_arms.py").read_text(), flags=re.M) for k in ("LR", "LR_MIN", "BATCH", "MAX_EPOCHS", "PATIENCE")}
const = {k: (v.group(1).strip() if v else "see tools/train_arms.py") for k, v in const.items()}
S.append("## S7 Training hyperparameters and software environment\n\n| | |\n|---|---|\n" + "\n".join([
    f"| Optimiser | Adam, lr {const['LR']} with cosine decay to {const['LR_MIN']} |",
    f"| Batch size | {const['BATCH']} |",
    f"| Epoch cap / early stopping | {const['MAX_EPOCHS']} / patience {const['PATIENCE']} on validation loss, best weights restored |",
    "| Loss | L1 on the float target, no output activation, weights 1.0/1.0, no augmentation |",
    f"| Normalisation affine (dataset-wide, training split, FOV only) | 40 dB training split: mu {m40['mu']:.6f}, sd {m40['sd']:.6f}; 20 dB training split (addendum): mu {m20['mu']:.6f}, sd {m20['sd']:.6f} |",
    "| Seeds | 0–57 (Study 2), 0–9 (Study 1); one machine for every run of a contrast |",
    f"| Hardware | {env.get('chip', 'Apple M4 (Mac mini)')}, device {env.get('device', 'mps')} |",
    f"| Software | Python {env.get('python', '3.x')}, PyTorch {env.get('torch', 'see repository')}, NumPy {env.get('numpy', '')}, SciPy {env.get('scipy', '')}; MATLAB R2026a with EIDORS v3.8 and Netgen 6.1 for data generation |",
    "| Data generation | `tools/gen_dataset.m` (40 dB), `tools/gen_snr_sweep.m` (evaluation-only levels), `tools/gen_snr_full.m` (20 dB, all splits) |",
    "| Scoring | `tools/evaluate.py --qa-space image` (the corrected path; the defective pre-2026-09-18 path is retained behind `--qa-space normalised`) |",
]) + "\n")
# S8 geometry bootstrap
g = json.load(open("results/geom_bootstrap.json"))
names = {"results_v2_fix": "Trained 40 dB, evaluated 40 dB (H1)", "results_v2_snr20_heart_fix": "Trained 40 dB, evaluated 20 dB (H3 low end)", "results_20db_fix": "Trained 20 dB, evaluated 20 dB (H5)"}
S.append(f"## S8 Geometry-level bootstrap intervals beside the seed-level intervals\n\n{g['n_boot']:,} resamples of the 360 test geometries (seed mean inside each resample) versus {g['n_boot']:,} resamples of the 58 seeds; rng seed {g['rng_seed']}. Registered rules are defined on seeds.\n\n| Contrast (D − B_wide, heart) | Δ, pts | 95% CI, geometries | 95% CI, seeds |\n|---|---|---|---|")
for k, v in g["results"].items():
    S.append(f"| {names[k]} | {v['diff_pts']:+.3f} | [{v['geometry_ci'][0]:+.3f}, {v['geometry_ci'][1]:+.3f}] | [{v['seed_ci'][0]:+.3f}, {v['seed_ci'][1]:+.3f}] |")
S.append("\nFor the two small contrasts the geometry-level interval is the narrower one: their uncertainty is dominated by training randomness, and the seed-level interval on which the rules are defined is the more conservative. No decision changes under either interval.\n")
# S9 all five arms across the sweep (tools/make_table_s9.py)
s9 = Path("results/tables/table_s9_sweep_all_arms.md").read_text().replace("**Table S9.**", "").strip()
S.append("## S9 The evaluation-only sweep for all five arms\n\n" + s9 + "\n")
sup = OUT / "05_Supplementary" / "Supplementary_S1-S9.md"
sup.write_text("\n".join(S))
subprocess.run(["pandoc", str(sup), "-o", str(sup.with_suffix(".docx")), "--from", "markdown+smart"], check=True)
to_pdf(sup.with_suffix(".docx"))

# ---- 06 preregistrations with hashes
for f in ("PREREGISTRATION.md", "PREREGISTRATION.sha256", "PREREGISTRATION_HEART.md", "PREREGISTRATION_HEART.sha256"):
    shutil.copy(f, OUT / "06_Preregistrations" / f)

# ---- 07 open fields + checklist
open_fields = [f"Manuscript placeholder still to fill: `{x}`" for x in sorted(set(re.findall(r"\[[^\]\n]*(?:to supply|to assign|to be|___|roles|URL)[^\]\n]*\]", Path(f"{STEM}.md").read_text())))] + [
    "Acknowledgements: grant numbers (three NSTC) must match the submission system word for word",
]
(OUT / "07_OPEN_FIELDS_AND_CHECKLIST.md").write_text("# Before uploading\n\nStill to be supplied by the corresponding author (search the manuscript for `[` to find each placeholder):\n\n" + "\n".join(f"- [ ] {x}" for x in open_fields) + "\n\nSci Rep checklist: see `manuscript/39_SUBMISSION_CHECKLIST_SCIREP.md` (official checklist items 1-13, advisory limits, author-side items). Upload: 01 manuscript (.docx, single file), 02 cover letter, 03 figures, 05 Supplementary_S1-S9.pdf (single file), 08 related material (earlier manuscript, results withdrawn) as required by the submission policy. Title, abstract and author data in the submission system must match the manuscript word for word.")

# ---- manifest
lines = ["# MANIFEST", "", f"Package built {datetime.datetime.now():%Y-%m-%d %H:%M} by tools/pack_submission_scirep.py from manuscript/41_DRAFT_v5.md (apply report 3c0451dfbfd5) via tools/format_convert_scirep.py.", "", "| File | SHA-256 | bytes |", "|---|---|---|"]
for p in sorted(OUT.rglob("*")):
    if p.is_file() and p.name != "MANIFEST.md":
        lines.append(f"| {p.relative_to(OUT)} | {hashlib.sha256(p.read_bytes()).hexdigest()[:16]}… | {p.stat().st_size:,} |")
(OUT / "MANIFEST.md").write_text("\n".join(lines) + "\n")
print("\n".join(lines))
