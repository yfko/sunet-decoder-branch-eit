# Addendum to the round-1 re-review: scoped verification of revision round 1d (v4 → v5)

Addendum for round `sunet-recon-tier3-rereview-round1-20261031` (legacy v1.0 re-review family). Scoped seat-verifier call (Phase 2B′ shape), fresh context, 2026-10-31. Judge: Claude Fable 5.1. Scope: the round-1d blocks only (B0023, B0028, B0066, B0074, B0116, B0158); regression attribution confined to these six; previously-missed issues out of scope by instruction. Read-only on the manuscript; this call emits only `addendum_v5.json` (sha256 `5ef6c81bdc81a3829b57583a7ac4b5a98ba3f7723ca31e7e0e041b407bdc057f`) and this file.

Object: `17_DRAFT_v4.md` (sha256 `6379490727ef0fe5a2452a1d10f8e5693c091a0839a333e32f1b57e90aeaeb66`) → `19_DRAFT_v5.md` (sha256 `bf252f799a3a489d8dc1a7531ab51cfcd43e28820c4af15ade33daf6a441c732`), judged against `revision-authority-round1d/roadmap.json` (sha256 `e2b2144d46f3…`; five items REV-M1d-1 … -5, all must_fix). Patch `revision-authority-round1d/revision_patch_round1d.json` sha256 `1ecf52149abd…`; apply report `19_DRAFT_v5.md.apply-report.json` sha256 `37f0075cc59c…`. The re-review it extends: `18_REVIEWER_PANEL_rereview_round1.md` (sha256 `e2307b8f5fb2…`), Decision (final for this round) Minor Revision under rule B5, whose operands were the REV-M1-2 and REV-M1-19 consider-level residuals and the three minor regressions NEW-1, NEW-2, NEW-3.

## Disclosure

This verification round ran on the same model family that drove the revisions; over-optimization to this judge's latent biases is possible (Ren et al. 2026, arXiv:2607.13104 §8.1.2).

## Candidate scoped decision

**Accept (scoped).** All five round-1d items are FULLY_ADDRESSED and the six replace_block operations introduced no regression. The B5 operand set of 18_ is closed: the two must_fix residuals (REV-M1-2 → REV-M1d-4; REV-M1-19 → REV-M1d-5) and the three minor regressions (NEW-1 → REV-M1d-1; NEW-2 → REV-M1d-2; NEW-3 → REV-M1d-3) each have a closing anchor in v5. Verdict counts: FULLY 5 / PARTIALLY 0 / NOT 0 / WORSE 0 / CANNOT 0. The decision is a candidate: the dispatching layer records it in the sidecar and derives the round decision; this seat does not.

## Per-item verdicts

| Item | Block | Criterion (roadmap `verification_criteria`) | Verdict | Anchors in v5 | Note |
|---|---|---|---|---|---|
| REV-M1d-1 (NEW-1) | §2.1 B0023 | B0023 names the reconstructors in full or after their definition; no abbreviation is used before it is defined. | FULLY_ADDRESSED | "(training-split SD ratio; GREIT, Gauss–Newton, back-projection)". Regex `\bGN\b` / `\bBP\b` over all 160 blocks: first hits B0024 (where "One-step Gauss–Newton (GN)" and "Back-projection (BP)" are defined), B0025, B0031; none in B0001–B0023. difflib v4→v5: 5 ops, confined to the parenthesis and to "which is what makes … weak for this simulation" → "which makes … weak in this simulation"; the ratios 0.14 / 0.085 / 0.099 and both citation anchors unchanged. | GREIT appears from the Abstract (B0006) onward as the algorithm's name, as in v4. Observation, pre-existing and not attributed to 1d: "SD" is never expanded anywhere in the manuscript; it was in v4's B0023 too. |
| REV-M1d-2 (NEW-2 = 16b N1) | §4.4 B0074 | B0074 no longer ranks this study's losses against the analogue range; it calls them losses of the same kind and keeps the two differences that forbid a comparison of magnitudes. | FULLY_ADDRESSED | "the 16 to 62 points lost here and the exploratory 19 to 34 points are losses of the same kind, but two differences forbid a comparison of magnitudes: in those studies the label is anatomy and only the input changes with the domain; here the reference is the held-out reconstructor's own cardiac image and changes with it … Those studies used patients and manufacturers; this one simulation, three conventional algorithms and thirty seeds." "start where that range ends" absent. difflib: 3 ops ("start where that range ends" → "are losses of the same kind"; "And t" → "T"; " used" deleted). The four ref/anchor markers byte-identical to v4; number sequence identical (21, 31, 0.89, 0.91, 0.60, 0.69, 2020, 4, 17, 0.72, 0.76, 0.68, 0.59, 2018, 16, 62, 19, 34); 138 → 137 words. | The replacement is the second fix 16b_CITATION_RECHECK_v4.md L188 offered ("Drop the ranking"). The closing clause is elliptical ("this one simulation, …"); grammatical, decision-inert. |
| REV-M1d-3 (NEW-3) | §2.2 B0028; Table 4 B0116; S2 B0158 Training row | B0028 and the Table 4 registered-state cell give the campaign window as the record gives it (2026-09-24 16:26 to 2026-09-26 00:44) and the hashing time (17:41 on 2026-09-26); S2 Table's training row carries the same window. | FULLY_ADDRESSED | B0028: "trained between 2026-09-24 16:26 and 2026-09-26 00:44 and scored on 2026-09-26, before the registered state was hashed (17:41)". B0116 Registered row: "trained in the campaign of 2026-09-24 16:26 to 2026-09-26 00:44 and scored 2026-09-26, before hashing at 17:41". B0158 Training row: "the companion study's 58-seed campaign of 2026-09-24 16:26 to 2026-09-26 00:44 (two parallel processes; no per-seed completion times were logged)". Sources: `../../RESULTS_STUDY2.md` L231–L232; `../../PREREGISTRATION_RECON.sha256` L2 ("registered 2026-09-26 17:41 CST"); `../../results_20db_fix/*` mtime Sep 26 00:45:51 2026. B0116 row and B0158 Training row byte-identical to `tools/recon_draft_tables.py` L141, L167. | The three surfaces agree with each other and with the record; the before-hashing ordering holds (00:44 < 17:41). "No per-seed completion times were logged" is an absence claim traceable only to the silence of the surviving records (§十之二; `per_seed.csv` has no time column; `runs_20db/` is not on this machine). B0028's last clause was also re-worded ("so a between-campaign difference is confounded with every contrast pairing …"); no claim changed. |
| REV-M1d-4 (REV-M1-2 residual) | §4.1 B0066 | The last sentence of B0066 carries "(first addendum; descriptive)" beside the M2′ quantities. | FULLY_ADDRESSED | "… differed by −0.08 to +0.36 points with two of six intervals favouring pooling (first addendum; descriptive), a difference this design cannot separate from threefold optimisation steps." difflib: exactly 1 op, the insertion of " (first addendum; descriptive)". | Matches the standing labels of the other number-carrying clauses of B0066. |
| REV-M1d-5 (REV-M1-19 residual) | S2 Table B0158 | S2 Table states the contact impedance value and its source, the GREIT training-target distribution (spiral, radii, plane), the desired-image function and radius, the noise-figure calibration target, and the normalised-difference setting, every value traceable to a named script line. | FULLY_ADDRESSED | Forward model row: "electrode contact impedance 0.01 in model units (the `ng_mk_fwd_model` default); normalised difference data for all three reconstructors (`mdl_normalize`)". GREIT row: "1,000 simulated training targets on the GREITv1 spiral (`distr` 0: radial position 0 to 0.9 of the mesh half-width in equal steps, angle 4321 × that fraction in radians, in the electrode plane, each of radius 0.05 of the mean half-width); desired image the EIDORS default sigmoid of radius 0.2 of the model radius (`GREIT_desired_img_sigmoid`, steepness 10/radius); noise figure 0.5 (nominal) calibrated on one central target of radius 0.02 (`target_size`)". Every value traced to a source line in the fact-check table below (read in this call, not taken from the author event). difflib v4→v5: 5 ops, all inside the Forward model, GREIT and Training rows; those three rows are byte-identical to `tools/recon_draft_tables.py` L157, L160, L167; every other row unchanged. | The inexact v4 phrase "training targets of radius parameter 0.02" is gone. Two qualifiers have no source line of their own and are decision-inert: "in model units" (EIDORS states no unit for `z_contact`) and the implicit unit of "radius 0.02" (a fraction of the model radius under `mk_GREIT_model`'s default, 0.02 × 0.5 × diameter; the row states the fraction explicitly only for the 0.2 desired-image radius). |

## Chain check

| Check | Result |
|---|---|
| sha256(`17_DRAFT_v4.md`) = apply report `base_draft_hash` 6379490727ef; = roadmap `base_draft_sha256` | yes |
| sha256(`19_DRAFT_v5.md`) = apply report `output_draft_hash` bf252f799a3a | yes |
| sha256(patch file) = apply report `patch_digest` 1ecf52149abd… | yes |
| sha256(`roadmap.json`) = patch and report `roadmap_sha256` e2b2144d46f3… | yes |
| sha256(`17_DRAFT_v4.md.block-manifest.json`) = roadmap `block_manifest_sha256` a820e6e56fb6… | yes |
| sha256(`claim-surface-manifest.json`) = witness `claim_surface_manifest_sha256` 6e4d0ed12189… | yes |
| sha256(`author-adjudication.json`) = witness `author_adjudication_sha256` bbd5c83b351f… (file hashed, not read) | yes |
| Block split on `<!--block:BNNNN-->`: 160 blocks in both files, same order, no duplicate id, identical (empty) preamble | yes |
| Blocks that differ v4 vs v5 | exactly B0023, B0028, B0066, B0074, B0116, B0158 (the six the patch names); 154 byte-identical (report: 154 / 160, preserved ratio 0.9625) |
| Each patch `old_hash` = v4 manifest entry = sha256₁₂ of the v4 block body (whitespace-stripped) | 6 / 6 |
| Each patch `new_text` = v5 block body; v5 manifest hash = sha256₁₂(new_text) | 6 / 6 |
| Hash convention reproduced for all 160 blocks of both manifests | yes (160 / 160 each) |
| Structural flags | none: section_count_delta 0, touched_ratio 0.0375 < 0.6, no heading op, no fresh block, no pure move |
| `check_recon_draft.py` (run from the SunetBeta project root on `RECON_paper/manuscript/19_DRAFT_v5.md`) | main text **7,995** words (ceiling 8,000; v4 7,996); abstract **296** (≤ 300); ASCII minus before a digit in prose 0; citations 82 instances / 70 distinct, slugs outside corpus [], cited-but-unlisted [], listed-but-uncited []; R10b leak scan clean. Section 1–3 "OUT OF BAND" lines refer to the pre-round-1b band, which the PCR replaced by the 8,000 ceiling. |
| `check_recon_draft_numbers.py` | 375 numbers in prose; **0** not derivable from the result/registration files |
| ASCII hyphen-minus before a digit inside the six changed blocks (outside code spans and markers) | 0 in each |

## Fact-check table (statement → source read in this call)

| S2 / 1d statement | Source file:line | Status |
|---|---|---|
| Contact impedance 0.01 is the `ng_mk_fwd_model` default | `eidors/meshing/netgen/ng_mk_fwd_model.m:37-38` (`if nargin<5 … z_contact=0.01; % singular if z_contact=0`); `eidors/meshing/netgen/ng_mk_cyl_models.m:120` calls it with four arguments | traced |
| No project script overrides `z_contact` | grep over `tools/gen_dataset.m`, `tools/gen_recon_full.m`, `EIT_noise_geometry/src/p2_build_env.m`: no hit | traced (absence) |
| "in model units" (contact impedance) | none; `ng_mk_fwd_model.m:16` gives only "vector or scalar electrode contact impedance" | qualifier without a source line; decision-inert |
| Normalised difference, GREIT | `p2_build_env.m:38` (`mdl_normalize(fmdlG,1)`); `mk_GREIT_model.m:389` (`opt.normalize = fmdl.normalize_measurements`); `calc_GREIT_RM.m:37-38` (`Y = vi./(vh*ones(1,size(vi,2))) - 1`) | traced |
| Normalised difference, GN | `tools/gen_recon_full.m:47`; `inv_solve_diff_GN_one_step.m:41` → `calc_difference_data.m:36,41` (`if mdl_normalize(fwd_model)`) | traced |
| Normalised difference, BP | `eidors/models/mk_common_gridmdl.m:100` (`inv_mdl.fwd_model = mdl_normalize(inv_mdl.fwd_model, 1)`, reached from the `'backproj'` branch at :43-45, :80) | traced |
| Coarse cylinder maxsz 0.20; 64 × 64; Nsim 1,000; NF 0.5; `distr` 0; `target_size` 0.02 | `p2_config.m:12` (`P.maxsz = 0.2`), `:21-22` (`P.greit = struct('imgsz',[64 64], 'distr',0, 'Nsim',1000, 'target_size',0.02, 'noise_figure',0.5)`); `p2_build_env.m:36,39` | traced |
| GREITv1 spiral: r 0 → 0.9 of the half-width in equal steps; angle 4321 r; electrode plane; radius 0.05 of mean half-width | `mk_GREIT_model.m:24` ("0 -> original (as per GREITv1, default)"), `:173-175` (maxx, maxy = max |node − centre|), `:181-187` (`r = linspace(0,0.9, Nsim); th = r*4321; … opt.target_plane … 0.05*mean([maxx,maxy])`), `:349-350` (`target_plane` default = mean electrode height; `P.greit` sets none) | traced |
| Desired image = EIDORS default sigmoid | `eidors/eidors_startup.m:37` (`eidors_default('set','GREIT_desired_img','GREIT_desired_img_sigmoid')`); `calc_GREIT_RM.m:42-48` | traced |
| Desired-image radius 0.2 of the model radius | `p2_build_env.m:39` (second argument 0.2); `mk_GREIT_model.m:15,131,144` (radius passed through); `GREIT_desired_img_sigmoid.m:8-9` ("fraction of the model radius (half the larger dimension in xy)"), `:167-172,215-216` (radius non-empty → used directly in the [−1, 1]-rescaled frame) | traced |
| Steepness 10/radius | `GREIT_desired_img_sigmoid.m:23,184-185` | traced |
| NF calibrated on one central target of radius 0.02 (`target_size`) | `mk_GREIT_model.m:378-383` (default `noise_figure_targets`: `xyzr = mean(fmdl.nodes); xyzr(3) = opt.target_plane; xyzr(4) = mean(opt.target_size)*0.5*R`, R the xy extent, so 0.02 × model radius), `:114-127` (`vi_NF` simulated from it); `p2_config.m:22` | traced; the row leaves implicit that 0.02 is a fraction of the model radius |
| Cylinder radius 2, height 2; 16 electrodes of radius 0.1 at height 1; forward maxsz 0.10; stim pattern; 208 measurements | `tools/gen_dataset.m:107,131`; `p2_build_env.m:24`; `ng_mk_cyl_models.m:7,14,19` (argument meanings); 16 × 13 = 208 | traced (unchanged from v4) |
| Campaign 2026-09-24 16:26 → 2026-09-26 00:44; 58 seeds (116 runs); two parallel processes | `../../RESULTS_STUDY2.md:231-232` | traced |
| Hashed 17:41 on 2026-09-26 | `../../PREREGISTRATION_RECON.sha256:2` ("registered 2026-09-26 17:41 CST after PI confirmation") | traced |
| Scored on 2026-09-26 | `../../results_20db_fix/per_image.csv, per_seed.csv, summary.json` mtime Sep 26 00:45:51 2026; `RESULTS_STUDY2.md:235` (scoring command) | traced (file timestamps) |
| "no per-seed completion times were logged" | §十之二 records none; `per_seed.csv` columns `arm,seed,channel,params,width_mult,mae,dsc,iou,sens,spec,assd,hd95`; `runs_20db/` not present on this machine | absence claim; traceable only to the silence of the surviving records |
| B0074 numbers and four anchors unchanged | scripted comparison v4 vs v5 | traced |
| B0066 standing label; B0023 abbreviations | scripted comparison v4 vs v5; regex over all blocks | traced |

## New issues

None. The six replace_block operations are confined to the wording the roadmap names; no number of this study, verdict, hash, reference or scope rule changed, and the checkers' totals moved by one word (7,996 → 7,995).

Four observations, decision-inert, not recorded as issues:

- §2.1 B0023: "SD" (training-split SD ratio) is never expanded in the manuscript. Pre-existing (in v4's B0023), outside NEW-1's GN/BP scope.
- S2 Table B0158: "in model units" for the 0.01 contact impedance and the unit of "radius 0.02" for the calibration target are the authors' qualifiers; the values and their sources are traced; the fraction-of-model-radius reading of 0.02 is implicit.
- S2 Table B0158, Training row: "no per-seed completion times were logged" is an absence claim resting on the silence of RESULTS_STUDY2 §十之二 and of `results_20db_fix/per_seed.csv`; the raw `runs_20db/` directory is not on this machine.
- §4.4 B0074: "this one simulation, three conventional algorithms and thirty seeds" is elliptical ("used" carried from the previous clause).

## What was checked

1. Hashes: sha256 of `17_` and `19_` against the apply report; sha256 of the patch against `patch_digest`; sha256 of the roadmap, the v4 block manifest, the claim-surface manifest and `author-adjudication.json` (hashed, not opened) against the witness fields.
2. Block diff on `<!--block:BNNNN-->` markers (160 blocks, same order, empty preamble): exactly six blocks differ; the patch's `old_hash` values equal the v4 manifest and the recomputed sha256₁₂ of each v4 block; each `new_text` equals the v5 block; the v5 manifest's hashes equal sha256₁₂ of each `new_text`; the convention reproduces all 160 entries of both manifests.
3. REV-M1d-1: regex for `\bGN\b`, `\bBP\b`, `\bGREIT\b`, `\bSD\b` over every block in order; B0024's definitions; difflib on B0023.
4. REV-M1d-2: presence/absence of the two clauses; ref/anchor marker lists v4 vs v5; number sequence v4 vs v5; word count; 16b_CITATION_RECHECK_v4.md §4 N1 (L175–L190).
5. REV-M1d-3: the window and time strings in B0028, B0116, B0158; RESULTS_STUDY2 §十之二 (L229–L244) and a grep for every other `runs_20db` or hh:mm mention (none); PREREGISTRATION_RECON.sha256; `results_20db_fix` file times and `per_seed.csv` header; `tools/recon_draft_tables.py` L141, L167 literal rows against v5.
6. REV-M1d-4: difflib on B0066 (one insertion).
7. REV-M1d-5: EIDORS v3.8 source — `ng_mk_fwd_model.m`, `ng_mk_cyl_models.m`, `mk_GREIT_model.m` (header, `stim_targets` case 0, `calc_radius`, `parse_options`, NF block), `calc_GREIT_RM.m`, `GREIT_desired_img_sigmoid.m` (header and `parse_opt`), `mk_common_gridmdl.m`, `mdl_normalize.m`, `inv_solve_diff_GN_one_step.m`, `calc_difference_data.m`, `eidors_startup.m`; project scripts `tools/gen_recon_full.m`, `tools/gen_dataset.m`, `EIT_noise_geometry/src/p2_build_env.m`, `EIT_noise_geometry/src/p2_config.m`; `tools/recon_draft_tables.py` L157, L160 literal rows against v5.
8. Checkers: `tools/check_recon_draft.py` and `tools/check_recon_draft_numbers.py` on `19_DRAFT_v5.md` (the first must be run from the SunetBeta root so that `refs/refs_in_recon.json` resolves).
9. Not read, by instruction: `14_RESPONSE_TO_PANEL_round1.md`, `author_event_20261031d.txt`, `author-choices.json`, `author-adjudication.json` (sha256 only), NOTES files, `03_PAPER_OUTLINE.md`. Blocks outside the six were not re-examined.
