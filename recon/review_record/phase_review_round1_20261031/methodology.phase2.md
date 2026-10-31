contract_role: methodology

## Dimension Scores

### D1: methodology_rigor
score: warn
trigger: "a registered rule is applied correctly but the registered wording is paraphrased rather than quoted"

### D2: domain_accuracy
score: not_assessed

### D3: argumentative_coherence
score: warn
trigger: "Verdict wording differs in strength between Abstract, Results and Discussion without contradicting the registered outcome"

### D4: cross_disciplinary_relevance
score: not_assessed

### D5: writing_and_structure
score: not_assessed

### D6: venue_fit_and_contribution
score: not_assessed

## Review Body

Summary. The design can answer the questions it poses. Thirty paired seeds per arm and row, a registered smallest effect of interest (the control arm's seed SD), a two-sided Wilcoxon signed-rank test beside a percentile bootstrap interval and dz, a transfer rule on a difference of differences, and an equivalence rule with a margin fixed before the runs are each appropriate to the question they judge, and the manuscript keeps the registered, first-addendum, second-addendum and exploratory standings apart in nearly every numbered sentence. I re-derived every cell-level quantity that the tables allow: all 23 paired differences and six floors in Tables 1 and 3 follow from the printed means and SDs, the six registered and six E1 differences of differences in Table 2 follow from the printed per-cell differences and the diagonal differences, the six MDE80 values equal 0.53 times the printed SD, the bootstrap half-widths match the printed SDs at n = 30, the six M2′ and twelve L3′ differences follow from Tables 1 and 3, dz agrees with Δ and the interval width in every cell I checked (for example R1-GN: half-width 0.145 points implies a paired SD near 0.41, giving dz 0.79 as printed), and all twelve Wilcoxon p values reproduce under the normal approximation with continuity correction that Table 1 names (receipts AR1 to AR12). The expectation hit rates (3/3 and 1/3; 3/3 and 1/3; 3/3 and 0/3) and the counts "eight of nine", "four of the five", "fifteen times" and "twenty verdict cells" all check against the tables. Numbers are not the weakness of this manuscript.

The weaknesses are of verification and of wording. The study's central methodological claim is that every verdict follows a rule and an interpretation sentence fixed before the data were read, but the manuscript never shows those sentences; it reports them in indirect speech, and the only surface where a reader could check them is a deposit that is still a material gap. Two post-read decisions about registered analyses (withholding the registered interpretation of M1, and listing but not reading the registered secondary path) are disclosed where they occur but are absent from the deviation record the manuscript says it keeps. Several reporting elements the Methods promise for every cell are not in the tables. On coherence, one heading and one Abstract sentence say the branch "adds nothing measurable" where Table 3 shows a measured deficit with an interval excluding zero, and the Discussion's "twenty of twenty falsified" is stated without the manuscript's own admission that eight of those cells did not pose the intended question. None of these flips a verdict; all are repairable by rewriting and by one or two supplementary tables.

Strengths.

### S1: Paired-seed design with a registered smallest effect of interest and complete per-cell inferential reporting
Every contrast is paired within seed over thirty seeds, the floor is fixed as the control arm's seed SD, and each tested cell carries n, Δ, a 100,000-resample percentile bootstrap interval with a stated seed, dz, W and p. The floor rule deliberately does not power a below-floor effect and the manuscript says so.
**Evidence Anchor**: text: block B0039 "Seeds are the unit of replication and every contrast is paired within seed."

### S2: Equivalence tested against a pre-fixed margin rather than inferred from non-significance
The second addendum fixes ±1.0 point before training, states the margin's reasons, uses a 95% interval (TOST at α = 0.025) and reports how far outside the margin each interval lies, then adds a labelled post-hoc sensitivity statement rather than moving the margin.
**Evidence Anchor**: text: block B0069 "Non-significance cannot establish equivalence; a margin can"

### S3: Hash-chained preregistration with an explicit read-state column
Table 4 gives, for each of the four states, what it governs, what had been read when it was written, and what was fixed before the runs; the hash is written into every run's metadata. This is the right structure for a study whose addenda are confirmatory for their own runs and exploratory in origin, and the double standing is named as such.
**Evidence Anchor**: table: Table 4, column "Written after reading"

### S4: Expectations, hit rates and achieved sensitivity reported as they fell
The addenda's pre-stated expected ranges are reported beside the outcomes with the verdict and magnitude hit rates separated, and the R3 cells carry MDE80 from the observed seed SD because the registered power table assumed diagonal-cell variability.
**Evidence Anchor**: text: block B0078 "the hit rates are reported as they fell"

### S5: Internal numerical consistency between text and tables
Every paired difference, floor, difference of differences, M2′, L1 and L3′ value I could recompute from the printed means and SDs agrees with the printed value to rounding, and every number quoted in the text matches its table cell.
**Evidence Anchor**: table: Table 1, Δ and Floor columns against the mean ± SD columns

### S6: Multiplicity and reporting rationale stated and defensible
The decision not to correct across twenty verdicts is argued from the direction of the verdicts (every verdict is "not confirmed", so multiplicity inflates false confirmations), the one negative interval is described and not tested, and in-pool and out-of-pool performance are reported separately.
**Evidence Anchor**: text: block B0040 "multiplicity inflates false confirmations, not false falsifications"

Weaknesses.

### W1: The registered rules and fixed interpretation sentences are never quoted, so "applied as written" cannot be verified from the manuscript
The manuscript's methodological contribution rests on verdicts following rules and interpretation sentences fixed before the data were read (Abstract, Section 1.4, Section 5). Section 2.6 states the rules in the authors' words, and every Results subsection reports the fixed reading in indirect speech ("the registered reading applies", "the fixed reading is that"), so a reader cannot tell quotation from paraphrase or check that the sentence used matches the hashed one. The deposit that would allow the check (S1 Appendix, Zenodo) is a material gap at this stage. Why it matters: a preregistered study whose rules are visible only by paraphrase is, for the reader, a described preregistration rather than a verifiable one, and the interpretation sentences are where wording drift would be hardest to notice. Remedy: add a supplementary table with one row per hypothesis (R1, R3, M1, M1′, L1, L2) quoting verbatim the registered decision rule and both outcome interpretation sentences, with the hash state that governs each; in Results, mark the interpretation sentences as quotations.
**Severity**: Major
**Evidence Anchor**: absence: Sections 2.5, 2.6 and 3.1 to 3.6 — expected the verbatim registered decision rule and both fixed interpretation sentences for each of R1, R3, M1, M1′, L1 and L2; checked Methods 2.5 and 2.6, every Results subsection, Table 4 and the S1 Appendix caption
**Confidence**: 4 — preregistration reporting practice; the gap is visible on the manuscript's surface

### W2: Two post-read decisions about registered analyses are disclosed in place but not catalogued as deviations
Section 3.3 reports M1 falsified in all three cells and then withholds the registered interpretation from the GN and BP cells because the input was unreadable; no registered interpretation is applied to the GREIT cell either, so the fixed reading of a falsified M1 appears nowhere. Section 3.2 lists the registered secondary scoring path and does not read it because it moves the background off zero. Both decisions were taken after the cells were read, both are reasonable manipulation-check arguments, and both are disclosed where they occur, but Section 2.5 and Table 4 record only the two pre-read deviations, and the manuscript adopts a deviation-reporting structure under which a decision not to interpret or not to read a registered analysis is a deviation with a timing and a rationale. Why it matters: the manuscript's own standard is that deviations are reported as they fell; a reader of the deviation record would conclude there were two. Remedy: add both to the deviation record (and S2 Table) with timing "after reading the cell", rationale, and consequence; quote the registered M1 interpretation and state in one sentence why it is not applied.
**Severity**: Major
**Evidence Anchor**: text: block B0053 "the registered interpretation of a falsified M1 is not applied to them"
**Confidence**: 4 — preregistration deviation reporting; the timing is stated in the manuscript itself

### W3: "Adds nothing measurable" contradicts the GN held-out cell
The heading of Section 3.6 and the Abstract say the branch "added nothing measurable" on an unseen reconstructor, and the Conclusion that "its difference reversed sign". Table 3 shows, for GN, Δ = −3.9 points, 95% CI −5.3 to −2.4, p 1.2e−04, D above B_wide on 4 of 30 seeds: a measured deficit, which Section 3.6 itself describes as the information in the cell. The L2 verdict (falsified) is unaffected, but "nothing measurable" states an absence where the table shows a presence, and the manuscript's own vocabulary for the branch's null elsewhere is "below the registered floor", not "no effect". Remedy: reword to "no measurable benefit" in the heading and Abstract, and keep the GN deficit as described, not tested.
**Severity**: Major
**Evidence Anchor**: text: block B0062 "On an unseen reconstructor the branch adds nothing measurable"
**Confidence**: 5 — direct comparison of heading and Abstract against Table 3

### W4: Reporting elements the Methods promise for every cell are not in the tables
Section 2.6 says every cell is reported with the paired-difference SD; Tables 1 and 3 have no such column (Table 2 has the SD of the difference of differences), so dz is the only route to it. Section 2.6 says achieved sensitivity is reported for the R3 and E1 cells; Table 2 carries MDE80 for the R path only. Section 2.3 says the lung channel is reported in every cell; only Table 3 has a lung column, and the "at most 0.03 points" and "0.985 to 0.988" lung statements in Sections 3.1 and 3.5 have no table surface. Section 2.6 also speaks of "exact p values" while Table 1 states a continuity correction, which belongs to the normal approximation (and reproduces all twelve p values, AR1 to AR12). Remedy: add the paired-difference SD and lung Dice columns (or move them to S1 Table and say so), add MDE80 for the E1 cells, and replace "exact" with the approximation actually used.
**Severity**: Minor
**Evidence Anchor**: absence: Tables 1, 2 and 3 and their footnotes — expected the paired-difference SD per cell, MDE80 for the six E1 cells and the lung-channel Dice for every cell promised in Sections 2.3 and 2.6; checked Table 1, Table 2, Table 3, their footnotes and the S1 Table caption
**Confidence**: 4 — statistical reporting completeness

### W5: "Twenty of twenty falsified" is stated without the manuscript's own count of uninformative cells
Section 4.5 opens with twenty verdict cells, twenty falsified. By the manuscript's own account four R3 cells presented an input the network could not read, two M1 cells did the same, and two L2 cells had a floor of 9.49 points that "could hardly have been met there whatever the branch did". Eight of the twenty verdicts are therefore in cells that, the authors say, did not pose the intended question, and the methodological contribution ("a preregistered study whose hypotheses were mostly falsified") reads stronger in Section 4.5 and the Abstract than the body supports. Remedy: state in Section 4.5 that twelve cells were informative and eight were falsified in cells the design did not succeed in posing, and carry that count into Section 1.4's contribution list.
**Severity**: Minor
**Evidence Anchor**: text: block B0077 "Of twenty verdict cells, twenty were falsified."
**Confidence**: 4 — the eight cells are each identified as such in Sections 3.2, 3.3 and 3.6

### W6: "Never worse" and "could not be separated at 0.4 points" are looser than the M2′ numbers
M2′ has one negative point estimate (D on BP, −0.083 points, CI −0.32 to +0.13) and four intervals spanning zero, so "never worse than retraining on any reconstructor" is true of the intervals' lower bounds at about 0.3 points, not of every point estimate. The Conclusion's "two remedies that could not be separated at 0.4 points" sits beside two intervals that exclude zero (B_wide on GREIT and GN) and one upper bound of +0.50. Since M2′ is reported and not tested, the sentence should describe rather than conclude. Remedy: "pooled training was never worse than retraining by more than 0.3 points in any cell, and in two of six cells was better by a small amount" or similar; drop "could not be separated at 0.4 points" or state the bound as the widest interval.
**Severity**: Minor
**Evidence Anchor**: text: block B0056 "Pooled training was never worse than retraining on any reconstructor"
**Confidence**: 4 — descriptive-statistics wording against Table 1's M2′ footnote

### W7: The GREIT row comes from a different training campaign, which confounds the GREIT M2′ and R3 comparisons
The GREIT single-source networks were trained in the companion study and re-scored here; the mixed-ps, mixed and loro rows were trained in this study. The one M2′ interval that most clearly favours pooling (B_wide on GREIT, +0.36, CI +0.23 to +0.50) and the two GREIT-trained R3 cells therefore compare networks from two training campaigns, and any environment or library drift between campaigns is confounded with the row effect. The Abstract names the optimisation-steps confound for M2′ but not this one. Remedy: state the training dates, library versions and code tag of the companion campaign, or retrain the GREIT row in this campaign for the comparison; at minimum add the confound to Section 3.4's qualifications.
**Severity**: Minor
**Evidence Anchor**: text: block B0028 "The GREIT row reuses seeds 0 to 29 of the companion study's 20 dB training"
**Confidence**: 3 — deep-learning reproducibility; the effect is small relative to the stated confounds

### W8: Run-to-run determinism on the stated hardware is not addressed
Thirty seeds were trained on one Apple-silicon machine with PyTorch 2.8.0. Seeds fix initialisation and data order but not kernel determinism on that backend, so another researcher re-running seed k would not obtain the printed per-seed Dice, only a draw from the same distribution. The manuscript treats seeds as the unit of replication and reports per-seed values in S1 Table, so it should say whether deterministic algorithms were enforced and, if not, how far a repeated seed moves (one re-run of one seed would suffice). Remedy: one sentence in Section 2.2 or 2.7.
**Severity**: Minor
**Evidence Anchor**: absence: Sections 2.2 and 2.7 — expected a statement of whether deterministic kernels were enforced or how far a single seed reproduces run to run on the stated hardware; checked Sections 2.2, 2.6, 2.7 and the S2 Table caption
**Confidence**: 3 — deep-learning reproducibility practice

### W9: The upper-bound status of the held-out loss rests on an unstated non-negativity assumption
The manuscript reports every held-out loss as an upper bound on the input-side generalisation loss because the reference moves with the reconstructor. That holds if the reference-style component of the loss is non-negative, which is plausible but not shown, and Section 2.3 says its size was not measured. Since the qualification is attached to every held-out number, its assumption should be stated once. Remedy: in Section 2.3, "an upper bound, on the assumption that a change of reference style can only lower Dice relative to the held-out reconstructor's own cardiac image".
**Severity**: Minor
**Evidence Anchor**: text: block B0031 "is reported as an upper bound on the input-side generalisation loss, because the reference moves with the reconstructor"
**Confidence**: 3 — reasoning about the endpoint; the direction is likely but unproven

### W10: Which no-retraining path M3′ is computed against is not stated
M3′ is defined in Section 3.4 as the share of the no-retraining loss that pooling removed. The printed values are consistent with mixed-ps→Y minus the registered-path X→Y Dice (they reproduce the printed Δ(X→Y) R to 0.1 point), not with the E1 path, but neither the Table 2 caption nor Section 3.4 says so, and Table 2 places M3′ beside the E1 columns. Remedy: state the path in the caption and the text.
**Severity**: Minor
**Evidence Anchor**: table: Table 2, M3′ B_wide / D (A1) column and its caption
**Confidence**: 4 — derived from the printed values

### W11: Identical B_wide seed SD for the GREIT and BP held-out cells should be confirmed
Table 3 prints 0.0949 as B_wide's SD on both the GREIT and BP held-out cells, with means 0.3431 and 0.5995 and per-seed ranges 0.187 to 0.504 and 0.323 to 0.709; the text then uses the same floor, 9.49, for both. Two cells with different means and ranges having the same SD to four decimals is possible but uncommon enough to check against the per-seed file. Remedy: confirm, or correct one value and the floor that depends on it.
**Severity**: Minor
**Evidence Anchor**: table: Table 3, B_wide Dice (mean ± SD) column, GREIT and BP rows
**Confidence**: 2 — a pattern check, not an error found

### W12: The three signs of "the reconstructor behaves as a domain" carry three different evidence standings
Section 4.1 says all three signs appeared. The first (loss without retraining) rests on the exploratory E1 re-scoring and on falsified R3 cells four of which were uninformative; the second (no loss when pooled) rests on M2′, a reported and untested quantity; only the third (failure outside the pool) rests on a tested rule. Section 4.1 labels each, but the Abstract's and heading's "behaves as a domain" is unqualified. Remedy: in the Abstract and Section 4.1 heading or first sentence, say that the three signs are of exploratory, descriptive and tested standing respectively.
**Severity**: Minor
**Evidence Anchor**: text: block B0066 "All three signs named in Section 1.1 appeared."
**Confidence**: 3 — standing of evidence; the labels are present in the body

Questions for the authors. What SD and test underlie the statement that n = 30 gives at least 0.89 power for a floor-sized effect, and is the computation in S2 Table? Were the Wilcoxon p values computed by the normal approximation with continuity correction throughout (as Table 1 says and AR1 to AR12 reproduce), or exactly for some cells? Does the R-path Dice for the six no-retraining cells appear in S1 Table, since M3′ depends on it and the text quotes only the E1 Dice? Were any seeds excluded or re-run in any row?

Scope of this review. I did not assess literature coverage, the EIDORS reconstructor settings or noise-figure matching (domain seat), cross-field framing (perspective seat), or venue fit (editor). Statistical reporting against the manuscript's own criterion (every cell with n, Δ, CI, control SD, paired SD, dz, W, p): PARTLY_MEETS, for the reasons in W4; the reported elements are internally consistent.

## Arithmetic Receipts

### AR1
procedure_id: p_from_test_statistic
evidence_anchor: table: Table 1, row R1-GN (GN → GN), columns W and p
reported_inputs: W = 48; n = 30 paired seeds; p = 1.5e−04; two-sided with continuity correction (Table 1 caption)
assumptions: the continuity correction named in the Table 1 caption implies the large-sample normal approximation to the signed-rank distribution; no zero differences or ties among the 30 paired Dice differences (not stated by the paper; ties would shrink the variance slightly and move p further from, not toward, the printed value only if W were the larger rank sum)
derivation: mean = n(n+1)/4 = 232.5; SD = sqrt(n(n+1)(2n+1)/24) = sqrt(2363.75) = 48.6185; z = (48 + 0.5 − 232.5)/48.6185 = −3.785; two-tailed p = 2·Φ(−3.785)
derived_value_or_range: two-tailed p = 1.54e−04
comparison_rule: derived p rounded to the two significant figures printed must equal the printed value
status: consistent
tail_convention: two-tailed
test_family: z
statistic_value: −3.785
df: none
reported_p_comparator: equals
reported_p_value: 0.00015

### AR2
procedure_id: p_from_test_statistic
evidence_anchor: table: Table 1, row R1-BP (BP → BP), columns W and p
reported_inputs: W = 29; n = 30; p = 3.0e−05; two-sided with continuity correction
assumptions: normal approximation with continuity correction as in AR1; no ties or zero differences (not stated)
derivation: z = (29 + 0.5 − 232.5)/48.6185 = −4.175; two-tailed p = 2·Φ(−4.175)
derived_value_or_range: two-tailed p = 2.98e−05
comparison_rule: derived p rounded to two significant figures must equal the printed value
status: consistent
tail_convention: two-tailed
test_family: z
statistic_value: −4.175
df: none
reported_p_comparator: equals
reported_p_value: 0.00003

### AR3
procedure_id: p_from_test_statistic
evidence_anchor: table: Table 1, row GREIT → GREIT (ref), columns W and p
reported_inputs: W = 104; n = 30; p = 0.0085; two-sided with continuity correction
assumptions: as AR1
derivation: z = (104 + 0.5 − 232.5)/48.6185 = −2.633; two-tailed p = 2·Φ(−2.633)
derived_value_or_range: two-tailed p = 0.00848
comparison_rule: derived p rounded to two significant figures must equal the printed value
status: consistent
tail_convention: two-tailed
test_family: z
statistic_value: −2.633
df: none
reported_p_comparator: equals
reported_p_value: 0.0085

### AR4
procedure_id: p_from_test_statistic
evidence_anchor: table: Table 1, row M1 (mixed → GREIT), columns W and p
reported_inputs: W = 211; n = 30; p = 0.67; two-sided with continuity correction
assumptions: as AR1
derivation: z = (211 + 0.5 − 232.5)/48.6185 = −0.432; two-tailed p = 2·Φ(−0.432)
derived_value_or_range: two-tailed p = 0.666
comparison_rule: derived p rounded to two decimals must equal the printed value
status: consistent
tail_convention: two-tailed
test_family: z
statistic_value: −0.432
df: none
reported_p_comparator: equals
reported_p_value: 0.67

### AR5
procedure_id: p_from_test_statistic
evidence_anchor: table: Table 1, row M1 (mixed → GN), columns W and p
reported_inputs: W = 221; n = 30; p = 0.82; two-sided with continuity correction
assumptions: as AR1
derivation: z = (221 + 0.5 − 232.5)/48.6185 = −0.226; two-tailed p = 2·Φ(−0.226)
derived_value_or_range: two-tailed p = 0.821
comparison_rule: derived p rounded to two decimals must equal the printed value
status: consistent
tail_convention: two-tailed
test_family: z
statistic_value: −0.226
df: none
reported_p_comparator: equals
reported_p_value: 0.82

### AR6
procedure_id: p_from_test_statistic
evidence_anchor: table: Table 1, row M1 (mixed → BP), columns W and p
reported_inputs: W = 230; n = 30; p = 0.97; two-sided with continuity correction
assumptions: as AR1
derivation: z = (230 + 0.5 − 232.5)/48.6185 = −0.041; two-tailed p = 2·Φ(−0.041)
derived_value_or_range: two-tailed p = 0.967
comparison_rule: derived p rounded to two decimals must equal the printed value
status: consistent
tail_convention: two-tailed
test_family: z
statistic_value: −0.041
df: none
reported_p_comparator: equals
reported_p_value: 0.97

### AR7
procedure_id: p_from_test_statistic
evidence_anchor: table: Table 1, row M1′ (mixed-ps → GREIT), columns W and p
reported_inputs: W = 209; n = 30; p = 0.64; two-sided with continuity correction
assumptions: as AR1
derivation: z = (209 + 0.5 − 232.5)/48.6185 = −0.473; two-tailed p = 2·Φ(−0.473)
derived_value_or_range: two-tailed p = 0.636
comparison_rule: derived p rounded to two decimals must equal the printed value
status: consistent
tail_convention: two-tailed
test_family: z
statistic_value: −0.473
df: none
reported_p_comparator: equals
reported_p_value: 0.64

### AR8
procedure_id: p_from_test_statistic
evidence_anchor: table: Table 1, row M1′ (mixed-ps → GN), columns W and p
reported_inputs: W = 70; n = 30; p = 8.6e−04; two-sided with continuity correction
assumptions: as AR1
derivation: z = (70 + 0.5 − 232.5)/48.6185 = −3.332; two-tailed p = 2·Φ(−3.332)
derived_value_or_range: two-tailed p = 8.62e−04
comparison_rule: derived p rounded to two significant figures must equal the printed value
status: consistent
tail_convention: two-tailed
test_family: z
statistic_value: −3.332
df: none
reported_p_comparator: equals
reported_p_value: 0.00086

### AR9
procedure_id: p_from_test_statistic
evidence_anchor: table: Table 1, row M1′ (mixed-ps → BP), columns W and p
reported_inputs: W = 95; n = 30; p = 0.0048; two-sided with continuity correction
assumptions: as AR1
derivation: z = (95 + 0.5 − 232.5)/48.6185 = −2.818; two-tailed p = 2·Φ(−2.818)
derived_value_or_range: two-tailed p = 0.00483
comparison_rule: derived p rounded to two significant figures must equal the printed value
status: consistent
tail_convention: two-tailed
test_family: z
statistic_value: −2.818
df: none
reported_p_comparator: equals
reported_p_value: 0.0048

### AR10
procedure_id: p_from_test_statistic
evidence_anchor: table: Table 3, row GREIT (held-out), columns W and p
reported_inputs: W = 153; n = 30; p = 0.10; two-sided with continuity correction (Table 1 convention; Table 3 caption does not restate it)
assumptions: as AR1, plus that Table 3 uses the Table 1 p convention (the paper gives one statistical procedure in Section 2.6)
derivation: z = (153 + 0.5 − 232.5)/48.6185 = −1.625; two-tailed p = 2·Φ(−1.625)
derived_value_or_range: two-tailed p = 0.104
comparison_rule: derived p rounded to two decimals must equal the printed value
status: consistent
tail_convention: two-tailed
test_family: z
statistic_value: −1.625
df: none
reported_p_comparator: equals
reported_p_value: 0.10

### AR11
procedure_id: p_from_test_statistic
evidence_anchor: table: Table 3, row GN (held-out), columns W and p
reported_inputs: W = 45; n = 30; p = 1.2e−04; two-sided with continuity correction
assumptions: as AR10
derivation: z = (45 + 0.5 − 232.5)/48.6185 = −3.846; two-tailed p = 2·Φ(−3.846)
derived_value_or_range: two-tailed p = 1.20e−04
comparison_rule: derived p rounded to two significant figures must equal the printed value
status: consistent
tail_convention: two-tailed
test_family: z
statistic_value: −3.846
df: none
reported_p_comparator: equals
reported_p_value: 0.00012

### AR12
procedure_id: p_from_test_statistic
evidence_anchor: table: Table 3, row BP (held-out), columns W and p
reported_inputs: W = 197; n = 30; p = 0.47; two-sided with continuity correction
assumptions: as AR10
derivation: z = (197 + 0.5 − 232.5)/48.6185 = −0.720; two-tailed p = 2·Φ(−0.720)
derived_value_or_range: two-tailed p = 0.472
comparison_rule: derived p rounded to two decimals must equal the printed value
status: consistent
tail_convention: two-tailed
test_family: z
statistic_value: −0.720
df: none
reported_p_comparator: equals
reported_p_value: 0.47
