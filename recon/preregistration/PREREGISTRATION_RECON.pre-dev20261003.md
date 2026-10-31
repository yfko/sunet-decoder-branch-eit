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

(none yet)
