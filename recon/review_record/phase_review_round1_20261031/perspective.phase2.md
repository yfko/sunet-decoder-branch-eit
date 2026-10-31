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
