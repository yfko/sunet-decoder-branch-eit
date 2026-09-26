# Pre-registration — does a divided branch improve lung EIT segmentation?

**Registered 2026-08-28, before any arm was trained.**

The computation run before this file was fixed is exactly: the 50-sample pilot
of `tools/gen_dataset.m` (which verified its three `ASSUMPTION` markers, one of
which was falsified and corrected), the full 3600-sample dataset generation, and
a timing measurement of one partial epoch. No arm was trained to completion, no
metric was computed on any arm, and no contrast was evaluated. The pilot record
is `Nov142025/ARS_Review_2026-08-27/10_Pilot_Results.md`.

Once results exist this text is not edited — corrections go under
**Deviations** (§8).

The SHA-256 of this file is written into `runs/run_meta.json` by
`tools/train_arms.py` (field `prereg_sha256`), following the convention of
`../EIT_noise_geometry/PREREGISTRATION.md`. A later edit is therefore
detectable.

---

## 1. Why this study is a rebuild, not a first attempt

This is stated here so that it cannot later be presented as anything else.

A manuscript making the claim below was submitted five times between 2022 and
2025 and rejected, most recently by Scientific Reports on 30 October 2025 and by
IEEE Sensors Journal in November 2025. During the audit that followed
(`Nov142025/ARS_Review_2026-08-27/`), the results supporting that claim were
found not to be interpretable:

- the three compared models solved **three different tasks** on three different
  datasets, with epoch budgets of 1, 50 and 30, different loss weightings, and
  data augmentation applied only to the baseline;
- the heart target for 1200 of ~2800 training samples was **a single image
  replicated**, so one output head was regressing a constant;
- every image was **min–max normalised per frame** and written to JPEG, which
  removed the conductivity scale that the reported MAE was supposed to measure;
- the reported DSC came from a 37-line script operating on one example image,
  not from a pass over the test set.

Those results are withdrawn. No number from them is carried forward, and none
is used to motivate a hypothesis here. **The question below has therefore never
actually been tested**, which is why a directional hypothesis is still
legitimate rather than a prediction of a known answer.

Relationship to prior published work is disclosed in the manuscript: this study
follows Ko & Cheng 2021 *Physiol. Meas.* (U-Net lung segmentation in EIT) and
Ko & Cheng 2021 *PLOS ONE* (semi-Siamese U-Net, lung/heart separation). The
increment over the latter is the controlled comparison specified here, which
that paper did not perform.

## 2. The claim being tested

The architecture under test splits the U-Net expanding path into two decoders,
so that one head predicts the pure-lung reconstruction and the other the pure
heart. The claim in the withdrawn manuscript was that this split — and splitting
*early*, at the bottleneck rather than at the terminal block — is what improves
segmentation.

That claim was never separable from two duller explanations. A second decoder
roughly doubles decoder parameters, and a second supervised target is a
well-known regulariser. Either alone predicts the observed direction.

**H1 (primary, directional).** At matched parameter count and matched
supervision, splitting the decoder improves lung segmentation:

    DSC(D) > DSC(B_wide)

**H2 (position).** At matched parameter count, splitting early beats splitting
late:

    DSC(D) > DSC(C_wide)

**H3 (supervision).** The auxiliary heart target improves the lung output even
without branching:

    DSC(B) > DSC(A)

**H4 (the withdrawn comparison, recorded for transparency).** The contrast the
rejected manuscript actually made, `D` against `A`, is expected to favour `D`.
It is reported but carries no weight, because it confounds branching, capacity
and supervision. It is registered here so that a positive D−A result cannot
later be presented as support for H1.

## 3. What falsifies each hypothesis

Stated numerically, before the data exist. Primary endpoint: **lung-channel DSC
on the quarter-amplitude set, test split, mean over 10 seeds.**

| | confirmed if | falsified if |
|---|---|---|
| **H1** | mean DSC(D) − DSC(B_wide) exceeds the seed-to-seed SD of B_wide, **and** Wilcoxon signed-rank over the 10 paired seeds gives p < 0.05 | the difference is within B_wide's seed SD, or p ≥ 0.05, or the sign is reversed |
| **H2** | same rule applied to D − C_wide | same |
| **H3** | same rule applied to B − A | same |
| **H4** | — | — (reported, not tested) |

The effect-size clause is what carries the argument; the test guards against a
difference that is consistent across seeds but trivially small.

**Attainability check.** On *n* paired seeds the smallest two-sided p a Wilcoxon
signed-rank test can return is 2/2ⁿ — 0.0625 at n = 5, 0.00195 at n = 10. A rule
at α = 0.05 is unsatisfiable with 5 seeds. This is why n = 10, and
`tools/evaluate.py` warns if the floor exceeds α.

**If H1 is falsified**, the finding is that the divided branch buys nothing that
an equally-sized single decoder does not, and the manuscript says so — including
in its title, which can no longer assert the importance of the divided-branch
structure. A parameter-matched negative result on decoder splitting is a
contribution this field does not currently have, and it will be written up as
the primary result rather than buried. This sentence exists so that the outcome
cannot later be reported as though something else had been expected.

**If H1 is confirmed but H2 is falsified**, branching helps and position does
not, and every claim about the *timing* of divergence is dropped.

## 4. Design

Five arms, differing **only** in decoder topology and width. Encoder, block
structure, skip connections, normalisation and initialisation are shared.

| Arm | Decoder | Outputs | Parameters |
|---|---|---|---|
| A | 1 × base | 1 (lung) | 7,762,465 |
| B | 1 × base | 2 (lung, heart) | 7,762,498 |
| B_wide | 1 × width 1.5312 | 2 | 10,743,738 (−0.62% vs D) |
| C | 2, split at the last block | 2 | 7,798,498 |
| C_wide | 2, split at the last block, width 1.5312 | 2 | 10,817,706 (+0.06% vs D) |
| D | 2, split at the bottleneck | 2 | 10,811,298 |

Counts are from `python tools/arms.py` and are fixed by that file. Width
multipliers are solved by bisection to match D and are quantised to multiples of
8 channels, so the residual mismatch is reported rather than claimed to be zero.

**Data.** `tools/gen_dataset.m`, N = 3600 geometries. `r_lung` ~ U(0.30, 0.60)
and `r_heart` ~ U(0.15, 0.30) are drawn **independently** per sample, with
centre jitter ±0.05, so neither output head can be solved by predicting a
constant. Phantom parameters are inherited unchanged from
`../EIT_noise_geometry/src/p2_config.m`: 16 electrodes, σ_lung 0.5, σ_heart 2.0,
background 1.0 S/m. Reconstruction is GREIT at 64×64.

**The `r_heart` lower bound is 0.15, not the 0.10 of the withdrawn manuscript.**
At 0.10 the heart occupies ~27 elements of the 161,714-element forward mesh,
below the discretisation limit for a recognisable sphere; at 0.15 it occupies
~91. The departure from the manuscript's stated range is deliberate and is
recorded here rather than discovered later. It is disclosed in the Methods.

**Inclusions are painted, not meshed.** A Netgen CSG mesh conforming to the
inclusions must be rebuilt per geometry, and one such build exceeded 31 minutes
on this machine — 3600 of them is not runnable. Inclusions are therefore painted
onto a plain cylinder mesh built once, the `cyl_paint` mode of
`../EIT_noise_geometry/src/p2_build_geom.m`. That project measured the cost of
the substitution at the cylinder reference geometry: painted and CSG inclusions
of matched volume gave identical component selections and shape deformation
agreeing within 0.015 (`RESULTS_AXIS2.md`, "Painting against meshing").

**Forward and reconstruction meshes are separate, deliberately.** Painting
removes the mesh difference CSG gave for free, so the forward model is built at
`maxsz` 0.10 (161,714 elements) against the GREIT model's 0.2. This is the
inverse-crime guard and is not optional.

**Field of view.** GREIT reconstructs a circular FOV into a square raster, so
868 of 4096 pixels carry no data. Every loss, normalisation statistic and metric
is restricted to the 3228-pixel FOV mask.

**Splits.** 80/10/10 by *geometry*, not by frame, so no geometry appears in both
training and test. The split is fixed by seed 20260828 and is identical for
every arm and every training seed.

**Targets.** The pure-lung and pure-heart GREIT reconstructions, as float. The
true conductivity field on the same raster is also stored and used only in a
clearly-labelled secondary analysis; the primary endpoint is against the
reconstruction.

## 5. Outcomes

**Primary**: lung DSC (quarter-amplitude set), test split, mean ± SD over 10
seeds, for each arm; and the three contrasts of §3.

**Secondary, reported for every arm and both channels**: MAE in the
reconstruction's own units, IoU, sensitivity, specificity, ASSD, Hausdorff-95,
per-image distributions with bootstrap 95% CIs, parameter count, FLOPs and
inference time per frame.

Secondary outcomes are secondary. A significant result on a secondary metric
does not rescue a falsified H1, and will not be reported as though it did.

**Not reported**: pixel accuracy, and the `1 − MSE` quantity used as "accuracy"
in the withdrawn manuscript. Both saturate near 1 on these images and cannot
discriminate between arms.

## 6. What is fixed and will not be tuned

Per-arm tuning of any item below invalidates the comparison. All are constants
in `tools/train_arms.py`.

| | |
|---|---|
| Optimizer | Adam, lr 1e-3, cosine decay to 1e-5 |
| Batch size | 16 |
| Max epochs | 200, early stopping on validation loss, patience 20, best weights restored |
| Loss | L1 on the float target, no output activation |
| Loss weights | 1.0 / 1.0 across the two heads |
| Augmentation | none. Horizontal flip is excluded permanently: it mirrors the thorax, swapping the lungs and moving the heart |
| Normalisation | one dataset-wide affine from the training split, applied unchanged to validation and test. Never per-image |
| Seeds | 0–9 |
| DSC threshold | quarter-amplitude, `|img| > 0.25·max|img|` — EIDORS `calc_hm_set(img, 0.25)`, not a threshold chosen for this study |

No architecture, hyperparameter or threshold is selected on the test split. The
test split is read once, after all 50 runs are complete.

## 7. Analyses not covered here

The measured-data arm (montreal_data_1995 and the Dräger PulmoVista recording)
and the noise/geometry sweep are **not** preregistered by this file. They follow
after the arm comparison and will be registered separately, because their design
depends on its outcome. Nothing in them may be used to revisit H1–H3.

## 8. Deviations

Any change after results exist is recorded here, dated, with its reason — never
by editing the text above.

| Date | Change | Reason |
|---|---|---|
| 2026-08-29 | **Endpoint mis-specification recorded. The primary endpoint is NOT changed.** | See below. |
| 2026-09-18 | Corresponding author's attestation of the architecture's original design intent added. **No hypothesis, endpoint, arm or analysis changes.** | See below. |

### 2026-08-29 — the primary endpoint does not match the mechanism it was meant to test

**What was found.** After the results were unblinded, the corresponding author
pointed out that in lung EIT the lung component dominates the image and the
cardiac component is suppressed — which is the entire physical motivation for a
divided branch. Measured on this study's own dataset (3600 frames, within the
field of view):

| | median peak amplitude | energy |
|---|---|---|
| Lung | 27.22 | — |
| Heart | 5.96 | — |
| ratio | **4.6×** | **56×** |

The heart carries a median of **1.7%** of the reconstruction's total energy.

The lung channel is therefore the easy half of the task by construction, and
this is the same phenomenon as the ceiling effect reported in §5 of the results:
all six arms reach ~0.994 lung DSC because lung segmentation needs no
architectural help. The mechanism the manuscript argues — that a second branch
specialises in the *weaker* component — predicts an effect on the **heart**
channel, not the lung.

**Why the endpoint was chosen as it was.** §3 registered lung DSC because the
withdrawn manuscript's title and its Table 1 both report lung. That followed the
manuscript's stated *outcome* rather than its stated *mechanism*, which are
inconsistent with each other in the original. The choice was made before any
data existed, and the physical argument above was equally available at that
time. It was simply not used.

**What is NOT being done.** The primary endpoint is **not** switched to the
heart channel. The argument for heart pre-dates the data; invoking it only after
seeing that the heart contrast looks more favourable would be outcome
switching, which is precisely what this file exists to prevent. The registered
hypotheses stand as tested and as falsified.

**It would also change nothing.** On the heart channel, D − B_wide = +0.355
percentage points, 95% CI [−0.153, +0.864], p = 0.232. The heart contrast is
null as well.

**What follows instead.** The heart result is reported as the registered
secondary outcome, together with the observation that this study was
**underpowered for it**: the observed paired effect is Cohen's dz = 0.500, and
n = 10 seeds gives roughly 29% power. Detecting an effect of that size at 80%
power requires n ≈ 34 seeds. The heart p-value is therefore evidence of
insufficient power, not evidence of absence — a distinction the manuscript must
state explicitly.

The successor study (already excluded from this one by §7) will preregister
**heart-channel performance as its primary endpoint**, on a task that is not at
ceiling (measurement noise, realistic thoracic geometry, and/or the measured
PulmoVista and montreal_data_1995 arms), powered on dz = 0.500 unless the harder
task is expected to amplify it.

### 2026-09-18 — the architecture was designed for the heart, attested by its author

**This changes nothing that was registered.** The primary endpoint of this study
remains the lung channel, still not switched, and every hypothesis stands as
tested and as falsified. What is added is a fact that was available in 2026-08
and was not obtained: first-hand testimony about what the architecture was built
to do.

**The attestation.** Yen-Fen Ko, corresponding author of the present work and
**the original author of the semi-Siamese U-Net**, states that the design was
created for **cardiac** segmentation — specifically, simultaneous heart and lung
segmentation — on the grounds that the lung is already comparatively easy to
reconstruct and to learn, and therefore is not what the architecture was
addressing.

**Why this is stronger than the argument recorded above on 2026-08-29.** That
entry inferred the correct endpoint from measured amplitudes: the lung dominates
the reconstruction, the cardiac component is suppressed, so a branch that
specialises in the weaker component predicts an effect on the heart. That is an
inference from this study's own data. The attestation is direct evidence of
design intent from the person who made the design, and it reaches the same
conclusion by a route that does not depend on this dataset at all.

**What it explains.** The 2026-08-29 entry noted that the withdrawn manuscript's
stated outcome and its stated mechanism "are inconsistent with each other in the
original" and left that inconsistency unexplained. It is now explained. The
manuscript is titled for lung segmentation and its Table 1 reports lung, while
its mechanism section argues about cardiac impedance amplitudes (citing Graf &
Riedel) and claims the second branch "specialises in learning the weaker
conductivity changes". The architecture was built for the heart; the paper was
written around the lung. The mis-specification recorded here therefore
originates in the withdrawn manuscript's own framing, which this preregistration
followed — it reported the easy half of the task while its contribution was
aimed at the hard half.

**Consequences, none of them retrospective.**

* The successor study (`PREREGISTRATION_HEART.md`, registered 2026-08-29, hash
  `2f2e1a0b946f2748…`) is not merely a more sensitive endpoint. It is the first
  test of the problem the architecture was designed to solve.
* This study keeps its status: a registered, falsified result on an endpoint that
  did not match the mechanism, reported as such. That record is the reason the
  successor study could be registered prospectively rather than reached by
  outcome switching.
* The exact reference for the original semi-Siamese U-Net is to be pinned when
  the manuscript is drafted, and verified through the mandatory citation check
  rather than asserted here.

  > *Added 2026-09-19, the sentence above left standing.* Pinned and verified
  > earlier than expected. The original is **Ko Y F and Cheng K S 2021
  > Semi-Siamese U-Net for separation of lung and heart bioimpedance images: A
  > simulation study of thorax EIT *PLoS One* 16 e0246071**, doi
  > `10.1371/journal.pone.0246071`, PMID 33529234. Every field was fetched from
  > Crossref and PubMed by `tools/cite.py` and none was typed, per
  > MANUSCRIPT_RULES R12d; the per-entry check table is
  > `refs/prior_works_table.md`. No retraction or correction is recorded
  > against it.
