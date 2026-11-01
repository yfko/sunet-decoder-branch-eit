"""Stage the RECON tier-3 study into the public repository working tree (github.com/yfko/sunet-decoder-branch-eit, local
~/work/sunet-decoder-branch-eit) under recon/, so the PI can review, commit, push and tag it (the assistant never commits).

    python3 tools/sync_repo_recon.py            # copies, writes recon/README.md and COMMIT_MSG_repo_recon_<date>.txt, prints the diff summary

Copied: RECON code (tools/*recon*, gen_recon_full.m, eval/run scripts, figure/table/package tooling), results_recon/ (per-seed files,
aggregated results, gates, seed-0 diagnostics, run_meta, diagnostic PNGs), the four preregistration states with the hash file,
RESULTS_RECON.md, figures/recon/, and the review record of the manuscript (panel, re-review, citation audits, disclosure).
Datasets (*.mat) and checkpoints stay excluded as in the core repository's .gitignore.
"""
import shutil, subprocess, datetime, hashlib, re
from pathlib import Path
SRC = Path(".").resolve(); REPO = Path.home() / "work/sunet-decoder-branch-eit"; DST = REPO / "recon"
assert (REPO / ".git").exists(), REPO
sha = lambda p: hashlib.sha256(Path(p).read_bytes()).hexdigest()[:12]
if DST.exists(): shutil.rmtree(DST)
(DST / "tools").mkdir(parents=True)
code = ["gen_recon_full.m", "recon_compat_check.m", "recon_heart_check.m", "build_mixed_dataset.py", "build_mixed_dataset_ps.py", "build_loro_dataset_ps.py",
        "eval_recon_matrix.sh", "eval_recon_mixed_ps.sh", "eval_recon_loro.sh", "run_recon_mini.sh", "run_recon_mixed_ps_mini.sh", "run_recon_loro_mini.sh", "recon_pipeline_air.sh",
        "pilot_recon_checks.py", "recon_results.py", "recon_delta_ci.py", "recon_scale_check.py", "recon_shift_inputs.py", "recon_mixed_ps_gate.py", "recon_mixed_ps_preds.py",
        "recon_loro_gate.py", "recon_loro_mask_check.py", "recon_loro_preds.py", "render_recon_add12.py", "recon_draft_tables.py", "recon_s1_table.py",
        "recon_figstyle.py", "make_recon_fig1.py", "make_recon_fig2.py", "make_recon_fig5.py", "check_recon_draft.py", "check_recon_draft_numbers.py",
        "format_convert_plos.py", "make_system_fields_plos.py", "pack_submission_plos.py", "ready_gate_plos.py", "sync_repo_recon.py"]
missing = [c for c in code if not (SRC / "tools" / c).exists()]; assert not missing, missing
for c in code: shutil.copy(SRC / "tools" / c, DST / "tools" / c)
# shared tools already in the repo root tools/ (train_arms.py, arms.py, evaluate.py, cite.py, apply_ref_overrides.py): compare and report
shared = {}
for c in ("train_arms.py", "arms.py", "evaluate.py", "cite.py", "apply_ref_overrides.py", "figstyle.py"):
    a, b = SRC / "tools" / c, REPO / "tools" / c
    shared[c] = "same" if a.exists() and b.exists() and sha(a) == sha(b) else ("repo lacks" if not b.exists() else "DIFFERS")
# results
shutil.copytree(SRC / "results_recon", DST / "results_recon", ignore=shutil.ignore_patterns("review", "*.pre-*"))
# preregistration states + hash file, results record
(DST / "preregistration").mkdir()
for f in ("PREREGISTRATION_RECON.pre-dev20261003.md", "PREREGISTRATION_RECON.pre-add11_20261003.md", "PREREGISTRATION_RECON.pre-add12_20261011.md", "PREREGISTRATION_RECON.md", "PREREGISTRATION_RECON.sha256"):
    shutil.copy(SRC / f, DST / "preregistration" / f)
shutil.copy(SRC / "RESULTS_RECON.md", DST / "RESULTS_RECON.md")
# figures, refs (RECON registry + strings), review record
shutil.copytree(SRC / "figures/recon", DST / "figures")
(DST / "refs").mkdir()
for f in ("refs_in_recon.json", "prior_works_recon.json", "prior_works_recon_table.md", "prior_works_recon_strings.md", "overrides.json", "01_JOURNAL_REQUIREMENTS_PLOSONE.md"):
    shutil.copy(SRC / "refs" / f, DST / "refs" / f)
M = SRC / "RECON_paper/manuscript"; RR = DST / "review_record"; RR.mkdir()
for f in ("12_REVIEWER_PANEL_round1.md", "14_RESPONSE_TO_PANEL_round1.md", "16_CITATION_AUDIT_v3.md", "16b_CITATION_RECHECK_v4.md", "18_REVIEWER_PANEL_rereview_round1.md",
          "21_CITATION_RECHECK_v6.md", "25_CITATION_RECHECK_v7.md", "26_DISCLOSURE_plos.md", "32_DISCLOSURE_plos_v8.md", "35_DISCLOSURE_plos_v9.md", "28_READY_GATE_plos_20261031.md", "28_READY_GATE_plos_20261101.md", "23_DRAFT_v7.md.apply-report.json", "20_DRAFT_v6.md.apply-report.json", "30_DRAFT_v8.md.apply-report.json", "33_DRAFT_v9.md.apply-report.json"):
    if (M / f).exists(): shutil.copy(M / f, RR / f)
for d in ("phase_review_round1_20261031", "phase_rereview_round1_20261031"):
    shutil.copytree(M / d, RR / d, ignore=shutil.ignore_patterns("*.pre-*"))
for d in ("revision-authority-round1", "revision-authority-round1b", "revision-authority-round1c", "revision-authority-round1d", "revision-authority-round1e", "revision-authority-round1f", "revision-authority-round1g", "revision-authority-round1h"):
    shutil.copytree(M / d, RR / d)
# recon README
readme = f"""# recon/ — the companion study on reconstructor change

Code, preregistration states and per-seed results for the tier-3 study *Does a decoder branch for the cardiac component of lung EIT survive a change of reconstructor? A preregistered, parameter-matched study with leave-one-reconstructor-out training* (submitted to PLOS ONE). It re-uses this repository's training and scoring code (`../tools/train_arms.py`, `arms.py`, `evaluate.py`) and the GREIT networks of `../results_20db_fix` (seeds 0–29), and adds one-step Gauss–Newton and Sheffield back-projection reconstructions, pooled and leave-one-reconstructor-out training rows.

| Path | What |
|---|---|
| `preregistration/` | The four hashed states of `PREREGISTRATION_RECON.md` (registered 4b4c7a6d…, 2026-09-26; deviation record 3fdc703d…; first addendum 0060eedf…; second addendum 9589b298…) and the hash file |
| `RESULTS_RECON.md` | Laboratory record of every number, in registered order (Chinese) |
| `results_recon/<cell>/` | `per_seed.csv`, `per_image.csv`, `summary.json` for the 39 cells (`<train>__<eval>[_e1|_ownaffine]`, `mixed__*`, `mixedps__*`, `loro_<held-out>__<eval>`); `recon_results.json`, `recon_delta_ci.json`, gates and seed-0 diagnostics |
| `tools/` | Reconstructor datasets (`gen_recon_full.m`, `build_*_dataset*.py`), the training/scoring drivers, the registered statistics (`recon_results.py`, `recon_delta_ci.py`), tables and figures (`recon_draft_tables.py`, `recon_s1_table.py`, `make_recon_fig*.py`), the PLOS ONE deliverable and package tooling |
| `figures/` | Fig 1, 2 and 5 (PDF, PNG, TIFF) |
| `refs/` | The citation registry of this paper (`refs_in_recon.json`, 72 entries) with the generated strings and the documented overrides |
| `review_record/` | Simulated five-seat review (2026-10-31), its three-gate re-review and scoped re-verifications, the revision-authority chains of rounds 1–1h, the citation audits and the AI-disclosure checks |

Datasets (`*.mat`) and checkpoints are excluded as in the root `.gitignore`; the Gauss–Newton and back-projection datasets regenerate from `tools/gen_recon_full.m` with the seeds recorded in `results_recon/run_meta_*.json`.
"""
(DST / "README.md").write_text(readme, encoding="utf-8")
# commit message draft (the PI commits)
n_files = sum(1 for p in DST.rglob("*") if p.is_file())
msg = f"""RECON review record update after rounds 1h (placeholders, S1 Data, figure sentence): v9 chain, disclosure and re-verification reports

Adds recon/ with the reconstructor-change study (GREIT / one-step Gauss-Newton / back-projection; pooled and leave-one-reconstructor-out rows): {n_files} files.
Manuscript draft 33_DRAFT_v9 (32cf6b27f35b); deliverable 34_SUBMISSION_plos_v9; re-review Minor Revision -> rounds 1d/1e/1g/1h scoped Accept; citation re-checks and AI-disclosure check on file.
Shared tools vs repo root: {', '.join(f'{k} {v}' for k, v in shared.items())}.

Co-Authored-By: Claude Fable 5.1 <noreply@anthropic.com>
"""
(SRC / f"COMMIT_MSG_repo_recon_{datetime.date.today():%Y%m%d}.txt").write_text(msg, encoding="utf-8")
st = subprocess.run(["git", "-C", str(REPO), "status", "--short"], capture_output=True, text=True).stdout
print(f"staged {n_files} files under {DST}; shared tools: {shared}")
print("git status lines:", len(st.strip().splitlines()), "| untracked recon/:", "?? recon/" in st)
