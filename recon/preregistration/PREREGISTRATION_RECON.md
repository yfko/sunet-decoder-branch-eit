# Pre-registration — is the matched-training null GREIT-bounded, and does the branch's shift tolerance survive a change of reconstructor?

**STATUS: confirmed by the PI 2026-09-26 (NF matched to GREIT; n = 30; mixed row included) and hashed the same day; the hash is in `PREREGISTRATION_RECON.sha256` and is written into every `run_meta.json`. After this point the body is not edited; corrections go to §10.**

This is the registered simulation pilot of the Spectra imaging paper (`發表界線條款_20260922.md` §三) and, under that clause's tier-3 fallback, a standalone paper. It answers the question the original semi-Siamese study listed as future work: the separation effect "obtained by the different reconstruction algorithms … notably, Shield back-projection algorithm, FEM-based linearized Newton-Raphson algorithm, and Graz consensus reconstruction algorithm (GREIT)" (Ko and Cheng 2021, PLoS One, Conclusions). It inherits everything from `PREREGISTRATION_HEART.md` (hash `2f2e1a0b946f2748…`, addendum `a252444b…`) that it does not explicitly change.

## 1. What the core paper established, and what it left open

The core paper's addendum (§9.2) found that when D and B_wide are trained and evaluated at the same noise level, the branch is worth +0.223 Dice points at 40 dB (floor 0.670) and +0.229 at 20 dB (floor 0.384), clearing the registered floor at neither, while a network trained at 40 dB and evaluated at 20 dB gains +2.097 points. Its Discussion attributes the evaluation-only advantage mainly to tolerance of a training–evaluation mismatch, and states that "the branch's benefit depends on the perturbation, not on the nominal level", with GREIT passing a median 8.5% of peak into the image at a tenfold noise increase. Its first Limitation is that every image was GREIT-reconstructed.

Two things are therefore open, and they are different questions:

- **Diagonal (matched training, different reconstructor).** GREIT is a heavily regularised inverse. A reconstructor that lets more measurement noise into the image at the same nominal SNR presents the network with a larger perturbation even when training and evaluation are matched. Does the branch then clear the floor? If yes, the core paper's matched-training null is GREIT-bounded and the perturbation account is supported. If no, the null extends across the three reconstructors the original study named.
- **Off-diagonal (cross-reconstructor shift, evaluation only).** The core paper showed the branch tolerates a noise-amplitude shift it was not trained on. Does that tolerance transfer to a different kind of shift, a change of reconstructor?

The training × evaluation matrix makes the two visible:

| trained on ↓ / evaluated on → | GREIT | GN | BP |
|---|---|---|---|
| **GREIT** | H5 (done: +0.229, falsified) | R3 | R3 |
| **GN** | R3 | **R1** | R3 |
| **BP** | R3 | R3 | **R1** |

## 2. Claims and non-claims

**Tested:** whether the branch's matched-training advantage clears the registered floor under two reconstructors other than GREIT (R1), and whether its advantage under a cross-reconstructor shift exceeds its matched advantage (R3).

**Not claimed, whatever the outcome:** any ranking of reconstructors by image quality (the three are nuisance variables; heart DSC of the downstream network is the endpoint and will differ between them, and that difference is reported, not interpreted as reconstructor quality); anything about learned reconstructors (flagship line); anything at 40 dB or any noise level other than 20 dB; anything about arms other than D and B_wide; anything about loss weighting; any measured-data result (that is the hardware experiment this pilot serves).

## 3. Hypotheses and what falsifies them

Primary endpoint, unchanged: **heart-channel DSC on the quarter-amplitude set (`calc_hm_set(img, 0.25)` in image units, the corrected evaluation path), test split, mean over the registered seeds, at 20 dB.** Each reconstructor's targets are its own single-organ reconstructions, as in the core paper.

| | confirmed if | falsified if |
|---|---|---|
| **R1-GN** (train GN, eval GN) | mean DSC_heart(D) − DSC_heart(B_wide) exceeds B_wide's seed-to-seed SD under that condition **and** Wilcoxon signed-rank (two-sided, normal approximation with continuity correction) over paired seeds gives p < 0.05 | either condition fails, or the sign is reversed |
| **R1-BP** (train BP, eval BP) | same rule | same |
| **R3-(X→Y)**, six cells: X ∈ {GREIT, GN, BP} trained, Y ≠ X evaluated, no retraining | Δ(X→Y) − Δ(X→X) > 0 with a 95% percentile bootstrap CI over paired seeds (100,000 resamples) that excludes zero, where Δ is the paired D − B_wide heart-DSC difference | the CI contains zero, or the difference is negative |

R1 has the same two-condition form as H1 and H5, applied at the level where the branch is expected to matter. R3 has the same form as H3, with the shift being the reconstructor instead of the noise amplitude.

**Interpretations, fixed now so they cannot be re-described later.**

- R1-GN or R1-BP confirmed while H5 (GREIT) is falsified: the matched-training null of the core paper is GREIT-bounded; the branch pays off under matched training when the reconstructor passes enough of the measurement perturbation into the image. The perturbation account of §4.1 of the core paper is supported, and the hardware experiment must register which reconstructor it deploys as a design variable, not a nuisance.
- R1-GN and R1-BP both falsified: the null extends across the three reconstructors the original study named. The sentence the imaging paper may then write is "a network trained at its operating noise level does not need the branch under any of the three conventional reconstructors tested", and the hardware experiment's primary contrast is the sim-to-real shift, not the branch.
- R3 confirmed in a cell: the branch's shift tolerance is not specific to noise amplitude; it transfers to a reconstructor change. R3 falsified in a cell: the tolerance seen in the noise sweep is specific to that kind of shift. Cells are reported individually and never pooled; a mixed pattern is reported as mixed.
- Any R1 confirmed does not retroactively change H1 or H5; any R3 result does not change H3.

**Secondary, reported not tested:** (a) the image-domain perturbation each reconstructor passes at 40→20 dB, computed as in `tools/noise_perturbation.py` (median peak fraction and RMS fraction over the 360 test frames), so that the three reconstructors can be placed on the perturbation axis the core paper defined; with three points no correlation is tested. (b) The lung channel in every cell (H4 expectation carried over: no difference). (c) Each off-diagonal cell re-evaluated with the evaluation set's own dataset-wide affine instead of the training set's ("scale-matched shift"), to separate a pure scale mismatch from a structural one. The registered R3 cells use the training set's affine, as the noise sweep did, because that is what deployment sees. (d) Absolute heart DSC of B_wide and D per cell.

## 4. Arms, reconstructors, data

**Arms:** D and B_wide only (`tools/arms.py`, unchanged). Nothing else is trained.

**Reconstructors**, all EIDORS v3.8, all on the registered coarse cylinder model (`ng_mk_cyl_models([2,2,0.2],[16,1],[0.1])`, adjacent stimulation, `no_meas_current`), all sliced to 64×64 by the same `slice64`:

| | solver | regularisation | how the strength is set |
|---|---|---|---|
| GREIT | `mk_GREIT_model`, as registered (`P.greit`: imgsz 64×64, Nsim 1000, target_size 0.02, noise_figure 0.5) | GREIT training set | unchanged from the core paper |
| GN | `inv_solve_diff_GN_one_step`, solved directly on GREIT's own 64×64 reconstruction grid (`rec_model` with `mk_coarse_fine_mapping` from the registered coarse cylinder), so GN images land on the GREIT raster with no resampling | Laplace prior (`prior_laplace`) | hyperparameter set by a bounded bisection in log10(hp) so that GN's noise figure equals GREIT's **realised** noise figure on one common reference frame (the environment phantom): GREIT 0.602 → GN hp 0.0016, NF 0.607 (`tools/recon_compat_check.m`, log in `results/recon_compat_check.log`). EIDORS's `choose_noise_figure` on the 27,981-element 3D mesh did not converge in 2.7 h and is not used |
| BP | `mk_common_gridmdl('backproj')`, the Sheffield MKI back-projection matrix on EIDORS's 16-electrode adjacent grid model (EIDORS's own `inv_solve_backproj` is documented as incomplete and is not used); it accepts the registered 208-value frames | none | no free parameter; realised noise figure on the same reference frame 0.831. Its 32×32 raster is upsampled 2×2 to 64×64 and masked to the GREIT field of view |

PI decision 2026-09-26: GN noise figure matched to GREIT's. The pre-hash compatibility check (below) fixed how: GREIT's realised NF on a common reference frame, not the nominal 0.5 used to build GREIT, so that the two operators are compared at equal noise amplification on the same data. The alternative (EIDORS default hyperparameter) is not run.

**Pre-hash compatibility check (2026-09-26, `results/recon_compat_check.log`, `tools/recon_heart_check.m`)**, run on the environment phantom only, no dataset, no network: all three reconstructors accept the 208-value frames; the lung-only frame peaks at the same pixel in all three (row 31, columns 49/51/49); the heart-only frame peaks centrally in all three (row 31, columns 32/33/33); the heart quarter-amplitude set covers 8.6% (GREIT), 16.7% (GN) and 14.0% (BP) of the field of view. No edge artefact dominates a single-organ image.

**Data:** the registered 3,600 geometries and noise seeds of `data/v2` (`gen_dataset.m`, `noise_seed0 + i`), all splits re-noised at **20 dB** exactly as `gen_snr_full.m` does for GREIT, then reconstructed three times per geometry (mixed, lung only, heart only) with each reconstructor → `data/v2_full_snr20_gn/`, `data/v2_full_snr20_bp/`. The GREIT dataset at 20 dB already exists (`v2_full_snr20`). The training split is therefore bit-identical in geometry and noise across the three datasets; only the reconstruction operator differs. **New: the generator saves the boundary voltages `vh, vi_m, vi_l, vi_h` alongside the images** (they are not saved today), so that the measurement-domain line (`../EIT_measurement-domain_separation/`) can reuse them without a third generation.

**Training:** `train_arms.py`, every constant unchanged (Adam 1e-3 cosine to 1e-5, batch 16, ≤200 epochs, patience 20, L1, weights 1.0/1.0, no augmentation, dataset-wide affine from that dataset's training split), on the same Mac mini, `run_meta.json` carrying this file's hash and each dataset's hash.

## 5. Seeds and power

Registered **n = 30 seeds (0–29)** per arm per reconstructor for GN and BP: 2 × 2 × 30 = **120 runs**. The GREIT row reuses `runs_20db` seeds 0–29 (already trained under §9.2; no new GREIT training), so all nine cells are compared on the same thirty seeds; the 58-seed GREIT numbers of §9.2 are reported beside them as the reference.

Why 30 and not 58. R1 asks whether the branch **clears the floor**, and the floor is by construction an effect of about one control-SD; in the three matched or mismatched contrasts already measured, the floor sits at dz ≈ 0.61–0.81. R3 asks about a difference the noise sweep put at dz ≈ 1.2. Paired power at α = 0.05:

| dz | n = 20 | n = 30 | n = 58 |
|---|---|---|---|
| 0.40 (H5-sized effect, below the floor) | 0.40 | 0.56 | 0.85 |
| 0.60 (floor, low end) | 0.72 | 0.89 | 0.99 |
| 0.80 (floor, high end) | 0.92 | 0.99 | 1.00 |
| 1.19 (noise-sweep shift effect) | 1.00 | 1.00 | 1.00 |

n = 30 gives ≥ 0.89 power for a floor-sized R1 effect and > 0.99 for an R3 effect of the size already seen. It does **not** power a below-floor effect of the H5 size; such an effect would be reported with its interval and would not confirm R1, which is what the floor is for. PI decision 2026-09-26: n = 30 (120 runs, ≈33 h at the mini's measured 3.65 runs/h with two processes; the mixed row of §9 adds 60 runs on a training split three times larger, ≈2.5× the wall time per run, ≈40 h). **n is fixed at hashing and not revised after any contrast is seen.**

## 6. Pilot, and what it may not look at

Before the 120 runs, a pilot on the two new datasets checks only the data: (i) the 40 dB self-check of `gen_snr_sweep.m` replays exactly; (ii) for each reconstructor, the quarter-amplitude set of the single-organ targets covers a plausible organ fraction (the core paper's defect, §2.5, was found because the heart mask covered 94.8% of the field; the registered figure for GREIT is 0.087 mean), and the corrected `--qa-space image` path is used; (iii) the noise figure of GN is 0.5 ± 0.05 and BP's is recorded; (iv) the image-domain perturbation of §3(a) is computed; (v) the BP grid raster is aligned with the GREIT raster (the single-organ BP reconstructions peak at the same pixel locations as the GREIT ones, within one pixel, on ten test frames); (vi) the GREIT replay of one test frame at 20 dB reproduces `v2_full_snr20` to floating-point precision, proving the forward-mesh replay is exact. The pilot trains **no arm** and computes **no contrast**. Any design change after the pilot is made before hashing; none after.

## 7. Mixed-reconstructor training (fourth training row; PI decision 2026-09-26: included, see §9)

A fourth training condition, **mixed**, in which each seed is trained on the union of the three reconstructors' training splits (8,640 frames; validation split likewise pooled; one dataset-wide affine estimated on the pooled training split), then evaluated on each reconstructor's test split. It asks a question the branch cannot answer alone: whether the training distribution, rather than the architecture, buys reconstructor-agnosticism at matched parameter count. Rules in §9.

## 8. Order of operations

1. PI confirms this text (decisions ⚠️: NF matching, n, §7); hash recorded in `PREREGISTRATION_RECON.sha256`; hash copied into the imaging paper's boundary record.
2. `gen_recon_full.m` (new; derived from `gen_snr_full.m` + `gen_dataset.m`, with voltages saved) on the Air: GN and BP datasets at 20 dB.
3. Pilot of §6 on the Air; results into `RESULTS_RECON.md` §0.
4. `train_arms.py --arms D B_wide --seeds 0..29 --prereg PREREGISTRATION_RECON.md` on the mini, once per new dataset, then once on the pooled dataset of §9 (`data/v2_full_snr20_mixed/`, built by concatenation with a recorded frame-to-source map).
5. `evaluate.py` for all twelve cells (four trained sets × three evaluation sets) plus the scale-matched variants of §3(c); per-seed files kept.
6. `RESULTS_RECON.md` filled in registered order (R1-GN, R1-BP, the six R3 cells, M1, then secondaries) **before any manuscript text**.
7. Adversarial review (`academic-paper-reviewer`) after step 6, not before.

## 9. Mixed-reconstructor training: rules

**M1 (tested), three cells (mixed→GREIT, mixed→GN, mixed→BP):** the R1 rule applied to D − B_wide trained on the pooled split and evaluated on reconstructor Y. Confirmed if the difference exceeds B_wide's seed SD under that cell **and** p < 0.05; falsified otherwise. Fixed interpretation: confirmed in a cell means the branch pays off when the training distribution spans reconstructors, i.e. the branch adds something on top of domain randomisation; falsified means it does not, extending the matched-training null to a pooled training distribution.

**M2 (reported, not tested), per Y:** DSC_heart(B_wide, mixed→Y) − DSC_heart(B_wide, Y→Y), paired by seed, with a 95% bootstrap CI — the cost of pooling relative to specialising. The same for D.

**M3 (reported, not tested), per (X, Y) with X ≠ Y:** DSC_heart(B_wide, mixed→Y) − DSC_heart(B_wide, X→Y), paired by seed, with CI — how much of the off-diagonal penalty pooling removes. The same for D.

M2 and M3 are the quantities a practitioner needs; they are reported with intervals and no verdict, because "pooling helps" is expected and the paper does not claim it as a finding. What the paper may claim from M1–M3 is the ordering of three remedies for reconstructor change at matched parameter count, the branch, retraining on the target reconstructor, and pooled training, each measured on the same seeds and geometries.

**What §9 does not licence:** any statement about pooled training at 40 dB, about pooling more than these three reconstructors, or about learned reconstructors; any reconstructor ranking.

**Cost:** 2 arms × 30 seeds = 60 runs on an 8,640-frame training split, ≈2.5× the per-run time, ≈40 h on the mini; checkpoints ≈2.4 GB.

## 10. Deviations

Any change after hashing is recorded here, dated, with its reason, never by editing the text above.

| Date | Change | Reason |
|---|---|---|
| 2026-10-03 | §6(iii)'s acceptance band for GN's noise figure (0.5 ± 0.05) is superseded by §4's matching rule. **No hypothesis, endpoint, arm, reconstructor setting, sample size, or decision rule changes.** | Internal inconsistency in the hashed text; see below. |
| 2026-10-03 | §6(v)'s alignment tolerance ("within one pixel") was not met by BP (maximum offset 2 px); the automatic pilot gate used ≤ 3 px and passed it. **No hypothesis, endpoint, arm, reconstructor setting, sample size, or decision rule changes.** | Gate looser than the registered text; see below. |

**Both entries were written on 2026-10-03 before any cell of the §8 step-5 matrix had been read.** At the time of writing, the scoring had produced per-seed files on the Mac mini but no number from any of them had been opened, printed or summarised. The PI decided both entries on the PI's own authority.

### 2026-10-03 — §6(iii) and §4 disagree on GN's noise figure

§6(iii) checks that "the noise figure of GN is 0.5 ± 0.05". That band was written when GN was to be matched to GREIT's **nominal** noise figure (0.5, the value used to build the GREIT model). Before hashing, the pre-hash compatibility check showed that GREIT's **realised** noise figure on the common reference frame is 0.602, and §4 was rewritten to match GN to that realised value (PI decision 2026-09-26, recorded in §4: "GREIT's realised NF on a common reference frame, not the nominal 0.5"). §6(iii) was not updated. GN's realised noise figure is 0.607 (hp 0.0016), which satisfies §4 (|0.607 − 0.602| = 0.005) and lies outside §6(iii)'s band. §4 governs; the GN reconstructor used throughout is the one §4 describes, unchanged. BP's noise figure (0.831) is recorded, as §6(iii) requires.

The automatic pilot gate (`tools/recon_pipeline_air.sh`, lines 24–37) did not test noise figures at all; they were recorded by `gen_recon_full.m` and transcribed into `results_recon/pilot_checks.json`.

### 2026-10-03 — BP's raster alignment exceeds §6(v)'s one-pixel tolerance

§6(v) requires that the single-organ BP reconstructions peak at the same pixel locations as the GREIT ones, within one pixel, on ten test frames. Measured on the heart target (`results_recon/pilot_checks.json`, `heart_peak_offset_vs_greit_*`): GN's maximum offset is 1 px (all ten frames (1, 0) in row, column); BP's is 2 px (row offset 2 px on seven of ten frames, 1 px on three; column offset 0–1 px). The automatic gate used ≤ 3 px and passed, and the pipeline proceeded to training. §6 says "any design change after the pilot is made before hashing; none after", so the BP reconstructor is not changed and nothing is retrained. BP is analysed as registered.

What this means for reading BP cells is a matter for the results interpretation, not for this entry. The offset is reported beside every BP cell in `RESULTS_RECON.md`.

### 2026-10-03 — not a deviation: scoring script fixed for bash 3.2

`tools/eval_recon_matrix.sh` used `declare -A`, which the Mac mini's bash 3.2 does not support; the 2026-09-29 run stopped at that line before scoring any cell. The two lookups were rewritten as `case` functions with the same mapping and the script was re-run on 2026-10-03. Cells, arguments, affines and seeds are unchanged; a dry run printed the same 21 `evaluate.py` invocations (12 registered cells and the 9 off-diagonal cells of §3(c); the mixed row has no diagonal, so all three of its cells are off-diagonal). The failed version is kept on the mini as `tools/eval_recon_matrix.sh.bak_20260929_bash32fail`.

## 11. Addendum (drafted 2026-10-03, AFTER the registered matrix was read; confirmed by the PI and hashed the same day, before any run it names was started)

### 11.1 What this addendum adds, and what it does not touch

**It is written after unblinding, and says so.** All twelve registered cells and the nine own-affine cells had been read (`RESULTS_RECON.md`, 2026-10-03) when this text was drafted. It therefore cannot have the standing of §§1–9. What it can do is fix, before the new runs exist, what they are, how they are scored and how each outcome will be read.

**Untouched.** The verdicts under hash `4b4c7a6d…` stand as recorded: R1-GN and R1-BP falsified; all six R3 cells falsified; all three M1 cells falsified. No registered cell is re-scored, re-tested or re-described by this addendum. The registered M1 row is reported as it is, with the scale fact beside it.

**Added.** One new training row, **mixed-ps** (pooled training with a per-source affine), tested by **M1′** and described by **M2′** and **M3′**; and one exploratory re-scoring of the six R3 cells, **E1** (PI decision 2026-10-03: included), with no verdict.

### 11.2 Why: the registered mixed row did not pose §7's question

§7 specified "one dataset-wide affine estimated on the pooled training split". §4 says nothing about the reconstructors' output scales and §6 did not check them. Measured after scoring (`results_recon/scale_check.json`): GREIT's image amplitude is 161 times GN's and 188 times BP's. Under the pooled affine a GN or BP frame varies by 1/132 or 1/156 of what a GREIT frame does, and its heart target by 1/346 or 1/318 (`results_recon/figs/mixed_affine_inputs.png`). With an L1 loss, 5,760 of the 8,640 training frames therefore contributed almost nothing to the gradient, and at evaluation the network was shown near-constant GN and BP inputs. The registered mixed row is, in effect, GREIT training with two thirds of the frames near-constant; mixed→GN and mixed→BP (heart DSC 0.40–0.45, seed SD 0.25–0.30) measure a network's response to an input it cannot see. That is a property of the registered design, not a coding error, and the registered verdicts are not revised because of it. But the question §7 asked — whether a training distribution spanning reconstructors buys reconstructor tolerance at matched parameter count, and whether the branch adds anything on top — was not posed.

A second fact, found on 2026-10-03 with `tools/recon_shift_inputs.py` (seed 0 only; it computes no DSC and no D − B_wide contrast; `results_recon/shift_inputs.json`, `results_recon/figs/shift_inputs_D_seed0.png`), bears on how the new row is scored. `evaluate.py`'s own-affine path, used for §3(c), feeds the network with the evaluation set's affine **and** undoes the output with it. A network trained on X places its background at −mu_X/sd_X in normalised units; undone with Y's affine, the background is no longer at zero in image units, and the quarter-amplitude set, which is not shift-invariant, takes in the background. On seed 0 the predicted heart mask of D covers 81% (GN→GREIT), 69% (BP→GN), 54% (BP→GREIT) and 47% (GN→BP) of the field of view against targets of 9–17%. §3(c) therefore does not isolate a scale mismatch as it was meant to. The same seed-0 pass shows that in the registered R3 cells that cross GREIT the input is degenerate (GREIT→GN, GREIT→BP: median within-frame SD 0.005 against 0.82 on the diagonal) or 131–154 times over-range (GN→GREIT, BP→GREIT); only GN→BP and BP→GN present the network with an input in its trained range. How this bears on reading R3 is a matter for the results interpretation; it is recorded here because it constrains the design below.

### 11.3 The mixed-ps row

**Data.** `data/v2_full_snr20_mixed_ps/dataset.mat`, built by `tools/build_mixed_dataset_ps.py` (new; `build_mixed_dataset.py` and `train_arms.py` are not edited). Each source's `recon_mixed`, `recon_lung` and `recon_heart` are standardised with that source's **own** training-split affine — the (mu, sd) its single-reconstructor row was trained with, computed by the same `train_arms.normalise` — and then concatenated exactly as the registered pooled set was: the same 3,600 geometries and noise seeds per source, the same splits (8,640 / 1,080 / 1,080), the same frame-to-source map. `train_arms.py` then estimates its one dataset-wide affine on this file as it always does; that affine is the identity up to rounding (§11.4).

Why a per-source affine and not a common rescaling or a per-frame normalisation. It makes every frame of the pooled training set identical, to rounding, to the frame the corresponding single-reconstructor row was trained on, so that mixed-ps→Y and Y→Y differ **only** in the composition of the training set — which is the comparison M2 was registered to make. Per-frame normalisation is excluded by `train_arms.normalise` ("never per-image"). The cost is stated in §11.7: the normalisation is source-aware.

**Training.** `train_arms.py --arms D B_wide --seeds 0..29 --prereg PREREGISTRATION_RECON.md --out runs_recon_mixed_ps`, every constant unchanged, on the same Mac mini, two processes (seeds 0–14, 15–29), `run_meta.json` carrying this file's addendum-state hash and the dataset's hash. **n = 30, fixed here and not revised.** 60 runs.

**Scoring.** For Y ∈ {GREIT, GN, BP}: `evaluate.py --data <Y>/dataset.mat --runs runs_recon_mixed_ps --primary D B_wide --channel heart` with **no** `--affine-from-data`, so input and output both use Y's own training-split affine. For this row that path is zero-consistent, because Y's affine is the one its frames were trained under. Endpoint unchanged: heart-channel DSC on the quarter-amplitude set in image units, test split, seeds 0–29, 20 dB.

### 11.4 Gate before training (run 2026-10-03 on the Air; data only, no arm trained, no checkpoint opened, no contrast computed)

`tools/recon_mixed_ps_gate.py` → `results_recon/mixed_ps_gate.json`, `results_recon/figs/mixed_ps_inputs.png`. Dataset SHA-256 `ba879fd1…0014c2ebf`.

| check | criterion | measured |
|---|---|---|
| pooled affine is the identity | \|mu\| ≤ 1e-3 and \|sd − 1\| ≤ 1e-3 | mu 1.1e-07, sd 0.99999982 |
| input equals the single-source row's input | max abs difference ≤ 1e-3 (normalised units) on the test split | GREIT 1.4e-06, GN 1.9e-06, BP 1.4e-06 |
| fields of view identical across sources and the pooled file | exact | identical |
| inputs on one scale | median within-frame SD, largest over smallest ≤ 2 | 0.817 / 0.847 / 0.813 → 1.04 |
| heart targets on one scale | training-split SD, largest over smallest ≤ 2 | 0.144 / 0.084 / 0.099 → 1.71 |
| quarter-amplitude set survives the round trip | mean heart coverage of the test targets unchanged | 0.0863 / 0.1649 / 0.1330, identical before and after |
| the picture | the three sources are visibly comparable after the affine | `mixed_ps_inputs.png`, inspected |
| scoring script | dry run under the mini's bash 3.2 prints exactly the three invocations of §11.3 | **to be done on the mini before training starts; training does not start if it fails** |

All data checks pass. The heart-target ratio of 1.71 means a GREIT frame weighs up to 1.7 times a GN frame in the L1 loss; this is inside the criterion, is not corrected, and is reported.

### 11.5 Hypotheses, rules and fixed interpretations

**M1′ (tested), three cells (mixed-ps→GREIT, mixed-ps→GN, mixed-ps→BP).** The R1 rule, unchanged: confirmed if mean DSC_heart(D) − DSC_heart(B_wide) exceeds B_wide's seed-to-seed SD in that cell **and** Wilcoxon signed-rank (two-sided, normal approximation with continuity correction) over the thirty paired seeds gives p < 0.05; falsified if either fails or the sign is reversed. Cells are reported individually and never pooled.

**Expectation, stated before the runs.** Falsified in all three cells, with a difference of the size seen on the three diagonals (+0.27 to +0.63 points) and below the floor. The power table of §5 applies unchanged: n = 30 does not power a below-floor effect and is not meant to.

**Interpretations, fixed now.**
- M1′ falsified in a cell: under pooled, source-aware-normalised training the branch does not clear the floor on that reconstructor; the matched-training null extends to a training distribution that spans the three reconstructors.
- M1′ confirmed in a cell: the branch adds something on top of pooled training on that reconstructor. This would be a result from a post-unblinding addendum and is reported as such; it changes neither M1's record nor R1's, and the imaging paper may not lead with it.
- Neither outcome changes R1, R3 or M1.

**M2′ (reported, not tested), per Y and per arm:** DSC_heart(mixed-ps→Y) − DSC_heart(Y→Y), paired by seed, 95% percentile bootstrap CI (100,000 resamples, seed 20260904). The cost of pooling relative to specialising.

**M3′ (reported, not tested), per (X, Y), X ≠ Y, per arm:** DSC_heart(mixed-ps→Y) − DSC_heart(X→Y), the latter being the registered cell, paired by seed, same CI. How much of the off-diagonal penalty pooling removes. Because four of the six registered X→Y cells present a degenerate or over-range input (§11.2), M3′ in those cells is reported with that note and is not described as the size of a "reconstructor shift".

M2′ and M3′ carry no verdict. What the paper may say from M1′–M3′ is what §9 allowed: the ordering of three remedies for a reconstructor change at matched parameter count — the branch, retraining on the target reconstructor, and pooled training — on the same seeds and geometries, with the pooled remedy now being the mixed-ps row and labelled as an addendum.

**A validity rule, fixed in advance so that it is not decided after the fact.** The mixed-ps row is read if the gate of §11.4 passes, whatever the DSC values turn out to be. No cell is set aside on the grounds of its outcome.

**E1 (exploratory; PI decision 2026-10-03: included).** The six R3 cells re-scored on the existing checkpoints with the input normalised by the evaluation set's affine and the output undone with the **training** set's affine, which keeps the predicted background at zero and is what §3(c) was meant to be. It needs one new flag in `evaluate.py` (not a frozen file), whose default leaves every existing path unchanged and is shown to reproduce one registered cell bit for bit. Reported per cell as Δ and the difference of differences with the R3 bootstrap, **labelled exploratory, with no verdict.** It cannot confirm R3 in any cell and cannot be cited as support for a shift-tolerance claim; a secondary analysis does not rescue a falsified primary. No training; about 20 minutes of scoring, done on the mini together with the M1′ scoring.

### 11.6 Order of operations and cost

1. PI confirms this text (done 2026-10-03, E1 included); the text is appended to `PREREGISTRATION_RECON.md`; the addendum-state hash goes into `PREREGISTRATION_RECON.sha256` as a third line (the registered hash `4b4c7a6d…` still governs §§1–9; the deviation-state hash `3fdc703d…` is kept).
2. The dataset and the two new scripts are copied to the mini; the dataset hash is checked against §11.4; the scoring dry run of §11.4 is done.
3. Training is started by hand when the mini is free (another project's training occupies it until about 2026-10-05; the two are not run concurrently; PI decision 2026-10-03: no automatic start). 60 runs on an 8,640-frame training split, ≈ 40 h; checkpoints ≈ 2.4 GB.
4. Scoring (three cells, plus the six E1 cells), then `RESULTS_RECON.md` gains a new section for M1′, M2′, M3′ and E1, in that order, **before** the results interpretation is completed and before any manuscript text. Existing sections are not edited.
5. Adversarial review (`academic-paper-reviewer`) after step 4, not before.

### 11.7 What this addendum does not licence

Any re-reading of M1 as anything other than falsified; any claim that pooled training is "reconstructor-agnostic" without the qualification that the normalisation is source-aware (the affine applied at deployment is the one belonging to the reconstructor in use, which is always known); anything at 40 dB or any noise level other than 20 dB; pooling more than these three reconstructors; learned reconstructors; any reconstructor ranking; any statement that E1 supports R3.


## 12. Second addendum (drafted 2026-10-11, AFTER the section-11 results were read; to be confirmed by the PI and hashed before any run it names is started)

### 12.1 Standing, and what this addendum does not touch

**Written after the section-11 results were read, and says so.** The three mixed-ps cells (M1′), M2′, M3′ and E1 had been read (`RESULTS_RECON.md` §9–§10, interpretation parts 1–2, five-seat review and two revision rounds, 2026-10-10/11) when this text was drafted. It has the standing of §11, not of §§1–9: it fixes, before the new runs exist, what they are, how they are scored and how each outcome will be read.

**Untouched.** Every verdict under hashes `4b4c7a6d…` (R1, R3, M1) and `0060eedf…` (M1′) stands as recorded. No registered or addendum cell is re-scored.

**Added.** Three training rows, **loro-GREIT, loro-GN, loro-BP** (leave-one-reconstructor-out: pooled training on two reconstructors with a per-source affine, evaluated on the third, which the network never saw), tested by **L1** (a pre-registered equivalence margin) and **L2** (the R1 rule), described by **L3′**.

### 12.2 Why

§11 established that pooled training with a per-source affine could not be ordered against retraining on the deployed reconstructor (M2′: differences −0.08 to +0.36 points, CIs within [−0.32, +0.50]). Every evaluation reconstructor was inside the training pool, so that result is in-pool multi-source learning, and the interpretation (part 2 §11.2) and the boundary clause (§三, 2026-10-11 note) restrict the deployment recipe to "in-pool reconstructors only; no reconstructor-agnostic claim". The five-seat review (R3-W2, R3-Q1) named the missing cell: a reconstructor the pool never contained. This addendum runs it. It is the one addition that can turn the recipe from a scope statement into a tested generalisation claim; it is also the addition most likely to fail, which is why its margin is fixed now.

### 12.3 The rows

**Data.** `data/v2_full_snr20_loro_{greit,gn,bp}/dataset.mat`, built by `tools/build_loro_dataset_ps.py` (new; `build_mixed_dataset_ps.py`, `train_arms.py` and `evaluate.py` are not edited). Row loro-Y pools the two reconstructors other than Y, each standardised with its **own** training-split affine exactly as §11.3 does, then concatenated: the same 3,600 geometries and noise seeds per source, the same splits (5,760 / 720 / 720), the same frame-to-source map. Y's frames are absent from training and validation. `train_arms.py` estimates its one dataset-wide affine on this file as always; that affine is the identity up to rounding (§12.4).

**Training.** `train_arms.py --arms D B_wide --seeds 0..29 --prereg PREREGISTRATION_RECON.md --out runs_recon_loro_<Y>`, every constant unchanged, on the same Mac mini, two processes (seeds 0–14, 15–29), the three rows in sequence, `run_meta.json` carrying this file's section-12 addendum-state hash and the dataset's hash. **n = 30 per row, fixed here and not revised.** 180 runs.

**Scoring.** For each row loro-Y: `evaluate.py --data <Y>/dataset.mat --runs runs_recon_loro_<Y> --primary D B_wide --channel heart` with **no** `--affine-from-data`: input and output use Y's own training-split affine. This is the deployment path of §11.7's source-aware caveat — the affine of the reconstructor in use is always known, but **the network has never seen that reconstructor's images**. For the two in-pool reconstructors X of each row the same call with `--data <X>` is also run and reported, not tested (a two-source in-pool reference, `results_recon/loro_<Y>__<X>`). Endpoint unchanged: heart-channel DSC on the quarter-amplitude set in image units, test split, seeds 0–29, 20 dB. Nine `evaluate.py` invocations in all (`tools/eval_recon_loro.sh`).

### 12.4 Gate before training (run 2026-10-11 on the Air; data only, no arm trained, no checkpoint opened, no contrast computed)

`tools/recon_loro_gate.py` → `results_recon/loro_gate.json`, `results_recon/figs/loro_inputs.png`. Dataset SHA-256: loro-GREIT `08e1b702…f10b6dae1`, loro-GN `9ea5af3e…fa6486273`, loro-BP `3f29b53c…02e3f3e0`.

| check | criterion | measured (loro-GREIT / loro-GN / loro-BP) |
|---|---|---|
| pooled affine is the identity | \|mu\| ≤ 1e-3 and \|sd − 1\| ≤ 1e-3 | mu −3.4e-08 / −2.8e-07 / −4.9e-08; sd 1.00000000 / 0.99999911 / 0.99999946 |
| in-pool input equals the single-source row's input | max abs difference ≤ 1e-3 on the test split | ≤ 9.5e-07 / ≤ 5.7e-06 / ≤ 4.3e-06 |
| held-out input (own affine) on the pool's scale | within-frame SD, largest over smallest over pool + held-out ≤ 2 | 1.04 / 1.04 / 1.04 |
| fields of view identical | exact | identical |
| the picture | pool frames and held-out frame visibly comparable | `loro_inputs.png`, inspected |
| scoring script | dry run on the mini's bash 3.2 prints exactly the nine invocations of §12.3 | **to be done on the mini before training starts; training does not start if it fails** |

### 12.5 Hypotheses, rules and fixed interpretations

**L1 (tested), three cells (loro-GREIT→GREIT, loro-GN→GN, loro-BP→BP), with a margin fixed here.** Quantity: DSC_heart(B_wide, loro-Y→Y) − DSC_heart(B_wide, mixed-ps→Y), paired by seed index (seed s against seed s, as M2 and M2′ were paired), 95% percentile bootstrap CI over the thirty pairs (100,000 resamples, seed 20260904). **Confirmed if the whole CI lies within [−1.0, +1.0] Dice points; falsified otherwise.** Cells are reported individually and never pooled. The same quantity for D is reported beside it, not tested.

Why B_wide: it is the control arm and the practitioner's default; the branch is tested separately by L2. Why ±1.0 point: it is larger than every registered floor (0.17–0.66 points), so a loss inside it is below what the registered rules can resolve, and it is an order of magnitude below the smallest no-retraining loss in an in-range cell (11.7 points, §9(c)) and below every E1 loss (≥ 19 points, §9(d)); a margin chosen after the runs would have been a repeat of the §8.2 error the review caught (interpretation part 2, caveat 1; RESEARCH_PRIMER 二.4b). The margin is a design choice; it is not derived from a power calculation, and §5's power table does not apply to it.

**L2 (tested), three cells, the R1 rule unchanged:** confirmed if mean DSC_heart(D) − DSC_heart(B_wide) on loro-Y→Y exceeds B_wide's seed-to-seed SD in that cell **and** Wilcoxon signed-rank (two-sided, normal approximation with continuity correction) over the thirty paired seeds gives p < 0.05; falsified if either fails or the sign is reversed.

**Expectation, stated before the runs.** L1: falsified in loro-GREIT (GREIT's spatial structure and amplitude differ most from GN and BP; E1 put GN- and BP-trained networks at 0.66–0.76 on GREIT), uncertain in loro-GN and loro-BP (E1's single-source GN↔BP crossings gave 0.63–0.77; a two-source pool may do better, but the margin is tight). The honest expectation is three falsifications with losses of 5–30 points relative to mixed-ps; the value of the rows is the per-reconstructor magnitude. L2: falsified in all three cells, with a difference of the size seen in every matched cell so far (−0.02 to +0.63 points), below the floor.

**Interpretations, fixed now.**
- L1 confirmed in a cell: pooled training with a per-source affine generalises, at the 1-point level and in this simulation, to that conventional reconstructor without ever seeing it; the imaging paper's deployment recipe may drop "in-pool only" **for that reconstructor** and must still say "three conventional reconstructors, 20 dB, registered cylinder". L1 falsified in a cell: the recipe stays in-pool only for that reconstructor, and the loss is reported as the cost of deploying on an unseen reconstructor.
- L2 confirmed in a cell: the branch adds something on an unseen reconstructor; a result from a second post-unblinding addendum, reported as such, changing neither R1, M1 nor M1′, and the imaging paper may not lead with it. L2 falsified: the matched-training null extends to a reconstructor the network never saw.
- Neither outcome changes R1, R3, M1 or M1′.

**L3′ (reported, not tested), per Y and per arm:** DSC_heart(loro-Y→Y) − DSC_heart(Y→Y) (the cost of never seeing Y relative to specialising on it) and DSC_heart(loro-Y→Y) − DSC_heart(X→Y) for the two registered no-retraining cells X→Y (how much two-source pooling removes of the single-source off-diagonal penalty; the four cells crossing GREIT carry the §11.2 degenerate/over-range note), paired by seed, same CI. The in-pool references `loro_<Y>__<X>` are reported as absolute DSC with seed SD.

**A validity rule, fixed in advance.** The three rows are read if the gate of §12.4 passes, whatever the DSC values turn out to be. No cell is set aside on the grounds of its outcome.

### 12.6 Order of operations and cost

1. PI confirms this text (three rows or fewer — the choice of rows is fixed here before hashing); the text is appended to `PREREGISTRATION_RECON.md`; the addendum-state hash goes into `PREREGISTRATION_RECON.sha256` as a fourth line (the registered hash `4b4c7a6d…` still governs §§1–9; `0060eedf…` still governs §11).
2. The three datasets and the two scripts (`tools/run_recon_loro_mini.sh`, `tools/eval_recon_loro.sh`) are copied to the mini; dataset hashes are checked against §12.4; the scoring dry run of §12.4 is done on the mini.
3. Training is started by hand when the mini is free. Three rows × 60 runs on a 5,760-frame training split: the §11 row (8,640 frames) took 58 h wall for 60 runs, so about 39 h per row, **about 5 days for the three**; checkpoints ≈ 2.4 GB per row (mini has 27 GB free).
4. Scoring (nine cells), then `RESULTS_RECON.md` gains a new section for L1, L2, L3′ in that order (existing sections untouched); the interpretation gains a new part (patch round, re-anchored); scoped review after that.
5. The rows are not run concurrently with any other training on the mini.

### 12.7 What this addendum does not licence

Any re-reading of M1, M1′ or R3; any claim beyond the three conventional reconstructors named, in particular "reconstructor-agnostic" without the clause "for the three conventional reconstructors tested, with the deployed reconstructor's own affine"; anything at 40 dB; learned reconstructors; any reconstructor ranking; any use of L3′ or the in-pool references as a verdict.
