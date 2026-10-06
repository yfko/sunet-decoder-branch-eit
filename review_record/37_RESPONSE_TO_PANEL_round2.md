# Response to the Round-2 panel (Sci Rep version) — SUnet core paper, revision round 3 (2026-10-06)

**Panel**: `33_REVIEWER_PANEL_round2_scirep.md` (five seats in separate contexts, Major Revision; letter sha256 `68741c66…`). Immutable roadmap: `revision-authority-round3/roadmap.json` (REV-R3-1…15, sha256 `a3b4e7a0…`), transcribed from the letter's REV-1…15 in source order.
**Author triage**: every item `will_address` (PI, 2026-10-06; `author_event_20261006.txt`; sidecar `author-adjudication.json`, sha256 `ac94e797…`).
**Base**: `29_DRAFT_v3.md` (anchored, 126 blocks, hash `0a5114777ca6`). **Revised**: `34_DRAFT_v4.md` by deterministic patch apply (`phase6_revision/revision_patch_round3.json`, 28 ops, digest `7fed3136…`; `34_DRAFT_v4.md.apply-report.json`, format 1.3, authorization witness PASS, 99/126 blocks byte-identical, one new block B0127, three §4 heading changes acknowledged as structural). Output hash `67570787bd55`.
**Deliverable**: `36_SUBMISSION_scirep_v4.{md,docx,pdf}` (abstract from `31_ABSTRACT_SCIREP_bilingual.md`, 199 words; 54 references in Nature style; figures renumbered by first citation).
**New analysis**: Table S9 (`results/tables/table_s9_sweep_all_arms.md`, `results/sweep_all_arms_heart.json`), computed from the registered per-seed files `results_v2_snr*_heart_fix/per_seed.csv`. No new training.
**Citation audit after the change**: `35_CITATION_AUDIT_v4.md` (54 entries, 67 in-text uses, zero orphans, self-citation 3/54).

Facts checked against code and registered files before the text was written (recorded in the header of `phase6_revision/emit_patch_round3.py`): `tools/evaluate.py` line 157 calls `scipy.stats.wilcoxon(a, b)` with defaults (asymptotic, no continuity correction above n = 50); `PREREGISTRATION_HEART.md` lines 192–213 size n from the pre-correction Study 1 dz = 0.500 (29% at n = 10) scaled to 0.376 → 58; `results_v1_heart_fix/summary.json` gives the post-correction Study 1 D − B_wide dz = 0.336; `tools/gen_dataset.m` places lung centres at (±1.0, 0.1) and the heart at (0, 0.1) with radii ≤ 0.60 and ≤ 0.30 and jitter ±0.05, so the largest radii sum (0.90) equals the smallest centre distance and the organs cannot overlap; Table S9 from the registered per-seed files. One further check made while writing this letter: at 60, 50 and 40 dB the mean of per-seed relative error reductions is +1.1%, +1.4% and +3.5% against ratios of means of +5.0%, +5.2% and +6.5% (4.5-, 3.7- and 1.9-fold), and from 35 dB down the two agree within 20%, which is what §3.2 now states.

Nothing registered was touched: numbers, H1–H5 verdicts, the §3 registered results, `PREREGISTRATION*.md`, `RESULTS_*.md`.

---

## Required revisions (must_fix)

### REV-R3-1 — The addendum cannot apportion the evaluation-only benefit between mismatch tolerance and weak-component protection (R1-W2, DA-M1; DA-M3 shares the surface) — **addressed**

**The panel's point.** Retraining at 20 dB removed the training–evaluation mismatch and, by the paper's own operational definition of "under threat" (the control arm's loss), the threat at the same time; the sentences saying "most of the benefit is mismatch tolerance" apportion what the design cannot, and the §1 statement receives no verdict in the matched condition.

**What changed and where.** Every sentence that apportioned has been returned to the registered reading of the addendum ("attributable in whole or in part to distribution-shift tolerance"), and the paper now says in each place that the two were removed together and are not apportioned.
- Abstract (B0005, mirrored in `31_`): the closing sentence is now "Retraining removed the training–evaluation mismatch and the control arm's loss together, so the evaluation-only benefit is attributed to mismatch tolerance in whole or in part, unapportioned." The former "most of that benefit is mismatch tolerance" is gone.
- §1 last paragraph (B0013): the contribution sentence no longer claims to say "how much of that sensitivity belongs to the training condition rather than to the network"; it now reads "of what becomes of that sensitivity when the network is trained at the level at which it is evaluated". The paragraph closes with the verdict the panel asked for: "When the network is instead trained at the heavier level, that benefit disappears together with the loss it accompanied, and the statement under test receives no separate verdict in the matched condition, for a reason Section 4.1 sets out."
- §3.5 closing paragraph (B0125): one sentence added after the registered reading: "Retraining at 20 dB removed the training-evaluation mismatch and the control arm's loss of the cardiac component together (8.8 points lost at 20|40 against 0.8 at 20|20), so the addendum does not say how much of the evaluation-only benefit belongs to each reading, and this paper does not apportion it."
- §4.1 heading (B0050): "What the addendum does and does not attribute" (replacing the heading that asserted the benefit "belongs mostly to the training-evaluation mismatch").
- §4.1 first paragraph (B0051): "this prediction does not hold once training and evaluation are matched" replaces "holds only while … mismatched"; the closing sentence "The design that can distinguish them found that most of the effect is the latter" is replaced by three sentences stating that the addendum changed two things at once (unseen noise gone; control-arm loss 8.8 → 0.8 points), that it therefore removed the mismatch and the threat together, and that under the pre-fixed reading the result is attributable to shift tolerance in whole or in part "and the design cannot say which".
- §4.1 second paragraph (B0052): "the larger part of the evaluation-only advantage is distribution-shift tolerance" is replaced by "the retrained condition does not separate them either, because on this phantom the threat arose only through the mismatch. What the addendum establishes is narrower and sufficient for practice: the benefit does not survive matched training, whichever reading of its cause is preferred." "What the addendum adds is that the threat, so defined, is largely a threat to a network that has not seen the noise before" became "did not survive training at the heavier level".
- §5 (B0064): "most of what it was worth in the evaluation-only sweep was tolerance of noise the network had not seen" is replaced by "what it was worth in the evaluation-only sweep did not survive training on that noise", and the shrinkage sentence now says the change "removes the training-evaluation mismatch and the control arm's loss together, so the design attributes the evaluation-only benefit to tolerance of unseen noise in whole or in part and does not apportion it."

**What did not change and why.** The registered reading sentence in §3.5 and the H3 and H5 verdicts are untouched. One sentence that contains "most" remains, in §3.5 (B0123): "Most of the gap that the branch closed in the evaluation-only sweep is closed by training at the operating level alone." It states a measured quantity (the control arm recovers 8.0 of the 8.8 points by retraining) and does not attribute the benefit to one reading over the other, so it was left as it is. R3-W5 (the shift-tolerance result is undersold to the robustness reader) is served inside the registered wording, as the letter's arbitration asked: the abstract and §5 keep the shift-tolerance reading visible ("in whole or in part") without apportioning.

### REV-R3-2 — n = 58 was sized for the p-condition only; the floor demands a standardised effect near 1; the dz 0.376 and 29% figures were not reproducible from the stated numbers (R1-W1, R1-W4) — **addressed as a disclosure, not a redesign**

**The panel's point.** §2.4 presented n = 58 as if it powered the whole registered rule, and the figures 0.376 and 29% could not be derived from the post-correction Study 1 contrast (dz = 0.34).

**What changed and where.**
- §2.4 sample-size paragraph (B0029) now states the registered chain in full: Study 1's heart contrast as it stood before the scoring correction, dz = 0.500 (about 29% power at n = 10), scaled by the pilot's larger variance to dz ≈ 0.376, requiring 58 seeds for 80% power on the Wilcoxon condition at p < 0.05; that after the correction Study 1's contrast is dz = 0.34; that the calculation covered the p-condition only; that the floor condition (0.670 points at 40 dB against a paired-difference SD of 0.83 points) asks for a standardised effect of about 0.8; and that "the registered rule as a whole therefore had little power to confirm at the anticipated effect: it was sized to detect that effect, and it would confirm only an effect roughly twice as large. This is a property of the rule as registered, stated here rather than revised."
- §2.1 (B0017): the Study 1 secondary outcome now says "dz = 0.34 after the scoring correction of Section 2.5; the preregistration's sample-size calculation used the pre-correction estimate, Section 2.4", so the two effect sizes are stated consistently and the reader is told which one fed the calculation.
- §4.2 (B0055): one sentence added: the floor "asks for a difference of about 0.8 standard deviations of the paired difference, while the sample was sized for an effect of 0.376 on the p-condition (Section 2.4), so the study was powered to detect the anticipated effect, not to confirm the rule at it."

**What did not change and why.** The rule, the floor and n = 58 are as registered and are not revised; the preregistration file is not edited. The "about 0.8" is the floor divided by the observed paired-difference SD at 40 dB; the panel's "dz near 1" is the same quantity read against the seed-to-seed SD of one arm, and the text gives the number rather than the label.

### REV-R3-3 — The phantom's heart is spatially disjoint from the lungs while §1 motivates the problem with overlap (R2-W1) — **addressed**

**The panel's point.** The manuscript did not say that the in-vivo spatial-overlap difficulty is absent from the phantom by construction.

**What changed and where.**
- §2.3 (B0023) now gives the geometry: lung centres at (±1.0, 0.1), heart centre at (0, 0.1), jitter ±0.05, and the consequence: "The heart inclusion therefore lies between the lung inclusions and never overlaps them: the largest radii sum to 0.90 model units and the centres are never closer than that. The in-vivo situation in which the cardiac-related signal is distributed within the ventilated lung (Section 1) is absent from this phantom by construction. The difficulty it reproduces is amplitude, together with the blurring by which the reconstruction spreads each inclusion into its neighbour's region."
- Limitation three (B0062): "in particular the heart inclusion never overlaps the lung inclusions (Section 2.3), so the spatial overlap of the cardiac-related signal with the ventilated lung that in-vivo separation must contend with was not part of the task, and the weak-component difficulty tested here is one of amplitude and reconstruction blur only."
- §1 first paragraph (B0009): the premise measurement is introduced as made "on the simulated phantom used throughout this paper, in which the heart inclusion lies beside the lung inclusions rather than within the lung field (Section 2.3)".

**What did not change and why.** The in-vivo motivation (Leathard, Graf) stays in §1 because it is what the field's problem is; the paper now says which part of that problem the phantom reproduces. The generator's `overlap` column exists and is zero at these registered parameters; the geometry was not changed.

### REV-R3-4 — §3.1 called the 0.22-point contrast "a near-zero residual whose sign happened to be positive" while §3.5 treats it as reproducible (DA-M3) — **addressed**

**The panel's point.** Two incompatible descriptions of the same number.

**What changed and where.** §3.1 last paragraph (B0038): the sentence is replaced by "It is a small difference that the data resolve: its seed-level and geometry-level intervals both exclude zero (Section 3.5), it is unrelated at the seed level to the 20 dB effect, and it is one third of the registered floor." The preceding sentence, that the positive mean at 40 dB is not a small version of the low-SNR effect, stays, because the seed-level correlation (ρ = −0.10) supports it.

**What did not change and why.** §3.5 and §5 already described the contrast as reproducible and below the floor; they were not altered for this item, so the two sections now say the same thing.

---

## Suggested revisions (should_fix)

### REV-R3-5 — Stated implication outruns the tested cell; onset without the descriptive label; a paragraph that addresses reviewers (R3-W4, R1-W11, EIC-W2; CONSENSUS-3) — **addressed**

- §5 closing sentence (B0064) is scoped: "On this phantom, with this reconstructor and this noise model, an architectural comparison without its measurement-chain and training-condition context would have returned a different answer at every level, and the value of this branch was a property of that combination rather than of the branch."
- The onset carries the label in the Abstract ("a descriptive onset at 35–30 dB") and in §5 ("beginning, descriptively, between 35 and 30 dB").
- §1 (B0012): "Three questions follow directly, and it is better to answer them here than to leave them to a reviewer" and the question-and-answer form are replaced by "Three distinctions follow." and three declarative sentences for readers.

### REV-R3-6 — Width is an unexcluded rival for the evaluation-only 20 dB advantage; the sweep reported no B, C or C_wide rows (DA-M2) — **addressed by re-analysis of existing files**

- All five arms had been scored at every sweep level; Table S9 reports them with the four contrasts the DA asked for. New paragraph in §3.2 (B0127, inserted after B0043): B_wide − B lies between −0.12 and −0.01 points across the seven levels (−0.124 points at 20 dB, CI −0.499 to +0.238, 28 of 58 seeds); C_wide − C is at most +0.03 points; D − B tracks the registered contrast level for level (+1.973 at 20 dB, CI +1.621 to +2.328, 54 of 58 seeds, against +2.097 for D − B_wide); the late split C_wide − B_wide reaches +0.425 points at 20 dB (CI +0.003 to +0.851). Conclusion as written: "The evaluation-only advantage therefore belongs to the position of the split, not to decoder width, and the capacity control removes 0.12 points of it at most."
- Supplementary list (B0083) adds S9; §2.6 (B0034) lists these contrasts among the unregistered, descriptive analyses.
- Not changed: Table 2 and its caption (B0041, B0082) keep the registered D − B_wide row only; the five-arm table is supplementary so that the registered table stays as registered.

### REV-R3-7 — The abstract and §5 led with the positive clause of a regime whose significance was not argued (DA-M4) — **addressed**

- The Abstract's results now open with the matched-training results (0.223 points at 40 dB; 0.229 at 20 dB after the registered retraining; below both floors) and then report the evaluation-only growth, the 9.2-fold ratio and the unapportioned attribution.
- §5 (B0064) opens: "a decoder branch dedicated to the cardiac component is worth 0.22 to 0.23 Dice points to a network trained at the level at which it is evaluated, at 40 dB and at 20 dB alike, and it clears the registered floor at neither level." The evaluation-only regime is the second clause, with its scope ("for a network trained at 40 dB and evaluated under heavier noise").
- The significance of the fixed-level-training regime is not argued separately; it is stated with its scope, and §4.1 gives the practical reading (train at the operating level).

### REV-R3-8 — The 40 dB p = 0.0983 corresponds to the normal approximation without continuity correction, contrary to the Methods (R1-W3) — **addressed; the code was right and the text was wrong**

- `tools/evaluate.py` calls `scipy.stats.wilcoxon` with defaults. §2.4 (B0028) now states: "computed with the asymptotic normal approximation without continuity correction, the default of the SciPy implementation above n = 50 and the procedure the scoring code applied." Table 3 and every reported p-value are unchanged because they were already the values of that procedure.

### REV-R3-9 — Multiplicity; unregistered contrasts not listed; the floor's own sampling error at H5; the relative-error statistic is a mean of ratios (R1-W5–W8) — **addressed, four statements added**

- §2.4 (B0028): "No multiplicity adjustment is applied: the four registered rules are separate pre-specified decisions, each with its own floor, H3 rests on one interval, and the per-level tests and intervals of the sweep are descriptive and reported with their unadjusted values."
- §2.6 (B0034) lists the unregistered contrasts with p-values or intervals: B, C and C_wide against B_wide and each other at 40 dB and across the sweep (§3.1, S9), the 50 dB anchor for the H3 statistic, the seed-removal sensitivity at 20 dB, and the geometry-level intervals of the addendum.
- §3.5 (B0122): "The floor is itself an estimate from 58 seeds, with a standard error of about 0.036 points, and the upper limit of the difference's interval lies within one such error of it, so this is the marginal case that a registered rule returns as falsified rather than adjudicates." (SE of an SD from n = 58: 0.384 / √(2 × 57) ≈ 0.036.)
- §3.2 (B0042): the statistic is defined as "averaging the ratios over seeds", and the divergence is stated: "this mean of ratios differs from the ratio of the mean gain to the mean error, by several-fold at the high-SNR levels where both are close to zero, and the intervals refer to the mean of ratios." Checked from the per-seed files while writing this letter: 4.5-, 3.7- and 1.9-fold at 60, 50 and 40 dB; within 20% from 35 dB down.

### REV-R3-10 — Four citation sentences: Graf 2017 is body posture; the quarter-amplitude set is GREIT's convention; Murphy 2019; the bolus method cited second-hand (R2-W2–W5) — **three corrected, one not accepted, one primary source added**

- Graf and Riedel 2017 (B0009): "depends strongly on body position" replaces "position in the thorax" (the paper's own title and anchored quote say "position dependent").
- Quarter-amplitude set (B0009 and the Fig. 2 caption, B0079): attributed to GREIT's figure-of-merit convention (Adler et al. 2009), "that lies within the 20 to 35% range clinical region-of-interest methods use (Pulletz et al., 2006)"; the ROI paper is no longer cited as the source of the threshold.
- Bolus method (B0009): Frerichs et al. 2002 (IEEE TMI; regional lung perfusion by EIT compared with electron-beam CT) is added as the primary source through `tools/cite.py` (R12d; PubMed record checked), and Borges 2012 is kept as the piglet comparison. Reference list 53 → 54 (B0074, B0075).
- Murphy et al. 2019 (B0027): **R2-W4 not accepted.** The PubMed abstract states that the network was trained on EIT data for cardiac-output estimation, so the citation stays as an EIT example; the sentence is reworded to "with poorly contacting electrodes, unspecified in advance, for cardiac-output estimation from thoracic EIT data", which is what the abstract supports. Recorded in `35_CITATION_AUDIT_v4.md`.

### REV-R3-11 — Venue-format departures (EIC-W1, W3, W4, W5, W8) — **partially addressed; the reference-rendering gaps remain**

- Companion-studies sentence (B0013): replaced by "The companion conditions named in Section 4.4 are not tested here", which is true of the reference list.
- Abstract sentence three: rewritten in B0005 and `31_` ("The second of two preregistered simulation studies (EIDORS, GREIT) registered heart-channel Dice as primary endpoint, five arms of 58 seeds, a primary signal-to-noise ratio of 40 dB and an evaluation-only sweep from 60 to 20 dB.").
- Figure order: Fig. 1 and Fig. 2 are swapped at format-convert so that figures are numbered by first citation in `36_`; the working draft keeps its figure labels.
- Table 2 caption: the inline LaTeX is replaced in the deliverable by `tools/format_convert_scirep.py` (the caption in `36_` reads as plain text); the working-draft caption (B0082) is unchanged.
- **Not yet fixed**: the four rendering gaps in the reference list are still present in `36_` (Lakens 2013 without its article number 863; Ronneberger 2015 without its LNCS volume number; the stray "⋆" in the Herzberg 2023 title; the "Help?" title ending of Xin 2022). They are registry-rendering corrections to be made in `refs/overrides.json` and re-rendered before packing; they do not touch the draft.

### REV-R3-12 — "Dice points" undefined; the locus of the hypothesised interference not stated for a shared-encoder design (R3-W1, W2) — **addressed**

- Abstract: "0.223 Dice points (hundredths of Dice)". §2.4 (B0028): "Differences between arms are reported in Dice points, hundredths of the Dice coefficient."
- §1 (B0011): "In the arms compared here every network shares the encoder and the bottleneck, so any interference acts on the shared features and on the gradients that reach them, and a decoder branch can relieve it only by giving each target its own path after the bottleneck."

---

## Consider

### REV-R3-13 — Checkpoints on request rather than deposited; MPS determinism; compute footprint (EIC-W6, R1-W9, R1-W10) — **determinism and footprint stated; deposit is a pending PI decision**

- §2.4 (B0027): "Each run seeds the data order and the initialisation and requests deterministic algorithms, but the MPS backend does not guarantee bit-identical results on re-execution, so a seed defines a replicate rather than an exactly reproducible run. Parameter counts are matched, while compute and activation footprint, which differ between a widened and a split decoder, were not measured." (`tools/train_arms.py` seeds torch and numpy and requests deterministic algorithms with `warn_only=True`.)
- Deposit of the rule-bearing checkpoints or per-seed predictions (Zenodo) is the PI's decision and is not yet made; Data Availability (B0072) is unchanged. FLOPs were not measured and the text says so rather than estimating them.

### REV-R3-14 — Venue-suggested order, the 4,500-word recommendation, and the Discussion's sentence-length subheadings (EIC-W7, EIC-W2) — **subheadings shortened; order and length are author decisions**

- §4.1, §4.2 and §4.3 headings (B0050, B0054, B0057) are now short noun phrases ("What the addendum does and does not attribute"; "When a registered rule and an interval estimate disagree"; "Relation to the original architecture"). The §4.4 heading was already short.
- IMRaD order is kept. Main text (Sci Rep count, excluding Methods) is 7,271 words against the 4,500-word recommendation; the venue checklist does not make the limit mandatory, and the PI has decided not to cut.

### REV-R3-15 — Why interference is the frame for complementary targets; the shift-tolerance result for the robustness reader (R3-W3, R3-W5) — **one sentence added; the reframing is inside REV-1**

- §1 (B0011): "The two targets are complementary parts of one input, which a multi-task reader would call maximally related tasks. Whether even related targets compete for shared features when one of them is small is the empirical question, and the registered design asks it rather than assuming either answer."
- The shift-tolerance reading stays visible in the Abstract, §4.1 and §5 through the registered "in whole or in part" wording (REV-R3-1); no separate robustness framing was added, as the letter's arbitration asked.

---

## Things the panel should know about this revision

1. **One new block and 27 replaced blocks**; 99 of 126 blocks are byte-identical to v3. The patch was emitted from the roadmap and the author sidecar and applied with the authorization witness; three §4 headings tripped the structural flag and were acknowledged (REV-R3-14).
2. **Abstract**: the working draft's B0005 and the submission abstract in `31_` carry the same sentences; `31_` is 199 words.
3. **Deliverable** `36_` was regenerated from v4 by the same converter as `32_`, with two converter fixes (Table 2 caption, figure order). The four reference-rendering gaps listed under REV-R3-11 are still visible there.
4. **Pending author-side items, not in this revision**: repository tag and the URL/tag fields in `AUTHOR_FIELDS.json`; the AI-use statement's "accessed September 2026" to be updated to October; the Zenodo deposit decision (REV-R3-13); confirmation of the Vandenhende 2020 author order against the BMVC PDF.
5. **Unregistered claim drift**: the claim-surface manifest is empty (no registered surfaces), so the headline wording changes of REV-R3-1 are on the review surface, not machine-witnessed; their authority is the addendum's pre-fixed reading in `PREREGISTRATION_HEART.md` §9.
