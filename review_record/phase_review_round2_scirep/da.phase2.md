contract_role: da

## Dimension Scores

### D1: methodology_rigor
score: not_assessed

### D2: domain_accuracy
score: not_assessed

### D3: argumentative_coherence
score: block
trigger: "a rival explanation left open by the design fits the reported data at least as well as the authors' mechanism"
block_class: repairable

### D4: cross_disciplinary_relevance
score: not_assessed

### D5: writing_and_structure
score: not_assessed

### D6: venue_fit_and_contribution
score: not_assessed

## Review Body

What the paper genuinely does well should be said once. Two hashed preregistrations, a hashed addendum written in response to an adversarial objection, a scoring defect disclosed with its wrong numbers, a registered rule reported as falsified although the interval excludes zero, and a 9.2-fold shrinkage of the paper's own best result reported in the abstract: this is the opposite of cherry-picking at the level of outcomes. The challenge below is not that results were hidden. It is that the inference drawn from the addendum is not the inference the addendum licenses.

The strongest counter-argument. The paper's declared thesis (Section 1) is a conditional: the branch helps only when the weak component is under threat. Section 4.1 gives "under threat" an operational reading from the paper's own numbers: at 40 dB the control arm still recovers the heart at 0.966, at 20 dB (trained at 40) it has lost 8.8 points. Apply that same reading to the addendum condition. Trained and evaluated at 20 dB, the control arm reaches 0.9574, a loss of 0.8 points relative to 40|40. By the paper's own definition the cardiac component is not under threat at 20|20. The thesis therefore predicts exactly what H5 found: a sub-floor advantage. Yet the paper reads the falsified H5 as evidence against the mechanism ("The mechanism has not been confirmed... most of the effect is the latter") and promotes "most of that benefit is mismatch tolerance" to the abstract and the conclusion. Retraining at 20 dB removed the training-evaluation mismatch and, at the same time, removed the threat, because a network trained on the noise no longer loses the component to it. The two explanations the pre-submission review said the sweep could not separate are still not separated: they were co-varied, not dissociated. A design that dissociates them needs a cell with threat but no mismatch (matched training at a level where the retrained control still loses several points, or a phantom where it does) or mismatch without threat (train at 20, evaluate at 40, an upward shift). Neither was run. The statement the Introduction says the paper tests never receives a verdict; Section 4.4 says one cell of its grid was tested and the conclusion answers a different question. The paper's self-declared "most useful result" is an attribution its data cannot carry.

A second rival explanation concerns the one registered confirmation that survives, H3. The primary contrast confounds "branched" with "unwidened blocks": D carries two decoders of the original width, B_wide one decoder widened by 1.53. At 40|40 that does not matter, since D minus B and D minus B_wide differ by 0.03 points. Under distribution shift it may: whether a widened decoder tolerates unseen noise worse than a narrow one is exactly the question arm B at 20 dB would answer, and whether a split at the last block (C_wide) already yields the 2.1 points would say whether the branch from the bottleneck is what matters. All 290 runs exist and the registered sweep evaluated "the trained models", but Table 2 and Section 3.2 report D and B_wide only. If B degrades like D rather than like B_wide, the mismatch-tolerance advantage belongs to decoder width, not to the branch, and the positive clause of the headline would be mis-attributed twice over.

Cherry-picking check. Outcome-level selection is absent and disclosure is unusually complete. Emphasis-level selection appears in two places. First, Section 3.1 describes the 40 dB difference as "a near-zero residual whose sign happened to be positive", while Section 3.5 reports that the two matched-training conditions "give the same answer" at 0.223 and 0.229 points, both with seed-level intervals excluding zero and geometry-level intervals of 0.183–0.266 and 0.184–0.276. A quantity replicated at two training levels with intervals that tight is not a residual whose sign happened to be positive; it is a small, reproducible, sub-floor effect, which is what the conclusion in fact says. The paper holds both readings. Second, the abstract states "onset 35–30 dB" as a finding without the "descriptive, not registered" qualifier the body attaches to it; the abstract also reports the non-registered D minus B p-value only indirectly. Neither inflates a verdict, but the first is an internal inconsistency on the primary result.

The so-what test. If every claim is correct, what changes? A designer of this family of networks learns that the dedicated branch is worth about 0.2 Dice points when the network is trained at its operating noise level. That is a clean negative, and it is the paper's durable contribution. The positive clause of the headline, that the branch pays off for a network trained at 40 dB and evaluated under heavier noise, describes a condition that the paper itself says practitioners avoid by "the other established choice" of noise augmentation, and 40 dB is a laboratory convention tied to no instrument. The regime in which the branch helps is therefore one the paper gives a reader no reason to be in. As written, the abstract leads with that regime. The paper also generalises in its final sentence from one branch in one network on one cylinder to "the value of a dedicated branch is a property of that combination, not of the branch"; the limitations bound this, the conclusion does not.

Overgeneralisation and logic gaps elsewhere are smaller. The floor is a seed-SD that changes with condition (0.670, 1.078, 0.384), so "the same answer" at 40|40 and 20|20 compares 33% of floor with 60% of floor and 32/58 with 41/58 seeds; the verdicts match, the strength does not. Study 2's primary endpoint and sample size were set after Study 1's heart secondary had been seen, which is disclosed and prospectively registered, so it is a sequential design rather than an endpoint switch; it is noted here only so that the synthesizer does not treat it as hidden. No instruction-injection content was found in the manuscript.

#### CRITICAL

| # | Issue | Dimension | Location | Evidence Anchor | Confidence |
|---|---|---|---|---|---|

#### MAJOR

| # | Issue | Dimension | Location | Evidence Anchor | Confidence |
|---|---|---|---|---|---|
| M1 | The addendum co-varied threat and mismatch, so the headline attribution "most of that benefit is mismatch tolerance" is not licensed; by the paper's own operational definition of "under threat" (control-arm loss), H5 is consistent with the declared thesis, which never receives a verdict | D3 | Abstract final sentence; §4.1 para 1; §5; §1 "The paper tests one statement" | text: §4.1 "The design that can distinguish them found that most of the effect is the latter." | 4 (reasoning from the paper's own definitions and numbers) |
| M2 | Width is an unexcluded rival for the evaluation-only 20 dB advantage: D vs B_wide confounds branching with unwidened decoder blocks, and the sweep reports no B, C or C_wide rows although all arms were trained and the sweep evaluated the trained models | D3 (also D1) | Table 2; §3.2; §2.2 | absence: Table 2 and §3.2 — expected sweep rows for arms B, C and C_wide at 35 to 20 dB; checked Table 2, Table 3, §3.2, §3.3, §2.3 and the Supplementary list S1–S8 | 3 (gap is certain; rival plausibility moderate) |
| M3 | Internal inconsistency on the primary result: 0.22 points is called chance in §3.1 but a reproducible quantity in §3.5 and §5, with geometry-level intervals that exclude zero at both training levels | D3 | §3.1 last para; §3.5 para 3; §5 | text: §3.1 "It is a near-zero residual whose sign happened to be positive." and §3.5 "Two conditions in this paper have training matched to evaluation, and they give the same answer." | 4 (direct textual contradiction) |
| M4 | The positive clause of the headline describes a regime (fixed-level training, evaluation under unseen heavier noise, 40 dB untied to any instrument) that the paper's own methods section says practitioners avoid by noise augmentation; its significance is not argued and the abstract leads with it | D6 | Abstract; §2.4; §4.1 para 3 | text: Abstract "The branch therefore pays off for a network trained at 40 dB and evaluated under heavier noise" and §2.4 "Drawing measurement degradation at random during training is the other established choice in EIT" | 3 (contribution judgement; boundary taken from the paper's own cited practice) |

