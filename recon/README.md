# recon/ — the companion study on reconstructor change

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
