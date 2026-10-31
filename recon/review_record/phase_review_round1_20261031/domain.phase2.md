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
