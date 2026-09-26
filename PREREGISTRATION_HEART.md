# Pre-registration — does a divided branch recover the *suppressed* component?

**Registered 2026-08-29, before any arm of this study was trained.**

The computation run before this file was fixed is exactly: the SNR pilot of §7
(five 300-geometry datasets at 60–20 dB, plus 15 and 10 dB; arm B only, one seed
per level), the heterogeneity pilot (two 300-geometry datasets, arm B only), the
confirmation pilot recorded in §7 (900 geometries, arm B only, three seeds), the
full 3600-geometry dataset `data/v2`, and machine benchmarks that train on
synthetic data. **No arm other than B has been trained on any of it, and no
contrast between arms has been computed.**

Every pilot's purpose was to characterise the task, and each one changed the
design before this text was fixed — the SNR sweep, the switch to heterogeneous
conductivity, the correction of the §7 selection rule from median to mean, and
the sample size in §6. That is what pilots are for, and it is why they precede
registration rather than follow it.

Once results exist this text is not edited — corrections go under
**Deviations** (§8).

**Relationship to the first study.** `PREREGISTRATION.md` (registered
2026-08-28, SHA-256 `eebf21a2…`) tested the same six architectures with
**lung**-channel DSC as its primary endpoint, and falsified all four of its
hypotheses. Its §8 records why that endpoint was mis-specified: in lung EIT the
lung component dominates and the cardiac component is suppressed, so the
mechanism the architecture claims — a second branch specialising in the weaker
component — predicts an effect on the **heart** channel.

That study was also underpowered where it mattered. Its heart contrast measured
Cohen's dz = 0.500 — a medium effect — at n = 10 seeds, giving roughly 29%
power. Its heart p-value was evidence of insufficient n, not of absence.

The primary endpoint of that study was **not** switched after unblinding. This
is a separate, prospectively registered study that tests the mechanism on the
endpoint the mechanism is about, on a task that is not at ceiling. Both studies
are intended for **one manuscript**, reported in order.

---

## 1. The measurement that motivates this study

From the first study's own dataset (3600 frames, within the field of view):

| | median peak amplitude | ratio |
|---|---|---|
| Lung reconstruction | 27.22 | — |
| Heart reconstruction | 5.96 | **4.6×** |
| Energy | — | **56×** |

**The heart carries a median 1.7% of the reconstruction's total energy.**

Two consequences follow, and together they define this study:

1. **The heart is the hard half of the task.** Lung segmentation reached ~0.994
   DSC in every architecture including the plain baseline — it needs no
   architectural help. Any effect of branching must live in the heart channel.
2. **The first study's task was too uniform to challenge any architecture.**
   Each sample had only six free parameters — two radii and two centres — with
   constant conductivity inside each organ. The pilot showed the consequence:
   the mean heart DSC sat at 0.991, and making the measurement noisier barely
   moved it (0.999 at 20 dB). What did move it was **heterogeneous organ
   conductivity**: mean heart DSC fell to 0.983, with a heavier tail. The task,
   not the noise level, was the binding constraint.

   *(A note on statistics, because it changed this design: an earlier draft
   judged headroom by the median per-image DSC. That statistic reads 1.0000 in
   every condition tested — more than half of all images are individually
   perfect — while the mean, which is what the hypotheses are tested on, varies
   informatively. Judging the task by the median would have rejected settings
   that discriminate perfectly well. All criteria here use the mean.)*

## 2. The claim being tested

The architecture splits the U-Net expanding path into two decoders, one per
output. The manuscript's mechanism is that the second branch "specialises in
learning the weaker conductivity changes", citing Graf & Riedel on
cardiac-related impedance amplitudes.

If that mechanism is real, then under measurement noise a branched decoder
should preserve the suppressed cardiac component better than an unbranched
decoder of the same size.

**H1 (primary, directional).** At matched parameter count and matched
supervision, under measurement noise, splitting the decoder improves *heart*
segmentation:

    DSC_heart(D) > DSC_heart(B_wide)

**H2 (position).** At matched parameter count, splitting early beats splitting
late on the heart channel:

    DSC_heart(D) > DSC_heart(C_wide)

**H3 (robustness, directional).** The advantage of branching, if any, *grows* as
SNR falls — i.e. the heart-DSC-versus-SNR curve for D degrades more slowly than
that of B_wide. This is the mechanism's sharpest prediction: a branch that
specialises in the weak component should matter most when the weak component is
most threatened.

**H4 (lung, recorded for contrast).** On the lung channel, no difference is
expected between any arms, replicating the first study under noise. Reported,
not tested.

## 3. What falsifies each hypothesis

Primary endpoint: **heart-channel DSC on the quarter-amplitude set, test split,
mean over the registered seeds, at the registered SNR (§5).**

| | confirmed if | falsified if |
|---|---|---|
| **H1** | mean DSC_heart(D) − DSC_heart(B_wide) exceeds B_wide's seed-to-seed SD, **and** Wilcoxon signed-rank over the paired seeds gives p < 0.05 | difference within B_wide's seed SD, or p ≥ 0.05, or sign reversed |
| **H2** | same rule applied to D − C_wide | same |
| **H3** | the paired difference (D − B_wide) at the lowest SNR level exceeds that at the highest, with a 95% bootstrap CI on the difference-of-differences excluding zero | the CI contains zero, or the ordering is reversed |
| **H4** | — | — (reported, not tested) |

**If H1 is falsified**, the conclusion is that decoder branching does not recover
the suppressed cardiac component better than an equally-sized single decoder,
*on a task where that component is genuinely at risk*. Combined with the first
study, that is a two-endpoint, two-noise-regime null with matched controls — a
stronger and more useful negative result than either study alone, and it will be
reported as the primary finding rather than buried. This sentence exists so that
the outcome cannot later be reported as though something else had been expected.

**If H1 is confirmed but H3 is falsified**, branching helps but not by the
mechanism claimed, and the mechanism section is rewritten accordingly.

## 4. Arms

Five arms, from `tools/arms.py`, unchanged from the first study. **Arm A is
dropped**: it has no heart head and therefore cannot be scored on the primary
endpoint.

| Arm | Decoder | Parameters |
|---|---|---|
| B | 1 × base, 2 outputs | 7,762,498 |
| **B_wide** | 1 × widened ×1.5312, 2 outputs — **capacity control** | 10,743,738 |
| C | 2, split at the last block | 7,798,498 |
| C_wide | 2, split at the last block, widened | 10,817,706 |
| **D** | 2, split at the bottleneck — **early branch** | 10,811,298 |

Primary contrast **D − B_wide**: identical parameter count (−0.62%), identical
supervision, identical data and schedule; the only difference is whether the
decoder is split.

## 5. Data and noise

Generated by `tools/gen_dataset.m` with the noise option added, using the phantom
of `../EIT_noise_geometry/src/p2_config.m` unchanged: 16 electrodes, σ_lung 0.5,
σ_heart 2.0, background 1.0 S/m, `r_lung` ~ U(0.30, 0.60) and `r_heart` ~
U(0.15, 0.30) drawn independently, centre jitter ±0.05, painted inclusions on a
`maxsz` 0.10 forward mesh, GREIT reconstruction at 64×64 on a separate `maxsz`
0.2 model. N = 3600 geometries, 80/10/10 split by geometry.

**Organ conductivity is heterogeneous**, not constant as in the first study:
σ(x) = σ₀(1 + 0.25·f(x)) with f a sum of 8 random sinusoids at correlation
length 0.60, realised coefficient of variation ≈ 0.18 (lung) and 0.14 (heart).
Real lung tissue is inhomogeneous, its absence was raised by the domain review,
and the pilot showed it is the change that actually moves the endpoint.

**Noise is applied to the measurement frame before reconstruction**, not to the
image — that is where instrument noise physically enters. Implementation:
`../EIT_noise_geometry/src/p2_add_noise.m`, whose SNR follows the EIDORS
convention (`add_noise` with two data arguments: ratio of norms of the difference
frame to the noise, quoted in dB). Both the difference-frame and absolute-frame
SNR are recorded, per `ref/EIDORS_NOTES.md` §2.

| | |
|---|---|
| **Training/primary SNR** | **40 dB** (§7) |
| Secondary SNR sweep (evaluation only) | 60, 50, 40, 30, 20 dB |
| Noise seed | independent of the training seed; recorded per frame |

Models are trained once at the primary SNR and evaluated across the sweep. The
sweep does not multiply training cost.

## 6. Outcomes, statistics and what is fixed

**Primary**: heart DSC (quarter-amplitude set) at the registered SNR, test split,
mean ± SD over seeds, and the three contrasts of §3.

**Secondary**: heart MAE / IoU / sensitivity / specificity / ASSD / HD95; the
same set on the lung channel; per-image distributions with bootstrap 95% CIs;
the SNR sweep; parameter count, FLOPs and inference time.

Secondary outcomes are secondary. A significant result on a secondary metric
does not rescue a falsified H1, and will not be reported as though it did.

**Not reported**: pixel accuracy, and the `1 − MSE` quantity used as "accuracy"
in the withdrawn manuscript.

**Seeds and power.** The first study measured the heart contrast D − B_wide at
Cohen's **dz = 0.500** with n = 10, giving roughly **29% power** — its heart
p-value was evidence of insufficient n, not of absence.

Powering this study on that dz alone would be wrong, because the §7 pilot showed
the harder task also has **larger seed-to-seed variance**: arm B's heart-DSC SD
across seeds is **0.0077** here against **0.0058** in the first study, a 33%
increase. If the effect size in DSC points is unchanged, that scales dz down to
≈ 0.376.

| assumption | dz | n for 80% power |
|---|---|---|
| effect unchanged, variance unchanged | 0.500 | 34 |
| **effect unchanged, variance as measured in the pilot** | **0.376** | **58** |
| effect unchanged, variance 50% larger | 0.333 | 73 |
| mechanism holds and the effect grows 1.5× | 0.564 | 27 |

Which row applies cannot be known before the study runs: the pilot measured the
variance but says nothing about the effect, because it trained one arm and
computed no contrast.

This study therefore registers **n = 58 seeds per arm** (seeds 0–57), 5 arms =
**290 runs**, ≈ 97 h sequential at the Mac mini M4's benchmarked 20 min/run,
less if runs are executed concurrently (see below).

n = 58 covers the row the pilot's own measurement points to. Choosing n = 34
would have covered only the most optimistic row, and repeating the first study's
failure mode — an underpowered null — is the specific outcome this design exists
to avoid.

**n is not revised in either direction after seeing any arm contrast.** n = 58 is
fixed here.

**Concurrent execution.** Runs may be executed as several concurrent processes on
one machine. Each run is independent and seeded, so concurrency changes
scheduling only, not results. Splitting work across *different* machines is not
permitted for this study: it would place hardware differences inside the paired
contrasts. All 290 runs execute on the same machine, recorded in
`runs/run_meta.json`.

**Fixed and not tunable per arm** (constants in `tools/train_arms.py`, unchanged
from the first study): Adam lr 1e-3 cosine to 1e-5; batch 16; ≤200 epochs, early
stopping on validation loss, patience 20, best weights restored; L1 loss on the
float target, no output activation; loss weights 1.0/1.0; **no augmentation**,
horizontal flip permanently excluded; one dataset-wide normalisation affine from
the training split over the field of view, never per-image; DSC threshold at the
quarter-amplitude set, EIDORS `calc_hm_set(img, 0.25)`.

The test split is read once, after all 170 runs are complete.

## 7. The pilot, and what it may not look at

One thing is unfixed: the primary SNR. It is chosen by a pilot, run **before**
this file is hashed, under these constraints:

**What the pilot does.** Generate a dataset of 900 geometries with heterogeneous
organ conductivity at 40 dB. Train **arm B only**, three seeds, and record the
per-seed mean heart DSC on the test split and the SD across those three seeds.

**What it is for.** To confirm the task has headroom on the endpoint's own
statistic, and to estimate the seed-to-seed SD that the power calculation needs.

> **Selection rule, revised 2026-08-29 before the pilot's final run.** The
> statistic is the **mean** heart DSC over the test split, per seed — the same
> statistic the study's hypotheses are tested on. An earlier draft of this
> section used the *median* over images and a 5th-percentile floor. That was a
> design error: the median saturates at 1.0000 in every condition tested,
> including conditions where the mean differs substantially, because more than
> half the images are individually perfect while the mean is carried by the
> tail. A rule written on the median would have rejected task settings that are
> in fact perfectly able to discriminate.
>
> The registered task is **heterogeneous organ conductivity at 40 dB**, chosen
> on these grounds and not on a threshold search:
>
> * heterogeneity is what demonstrably moves the endpoint — in the pilot it took
>   mean heart DSC from 0.991 (homogeneous, first study) to 0.983, and it is
>   also the more realistic phantom, answering a referee criticism;
> * 40 dB is instrument-realistic, and the pilot showed noise level is *not* the
>   binding factor — mean heart DSC was 0.999 at 20 dB homogeneous;
> * the pilot's remaining job is therefore not to search SNR but to measure the
>   seed-to-seed SD at the chosen setting, so that §6's power calculation rests
>   on this task rather than on the first study's.
>
> **Confirmation required before registering**: mean heart DSC ≤ 0.99 and the
> seed-to-seed SD non-zero at n = 3 seeds. If mean heart DSC > 0.99, raise
> `het_amp` to 0.40 and re-run the pilot rather than lowering SNR.
>
> **Pilot result, 2026-08-29 — passed.** Arm B, 3 seeds, 900 geometries,
> heterogeneous conductivity at 40 dB, evaluated on the 90-geometry test split:
>
> | | mean DSC | seed-to-seed SD | first study, homogeneous |
> |---|---|---|---|
> | Heart | **0.9792** | 0.0077 | 0.9908 ± 0.0058 |
> | Lung | 0.9874 | 0.0035 | 0.9947 ± 0.0027 |
>
> Both conditions met. The heart endpoint has moved roughly twice as far from
> 1.0 as in the first study, and the lung channel — which was at ceiling there —
> now has headroom too. The per-image median remains 1.0000 in every condition,
> which is exactly why the criteria are written on the mean.
>
> The measured SD is what sets n in §6.

**What the pilot may not do.** It trains one arm. It computes **no contrast
between arms**, and no arm other than B is trained until this file is hashed.
The pilot's purpose is to characterise the task, not to compare architectures.

## 8. Deviations

Any change after results exist is recorded here, dated, with its reason — never
by editing the text above.

| Date | Change | Reason |
|---|---|---|
| 2026-09-01 | §1's motivating evidence is superseded. **No hypothesis, endpoint, arm, or sample size changes.** | See below. |
| 2026-09-04 | Post-hoc lung-channel comparison disclosed; §3's outcome grid has no cell for the observed combination. **No hypothesis, endpoint, arm, sample size, or decision rule changes.** | See below. |
| 2026-09-18 | Implementation defect found in the DSC mask; **every heart-channel number reported before this date is superseded, including the whole 2026-09-04 entry.** Re-scored only — nothing retrained. **No hypothesis, endpoint, arm, sample size, or decision rule changes.** | See below. |

### 2026-09-01 — §1 motivates the study with the wrong measurement

§1 argues that the heart is the hard half of the task because it "carries a
median 1.7% of the reconstruction's total energy". That figure is correct for
this study's phantom, but it is **not the claim the manuscript makes**, and it
does not generalise.

**What the claim actually is.** The corresponding author clarified that
"lung dominates, heart is suppressed" refers to *EIT imaging*: the cardiac
component cannot be obtained directly from the reconstructed image. That is a
statement about **separability**, not about relative energy. An organ can carry
appreciable energy and still be inextricable from a blurred, ill-posed
superposition.

**Why the energy figure does not carry it.** Regenerating the same paired-organ
task on a real adult thorax (`mk_library_model('adult_male_16el_lungs')`, EIDORS
shape_library) gives a lung/heart energy ratio of **4.1×**, with the heart at
**20%** of total energy — against 56× and 1.7% in this study's cylinder. The
ratio is dominated by phantom geometry, so it cannot support a general statement
about EIT.

**The evidence that does carry it**, measured on this study's own dataset
(`data/v2`, all 3600 frames) and requiring no training. Apply the quarter-
amplitude threshold — `calc_hm_set(img, 0.25)`, the rule clinical ROI methods
use and the same rule this study's DSC uses — to the **mixed** image, and score
what comes out against each organ's own reconstruction:

| | lung | heart |
|---|---|---|
| Cylinder (this study) | **0.951** | **0.099**, median **0.000** |
| Real adult thorax (20 frames, exploratory) | 0.849 | 0.578 |

On this study's phantom, the same threshold that recovers the lung at DSC 0.95
recovers the heart at 0.099, and on more than half the frames recovers **nothing
at all**. That is the premise, demonstrated rather than asserted, and it holds in
the direction claimed on both geometries.

**What changes.** The manuscript will motivate the study with the separability
measurement, not the energy ratio, and will report the threshold baseline as the
clinical comparator the reviewers asked for (ARS review D W4; Scientific Reports
referee 1 item 3). Script: `tools/probe_separability.py`. Figure:
`figures/fig1_separability.pdf`.

**What does not change.** H1–H4, the primary endpoint, the arms, the training
protocol and n = 58 all stand exactly as registered. The motivation for asking a
question is not the question.

### 2026-09-04 — an unregistered analysis, and a gap in §3's outcome grid

**Nothing above is changed.** H1 and H2 are falsified and H3 is confirmed, each
by the rule registered for it. This entry records two things that the registered
text does not cover, so that neither can later be presented as though it had been.

**1. The heart-versus-lung comparison is post-hoc.** §3 registers H4 as
"reported, not tested", and registers no comparison *between* channels. After
seeing H3 confirmed on the heart channel, the same sweep was scored on the lung
channel and the two were compared. That comparison is exploratory. It does not
and cannot falsify H3.

What it found: at 20 dB, once each channel's own ceiling is divided out, the
relative error reduction is 3.43% on the heart and 3.50% on the lung — a
difference of −0.07 percentage points, 95% bootstrap CI [−3.75, +3.55]. On raw
DSC points the difference is +0.104, CI [−0.116, +0.322]. In standardised terms
the lung effect is the larger of the two (dz +0.449 against +0.266) and far more
strongly evidenced (p = 0.0005 against 0.047).

So the low-SNR advantage is not specific to the suppressed component. The
mechanism §2 attributes to the architecture — a second branch that "specialises
in learning the weaker conductivity changes" — does not explain it. What the data
support is a channel-agnostic robustness effect at a noise level (20 dB) far
below the instrument-realistic 40 dB registered in §5.

**H4's registered expectation is contradicted.** §3 states that on the lung
channel "no difference is expected between any arms". At 40 dB that held
(−0.0001, p = 0.50). At 20 dB it did not (+0.0015, p = 0.0005).

**2. §3's outcome grid has no cell for this combination.** The text anticipates
"H1 confirmed but H3 falsified" and prescribes what to do. It does not anticipate
**H1 falsified but H3 confirmed**, which is what happened. No rule is invented
here to fill the gap; the results are reported as they fell, and the manuscript
must state that this combination was not pre-specified.

**Fragility of the confirming result, recorded for honest reporting.** The 20 dB
heart contrast rests on 35 of 58 seeds (58%); removing the three largest
contributors moves it from +0.251 to +0.148 DSC points; its own 95% CI is
[+0.010, +0.492]. H3's difference-of-differences is robust to the anchor choice
(60 dB: +0.300, CI [+0.049, +0.547]; 50 dB: +0.306, CI [+0.063, +0.546]).

Scripts: `tools/gen_snr_sweep.m`, `tools/h3_snr.py`. Results:
`results_v2_snr{60,50,40,30,20}[_lung]/`. Full record: `RESULTS_STUDY2.md`.

### 2026-09-18 — the quarter-amplitude set was taken in the wrong space, and every heart number moves

**This entry supersedes the analysis reported on 2026-09-04. That entry is left
standing and unedited**, because it is itself evidence: it records what was
concluded while the metric was broken, and erasing it would hide that the
conclusions of 2026-09-04 were an artefact rather than a finding.

**Nothing registered changes.** No hypothesis, endpoint, arm, sample size or
decision rule is touched, and no model was retrained. Only the scoring changed.

**The defect.** §6 registers the DSC threshold as "the quarter-amplitude set,
EIDORS `calc_hm_set(img, 0.25)`", which thresholds an image in its own units.
`tools/evaluate.py` applied that rule *after* `train_arms.normalise()`, a
dataset-wide affine `(x − mu)/sd` with mu = −4.267822265625. **The
quarter-amplitude set is not affine-invariant.** The heart reconstruction's
near-zero background moves to +0.481 while its peak moves to 1.135, so the
background clears 0.25 × peak and the entire field of view enters the mask.

Measured on `data/v2`, mask area as a fraction of the field of view:

| | as implemented | as registered | true organ fraction |
|---|---|---|---|
| Heart | **0.948** (median 1.000) | 0.087 | 0.0020 |
| Lung | 0.454 (median 0.253) | 0.251 | — |

Most frames therefore scored DSC exactly 1.0000 by comparing two whole-field
masks. §7 of this document records "the per-image median remains 1.0000 in every
condition" and attributed it to an easy task; the real cause was the mask.

**This is a bug, not a deviation.** The implementation did not compute the
registered quantity. Fixing it is required to obtain the registered analysis, in
the same category as the `--channel` fix of 2026-09-04. The fix adds
`--qa-space`, defaulting to the registered behaviour; `--qa-space normalised`
reproduces the defective numbers and was verified to reproduce study 1's
`summary.json` byte-identically, confirming the change is isolated.

**Registered decisions after re-scoring.** H1 and H2 remain **falsified** at the
registered SNR of 40 dB: D − B_wide = +0.2234 DSC points against B_wide's
seed-to-seed SD of 0.6695, Wilcoxon p = 0.0983. H3 is **confirmed**, far more
strongly than before: difference-of-differences D(20 dB) − D(60 dB) = **+1.937
points, 95% bootstrap CI [+1.400, +2.465]**, and +1.928 [+1.394, +2.455] against
the 50 dB anchor.

⚠️ At 30 dB (+0.0062 against SD 0.0050, p < 0.0001) and at 20 dB (+0.0210
against SD 0.0108, p < 0.0001) both H1 conditions would be met. **That is not
H1.** §3 defines H1 at the registered SNR, which §5 fixes at 40 dB. The sweep is
registered for H3 and for nothing else.

**What the 2026-09-04 entry claimed, and what replaces it.**

| 2026-09-04, on the defective metric | 2026-09-18, on the registered quantity |
|---|---|
| relative error reduction 3.43% heart, **3.50% lung**, difference −0.07 pp, CI [−3.75, +3.55] | **16.16% heart, 0.80% lung**, difference **+15.36 pp, CI [+11.39, +19.28]** |
| the **lung** effect is the larger (dz +0.449 against +0.266) | the **heart** effect is far larger (dz +1.189 against +0.186) |
| "the low-SNR advantage is **not specific** to the suppressed component" | it is strongly specific to it |
| "the mechanism … **does not explain it**" | the evidence is consistent with the mechanism's direction |
| **H4's registered expectation is contradicted** at 20 dB (+0.0015, p = 0.0005) | H4's expectation **holds**: +0.0002, p = 0.0573 |
| the confirming result is fragile: 35/58 seeds, −41% on dropping three seeds | **robust**: 50/58 seeds (86%), −8% on dropping three |

**The post-hoc caveat still stands and is not weakened by the reversal.** §3
makes the lung channel "reported, not tested" and registers no between-channel
comparison. The channel-specificity analysis remains exploratory in both
directions: it could not falsify the mechanism on 2026-09-04 and it cannot
confirm it now.

**What does not change.** The separability premise is unaffected:
`tools/probe_separability.py` reads the raw reconstructions directly and never
calls `normalise`, so the quarter-amplitude threshold recovering the lung at DSC
0.951 and the heart at 0.099 (median 0.000) stands as reported.

**A second gap in §3's outcome grid.** The 2026-09-04 entry recorded that the
grid has no cell for "H1 falsified but H3 confirmed". It also has no cell for
what the corrected numbers produce: **a registered decision rule that returns
"falsified" while the effect estimate's 95% CI excludes zero** (+0.2234 points,
CI [+0.0196, +0.4412]). No rule is invented here to reconcile them. Both are
reported, and the manuscript must state that the "difference exceeds the
control's seed-to-seed SD" criterion is the one that fails by the widest margin.

Detail: `METRIC_DEFECT_2026-09-18.md`. Numbers: `RESULTS_STUDY2.md`.
Results: `results_v2_fix/`, `results_v2_snr{60,50,40,30,20}_heart_fix/`.

---

## 9. Addendum (registered 2026-09-23, before any run below was started; PI-confirmed draft of the same day)

### 9.1 What this addendum adds, and what it does not touch

Nothing above this section changes. H1–H4, the primary endpoint, the five arms, n = 58, the 40 dB primary level and the decision rules of §3 stand as registered and as already reported. This addendum registers three additional analyses that the first-round review identified as necessary to bound the *interpretation* of H3, and fixes their decision rules before any of them is run.

### 9.2 Retrained contrast at 20 dB (answers R1)

**Motivation, stated so it cannot be re-described later.** H3 was registered and confirmed as an evaluation-only sweep: every model was trained at 40 dB. At 20 dB the inputs are out of the training distribution, so two mechanisms make the same prediction in that design — a branch that protects the weak component when it is threatened, and a two-stream network that tolerates unfamiliar inputs better than a one-stream network. The registered result does not separate them. This addendum does.

**Design.** Arms D and B_wide only (the primary contrast), retrained from scratch at 20 dB on a dataset in which the training, validation and test splits are all re-noised at 20 dB from the registered geometries and noise seeds (`tools/gen_snr_full.m`; same geometries, same `noise_seed0 + i`, amplitude scaling only; the forward mesh and organ fields are the registered ones). Seeds 0–57, the same 58 seeds. All training constants of §6 unchanged. All 116 runs on the same machine as the original 290 (Mac mini M4), recorded in `runs_20db/run_meta.json` with the hash of this file.

**Primary quantity.** The paired difference D − B_wide on heart-channel Dice at 20 dB, for models trained at 20 dB (call it Δ_20|20), against the already-reported evaluation-only difference for models trained at 40 dB (Δ_20|40 = +2.097 points).

**Pre-specified decision rule (H5).**
- H5 is *confirmed* if Δ_20|20 exceeds B_wide's seed-to-seed SD at 20 dB (trained at 20 dB) **and** Wilcoxon signed-rank over paired seeds gives p < 0.05 — the same two-condition form as H1, applied at the level where the branch is expected to matter.
- H5 is *falsified* if either condition fails.
- **Interpretation, fixed now.** If H5 is confirmed, the branch's benefit at 20 dB is not an artefact of distribution shift: it is present when the network is trained at the operating noise level, and the paper's headline stands with "under threat" read as the operating noise level. If H5 is falsified, the evaluation-only H3 result is attributable in whole or in part to distribution-shift tolerance, and the paper's headline must be narrowed to "for a network trained at 40 dB and evaluated under heavier noise"; H3 itself remains confirmed as registered.
- **Secondary, reported not tested**: Δ_20|20 versus Δ_20|40 with a 95% bootstrap CI on the difference (seeds resampled); the lung channel at 20|20 (H4 expectation carried over: no difference expected).

**What this addendum does not licence.** No other arm is retrained. No level other than 20 dB is used for training. A confirmed H5 does not retroactively change the H1 decision at 40 dB.

### 9.3 Two additional evaluation-only levels (answers R5)

The registered sweep has 10 dB resolution, so "the onset lies between 40 and 30 dB" is a statement at grid resolution. Two further evaluation-only levels, **35 dB and 25 dB**, are generated by the registered procedure (`tools/gen_snr_sweep.m`, test split only, same seeds) and scored with the already-trained 40 dB models, for D and B_wide. They are **descriptive**: they refine where the advantage appears and do not carry a decision rule. They are reported with the same statistics as the five registered levels (paired difference, bootstrap CI, dz, relative error reduction, seeds with D > B_wide). The H3 statistic is not recomputed with these levels; its anchors remain 60 and 20 dB as registered.

### 9.4 Geometry-level uncertainty (answers R4)

Every seed is scored on the same 360 test geometries, so the seed-level bootstrap intervals in the paper describe training-run variability only. For the 40 dB and 20 dB contrasts (D − B_wide, heart channel; and for Δ_20|20 once available), a second interval is computed by resampling **test geometries** (per-image Dice from `per_image.csv`, 100,000 resamples of the 360 frames, seed-mean taken inside each resample). Both intervals are reported side by side; neither replaces the registered rule, which is defined on seeds.

### 9.5 Order of operations

1. PI confirms this text; it is appended as §9 of `PREREGISTRATION_HEART.md`; `shasum -a 256` recorded in `PREREGISTRATION_HEART.sha256` as the addendum hash (the original registered hash is retained above it).
2. `gen_snr_sweep([35 25])` and `gen_snr_full(20)` are run on the Air (MATLAB R2026a, EIDORS v3.8); outputs packed with `pack_sweep_delta.py` (35/25) and transferred; the 20 dB full dataset is transferred whole.
3. On the mini: `train_arms.py --data <20dB full> --arms D B_wide --seeds 0..57 --out runs_20db --prereg PREREGISTRATION_HEART.md`; then `evaluate.py` on runs_20db at 20 dB; `evaluate.py` on the original runs at 35 and 25 dB; per-image files for 9.4 exported.
4. Results recorded in `RESULTS_STUDY2.md` §十 (new) before any manuscript text is revised.

### 9.6 Cost

116 training runs ≈ 39 h sequential at 20 min/run (mini); 35/25 dB generation ≈ 2 × the per-level time of the original sweep; 20 dB full-split generation ≈ 10 × a single sweep level (3,600 forward and inverse solves).
