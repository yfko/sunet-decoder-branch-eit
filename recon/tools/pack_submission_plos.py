"""Complete the PLoS One submission package for the RECON tier-3 paper (run AFTER tools/format_convert_plos.py and
tools/make_system_fields_plos.py, which fill the flat manuscript/figure/SI files):

    python3 tools/pack_submission_plos.py submission_PLOS_20261031

Adds  02_Cover_letter/Cover_letter_PLOS.{md,docx}   (letter body only, from RECON_paper/manuscript/25_COVER_LETTER_PLOS.md)
      S1_Data/ + S1_Data.zip                       (S1 Data, Supporting Information; PI 2026-10-31: no Zenodo) per-seed files for every cell, aggregated results, gate and seed-0 diagnostic files,
                                                    the four preregistration states with the hash file, README (every file hashed)
      08_Related_material/Companion_core_paper_SciRep_submission.docx   (the companion manuscript as submitted to Sci Rep 2026-10-15)
      CHECKLIST_author_fields.md                    author-supplied items still open
      MANIFEST.sha256                               SHA-256 of every file in the package
"""
import hashlib, json, re, shutil, subprocess, sys, zipfile, datetime
from pathlib import Path
PKG = Path(sys.argv[1] if len(sys.argv) > 1 else "submission_PLOS_20261031"); M = Path("RECON_paper/manuscript"); R = Path("results_recon")
sha = lambda p: hashlib.sha256(Path(p).read_bytes()).hexdigest()
# ---- cover letter: body between 'Dear' and the ORCID line
cl = (M / "25_COVER_LETTER_PLOS.md").read_text(encoding="utf-8"); body = cl[cl.index("Dear Academic Editor"):]; body = body[:body.index("0000-0003-2986-9984") + len("0000-0003-2986-9984")]
(PKG / "02_Cover_letter").mkdir(exist_ok=True); (PKG / "02_Cover_letter/Cover_letter_PLOS.md").write_text(body + "\n", encoding="utf-8")
subprocess.run(["pandoc", str(PKG / "02_Cover_letter/Cover_letter_PLOS.md"), "-o", str(PKG / "02_Cover_letter/Cover_letter_PLOS.docx"), "--from", "markdown+smart"], check=True)
import docx
from docx.shared import Pt, Cm
_d = docx.Document(PKG / "02_Cover_letter/Cover_letter_PLOS.docx")
for _s in _d.sections: _s.top_margin = _s.bottom_margin = Cm(2.0); _s.left_margin = _s.right_margin = Cm(2.2)
for _p in _d.paragraphs:
    _p.paragraph_format.space_after = Pt(6); _p.paragraph_format.space_before = Pt(0); _p.paragraph_format.line_spacing = 1.0
    for _r in _p.runs: _r.font.size = Pt(10.5); _r.font.name = "Times New Roman"
_d.save(PKG / "02_Cover_letter/Cover_letter_PLOS.docx")   # one page (PLoS: cover letter <= 1 page)
# ---- related material
src = Path("submission_SciRep_20261008/01_Manuscript/Manuscript_SciRep.docx"); (PKG / "08_Related_material").mkdir(exist_ok=True)
shutil.copy(src, PKG / "08_Related_material/Companion_core_paper_SciRep_submission.docx")
# ---- S1 Data: the minimal data set as a Supporting Information zip (PLoS allows SI files < 20 MB; the same files are in the repository release)
Z = PKG / "S1_Data"
if Z.exists(): shutil.rmtree(Z)
(Z / "per_seed").mkdir(parents=True); (Z / "preregistration").mkdir()
cells = sorted(d.name for d in R.iterdir() if d.is_dir() and (d / "per_seed.csv").exists()); assert len(cells) == 39, len(cells)
for c in cells:
    for f in ("per_seed.csv", "summary.json"):
        if (R / c / f).exists(): shutil.copy(R / c / f, Z / "per_seed" / f"{c}__{f}")
for f in ("recon_results.json", "recon_delta_ci.json", "scale_check.json", "pilot_checks.json", "loro_gate.json", "mixed_ps_gate.json",
          "shift_inputs.json", "loro_preds_seed0.json", "mixed_ps_preds_seed0.json", "loro_mask_check_seed0.json",
          "run_meta_loro_bp.json", "run_meta_loro_gn.json", "run_meta_loro_greit.json", "run_meta_mixed_ps.json"):
    shutil.copy(R / f, Z / f)
states = [("PREREGISTRATION_RECON.pre-dev20261003.md", "4b4c7a6d"), ("PREREGISTRATION_RECON.pre-add11_20261003.md", "3fdc703d"),
          ("PREREGISTRATION_RECON.pre-add12_20261011.md", "0060eedf"), ("PREREGISTRATION_RECON.md", "9589b298")]
for f, pre in states:
    assert sha(f).startswith(pre), f; shutil.copy(f, Z / "preregistration" / f)
shutil.copy("PREREGISTRATION_RECON.sha256", Z / "preregistration/PREREGISTRATION_RECON.sha256")
for f in ("S3_Table.csv", "S3_Table_derived.csv", "S3_Table.xlsx"): shutil.copy(PKG / f, Z / f)
readme = ["# S1 Data — minimal data set of *Does a decoder branch for the cardiac component of lung EIT survive a change of reconstructor?* (RECON tier-3 study)", "",
          f"Assembled {datetime.date.today()} by tools/pack_submission_plos.py from the project's result files; nothing typed by hand.", "",
          "- per_seed/<cell>__per_seed.csv: per-seed, per-channel metrics (Dice, IoU, sensitivity, specificity, MAE, ASSD, HD95) on the test split for both arms (B_wide, D), seeds 0-29; <cell> = <training row>__<evaluation reconstructor>[_e1|_ownaffine]; loro_<H>__<Y> = trained without H, evaluated on Y; mixedps = pooled with per-source affines.",
          "- recon_results.json: every registered and addendum statistic (tools/recon_results.py); recon_delta_ci.json: bootstrap intervals, MDE80, training records; scale_check.json: training-split amplitude statistics.",
          "- pilot_checks.json, loro_gate.json, mixed_ps_gate.json: the pre-read gates; shift_inputs.json, loro_preds_seed0.json, mixed_ps_preds_seed0.json, loro_mask_check_seed0.json: seed-0 diagnostics; run_meta_*.json: dataset and preregistration hashes recorded by the training script.",
          "- preregistration/: the four hashed states of PREREGISTRATION_RECON.md (4b4c7a6d registered 2026-09-26; 3fdc703d deviation record 2026-10-03; 0060eedf first addendum 2026-10-03; 9589b298 second addendum 2026-10-11) and the hash file.",
          "- S3_Table.*: the per-seed table as submitted (S3 Table of the manuscript) with the derived per-seed quantities.",
          "", "This archive is S1 Data of the article. The same files, with the data-generation, training, scoring and figure code, are in the project repository github.com/yfko/sunet-decoder-branch-eit under the tagged release named in the manuscript (recon/). Model checkpoints are available from the corresponding author.", "", "## SHA-256", ""]
files = sorted(p for p in Z.rglob("*") if p.is_file())
readme += [f"{sha(p)}  {p.relative_to(Z)}" for p in files]
(Z / "README.md").write_text("\n".join(readme) + "\n", encoding="utf-8")
with zipfile.ZipFile(PKG / "S1_Data.zip", "w", zipfile.ZIP_DEFLATED) as z:
    for p in sorted(Z.rglob("*")):
        if p.is_file(): z.write(p, arcname=str(p.relative_to(PKG)))
# ---- author-field checklist
md = (PKG / "Manuscript.md").read_text(encoding="utf-8"); gaps = sorted(set(re.findall(r"\[MATERIAL GAP:[^\]]*\]", md)))
chk = ["# Author-supplied fields still open (fill on submission day)", ""] + [f"- [ ] {g}" for g in gaps] + [
       "- [ ] Suggested Academic Editors in the cover letter and the system (PI)", "- [ ] CRediT roles confirmed for this paper (PI)",
       "- [ ] Upload S1_Data.zip as Supporting Information file S1 Data (the minimal data set; no Zenodo deposit, PI decision 2026-10-31)",
       "- [ ] GitHub: tag the release named in the manuscript after copying the RECON tools/results (see NOTES) and paste the tag",
       "- [ ] Companion preprint DOI if posted before submission (then cite it and revise the Related manuscript statement)",
       "- [ ] Wang 2024 (IEEE Trans Instrum Meas 73) article number, if the PI can read it from IEEE Xplore (pages 1-16 kept otherwise)"]
(PKG / "CHECKLIST_author_fields.md").write_text("\n".join(chk) + "\n", encoding="utf-8")
# ---- manifest
lines = [f"{sha(p)}  {p.relative_to(PKG)}" for p in sorted(PKG.rglob("*")) if p.is_file() and p.name != "MANIFEST.sha256"]
(PKG / "MANIFEST.sha256").write_text("\n".join(lines) + "\n")
print(f"package complete: {len(lines)} files; S1 Data {len(files)} files, zip {(PKG / 'S1_Data.zip').stat().st_size // 1024} KB; cells {len(cells)}; open fields {len(gaps)}")
