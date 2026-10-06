contract_role: domain

## Dimension Scores

### D1: methodology_rigor
score: not_assessed

### D2: domain_accuracy
score: warn
trigger: "several citation sentences that overstate or over-generalise an abstract in ways that do not change the gap"

### D3: argumentative_coherence
score: not_assessed

### D4: cross_disciplinary_relevance
score: not_assessed

### D5: writing_and_structure
score: not_assessed

### D6: venue_fit_and_contribution
score: not_assessed

## Review Body

Reviewer identity: thoracic EIT physiologist/engineer (ventilation and cardiac-related signal separation, GREIT and EIDORS, instrument SNR and electrode artefacts, deep-learning post-processing of EIT). Calibration status: NOT_CALIBRATED. I could not fetch any source; every judgement below is from my own reading knowledge of the cited papers, and the Confidence field says how far that knowledge reaches.

Summary. The cardiac-separation lineage in the Introduction is the one a thoracic EIT reader would expect, in the right order and with the right original sources: ECG-gated averaging of applied potential tomography (1988), frequency-domain filtering (1992), PCA-plus-template fitting (2008), adaptive harmonic estimation (2025), the breath-hold-trained Siamese feature-matching method (2022), with the Borges piglet study correctly used to keep pulsatility apart from perfusion. The post-reconstruction deep-learning lineage (Deep D-bar, graph U-net, D-bar organ boundaries) is correctly characterised, and the paper is right that its network belongs there. The dual-branch disambiguation against Wang et al. and Yu et al. is correct and useful. The EIDORS SNR convention, the GREIT description, the Adler and Guardo noise-figure lineage and the Gagnon mesh-phantom result are stated as the field states them. Against that, I found one citation sentence that misreads its source (Graf and Riedel), one attribution that conflates the GREIT quarter-amplitude set with the clinical ROI thresholds of Pulletz, one sentence that files a bioimpedance cardiac-output study under EIT, and one place where the original saline-bolus source is cited second-hand. None of these changes the gap or the result. The one domain issue that bears on how the field will read the contribution is framing: the Introduction motivates the problem with cardiac-related changes *inside the lung field* (refs 4, 5, 8, 14), where the cardiac and ventilatory components overlap spatially, while the phantom's cardiac component is a conductive heart disc spatially disjoint from the lung discs. The paper says the simulation is not a thorax, but it does not say that this particular feature of the in-vivo problem, the spatial overlap that ref 14 names as the limitation of existing methods, is absent by construction.

Citation sentences checked (34 added sentences plus the earlier 19). Represented correctly to the best of my knowledge, high confidence: 1, 2, 3, 6, 9, 12, 21, 22, 23, 25–35, 37, 38, 39, 43–51, 53. Represented correctly with moderate confidence (I know the paper but not the specific number or phrase attributed): 4 (the 9% and 0.9–2.6% figures), 8, 10 (the "about fifteen seconds" figure), 11, 13, 15 (the "three patients" count), 19, 20, 52 (the word "ringing"). Sentences I could not check because I do not know the paper well enough to vouch for the attributed claim: 14, 24, 36 (in particular the claim that its noise evaluation was without retraining), 40, 41, 42. Misread or misattributed: 5, 7, 41 (see W2–W4).

### S1: Cardiac-separation lineage is correct, complete and primary-sourced
The Introduction's second paragraph names the standard routes with their original papers rather than reviews, in chronological order, and correctly states that every one of them works on the pixel time series. The Deibele description (PCA combined with frequency filtering, beat-by-beat after a short set-up) matches that paper, and the Silva sentence correctly identifies spectral and spatial overlap as the named limitation.
**Evidence Anchor**: text: §1 paragraph 2 "the methods used to recover them all work on the pixel time series"

### S2: Pulsatility is correctly kept apart from perfusion
The Borges piglet study is used for exactly what it showed, bolus first-pass agreeing with SPECT and beating the pulsatility estimate, and the paper draws the correct consequence that a frame-wise method recovers the cardiac-related component of the image, not blood flow. This distinction is often blurred in the deep-learning EIT literature and is handled correctly here, and it is repeated in Limitation 4.
**Evidence Anchor**: text: §1 paragraph 1 "what any frame-wise method recovers is the cardiac-related component of the image, not a measurement of regional blood flow"

### S3: Post-reconstruction deep-learning lineage correctly characterised
Deep D-bar (simulation-trained, applied to tank data without transfer), the graph U-net (domain-independent post-processing) and Capps and Mueller (organ boundaries from scattering transforms) are each described as they read, and the paper correctly places itself in that line rather than in learned reconstruction from voltages.
**Evidence Anchor**: text: §1 paragraph 4 "A second line keeps a conventional reconstructor and places the network after it."

### S4: Dual-branch terminology disambiguated correctly
The Wang et al. and Yu et al. architectures do branch on the encoder or fusion side and reconstruct conductivity from voltages; the paper is right that they are not the same design and not competing on the same task.
**Evidence Anchor**: text: §4.3 "branches on the encoder side and reconstructs from voltages"

### S5: Instrument and reconstructor facts stated as the field states them
The EIDORS SNR convention (norm of the difference frame over norm of the noise), the Adler and Guardo 1996 contrast-detection and noise-amplification framing, the Gagnon mesh-phantom finding that system SNR depends on frame rate, frequency, current and strategy, and the Boyle and Adler point that electrode-area and contact-impedance errors are structured artefacts rather than additive noise are all correct, and the paper correctly refuses to tie 40 dB to any instrument.
**Evidence Anchor**: text: §2.3 "the ratio of the norm of the difference frame to the norm of the noise"

### W1: The phantom's cardiac component is spatially disjoint from the lungs, and the framing does not say so
The Introduction motivates the problem with cardiac-related impedance changes in the lung field (Leathard, Graf and Riedel, Frerichs 2009) and with the spectral and spatial overlap that Silva et al. name as the limitation of existing methods. In vivo, the cardiac-related component that matters for perfusion is the pulsatile change inside the lung regions, co-located with the ventilation signal; the heart-region signal is the part the clinical methods usually discard. The phantom reconstructs a heart disc at 2.0 S/m beside lung discs at 0.5 S/m, so its cardiac component is spatially separate from the lungs and opposite in sign, and the spatial-overlap difficulty that the Introduction invokes is absent by construction. The paper's statement that the cylinder is not a thorax and that the component is not perfusion covers part of this, but not the specific point that the hard feature of the in-vivo separation problem is not represented. A thoracic EIT reader will see the title ("the cardiac component of lung EIT") and expect the former. Remedy: state in §2.3 and Limitation 3 that the simulated cardiac component is the heart-region contrast, spatially disjoint from the lung regions, so that the frame-wise task here is easier in that respect than the in-vivo problem; consider whether the title should say "simulated" or "heart-region component". No new data are needed. Severity reflects that the framing of the contribution, not the measured result, is affected.
**Severity**: Major
**Evidence Anchor**: text: §1 paragraph 1 and §2.3 "The cardiac-related signal in the same frames carries information of its own." "two lung inclusions at 0.5 S/m and one heart inclusion at 2.0 S/m"
**Confidence**: 4 — I know the in-vivo cardiac-related signal distribution and the phantom convention of the original semi-Siamese study well; I have not seen the authors' supplementary phantom figures beyond Fig. 1.

### W2: Graf and Riedel (ref 5) is about body posture, not location in the thorax
Graf and Riedel measured healthy volunteers in supine, prone and lateral positions and reported that the amplitude of cardiac-related impedance changes depends strongly on body position (posture). The manuscript reads "position" in the title as anatomical position within the thorax. The sentence should say that the amplitude depends strongly on body position, which still supports the point being made (the signal is small and variable). The Leathard sentence immediately before it already carries the regional-variation claim.
**Severity**: Minor
**Evidence Anchor**: text: §1 paragraph 1 "its amplitude depends strongly on position in the thorax [5]"
**Confidence**: 4 — I know this paper's design; I have not re-read its abstract today.

### W3: The quarter-amplitude set is a GREIT figure-of-merit convention, not the clinical ROI threshold of ref 7
The 0.25 threshold the paper uses (EIDORS `calc_hm_set(img, 0.25)`) is the quarter-amplitude set defined in the GREIT figures of merit (ref 39). Pulletz et al. (ref 7) compared clinical lung-ROI definitions and, to my recollection, used functional-image thresholds of 20% and 35% of the maximum, with 20% the value later adopted in clinical practice, not 25%. The sentence attributes the quarter-amplitude threshold to clinical ROI methods via ref 7. Remedy: cite ref 39 for the quarter-amplitude set and, if ref 7 is kept, say that clinical ROI thresholds are of the same order (20–35%) rather than that they are the quarter-amplitude threshold. The same wording appears in the Fig. 2 legend.
**Severity**: Minor
**Evidence Anchor**: text: §1 paragraph 1 "Applying the quarter-amplitude threshold that clinical region-of-interest methods use [7]"
**Confidence**: 3 — I am sure of the GREIT definition; I am less sure of the exact threshold values Pulletz tested.

### W4: Ref 41 is a bioimpedance cardiac-output study and is filed under EIT
The sentence lists three precedents for random measurement degradation during training "in EIT". Murphy et al. (ref 41) is, by its own title, a bioimpedance approach to cardiac-output measurement, and to my knowledge it is not an EIT reconstruction or post-processing study; I also cannot confirm from memory that the degradation it drew was "unspecified poor electrode contact". Remedy: either verify the sentence against the full text and reword the lead-in to "in impedance measurement" or drop ref 41 and keep refs 40 and 42, which are EIT.
**Severity**: Minor
**Evidence Anchor**: text: §2.4 "with unspecified poor electrode contact for cardiac-output estimation [41]"
**Confidence**: 2 — I know the group and the title, not the method section.

### W5: The saline-bolus perfusion method is cited second-hand
The bolus method is introduced through Borges 2012 (ref 6) and Stowe 2019 (ref 13). The original demonstration of saline-bolus perfusion EIT against electron-beam CT is Frerichs et al., J. Appl. Physiol. 2002 (I can attest the paper exists; volume and pages should be verified before use). Given that the desk rejection cited a thin reference list, adding the primary source is cheap. [FIELD-NORM UNVERIFIED] — the expectation that the primary source be cited is a general citation norm I have not grounded in a venue policy, so this stays Minor.
**Severity**: Minor
**Evidence Anchor**: absence: §1 paragraph 1 and §4.4 — expected the original saline-bolus perfusion EIT reference as the primary source for the bolus method; checked Introduction, Discussion, Limitations and the reference list
**Confidence**: 4 — I know the 2002 paper; I have not checked its bibliographic details today.

Further domain notes without a severity. (a) The number attributed to Leathard (0.9–2.6% cardiac-related versus about 9% ventilatory) is plausible but I cannot confirm the exact range from memory; it should be checked against the abstract once more before submission. (b) The claim that Wang et al. (ref 36) evaluated across test-frame SNR without retraining is the one methodological precedent the paper leans on for its sweep design, and it is one I cannot vouch for; it deserves a full-text check rather than an abstract check. (c) The Herzberg sentence says the graph U-net was applied "including three-dimensional measurements"; I recall domain-independence across meshes and devices but am not certain of a 3D case. (d) The title of ref 22 carries a stray "⋆" from the publisher's metadata. (e) The contribution statement is correctly positioned: I know of no EIT study that takes the matched-capacity multi-decoder versus single-decoder contrast across noise levels as its subject, and the nearest EIT precedent is indeed the original semi-Siamese paper. (f) Terminology is otherwise consistent with field usage; "cardiac-related", "perfusion" and "pulsatility" are kept apart throughout, and "Dice points" is defined before use.
