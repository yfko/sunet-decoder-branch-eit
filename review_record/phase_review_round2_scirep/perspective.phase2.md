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
trigger: "the practical implication is stated at a scope slightly wider or narrower than the evidence"
rationale: The multi-task framing is correct and every claim about the adjacent field is tied to a citation the adjacent field would recognise, and the practical lesson is scoped to method comparers rather than clinicians. Two things stop this being a pass for a broad-readership venue. The effect unit used from the abstract onward ("Dice points", meaning hundredths of Dice) is never defined, so an adjacent reader meets "0.223 Dice points ... below the 0.670 floor" in the abstract with no way to size the effect. And the closing sentence of the Conclusion generalises from one phantom, one reconstructor and one pair of targets to "a dedicated branch" and "an architectural comparison" in general. Neither inverts the takeaway; both would mislead an adjacent reader who stops at the abstract and the last paragraph. Each weakness below is Minor on its own.

### D5: writing_and_structure
score: not_assessed

### D6: venue_fit_and_contribution
score: not_assessed

## Review Body

I review this from multi-task learning and medical-image-analysis validation, not from EIT. I may miss conventions of the EIT literature; what I can judge is whether a reader from my side of the fence can follow the design, whether the concepts the paper borrows from my side are used the way we use them, and what that reader will carry away.

Seat recommendation, advisory only and not an editorial decision: Minor Revision, confidence 4 of 5. Calibration status NOT_CALIBRATED.

**What an adjacent reader takes away.** The design is legible: one shared encoder, decoder split at the bottleneck versus a widened single decoder at matched parameter count and matched supervision, loss weights fixed at 1:1, a preregistered primary level, an evaluation-only SNR sweep, and a registered retraining at the harshest level. The result an MTL reader will recognise is clean: a task-specific decoder for the minority target buys no accuracy at matched train/test condition (0.2 hundredths of Dice at both 40 and 20 dB, under a floor set at the seed-to-seed scatter), and buys about 2 hundredths of Dice when the network is evaluated on noise it was not trained on. In robustness-benchmark vocabulary that is "D is more shift-tolerant than its capacity-matched control, but not more accurate in-distribution", which is a perfectly respectable architectural statement and the one I would have liked the paper to say in those words (W5).

**Assumption audit.** The explicit assumption, that a dedicated decoder protects a weak component when it is under threat, is stated and tested. The implicit assumption I would flag is that "task interference" in the MTL sense is the mechanism, when every arm shares the encoder and arm B shares everything up to a 1×1 head; what the branch frees is decoder-level sharing only, and the paper does not say so (W2). A second implicit assumption is that the two targets behave like two tasks. Under a linear reconstructor the heart-only and lung-only reconstructions are close to a decomposition of the mixed input, which in MTL terms makes them maximally related tasks, the case where decoder separation is expected to matter least; the matched-training null is what my field would predict, and saying so would turn a bare null into an explained one (W3). The paradigmatic assumption, that a simulation with a settable noise level is the right instrument for this question, is defended explicitly and I accept the defence.

**Cross-disciplinary connections.** The paper already reaches across well: unitary scalarization, branched MTL under a fixed budget, the nnU-Net-Revisited baseline critique, corruption benchmarks, acquisition shift, FFDNet-style noise-level dependence. These are the right references and they are used in the sense their authors intended. Two further leads, which I cannot ground in session materials and therefore mark as search leads: [UNVERIFIED] the task-grouping literature (Standley et al., ICML 2020, "Which tasks should be learned together"; Fifty et al., NeurIPS 2021) gives a vocabulary for W3, because it predicts when separating decoders helps from the affinity of the tasks. [UNVERIFIED] Metrics Reloaded (Maier-Hein et al., Nature Methods 2024) speaks directly to Section 2.5: scoring a regression output by a post-hoc threshold mask is exactly the metric-selection pitfall that framework catalogues, and citing it would make the defect disclosure read as methodology rather than confession.

**Practical impact and stakeholders.** The paper is careful that nobody treating patients should act on it, and gives a method comparer a usable recipe (measure the image-domain perturbation the reconstructor passes, compare with 8.5% of peak, ask whether the deployed network was trained at that level). From my side the actionable implication is for anyone building two-decoder networks in medical imaging: if you can train at the operating condition, do that before adding a branch. The paper never quite says this at the scope it has earned, saying instead something wider (W4). The missing experimental cell that my field would run first, training on a mixture of noise levels, is named as "the other established choice" and left untested; that is an acceptable scope decision but it deserves one sentence in the limitations, because for a robustness reader it is the obvious third condition between evaluation-only and retrain-at-level.

**Broader implications.** No ethical concern: simulated data, no patients, code and preregistrations public. The paper's most transferable contribution to my field is procedural, not architectural: the sequence match capacity, register a floor, sweep the shift, then retrain at the shifted level, is a template other multi-decoder comparisons could copy, and the honest account of what the addendum changed is rarer than it should be.

### Strengths

#### S1: The multi-task framing is correct and the weighting-versus-branching distinction is the right one
Evidence Anchor: text: §1 "Weighting and branching are therefore two answers to one problem"
An MTL reader will recognise loss weighting and branching as two remedies for the same gradient-competition problem, and the decision to fix weights at 1:1 is defended with the two NeurIPS 2022 unitary-scalarization results rather than asserted.

#### S2: Capacity matching is explained with its own limit stated
Evidence Anchor: text: §2.2 "Matched parameter count is not matched architecture."
This is the nnU-Net-Revisited point applied correctly, and the paper pre-empts the obvious objection that a widened decoder and a second decoder differ in shape as well as count.

#### S3: The train/evaluation mismatch is named in the adjacent field's vocabulary
Evidence Anchor: text: §4.1 "the evaluation-only sweep is an acquisition shift between the data the network was developed on and the condition it was tested in"
Calling the sweep an acquisition shift, and tying the training-level dependence to FFDNet and to Gaussian-noise augmentation, places the result where a medical-imaging reader will find it.

#### S4: Terminology is disambiguated for outsiders
Evidence Anchor: text: §1 "The term *dual-branch* also carries a different meaning in the EIT reconstruction literature."
Segmentation, separation, weak and dominant component are defined on first use, and the encoder-side versus decoder-side branch distinction is drawn explicitly, which spares an adjacent reader a wrong analogy.

#### S5: The practical lesson is scoped to the right audience
Evidence Anchor: text: §4.2 "The practical lesson is for anyone comparing architectures rather than for anyone treating patients."
The paper says who should act on it and who should not, and gives the method comparer a concrete recipe.

#### S6: The regulariser reading of the second decoder is acknowledged
Evidence Anchor: text: §4.4 "a second decoder may act as a regulariser of the shared encoder rather than as a specialist for its target"
This is the alternative an MTL reviewer would raise first, and the paper raises it itself with the right precedent.

#### S7: The scoring-defect disclosure is a validation lesson the adjacent field needs
Evidence Anchor: text: §2.5 "This is a failure to compute the registered quantity, not a change of quantity."
Dice on a thresholded regression output failing silently under an affine shift, caught only by plotting, is exactly the class of metric failure medical-image-analysis validation guidance warns about.

### Weaknesses

### W1: The effect unit "Dice points" is never defined
**Severity**: Minor
**Evidence Anchor**: text: Abstract "led its capacity-matched control by 0.223 Dice points (95% CI 0.020–0.441), below the 0.670 floor"
**Confidence**: 5 — a reader from medical image analysis expects Dice on [0, 1] or in percent, and the unit is used from the abstract onward without definition.
Every effect in the abstract, the text and the tables is in hundredths of Dice, which the reader must infer from Table 1 (0.9679 minus 0.9657 equals 0.223 "points"). An adjacent reader who stops at the abstract cannot size the effect and cannot tell whether a 0.670 floor is absurd or tiny. One clause at first use ("in Dice points, that is, hundredths of Dice") in the abstract and in Section 2.4 resolves it.

### W2: The locus of the hypothesised interference is not stated, although every arm shares the encoder
**Severity**: Minor
**Evidence Anchor**: text: §1 "its known failure mode is task interference, in which the gradients of one task degrade the shared features that another task needs"
**Confidence**: 4 — this is the first question an MTL reader asks of a shared-encoder design.
The paper motivates the branch by task interference in shared features, but the encoder is shared in all five arms, so the contrast D minus B_wide tests decoder-level sharing only. Encoder-level interference, where the MTL literature usually locates the problem, is untested by construction. A sentence in Section 2.2 saying that the design isolates decoder sharing and leaves encoder sharing fixed would prevent an adjacent reader from reading the null as evidence against interference in general.

### W3: The two targets are near-complementary decompositions of one input, which my field would read as maximally related tasks
**Severity**: Minor
**Evidence Anchor**: text: §2.3 "the network's input is the mixed reconstruction and its two targets are the single-organ reconstructions"
**Confidence**: 3 — the argument depends on how far GREIT's linearity carries at these contrasts, which I cannot judge from outside EIT.
If the lung-only and heart-only reconstructions approximately sum to the mixed reconstruction, then one target is nearly determined by the input and the other, and the task-grouping literature would predict little benefit from separate decoders. That both explains the matched-training null and bounds its transfer: the result need not hold for two-decoder networks whose targets are not decompositions of a common input (segmentation plus classification, for instance). Stating this would make the null an expected one and would make the scope limit precise for the adjacent reader.

### W4: The closing sentence generalises beyond the tested cell
**Severity**: Minor
**Evidence Anchor**: text: §5 "the value of a dedicated branch is a property of that combination, not of the branch"
**Confidence**: 4 — the sentence reads as a general principle about branches and about architectural comparison, whereas the evidence is one phantom, one reconstructor, one noise model and one pair of targets.
Section 4.4 fences the claim correctly ("tested one cell of that grid"), and the first sentence of the Conclusion is correctly scoped to GREIT-reconstructed simulated lung EIT. The last sentence drops the fence. Rewording it as a recommendation ("an architectural comparison should report its measurement-chain and training-condition context") rather than a finding would keep the moral and lose the overreach.

### W5: The shift-tolerance result is undersold to the robustness reader
**Severity**: Minor
**Evidence Anchor**: text: §4.1 "That sentence is about this measurement chain, not about the branch."
**Confidence**: 3 — a framing preference from the corruption-benchmark literature, not a dispute about the numbers.
The paper treats the evaluation-only advantage as belonging to the training condition rather than to the branch. The absolute recovery under retraining (8.0 of 8.8 points) does belong to the training condition, but the relative advantage of D over its capacity-matched control under unseen noise (2.1 points, dz above one) is a property of the architecture, and it is the kind of result the robustness benchmarks the paper cites exist to report. Stating both halves in one sentence, "the branch buys shift tolerance at matched capacity but not in-distribution accuracy", would give the adjacent reader the correct takeaway and avoid the reading that the branch does nothing.

### Questions for Authors
1. In MTL terms, which shared parameters does the bottleneck split free, and would a split at the encoder (fully separate streams, capacity-matched) be the natural next arm?
2. How close to additive are the lung-only and heart-only GREIT reconstructions relative to the mixed one on this phantom? If near-additive, does that change how you would frame the two outputs as "tasks"?
3. Would training on a mixture of SNR levels, the third condition between evaluation-only and retrain-at-level, be expected to shrink the branch advantage as far as retraining did?

### Minor Issues
- "Dice points" and "pts" are used interchangeably; define once and use one form.
- The practitioner's recipe in Section 4.1 would be easier to find under its own short heading or in the Conclusion.
