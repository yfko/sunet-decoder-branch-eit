contract_role: methodology

## Dimension Scores

### D1: methodology_rigor
score: warn
trigger: "statistical reporting is incomplete or under-justified, for example missing multiplicity handling across sweep levels, an unjustified normal approximation, a power claim without a stated calculation, an unlabelled exploratory analysis, or missing reproducibility detail, without changing what the stated procedure would conclude"

### D2: domain_accuracy
score: not_assessed

### D3: argumentative_coherence
score: warn
trigger: "a claim is overstated or under-qualified relative to the evidence, for example a generalisation beyond the tested conditions or a null result read as equivalence without a sensitivity bound, while the central thesis survives once reworded"

### D4: cross_disciplinary_relevance
score: not_assessed

### D5: writing_and_structure
score: not_assessed

### D6: venue_fit_and_contribution
score: not_assessed

## Review Body

This is a preregistered, paired, seed-replicated simulation study whose registered machinery (hashed preregistrations, effect-size floors, seed-level bootstrap, a registered addendum that retrains at the heavier noise level) is well above the usual bar for architecture comparisons in medical imaging. The two prior panel rounds have evidently been absorbed: the replication unit is explicit, seed-level and geometry-level intervals sit side by side, W is reported with p, the floor has a stated rationale, and the addendum closes the distribution-shift objection as far as the data allow. The internal arithmetic is tight: every paired difference, floor, H3 statistic, the 9.2-fold ratio and the 0.6% parameter margin recompute from the tabled values. What remains is at the reporting and interpretation layer rather than the design layer, with two exceptions that I grade Major. First, the sample-size justification covers only the p-condition of the registered rule, and under the effect size the study was sized for the two-condition rule had essentially no chance of returning "confirmed"; the paper should say so, because it changes what "the registered rules found no benefit" means. Second, the addendum is read as separating weak-component protection from distribution-shift tolerance, but under the paper's own operational definition of "threat" the two readings make the same prediction in the retrained condition, so the headline attribution of "most of that benefit" to mismatch tolerance is one of two readings the design leaves open. Neither finding touches the registered verdicts themselves (H1, H2, H5 falsified; H3 confirmed), which stand as reported. One arithmetic receipt mismatches: the 40 dB p-value corresponds to the normal approximation without the continuity correction the Methods say was applied; the discrepancy is in the fourth decimal and changes nothing, but the Methods sentence and the computed value should agree.

### S1: Preregistered decision rules with an effect-size floor, hashed before training, with the outcome grid's missing cells reported as they fell
**Evidence Anchor**: text: §2.6 "No rule was invented afterwards to reconcile them. Both outcomes are reported as they fell."

The rules were fixed before any arm contrast existed, the combination that occurred (H1 falsified, H3 confirmed; rule falsified while the interval excludes zero) was not pre-specified, and the paper reports it without inventing a reconciling rule. This is the correct handling and it is rare.

### S2: Seeds as the replication unit, every contrast paired within seed, with seed-level and geometry-level intervals distinguished and both reported
**Evidence Anchor**: text: §2.4 "the seed-level bootstrap intervals reported throughout describe training-run variability, not variability over test geometries"

The source of variation that each interval describes is named, the registered rules are defined on seeds, and the geometry-level intervals (Table 3, S8) let a reader see that the small contrasts are dominated by training randomness.

### S3: The registered addendum retrains both primary arms at the heavier level with its reading fixed before the run
**Evidence Anchor**: text: §2.7 "Both readings were fixed in advance."

The addendum was hashed, both interpretive readings of H5 were written before the 116 runs, and the paper narrows its headline exactly as the pre-specified reading requires. This is the single most valuable design element in the paper.

### S4: The scoring defect is disclosed with a byte-for-byte reproducible defective path
**Evidence Anchor**: text: §2.5 "The defective path is retained behind a flag and reproduces the pre-fix summary files byte for byte"

The defect, its mechanism (affine shift before a quarter-amplitude threshold), its measured consequence (mask covering 0.948 of the field) and the pre-fix conclusions are all disclosed, and the fix is shown to be isolated. This is a model of how to report a scoring error.

### S5: The explicit practical-significance rationale for the floor, and the disagreement between rule and interval reported rather than resolved post hoc
**Evidence Anchor**: text: §4.2 "Reporting both, and not revising the rule after seeing the interval, is the point of having registered the rule."

### S6: Internal numerical consistency across tables
**Evidence Anchor**: table: Table 3, rows "B_wide heart DSC (mean ± SD)", "D heart DSC (mean ± SD)" and "D − B_wide, pts [95% CI, seeds]"

Every paired difference in Tables 1 to 3 recomputes from the arm means to within rounding (0.9679 − 0.9657 = 0.22 pts; 0.8985 − 0.8775 = 2.10 pts; 0.9597 − 0.9574 = 0.23 pts), every floor equals the tabled control SD, the H3 statistic equals 2.097 − 0.160, the 9.2-fold ratio equals 2.097/0.229, and the parameter ratio 10,811,298/10,743,738 equals 1.0063. I found no internal contradiction among reported numbers.

### S7: Code, preregistrations, deviation log and per-seed result files are public under a tagged release
**Evidence Anchor**: text: §2.8 "are available at https://github.com/yfko/sunet-decoder-branch-eit (tag v1.0-submission)"

### W1: The sample-size justification covers only the p-condition; the registered two-condition rule had essentially no power at the effect size the study was sized for
**Severity**: Major
**Evidence Anchor**: text: §2.4 "Scaling Study 1's heart effect by that variance gave dz ≈ 0.376, and 80% power at that effect size requires 58 seeds."
**Confidence**: 4 — paired-design power arithmetic is my core competence; the only input I had to infer is SD of the paired difference, which follows from the reported dz and mean difference.

The 80% figure is correct for a two-sided paired test at dz = 0.376 with n = 58 (I obtain 0.804 from the noncentral t). But the H1 rule has two conditions, and the floor condition is a comparison of the mean paired difference against the control arm's single-run seed-to-seed SD. From the reported +0.223 points and dz = 0.27, the SD of the paired difference at 40 dB is about 0.83 points and the SE of its mean over 58 seeds is about 0.11 points. The effect the study was powered for is therefore a mean difference of about 0.31 points, against a floor of 0.670 points: at that effect size the probability of passing the floor is about 0.05%. For the full rule to return "confirmed" with 80% probability the true effect would have to be roughly dz 0.9, more than twice the anticipated effect. The floor is a legitimate practical-significance criterion, and the paper says so, but the sentence "80% power" describes a test the rule does not run. The consequence for the reader is material: "the registered rules found no benefit" (Abstract, §1, §3.1) means "no benefit of at least about 0.8 of the paired-difference SD", and the paper nowhere states the minimal effect the rule could have confirmed. The authors could consider (i) stating the power of the complete rule at the design effect, or equivalently the smallest true effect at which the rule passes with 80% probability, for H1, H2 and H5; (ii) rewording the sample-size paragraph so that "80% power" is tied explicitly to the p-condition; and (iii) adding one clause to each "no benefit" statement naming the floor in effect-size units. No re-analysis is needed; the registered verdicts are unchanged.

### W2: The addendum does not separate weak-component protection from distribution-shift tolerance, yet the paper attributes most of the benefit to the latter
**Severity**: Major
**Evidence Anchor**: text: §4.1 "The design that can distinguish them found that most of the effect is the latter."
**Confidence**: 4 — the point is logical, not domain-specific, and the paper's own operational definition of threat is the premise.

Section 4.1 operationalises "under threat" by the control arm's loss of heart Dice (8.8 points at 20|40). In the retrained condition the control arm recovers 8.0 of those 8.8 points, so by that definition the cardiac component is no longer under threat at 20|20, and the mechanism "the branch helps when the component is under threat" predicts exactly the small advantage observed. Distribution-shift tolerance predicts the same thing. The training condition changes the threat and the familiarity together, so the addendum shows that the evaluation-only advantage does not survive matched training; it does not show which of the two readings explains it. The paper half-acknowledges this ("the threat, so defined, is largely a threat to a network that has not seen the noise before") and then resolves it in one direction in the same section, in the Abstract ("most of that benefit is mismatch tolerance") and in the Conclusion. The registered reading of a falsified H5 was "attributable in whole or in part to distribution-shift tolerance", which is the defensible statement; the quantified attribution ("most", "the larger part") is not entailed. The central thesis survives rewording: the supportable claim is that the branch's advantage tracks the control arm's loss on the cardiac component, that matched training removes most of that loss and most of the advantage with it, and that whether the residual mechanism is protection or tolerance would need a condition in which the component stays under threat while training matches evaluation (for example a lower SNR, a smaller heart or a weaker contrast at matched training). The authors could consider restating §4.1's second paragraph, the Abstract's final sentence and the Conclusion in that form, and deleting or qualifying the sentence anchored above.

### W3: The reported 40 dB p-value corresponds to the normal approximation without the continuity correction the Methods state
**Severity**: Minor
**Evidence Anchor**: table: Table 3, column "40 dB trained, 40 dB evaluated", rows "Wilcoxon W" (642) and "p" (0.0983)
**Confidence**: 4 — the signed-rank normal approximation at n = 58 is fully specified by the paper and the arithmetic is in AR1.
**Arithmetic Receipt**: AR1

With n = 58, the null mean of W is 855.5 and its SD is 129.16. With the continuity correction, z = (642 − 855.5 + 0.5)/129.16 = −1.649 and the two-sided p is 0.0991; without it, z = −1.653 and p is 0.0983, which is the reported value. The same check on W = 427 and W = 433 is consistent either way at the reported precision (AR3, AR4), so the inconsistency is only visible at 40 dB. A tie correction to the variance cannot reconcile the two, because it would move p in the wrong direction. Nothing changes (both values exceed 0.05 and the floor decides H1), but the Methods sentence "computed with the normal approximation and continuity correction" and the number in the table should agree, and the statement that n = 58 "exceeds the limit of the exact method" describes a software default rather than a mathematical limit; the exact signed-rank distribution at n = 58 is cheap to compute and would remove the question. The authors could consider either reporting the corrected values or amending the Methods sentence, and stating the software and version that produced the p-values.

### W4: The effect-size input to the power calculation is not reproducible from the stated numbers, and the Study 1 power figure matches a different calculation from the one described
**Severity**: Minor
**Evidence Anchor**: text: §2.1 "D minus B_wide 0.46 points, p = 0.32, dz = 0.34, roughly 29% power at n = 10"
**Confidence**: 3 — I can show the stated inputs do not yield the stated outputs, but I cannot see the preregistration's own derivation.

Two reported figures do not follow from their stated inputs. (i) The paper says the pilot SD was 33% larger than Study 1's and that scaling Study 1's heart effect by that variance gave dz ≈ 0.376. Study 1's own dz was 0.34; a larger SD at the same effect lowers dz (0.34/1.33 ≈ 0.26, or 0.34/1.15 ≈ 0.30 if the 33% refers to variance), so the derivation that raises it to 0.376 is not the one described. (ii) At dz = 0.34 and n = 10, the two-sided power of a paired test is about 16%, not 29%; 29% is what a one-sided test at dz = 0.376 gives. These are reporting issues: n = 58 was fixed before data and is not in question. The authors could consider writing out the derivation in Supplementary S2 or S7 so that both figures recompute, and stating the sidedness used in each power statement.

### W5: No statement of multiplicity handling across the seven sweep levels or the four registered rules
**Severity**: Minor
**Evidence Anchor**: absence: §2.4 and §3.2 — expected a statement of whether and how the seven per-level Wilcoxon tests, the seven relative-error-reduction intervals and the four registered decision rules are adjusted for multiplicity; checked §2.4, §2.6, §3.2, Table 2 and its note
**Confidence**: 4 — standard reporting expectation; the dependence structure is given in the paper itself.

The registered H3 is a single statistic, so the confirmatory layer has no multiplicity problem. The descriptive onset, however, is read off as the highest-SNR level at which p first falls below 0.05 and the interval first excludes zero, a minimum-p selection over seven correlated levels, and the Abstract reports "onset 35–30 dB" without that qualifier. The seven tests are strongly dependent (ρ ≥ 0.99 between adjacent high-SNR levels), so a Bonferroni bound of 0.05/7 = 0.0071 is conservative; the 35 dB p of 0.0011 survives it, but the 95% relative-error-reduction interval at 35 dB (+2.77 to +11.25) has not been checked at a corrected level. The authors could consider one sentence stating that no adjustment was applied, that the onset is selected from seven levels, and that it survives a Bonferroni-corrected p; and reporting the 35 dB ceiling-free interval at the corrected level, which would make the onset claim in the Abstract defensible as stated.

### W6: Unregistered contrasts and sensitivity analyses are reported with p-values but are not listed among the non-pre-specified analyses
**Severity**: Minor
**Evidence Anchor**: text: §3.1 "Against the unwidened arm B, D gained +0.191 points (CI +0.027 to +0.361, p = 0.041)"
**Confidence**: 4 — the registration status is stated in §2.4 and the contrast is not among its rules.

Section 2.6 says three analyses were not registered and names them. The paper also reports the D − B contrast with p = 0.041 (the only p below 0.05 at 40 dB, and the one that a reader could take as evidence for the branch), the B, C and C_wide contrasts against B_wide, the alternative 50 dB anchor for H3, the removal of the three largest seeds at 20 dB, and the 47-of-58 per-seed slope; none of these is in the §2.6 list, and the D − B result is repeated in the Table 1 note without a label. The authors could consider extending §2.6 to enumerate every unregistered quantity that carries a p-value or interval, and marking D − B as descriptive where it appears.

### W7: The H5 floor verdict is marginal and the floor's own sampling uncertainty is not reported
**Severity**: Minor
**Evidence Anchor**: table: Table 3, column "20 dB trained, 20 dB evaluated", rows "D − B_wide, pts [95% CI, seeds]" (+0.229 [+0.081, +0.373]) and "Floor (B_wide seed SD), pts" (0.384)
**Confidence**: 4 — the SE of a sample SD at n = 58 is standard.

At 40|40 the floor (0.670) lies well outside the interval (upper bound 0.441), so the H1 floor failure is robust. At 20|20 the interval's upper bound is 0.373 against a floor of 0.384, and the floor is itself a sample SD over 58 seeds with a relative SE of about 9% (±0.036 points). The registered rule compares two point estimates and was followed correctly; the paper should say that this particular comparison is within one floor-SE of flipping, so that "clears neither floor" in the Abstract and Conclusion is read with the right weight. The 9.2-fold shrinkage, which is the result that matters, does not depend on this.

### W8: The relative-error-reduction statistic is a mean of per-seed ratios and diverges from the ratio of means by up to 4.5-fold at high SNR
**Severity**: Minor
**Evidence Anchor**: table: Table 2, column "Relative error reduction, % [95% CI]", heart rows at 60, 50 and 40 dB (+1.11, +1.40, +3.47)
**Confidence**: 3 — the direction of the divergence follows from the covariance of numerator and denominator; I cannot quantify the interval effect without the per-seed files.

From the tabled arm means, (D − B_wide)/(1 − B_wide) is 5.0%, 5.2% and 6.4% at 60, 50 and 40 dB, against the reported per-seed means of 1.1%, 1.4% and 3.5%; the two agree within a point from 30 dB down. The divergence is expected, because the denominator is the control arm's own error on the same seed and a poor B_wide seed inflates both numerator and denominator, but it means the ceiling-free measure at high SNR is driven by seed-level covariance rather than by the aggregate gain, and the lung values of −8.7% to −5.1% (ratio of means: about −1.7%) show the same amplification. The descriptive statements that the high-SNR intervals contain zero and that "the initial step is at least as sharp as in raw points" depend on this estimator choice. The authors could consider stating the estimator in the table note, reporting the ratio of means beside the mean of ratios, or bootstrapping the ratio of seed means instead.

### W9: Parameter count is matched but compute and activation footprint are not reported
**Severity**: Minor
**Evidence Anchor**: text: §2.2 "The comparison holds capacity constant, not shape."
**Confidence**: 3 — architectural, inferred from the described widening and splitting; I have not seen the per-arm diagrams in S1.

The paper is explicit that matched parameters is not matched architecture. A second decoder of the original width and a single decoder widened by 1.5312 differ in forward FLOPs, activation memory and effective training compute per epoch, and D has 0.6% more parameters in addition. None of these is reported. The authors could consider adding FLOPs per forward pass, peak activation memory and mean wall-clock per run to Table 1 or S7, so that a reader can see which capacity measures were matched and which were not.

### W10: Determinism of seeded training runs is not stated, and model checkpoints are available only on request
**Severity**: Minor
**Evidence Anchor**: text: §Data Availability "are available from the corresponding author on request, because their size exceeds what the repository host accepts"
**Confidence**: 3 — reproducibility practice; the MPS backend's determinism behaviour is version-dependent.

Seeds are the unit of replication, so a reader needs to know whether a seed reproduces a run bit for bit on the stated hardware (Apple M4, MPS backend) or only in distribution; neither is stated. Seventeen gigabytes of checkpoints exceed GitHub's limits but not Zenodo's or OSF's; at minimum the 232 checkpoints of the three rule-bearing contrasts, or the per-seed test predictions from which every Dice value derives, could be archived with a DOI. The authors could consider adding a determinism statement to S7 and a DOI-backed archive for checkpoints or predictions.

### W11: The Abstract and Conclusion report the onset without the descriptive label the Results attach to it
**Severity**: Minor
**Evidence Anchor**: text: Abstract "onset 35–30 dB, lung channel flat"
**Confidence**: 4 — direct comparison of the paper's own sections.

Section 3.2 and Limitation 6 are clear that the onset shape was not a registered test. The Abstract lists it between two registered results without qualification, and the Conclusion states "beginning between 35 and 30 dB" as a finding. The authors could consider one word ("descriptively") in each place.

## Arithmetic Receipts

### AR1
procedure_id: p_from_test_statistic
evidence_anchor: table: Table 3, column "40 dB trained, 40 dB evaluated", rows "Wilcoxon W" and "p"
reported_inputs: Wilcoxon signed-rank test over 58 paired seeds, W = 642 (smaller signed-rank sum), p = 0.0983, two-sided, normal approximation with continuity correction, no zero differences (§2.4)
assumptions: two-sided test as stated; normal approximation with continuity correction as stated; no tie correction to the null variance because the paper reports no tied absolute differences; test family z as the paper's stated approximation implies
derivation: n = 58; null mean n(n+1)/4 = 855.5; null variance n(n+1)(2n+1)/24 = 16682.25; SD = 129.160; with continuity correction z = (642 − 855.5 + 0.5)/129.160 = −1.6491, two-sided p = 2 × Φ(−1.6491) = 0.0991; without the correction z = (642 − 855.5)/129.160 = −1.6530, two-sided p = 0.0983
derived_value_or_range: two-tailed p = 0.0991 with the stated continuity correction (one-tailed 0.0496); without the correction two-tailed p = 0.0983
comparison_rule: reported p at four decimals must equal the derived two-tailed value under the stated procedure, rounded to four decimals
status: mismatch
tail_convention: two-tailed
test_family: z
statistic_value: -1.6491
df: none
reported_p_comparator: equals
reported_p_value: 0.0983
finding_ref: W3

### AR2
procedure_id: p_from_test_statistic
evidence_anchor: table: Table 3, column "40 dB trained, 20 dB evaluated", rows "Wilcoxon W" and "p"
reported_inputs: Wilcoxon signed-rank test over 58 paired seeds, W = 97, p < 0.0001, two-sided, normal approximation with continuity correction (§2.4)
assumptions: two-sided test as stated; normal approximation with continuity correction as stated; no tie correction to the null variance
derivation: n = 58; null mean 855.5; SD 129.160; z = (97 − 855.5 + 0.5)/129.160 = −5.8687; two-sided p = 2 × Φ(−5.8687) = 4.4 × 10⁻⁹; without the correction z = −5.8726, p = 4.3 × 10⁻⁹
derived_value_or_range: two-tailed p = 4.4 × 10⁻⁹ (one-tailed 2.2 × 10⁻⁹)
comparison_rule: derived two-tailed p must satisfy the reported inequality p < 0.0001
status: consistent
tail_convention: two-tailed
test_family: z
statistic_value: -5.8687
df: none
reported_p_comparator: less_than
reported_p_value: 0.0001

### AR3
procedure_id: p_from_test_statistic
evidence_anchor: table: Table 3, column "20 dB trained, 20 dB evaluated", rows "Wilcoxon W" and "p"
reported_inputs: Wilcoxon signed-rank test over 58 paired seeds, W = 427, p = 0.0009, two-sided, normal approximation with continuity correction (§2.4, §3.5)
assumptions: two-sided test as stated; normal approximation with continuity correction as stated; no tie correction to the null variance
derivation: n = 58; null mean 855.5; SD 129.160; z = (427 − 855.5 + 0.5)/129.160 = −3.3137; two-sided p = 2 × Φ(−3.3137) = 0.00092; without the correction z = −3.3176, p = 0.00091
derived_value_or_range: two-tailed p = 0.00092 (one-tailed 0.00046); 0.0009 at four decimals under either variant
comparison_rule: reported p at four decimals must equal the derived two-tailed value rounded to four decimals
status: consistent
tail_convention: two-tailed
test_family: z
statistic_value: -3.3137
df: none
reported_p_comparator: equals
reported_p_value: 0.0009

### AR4
procedure_id: p_from_test_statistic
evidence_anchor: text: §3.2 "At 35 dB the Wilcoxon p first falls below 0.05 (W = 433, p = 0.0011)"
reported_inputs: Wilcoxon signed-rank test over 58 paired seeds at the 35 dB evaluation-only level, W = 433, p = 0.0011, two-sided, normal approximation with continuity correction (§2.4); Table 2 reports 0.0011 at the same level
assumptions: two-sided test as stated; normal approximation with continuity correction as stated; no tie correction to the null variance
derivation: n = 58; null mean 855.5; SD 129.160; z = (433 − 855.5 + 0.5)/129.160 = −3.2673; two-sided p = 2 × Φ(−3.2673) = 0.00109; without the correction z = −3.2711, p = 0.00107
derived_value_or_range: two-tailed p = 0.00109 (one-tailed 0.00054); 0.0011 at four decimals under either variant
comparison_rule: reported p at four decimals must equal the derived two-tailed value rounded to four decimals
status: consistent
tail_convention: two-tailed
test_family: z
statistic_value: -3.2673
df: none
reported_p_comparator: equals
reported_p_value: 0.0011

### AR5
procedure_id: p_from_test_statistic
evidence_anchor: text: §2.1 "D minus B_wide 0.46 points, p = 0.32, dz = 0.34, roughly 29% power at n = 10"
reported_inputs: Study 1 heart-channel contrast D minus B_wide, 0.46 points, p = 0.32, dz = 0.34, n = 10 seeds
assumptions: none beyond what the paper states; the paper does not say whether this p is from the Wilcoxon signed-rank rule of Study 1 or from a paired t-test implied by dz
derivation: if paired t, t = dz × √n = 0.34 × 3.162 = 1.075 on df = 9, two-sided p ≈ 0.31; if exact Wilcoxon at n = 10 the statistic W is not reported and p cannot be derived; the two families are not distinguishable from the text and the t-based value is only approximately equal to the reported 0.32
derived_value_or_range: paired-t two-tailed p ≈ 0.31; Wilcoxon not derivable without W
comparison_rule: not applied; the test family that produced the reported p is not identifiable
status: not_computable
not_computable_reason: test_family_ambiguous
tail_convention: unstated
test_family: unavailable
statistic_value: unavailable
df: unavailable
reported_p_comparator: equals
reported_p_value: 0.32

### AR6
procedure_id: grim
evidence_anchor: table: Table 1, column "Heart DSC (mean ± SD)", all five arm rows
reported_inputs: seed means of heart Dice over 58 seeds, each a mean over 360 test frames of a continuous quarter-amplitude-set Dice coefficient, reported to four decimals with SD
assumptions: none; Dice on a 64 × 64 grid is a ratio of pixel counts and the per-seed value is a mean of 360 such ratios, so the data are not on a known discrete scale with a single analytic N
derivation: GRIM and GRIMMER require an unweighted mean of integer-scale items with known granularity; the reported means are averages of continuous ratios over 360 frames and then over 58 seeds, and no integer scale or single item N applies
derived_value_or_range: none; no feasible-set reachability check is defined for this quantity
comparison_rule: none; the procedure's preconditions are not met
status: not_applicable

### AR7
procedure_id: n_from_df
evidence_anchor: absence: Tables 1 to 3 and §2.4 — expected a reported degrees of freedom for any t, F or chi-square statistic; checked Table 1, Table 2, Table 3, §2.4, §3.1, §3.2, §3.5
reported_inputs: no degrees of freedom are reported anywhere; every rule-bearing test is a Wilcoxon signed-rank test over n = 58 paired seeds, which has no df, and every interval is a percentile bootstrap
assumptions: none
derivation: n_from_df inverts a reported df under a named identity; with no df reported there is nothing to invert, and the paired n = 58 is stated directly and matches the 58 seeds per arm in every table
derived_value_or_range: none
comparison_rule: none; no df to compare
status: not_applicable
