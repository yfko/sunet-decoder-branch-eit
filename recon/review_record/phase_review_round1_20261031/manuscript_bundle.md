<!--block:B0001-->

<!--block:B0002-->
# Does a decoder branch for the cardiac component of lung EIT survive a change of reconstructor? A preregistered, parameter-matched study with leave-one-reconstructor-out training

<!--block:B0003-->
**Short title:** Decoder branch and reconstructor change in lung EIT

<!--block:B0004-->
Yen-Fen Ko¹\*, Chang-Wen Chen², Tang-Chuan Wang³

<!--block:B0005-->
¹ Department of Biomedical Engineering, China Medical University, Taichung City, Taiwan
² Department of Critical Care Medicine, Fu Jen Catholic University Hospital, New Taipei City, Taiwan
³ School of Medicine, College of Medicine, China Medical University, Taichung City, Taiwan; Department of Master Program for Biomedical Engineering, College of Biomedical Engineering, China Medical University, Taichung City, Taiwan
\*Corresponding author: Yen-Fen Ko (kklven@gmail.com)

<!--block:B0006-->
**Abstract** — Post-reconstruction networks for lung electrical impedance tomography (EIT) inherit the reconstructor they were trained on; whether a decoder branch for the weak cardiac component still helps under another conventional reconstructor was left open by the study that proposed it. We preregistered and hashed a parameter-matched comparison of a two-decoder network (D) against a widened single-decoder control (B_wide) on simulated 16-electrode lung EIT at 20 dB, reconstructed by GREIT, one-step Gauss–Newton and back-projection, scored by heart-channel Dice against each reconstructor's own heart image. Under matched training the branch stayed below the registered floor on every reconstructor (+0.27 to +0.63 Dice points against floors of 0.34 to 0.66). The registered transfer hypothesis for a reconstructor change without retraining was falsified in all six cells, with no evidence in the two in-range cells that the branch's advantage grew under the shift; exploratory re-scoring put the cost of not retraining at 19 to 33 points. In a post-unblinding, pre-hashed addendum, a single global normalisation collapsed two reconstructors whose amplitudes lie two orders of magnitude below the third's; with a per-source affine, pooled training was never worse than retraining on the deployed reconstructor (−0.08 to +0.36 points; two of six intervals favoured pooling, confounded with threefold optimisation steps). In a second addendum, leaving one reconstructor out of the pool cost 62, 16 and 36 points on it against a pre-fixed margin of ±1.0 point (an upper bound, since the reference moves with the reconstructor), falsified in all three cells, and the branch added nothing measurable there. The reconstructor behaves as a domain: the remedy for a reconstructor change lies in the training data, not in this branch, and the benefit of pooled training stops at the pool boundary for the three conventional reconstructors tested. Every verdict follows a rule fixed before its data were read.

<!--block:B0007-->
**Keywords** — electrical impedance tomography; decoder branch; cardiac component; domain shift; pooled training; equivalence testing; preregistration

<!--block:B0008-->
---

<!--block:B0009-->
## 1. Introduction

<!--block:B0010-->
### 1.1 Clinical indices are insensitive to the reconstructor; a pixel-level network is not

<!--block:B0011-->
Chest EIT reconstructs conductivity change from boundary voltages; its clinical use rests on regional ventilation indices computed from the images (Frerichs et al., 2017) . Those indices are insensitive to which linear reconstructor produced the image: four algorithms applied to the same recordings gave five ventilation indices with no significant difference between them (Zhao et al., 2014) , and twelve reconstructions differed in appearance by amounts that were not negligible while the clinical parameters derived from them were close (Grychtol et al., 2014a) . A network that reads pixels sees the appearance, not the index. This paper uses *domain* for the reconstructor in a narrow, operational sense: we call the reconstructor a domain if, for a pixel-level post-reconstruction network, a change of reconstructor shows the three signs that multi-site segmentation studies associate with a domain shift: a loss of performance without retraining, no loss when the new reconstructor's images are pooled into training, and a failure when the new reconstructor is outside the training pool. The paper does not claim domain generalisation; that literature is cited only where compared (Zhou et al., 2023; Yoon et al., 2024)  . One difference from it governs every held-out number below: there the label is anatomy and does not change with the site, whereas here the reference is the reconstructor's own single-organ reconstruction and moves with it, so a held-out loss is an upper bound on the input-side generalisation loss (Section 2.3).

<!--block:B0012-->
### 1.2 The decoder branch and what the original study left open

<!--block:B0013-->
The cardiac-related impedance change in lung EIT frames is several times smaller than the ventilation change (Leathard et al., 1994)  and highly position dependent (Graf and Riedel, 2017) . Three studies of ours precede it: a U-Net for lung segmentation in EIT (Ko and Cheng, 2021a) , the semi-Siamese U-Net that separates lung and heart images with one encoder and two parallel decoders (Ko and Cheng, 2021b) , and heart-related image reconstruction from GREIT frames with optimised loss weights (Ko et al., 2025) . Throughout, *segmentation* names the task of producing a Dice-scored mask, and *separation*, *weak component* and *dominant component* name the mechanism. The semi-Siamese study's conclusions state that "the separation effect of the EIT image obtained by the different reconstruction algorithms will be investigated" (Ko and Cheng, 2021b) , naming GREIT, Gauss–Newton and back-projection; this paper answers it. A companion simulation study from our group, currently in review, evaluates the same two arms under GREIT across noise levels; this paper relies on none of its reported findings, re-uses its GREIT-trained networks re-scored here (Section 2.2), and the two are declared related submissions [MATERIAL GAP: preprint DOI].

<!--block:B0014-->
We test, for a change of reconstructor, whether a decoder branch dedicated to a weak component yields a measurable benefit when that component is under threat. The branch is a decoder-side branch serving one target each, of the branched multi-task family (Vandenhende et al., 2022) , with EIT relatives in a dual-branch reconstructor (Wang et al., 2024)  and a multi-branch network built for noise tolerance (Yu et al., 2024a) . All sit downstream of a reconstruction operator, as do the post-processing networks for EIT (Hamilton and Hauptmann, 2018; Herzberg et al., 2023; Zhang et al., 2022b)   , and the operator is not neutral: the same U-Net placed after a linearised reconstruction or after D-bar performs differently (Denker et al., 2025) .

<!--block:B0015-->
### 1.3 What the literature does and does not contain

<!--block:B0016-->
Multi-source training and its failures are documented clinically: pneumonia detection generalised variably across hospitals (Zech et al., 2018) , cross-institutional tumour segmentation lost Dice (AlBadawy et al., 2018)  and multi-site segmentation needed site-specific normalisation (Liu et al., 2020) . The closest analogue to a change of EIT reconstructor is a change of computed tomography (CT) reconstruction kernel: a training-by-evaluation matrix with a pooled row (Hoang-Thi et al., 2021)  and a cross-evaluation varying kernel, slice thickness and dose one at a time (Zeng et al., 2022) .

<!--block:B0017-->
Three bounded absence statements follow from a search of OpenAlex, Crossref, PubMed and Semantic Scholar on 2026-10-11 (31, 31 and 38 strings; repository). To our knowledge within that search, no EIT deep-learning study has trained on one conventional reconstructor's images and evaluated on another's, or pooled several reconstructors' outputs; the nearest broadens the training domain in geometry, not reconstructor (Hamilton et al., 2019) . None compared a single global normalisation affine with one affine per source, or reported how pooled training fails when sources differ in amplitude by two orders of magnitude; the nearest places per-source normalisation in batch-normalisation layers (Karani et al., 2018) . And none applied an equivalence margin fixed before the runs to leave-one-source-out against pooled training; the nearest is a leave-one-centre-out comparison concluded from a non-significant p value (Holzschuh et al., 2024) .

<!--block:B0018-->
### 1.4 Questions, preregistration and the standing of each result

<!--block:B0019-->
Three questions were asked, each judged by rules fixed before the data were read. The registered part (hash 4b4c7a6d…, 2026-09-26) asked whether the branch clears a registered floor under matched training on Gauss–Newton and back-projection (R1), whether its advantage is larger under a cross-reconstructor shift than under matched training in six evaluation-only cells (R3, the registered form of the transfer question), and whether it clears the floor after pooled training under one normalisation affine (M1). After those cells had been read, a first addendum (hash 0060eedf…, 2026-10-03) fixed a pooled row with one affine per source (M1′, M2′, M3′) and an exploratory re-scoring (E1); after that row had been read, a second addendum (hash 9589b298…, 2026-10-11) fixed three leave-one-reconstructor-out rows with an equivalence margin of ±1.0 point (L1), the branch rule on the held-out reconstructor (L2) and descriptive quantities (L3′). In the vocabulary of confirmatory methodological research (Lange et al., 2025)  the addenda have a double standing: confirmatory for their own runs, exploratory in origin.

<!--block:B0020-->
The paper contributes four things: registered, the matched-training null of the branch extends to the two other conventional reconstructors, with no evidence that its advantage grows under a reconstructor change; from the first addendum, pooled training with a per-source affine was never worse than retraining on the deployed reconstructor, and a global affine is a failure mode worth reporting; from the second, the pooled recipe does not generalise to a reconstructor outside the pool, tested and falsified at a pre-fixed margin, and the branch adds nothing measurable there; and, methodologically, a preregistered study whose hypotheses were mostly falsified, reported with its deviations and expectation hit rates.

<!--block:B0021-->
## 2. Materials and Methods

<!--block:B0022-->
### 2.1 Simulation and the three reconstructors

<!--block:B0023-->
All images were generated with the EIDORS toolbox, v3.8 (Adler and Lionheart, 2006)  on the registered 16-electrode cylinder with 3,600 geometries: background 1.0 S/m, two lung inclusions at 0.5 S/m and one heart inclusion at 2.0 S/m, with randomised radii, centres and heterogeneous conductivity. For each geometry three forward and three inverse solves were run (mixed, lung only, heart only): the network's input is the mixed reconstruction and its targets the single-organ reconstructions. Gaussian measurement noise was added to the voltage frame before reconstruction at a signal-to-noise ratio (SNR) of 20 dB in the EIDORS convention, the ratio of the norm of the difference frame to the norm of the added noise. The level is fixed and stated because an EIT system's SNR depends on its operating conditions (Gagnon et al., 2010) . Geometries and noise seeds were split 2,880/360/360 into training, validation and test frames, bit-identical across the three reconstructors, so that the datasets differ only in the reconstruction operator.

<!--block:B0024-->
The three reconstructors are those the original study named, each at one fixed setting. GREIT, the Graz consensus reconstruction algorithm for EIT (Adler et al., 2009)  was built as registered on a 64 × 64 grid (nominal noise figure 0.5, realised 0.602 on a common reference frame; noise figure after Adler and Guardo (1996) ). One-step Gauss–Newton (GN) with a Laplace prior was solved on GREIT's grid, its hyperparameter set by bisection so that its noise figure matched GREIT's realised value (hp 0.0016, noise figure 0.607). Back-projection (BP) used the Sheffield back-projection matrix distributed with EIDORS (Adler and Lionheart, 2006) , with no free parameter (noise figure 0.831); its 32 × 32 raster was upsampled two-fold and masked to GREIT's field of view. Because reconstruction settings strongly influence what a reconstructor produces (Thürk et al., 2019) , every result holds for these three operators at these settings.

<!--block:B0025-->
One pipeline fact, measured after the registered matrix was scored, governs the pooled rows. Over the training split the mixed-image standard deviation is 8.92 for GREIT, 0.0555 for GN and 0.0474 for BP: GREIT's amplitude is 161 times GN's and 188 times BP's (Fig 1), a difference that is not neutral for a network whose normalisation is estimated once over a pooled training set (Section 2.4).

<!--block:B0026-->
### 2.2 Arms

<!--block:B0027-->
Two arms share one U-Net encoder (Ronneberger et al., 2015) , bottleneck, block structure, loss, optimiser schedule and dataset. The encoder takes a 1 × 64 × 64 input through four levels of 32, 64, 128 and 256 channels (two 3 × 3 convolutions with batch normalisation and rectified linear units per level, 2 × 2 max-pooling) to a 512-channel bottleneck; a decoder mirrors it with 2 × 2 transposed convolutions and skip concatenation, the original width being 32 channels at the finest level, and ends in a 1 × 1 output convolution. Arm D splits at the bottleneck into two decoders of the original width, one per target, and is the architecture under test. Arm B_wide has one decoder with two output heads, widened by 1.5312 (channel counts rounded to multiples of eight: 48, 96, 192 and 392 from fine to coarse) so that its parameter count (10,743,738) matches D's (10,811,298) to within one percent. The primary contrast, D minus B_wide, holds supervision, data, schedule and capacity constant, so that the remaining difference is whether the decoder is split. Fixed-budget comparison of branch structures follows the branched multi-task literature (Vandenhende et al., 2020) , and an adequately configured, capacity-matched baseline is the control whose absence lets a new architecture appear to beat a U-Net (Isensee et al., 2024) . Matched parameter count is not matched architecture, and other controls (matched floating-point operations, an unsplit decoder of the original width) were not run.

<!--block:B0028-->
The second decoder is hard parameter sharing (Caruana, 1997) . The two L1 losses were summed with fixed weights of 1.0 each, a scope decision: the original study proposed the branch together with a multi-weighted loss and attributed its improvement to their interaction, and this study evaluates the branch alone. Fixed weights are a defensible default, since unit or tuned fixed weights have matched specialised multi-task optimisers in controlled comparisons (Kurin et al., 2022; Xin et al., 2022)  ; learned weighting (Kendall et al., 2018)  was not tested. Training settings, fixed before registration: Adam at 1 × 10⁻³ with cosine decay to 1 × 10⁻⁵, batch 16, at most 200 epochs with early stopping on validation loss (patience 20, best weights restored), L1 loss on the float target, no output activation, no augmentation, and one dataset-wide normalisation affine estimated from that dataset's training split and applied to inputs and targets. Thirty seeds (0 to 29) per arm and training row were trained on one machine (Mac mini M4); seed-to-seed variability is of the order of the effects at stake (Renard et al., 2020) . The GREIT row reuses seeds 0 to 29 of the companion study's 20 dB training (same machine, same code).

<!--block:B0029-->
### 2.3 Endpoint

<!--block:B0030-->
The primary endpoint is heart-channel Dice on the quarter-amplitude set, the region above one quarter of the image's peak, the threshold clinical region-of-interest methods apply to EIT images (Pulletz et al., 2006) , computed in image units on the test split and averaged over seeds; one Dice point is 0.01. The reference for each reconstructor is that reconstructor's own single-organ heart reconstruction, not the anatomical heart. This is registered and follows from the task: the network separates the cardiac component of a reconstructed image, and the correct answer is by definition what that reconstructor produces when only the heart is present. Scoring against an anatomical mask would fold each reconstructor's blur and bias into the endpoint; comparing reconstructors by image quality is outside this paper's claims. Dice against an anatomical reference was not computed. The lung channel is reported in every cell and not tested, with the registered expectation of no arm difference.

<!--block:B0031-->
Two consequences matter for the held-out cells. The quarter-amplitude set is a threshold relative to the image's own peak, so a uniform over-amplitude leaves the set unchanged while a raised background or a changed shape alters it. And when the network is evaluated on a reconstructor it did not see, the reference changes with the reconstructor: a network trained on GN and BP heart images is scored against GREIT heart images it never saw. A held-out loss therefore combines a change of input distribution with a change of reference style, and is reported as an upper bound on the input-side generalisation loss, because the reference moves with the reconstructor. How much of a given loss is attributable to the reference style was not measured.

<!--block:B0032-->
### 2.4 Design matrix and normalisation paths

<!--block:B0033-->
Fig 2 shows the design. Three single-reconstructor rows give the matched cells; six off-diagonal cells evaluate a trained row on another operator without retraining; two pooled rows train on all three reconstructors (8,640/1,080/1,080 frames), one with a single affine over the pooled split (mixed, registered) and one with each source standardised by its own training-split affine before pooling (mixed-ps, first addendum); three leave-one-reconstructor-out rows train on two sources with per-source affines (5,760/720/720 frames) and are evaluated on the third, which the network never saw (loro, second addendum). The training-by-evaluation crossing follows EIT cross-condition designs (Jeschke et al., 2025) . The per-source affine is fixed, not learned, because this study measures the network's response to a source difference and a learned normaliser would absorb part of it (Section 4.3).

<!--block:B0034-->
Three evaluation paths differ in which affine standardises the input and undoes the output. The registered off-diagonal cells use the training set's affine for both. A registered secondary path used the evaluation set's affine for both; it misplaces the output's zero in image units and is listed but not read (Section 3.2). The exploratory E1 path (first addendum) standardises the input with the evaluation set's affine and undoes the output with the training set's, keeping the predicted background at zero. The pooled and held-out rows are scored with the evaluation reconstructor's own training-split affine for both. Each pooled and held-out row passed a data-only gate before training (pooled affine the identity to rounding; in-pool frames matching the single-source rows to within 2 × 10⁻⁶; source within-frame SDs within 4%). Because the normalisation is source-aware, every pooled-training statement carries the clause that the deployment affine is the deployed reconstructor's own; nothing in the held-out protocol is selected on the held-out reconstructor (Yu et al., 2024b) .

<!--block:B0035-->
### 2.5 Preregistration, hashes and deviations

<!--block:B0036-->
Table 4 gives the four SHA-256 states of the preregistration file, what each governs, and what had been read when each was written. The registered state (2026-09-26) fixed R1, R3 and M1 with their rules, interpretations in both outcomes, n = 30 and the pilot before any arm was trained. Two deviations were recorded on 2026-10-03 before any cell was read: the pilot's acceptance band for GN's noise figure predated the change of matching rule from GREIT's nominal to its realised value, and BP's single-organ peaks were offset from GREIT's by up to 2 pixels against a registered tolerance of one pixel (2 pixels is one pixel of BP's native grid). No hypothesis, endpoint, arm, setting, sample size or rule changed; BP was analysed as registered, with the offset noted beside every BP cell.

<!--block:B0037-->
The first addendum was written after the registered matrix had been read and says so; it fixed the mixed-ps row, the M1′ rule and expectation, M2′, M3′ and E1 before any of those runs started. The second addendum was written after the first addendum's results had been read; it fixed the three held-out rows, the L1 margin of ±1.0 point with its reasons (above every registered floor, an order of magnitude below the smallest in-range no-retraining loss, not power-derived), the L2 rule and the expectations, before training; each hash is written into every run's metadata. The hashes are internal, without third-party timestamp; the four preregistration states are deposited with the minimal dataset (Section 2.7; S1 Appendix). Deviations follow the reporting structure of Willroth and Atherton (2024) , and each addendum lists what it does not licence (reconstructor ranking, other noise levels, learned or additional reconstructors, descriptive quantities as verdicts).

<!--block:B0038-->
### 2.6 Statistical analysis

<!--block:B0039-->
Seeds are the unit of replication and every contrast is paired within seed. The branch rule (R1, M1, M1′, L2) has two conditions: the mean paired difference D minus B_wide on heart Dice must exceed B_wide's seed-to-seed standard deviation in that cell, the registered floor, and the two-sided Wilcoxon signed-rank test over the 30 paired seeds (Wilcoxon, 1945)  must give p < 0.05; otherwise, or if the sign is reversed, the hypothesis is falsified. The floor is the registered smallest effect of interest; n = 30 gives at least 0.89 power for a floor-sized effect at diagonal-cell variability and deliberately does not power a below-floor effect. The transfer rule (R3) requires the difference of differences, Δ(X→Y) minus Δ(X→X), to be positive with a 95% percentile bootstrap interval over paired seeds (100,000 resamples, seed 20260904) that excludes zero. The equivalence rule (L1) requires the 95% percentile bootstrap interval of the control arm's paired difference between the held-out row and the in-pool pooled row to lie entirely within ±1.0 point; a two-sided 95% interval inside the margin corresponds to two one-sided tests at α = 0.025 (Schuirmann, 1987) , more conservative than the 90% interval usual in equivalence testing (Lakens, 2017; Lakens et al., 2018)  . Pairing by seed follows the registered rule; with effects 14 to 58 points outside the margin, paired or unpaired resampling affects no verdict.

<!--block:B0040-->
Every cell is reported with n, the paired difference, its 95% bootstrap interval, the control arm's seed SD, the paired-difference SD, Cohen's dz (Lakens, 2013) , the Wilcoxon statistic W, and exact p values at or above 0.001 (intervals are rarely reported in segmentation studies; Christodoulou et al., 2024) . For the R3 and E1 cells the achieved sensitivity (the difference of differences detectable with 80% power at n = 30 from that cell's observed seed SD) is reported, because the registered power table assumed diagonal-cell variability. No multiple-comparison correction was applied over the twenty verdicts: every verdict is of the form "not confirmed", and multiplicity inflates false confirmations, not false falsifications; the one interval excluding zero in the negative direction (L2 on GN) is described, not tested. Analyses used Python 3.9, PyTorch 2.8.0, NumPy 2.0.2 and SciPy 1.13.1.

<!--block:B0041-->
### 2.7 Data, code and AI use

<!--block:B0042-->
The minimal dataset (per-seed Dice for every cell, the aggregated results file, gate and seed-0 diagnostic files) and the four preregistration states with their hash file are deposited on Zenodo [MATERIAL GAP: Zenodo DOI, to be minted at submission]; the data-generation, training, scoring and figure code is in the project repository under a tagged release [MATERIAL GAP: repository tag for this paper]. Checkpoints are available from the corresponding author. The use of artificial-intelligence tools is disclosed in the Acknowledgments.

<!--block:B0043-->
## 3. Results

<!--block:B0044-->
Results fall under three standards: the registered verdicts in Sections 3.1 to 3.3, the first addendum's rows in 3.1 to 3.4 where labelled, and the second addendum in 3.5 and 3.6. Every quantity is heart-channel Dice in points (0.01) on the test split over seeds 0 to 29 (per-seed values in S1 Table); every addendum quantity is labelled. The registered pilot checks passed (S2 Table).

<!--block:B0045-->
### 3.1 Under matched training, the branch stays below the registered floor on all three reconstructors

<!--block:B0046-->
Table 1 gives the matched cells. On GN the paired difference D minus B_wide was +0.323 points (95% CI +0.183 to +0.470; p 0.00015) against a floor of 0.449; on BP it was +0.631 (CI +0.399 to +0.885; p 3 × 10⁻⁵) against a floor of 0.664. Both p values pass and neither difference exceeds its floor, so R1-GN and R1-BP are falsified, and the registered reading applies: the null extends across the three reconstructors the original study named. The GREIT diagonal reference shows the same pattern (Table 1). In the first addendum the mixed-ps row gave −0.015 (floor 0.173, p 0.64) on GREIT, +0.201 (floor 0.248, p 0.00086) on GN and +0.404 (floor 0.531, p 0.0048) on BP: M1′ falsified in all three, by sign reversal on GREIT and by the floor on GN and BP (expectation met on 3 of 3 verdicts and 1 of 3 magnitudes). Under pooled, source-aware-normalised training the branch does not clear the floor on that reconstructor.

<!--block:B0047-->
These are differences below the floor, not zero: four of the five cells have p < 0.05 and an interval excluding zero, with difference-to-floor ratios of 0.72 to 0.95, and the fifth reversed sign because B_wide rose by 0.36 points under pooling while D did not. The lung channel differed between arms by at most 0.03 points in the matched cells, as registered.

<!--block:B0048-->
### 3.2 The transfer hypothesis is falsified in all six no-retraining cells, and in the two cells with in-range input the branch's advantage shows no evidence of growing under the shift

<!--block:B0049-->
Table 2 and Fig 2 give the six registered off-diagonal cells, scored with the training set's affine. The difference of differences, Δ(X→Y) − Δ(X→X), was negative in five cells (−1.07 to −10.05 points) and positive with an interval containing zero in the sixth (BP→GN, +2.97, CI −0.12 to +5.84), so all six R3 cells are falsified. The fixed reading is that whatever shift tolerance the branch has is specific to the kind of shift.

<!--block:B0050-->
The six cells do not pose the same question. A seed-0 diagnosis (S3 Fig) shows that under the training set's affine the GREIT-trained networks saw GN and BP frames as nearly constant (within-frame SD 0.005 and 0.004 against 0.82 on the diagonal), while GN- and BP-trained networks saw GREIT frames 131 and 154 times over their trained range; those four cells measure both arms' response to an input the network cannot read, and both arms fail there. Only GN→BP and BP→GN present an in-range input; there the differences of differences have opposite signs, both intervals contain zero, and the achieved sensitivities are 15.8 and 4.5 points, because the quantity's seed SD far exceeds the registered power table's assumption. For transfer the result is no evidence, not a demonstrated absence; the two negative intervals are described, not interpreted (R3 has no rule in that direction). The registered secondary path (evaluation set's affine for input and output) is listed in Table 2 and not read, because it moves the output's background off zero and the mask fills the field.

<!--block:B0051-->
The exploratory E1 re-scoring (first addendum; no verdict) kept the input in range and the background at zero. Under it both arms lost about 19 to 33 points relative to their diagonals in every cell (Table 2), and in the two in-range cells the difference of differences changed sign in one when only the input affine changed. E1 confirms R3 in no cell and is not evidence of any tolerance of the branch; it supports one sentence: a reconstructor change without retraining costs about 19 to 33 heart-Dice points even after scale correction, a figure that depends on the affine used.

<!--block:B0052-->
### 3.3 A single global affine collapses two of the three reconstructors; a per-source affine restores pooled training

<!--block:B0053-->
The registered pooled row used one affine over the 8,640 pooled frames. Because GREIT's amplitude is 161 and 188 times GN's and BP's, that affine left GN and BP inputs varying by 1/132 and 1/156 of a GREIT input and their heart targets by 1/346 and 1/318 (Fig 3). The networks scored 0.45 ± 0.30 and 0.41 ± 0.30 (B_wide; D similar) on GN and BP, and 0.946 on GREIT. M1 is falsified in all three cells under its rule (sign reversed on GN and BP; +0.094 below a floor of 0.954 on GREIT), and the verdicts stand. Whether the registered row posed its intended question is a design matter: on GN and BP the networks were shown an input they could not read, so those two cells are not evidence about pooled training, and the registered interpretation of a falsified M1 is not applied to them.

<!--block:B0054-->
The mixed-ps row (first addendum) standardised each source with its own training-split affine before pooling; the pre-training gate confirmed that the pooled affine was then the identity to rounding and that the three sources' inputs were on one scale, while GREIT heart targets still weigh up to 1.7 times GN's in the loss. On that row both arms scored 0.958 to 0.968 on all three reconstructors (Table 1), the level of the diagonals.

<!--block:B0055-->
### 3.4 Pooled training with a per-source affine was never worse than retraining on the deployed reconstructor

<!--block:B0056-->
M2′ (first addendum; reported, not tested) is the paired difference between the mixed-ps row and the matched row on the same reconstructor (Table 1). The six values run from −0.083 to +0.360 points and all six intervals lie within [−0.32, +0.50]. Pooled training was never worse than retraining on any reconstructor, and two of the six intervals, both for the control arm on GREIT and GN, lie above zero.

<!--block:B0057-->
Three qualifications belong to the result. Pooling is expected to help and is not claimed as a finding, as the preregistration stated in advance. It is not free: the mixed-ps row reached a similar best epoch to the single-source rows (median 57 and 74.5 epochs against 56 to 72.5) on three times as many frames per epoch, so each run took about three times the optimisation steps and wall time, and this design cannot separate the benefit of three renderings per geometry from that of three times the steps. And the normalisation is source-aware. M3′, the share of the no-retraining loss that pooling removed, is in Table 2 (+34.7/+44.8 points for GN→BP and +15.1/+11.7 for BP→GN in the two in-range cells; the four cells crossing GREIT carry the degenerate or over-range note).

<!--block:B0058-->
### 3.5 Pooled training does not generalise to a reconstructor outside the pool: 62, 16 and 36 points

<!--block:B0059-->
Table 3 and Fig 2 give the held-out rows. L1 compares the control arm on the held-out reconstructor with the same arm on the in-pool mixed-ps row, against a margin of ±1.0 point fixed before training. The differences were −61.8 points (CI −65.1 to −58.5) on GREIT, −15.8 (−16.7 to −14.9) on GN and −35.8 (−39.4 to −32.7) on BP (D beside, untested, in Table 3). No interval approaches the margin, and L1 is falsified in all three cells. The fixed reading applies to each reconstructor in turn: the recipe stays in-pool only for that reconstructor, and the loss is reported as the cost of deploying on an unseen reconstructor. The addendum expected three falsifications with losses of 5 to 30 points: met on 3 of 3 verdicts and 1 of 3 magnitudes (GN). The six in-pool reference cells of the same rows scored 0.957 to 0.967, the level of the diagonals, so the two-source pools were not deficient: the networks failed only on the source they had not seen. The loss order, GN smallest and GREIT largest, is the two-source pool's coverage of the held-out reconstructor, not a ranking of reconstructors. Because the reference image moves with the reconstructor (Section 2.3), each loss is an upper bound on the input-side generalisation loss.

<!--block:B0060-->
Relative to single-source training without retraining (L3′; reported, not tested), the two-source pools showed no evidence in either direction of improving performance on the third source in the two registered in-range cells (B_wide −0.7 and −1.2 points, D −8.2 and +6.1; Table 3), with the caveat that the two sides use different affine policies (Section 4.4). The lung channel also fell on the held-out reconstructor (B_wide 0.914, 0.927 and 0.789 against 0.985 to 0.988 in every in-pool cell), so the failure is of the whole network's input side, not of the cardiac channel.

<!--block:B0061-->
Fig 4 and S3 Fig show seed 0 of each held-out cell; what follows describes one seed of thirty; only the point that the loss is not a scoring defect rests on all thirty, since the same scoring path gives 0.96 in the nine in-pool cells. The three cells fail in three ways. On GREIT the predicted heart peaks at 0.37 to 0.39 of the target's peak and spreads over the field. On GN shape and position are right but the output peaks at 4.6 to 5.2 times the target with a background raised to 0.34 of the target's peak; whether that loss owes anything to GN's target style, a heart image with a ring-shaped halo, or to the over-amplitude itself was not tested. On BP the shape is right, the peak 1.2 to 1.7 times the target's and the background negative, contributing 32% to 39% of the mask; this cell is also the most seed-dependent (Table 3). The GREIT and BP failures are unrelated to the held-out target style: the output is wrong before any reference is applied.

<!--block:B0062-->
### 3.6 On an unseen reconstructor the branch adds nothing measurable

<!--block:B0063-->
L2 applies the branch rule in the three held-out cells (Table 3). D minus B_wide was −3.2, −3.9 and −2.5 points on GREIT, GN and BP: falsified in all three by sign reversal, and the fixed reading is that the matched-training null extends to a reconstructor the network never saw. The addendum expected three falsifications in the matched range (−0.02 to +0.63): verdicts met (3 of 3), magnitudes and directions not (0 of 3). The three cells do not carry equal weight: on GREIT and BP the floor is 9.49 points, fifteen times the largest matched difference in this study, so the rule could hardly have been met there whatever the branch did, and the information lies in the sign, consistent across the three cells, and in the GN cell (CI −5.3 to −2.4; p 0.00012; D above B_wide on 4 of 30 seeds). Beside E1's six exploratory cells, the branch's difference is negative in eight of nine out-of-distribution cells, a description and not a verdict, taken up in Section 4.6.

<!--block:B0064-->
## 4. Discussion

<!--block:B0065-->
### 4.1 The reconstructor behaves as a domain, and the remedy lives in the training data

<!--block:B0066-->
All three signs named in Section 1.1 appeared. Without retraining, a change of reconstructor cost both arms about 19 to 33 heart-Dice points even after scale correction (exploratory), and the registered transfer hypothesis was falsified in every cell. With the deployed reconstructor's images in the training pool, pooled training with a per-source affine was never worse than retraining on that reconstructor (first addendum). With the deployed reconstructor outside the pool, the same recipe lost 16 to 62 points (an upper bound, Section 2.3), falsified against a margin fixed in advance (second addendum). Fig 5 arranges the remedies tested. Only putting the target reconstructor's images into training recovered the loss, and the two ways of doing so could not be separated at 0.4 points.

<!--block:B0067-->
"The remedy lives in the training data" is not a tautology, because four of its parts could have failed and did not. In-pool pooling could have cost accuracy; it did not. A single global affine did destroy pooling, so the recipe depends on a normalisation step the preregistration had not foreseen. Two sources pooled gave no evidence of helping on a third, so within this study the benefit of pooling is one of inclusion, not of diversity. And the one architectural remedy tested, the branch, had no measurable effect at any of the three layers. That last statement is bounded: the branch's null is consistent across the three training conditions tested (matched, in-pool pooled, unseen), but these are three conditions of one design, not independent replications, and other architectural remedies, such as source-specific normalisation layers (Karani et al., 2018; Liu et al., 2020)  , were not tested; nothing here says the remedy cannot lie on the architecture side. The reading of a second decoder as a regulariser rather than a specialist (Myronenko, 2019)  predicts no advantage on a matched in-distribution task and is consistent with every in-pool cell. The lung channel's fall on the held-out reconstructor shows that the failure is of the whole input side, beyond what a branch dedicated to the cardiac output could repair.

<!--block:B0068-->
### 4.2 A falsified equivalence licenses an in-pool recipe, tested rather than assumed

<!--block:B0069-->
A leave-one-source-out comparison is usually reported as a non-significant difference, as in a four-centre segmentation study that read median Dice of 0.76 pooled against 0.74 held out, p = 0.18, as compatibility (Holzschuh et al., 2024) . Non-significance cannot establish equivalence; a margin can (Lakens, 2017) . This study fixed one before the runs and the test came out falsified: the deployment recipe of pooled training with a per-source affine is in-pool only, and that restriction is a tested result. The conclusion is insensitive to the margin, since every interval lies 14 to 58 points outside it and would lie outside ±5 or ±10 points as well; this is a post-hoc sensitivity statement, not a change of margin. Within this study's scope the term "reconstructor-agnostic" is falsified, and any source-aware statement must read "for the three conventional reconstructors in the training pool, with the deployed reconstructor's own affine". Within the search of Section 1.3, one precedent exists for equivalence testing on segmentation Dice (Venkatesh et al., 2026) ; it is not a convention of the field.

<!--block:B0070-->
Four qualifications attach to the recipe: it is in-pool only; it holds for these three conventional reconstructors at one setting each, on the registered cylinder, at 20 dB, in simulation; its 0.96 is an addendum value and its no-retraining cost of 19 to 33 points is exploratory; and it is scored against each reconstructor's own cardiac image. A fifth concerns "unseen": pool membership was binary, and implementation variants of one algorithm, whose settings alone change the output substantially (Thürk et al., 2019) , were not tested, so the 16 to 62 points (an upper bound, Section 2.3) are the cost of a different algorithm, not of a variant.

<!--block:B0071-->
### 4.3 Amplitude scales must be compared, and the network's input drawn, before reconstructors are pooled

<!--block:B0072-->
The registered pooled row failed for a reason the preregistration did not anticipate and the pilot did not check, and the failure was found only when the network's normalised inputs were plotted after scoring. Reconstructed EIT amplitude is not a shared currency: within one algorithm it changes with the reconstructed quantity (Grychtol and Adler, 2014b) , and across algorithms it differed here by two orders of magnitude. Where sources are already on comparable scales, as in multi-centre magnetic resonance imaging (MRI), the choice among normalisation methods changes Dice by less than 0.02 (Albert et al., 2023) ; the failure here was not a wrong choice among such methods but the absence of any per-source step. That step can also live in batch-normalisation layers (Karani et al., 2018)  or be learned across datasets (Delisle et al., 2021) ; this study kept it at the input and fixed, so that the network's response to the source difference could be measured alone.

<!--block:B0073-->
### 4.4 The held-out losses resemble those of multi-source studies, and are not directly comparable to them

<!--block:B0074-->
The nearest clinical analogues are a left-ventricle segmentation network that fell from Dice 0.89 to 0.60 when the MRI manufacturer changed (Yan et al., 2020)  and cross-institutional tumour segmentation at 0.59 to 0.68 (AlBadawy et al., 2018) ; the 16 to 62 points lost here and the exploratory 19 to 33 points are of that order, but two differences forbid a comparison of magnitudes: in those studies the label is anatomy and only the input changes with the domain; here the reference is the held-out reconstructor's own cardiac image and changes with it, so this study's losses are upper bounds on the input-side generalisation loss. And those studies used patients and manufacturers; this one used simulation, three conventional algorithms and thirty seeds.

<!--block:B0075-->
The claim that training-source diversity improves out-of-distribution performance (Mårtensson et al., 2020)  was neither seen nor contradicted: in the two in-range cells, two-source pooling against single-source no-retraining showed no evidence in either direction, with only two sources, thirty seeds, intervals of ±2 to ±7 points, and a different affine policy on the two sides, which alone moved these cells by 4 to 14 points in E1. In-pool and out-of-pool performance are reported separately because pooled models can look strong internally and weak externally (Zech et al., 2018) . A reconstructor change is one kind of acquisition shift (Castro et al., 2020) , and that tolerance depends on the kind of shift has a CT analogue in kernel changes being costly where slice-thickness changes were not (Zeng et al., 2022)  and a general one in corruption benchmarks, where a network's tolerance differs by corruption type (Kamann and Rother, 2021; Boone et al., 2023)  . Two next steps lie outside this study: learned harmonisation, which outperforms the location-scale baseline this fixed affine amounts to (Du et al., 2022) , and training-distribution randomisation (Billot et al., 2023) , which three fixed reconstructors are not.

<!--block:B0076-->
### 4.5 Most registered hypotheses were falsified, and that is what a preregistered study reports

<!--block:B0077-->
Of twenty verdict cells, twenty were falsified. Registered Reports return positive results far less often than the standard literature, 44% against 96% in one comparison (Scheel et al., 2021) , and a null against a matched baseline is the kind of result most exposed to under-reporting in computational fields (McGreivy and Hakim, 2024; Borji, 2018; Varoquaux and Cheplygina, 2022)   . Preregistration exists to make such results reportable (Nosek et al., 2018; Chambers and Tzavella, 2021)  , and simulation comparisons can be made to favour any method unless their rules are fixed in advance (Pawel et al., 2024) .

<!--block:B0078-->
The obvious objection is that the registered part governed the least informative cells and every number a reader will quote came from the addenda. Three facts answer it. The addenda were hashed before their runs, with rules, margins and expectations written down, and the hit rates are reported as they fell (M1′ 3 of 3 verdicts, 1 of 3 magnitudes; L1 3 of 3, 1 of 3; L2 3 of 3, 0 of 3); no registered verdict was revised. Both addenda went against the authors' own recipe: the first left the branch below the floor, and the second turned the pooled recipe from "generalises" into "in-pool only". And the second addendum's rows were those a simulated review round, recorded in the repository before the addendum was written, had asked for.

<!--block:B0079-->
### 4.6 Limitations

<!--block:B0080-->
The study is simulated, on one registered cylinder, at one noise level; every other level is outside its scope. Each reconstructor was run at one setting, the three are conventional linear operators, and learned reconstructors were not studied. Held-out losses are upper bounds on the input-side loss; the reference style's contribution was not measured. The three failure modes of Section 3.5 are a one-seed description and their mechanisms were not tested. Only additive Gaussian measurement noise was simulated; electrode and boundary-shape errors, which produce structured artefacts (Boyle and Adler, 2011) , were not. Architectural remedies other than the branch were not tested, and all runs came from one team and code base.

<!--block:B0081-->
The corresponding author is the original author of the semi-Siamese architecture, so this is not a neutral comparison in the sense of Boulesteix et al. (2013) ; preregistration of the rules before the data, and results that went against the authors' own architecture, are the study's answer to that. Finally, the branch's negative difference in eight of nine out-of-distribution cells is a candidate hypothesis for a future preregistration, not a conclusion: it spans two protocols (single-source re-scoring and two-source leave-one-out), and a two-decoder arm may simply have more ways to fail once its control arm has failed.

<!--block:B0082-->
### 4.7 Implications for a hardware study

<!--block:B0083-->
For a planned measurement study with the same reconstructors, these results are design variables, not findings. The per-source affine of each reconstructor and the pooled training row should be registered as design variables; amplitude scales should be compared and the network's inputs drawn before any pooling; and "the same reconstructor" should be defined as algorithm, implementation and hyperparameters together. The primary contrast of such a study is simulation against measurement, with the branch a secondary arm.

<!--block:B0084-->
## 5. Conclusion

<!--block:B0085-->
The question the original study left open has an answer for the three conventional reconstructors it named, in simulation at 20 dB: the separation benefit of a decoder branch for the cardiac component does not appear under a change of reconstructor. Under matched training the branch stayed below the registered floor on GREIT, Gauss–Newton and back-projection; without retraining, its advantage showed no evidence of growing under the shift; in pooled training it stayed below the floor; and on a reconstructor the network had never seen its difference reversed sign. The cost of a reconstructor change was recovered by putting that reconstructor's images into training, by retraining or by pooling with a per-source affine, two remedies that could not be separated at 0.4 points, and by nothing else that was tested. The benefit of pooling stops at the pool boundary: leaving one reconstructor out cost 62, 16 and 36 points on GREIT, Gauss–Newton and back-projection against a margin of ±1.0 point fixed before the runs, an upper bound on the input-side loss because the reference moves with the reconstructor, so the in-pool restriction of the recipe is a tested and falsified generalisation claim, not an assumption. Every verdict followed a rule written and hashed before the data it judged were read. Learned harmonisation, wider randomisation and measured data lie outside this study and are where the next tests belong.

<!--block:B0086-->
## Acknowledgments

<!--block:B0087-->
The authors used Claude (Anthropic; Fable 5.1 and Opus 5.5, accessed September to October 2026) throughout this work. The assistant wrote the analysis, scoring and figure scripts in the project repository that produced every reported number, figure and table, drafted and revised the manuscript text, ran the simulated peer-review panels recorded in the repository, and carried out the citation verification recorded there. The authors defined the research questions, wrote and fixed the preregistration and both addenda before the runs they govern were started, made every design decision, and verified the outputs by re-deriving every reported number from the per-seed result files, by inspecting the plotted model inputs and outputs, and by reading and correcting the text. No figure was generated by an AI tool.

<!--block:B0088-->
## Related manuscript

<!--block:B0089-->
A companion simulation study by the same group, evaluating the same two arms under GREIT across measurement-noise levels, is under review elsewhere and is declared as a related submission; a copy accompanies this submission. The present manuscript relies on none of its reported findings; its GREIT training row re-uses that study's trained networks, re-scored here (Section 2.2). [MATERIAL GAP: preprint DOI, to be inserted when the companion study is posted as a preprint; until then it is not cited.]

<!--block:B0090-->
## References

<!--block:B0091-->
[Vancouver strings generated by `tools/cite.py` from Crossref and PubMed metadata (`refs/prior_works_recon_strings.md`, 2026-10-17), listed below in order of first citation; citation-sequence numbers in the text are applied by format-convert.]

<!--block:B0092-->
1. Frerichs I, Amato MBP, van Kaam AH, Tingay DG, Zhao Z, Grychtol B, et al. Chest electrical impedance tomography examination, data analysis, terminology, clinical use and recommendations: consensus statement of the TRanslational EIT developmeNt stuDy group. Thorax. 2017;72:83-93. doi:10.1136/thoraxjnl-2016-208357
2. Zhao Z, Frerichs I, Pulletz S, Müller-Lisse U, Möller K. The influence of image reconstruction algorithms on linear thorax EIT image analysis of ventilation. Physiol Meas. 2014;35:1083-1093. doi:10.1088/0967-3334/35/6/1083
3. Grychtol B, Elke G, Meybohm P, Weiler N, Frerichs I, Adler A. Functional Validation and Comparison Framework for EIT Lung Imaging. PLoS One. 2014;9:e103045. doi:10.1371/journal.pone.0103045
4. Zhou K, Liu Z, Qiao Y, Xiang T, Loy CC. Domain Generalization: A Survey. IEEE Trans Pattern Anal Mach Intell. 2023;45:4396-4415. doi:10.1109/tpami.2022.3195549
5. Yoon JS, Oh K, Shin Y, Mazurowski MA, Suk HI. Domain Generalization for Medical Image Analysis: A Review. Proc. IEEE. 2024;112:1583-1609. doi:10.1109/jproc.2024.3507831
6. Leathard AD, Brown BH, Campbell J, Zhang F, Morice AH, Tayler D. A comparison of ventilatory and cardiac related changes in EIT images of normal human lungs and of lungs with pulmonary emboli. Physiol Meas. 1994;15:A137-A146. doi:10.1088/0967-3334/15/2a/018
7. Graf M, Riedel T. Electrical impedance tomography: Amplitudes of cardiac related impedance changes in the lung are highly position dependent. PLoS One. 2017;12:e0188313. doi:10.1371/journal.pone.0188313
8. Ko YF, Cheng KS. U-Net-based approach for automatic lung segmentation in electrical impedance tomography. Physiol Meas. 2021;42:025002. doi:10.1088/1361-6579/abe021
9. Ko YF, Cheng KS. Semi-Siamese U-Net for separation of lung and heart bioimpedance images: A simulation study of thorax EIT. PLoS One. 2021;16:e0246071. doi:10.1371/journal.pone.0246071
10. Ko YF, Lin YD, Su PL. Reconstruction of Heart-related Imaging from Lung Electrical Impedance Tomography Using Semi-Siamese U-Net. Curr Med Imaging. 2025;21:e15734056408077. doi:10.2174/0115734056408077250610070821
11. Vandenhende S, Georgoulis S, Van Gansbeke W, Proesmans M, Dai D, Van Gool L. Multi-Task Learning for Dense Prediction Tasks: A Survey. IEEE Trans Pattern Anal Mach Intell. 2022;44:3614-3633. doi:10.1109/tpami.2021.3054719
12. Wang Z, Li X, Sun Y, Wang Q. Electrical Impedance Tomography Deep Imaging With Dual-Branch U-Net Based on Deformable Convolution and Hyper-Convolution. IEEE Trans. Instrum. Meas.. 2024;73:1-16. doi:10.1109/tim.2024.3369160
13. Yu H, Liu H, Liu Z, Wang Z, Jia J. High-resolution conductivity reconstruction by electrical impedance tomography using structure-aware hybrid-fusion learning. Comput Methods Programs Biomed. 2024;243:107861. doi:10.1016/j.cmpb.2023.107861
14. Hamilton SJ, Hauptmann A. Deep D-Bar: Real-Time Electrical Impedance Tomography Imaging With Deep Neural Networks. IEEE Trans Med Imaging. 2018;37:2367-2377. doi:10.1109/tmi.2018.2828303
15. Herzberg W, Hauptmann A, Hamilton SJ. Domain independent post-processing with graph U-nets: applications to electrical impedance tomographic imaging. Physiol Meas. 2023;44:125008. doi:10.1088/1361-6579/ad0b3d
16. Zhang T, Tian X, Liu X, Ye J, Fu F, Shi X, et al. Advances of deep learning in electrical impedance tomography image reconstruction. Front Bioeng Biotechnol. 2022;10:1019531. doi:10.3389/fbioe.2022.1019531
17. Denker A, Margotti F, Ning J, Knudsen K, Nganyu Tanyu D, Jin B, et al. Deep learning based reconstruction methods for electrical impedance tomography. Handbook of Numerical Analysis. 2025:127-175. doi:10.1016/bs.hna.2025.09.003
18. Zech JR, Badgeley MA, Liu M, Costa AB, Titano JJ, Oermann EK. Variable generalization performance of a deep learning model to detect pneumonia in chest radiographs: A cross-sectional study. PLoS Med. 2018;15:e1002683. doi:10.1371/journal.pmed.1002683
19. AlBadawy EA, Saha A, Mazurowski MA. Deep learning for segmentation of brain tumors: Impact of cross‐institutional training and testing. Med Phys. 2018;45:1150-1158. doi:10.1002/mp.12752
20. Liu Q, Dou Q, Yu L, Heng PA. MS-Net: Multi-Site Network for Improving Prostate Segmentation With Heterogeneous MRI Data. IEEE Trans Med Imaging. 2020;39:2713-2724. doi:10.1109/tmi.2020.2974574
21. Hoang-Thi TN, Vakalopoulou M, Christodoulidis S, Paragios N, Revel MP, Chassagnon G. Deep learning for lung disease segmentation on CT: Which reconstruction kernel should be used?. Diagn Interv Imaging. 2021;102:691-695. doi:10.1016/j.diii.2021.10.001
22. Zeng R, Lin CY, Li Q, Jiang L, Skopec M, Fessler JA, et al. Performance of a deep learning‐based CT image denoising method: Generalizability over dose, reconstruction kernel, and slice thickness. Med Phys. 2022;49:836-853. doi:10.1002/mp.15430
23. Hamilton SJ, Hänninen A, Hauptmann A, Kolehmainen V. Beltrami-net: domain-independent deep D-bar learning for absolute imaging with electrical impedance tomography (a-EIT). Physiol Meas. 2019;40:074002. doi:10.1088/1361-6579/ab21b2
24. Karani N, Chaitanya K, Baumgartner C, Konukoglu E. A Lifelong Learning Approach to Brain MR Segmentation Across Scanners and Protocols. Lecture Notes in Computer Science. 2018:476-484. doi:10.1007/978-3-030-00928-1_54
25. Holzschuh JC, Mix M, Freitag MT, Hölscher T, Braune A, Kotzerke J, et al. The impact of multicentric datasets for the automated tumor delineation in primary prostate cancer using convolutional neural networks on 18F-PSMA-1007 PET. Radiat Oncol. 2024;19:106. doi:10.1186/s13014-024-02491-w
26. Lange FJD, Wilcke JC, Hoffmann S, Herrmann M, Boulesteix A. On “Confirmatory” Methodological Research in Statistics and Related Fields. Stat Med. 2025;44:e70303. doi:10.1002/sim.70303
27. Adler A, Lionheart WRB. Uses and abuses of EIDORS: an extensible software base for EIT. Physiol Meas. 2006;27:S25-S42. doi:10.1088/0967-3334/27/5/s03
28. Gagnon H, Cousineau M, Adler A, Hartinger AE. A Resistive Mesh Phantom for Assessing the Performance of EIT Systems. IEEE Trans Biomed Eng. 2010;57:2257-2266. doi:10.1109/tbme.2010.2052618
29. Adler A, Arnold JH, Bayford R, Borsic A, Brown B, Dixon P, et al. GREIT: a unified approach to 2D linear EIT reconstruction of lung images. Physiol Meas. 2009;30:S35-S55. doi:10.1088/0967-3334/30/6/s03
30. Adler A, Guardo R. Electrical impedance tomography: regularized imaging and contrast detection. IEEE Trans Med Imaging. 1996;15:170-179. doi:10.1109/42.491418
31. Thürk F, Elenkov M, Waldmann AD, Böhme S, Braun C, Adler A, et al. Influence of reconstruction settings in electrical impedance tomography on figures of merit and physiological parameters. Physiol Meas. 2019;40:094003. doi:10.1088/1361-6579/ab248e
32. Ronneberger O, Fischer P, Brox T. U-Net: Convolutional Networks for Biomedical Image Segmentation. Lecture Notes in Computer Science. 2015;9351:234-241. doi:10.1007/978-3-319-24574-4_28
33. Vandenhende S, Georgoulis S, Van Gool L, De Brabandere B. Branched Multi-Task Networks: Deciding what layers to share. Proceedings of the British Machine Vision Conference 2020. 2020:59. doi:10.5244/c.34.59
34. Isensee F, Wald T, Ulrich C, Baumgartner M, Roy S, Maier-Hein K, et al. nnU-Net Revisited: A Call for Rigorous Validation in 3D Medical Image Segmentation. Lecture Notes in Computer Science. 2024;15009:488-498. doi:10.1007/978-3-031-72114-4_47
35. Caruana R. Multitask Learning. Machine Learning. 1997;28:41-75. doi:10.1023/a:1007379606734
36. Kurin V, De Palma A, Kostrikov I, Whiteson S, Mudigonda PK. In Defense of the Unitary Scalarization for Deep Multi-Task Learning. Advances in Neural Information Processing Systems 35. 2022:12169-12183. doi:10.52202/068431-0884
37. Xin D, Ghorbani B, Gilmer J, Garg A, Firat O. Do Current Multi-Task Optimization Methods in Deep Learning Even Help?. Advances in Neural Information Processing Systems 35. 2022:13597-13609. doi:10.52202/068431-0988
38. Kendall A, Gal Y, Cipolla R. Multi-task Learning Using Uncertainty to Weigh Losses for Scene Geometry and Semantics. 2018 IEEE/CVF Conference on Computer Vision and Pattern Recognition. 2018:7482-7491. doi:10.1109/cvpr.2018.00781
39. Renard F, Guedria S, Palma ND, Vuillerme N. Variability and reproducibility in deep learning for medical image segmentation. Sci Rep. 2020;10:13724. doi:10.1038/s41598-020-69920-0
40. Pulletz S, Genderingen HRv, Schmitz G, Zick G, Schädler D, Scholz J, et al. Comparison of different methods to define regions of interest for evaluation of regional lung ventilation by EIT. Physiol Meas. 2006;27:S115-S127. doi:10.1088/0967-3334/27/5/s10
41. Jeschke J, Ivanenko M, Smolik WT, Wanta D, Midura M, Wróblewski P. Machine Learning-Based Image Reconstruction in Wearable CC-EIT of the Thorax: Robustness to Electrode Displacement. Sensors (Basel). 2025;25:6543. doi:10.3390/s25216543
42. Yu H, Zhang X, Xu R, Liu J, He Y, Cui P. Rethinking the Evaluation Protocol of Domain Generalization. 2024 IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR). 2024:21897-21908. doi:10.1109/cvpr52733.2024.02068
43. Willroth EC, Atherton OE. Best Laid Plans: A Guide to Reporting Preregistration Deviations. Advances in Methods and Practices in Psychological Science. 2024;7:25152459231213802. doi:10.1177/25152459231213802
44. Wilcoxon F. Individual Comparisons by Ranking Methods. Biometrics Bulletin. 1945;1:80. doi:10.2307/3001968
45. Schuirmann DJ. A comparison of the Two One-Sided Tests Procedure and the Power Approach for assessing the equivalence of average bioavailability. J Pharmacokinet Biopharm. 1987;15:657-680. doi:10.1007/bf01068419
46. Lakens D. Equivalence Tests: A Practical Primer for t Tests, Correlations, and Meta-Analyses. Soc Psychol Personal Sci. 2017;8:355-362. doi:10.1177/1948550617697177
47. Lakens D, Scheel AM, Isager PM. Equivalence Testing for Psychological Research: A Tutorial. Advances in Methods and Practices in Psychological Science. 2018;1:259-269. doi:10.1177/2515245918770963
48. Lakens D. Calculating and reporting effect sizes to facilitate cumulative science: a practical primer for t-tests and ANOVAs. Front Psychol. 2013;4:863. doi:10.3389/fpsyg.2013.00863
49. Christodoulou E, Reinke A, Houhou R, Kalinowski P, Erkan S, Sudre CH, et al. Confidence Intervals Uncovered: Are We Ready for Real-World Medical Imaging AI?. Lecture Notes in Computer Science. 2024;15010:124-132. doi:10.1007/978-3-031-72117-5_12
50. Myronenko A. 3D MRI Brain Tumor Segmentation Using Autoencoder Regularization. Lecture Notes in Computer Science. 2019;11384:311-320. doi:10.1007/978-3-030-11726-9_28
51. Venkatesh V, Bathala L, Mathew RS, Yalavarthy PK. Performance benchmarking of deep learning models for real‐time median nerve segmentation and cross‐sectional area measurement in ultrasound imaging. Med Phys. 2026;53:e70414. doi:10.1002/mp.70414
52. Grychtol B, Adler A. Choice of reconstructed tissue properties affects interpretation of lung EIT images. Physiol Meas. 2014;35:1035-1050. doi:10.1088/0967-3334/35/6/1035
53. Albert S, Wichtmann BD, Zhao W, Maurer A, Hesser J, Attenberger UI, et al. Comparison of Image Normalization Methods for Multi-Site Deep Learning. Applied Sciences. 2023;13:8923. doi:10.3390/app13158923
54. Delisle PL, Anctil-Robitaille B, Desrosiers C, Lombaert H. Realistic image normalization for multi-Domain segmentation. Med Image Anal. 2021;74:102191. doi:10.1016/j.media.2021.102191
55. Yan W, Huang L, Xia L, Gu S, Yan F, Wang Y, et al. MRI Manufacturer Shift and Adaptation: Increasing the Generalizability of Deep Learning Segmentation for MR Images Acquired with Different Scanners. Radiol Artif Intell. 2020;2:e190195. doi:10.1148/ryai.2020190195
56. Mårtensson G, Ferreira D, Granberg T, Cavallin L, Oppedal K, Padovani A, et al. The reliability of a deep learning model in clinical out-of-distribution MRI data: A multicohort study. Med Image Anal. 2020;66:101714. doi:10.1016/j.media.2020.101714
57. Castro DC, Walker I, Glocker B. Causality matters in medical imaging. Nat Commun. 2020;11:3673. doi:10.1038/s41467-020-17478-w
58. Kamann C, Rother C. Benchmarking the Robustness of Semantic Segmentation Models with Respect to Common Corruptions. Int J Comput Vis. 2021;129:462-483. doi:10.1007/s11263-020-01383-2
59. Boone L, Biparva M, Mojiri Forooshani P, Ramirez J, Masellis M, Bartha R, et al. ROOD-MRI: Benchmarking the robustness of deep learning segmentation models to out-of-distribution and corrupted data in MRI. Neuroimage. 2023;278:120289. doi:10.1016/j.neuroimage.2023.120289
60. Du D, Lv W, Lv J, Chen X, Wu H, Rahmim A, et al. Deep learning–based harmonization of CT reconstruction kernels towards improved clinical task performance. Eur Radiol. 2022;33:2426-2438. doi:10.1007/s00330-022-09229-w
61. Billot B, Greve DN, Puonti O, Thielscher A, Van Leemput K, Fischl B, et al. SynthSeg: Segmentation of brain MRI scans of any contrast and resolution without retraining. Med Image Anal. 2023;86:102789. doi:10.1016/j.media.2023.102789
62. Scheel AM, Schijen MRMJ, Lakens D. An Excess of Positive Results: Comparing the Standard Psychology Literature With Registered Reports. Advances in Methods and Practices in Psychological Science. 2021;4:25152459211007467. doi:10.1177/25152459211007467
63. McGreivy N, Hakim A. Weak baselines and reporting biases lead to overoptimism in machine learning for fluid-related partial differential equations. Nat Mach Intell. 2024;6:1256-1269. doi:10.1038/s42256-024-00897-5
64. Borji A. Negative results in computer vision: A perspective. Image and Vision Computing. 2018;69:1-8. doi:10.1016/j.imavis.2017.10.001
65. Varoquaux G, Cheplygina V. Machine learning for medical imaging: methodological failures and recommendations for the future. NPJ Digit Med. 2022;5:48. doi:10.1038/s41746-022-00592-y
66. Nosek BA, Ebersole CR, DeHaven AC, Mellor DT. The preregistration revolution. Proc Natl Acad Sci U S A. 2018;115:2600-2606. doi:10.1073/pnas.1708274114
67. Chambers CD, Tzavella L. The past, present and future of Registered Reports. Nat Hum Behav. 2021;6:29-42. doi:10.1038/s41562-021-01193-7
68. Pawel S, Kook L, Reeve K. Pitfalls and potentials in simulation studies: Questionable research practices in comparative simulation studies allow for spurious claims of superiority of any method. Biom J. 2024;66:2200091. doi:10.1002/bimj.202200091
69. Boyle A, Adler A. The impact of electrode area, contact impedance and boundary shape on EIT images. Physiol Meas. 2011;32:745-754. doi:10.1088/0967-3334/32/7/s02
70. Boulesteix AL, Lauer S, Eugster MJA. A Plea for Neutral Comparison Studies in Computational Sciences. PLoS One. 2013;8:e61562. doi:10.1371/journal.pone.0061562

<!--block:B0093-->
## Supporting information

<!--block:B0094-->
**S1 Table.** Per-seed heart- and lung-channel Dice for every cell of the design (three matched, six no-retraining, two pooled, three held-out rows with their in-pool references), with the registered secondary-path values, E1, M3′ and L3′ in full.

<!--block:B0095-->
**S2 Table.** Pilot checks, the two recorded deviations, the four preregistration hashes and the training records (epochs and wall time per row and arm).

<!--block:B0096-->
**S3 Fig.** Seed-0 diagnostics: the network's input under each affine path for the six no-retraining cells, and the input, output and target of each held-out cell with the background-subtraction check.

<!--block:B0097-->
**S1 Appendix.** The preregistration in its four hashed states, with the hash file.

<!--block:B0098-->
## Figure captions

<!--block:B0099-->
**Fig 1. Three reconstructors, one geometry, three amplitude scales.** One test geometry at 20 dB reconstructed by GREIT, one-step Gauss–Newton and back-projection (mixed input and single-organ heart target for each), and the three training-split amplitude distributions on a common axis. GREIT's standard deviation is 161 times GN's and 188 times BP's.

<!--block:B0100-->
**Fig 2. The design matrix and its heart-Dice values.** Rows are training conditions (GREIT, GN, BP; mixed, registered single affine; mixed-ps, per-source affine; loro-GREIT, loro-GN, loro-BP), columns are evaluation reconstructors, cells give mean heart Dice over seeds 0–29 for B_wide and D. Diagonal cells are matched training; off-diagonal single-source cells are evaluation without retraining under the training set's affine; held-out cells of the loro rows are marked. Standing of each row is given at the left.

<!--block:B0101-->
**Fig 3. What the network saw under a single pooled affine and under per-source affines.** The same GREIT, GN and BP test frames after the registered pooled affine (top) and after per-source standardisation (bottom), on one colour scale, with the within-frame standard deviation printed. Under the single affine the GN and BP inputs vary by 1/132 and 1/156 of a GREIT input.

<!--block:B0102-->
**Fig 4. Seed 0 of the three held-out cells.** For each loro row, the held-out reconstructor's input, the B_wide and D predictions of the heart channel, and the target, in image units; printed values are the prediction's peak relative to the target's peak and its background median. Descriptive of one seed in thirty; the cell-level values are in Table 3.

<!--block:B0103-->
**Fig 5. The remedies tested for a reconstructor change, at matched parameter count.** Heart Dice of the control arm (B_wide, with D beside) for retraining on the deployed reconstructor (registered), pooled training with the deployed reconstructor in the pool (first addendum), pooled training with the deployed reconstructor outside the pool (second addendum), and single-source training evaluated on another reconstructor without retraining (registered; the two in-range cells), with 95% bootstrap intervals, and the branch's difference D − B_wide in each layer. Each column states its standing.

<!--block:B0104-->
## Tables

<!--block:B0105-->
**Table 1. Matched-training cells and the pooled rows.** Heart-channel Dice, test split, seeds 0–29 (n = 30). Δ = D − B_wide in Dice points (0.01); 95% CI by percentile bootstrap over paired seeds (100,000 resamples); floor = B_wide's seed-to-seed SD; W = Wilcoxon signed-rank statistic; p two-sided with continuity correction. Standing: R = registered (hash 4b4c7a6d…), A1 = first addendum (0060eedf…), ref = reference, not tested.

<!--block:B0106-->
| Cell (train → evaluate) | Standing | B_wide Dice (mean ± SD) | D Dice (mean ± SD) | Δ (points) | 95% CI | Floor | dz | W | p | D > B_wide | Verdict |
|---|---|---|---|---|---|---|---|---|---|---|---|
| R1-GN (GN → GN) | R | 0.9639 ± 0.0045 | 0.9672 ± 0.0029 | +0.323 | [+0.18, +0.47] | 0.449 | +0.79 | 48 | 1.5e−04 | 27/30 | falsified |
| R1-BP (BP → BP)¹ | R | 0.9565 ± 0.0066 | 0.9628 ± 0.0031 | +0.631 | [+0.40, +0.88] | 0.664 | +0.91 | 29 | 3.0e−05 | 26/30 | falsified |
| GREIT → GREIT | ref | 0.9575 ± 0.0034 | 0.9602 ± 0.0036 | +0.271 | [+0.11, +0.43] | 0.343 | +0.58 | 104 | 0.0085 | 23/30 | falsified |
| M1 (mixed → GREIT) | R | 0.9463 ± 0.0095 | 0.9472 ± 0.0125 | +0.094 | [−0.53, +0.70] | 0.954 | +0.05 | 211 | 0.67 | 16/30 | falsified |
| M1 (mixed → GN)² | R | 0.4514 ± 0.2991 | 0.4489 ± 0.2450 | −0.245 | [−14.32, +13.97] | 29.909 | -0.01 | 221 | 0.82 | 12/30 | falsified |
| M1 (mixed → BP)¹ ² | R | 0.4065 ± 0.2956 | 0.4008 ± 0.2469 | −0.562 | [−14.54, +13.38] | 29.560 | -0.01 | 230 | 0.97 | 16/30 | falsified |
| M1′ (mixed-ps → GREIT) | A1 | 0.9611 ± 0.0017 | 0.9610 ± 0.0051 | −0.015 | [−0.23, +0.17] | 0.173 | -0.03 | 209 | 0.64 | 16/30 | falsified |
| M1′ (mixed-ps → GN) | A1 | 0.9662 ± 0.0025 | 0.9682 ± 0.0026 | +0.201 | [+0.07, +0.32] | 0.248 | +0.58 | 70 | 8.6e−04 | 24/30 | falsified |
| M1′ (mixed-ps → BP)¹ | A1 | 0.9579 ± 0.0053 | 0.9619 ± 0.0053 | +0.404 | [+0.11, +0.69] | 0.531 | +0.49 | 95 | 0.0048 | 24/30 | falsified |

<!--block:B0107-->
¹ BP single-organ peaks are offset from GREIT's by up to 2 px on the 64 × 64 raster (one pixel of BP's native grid; preregistration §10). ² Under the single pooled affine the GN and BP inputs vary by 1/132 and 1/156 of a GREIT input (Section 3.3); the registered verdict stands, and the cell is not read as evidence about pooled training.

<!--block:B0108-->
M2′ (A1; reported, not tested): mixed-ps → Y minus Y → Y, paired by seed, points [95% CI]: B_wide: mixed-ps→GREIT − GREIT→GREIT +0.360 [+0.23, +0.50]; D: mixed-ps→GREIT − GREIT→GREIT +0.074 [−0.17, +0.30]; B_wide: mixed-ps→GN − GN→GN +0.229 [+0.08, +0.38]; D: mixed-ps→GN − GN→GN +0.107 [−0.01, +0.22]; B_wide: mixed-ps→BP − BP→BP +0.143 [−0.14, +0.43]; D: mixed-ps→BP − BP→BP −0.083 [−0.32, +0.13]. Registered M2 (R; mixed → Y minus Y → Y): B_wide: mixed→GREIT − GREIT→GREIT −1.1 [−1.5, −0.8]; D: mixed→GREIT − GREIT→GREIT −1.3 [−1.8, −0.9]; B_wide: mixed→GN − GN→GN −51.3 [−61.5, −40.5]; D: mixed→GN − GN→GN −51.8 [−60.2, −43.0]; B_wide: mixed→BP − BP→BP −55.0 [−65.2, −44.3]; D: mixed→BP − BP→BP −56.2 [−64.5, −47.2].

<!--block:B0109-->
**Table 2. Reconstructor change without retraining: the six registered R3 cells, the exploratory E1 re-scoring and M3′.** Difference of differences (DoD) = Δ(X→Y) − Δ(X→X) in points, 95% percentile bootstrap CI over paired seeds; SD = seed SD of the DoD; MDE80 = DoD detectable with 80% power at n = 30 (paired-t approximation, dz 0.53); input state from the seed-0 diagnosis (within-frame SD of the network's input under the training set's affine; diagonal ≈ 0.82). Standing: R = registered; E = exploratory, no verdict (A1); A1 = first addendum, reported, not tested.

<!--block:B0110-->
| Cell X → Y | Input state (R path) | Δ(X→Y) R | DoD R (points) | 95% CI | SD | MDE80 | Verdict (R) | Δ(X→Y) E1 | DoD E1 (points) | 95% CI | B_wide / D Dice under E1 | M3′ B_wide / D (A1) |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| GREIT → GN | degenerate (near-constant) | −7.66 | −7.93 | [−12.94, −3.47] | 13.5 | 7.2 | falsified | −5.00 | −5.27 | [−6.10, −4.45] | 0.737 / 0.686 | +22.7 / +30.6 |
| GREIT → BP¹ | degenerate (near-constant) | −0.80 | −1.07 | [−7.29, +4.39] | 16.6 | 8.8 | falsified | −7.50 | −7.77 | [−12.03, −3.38] | 0.710 / 0.635 | +22.6 / +23.8 |
| GN → GREIT | over-range | −1.53 | −1.85 | [−8.32, +4.24] | 17.9 | 9.5 | falsified | −5.77 | −6.09 | [−9.06, −3.44] | 0.713 / 0.656 | +28.7 / +30.2 |
| GN → BP¹ | in range | −9.73 | −10.05 | [−20.34, +0.50] | 29.8 | 15.8 | falsified | −1.87 | −2.20 | [−10.80, +6.54] | 0.647 / 0.629 | +34.7 / +44.8 |
| BP → GREIT¹ | over-range | −5.50 | −6.13 | [−12.18, −0.06] | 17.3 | 9.2 | falsified | +1.91 | +1.28 | [−3.06, +4.61] | 0.739 / 0.758 | +33.8 / +39.3 |
| BP → GN¹ | in range | +3.60 | +2.97 | [−0.12, +5.84] | 8.5 | 4.5 | falsified | −5.19 | −5.82 | [−13.13, +1.28] | 0.767 / 0.715 | +15.1 / +11.7 |

<!--block:B0111-->
¹ BP raster offset, see Table 1. The registered secondary path (evaluation set's affine for input and output) is listed and not read, because it moves the output's background off zero (Section 3.2): DoD GREIT → GN −5.20 [−6.11, −4.25]; GREIT → BP −5.08 [−9.35, −0.73]; GN → GREIT −2.10 [−3.33, −0.94]; GN → BP −2.38 [−4.47, −0.24]; BP → GREIT +0.13 [−1.99, +2.17]; BP → GN +3.14 [+0.63, +5.48].

<!--block:B0112-->
**Table 3. Leave-one-reconstructor-out rows (second addendum, hash 9589b298…).** Held-out cell loro-Y → Y: the network never saw Y. L1: B_wide on loro-Y → Y minus B_wide on mixed-ps → Y, paired by seed, 95% percentile bootstrap CI, margin ±1.0 point fixed before the runs (D beside, not tested). L2: Δ = D − B_wide on loro-Y → Y under the R1 rule. L3′ (reported, not tested): loro-Y → Y minus Y → Y, and minus the two registered no-retraining cells X → Y (in-range cells only; the four cells crossing GREIT carry the degenerate/over-range note and are in S1 Table). In-pool references: the same rows evaluated on their two pool members.

<!--block:B0113-->
| Held-out Y | B_wide Dice (mean ± SD) | D Dice (mean ± SD) | B_wide per-seed min–max | L1: B_wide loss vs mixed-ps (points) [95% CI] | L1 verdict | D loss (not tested) | L2: Δ (points) [95% CI] | Floor | dz | W | p | D > B_wide | L2 verdict | Lung Dice B_wide / D |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| GREIT | 0.3431 ± 0.0949 | 0.3115 ± 0.0824 | 0.187–0.504 | -61.8 [−65.1, −58.5] | falsified | -64.9 [−67.9, −62.0] | −3.2 [−7.5, +1.3] | 9.49 | -0.25 | 153 | 0.10 | 10/30 | falsified | 0.914 / 0.922 |
| GN | 0.8082 ± 0.0254 | 0.7691 ± 0.0279 | 0.729–0.858 | -15.8 [−16.7, −14.9] | falsified | -19.9 [−20.9, −18.9] | −3.9 [−5.3, −2.4] | 2.54 | -0.95 | 45 | 1.2e−04 | 4/30 | falsified | 0.927 / 0.931 |
| BP¹ | 0.5995 ± 0.0949 | 0.5748 ± 0.1387 | 0.323–0.709 | -35.8 [−39.4, −32.7] | falsified | -38.7 [−43.8, −33.9] | −2.5 [−8.1, +3.2] | 9.49 | -0.15 | 197 | 0.47 | 16/30 | falsified | 0.789 / 0.788 |

<!--block:B0114-->
¹ BP raster offset, see Table 1. In-pool references (B_wide / D Dice): loro-GREIT → GN 0.9653 / 0.9660; loro-GREIT → BP 0.9585 / 0.9619; loro-GN → GREIT 0.9605 / 0.9622; loro-GN → BP 0.9568 / 0.9619; loro-BP → GREIT 0.9605 / 0.9620; loro-BP → GN 0.9653 / 0.9673. L3′ relative to specialised training (loro-Y → Y minus Y → Y), points [95% CI]: B_wide: loro-GREIT→GREIT − GREIT→GREIT −61.4 [−64.8, −58.1]; D: loro-GREIT→GREIT − GREIT→GREIT −64.9 [−67.8, −62.0]; B_wide: loro-GN→GN − GN→GN −15.6 [−16.5, −14.7]; D: loro-GN→GN − GN→GN −19.8 [−20.8, −18.8]; B_wide: loro-BP→BP − BP→BP −35.7 [−39.3, −32.6]; D: loro-BP→BP − BP→BP −38.8 [−43.9, −34.1]. L3′ relative to the two in-range no-retraining cells: B_wide: loro-GN→GN − BP→GN −0.7 [−2.2, +0.8]; D: loro-GN→GN − BP→GN −8.2 [−10.4, −5.5]; B_wide: loro-BP→BP − GN→BP −1.2 [−7.4, +5.2]; D: loro-BP→BP − GN→BP +6.1 [−1.1, +13.0].

<!--block:B0115-->
**Table 4. The four SHA-256 states of the preregistration file: what each governs and what had been read when it was written.** The hash of each state is written into the metadata of every training run it governs; the four full texts and the hash file are deposited with the minimal dataset.

<!--block:B0116-->
| State (date) | SHA-256 (prefix) | Governs | Written after reading | Fixed before the runs |
|---|---|---|---|---|
| Registered (2026-09-26) | 4b4c7a6d… | R1 (2 cells), R3 (6 cells), M1 (3 cells); rules, interpretations in both outcomes, n = 30, pilot | Nothing: no arm trained, no contrast computed | All of the above |
| Deviation record (2026-10-03) | 3fdc703d… | Two §10 entries (GN noise-figure band; BP 2-px raster offset) | Pilot files only; no cell of the matrix | No hypothesis, endpoint, arm, setting, n or rule changed |
| First addendum (2026-10-03) | 0060eedf… | mixed-ps row: M1′ (3 cells, R1 rule), M2′, M3′ (reported), E1 (exploratory, no verdict) | All 12 registered cells and the 9 secondary-path cells | Row, scoring path, data gate, rule, expectation (3 falsifications, +0.27 to +0.63), readings of both outcomes |
| Second addendum (2026-10-11) | 9589b298… | loro-GREIT, loro-GN, loro-BP: L1 (equivalence, ±1.0 point), L2 (R1 rule), L3′ and in-pool references (reported) | The first addendum's results (M1′, M2′, M3′, E1) and the first review round | Rows, scoring path, data gate, margin and its reasons, rules, expectations (L1: 3 falsifications, 5–30 points; L2: 3 falsifications, −0.02 to +0.63), readings of both outcomes |

<!--block:B0117-->

<!--block:B0118-->
---

<!--block:B0119-->
