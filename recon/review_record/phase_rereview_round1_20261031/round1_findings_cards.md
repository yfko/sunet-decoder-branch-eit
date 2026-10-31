# Round-1 review findings: the five seats' Phase 2 cards (paper-visible findings), concatenated verbatim 2026-10-31 (sunet-recon-tier3 manuscript panel round 1; synthesis = 12_REVIEWER_PANEL_round1.md)

<!-- card source: eic.phase2.md sha256 ce3c2b4d2e2174940787ceed3072f84221f220dde7b804331de7c7feaabf1ff9 -->
contract_role: eic

## Dimension Scores

### D1: methodology_rigor
score: not_assessed

### D2: domain_accuracy
score: not_assessed

### D3: argumentative_coherence
score: not_assessed

### D4: cross_disciplinary_relevance
score: not_assessed

### D5: writing_and_structure
score: pass

### D6: venue_fit_and_contribution
score: block
trigger: "present a post-unblinding addendum result with the same confirmatory standing as a preregistered result"
block_class: repairable

## Review Body

Read as the handling academic editor for a journal whose criteria are technical soundness, conclusions supported by the data without overstatement, reproducible description, clear English, ethics and reporting standards, and which does not judge novelty or significance. The manuscript is a preregistered simulation study whose twenty verdict cells were all falsified, reported with two post-unblinding, pre-hashed addenda. On venue fit the question is not whether a negative result is interesting but whether it is sound, scoped and honestly labelled; this manuscript is within scope and is, in most of its surfaces, exemplary in keeping the registered, first-addendum, second-addendum and exploratory standings apart and in carrying its upper-bound qualification wherever a held-out number appears. It also reads as an independent unit: the companion manuscript is named, not cited, and no sentence rests on its findings.

The block on D6 is textual and repairable, not a soundness failure. It binds to two places where the manuscript's own standing discipline, which it imposes on itself in Section 1.4 and Table 4 and keeps in the abstract and Results, lapses: the GREIT matched cell, labelled a reference that is not tested, is given a verdict and counted among "every reconstructor" under the registered floor (W1); and the Conclusion presents registered, first-addendum and second-addendum results in one undifferentiated run of sentences (W2). Because the abstract and the Conclusion are the two surfaces a reader quotes, and because the venue criterion is supported-without-overstatement, these are the editor's business rather than a copy-editor's. Neither requires any new run or re-analysis; both are resolved by labelling. Two further wording items (W3, W4) move descriptive quantities toward verdicts or describe a measured negative as "nothing measurable", and three pre-submission completeness items (W5, W6) concern placeholders and the venue's required statements.

D5 passes: the IMRaD organisation is clean, each Results subsection states its standing in its first sentence, captions and table legends are self-contained (standing codes, hash prefixes and footnotes on the BP raster offset travel with the tables), every number I recomputed or cross-read between abstract, text and Tables 1 to 3 agreed (floors, differences, intervals, hit rates, the 20-of-20 count, the 161 and 188 amplitude ratios, the 15-fold floor remark), the main text is about 7,000 words with no venue limit to exceed, the abstract is at the venue's 300-word ceiling and the title within its character limit. Reference formatting was not re-audited per the dispatch.

### S1: The provenance of every rule is auditable from one table
Table 4 gives the four hashed states of the preregistration, what each governs, what had been read when it was written and what it fixed before the runs; the hash prefixes recur in the table legends. For an editor assessing whether "preregistered" is a decoration or a mechanism, this one table answers the question without recourse to the deposit.
**Evidence Anchor**: table: Table 4

### S2: The held-out loss is never reported without its upper-bound qualification
The qualification is defined once in Methods and repeated at every surface that carries a held-out number, abstract and Conclusion included, so a reader cannot quote a loss without the reason it is an upper bound.
**Evidence Anchor**: text: B0031 "is reported as an upper bound on the input-side generalisation loss, because the reference moves with the reconstructor"

### S3: Deviations and expectation hit rates are reported as they fell
Two protocol deviations are dated, placed before any cell was read, and footnoted beside every affected cell; the addenda's expectation hit rates on verdicts and magnitudes are given separately, including the 0 of 3 on L2 magnitudes, and Section 4.5 states the obvious objection to the addenda before answering it.
**Evidence Anchor**: text: B0078 "the hit rates are reported as they fell"

### S4: Independence from the unaccepted companion manuscript is stated and kept
The related submission is named and declared, not cited; the only dependency (re-use of GREIT-trained networks, re-scored here with this paper's code) is stated in Methods and in the related-manuscript statement, and I found no sentence that rests on the companion's findings.
**Evidence Anchor**: text: B0089 "The present manuscript relies on none of its reported findings"

### S5: Per-cell statistical reporting is complete and the tables can be read without the text
Every verdict cell carries n, both arms' mean and SD, the paired difference, its percentile-bootstrap interval, the floor, dz, W, exact p and the seed count favouring D; the registered secondary path and the descriptive quantities are listed with their standing rather than dropped.
**Evidence Anchor**: table: Table 1

### S6: Absence claims are bounded by a dated, enumerated search
The three "no study has" statements are tied to named databases, a date and string counts, and each names the nearest work that falls short, which is the form in which such a claim can be checked.
**Evidence Anchor**: text: B0017 "To our knowledge within that search, no EIT deep-learning study has trained on one conventional reconstructor's images and evaluated on another's"

### S7: The authors' interest in the architecture under test is disclosed
The corresponding author's authorship of the architecture is stated as a limitation on neutrality, with the preregistration and the direction of the results offered as the answer; this belongs in a venue whose readers are asked to trust a negative result against the authors' own method.
**Evidence Anchor**: text: B0081 "so this is not a neutral comparison in the sense of Boulesteix et al. (2013)"

### W1: The GREIT matched cell is a reference that is not tested, yet it carries a verdict and is counted under the registered floor
Section 1.4 states that the registered R1 covered Gauss–Newton and back-projection only; Table 1 codes the GREIT matched cell as "ref" and its legend defines ref as "reference, not tested", yet the same row's Verdict column reads "falsified", the Section 3.1 heading says "on all three reconstructors", the abstract says "below the registered floor on every reconstructor", and the Conclusion lists GREIT first among the reconstructors on which the branch "stayed below the registered floor". The data support the pattern; the standing does not support the verdict. The manuscript must choose: either the GREIT cell is a reference, in which case its Verdict entry becomes a dash and the abstract, 3.1 heading and Conclusion say that the two registered cells were falsified and the GREIT reference, re-scored here, showed the same pattern; or it carries a verdict, in which case its standing (whose rule, fixed when, read when) must be stated in Section 2.5 and Table 4. Either repair is textual.
**Severity**: Major
**Evidence Anchor**: text: B0006 "Under matched training the branch stayed below the registered floor on every reconstructor"
**Confidence**: 4 — editorial reading of standing labels against the manuscript's own Table 1 legend and Section 1.4; no domain judgement involved

### W2: The Conclusion drops the standing labels the rest of the manuscript carries
Section 1.4 and the first sentence of Section 3 commit the manuscript to keeping registered, addendum and exploratory standings apart, and the abstract does so. The Conclusion does not: the matched-training sentence (registered plus a reference), the pooled-training clause (first addendum), the unseen-reconstructor clause (second addendum), the 62/16/36-point sentence (second addendum) and the 0.4-point remark (first addendum, descriptive) run on without a label, and the closing sentence that every verdict followed a pre-hashed rule, while true, levels the standings rather than distinguishing them. A reader who quotes the Conclusion will attribute registered standing to the addenda, which is the objection Section 4.5 itself anticipates. The repair is a label per clause ("registered", "first addendum", "second addendum", "exploratory"), as the abstract already does.
**Severity**: Major
**Evidence Anchor**: text: B0085 "leaving one reconstructor out cost 62, 16 and 36 points on GREIT, Gauss–Newton and back-projection"
**Confidence**: 4 — direct comparison of the Conclusion's sentences with the standing rules stated in Sections 1.4 and 3

### W3: A descriptive quantity is carried to an equivalence-flavoured verdict with a number that is in no table
M2′ is declared "reported, not tested" and the manuscript's own rule is that pooled training is "never worse", never equivalent. The Discussion (Section 4.1) and the Conclusion both say the two remedies "could not be separated at 0.4 points". That is an equivalence statement about an untested quantity, and 0.4 is neither the largest point estimate (+0.360) nor an interval bound (the six intervals lie within [−0.32, +0.50]). Replace with the licensed form, for example that pooled training with a per-source affine was never worse than retraining, with the six differences between −0.08 and +0.36 points.
**Severity**: Minor
**Evidence Anchor**: text: B0085 "two remedies that could not be separated at 0.4 points"
**Confidence**: 4 — the manuscript's own standing rules and Table 1's M2′ block supply the check

### W4: "Nothing measurable" and "does not appear" misdescribe what was measured
The abstract and the Section 3.6 heading say the branch "added nothing measurable" on an unseen reconstructor, while Table 3 and Section 3.6 report a measured negative difference on Gauss–Newton (−3.9 points, interval −5.3 to −2.4, p 0.00012, D above B_wide on 4 of 30 seeds). The licensed wording is that the branch rule was falsified by sign reversal and the negative differences are described, not tested; "nothing measurable" is both inaccurate and a "no effect" form the manuscript elsewhere avoids. Likewise the Conclusion's opening sentence says the branch's benefit "does not appear" under a change of reconstructor, whereas under matched training the manuscript itself insists the differences are "below the floor, not zero". Align both with the registered vocabulary: below the registered floor; no evidence; sign reversed.
**Severity**: Minor
**Evidence Anchor**: text: B0006 "and the branch added nothing measurable there"
**Confidence**: 4 — text-against-table reading within the manuscript

### W5: Three material placeholders remain in the submission text
The Zenodo DOI for the minimal dataset and the four preregistration states, the repository release tag, and the companion preprint DOI are placeholders. For this venue the data-availability criterion is assessed at submission, and the preregistration's evidential weight in this manuscript rests on the deposit being resolvable; the related-manuscript statement also depends on the preprint being available to the editor and reviewers. These must be filled, or the related-manuscript statement reworded to say a copy accompanies the submission in lieu of a preprint, before submission.
**Severity**: Minor
**Evidence Anchor**: text: B0042 "Zenodo DOI, to be minted at submission"
**Confidence**: 5 — visible placeholders

### W6: The venue's required statements are not present as separate items
The venue requires a Data Availability Statement (which it publishes verbatim), a Funding statement, a Competing Interests statement and an Ethics statement (here: simulation, no human or animal data, not applicable). The bundle carries data and code availability inside Section 2.7, an AI-use disclosure in the Acknowledgments and the authors' interest in the architecture as a limitation, but none of the four as a separate statement, and nothing on funding. Add them in the venue's form; the Competing Interests statement should also carry the corresponding author's authorship of the architecture, which Section 4.6 already discloses.
**Severity**: Minor
**Evidence Anchor**: absence: front matter and Section 2.7 (B0042) — expected separate Data Availability, Funding, Competing Interests and Ethics statements; checked title page, Section 2.7, Acknowledgments, Related manuscript, Supporting information
**Confidence**: 4 — venue requirements as the editor applies them; the submission system may collect some of these outside the manuscript file

Questions for the authors, for the synthesizer to carry forward: (1) Is the GREIT matched cell to be read as a reference or as a verdict cell, and if the latter, under which hashed state? (2) Is the "0.4 points" in Sections 4.1 and 5 a rounding of the largest M2′ point estimate or of an interval bound, and will it be replaced by the licensed "never worse" form? (3) Can the GREIT training row be regenerated from this paper's deposit alone, or does its reproduction require the companion study's checkpoints?

---

<!-- card source: methodology.phase2.md sha256 02366bf5b54c1d45bcfb8cb7fe9f739b9a9080d0694a8f10313a6c40886d7f7b -->
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

---

<!-- card source: domain.phase2.md sha256 249e7cedefe6bdc8d70794fef7feb573388412f1db8dd3f3647f2f9937a91746 -->
contract_role: domain

## Dimension Scores

### D1: methodology_rigor
score: not_assessed

### D2: domain_accuracy
score: warn
trigger: "the Methods omit a detail a domain reader needs to interpret a reported quantity"

### D3: argumentative_coherence
score: not_assessed

### D4: cross_disciplinary_relevance
score: not_assessed

### D5: writing_and_structure
score: not_assessed

### D6: venue_fit_and_contribution
score: not_assessed

## Review Body

Reviewer lens: EIDORS-based thoracic EIT reconstruction (GREIT, one-step Gauss–Newton, Sheffield back-projection; noise figures, amplitude scales, per-source normalisation, single-organ targets, quarter-amplitude masks), with post-reconstruction deep-learning experience. I checked the Methods for self-containment and defensibility of the reconstructor settings, the EIT and reconstruction vocabulary, the attribution of prior work in the EIT and adjacent multi-source literature, the agreement of every quoted number with Tables 1 to 4, the labelling of evidence standing in sentences that carry numbers, and the scope of the conclusions.

Overall, the domain content is accurate and unusually disciplined. The reconstruction vocabulary (noise figure, hyperparameter, Laplace prior, one-step GN, Sheffield matrix, difference frame, GREIT grid) is used in its accepted sense; the choice to match GN's noise figure to GREIT's realised value is the established way to make two linear reconstructors comparable; the decision to score against each reconstructor's own single-organ image, and to report held-out losses as upper bounds because that reference moves with the reconstructor, is the correct reading of the task and is carried into every held-out sentence I checked. Every number I recomputed from Tables 1 to 3 agrees with the text in direction and, with one rounding exception, in magnitude; the twenty verdicts are reported as falsified with the registered rules applied as written; the scope clauses (three conventional reconstructors, one setting each, one cylinder, 20 dB, simulation) are repeated where needed, and no reconstructor ranking appears. The warn on D2 rests on one thing a domain reader needs and cannot find in the manuscript: the forward model and the reconstructor settings are specified only partly, so I cannot judge from the text alone that the three operators received the same data or that their settings are defensible, which is the specific question my seat is asked. A second finding concerns a factual tension between the preregistration timeline in Table 4 and the reuse of companion-study networks for the GREIT row. The remaining findings are minor.

### S1: Noise-figure matching of GN to GREIT's realised value
A domain-correct way to make two regularised linear reconstructors comparable, and the manuscript goes further than usual by reporting that the nominal 0.5 was realised as 0.602 on a common reference frame and matching to the realised value, with the resulting pilot-band mismatch recorded as a deviation rather than hidden.
- **Evidence Anchor**: text: block B0024 "its hyperparameter set by bisection so that its noise figure matched GREIT's realised value"

### S2: Reference choice and the upper-bound qualification
Scoring the separated cardiac component against the reconstructor's own heart-only reconstruction is the only coherent definition of the target for a post-reconstruction separation network, and the manuscript draws the consequence correctly: a held-out loss mixes an input shift with a reference-style shift and is reported as an upper bound in the Abstract, Sections 2.3, 3.5, 4.1, 4.2, 4.4, 4.6 and the Conclusion.
- **Evidence Anchor**: text: block B0031 "is reported as an upper bound on the input-side generalisation loss, because the reference moves with the reconstructor"

### S3: The amplitude-scale finding is real EIT pipeline knowledge
That GREIT, GN and BP outputs differ by two orders of magnitude in image units, that a single pooled affine therefore shows a network near-constant GN and BP inputs, and that the remedy is a per-source affine, is correct, is diagnosed by plotting the network's actual input rather than inferred, and is the kind of operational fact EIT deep-learning papers rarely report.
- **Evidence Anchor**: figure: Fig 1 (block B0099) and Fig 3 (block B0101), amplitude ratios 161 and 188 and input scale 1/132 and 1/156

### S4: Terminology discipline
The manuscript fixes its vocabulary before using it: segmentation versus separation, weak versus dominant component, and an operational definition of "domain" for the reconstructor with three observable signs, followed by an explicit statement that domain generalisation is not claimed.
- **Evidence Anchor**: text: block B0013 "names the task of producing a Dice-scored mask"

### S5: Scope bound on reconstructor settings
The manuscript states, with the right citation, that reconstruction settings strongly change what an operator produces, and binds every result to the three operators at the settings used; the Limitations add electrode and boundary-shape errors as untested structured-artefact sources.
- **Evidence Anchor**: text: block B0024 "every result holds for these three operators at these settings"

### S6: Bounded absence statements
The three "no prior study" statements are bounded by named databases, a search date and string counts, and each names the nearest work found, which is the correct way to make such a claim checkable.
- **Evidence Anchor**: text: block B0017 "To our knowledge within that search, no EIT deep-learning study has trained on one conventional reconstructor's images and evaluated on another's"

### W1: The forward model and the reconstructor settings are not self-contained
Section 2.1 gives the conductivities, the geometry count, the SNR and the split, and for each reconstructor one or two settings, but omits what a domain reader needs to judge that the three operators saw the same data and were configured defensibly: the stimulation and measurement pattern (the Sheffield back-projection matrix presupposes 16-electrode adjacent drive and measurement, so the pattern is implied for all three but never stated); the electrode model and contact impedance; whether the forward mesh is 2D, 2.5D or 3D, its density, and whether a different (coarser) mesh was used for the inverse solve; the cylinder radius and the ranges of inclusion radii and centres behind "randomised"; what "heterogeneous conductivity" means; GREIT's training-target settings (target radius, distribution, desired-image width), on which the reconstruction matrix depends as much as on the noise figure; how one-step GN was "solved on GREIT's grid" (a pixel-grid coarse-to-fine parametrisation, or a FEM solve rasterised afterwards); the interpolation used to upsample BP's 32 × 32 raster, which affects the quarter-amplitude mask and the 2-px offset; and whether the 20 dB SNR is an amplitude or power ratio and whether noise was added to the inhomogeneous frame or to the difference frame. None of these changes the verdicts, and the code is deposited, but the manuscript's own standard is that a reader can tell what was simulated and compared without external files, and here they cannot. Suggested fix: one paragraph in 2.1 (or S2 Table) listing pattern, electrode model, mesh, geometry ranges, GREIT training parameters, GN parametrisation, BP interpolation and the SNR definition in linear terms. Norm grounding: the TREND consensus statement cited as the manuscript's first reference (Frerichs et al., 2017) recommends reporting the stimulation pattern and the reconstruction algorithm with its settings, and the GREIT paper (Adler et al., 2009) shows the reconstruction matrix depends on the stimulation pattern and training targets.
- **Severity**: Major
- **Evidence Anchor**: absence: Section 2.1, blocks B0023 to B0024 — expected stimulation and measurement pattern, electrode model and contact impedance, mesh dimensionality and density, cylinder and inclusion size ranges, GREIT training-target settings, GN pixel-grid parametrisation, BP upsampling interpolation and the linear SNR definition; checked Sections 2.1 to 2.4, Table 4, the S1 to S2 Table and S1 Appendix captions, and the Fig 1 to Fig 3 captions
- **Confidence**: 4 — EIDORS user; the absent items are the ones needed to rebuild the three reconstruction matrices

### W2: The preregistration timeline and the reuse of companion-study networks are in tension
Table 4 states that the registered state was written when no arm had been trained and no contrast computed, and Section 2.5 repeats that the registered state fixed its rules "before any arm was trained". Section 2.2 states that the GREIT row reuses seeds 0 to 29 of the companion study's 20 dB training, and Section 1.2 that those networks are re-scored here. If the companion networks were trained before 2026-09-26, then one training row existed, and its diagonal performance was at least partly known, when R3's two GREIT-trained cells and their Δ(X→X) term were registered; the statement "no arm trained" would then be inaccurate for the GREIT row and would need a declared deviation, and the fourth stated contribution (a preregistered study reported with its deviations) depends on such statements being exact. If the companion training postdated the registration, the manuscript should say so, with the date, so that the reader does not have to infer it. Either way the registered R1, M1 and the second-addendum verdicts are untouched; the GREIT diagonal is a reference cell and no hypothesis is tested on it. Suggested fix: state the training date of the reused GREIT networks relative to hash 4b4c7a6d in Section 2.2 and in the "Written after reading" cell of Table 4, and record a deviation if the networks predate the registration.
- **Severity**: Major
- **Evidence Anchor**: text: block B0116 "Nothing: no arm trained, no contrast computed" and block B0028 "The GREIT row reuses seeds 0 to 29 of the companion study's 20 dB training"
- **Confidence**: 3 — the tension is on the page; which way it resolves is not

### W3: The Abstract assigns the global-affine collapse to the addendum
The sentence beginning "In a post-unblinding, pre-hashed addendum" goes on to say that a single global normalisation collapsed two reconstructors. The collapse is the registered M1 row (Table 1, standing R); the addendum is the per-source re-run. The sentence mislabels a registered result as addendum and so breaks the manuscript's own rule that each number-bearing sentence names its standing. Suggested fix: "The registered pooled row, with a single global normalisation, collapsed two reconstructors ...; in a post-unblinding, pre-hashed addendum with a per-source affine, pooled training was never worse ...".
- **Severity**: Minor
- **Evidence Anchor**: text: block B0006 "In a post-unblinding, pre-hashed addendum, a single global normalisation collapsed two reconstructors"
- **Confidence**: 4 — standing of each row is given in Table 1 and Table 4

### W4: Rounding of the exploratory no-retraining cost and of the margin distance
From Table 2 and Table 1, the E1 loss for arm D in GN → BP is 0.9672 − 0.629 = 33.8 points, which rounds to 34, while the Abstract, Sections 3.2, 4.1, 4.2 and 4.4 give "19 to 33". Likewise "14 to 58 points outside the margin" (Sections 2.6 and 4.2) is 13.9 and 57.5 from the Table 3 intervals. Neither changes a direction or a verdict; the text should either say "about 19 to 34" or state that the range is over the control arm only, and should round the margin distances consistently.
- **Severity**: Minor
- **Evidence Anchor**: table: Table 2 (block B0110) row GN → BP, E1 Dice 0.647 / 0.629, against Table 1 (block B0106) row R1-GN, D Dice 0.9672
- **Confidence**: 4 — arithmetic from the printed tables

### W5: "Weak cardiac component" is motivated clinically but not shown for this simulation
Section 1.2 grounds the weakness of the cardiac component in measured human data (Leathard et al., 1994), and the research question is framed around a weak component under threat. In the simulation the heart inclusion is at 2.0 S/m on a 1.0 S/m background (contrast +1.0) and the lungs at 0.5 S/m (contrast −0.5); whether the heart's contribution to the boundary voltages or to the reconstructed image is in fact the weaker one here depends on inclusion size and position and is not stated. One sentence giving the ratio of heart-only to lung-only amplitude in the difference frame or in the reconstructed image, per reconstructor, would make the term accurate for this study; without it a reader can reasonably ask whether the branch was tested on a weak component at all.
- **Severity**: Minor
- **Evidence Anchor**: text: block B0023 "two lung inclusions at 0.5 S/m and one heart inclusion at 2.0 S/m"
- **Confidence**: 3 — the needed quantity is computable from the deposited data but not printed

### W6: Multi-centre MRI is not "already on comparable scales"
Section 4.3 contrasts EIT with multi-centre MRI, "where sources are already on comparable scales". MRI intensities have no physical unit and differ across scanners and protocols, which is the reason intensity normalisation is studied at all in that literature; what Albert et al. (2023) support is that the choice among normalisation methods matters little, not that the sources are on one scale. The intended point survives if rephrased: MRI site differences are far smaller than the two orders of magnitude seen here, so the failure here is of a kind that literature does not test.
- **Severity**: Minor
- **Evidence Anchor**: text: block B0072 "Where sources are already on comparable scales, as in multi-centre magnetic resonance imaging (MRI)"
- **Confidence**: 3 — adjacent-field knowledge; the cited paper's own framing should be checked by the authors

### W7: The Sheffield back-projection algorithm is cited only through EIDORS
Back-projection is attributed to the EIDORS toolbox paper. EIDORS distributes the matrix; the algorithm and matrix originate with the Sheffield group, and a domain reader expects the original attribution beside the toolbox one. [UNVERIFIED] search lead: the Sheffield applied-potential-tomography back-projection papers by Barber and Brown (mid-1980s, J Phys E / Clin Phys Physiol Meas). [FIELD-NORM UNVERIFIED]
- **Severity**: Minor
- **Evidence Anchor**: text: block B0024 "Back-projection (BP) used the Sheffield back-projection matrix distributed with EIDORS (Adler and Lionheart, 2006)"
- **Confidence**: 3 — origin of the method is well known; exact metadata not grounded in session materials

### W8: The quarter-amplitude threshold is attributed to Pulletz et al. (2006) without the value being confirmed
Section 2.3 presents the 25% threshold as "the threshold clinical region-of-interest methods apply". My recollection is that the functional-ROI threshold most often attributed to that paper is 20% of the maximum, and that 25% appears elsewhere in the literature. If Pulletz et al. used 20%, the sentence should say "a threshold of the kind" and either keep 25% as the registered choice with a reason or cite the source of 25%. The endpoint itself is registered and unaffected.
- **Severity**: Minor
- **Evidence Anchor**: text: block B0030 "the threshold clinical region-of-interest methods apply to EIT images (Pulletz et al., 2006)"
- **Confidence**: 2 — recollection of the cited paper's threshold, not verified here

### W9: "No significant difference" for Zhao et al. (2014) should be verified against the paper
Section 1.1 states that four algorithms gave five ventilation indices "with no significant difference between them". My recollection of that study is that most parameters were insensitive to the algorithm but not all; if any index differed significantly, the sentence overstates the source. The argument of Section 1.1 (indices are far less sensitive than pixels) survives either way, but the manuscript's own standard requires the attribution to be exact.
- **Severity**: Minor
- **Evidence Anchor**: text: block B0011 "four algorithms applied to the same recordings gave five ventilation indices with no significant difference between them (Zhao et al., 2014)"
- **Confidence**: 2 — recollection of the cited paper's results, not verified here

Numbers checked and found consistent (not findings): Abstract ranges +0.27 to +0.63 against floors 0.34 to 0.66; −0.08 to +0.36 with two intervals above zero; 62, 16, 36 points; M1′ and L1 and L2 expectation hit rates against Table 4; difference-to-floor ratios 0.72 to 0.95; amplitude ratios 161 and 188 from the printed SDs; floor 9.49 as fifteen times 0.631; eight of nine negative out-of-distribution branch differences from Table 2 (E1) and Table 3 (L2); in-pool reference range 0.957 to 0.967; mixed-ps range 0.958 to 0.968; the L2 GN cell's interval, p and seed count. No exploratory number appears in the title or a heading; the Section 3.5 heading carries second-addendum values, which is permitted. The transfer result is phrased as "no evidence" throughout, the branch null as "below the registered floor" and "consistent across the three training conditions tested", pooled training as "never worse", and I found no reconstructor ranking and no claim at another noise level or for learned reconstructors. The companion study is named and not cited, and I found no sentence that relies on its findings; the reuse of its networks is W2.

Questions for the authors (clarifications, not findings): (1) Were the GREIT seeds 0 to 29 trained before or after 2026-09-26, and was their GREIT → GREIT heart Dice known when R3 was registered? (2) For one-step GN "on GREIT's grid", is the inverse parametrised on the 64 × 64 pixel grid through a coarse-to-fine mapping, or solved on a FEM and rasterised? (3) Was Gaussian noise added to the inhomogeneous frame only, with the homogeneous reference noise-free, and is 20 dB the amplitude (norm) ratio of 10? (4) Please confirm the numbers quoted for Holzschuh et al. (2024) (0.76 versus 0.74, p = 0.18) and Yan et al. (2020) (0.89 to 0.60) against those papers; I could not verify them here and they carry the comparison in Sections 4.2 and 4.4. (5) Section 3.2 quotes 131 and 154 for the over-range factor and Section 3.3 quotes 1/132 and 1/156 for the pooled-affine case; a half-sentence saying these are different affines on seed 0 would prevent a reader from reading them as a discrepancy.

---

<!-- card source: perspective.phase2.md sha256 f75198a2ce9825c54123879258c2f9e0d3cb734cc057da5d6382eae10479b9bf -->
contract_role: perspective

## Dimension Scores

### D1: methodology_rigor
score: not_assessed

### D2: domain_accuracy
score: not_assessed

### D3: argumentative_coherence
score: not_assessed

### D4: cross_disciplinary_relevance
score: warn
trigger: "the confirmatory or exploratory standing is left for the reader to infer rather than stated alongside the implication"

### D5: writing_and_structure
score: not_assessed

### D6: venue_fit_and_contribution
score: not_assessed

## Review Body

I read this manuscript as a reviewer from medical-image domain generalisation and multi-source training (leave-one-domain-out protocols, vendor and kernel shift, pooling against specialisation, per-source normalisation), not as an EIT specialist. My remit under the contract is D4 only: whether a reader from an adjacent field can follow the framing of "the reconstructor behaves as a domain", whether the comparison with the multi-source literature is fair, and whether the implications drawn are substantiated by the results reported and carry their evidence standing. I do not assess statistical validity, internal consistency of numbers, or domain-specific correctness; where I noticed something in those areas I have left it to the seats that own them.

Overall, the framing is unusually readable for an outsider. The operational definition of "domain" in Section 1.1 (three signs borrowed from multi-site segmentation, with an explicit disclaimer of domain generalisation), the early statement that the reference moves with the reconstructor so held-out losses are upper bounds, the four-state provenance table, and the prose explanation of the addenda's double standing together let a reader from my field locate every number on the right evidential shelf without opening the registration document. The comparison with the multi-source literature is, on the whole, fair: the manuscript names the structural difference (anatomical label fixed across sites versus a reference that changes with the source), refuses to compare magnitudes, and reports in-pool and out-of-pool performance separately. The weaknesses I found are concentrated where the manuscript synthesises across its three evidence standards, in Section 4.1 and the Conclusion, where the standing labels that are present everywhere else drop away and one descriptive quantity drifts toward an equivalence-like reading. None of them touches the core finding; they are matters of wording that an adjacent-field reader would otherwise quote with more force than the data carry.

### Strengths

### S1: "Domain" is defined operationally and the domain-generalisation claim is explicitly declined
The three-sign definition gives a reader from multi-source training a precise test of what the manuscript means, and the sentence that follows prevents the paper from being read as a domain-generalisation study.
**Evidence Anchor**: text: B0011 "we call the reconstructor a domain if, for a pixel-level post-reconstruction network, a change of reconstructor shows the three signs"

### S2: The moving-reference problem is named in the Introduction and carried through Methods, Results and Discussion
The distinction from leave-one-domain-out protocols in which the label is anatomy is exactly the one a reviewer from my field would raise, and the manuscript raises it first, and uses it to qualify the held-out loss as an upper bound in nearly every place the number appears.
**Evidence Anchor**: text: B0031 "A held-out loss therefore combines a change of input distribution with a change of reference style"

### S3: Magnitude comparison with multi-source segmentation studies is refused rather than made
Section 4.4 cites the nearest vendor-shift and cross-institution analogues and then states why their losses cannot be compared with these.
**Evidence Anchor**: text: B0074 "two differences forbid a comparison of magnitudes"

### S4: Provenance of the preregistration states is readable without the registration document
Table 4 tells an outside reader what each hashed state governs, what had been read when it was written and what it fixed, which is what a reader needs to judge "confirmatory for its own runs, exploratory in origin".
**Evidence Anchor**: table: Table 4 (B0116)

### S5: No selection on the held-out source
The manuscript states the model-selection constraint that domain-generalisation evaluation protocols have been criticised for violating, and cites that critique.
**Evidence Anchor**: text: B0034 "nothing in the held-out protocol is selected on the held-out reconstructor"

### S6: The double standing of the addenda is explained in prose before any addendum number appears
An adjacent-field reader does not need to know the confirmatory-methodological-research vocabulary to understand how to weigh the addenda.
**Evidence Anchor**: text: B0019 "the addenda have a double standing: confirmatory for their own runs, exploratory in origin"

### S7: The global-affine failure is shown as what the network saw, not only as a Dice number
Fig 3 as captioned puts the two normalisation paths on one colour scale with the within-frame SD printed, which is the figure a multi-source practitioner would want in order to recognise the failure mode in their own data.
**Evidence Anchor**: figure: Fig 3 caption (B0101)

### Weaknesses

### W1: Section 4.1 and the Conclusion drop the standing labels and move M2′ toward an equivalence reading
Everywhere else the manuscript labels each number with its standard. In the Conclusion the sentences that carry numbers do not name it: the no-retraining cost (exploratory), "stayed below the floor" in pooled training (first addendum), and the retraining-versus-pooling comparison (first addendum, descriptive) appear in one register, and only the leave-one-out losses say "fixed before the runs". More importantly, "could not be separated at 0.4 points" (also in B0066, "the two ways of doing so could not be separated at 0.4 points") is an equivalence-shaped statement about M2′, which the manuscript itself classifies as reported, not tested, and which in two of six intervals does separate the two remedies in pooling's favour. A reader from multi-source training would quote this as "pooling equals retraining", which the Abstract's own wording ("never worse", two intervals favour pooling, confounded with threefold steps) carefully avoids. Suggested remedy: in B0066 and B0085 replace the phrase with the Abstract's form, for example "pooled training with a per-source affine was never worse than retraining (first addendum; descriptive, −0.08 to +0.36 points, two of six intervals favouring pooling and confounded with optimisation steps)", and give each number-carrying sentence of the Conclusion its standard in brackets.
**Severity**: Major
**Evidence Anchor**: text: B0085 "two remedies that could not be separated at 0.4 points"
**Confidence**: 4 — multi-source training reviewer; the manuscript's own stated rules for descriptive quantities and for "never worse" make the standard explicit

### W2: "Inclusion, not diversity" is asserted in 4.1 but is "neither seen nor contradicted" in 4.4
Section 4.4 correctly states that the diversity claim was neither supported nor contradicted (two sources, thirty seeds, ±2 to ±7 point intervals, different affine policies on the two sides). Section 4.1 states the same L3′ result as a positive characterisation of the mechanism. From the domain-generalisation side, the inclusion-versus-diversity question is live and a two-source pool is close to the weakest possible test of it; the 4.1 sentence will be read as a finding against diversity. Suggested remedy: rewrite as "within this study, two-source pooling showed no evidence of helping on a third source, so the benefit demonstrated here is one of inclusion; whether diversity adds anything was not resolved (Section 4.4)".
**Severity**: Minor
**Evidence Anchor**: text: B0067 "within this study the benefit of pooling is one of inclusion, not of diversity"
**Confidence**: 4 — the two sentences are compared within the manuscript; the field's reading of such a sentence is my competence

### W3: The Section 3.5 heading and the Table 3 caption carry the held-out losses without the upper-bound qualification
The manuscript's own rule is that the held-out loss always carries its upper-bound qualification. The body of 3.5, the Abstract, 4.1, 4.2, 4.4 and the Conclusion comply; the heading of 3.5 and the Table 3 caption do not. A reader skimming headings and tables, which is how a reviewer from my field would first compare these numbers with leave-one-domain-out losses in the literature, meets 62, 16 and 36 points as if they were input-side generalisation losses. Suggested remedy: either remove the numbers from the heading or add "(upper bound)" to the heading and a one-clause note to the Table 3 caption.
**Severity**: Minor
**Evidence Anchor**: text: B0058 "Pooled training does not generalise to a reconstructor outside the pool: 62, 16 and 36 points"
**Confidence**: 4 — the rule is stated in the manuscript; locating the exceptions is a reading task

### W4: The registered interpretation sentence for R3 presupposes a contrast an outside reader cannot reconstruct
"Whatever shift tolerance the branch has is specific to the kind of shift" is a fixed sentence and I do not ask that it change. But to a reader without the companion study it is opaque: what other kind of shift is in view, and where was tolerance to it observed? The manuscript may not rely on the companion's findings, so the context cannot come from there. A neutral clause outside the fixed sentence would suffice, for example "the kind of shift tested here is a change of reconstructor; other kinds, such as a change of measurement-noise level, were not tested in this study", which states a design fact and no result.
**Severity**: Minor
**Evidence Anchor**: text: B0049 "whatever shift tolerance the branch has is specific to the kind of shift"
**Confidence**: 3 — I can judge the reader's experience but not what the registration permits around the fixed sentence

### W5: "Affine" is used as a noun throughout but is never defined at first use as location-scale standardisation
Readers from multi-site imaging will recognise the operation once they reach 4.4, where the fixed affine is called a location-scale baseline, but at first use in 2.2 and throughout 2.4, 3.2 and 3.3 the word has to be inferred. One clause at B0028, for example "a fixed per-dataset standardisation (subtract the training-split mean, divide by its standard deviation), referred to below as that dataset's affine", would settle the term for every later section and make the per-source versus global contrast legible to a harmonisation reader.
**Severity**: Minor
**Evidence Anchor**: text: B0028 "one dataset-wide normalisation affine estimated from that dataset's training split and applied to inputs and targets"
**Confidence**: 4 — terminology accessibility to the adjacent field is my remit

### W6: "Noise figure" is defined only by citation
The three reconstructors are matched on noise figure, and the matching rule is one of the two recorded deviations, yet the quantity itself is introduced only as "after Adler and Guardo (1996)". A reader from CT or MRI harmonisation, who will want to know whether the matching makes the three operators comparable in the sense they are used to, needs one clause (what ratio the noise figure is and why matching it is the fair comparison), not the reference alone. The domain seat should judge whether the setting is defensible; my point is only that the term is not self-contained.
**Severity**: Minor
**Evidence Anchor**: text: B0024 "noise figure after Adler and Guardo (1996)"
**Confidence**: 3 — I can report the gap for an outside reader but not the field's convention

### W7: "Reference" carries two meanings
"Reference" names the target image (each reconstructor's own single-organ reconstruction, which moves with the reconstructor and is the basis of the upper-bound argument) and also the untested reference cells ("ref" in Table 1, "in-pool reference cells" in 3.5). In a paper whose central caveat is that "the reference moves", a second meaning of the word in the same sections costs an outside reader a re-read. Suggested remedy: call the cells "comparison cells" or "in-pool anchors" and keep "reference" for the target image.
**Severity**: Minor
**Evidence Anchor**: text: B0059 "The six in-pool reference cells of the same rows scored 0.957 to 0.967"
**Confidence**: 4 — a reading-clarity observation within my remit

### W8: The practical implication of a source-aware recipe is not spelled out for a reader outside EIT
The manuscript states, correctly and repeatedly, that every pooled-training statement carries the clause that the deployment affine is the deployed reconstructor's own. In domain-generalisation terms this is a domain label required at test time, which is a known limitation of domain-specific normalisation. In EIT the reconstructor identity is presumably always known to the operator, so the requirement is harmless in practice, but the manuscript never says so, and Section 4.7 is where an adjacent-field reader would expect it, together with the point already made in 4.2 that "the same reconstructor" must be defined as algorithm, implementation and hyperparameters for the label to be reliable. One sentence would close the gap and would also make clear that the recipe is domain-aware, not domain-agnostic.
**Severity**: Minor
**Evidence Anchor**: absence: Section 4.7 (B0083) — expected a statement of whether the reconstructor identity needed to select the per-source affine is available at deployment and what that requires; checked Sections 2.4, 4.2, 4.7 and the Conclusion
**Confidence**: 4 — the test-time domain-label question is a standard one in my field; whether the identity is always available in EIT practice is for the authors to confirm

### W9: "A simulated review round" appears in 4.5 before it is explained
The Acknowledgments disclose that simulated peer-review panels were run with an AI assistant and recorded in the repository; Section 4.5 uses the phrase as part of the answer to the "preregistration as decoration" objection without that explanation. A reader who has not yet reached the Acknowledgments cannot tell what the round was or why its being on record matters. A parenthetical pointer to the Acknowledgments and the repository record would suffice.
**Severity**: Minor
**Evidence Anchor**: text: B0078 "the second addendum's rows were those a simulated review round, recorded in the repository before the addendum was written, had asked for"
**Confidence**: 3 — accessibility observation; the editorial seat may have a view on where such disclosure belongs

### Cross-disciplinary notes and questions for the authors

The comparison with the multi-source literature is fair in the respects I can judge: the Holzschuh et al. (2024) contrast is used to illustrate a methodological point about non-significance and equivalence, not to criticise that study's conclusion; the CT-kernel analogues are the right nearest neighbours; and the moving-reference caveat is applied to the manuscript's own numbers rather than only to others'. Two questions, which the authors may answer in a sentence each: first, is the reconstructor identity always available at deployment in the clinical EIT systems the planned hardware study targets, so that the per-source affine can be selected without inference (W8); second, since the mixed-ps row leaves GREIT heart targets weighing up to 1.7 times GN's in the loss, do the authors regard target-scale weighting as part of the per-source normalisation question for a future row, or as outside the paper's scope?

Reading leads, offered as search directions and not as citations: the protocol paper that formalised leave-one-domain-out model selection without access to the held-out domain [UNVERIFIED, search lead: Gulrajani and Lopez-Paz, "In Search of Lost Domain Generalization", ICLR 2021], if the authors wish to name the protocol they already follow in Section 2.4; and the domain-specific batch-normalisation line already cited (Karani et al., 2018) is the appropriate anchor for the "domain label at test time" sentence suggested in W8, so no new citation is needed there.

---

<!-- card source: da.phase2.md sha256 eadb512dcd4632a09299da1f4f7c169deabb290754187051c47dc83d39ebf1da -->
contract_role: da
## Dimension Scores

### D1: methodology_rigor
score: not_assessed

### D2: domain_accuracy
score: not_assessed

### D3: argumentative_coherence
score: block
trigger: "a post-unblinding or exploratory result is presented with confirmatory standing in the abstract or conclusions"
block_class: repairable

### D4: cross_disciplinary_relevance
score: not_assessed

### D5: writing_and_structure
score: not_assessed

### D6: venue_fit_and_contribution
score: not_assessed

## Review Body

**What the manuscript genuinely does well.** The two registered branch cells are judged exactly as the rule reads, with floor, interval, W and p side by side (table: Table 1, rows R1-GN and R1-BP, B0106), and both are called falsified although both p values pass; a less disciplined paper would have called them positive. The four no-retraining cells that the amplitude gap made unreadable are exposed rather than buried (text: B0050 "those four cells measure both arms' response to an input the network cannot read"). The pooled-training confound is volunteered against the authors' own interest (text: B0057 "this design cannot separate the benefit of three renderings per geometry from that of three times the steps"). Twenty falsifications out of twenty are reported as such, the expectation hit rates are printed as they fell, and the limitations section names the corresponding author's conflict of interest. These are real strengths and the Major rows below do not erase them; they are about the distance between what the rules licence and what the headline sentences say.

**Strongest counter-argument.** Strip the manuscript to what its registered rules actually established and little remains: two branch cells below a floor on two reconstructors, a transfer hypothesis that four of six cells could not test because the pilot never compared amplitude scales, and a pooled row that failed for the same unanticipated reason. Every number a reader will quote (62, 16 and 36 points; "never worse"; 19 to 33 points) comes from two addenda written after the registered matrix had been read and after its failure had been diagnosed, or from quantities the addenda themselves declare verdict-free. The thesis of the Discussion, "the reconstructor behaves as a domain", is defined in Section 1.1 by three signs, and only the third (L1) was ever tested against a rule: the first sign rests on the exploratory E1 re-scoring and the second on M2′, which Section 3.4 says is "reported, not tested" and whose six values include a negative one. The manuscript's own standard, stated at B0044 and repeated in each addendum, is that descriptive quantities carry no verdict; yet the abstract and the Conclusion present the recovery of the loss by pooling, the 0.4-point inseparability of the two remedies and the 62/16/36 losses in one register, and close with "every verdict followed a rule", a sentence that lends verdict standing to claims that never had one. The fixed interpretation sentences are applied selectively: the degenerate cells count as falsifications of the transfer hypothesis and the registered reading is applied to them, while the equally degenerate pooled cells have their registered interpretation withheld after the fact, and in both cases the choice favours the narrative that the branch fails and pooling works. The branch null is one design family's null stated at three layers, and the one held-out cell with a measurable effect (GN, −3.9 points, interval excluding zero) is summarised in a heading and in the abstract as "nothing measurable". None of this overturns the data; all of it means the paper's claims about its own epistemic standing are not yet true of the text.

**Why block rather than warn.** My Phase 1 warn trigger covers standing blurred in one Discussion or abstract sentence. Here the blur is systemic: the Conclusion paragraph carries no standing label on any number, Table 1 gives a verdict to a cell its own caption calls "not tested", the abstract's "never worse" sits beside a negative value, and a heading states a null the body's statistics contradict. Each is repairable by rewriting, none touches the per-seed data, so the block is repairable and not fatal.

**Minor findings (prose; none changes a core claim).** (1) The exploratory no-retraining cost is given as "about 19 to 33" points in B0051, B0066 and B0070, but from Table 2 the D arm on GN → BP under E1 loses 0.9672 − 0.629 = 33.8 points, so the stated range omits its own largest value (anchor: table: Table 2, E1 Dice column, row GN → BP, and Table 1 row R1-GN, B0110 and B0106; confidence 4, arithmetic from the tables). (2) M3′ is introduced as "the share of the no-retraining loss that pooling removed" (B0057) but tabulated in points, and the registered-path absolute Dice it subtracts from appear nowhere in the main tables, so the reader cannot recompute it from the manuscript (anchor: absence: Table 2 and Section 3.4 — expected the registered-path absolute Dice of the six no-retraining cells and a definition of M3′ as points or fraction; checked Table 2, its footnote, Section 3.2, Section 3.4, S1 Table caption; confidence 3, arithmetic from the tables). (3) Section 2.5 states that no setting or rule changed while the same sentence refers to "the change of matching rule from GREIT's nominal to its realised value" for the GN hyperparameter; whether that change preceded or followed registration is not said (anchor: text: B0036 "the change of matching rule from GREIT's nominal to its realised value"; confidence 3, reading of the deviation record). (4) "Within this study's scope the term 'reconstructor-agnostic' is falsified" (B0069) falsifies a term nobody in the manuscript or its cited literature is shown to have claimed for this pipeline (anchor: text: B0069 "is falsified, and any source-aware statement must read"; confidence 3, logic of the argument). (5) The loss order across held-out reconstructors is explained as the pool's coverage in the indicative mood, "is the two-source pool's coverage of the held-out reconstructor", an untested mechanism stated as fact in the same section whose later paragraph calls mechanisms untested (anchor: text: B0059 "is the two-source pool's coverage of the held-out reconstructor, not a ranking of reconstructors"; confidence 3, logic of the argument). (6) The Conclusion's opening, "the separation benefit of a decoder branch for the cardiac component does not appear under a change of reconstructor", uses a no-effect formulation where every other statement of the result says below the floor, and bundles matched-training cells on other reconstructors under "a change of reconstructor" (anchor: text: B0085 "does not appear under a change of reconstructor"; confidence 3, reading of the fixed vocabulary). (7) Contribution one says the branch null "extends" to two other reconstructors; a null can only extend from a prior null, which is either the companion study the paper says it does not rely on or the Table 1 reference cell it labels not tested (anchor: text: B0020 "the matched-training null of the branch extends to the two other conventional reconstructors"; confidence 3, logic of the argument).

**Alternative explanations the text does not close.** For the held-out losses: a reference-style mismatch between the held-out reconstructor's heart image and the style the network learned is a rival account of part of each loss; the manuscript names it, calls the loss an upper bound, and then reports that the attribution "was not measured", so the direction of the bound is asserted and the only support is a one-seed inspection that Section 4.6 itself calls untested. For the pooled benefit: threefold optimisation steps, named by the authors and not separable here. For the branch's negative sign in eight of nine out-of-distribution cells: the authors' own suggestion that a two-decoder arm has more ways to fail once its control has failed is at least as parsimonious as any specialisation account and is correctly left as a hypothesis. Stakeholder voice absent: a reader who must deploy a trained network on a hospital system whose reconstructor implementation differs in settings only; the manuscript says the variant case was not tested but the title and abstract speak of "a change of reconstructor" without that distinction.

**Field-norm and parity statement.** No Major row below rests on a claim about what the field should do; each rests on the manuscript's own stated standard (B0044, B0037) or on internal consistency between its sentences and its tables, so the Field-Norm columns are marked not applicable rather than left to an unverified norm. Each concern was checked against the bundle as a substantive claim regardless of how formally the manuscript phrases the sentence it attacks.

#### CRITICAL
| # | Dimension | Issue Description | Evidence Anchor | Confidence | Field-Norm Boundary | Evidence-Crossing Rationale |
|---|-----------|-------------------|-----------------|------------|---------------------|-----------------------------|

#### MAJOR
| # | Dimension | Issue Description | Evidence Anchor | Confidence | Field-Norm Boundary | Evidence-Crossing Rationale |
|---|-----------|-------------------|-----------------|------------|---------------------|-----------------------------|
| 1 | Logic chain / standing | The Conclusion presents the recovery of the loss by pooling, the 0.4-point inseparability of the two remedies (M2′, declared "reported, not tested" at B0056) and the 62/16/36 losses (second addendum) with no standing label on any sentence, then closes with "Every verdict followed a rule written and hashed before the data it judged were read", lending verdict standing to descriptive and addendum quantities. The abstract does the same for the "never worse" sentence (addendum-labelled, not descriptive-labelled). This breaches the manuscript's own rule at B0044 that every addendum quantity is labelled, and it is the trigger for the D3 block. | text: B0085 "two remedies that could not be separated at 0.4 points, and by nothing else that was tested" | 4 — preregistration reporting practice and reading of the manuscript's own standard | n/a: internal consistency with the manuscript's stated standard | n/a |
| 2 | Data-text consistency | "Never worse than retraining" is stated as a contribution (B0020), a heading (B0055), in the abstract and in the Conclusion, yet one of the six M2′ point estimates is negative (D on BP, −0.083 points, B0108) and the abstract's own parenthesis begins at −0.08. The defensible descriptive summary is "no interval below −0.32 points and no point estimate below −0.08", not a universal. Because M2′ carries no verdict, a universal descriptive claim is also a verdict in disguise. | text: B0006 "pooled training was never worse than retraining on the deployed reconstructor" | 4 — arithmetic from Table 1 and the fixed vocabulary of the manuscript | n/a: internal consistency | n/a |
| 3 | Selective application of fixed interpretation | The registered interpretation of a falsified M1 is withheld for the GN and BP cells because the input was unreadable, but the same unreadability in four R3 cells does not stop those cells being counted as falsifications in the abstract ("falsified in all six cells") with the fixed reading applied (B0049). The withheld interpretation sentence is never quoted, so the reader cannot judge what was set aside, and this post-read decision is absent from the deviation record, which lists only two pre-read deviations (B0036, B0116). Both asymmetric choices favour the narrative. | text: B0053 "the registered interpretation of a falsified M1 is not applied to them" | 4 — preregistration deviation reporting and logic of the stated rules | n/a: internal consistency | n/a |
| 4 | Data-conclusion mismatch | "No measurable effect at any of the three layers" (B0067), the heading "adds nothing measurable" (B0062) and the abstract's "added nothing measurable" contradict the manuscript's own statistics: Section 3.1 insists the matched differences are "below the floor, not zero" with p below 0.05 and intervals excluding zero in four of five cells (B0047), and the held-out GN cell shows −3.9 points, interval −5.3 to −2.4, p 0.00012 (B0113). A measured negative effect is not "nothing measurable"; it is a measurable effect below or opposite to the floor, which is what the rule vocabulary ("below the registered floor") was written to say. | text: B0067 "the one architectural remedy tested, the branch, had no measurable effect at any of the three layers" | 4 — arithmetic from Tables 1 and 3 and the manuscript's own Section 3.1 | n/a: internal consistency | n/a |
| 5 | Standing in tables and abstract | Table 1 defines "ref = reference, not tested" and then gives the GREIT → GREIT row the verdict "falsified"; the cell is not among the twenty verdict cells counted at B0077, yet the abstract says the branch "stayed below the registered floor on every reconstructor", folding a non-registered reference cell into the registered claim. Either the cell has a verdict or it is a reference; the table and caption cannot both stand. | table: Table 1, row GREIT → GREIT, columns Standing and Verdict (B0106) | 4 — reading of Table 1 against its caption and B0077 | n/a: internal consistency | n/a |
| 6 | Unsupported inference | The held-out loss is called "an upper bound on the input-side generalisation loss" in the abstract, B0011, B0031, B0059, B0066, B0070, B0074, B0080 and B0085, but the bounded quantity is never operationally defined (there is no reconstructor-independent reference in the design) and its direction is never shown; the only support is a one-seed description that Section 4.6 calls untested, and the manuscript itself says the attribution was not measured. An unmeasured decomposition cannot license a bound in either direction; the honest statement is that the loss conflates input and reference change and was not decomposed. | text: B0031 "How much of a given loss is attributable to the reference style was not measured." | 3 — logic of the stated endpoint; domain mechanisms left to the domain seat | n/a: internal consistency | n/a |
| 7 | Defence of preregistration standing | Section 4.5 answers the "decoration" objection partly by asserting that both addenda "went against the authors' own recipe", but Table 4 records that each addendum expected exactly the falsifications that occurred (M1′ 3 of 3 verdicts; L1 3 of 3; L2 3 of 3), so the results met the authors' stated expectations rather than going against them; "turned the pooled recipe from generalises into in-pool only" presupposes a prior generalisation claim the manuscript never made. The title attaches "preregistered" to "leave-one-reconstructor-out training", a design that exists only in the second addendum written after two rounds of results had been read (B0116). | text: B0078 "Both addenda went against the authors' own recipe" | 3 — logic of the argument against Table 4; title reading | n/a: internal consistency | n/a |

---
