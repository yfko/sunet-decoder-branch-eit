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
