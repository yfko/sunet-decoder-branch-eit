# academic-paper-reviewer · full · Round 1 · DRAFT_核心論文_v1.md

Date 2026-09-23 · contract `reviewer/reviewer_full/v2` · panel 5 · `criteria_binding_unavailable` (no #684 ReviewTargetContext; the TMI criteria in `refs/01_JOURNAL_REQUIREMENTS_TMI.md` are the Journal-Fit seat's own reading, not a bound target). READ-ONLY: no reviewer touched the manuscript.

## Review Panel Provenance (recorded, not inferred)

| Seat | Role ID | Actor type | Context ID | Peer outputs visible | Model family | Provider | Human reviewer ID |
|---|---|---|---|---|---|---|---|
| Journal-Fit | eic | model | same session | yes (sequential in one context) | Claude (Fable 5.1) | Anthropic | none |
| R1 | methodology | model | same session | yes | Claude (Fable 5.1) | Anthropic | none |
| R2 | domain | model | same session | yes | Claude (Fable 5.1) | Anthropic | none |
| R3 | perspective | model | same session | yes | Claude (Fable 5.1) | Anthropic | none |
| DA | da | model | same session | yes | Claude (Fable 5.1) | Anthropic | none |

| Axis | Status |
|---|---|
| Role-separated | true |
| Within-panel invocation-context separation | **false** |
| Blind to peer outputs | **false** |
| Model-family distinct | false |
| Provider distinct | false |
| Human-reviewer distinct | false |

Binary independence claim: not computed. Correlated-error disclosure: all five seats share one model family, one provider and one context; findings that recur across seats corroborate an angle, not an independent error process. The author of the draft is the same model; this panel is a structured self-audit, and the PI's own read and a real external review are the independent checks.

---

# Phase 0 — Field analysis and reviewer configuration

- Primary discipline: biomedical imaging (electrical impedance tomography). Secondary: deep learning for image segmentation; research-methodology (preregistration).
- Paradigm: quantitative, simulation-based controlled experiment with preregistered hypotheses. Maturity: full draft, pre-submission. Target: IEEE Transactions on Medical Imaging, Regular Paper.

| Seat | Configured identity | Focus |
|---|---|---|
| Journal-Fit (eic) | TMI associate editor for EIT/reconstruction; handles the journal's four Regular-Paper criteria and the "established method without methodological innovation" exclusion | Venue fit, contribution size relative to TMI's EIT record, writing/structure |
| R1 methodology | Statistician-engineer working on ML evaluation methodology: paired designs, seeds as replication units, preregistration, distribution shift | Design, decision rules, variance structure, inference scope |
| R2 domain | Thoracic EIT physiologist/engineer (ventilation and cardiac signal separation, GREIT, clinical ROI methods) | Domain accuracy, literature coverage, premise validity |
| R3 perspective | Multi-task learning researcher from the broader medical-image-analysis community | Cross-disciplinary relevance, practical implications, assumptions |
| DA | fixed | Strongest counter-argument, alternative explanations, over-generalisation |

Configuration presented to the PI with this file; adjustable for a re-run.

---

# Seat 1 — Journal-Fit Reviewer (eic)

## Phase 1 (paper-content-blind)

## Contract Paraphrase

D1 methodology_rigor: the design must answer the question, be replicable from the text, and state its limits. D2 domain_accuracy: facts and framing must be correct for the field and the relevant literature must be present. D3 argumentative_coherence: the argument must run from question to conclusion without gaps or contradictions. D4 cross_disciplinary_relevance: the work must connect to neighbouring fields where such connection changes what a reader would do. D5 writing_and_structure: the manuscript must be clear, correctly organised for the venue, and consistent in form. D6 venue_fit_and_contribution: the work must belong in this journal and add more than an increment to its record.

## Scoring Plan

### D5: writing_and_structure
dimension_id: D5
what_to_look_for: sections in the venue's expected order, abstract within limit, figures and tables cited, consistent terminology and citation form, prose that a specialist reads once.
what_triggers_block: manuscript is disorganised or unreadable, or violates a hard venue format rule that would cause return without review.
what_triggers_warn: readable but with structural or format issues that an editor would send back for correction before review.

### D6: venue_fit_and_contribution
dimension_id: D6
what_to_look_for: the manuscript's question and readership match the journal's scope statement, and the contribution is stated and defensible against the journal's own publication criteria.
what_triggers_block: the manuscript falls under a published exclusion of the journal or the contribution is not identifiable.
what_triggers_warn: the manuscript is within scope but its contribution is at risk under one of the journal's criteria and the framing does not yet defend it.
what_triggers_fatal: the manuscript's subject is outside the journal's scope statement altogether.

criteria_binding_unavailable

[CONTRACT-ACKNOWLEDGED]

## Phase 2 (paper-visible)

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
score: warn
trigger: "the contribution is at risk under one of the journal's criteria and the framing does not yet defend it"

## Review Body

Recommendation: Major Revision. Confidence 4 (core: editorial handling of EIT and imaging-methods manuscripts).

The manuscript is a controlled, preregistered evaluation of a decoder branch in a post-reconstruction network for lung EIT. It is well organised, within the abstract limit, cites every figure and table, and its terminology is disciplined. The registered negative result at 40 dB and the confirmed noise hypothesis are reported with a candour the journal rarely sees. My concern is fit, and it is the concern the authors themselves anticipate in their cover letter: TMI's EIT record is reconstruction with physical validation, and this is a simulation study of a segmentation-type stage. The manuscript's own framing, "a statement about how sensitive a post-reconstruction network is", is the right one for this journal, but it appears once in the Introduction and is not carried into the Discussion or Conclusion as the paper's contribution. Under criterion 4 (more than incremental) the paper currently reads as "we evaluated our own architecture and it helps only under heavy noise"; it needs to read as "we measured how a learned post-processing stage's benefit depends on what the reconstructor lets through, with a registered design that others can reuse". That is a framing revision, not new work.

### S1: Registered rules quoted and applied as registered
The decision rules of §2.4 are stated verbatim and the Results follow them in registered order, including the outcome the rules did not anticipate.
**Evidence Anchor**: text: §2.6 "No rule was invented afterwards to reconcile them."

### S2: Format compliance
Abstract single paragraph under 250 words, no equations in it; sections in the expected order; every figure and table cited.
**Evidence Anchor**: text: Abstract "the onset of that threat lies between 40 and 30 dB"

### W1: Contribution is framed as an architecture verdict rather than as a measurement-chain finding
**Problem**: The Introduction's strongest sentence for this journal, that the result is "a statement about how sensitive a post-reconstruction network is", is not the sentence the Discussion and Conclusion build on. §4.1 and §5 return to the branch. Under TMI criterion 4 and the "established method" exclusion, the branch is the weak part of the pitch and the measurement-chain dependence is the strong part.
**Evidence Anchor**: text: §1 "Because the branch sits downstream of the reconstruction, the answer is also a statement about how sensitive a post-reconstruction network is"
**Why it matters**: The paper's fit with this journal rests on which of the two it claims to be about.
**Suggestion**: Make the measurement-chain sensitivity the stated contribution in the Introduction's last paragraph, in §4.1's title and first paragraph, and in the Conclusion; keep the branch as the instance. State explicitly what the registered design offers a reader evaluating any post-reconstruction stage.
**Severity**: Major
**Confidence**: 4 — core expertise: venue fit

### W2: The absence of measured data is acknowledged but not defended against the journal's precedent
**Problem**: The cover letter defends the simulation-only design; the manuscript does not. Limitation 3 states the absence of measured data but does not say why the registered design could not have been run on measured data, nor what a reader should expect to transfer.
**Evidence Anchor**: text: §4.4 "Third, one phantom: a single cylinder with heterogeneous but simply parameterised organs, no thoracic geometry, and no measured data."
**Why it matters**: TMI's learned-EIT papers all carry physical validation; a reviewer will ask why this one does not.
**Suggestion**: One paragraph in §4.4 or §2.1 explaining that the registered controls (identical targets across arms, 290 runs, a noise sweep at fixed geometry) require a ground truth that measured EIT does not provide, and naming what measured data could test.
**Severity**: Minor
**Confidence**: 4 — core expertise: venue fit

---

# Seat 2 — Reviewer 1, Methodology (methodology)

## Phase 1 (paper-content-blind)

## Contract Paraphrase

D1 methodology_rigor: the design must be capable of answering the stated question, the analysis must match the design and the data, decision rules must precede data, every choice must be justified or declared, and the text must allow replication. D2 domain_accuracy: facts of the field must be right and the relevant prior work present. D3 argumentative_coherence: inferences must not exceed the design; alternative explanations the design cannot exclude must be named as such. D4 cross_disciplinary_relevance: connections to neighbouring methods where they change practice. D5 writing_and_structure: organisation and clarity fit for the venue. D6 venue_fit_and_contribution: belongs in the journal and adds more than an increment.

## Scoring Plan

### D1: methodology_rigor
dimension_id: D1
what_to_look_for: pre-specified hypotheses and rules, matched controls that isolate the manipulated variable, a replication unit whose variance matches the inference drawn, and reproducibility detail.
what_triggers_block: a design that cannot answer the question, an analysis that does not match the data structure, or rules altered after unblinding without disclosure.
what_triggers_warn: a sound design whose inferential scope is broader than its variance structure or training regime licenses, or a justified choice left unjustified.
what_triggers_fatal: evidence of undisclosed outcome switching or of results that cannot be reproduced from the described procedure.

### D3: argumentative_coherence
dimension_id: D3
what_to_look_for: each conclusion traceable to a registered or clearly labelled descriptive result; competing explanations that the design leaves open are named.
what_triggers_block: a conclusion that a registered result contradicts, or a headline claim resting on an unlabelled post-hoc analysis.
what_triggers_warn: a headline claim whose wording generalises beyond the conditions actually tested while the body is accurate.
what_triggers_fatal: the central claim is contradicted by the manuscript's own reported numbers.

criteria_binding_unavailable

[CONTRACT-ACKNOWLEDGED]

## Phase 2 (paper-visible)

contract_role: methodology
## Dimension Scores

### D1: methodology_rigor
score: warn
trigger: "a sound design whose inferential scope is broader than its variance structure or training regime licenses"

### D2: domain_accuracy
score: not_assessed

### D3: argumentative_coherence
score: warn
trigger: "a headline claim whose wording generalises beyond the conditions actually tested while the body is accurate"

### D4: cross_disciplinary_relevance
score: not_assessed

### D5: writing_and_structure
score: not_assessed

### D6: venue_fit_and_contribution
score: not_assessed

## Review Body

Recommendation: Major Revision. Confidence 5 (core: paired experimental design, preregistration, ML evaluation).

The design is the best-controlled comparison of a decoder branch I have seen in this literature: two hashed preregistrations, a capacity control within one percent, a position control, 58 paired seeds powered from a pilot that computed no contrast, and a scoring defect handled by re-scoring with the old path preserved and reproduced byte for byte. The registered rules are applied as written, including the uncomfortable 40 dB outcome. Two things limit what the design can support, and the manuscript's headline currently exceeds both.

### S1: Effect-size floor in the registered rule
Requiring the difference to exceed the control's seed SD, and reporting that this is the condition that fails by the widest margin, is exactly the discipline a p-value-only rule lacks.
**Evidence Anchor**: text: §3.1 "the floor is the condition it misses by the wider margin (0.223 against 0.670)"

### S2: Defect handling
The defect is classed correctly as a failure to compute the registered quantity, the fix is default, the old path is preserved and shown to reproduce prior output.
**Evidence Anchor**: text: §2.5 "This is a failure to compute the registered quantity, not a change of quantity."

### S3: Ceiling check
The relative-error-reduction analysis answers the most obvious alternative reading of the sweep and is labelled descriptive.
**Evidence Anchor**: table: Table 2, relative error reduction column with intervals

### W1: The sweep is evaluation-only under a 40 dB-trained model, and the inference is written as if it were about the branch under each noise level
**Problem**: Every model was trained at 40 dB and evaluated at 20 dB without retraining. The confirmed H3 is therefore a statement about how a 40 dB-trained branched network degrades under test-time noise it never saw, relative to a 40 dB-trained unbranched one. A network trained at 20 dB might show no branch advantage, or a larger one. The registered rule is exactly this evaluation-only contrast, so the registered result is sound; the title, abstract and §4.1 generalise it to "the branch pays off below the onset", which the design has not tested.
**Evidence Anchor**: text: §2.3 "The registered secondary sweep evaluated the trained models, without retraining, on test frames regenerated at 60, 50, 40, 30 and 20 dB"
**Why it matters**: Distribution shift tolerance and weak-component protection are different mechanisms with different practical consequences; a deployed network would be trained at its operating noise level.
**Suggestion**: Either (a) qualify the headline and §4.1 to "for a network trained at the registered level" and add this to Limitations, or (b) train D and B_wide at 20 dB (2 arms × 58 seeds ≈ 116 runs, about 39 h at the quoted 20 min/run) and report the trained-at-20 dB contrast as a registered addendum. Option (b) would also answer the DA's strongest counter-argument.
**Severity**: Major
**Confidence**: 5 — core expertise: ML evaluation under distribution shift

### W2: Seed-level intervals describe training-run variability, not phantom-population variability
**Problem**: Every seed is scored on the same 360 test geometries, so the seed-to-seed SD and every bootstrap interval reflect training stochasticity only. Variability across phantom geometries is averaged out before it reaches the interval. The intervals are correct for the question "would another training run reproduce this," and silent on "would another set of geometries."
**Evidence Anchor**: text: §2.4 "Seeds are the unit of replication, and every contrast is paired within seed."
**Why it matters**: The 40 dB interval excluding zero is interpreted in §3.1 and §4.2; readers will take it as an interval over phantoms.
**Suggestion**: State the scope of the intervals in §2.4, and add a frame-level (geometry) bootstrap of the 40 dB and 20 dB contrasts as a supplementary check; the per-image files exist.
**Severity**: Major
**Confidence**: 5 — core expertise: variance decomposition in paired designs

### W3: Wilcoxon p-values are reported without the test statistic or exact/asymptotic method
**Problem**: p = 0.098, 0.140, 0.041 and the sweep p-values are given without W, without stating exact versus normal approximation, and without the tie-handling rule.
**Evidence Anchor**: text: §3.1 "dz = 0.27, Wilcoxon p = 0.098"
**Why it matters**: Reproducibility of the registered decision.
**Suggestion**: Report W and the method (scipy default: exact for n ≤ 25 without ties, else normal approximation with continuity correction) once in §2.4.
**Severity**: Minor
**Confidence**: 5 — core expertise: nonparametric tests
**Arithmetic Receipt**: AR1

### W4: The floor rule is preregistered but its rationale is stated only in the Discussion
**Problem**: The "difference must exceed the control's seed SD" condition is unusual; §2.4 states it without the rationale that §4.2 gives.
**Evidence Anchor**: text: §4.2 "a condition written so that a difference too small to matter could not be declared a success on a p-value alone"
**Why it matters**: A reader of Methods should not have to reach the Discussion to understand the primary rule.
**Suggestion**: Move one sentence of rationale into §2.4.
**Severity**: Minor
**Confidence**: 4 — adjacent: preregistration practice

## Arithmetic Receipts

### AR1
procedure_id: p_from_test_statistic
evidence_anchor: text: §3.1 "dz = 0.27, Wilcoxon p = 0.098"
reported_inputs: test family Wilcoxon signed-rank; n = 58 paired seeds; p = 0.098; no test statistic W reported; tail not stated
assumptions: none licensed beyond the paired design; the manuscript does not state exact versus asymptotic computation
derivation: p from a Wilcoxon signed-rank test requires W (or the rank sums) and the method; neither is reported, so no recomputation is possible
derived_value_or_range: not derivable
comparison_rule: not applicable
status: not_computable
not_computable_reason: missing_reported_value
tail_convention: unstated

---

# Seat 3 — Reviewer 2, Domain (domain)

## Phase 1 (paper-content-blind)

## Contract Paraphrase

D1 methodology_rigor: design fit, rules before data, replicability. D2 domain_accuracy: the physics, the reconstruction facts, the terminology and the description of prior work must be right for thoracic EIT, and the literature that a domain reader expects must be present and correctly characterised. D3 argumentative_coherence: no gap between the domain premise and the conclusion drawn from it. D4 cross_disciplinary_relevance: connections outside the field. D5 writing_and_structure: clarity and organisation. D6 venue_fit_and_contribution: fit and increment for the journal.

## Scoring Plan

### D2: domain_accuracy
dimension_id: D2
what_to_look_for: correct statements about EIT reconstruction, noise, the cardiac signal, and the cited prior work; the standard approaches to the same problem in the field acknowledged and positioned.
what_triggers_block: a factual error about the modality or the reconstructor that a core claim depends on, or a mischaracterised cited work.
what_triggers_warn: the field's established approach to the same problem is absent from the framing, or a domain fact is stated without the qualification a specialist would require.
what_triggers_fatal: the premise the study rests on is false for the modality.

criteria_binding_unavailable

[CONTRACT-ACKNOWLEDGED]

## Phase 2 (paper-visible)

contract_role: domain
## Dimension Scores

### D1: methodology_rigor
score: not_assessed

### D2: domain_accuracy
score: warn
trigger: "the field's established approach to the same problem is absent from the framing"

### D3: argumentative_coherence
score: not_assessed

### D4: cross_disciplinary_relevance
score: not_assessed

### D5: writing_and_structure
score: not_assessed

### D6: venue_fit_and_contribution
score: not_assessed

## Review Body

Recommendation: Major Revision. Confidence 4 (core: thoracic EIT signal processing; adjacent: deep learning).

The domain facts are right. GREIT's regularisation and its suppression of measurement noise before image space are described correctly and, unusually, measured. The cardiac signal's small amplitude and position dependence are correctly attributed. The three prior works are characterised accurately, with quoted text, and the distinction from the encoder-side dual-branch reconstructor is correct and worth making. The separability measurement in Fig. 2 is a good way to state the premise. What is missing is the field's own answer to the problem the paper poses.

### S1: The premise is measured rather than asserted
Applying the clinical quarter-amplitude threshold to the mixed image and showing that it recovers the lung and not the heart is the right way to define "weak component" for this study.
**Evidence Anchor**: figure: Fig. 2 panels (b) and (c), printed DSC 0.948 and 0.000

### S2: The noise-to-image mapping is quantified
Stating that a tenfold noise change moves the GREIT input by a median 8.5% of peak, over the whole test split, is the number a domain reader wants and rarely gets.
**Evidence Anchor**: text: §2.3 "changed the reconstructed input by a median 8.5% of its peak (interquartile range 6.7 to 11.2%)"

### W1: Separation of cardiac from ventilatory signal in EIT is conventionally done in time, not in a single frame, and the manuscript does not say so
**Problem**: In thoracic EIT the cardiac-related component is routinely separated from ventilation by its frequency (band-pass or spectral filtering at the heart rate), by ECG gating, or by breath-hold acquisition; these are the established approaches and they operate on the time series, not on one reconstructed frame. The manuscript frames separation as a single-frame spatial problem and does not mention the temporal approaches, so a domain reader cannot tell why a learned single-frame separator is wanted, or how the simulated single-frame task relates to what is done with recordings.
**Evidence Anchor**: absence: §1 Introduction — expected positioning against frequency-domain and ECG-gated separation of the cardiac signal; checked §1, §4.3, §4.4, References
**Why it matters**: Without it, the paper's problem statement is incomplete for its own field, and the 2025 study's real-data result cannot be placed either.
**Suggestion**: One paragraph in §1 acknowledging temporal separation as the standard, stating what a frame-wise separator would add (e.g., no dependence on a stable heart-rate band, applicability to single frames), and citing the relevant methods. Citations must be verified through the authors' R12d pipeline; candidates the authors should check include the dynamic pulmonary/cardiac separation and ECG-gating literature in Physiological Measurement around 2008–2012. I name none as fact.
**Severity**: Major
**Confidence**: 4 — core expertise: EIT signal separation

### W2: "Instrument-realistic 40 dB" is registered but not sourced
**Problem**: The manuscript calls 40 dB instrument-realistic in five places and gives no instrument specification or reference. Reported voltage-domain SNR for research and clinical EIT systems varies widely with system, electrode and frequency, and several systems specify considerably higher figures; if that is so, the registered level is conservative and the onset sits even further from real instruments, which strengthens the negative result.
**Evidence Anchor**: text: §2.3 "The registered training and primary level was 40 dB."
**Why it matters**: The paper's practical reading (4.1) depends on where instruments sit relative to the onset.
**Suggestion**: Cite the system specification or published SNR measurements that motivated 40 dB (verified through R12d), and state the range.
**Severity**: Minor
**Confidence**: 3 — adjacent: instrument specifications vary and I have not checked current datasheets

### W3: The phantom's conductivity contrasts should be stated relative to tissue values
**Problem**: Lung 0.5, heart 2.0 and background 1.0 S/m are given as model values with no note on how they relate to tissue conductivities at the (unstated) excitation frequency.
**Evidence Anchor**: text: §2.3 "two lung inclusions at 0.5 S/m and one heart inclusion at 2.0 S/m"
**Why it matters**: A domain reader will ask whether the heart-to-lung contrast is realistic, because it sets the separability premise.
**Suggestion**: One sentence giving the intended ratio and its provenance (or stating that the phantom follows the companion noise-geometry study's configuration and is not tissue-calibrated).
**Severity**: Minor
**Confidence**: 4 — core expertise: tissue conductivity in EIT modelling

---

# Seat 4 — Reviewer 3, Perspective (perspective)

## Phase 1 (paper-content-blind)

## Contract Paraphrase

D1 methodology_rigor: design answers the question, replicable, limits stated. D2 domain_accuracy: correct for the field. D3 argumentative_coherence: no gaps or contradictions. D4 cross_disciplinary_relevance: the work should connect to what neighbouring communities already know about the same mechanism, and say what those communities can take from it, where doing so changes practice. D5 writing_and_structure: fit for the venue. D6 venue_fit_and_contribution: belongs and adds.

## Scoring Plan

### D4: cross_disciplinary_relevance
dimension_id: D4
what_to_look_for: the manuscript names the neighbouring literature on the same mechanism and states what its result means outside its own modality, within the scope it is willing to claim.
what_triggers_block: the manuscript makes cross-field claims it cannot support, or contradicts established results in the neighbouring field without engaging them.
what_triggers_warn: the mechanism under test has an established neighbouring literature that the manuscript neither engages nor explicitly scopes out.

criteria_binding_unavailable

[CONTRACT-ACKNOWLEDGED]

## Phase 2 (paper-visible)

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
trigger: "the mechanism under test has an established neighbouring literature that the manuscript neither engages nor explicitly scopes out"

### D5: writing_and_structure
score: not_assessed

### D6: venue_fit_and_contribution
score: not_assessed

## Review Body

Recommendation: Minor Revision. Confidence 3 (core: multi-task and multi-head architectures; adjacent: EIT).

The mechanism this paper isolates, a dedicated decoder for a task that the shared decoder under-serves, is the multi-task learning problem of task interference and its remedies (separate heads, soft or hard parameter sharing, loss weighting, gradient balancing). The paper's finding, that the dedicated branch matters only when the weak task is actually degraded, is a clean instance of a pattern that community would recognise, and the paper's own Limitation 2 (fixed 1:1 weights) is the same question that community asks first. The manuscript cites Caruana (1997) for the regularisation point and stops there. It is entitled to scope out cross-modality claims, and it does, but scoping out is not the same as not knowing the neighbours.

### S1: The practical lesson is stated for the right audience
Section 4.2's lesson is addressed to people comparing architectures rather than to clinicians, which is the honest audience for a simulation study.
**Evidence Anchor**: text: §4.2 "The practical lesson is for anyone comparing architectures rather than for anyone treating patients."

### W1: The multi-task learning framing of the mechanism is not engaged
**Problem**: The branch-versus-shared-decoder question is a hard-parameter-sharing question, and the "under threat" condition is a statement about when task interference becomes costly. The manuscript does not connect to that literature or state that it deliberately does not, so a reader from medical image analysis cannot tell whether the onset is a known phenomenon in new clothes or a new observation.
**Evidence Anchor**: text: §1 "A second decoder adds parameters, and a second supervised target is a well-known regulariser in its own right"
**Why it matters**: It affects how the contribution is read by the broader community the venue serves.
**Suggestion**: Two or three sentences in §1 or §4.3 placing the result in the task-interference / loss-weighting literature, with the explicit statement that weighting is left to the companion study; citations through R12d (candidates include the uncertainty-weighting and gradient-normalisation lines; verify).
**Severity**: Major
**Confidence**: 3 — core expertise: multi-task learning; adjacent to the modality

### W2: The reader is not told what to do with the onset
**Problem**: The Conclusion says an architectural comparison without its measurement-chain context is not a comparison, which is right, but it does not say what a practitioner should measure before choosing the branch: the image-domain perturbation their reconstructor produces at their instrument's SNR.
**Evidence Anchor**: text: §5 "An architectural comparison without its measurement-chain context is not a comparison"
**Why it matters**: The paper's most transferable point is left implicit.
**Suggestion**: One sentence in §4.1 or §5 stating the operational recipe: measure the reconstructor's image-domain perturbation at the operating SNR (as in §2.3), and compare it with the 8.5% median at which this study's onset had been passed.
**Severity**: Minor
**Confidence**: 4 — core expertise: translating evaluation results to practice

---

# Seat 5 — Devil's Advocate (da)

## Phase 1 (paper-content-blind)

## Contract Paraphrase

D1 methodology_rigor: from the adversary's side, the design must leave no alternative route to the same numbers that the authors have not closed. D2 domain_accuracy: no premise the field would reject. D3 argumentative_coherence: the chain from registered result to headline must survive the strongest reading against it; every generalisation must be earned by a tested condition, and every post-hoc analysis must be unable to carry weight it is not labelled for. D4 cross_disciplinary_relevance: no borrowed authority from neighbouring fields. D5 writing_and_structure: no rhetorical structure that hides a gap. D6 venue_fit_and_contribution: the contribution must survive the question "so what."

## Scoring Plan

### D3: argumentative_coherence
dimension_id: D3
what_to_look_for: the headline claim is stated at the same scope as the registered result; competing explanations that the design leaves open are named in the manuscript, not left for the reader.
what_triggers_block: a competing explanation that the design cannot exclude would, if true, reverse the headline, and the manuscript does not name it.
what_triggers_warn: a competing explanation the design leaves open would narrow the headline's scope, and the manuscript names it only partially or only in Limitations.
what_triggers_fatal: the headline is contradicted by the manuscript's own registered result.

criteria_binding_unavailable

[CONTRACT-ACKNOWLEDGED]

## Phase 2 (paper-visible)

contract_role: da
## Dimension Scores

### D1: methodology_rigor
score: not_assessed

### D2: domain_accuracy
score: not_assessed

### D3: argumentative_coherence
score: warn
trigger: "a competing explanation the design leaves open would narrow the headline's scope, and the manuscript names it only partially or only in Limitations"

### D4: cross_disciplinary_relevance
score: not_assessed

### D5: writing_and_structure
score: not_assessed

### D6: venue_fit_and_contribution
score: not_assessed

## Review Body

Strongest counter-argument. The paper says the branch pays off when the cardiac component is under threat. Here is the reading it has not excluded: the branch pays off when the input is out of distribution. Every network was trained at 40 dB. At 20 dB every network sees inputs it never saw, and the single-decoder networks, which must serve both outputs from one feature stream, may simply be worse at tolerating an unfamiliar input than a network with two streams, for reasons that have nothing to do with which component is weak. The paper's best evidence against this is channel specificity: the lung gains nothing at 20 dB. But the lung is also less perturbed (2.0 points of Dice lost against 8.8), so "the lung was not under threat" and "the lung was less out of distribution" are the same observation. The design cannot tell them apart, because noise level and distribution shift are confounded by construction in an evaluation-only sweep. The manuscript's own Limitation 1 comes close, and §2.3 states the sweep was evaluation-only, but nowhere does the paper say that the mechanism it names and the mechanism it has not excluded make the same prediction in this design. The registered H3 is untouched by this argument. The title is not.

Second challenge: the onset is located "between 40 and 30 dB" because those are adjacent grid points. The sweep's resolution is 10 dB, so the headline's precision is the grid's precision, and the paper presents it as a finding about where the onset is. An evaluation-only pass at 35 dB and 25 dB costs nothing but scoring time and would turn a grid artefact into a measurement.

Third, a cherry-picking check that comes out in the paper's favour: the relative-error-reduction analysis was introduced after the flat top was seen. It is labelled descriptive, it is applied to both channels and all levels, and it makes the 40 dB result look worse, not better. That is not cherry-picking. The seed-correlation analysis likewise cuts against the authors' registered-endpoint interval. The paper's post-hoc analyses are disclosed and they are not self-serving.

Fourth, the "so what" test. If everything in the paper is right, a practitioner learns that for one architecture on one cylinder with one reconstructor the branch does nothing at 40 dB. The paper's answer to "so what" is the measurement-chain point in §4.1 and §5, and it is a good answer, but it is asserted from one reconstructor. The paper is honest that it measured no other. The "so what" therefore rests on a plausibility argument the paper labels as such. That is acceptable, and it is why the paper's contribution is the design and the registered negative rather than the onset.

#### CRITICAL

| # | Issue | Dimension | Location | Evidence Anchor | Confidence |
|---|---|---|---|---|---|

#### MAJOR

| # | Issue | Dimension | Location | Evidence Anchor | Confidence |
|---|---|---|---|---|---|
| M1 | Distribution shift and "under threat" make the same prediction in an evaluation-only sweep, and the headline generalises to the mechanism the design cannot isolate | D3 | Title, Abstract, §4.1 | text: §2.3 "The registered training and primary level was 40 dB." | 5 — core: experimental confounds |
| M2 | Onset location is stated at grid resolution and presented as a measured location | D3 | Abstract, §3.2, §5 | text: §3.2 "Between 40 and 30 dB the advantage rises by 0.40 points, and at 20 dB it reaches 2.1 points" | 5 — core: measurement resolution |

---

# Phase 2 — Editorial synthesis (mechanical, reviewer_full v2)

## Step 1 — Role-scoped scoring matrix

| Dimension | Eligible seats | Assessed scores | Verdict (worst) |
|---|---|---|---|
| D1 methodology_rigor (mandatory) | methodology | warn | warn |
| D2 domain_accuracy (mandatory) | domain | warn | warn |
| D3 argumentative_coherence (mandatory) | da, methodology | warn, warn | warn |
| D4 cross_disciplinary_relevance (high) | perspective | warn | warn |
| D5 writing_and_structure (normal) | eic | pass | pass |
| D6 venue_fit_and_contribution (mandatory) | eic | warn | warn |

No fatal block declared by any seat. No dissent filed by any seat.

## Step 2 — Failure conditions

- F1 (any mandatory fatal block): did not fire.
- F2 (any mandatory block): did not fire.
- F3 (two or more mandatory dimensions warn or worse): **fired** (D1, D2, D3, D6).
- F4 (any high-priority block): did not fire.
- F5 (any dimension warn or worse): fired (D1, D2, D3, D4, D6).
- F0 (every dimension pass): did not fire.

## Step 3 — Precedence and decision

dimension_verdicts: [D1=warn, D2=warn, D3=warn, D4=warn, D5=pass, D6=warn]
fired_conditions: [F3, F5]
da_critical_adjudications: []
editorial_decision=major_revision

---

# Editorial Decision Letter

## Decision: Major Revision

The panel finds a preregistered, well-controlled and candidly reported study whose headline outruns its design in one specific way, whose problem statement omits the field's standard approach to the same problem, and whose contribution is framed for the wrong audience for the target journal. None of these requires new science to fix; one of them (R1) is best fixed with a modest additional experiment that the existing pipeline can run.

## Blocking Issues (immutable source order)

| Ref | Blocking issue | Source | Evidence anchor | Resolving item |
|---|---|---|---|---|
| R1 | Evaluation-only sweep under 40 dB-trained models; distribution shift and "under threat" not separable; headline generalises beyond the tested condition | R1-W1, DA-M1 | text: §2.3 "The registered secondary sweep evaluated the trained models, without retraining, on test frames regenerated at 60, 50, 40, 30 and 20 dB" | REV-1 |
| R2 | Temporal (frequency/ECG-gated) separation of the cardiac signal, the field's standard, is absent from the framing | R2-W1 | absence: §1 Introduction — expected positioning against frequency-domain and ECG-gated separation of the cardiac signal; checked §1, §4.3, §4.4, References | REV-2 |
| R3 | Contribution framed as an architecture verdict rather than as measurement-chain sensitivity, which is the paper's TMI-relevant claim | EIC-W1 | text: §1 "Because the branch sits downstream of the reconstruction, the answer is also a statement about how sensitive a post-reconstruction network is" | REV-3 |

## Reviewer summary

| Seat | Recommendation | Confidence |
|---|---|---|
| Journal-Fit | Major Revision | 4 |
| R1 Methodology | Major Revision | 5 |
| R2 Domain | Major Revision | 4 |
| R3 Perspective | Minor Revision | 3 |
| DA | findings only (0 Critical, 2 Major) | per finding |

## Consensus analysis

Sub-claims (decomposed from weaknesses):
- SC-1 The evaluation-only sweep leaves distribution shift and weak-component threat confounded, and the headline generalises past it. Raised R1-W1; corroborated DA-M1. Silent: EIC, R2, R3. **CONSENSUS-2 (R1, DA)**; no dispute.
- SC-2 Temporal separation literature absent. Raised R2-W1. Others silent. Single-seat finding, undisputed.
- SC-3 Contribution framing should be measurement-chain sensitivity. Raised EIC-W1; R3-W2 corroborates from the practice side (the operational recipe is left implicit). **CONSENSUS-2 (EIC, R3)**.
- SC-4 Intervals describe training-run variability only. Raised R1-W2. Undisputed.
- SC-5 Onset stated at grid resolution. Raised DA-M2. Undisputed; R1's suggestion (b) and DA's suggestion (35/25 dB evaluation pass) are compatible.
- SC-6 Multi-task learning literature not engaged. Raised R3-W1. Undisputed.
- SC-7 Minor items: Wilcoxon statistic/method (R1-W3), floor rationale placement (R1-W4), 40 dB provenance (R2-W2), conductivity contrast provenance (R2-W3), simulation-only defence in text (EIC-W2), operational recipe (R3-W2).

No SPLIT: no seat disputed another's finding. DA CRITICAL: none raised; nothing to adjudicate.

## Decision rationale

Four mandatory dimensions carry a warn from their owning seats, which fires F3 and yields Major Revision mechanically; the panel's qualitative reading agrees with the mechanical outcome. The decisive item is SC-1. The registered H3 is a statement about evaluation-time noise under 40 dB-trained models, and the paper's body says so, but its title, abstract and 4.1 state the mechanism as if the branch had been shown to help *when trained and deployed* under threat. The DA's counter-argument (distribution-shift tolerance) makes the same prediction as the paper's mechanism in this design, and the paper does not say so. That is repairable either by narrowing the claim or by one additional trained-at-20 dB contrast; the panel prefers the latter because it also answers SC-5 cheaply if paired with 35/25 dB evaluation passes. SC-2 is a framing omission a domain reader will notice immediately and is fixed with one paragraph and verified citations. SC-3 is a framing change that determines whether the paper survives TMI's criterion 4; it costs no new work. A Minor Revision would understate SC-1, and Reject would ignore that every item is repairable within the existing design and pipeline.

## Required revisions (must_fix)

| Ref | Item | Sub-claim | Severity | Anchor | Source | Cost scope | Bounded consequence |
|---|---|---|---|---|---|---|---|
| R1 | Separate distribution-shift from weak-component threat: retrain D and B_wide at 20 dB (≈116 runs) and report as a registered addendum, or narrow title/abstract/§4.1 to "for a network trained at the registered level" and add the confound to Limitations | SC-1 | Major | see Blocking R1 | R1, DA | new-data (≈39 h) or section rewrite (Title, Abstract, §4.1, §4.4) | headline scope matches design |
| R2 | Add one paragraph in §1 positioning frame-wise separation against temporal (frequency/ECG-gated) separation, with R12d-verified citations | SC-2 | Major | see Blocking R2 | R2 | section (§1) + 2–4 new references via cite.py | problem statement complete for the field |
| R3 | Reframe the stated contribution as measurement-chain sensitivity of a post-reconstruction stage in §1 last paragraph, §4.1 title/first paragraph, §5 | SC-3 | Major | see Blocking R3 | EIC, R3 | section rewrite (§1, §4.1, §5) | TMI criterion 4 defensible |
| R4 | State in §2.4 that seed-level intervals describe training-run variability; add a geometry-level bootstrap of the 40 and 20 dB contrasts to Supplementary | SC-4 | Major | text: §2.4 "Seeds are the unit of replication, and every contrast is paired within seed." | R1 | re-analysis (per-image files exist) + sentence | interval scope stated |
| R5 | Add evaluation-only passes at 35 and 25 dB (regenerate test frames; no retraining) and report the onset at 5 dB resolution, still labelled descriptive | SC-5 | Major | text: §3.2 "Between 40 and 30 dB the advantage rises by 0.40 points, and at 20 dB it reaches 2.1 points" | DA | re-analysis (2 sweep levels × 2 arms, scoring only) | onset location is a measurement, not a grid artefact |
| R6 | Two or three sentences placing the branch/shared-decoder question in the multi-task task-interference and loss-weighting literature, scoping weighting to the companion study; R12d-verified citations | SC-6 | Major | text: §1 "A second decoder adds parameters, and a second supervised target is a well-known regulariser in its own right" | R3 | section (§1 or §4.3) + 1–3 references | mechanism positioned for the broader readership |

## Suggested revisions (should_fix / consider)

| Ref | Item | Sub-claim | Severity | Source | Obligation |
|---|---|---|---|---|---|
| S1 | Report Wilcoxon W and computation method (exact vs asymptotic, ties) in §2.4 | SC-7 | Minor | R1-W3 | should_fix |
| S2 | Move one sentence of floor rationale from §4.2 into §2.4 | SC-7 | Minor | R1-W4 | should_fix |
| S3 | Source the 40 dB instrument-realistic level (specification or published SNR), state the range | SC-7 | Minor | R2-W2 | should_fix |
| S4 | State the provenance of the phantom conductivity contrasts | SC-7 | Minor | R2-W3 | should_fix |
| S5 | Defend the simulation-only design in the manuscript (why registered controls need simulated ground truth) | SC-7 | Minor | EIC-W2 | should_fix |
| S6 | State the operational recipe: measure the reconstructor's image-domain perturbation at the operating SNR and compare with the 8.5% median | SC-7 | Minor | R3-W2 | consider |

## Revision Roadmap (immutable source order; ordinals are transport refs, not work order)

REV-1 ↔ R1 · REV-2 ↔ R2 · REV-3 ↔ R3 · REV-4 ↔ R4 · REV-5 ↔ R5 · REV-6 ↔ R6 · REV-7..12 ↔ S1..S6.

Author triage (`will_address` / `wont_address` / `not_on_point`) is the PI's, recorded in a separate sidecar before `academic-paper` revision mode is run; this letter does not infer it.

## Notes for the PI (outside the letter)

- R1's two options differ in cost. Narrowing the claim is a wording change; the 20 dB retraining is ≈116 runs (≈39 h on the mini) and would need its own preregistration addendum before running, per the lab's rule. If the retraining is done, the 40 dB-trained and 20 dB-trained contrasts are two different registered quantities and must be reported as such.
- R2 and R6 add citations. Every one goes through `tools/cite.py`; the reviewers named candidate literatures, not verified references.
- R5 is cheap (two extra `gen_snr_sweep.m` levels, scoring only) and directly improves the headline.
- Boundary-clause check: no finding asks the paper to cross any of the seven not-claims. R2 and R6 add positioning, not claims. R1's retraining option stays inside "GREIT, 1:1, single cylinder".
