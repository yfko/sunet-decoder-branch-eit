# academic-paper-reviewer · full · Round 2 (Sci Rep) · 32_SUBMISSION_scirep.md

Date 2026-10-06 · contract `reviewer/reviewer_full/v2` · panel 5 · `criteria_binding_unavailable` (no #684 ReviewTargetContext; the Sci Rep criteria in `refs/01_JOURNAL_REQUIREMENTS_SCIREP.md` are the Journal-Fit seat's own reading). READ-ONLY: no reviewer touched the manuscript. Dispatch: five separate subagent contexts (Fable 5.1), each writing Phase 1 before opening the manuscript; every card passed `check_phase_conformance.py`; the synthesis passed `check_panel_synthesis.py`. Working files: `phase_review_round2_scirep/`.

## Review Panel Provenance (#540/#740, built and replay-validated by `review_panel_provenance.py`)

- **Typed artifact**: `phase_review_round2_scirep/provenance_artifact.json` · **Artifact SHA-256**: dc8fea76b4f22f52fe6d37bd33f84f285081de4201e23ef68a1962d6df04f3ed
- **Panel ID**: sunet-core-round2-scirep-20261006 · **Normalized manifest SHA-256**: e31b4ae4039d9ea3be36f6a89a5affc829a131d6430e490063fbccb2cbc9db6a · **Execution topology SHA-256**: 5f6b97561e1c1c6cfd9621d5a99af9285aa22e1caba6452d974528f4612285b0
- **Fresh-context scope**: `within_panel_attempt_only`

| Seat | Role ID | Actor type | Context ID | Peer outputs visible | Model family | Provider | Human reviewer ID |
|---|---|---|---|---|---|---|---|
| EIC | eic | model | subagent-eic-20261006 | false | claude-fable-5-1 | anthropic | none |
| R1 | methodology | model | subagent-methodology-20261006 | false | claude-fable-5-1 | anthropic | none |
| R2 | domain | model | subagent-domain-20261006 | false | claude-fable-5-1 | anthropic | none |
| R3 | perspective | model | subagent-perspective-20261006 | false | claude-fable-5-1 | anthropic | none |
| DA | da | model | subagent-da-20261006 | false | claude-fable-5-1 | anthropic | none |

| Provenance axis | Status |
|---|---|
| Role-separated | True |
| Within-panel invocation-context separation | True |
| Blind to peer outputs | True |
| Model-family distinct | False |
| Provider distinct | False |
| Human-reviewer distinct | False |

- **Binary independence claim**: Not computed. Persona or role diversity proves only `role_separated`.
- **Correlated-error disclosure**: All model-executed review seats used one model family; role separation does not remove correlated-error risk.

---

# Phase 0 — Field analysis and reviewer configuration

- Primary discipline: biomedical imaging (electrical impedance tomography). Secondary: deep learning for image separation; research methodology (preregistration). Paradigm: quantitative, simulation-based controlled experiment with preregistered hypotheses and a registered addendum. Maturity: revised full draft after two prior panel rounds and one desk reject. Target: Scientific Reports (technical soundness and scientific validity, not significance).

| Seat | Configured identity | Eligible dimensions |
|---|---|---|
| Journal-Fit (eic) | Scientific Reports Editorial Board Member, biomedical engineering / medical imaging; applies the technical-soundness criterion and the transcribed submission guidelines | D5, D6 |
| R1 methodology | Statistician-engineer in ML evaluation methodology: paired designs, seeds as replication unit, preregistered rules with floors, bootstrap scopes, Wilcoxon reporting, evaluation-only sweeps vs retraining | D1, D3 |
| R2 domain | Thoracic EIT physiologist/engineer: cardiac-signal separation, GREIT/EIDORS, instrument SNR and electrode artefacts, post-reconstruction deep learning; checks the 34 new citation sentences | D2 |
| R3 perspective | Multi-task learning / medical image analysis researcher outside EIT: branching, weighting, capacity-matched baselines, robustness benchmarks; accessibility for a broad readership | D4 |
| DA | fixed | D3 (co-owned) |

Configuration presented to the PI with this file; adjustable for a re-run.

---

# Seat 1 — Journal-Fit Reviewer (eic)

## Phase 1 (paper-content-blind)

## Contract Paraphrase

D1 (methodology_rigor, mandatory) asks whether the study was designed, run, analysed and reported to the standard a careful peer reviewer in this field would demand, and whether a reader could in principle reproduce it. From the editorial chair this is the dimension that decides whether the paper is safe to publish at all; it is owned by the methodology seat and I do not score it, but a methodology failure would override anything I say about fit or presentation.

D2 (domain_accuracy, mandatory) asks whether the manuscript's statements about the field, its prior work and its terminology are correct and fairly represented. This is the domain seat's dimension. For my purposes it matters as a background check on whether the contribution the paper claims is actually the contribution it makes relative to what the field already knows.

D3 (argumentative_coherence, mandatory) asks whether the central thesis hangs together: the evidence offered must support the claims drawn, and no logical slip may sit under the main argument. The devil's advocate owns it and the methodology seat may contribute. I do not score it, though over-promising in a title or abstract relative to what the body delivers is a structural symptom I may see from my own vantage point and will record under D5 rather than D3.

D4 (cross_disciplinary_relevance, high priority) asks whether a reader from a neighbouring field could follow the framing and definitions, and whether any claim that reaches across disciplines is backed up. The perspective seat owns it; I do not score it.

D5 (writing_and_structure, normal priority) is mine. It asks whether the manuscript is organised so a reader can follow it, whether the exposition is clear, whether figures and tables do their job, and whether the paper conforms to the conventions of the venue it is being submitted to. For an editorial board member of Scientific Reports that last clause is concrete: the journal has a defined article format with limits on title length, abstract length and form, number of display items, legend length, placement of data and code availability statements, documentation of AI use in the methods, placement of competing interests and author contributions, and a reference-count expectation. Defects here are usually repairable and rarely decision-bearing on their own, but an editorial office will return a submission that ignores them.

D6 (venue_fit_and_contribution, mandatory) is also mine. It asks whether the manuscript belongs in Scientific Reports and whether it makes an original contribution appropriate to that readership. The journal's stated criterion is technical soundness and scientific validity, not perceived importance; so the question is not "is this a big result" but "is this a sound, original, honestly interpreted study that the journal's broad readership can use". A paper that reaches a negative or narrowed conclusion fits the journal if the conclusion is fully supported by the data and the limitations are stated; it fails fit if it is derivative without acknowledging it, if its claims outrun its evidence, or if it belongs to a venue type the journal does not publish.

## Scoring Plan

### D5: writing_and_structure

dimension_id: D5
what_to_look_for: a logical section order that a reader can follow without back-tracking; a title, abstract and conclusion that say the same thing; figures and tables that are referenced, legible, self-explanatory through their legends, and not redundant with one another; and conformance to the Scientific Reports article format as transcribed in the project's journal-requirements file, including the title-length, abstract-length, display-item, legend-length, section-placement, availability-statement, AI-use-disclosure and reference-count conventions.
what_triggers_block: the manuscript departs from the venue format in a way the editorial office would return before review, for example a structured or over-length abstract, more display items than permitted, a missing data-availability or code-availability statement, or required back-matter sections absent or misplaced; or the exposition is disorganised enough that the main result cannot be located and understood from the text and display items.
what_triggers_warn: one or more venue-format departures that an editorial office would likely let through to review but would ask to be fixed before acceptance, for example a legend over the word limit, a title slightly over the word cap, a reference list well short of the venue's expectation, an availability statement in the wrong place, or AI-use not documented where the venue asks; or local clarity problems such as a figure that cannot be read without the text, an inconsistency between abstract and body numbers, or terminology that shifts between sections.

### D6: venue_fit_and_contribution

dimension_id: D6
what_to_look_for: whether the subject sits inside the journal's broad natural-sciences and biomedical-engineering scope; whether the contribution is original relative to the prior work the manuscript itself cites and relative to what I know of the field; whether the claims, including any negative or narrowed headline, are stated at the level the data support and no higher; whether the limitations are candid; and whether a general-science reader would be able to take away a usable conclusion.
what_triggers_block: the contribution as claimed is substantially the same as a cited or well-known prior result without acknowledgement, or the main claim is stated at a level the reported evidence does not support so that a reader of this journal would be misled about what was shown, or the manuscript is of an article type the journal does not publish.
what_triggers_warn: the contribution is real but its novelty or scope is overstated in title, abstract or conclusion relative to the body; or the limitations section omits a constraint that materially bounds generalisation; or the manuscript is positioned for a specialist sub-community without the framing a general-science readership needs.
what_triggers_fatal: the manuscript is out of scope for the journal or makes no original contribution at all, so that no revision could make it acceptable at this venue.

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
score: warn
trigger: "one or more venue-format departures that an editorial office would likely let through to review but would ask to be fixed before acceptance"

### D6: venue_fit_and_contribution
score: pass

## Review Body

Reviewer identity: Editorial Board Member, Scientific Reports, biomedical engineering and medical imaging. The journal's criterion is technical soundness and scientific validity, not perceived significance, and I have applied the submission guidelines as transcribed in the project's journal-requirements file.

Journal fit. The subject, a controlled architectural evaluation for a post-reconstruction stage in thoracic EIT, sits inside the journal's engineering and health-sciences scope and needs no special argument. The paper reports a preregistered primary hypothesis that was falsified, a registered secondary hypothesis that was confirmed, and a registered addendum whose result narrows the paper's own headline. It also discloses a scoring defect that reversed every pre-correction heart-channel number. This is exactly the kind of sound, honestly interpreted study the journal exists to publish regardless of whether the result is positive. The contribution is original within the manuscript's own framing: no cited prior work evaluates the decoder branch at matched capacity and matched supervision across noise levels with a retrained control, and the manuscript states the search it ran to establish that. The title, abstract and conclusion make the same narrowed claim, and the numbers in the abstract match Table 3 and the Results text to the last decimal. D6 passes.

Writing and structure. The manuscript is well organised and the prose is precise, but it is long for this venue and carries several format departures that the editorial office would not return the paper for but would expect to be fixed. The main text (Introduction, Results, Discussion, Conclusion) is about 6,600 words against the journal's strongly recommended 4,500; the fourth Introduction paragraph alone runs to roughly 700 words and includes the database search strings and dates, which belong in Methods or Supplementary material. Figures are not numbered in order of first citation. The abstract is at exactly 200 words, which leaves no room for the submission system's field. The reference list has Nature-style formatting gaps. None of these affects the science, so D5 is a warn, not a block.

### Strengths

#### S1: Title, abstract and conclusion state one claim, and the body delivers it
The abstract's eight numerical statements (0.223 points, CI 0.020 to 0.441, p 0.098, floor 0.670, 1.937 points, 9.2-fold, 0.229 points, floor 0.384) each appear verbatim in Results and in the three-condition summary table, and the conclusion repeats the narrowed headline without widening it. No over-promising.
**Evidence Anchor**: table: Table 3, rows "D − B_wide, pts [95% CI, seeds]", "Floor (B_wide seed SD), pts" and "Rule"

#### S2: Back-matter conforms to the venue checklist
Data Availability is a separate section before References; Code availability and the AI-use documentation are subsections of Methods; competing interests sit under a heading titled Additional Information; author contributions follow References; seven display items; every legend under 350 words (longest 213); 53 references; unstructured abstract without citations; six keywords; a 17-word title.
**Evidence Anchor**: text: §2.8 and §2.9 headings "Code availability" and "Use of artificial intelligence tools"

#### S3: The defect disclosure and the addendum are reported at the level the journal's soundness criterion asks for
The scoring defect, its mechanism, its byte-for-byte reproducibility, and the fact that it reversed the earlier conclusions are stated in the main text rather than buried in a supplement. The addendum's two readings were fixed before it ran, and the falsified reading is the one applied.
**Evidence Anchor**: text: §2.5 "Every heart-channel number reported before the correction was wrong, and the conclusions were the opposite of those reported here."

#### S4: Limitations are enumerated and bound the claim
Seven limitations are listed and each is tied to a specific claim it constrains, including the reconstructor dependence, the fixed loss weights, the absence of measured data, the two-level coverage of the matched-training result, and the regulariser reading of the branch.
**Evidence Anchor**: text: §4.4 "Seven limitations bound the claims."

#### S5: The premise is measured rather than asserted
Rather than stating that the cardiac component is small, the paper applies the clinical quarter-amplitude threshold to its own reconstructions and shows the heart is recovered on fewer than half the frames. This is good exposition for a general-science reader.
**Evidence Anchor**: figure: Fig. 2

### Weaknesses

### W1: Figures are not numbered in order of first citation
Fig. 2 is cited in the first paragraph of the Introduction; Fig. 1 is first cited in Methods §2.2. The journal numbers figures by first mention, and the typesetter will ask for this to be resolved. Either renumber (the separability figure becomes Fig. 1) or cite the arms figure earlier.
**Severity**: Minor
**Evidence Anchor**: figure: Fig. 2, first cited §1 paragraph 1, before Fig. 1 (first cited §2.2)
**Confidence**: 5 — direct count of first-citation positions against the venue convention

### W2: Main text is about 47% over the venue's strongly recommended length, and parts of the Introduction address reviewers rather than readers
Introduction, Results, Discussion and Conclusion total about 6,600 words against 4,500 strongly recommended. The limit is not enforced, but an Editorial Board Member reads "concise" as part of the format. Two specific moves would recover most of the excess without touching any claim: move the database search strings and dates from the fourth Introduction paragraph to Methods or Supplementary material, and remove or recast the paragraph that pre-answers three anticipated reviewer questions, which reads as a response-to-reviewers inserted into the article.
**Severity**: Minor
**Evidence Anchor**: text: §1 "Three questions follow directly, and it is better to answer them here than to leave them to a reviewer."
**Confidence**: 4 — word count computed on the submission file; the venue limit is advisory

### W3: The Introduction promises citations to companion studies that do not exist in the reference list
The sentence states that companion studies testing the same statement under other conditions are cited accordingly, but no companion study is cited anywhere in the manuscript; the only other mention says the weighting question is the subject of a companion study and is not tested here. A reader will look for the reference. Either cite the registered companion work (a preregistration record is citable) or reword to say the companion conditions are planned and unpublished.
**Severity**: Minor
**Evidence Anchor**: text: §1 "The companion studies test the same statement under the other conditions and are cited accordingly."
**Confidence**: 5 — searched the full text and reference list for any companion citation

### W4: Reference list has Nature-style formatting gaps
The journal does not copy-edit references, so these will print as submitted. Reference 45 lacks an article number; reference 43 lacks a volume; reference 22 carries a stray star glyph at the end of its title; references 6 and 42 carry NLM-style journal-name qualifiers "(1985)" and "(Basel)" that Nature style omits; title capitalisation is mixed between sentence case and title case (for example references 14, 20, 36, 47). A pass of the citation tool against the Nature template will fix all of these.
**Severity**: Minor
**Evidence Anchor**: text: Reference 22 "Domain independent post-processing with graph U-nets: applications to electrical impedance tomographic imaging⋆"
**Confidence**: 4 — checked against the transcribed Nature reference format

### W5: Table 2 caption contains inline LaTeX that will typeset incorrectly
The caption's expression uses an underscore inside a roman-font macro, so the subscript will take only the first letter and the remainder will print as text. Write the quantity in words or with a proper subscript. The same render check should confirm that the figure images, which the source embeds by absolute machine-local paths, are present in the submitted file.
**Severity**: Minor
**Evidence Anchor**: table: Table 2 caption, inline math expression for relative error reduction
**Confidence**: 4 — reading the source markup; the rendered submission file was not inspected

### W6: Model checkpoints are offered on request rather than deposited
The journal's data policy expects relevant data in a public repository where a suitable one exists. Seventeen gigabytes exceeds GitHub but is within the limits of general-purpose repositories such as Zenodo or figshare, which also issue a DOI. Depositing the checkpoints, or stating why deposition is not feasible beyond repository-host size, would close the point before an Editorial Board Member raises it.
**Severity**: Minor
**Evidence Anchor**: text: Data Availability "are available from the corresponding author on request, because their size exceeds what the repository host accepts"
**Confidence**: 4 — venue data-policy reading; repository limits from general knowledge

### W7: Discussion is divided by long declarative subheadings and Methods precedes Results, against the venue's suggested structure
The journal permits any structure, so this is not a defect, but its suggested form is Results with subheadings, Discussion without, and Methods last. The four Discussion subheadings are full sentences that state conclusions; a reader skimming headings reads four claims before the evidence. Consider short topical subheadings or none, and consider whether moving Methods after Discussion would serve the journal's general readership, who typically read Results first.
**Severity**: Minor
**Evidence Anchor**: text: §4.1 heading "The advantage under heavier noise belongs mostly to the training-evaluation mismatch, and this study measured that before it could be attributed to the branch"
**Confidence**: 3 — venue structure is advisory; the ordering is a judgement call for the authors

### W8: The abstract's third sentence is hard to parse on first reading
The sentence opens with a partitive phrase and then lists what the second study registered, so the subject arrives late and the parenthetical software names interrupt it. At exactly 200 words the abstract also has no slack if the submission system's field counts differently. One sentence rewritten in subject-verb order would fix both.
**Severity**: Minor
**Evidence Anchor**: text: Abstract "Of two preregistered simulation studies (EIDORS, GREIT), the second registered heart-channel Dice as primary endpoint"
**Confidence**: 4 — editorial reading; the word count was computed on the submission file

### Questions for Authors
1. Will the companion conditions referred to in the Introduction be registered or published in a citable form before this paper appears, so that the sentence promising citations can be made true?
2. Is deposition of the 17 GB of checkpoints in a DOI-issuing repository feasible, and if not, what prevents it?

### Overall signal
Minor Revision. Confidence 4. The paper fits the journal, the contribution is original and honestly bounded, and every defect found is a venue-format or clarity repair that leaves the claims untouched.

---

# Seat 2 — Reviewer 1, Methodology (methodology)

## Phase 1 (paper-content-blind)

## Contract Paraphrase

D1 (methodology_rigor, mandatory, owned by this seat): from the methodology-rigor lens this dimension asks whether the study design can answer the question the title poses, whether the unit of replication, the pairing structure, the interval procedure and the decision rules are stated before the data are looked at and then applied as stated, whether test statistics and p-values are reported with enough precision to be recomputed, whether multiplicity across repeated comparisons is handled or at least acknowledged, whether any normal approximation or asymptotic procedure is justified at the sample size actually used, and whether code, seeds, configurations and data are made available so that another group could obtain the same numbers.

D2 (domain_accuracy, mandatory, owned by the domain seat): from my lens this is about whether the quantities being measured, the noise model being swept, and the reference methods being compared are described in a way that is consistent with how the field defines them; I do not score it, but a methodological finding of mine may touch it where a domain definition is used as a measurement instrument.

D3 (argumentative_coherence, mandatory, co-owned by the Devil's Advocate and this seat): from the methodology-rigor lens this asks whether every stated conclusion is entailed by the reported evidence under the paper's own preregistered decision rules, whether a registered hypothesis that fails is reported as failing rather than reframed, whether an unregistered analysis is clearly labelled as exploratory and kept out of the headline, whether null results are interpreted with an explicit sensitivity bound rather than as equivalence, and whether the abstract, results and discussion make the same claim at the same scope.

D4 (cross_disciplinary_relevance, high priority, owned by the perspective seat): from my lens this concerns whether a reader from a neighbouring quantitative field can follow the design logic (what is paired with what, what is replicated, what a decision rule means) without domain-specific background; I do not score it.

D5 (writing_and_structure, normal priority, owned by the editor-in-chief seat): from my lens this concerns whether tables and figures carry the elements a methodologist needs (n, replication unit, interval type, test statistic) and whether the methods section is organised so that a procedure can be followed in order; I do not score it.

D6 (venue_fit_and_contribution, mandatory, owned by the editor-in-chief seat): from my lens this concerns whether the methodological contribution (a preregistered, capacity-matched design with a noise sweep) is itself substantive enough to matter to the venue's readership, and whether the reporting standard matches what the venue's methods-heavy readers expect; I do not score it.

## Scoring Plan

### D1: methodology_rigor
dimension_id: D1
what_to_look_for: Whether the replication unit and pairing structure are stated and used consistently; whether the preregistered decision rules, effect-size floors and interval procedures are applied exactly as registered; whether seeds, geometries and noise levels are kept distinct as sources of variation; whether multiplicity across a sweep of evaluation conditions is handled or acknowledged; whether a normal approximation for a rank test is justified at the stated n and whether ties and zero-differences are handled; whether unregistered or post-hoc analyses are labelled as such; whether the capacity-matching procedure actually matches the quantity the claim turns on; whether power or sensitivity statements are backed by a stated calculation; whether an evaluation-only sweep is distinguished from retraining; and whether code, seeds, configurations and data are available.
what_triggers_block: a preregistered decision rule, replication unit, interval procedure or matching procedure is applied differently from how it is stated, or an unregistered analysis is presented as if it were confirmatory, so that the headline conclusion cannot be reproduced from the stated procedure without re-analysis
what_triggers_warn: statistical reporting is incomplete or under-justified, for example missing multiplicity handling across sweep levels, an unjustified normal approximation, a power claim without a stated calculation, an unlabelled exploratory analysis, or missing reproducibility detail, without changing what the stated procedure would conclude
what_triggers_fatal: the design cannot in principle answer the stated question, for example the comparison arms differ on the very quantity the claim turns on, or the evaluation data are not independent of the training data, so that no re-analysis of the reported data can rescue the core claim

### D3: argumentative_coherence
dimension_id: D3
what_to_look_for: Whether each conclusion in the abstract, results and discussion is entailed by the reported evidence under the paper's own decision rules; whether a falsified registered hypothesis is reported as falsified rather than reframed as support; whether exploratory findings are kept out of the headline claim; whether null results are read with an explicit sensitivity bound rather than as equivalence; whether the scope of the headline claim matches the conditions actually tested; and whether the claim stated in one section contradicts the claim stated in another.
what_triggers_block: a stated conclusion is not entailed by the reported evidence under the paper's own decision rules, or the headline claim in one section contradicts the evidence or claim stated in another section
what_triggers_warn: a claim is overstated or under-qualified relative to the evidence, for example a generalisation beyond the tested conditions or a null result read as equivalence without a sensitivity bound, while the central thesis survives once reworded
what_triggers_fatal: the central thesis rests on a circular inference or a logical fallacy such that no rewording within the reported evidence can make the core argument valid

criteria_binding_unavailable

[CONTRACT-ACKNOWLEDGED]

## Phase 2 (paper-visible)

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

---

# Seat 3 — Reviewer 2, Domain (domain)

## Phase 1 (paper-content-blind)

## Contract Paraphrase

D1 (methodology_rigor, mandatory, owned by the methodology seat): the study design, data handling, statistics and reproducibility affordances must meet what a thoracic-EIT peer reviewer would expect of a simulation study. From the domain-accuracy lens I do not score this; I only note where a design choice rests on a domain fact that is wrong (for example a noise model or forward-model convention that the field would not recognise), and I hand that to the methodology seat rather than scoring it myself.

D2 (domain_accuracy, mandatory, owned by me): every claim about the EIT field must agree with the current evidence base; each cited work must be represented as it actually reads, not as the authors wish it read; and terminology (ventilation versus cardiac-related signal, perfusion versus pulsatility, GREIT versus Gauss-Newton versus back-projection, SNR conventions, electrode and contact-impedance artefacts) must be used as the field uses it. Because many citation sentences are reported to have been written from abstracts rather than full texts, the specific risk is sentences that are plausible but attribute to a paper a result, scope, or number it does not contain.

D3 (argumentative_coherence, mandatory, owned by the DA seat, methodology also eligible): the thesis must be internally consistent and the evidence must actually support the stated claims. I do not score this. Where a domain misstatement would propagate into the argument (a mischaracterised prior result used as the premise for the gap), I flag the misstatement under D2 and leave the argumentative consequence to the eligible seats.

D4 (cross_disciplinary_relevance, high priority, owned by the perspective seat): framing, definitions and implications must be readable by adjacent-field readers (deep-learning, physiology, instrumentation) and any interdisciplinary claim must be substantiated. Not mine to score; from my lens the only overlap is whether a definition offered to outsiders is also correct for insiders.

D5 (writing_and_structure, normal priority, owned by the EiC seat): organisation, clarity, figures and tables, venue conventions. Not mine to score. Terminology inconsistency that is purely stylistic belongs here; terminology that is wrong for the field belongs under D2.

D6 (venue_fit_and_contribution, mandatory, owned by the EiC seat): the manuscript must fit the configured venue and make an original, significant contribution for its readership. Not mine to score. I will state, as domain commentary only, whether the contribution is genuinely new relative to the EIT literature I know, so the EiC seat has a domain-grounded input, but I will not assign a score.

## Scoring Plan

### D2: domain_accuracy
dimension_id: D2
what_to_look_for: Each citation sentence checked against what I know of the cited paper (scope, method, population, direction and magnitude of result); field terminology (ventilation/cardiac-related/perfusion, GREIT/EIDORS conventions, SNR definitions, electrode artefacts) used as the field uses it; standard prior work on cardiac-ventilation separation in thoracic EIT (ECG gating, frequency filtering, PCA and template methods, bolus perfusion) and on deep-learning post-processing of EIT present and correctly characterised; no numeric or directional claim attributed to a source it does not contain; uncertainty on my side declared per sentence.
what_triggers_block: Two or more cited works are materially misrepresented in a way that bears on the gap or the interpretation (for example a method the paper claims is absent from the literature is in fact established and cited as if it were not), or a core field term is used wrongly throughout so that a thoracic-EIT reader would misread the claim.
what_triggers_warn: One cited work materially misrepresented, or several citation sentences that overstate or over-generalise an abstract in ways that do not change the gap, or a standard reference line of the subfield missing without justification, or a terminology slip confined to one passage.
what_triggers_fatal: The central claim rests on a factual error about the field that cannot be repaired by rewording (for example the cardiac-related EIT signal is characterised in a way that contradicts established physiology or the reconstruction-pipeline description is wrong such that the simulated separation problem is not the problem the paper says it is).
criteria_binding_unavailable

[CONTRACT-ACKNOWLEDGED]

## Phase 2 (paper-visible)

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

---

# Seat 4 — Reviewer 3, Perspective (perspective)

## Phase 1 (paper-content-blind)

## Contract Paraphrase

D1 (methodology_rigor, mandatory, owner methodology). From where I sit — multi-task learning and medical-image-analysis validation practice — this dimension asks whether the study design, data handling, statistics and reproducibility affordances would survive a referee in the paper's own field. I do not score it. My only interest in it is indirect: if the design choices that make a result credible to a methodologist (matched baselines, preregistration, seeds, released code) are also the choices that make it legible to an outsider, then D1 and D4 reinforce each other, and I will note that in prose rather than score it.

D2 (domain_accuracy, mandatory, owner domain). This asks whether the paper represents its own field's prior work and terminology correctly. It belongs to the domain seat. My lens touches it only where the manuscript makes claims about the adjacent field I represent — multi-task learning, shared-encoder/multi-decoder architectures, loss weighting, capacity-matched baselines, robustness under distribution shift. If those are misrepresented, that is a cross-disciplinary substantiation failure and I will report it under D4, not D2.

D3 (argumentative_coherence, mandatory, owners da and methodology). This asks whether the thesis is internally consistent and the evidence actually supports the claims. It is the Devil's Advocate's and the methodologist's territory; I will not hunt for fallacies or internal contradictions. Where a coherence problem shows up only when the paper's claim is read through the vocabulary of an adjacent field (for example, a multi-task framing that the adjacent field would reject), I will report the framing mismatch under D4 and leave the logic to D3's owners.

D4 (cross_disciplinary_relevance, high priority, owner perspective — my dimension). This asks three things of the manuscript as read by someone outside its home field: (i) can a reader from medical image analysis or multi-task learning follow the framing and definitions without the home field's tacit knowledge; (ii) when the paper borrows a concept from an adjacent field — branching, shared representations, capacity matching, robustness benchmarks, train/test mismatch — is the borrowed concept used in the sense the adjacent field would recognise, and is any claim about it backed by evidence or citation rather than assertion; (iii) is the practical implication stated at the scope the evidence licenses, neither over-generalised to the adjacent field nor hidden inside home-field jargon. This is high priority, not mandatory, so it cannot by itself produce a fatal block; a block here routes to major revision via F4, a warn to minor revision via F5.

D5 (writing_and_structure, normal, owner eic). This asks whether the manuscript is organised, clearly written, well-figured and venue-conformant. The editor-in-chief seat owns it. Accessibility to adjacent readers overlaps with clarity, but I will keep accessibility (D4) separate from general prose quality (D5): a paragraph can be beautifully written and still opaque to an outsider, or clumsy and still perfectly legible across fields.

D6 (venue_fit_and_contribution, mandatory, owner eic). This asks whether the paper fits the configured venue and makes an original, significant contribution for that readership. The editor seat owns it. Because the venue has a broad, multidisciplinary readership, the editor's fit judgement and my accessibility judgement will be correlated, but they are distinct questions: D6 asks whether the contribution matters to that readership; D4 asks whether that readership can understand and correctly transfer it.

## Scoring Plan

### D4: cross_disciplinary_relevance
dimension_id: D4
what_to_look_for: Whether the multi-task / branching framing matches how the adjacent field uses those terms; whether a medical-image-analysis or MTL reader can extract the design, the baseline-matching logic, and the noise-shift evaluation without EIT-specific tacit knowledge; whether claims about adjacent-field concepts (shared encoders, decoder branching, capacity matching, loss weighting, robustness under SNR shift, train/test mismatch) are substantiated by evidence or citation; and whether the stated practical implication is scoped to what the evidence shows rather than generalised to other modalities or tasks.
what_triggers_block: The central framing borrows an adjacent-field concept in a way that field would reject as a misreading, or the headline implication is generalised to adjacent-field settings that the evidence does not test, such that an adjacent reader would take away a conclusion the data cannot support.
what_triggers_warn: Adjacent-field concepts are used correctly but key definitions or the baseline-matching logic require home-field knowledge to follow, or one or more interdisciplinary claims are asserted without evidence or citation, or the practical implication is stated at a scope slightly wider or narrower than the evidence, in a way that would mislead but not invert an adjacent reader's takeaway.

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

---

# Seat 5 — Devil's Advocate (da)

## Phase 1 (paper-content-blind)

## Contract Paraphrase

D1 (methodology_rigor, mandatory, owned by the methodology seat). From the adversarial lens this dimension asks whether the design, data handling, statistics and reproducibility affordances would survive a hostile reader who assumes every unreported degree of freedom was exercised in the authors' favour. I do not score it, but any design hole that opens a rival explanation of the headline is something I will surface as a finding.

D2 (domain_accuracy, mandatory, owned by the domain seat). The adversarial question is whether prior work is represented so as to make the contribution look larger than it is, whether field terminology is used in a way that quietly smuggles in a conclusion, and whether any result statement is factually at odds with what the field already knows. I do not score it; I report misrepresentation of prior work only where it props up the central argument.

D3 (argumentative_coherence, mandatory, my owned dimension, co-eligible with methodology). This is the seat's home ground: does the central thesis stay the same thesis from title to conclusion, does each inferential step from evidence to claim actually follow, is there a simpler explanation the design cannot exclude, are results selectively emphasised, and does the scope of the conclusion exceed what was tested. A paper can be methodologically clean and still fail here if the words at the end claim more than the numbers in the middle, or if a conceded limitation is not carried into the headline.

D4 (cross_disciplinary_relevance, high priority, owned by the perspective seat). Adversarially: are the framing and definitions comprehensible to a reader outside the immediate subfield, and are any claims of relevance to adjacent fields actually substantiated rather than asserted. I do not score it; I note where an interdisciplinary claim is a logic gap.

D5 (writing_and_structure, normal priority, owned by the editor seat). Adversarially: does the organisation hide weaknesses, do figures and tables show what the text says they show, and do venue conventions get followed. I do not score it; I raise a structural point only when it obscures or misstates the argument.

D6 (venue_fit_and_contribution, mandatory, owned by the editor seat). Adversarially this is the "so what" dimension: if the conclusion is correct, what changes, is the increment sufficient for this venue, and is the contribution original rather than a restatement of what the field would already assume. I do not score it, but the so-what test is part of my review body and its result is handed to the owner seat as a finding.

## Scoring Plan

### D3: argumentative_coherence
dimension_id: D3
what_to_look_for: whether the headline claim in title, abstract and conclusion is the same claim the preregistered primary evidence supports; whether each step from result to interpretation follows without hidden assumptions; whether a rival explanation left open by the design fits the data as well or better; whether results are selectively emphasised; whether conceded limitations are carried into the headline; whether the scope of generalisation exceeds the tested conditions
what_triggers_block: the headline claim is not supported by the primary preregistered evidence, or a rival explanation left open by the design fits the reported data at least as well as the authors' mechanism, or the conclusions generalise beyond the conditions actually tested
what_triggers_warn: a stated conclusion outruns its evidence in scope or strength, a limitation that bears on the headline is conceded but not carried into the abstract or conclusions, or secondary analyses are selectively emphasised over preregistered ones without a stated rule
what_triggers_fatal: the authors' own reported data contradict the headline conclusion, or the core inference rests on an assumption shown false within the manuscript, such that no rewording rescues the central claim

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

---

# Phase 2 — Editorial synthesis (mechanical, reviewer_full v2)

## Step 1 — Role-scoped scoring matrix

| Dimension | Eligible seats | Assessed scores | Verdict (worst) |
|---|---|---|---|
| D1 methodology_rigor (mandatory) | methodology | warn | warn |
| D2 domain_accuracy (mandatory) | domain | warn | warn |
| D3 argumentative_coherence (mandatory) | da, methodology | block (repairable), warn | block |
| D4 cross_disciplinary_relevance (high) | perspective | warn | warn |
| D5 writing_and_structure (normal) | eic | warn | warn |
| D6 venue_fit_and_contribution (mandatory) | eic | pass | pass |

No fatal block declared by any seat. No Scoring Plan Dissent filed by any seat. No DA CRITICAL row.

## Step 2 — Failure conditions

- F1 (any mandatory dimension has a fatal block): did not fire.
- F2 (any mandatory dimension scores 'block'): **fired** (D3, da seat, repairable).
- F3 (two or more mandatory dimensions score 'warn' or worse): fired (D1, D2, D3).
- F4 (any high-priority dimension scores 'block'): did not fire.
- F5 (any dimension scores 'warn' or worse): fired (D1, D2, D3, D4, D5).
- F0 (every dimension scores 'pass'): did not fire.

## Step 3 — Precedence and decision

dimension_verdicts: [D1=warn, D2=warn, D3=block, D4=warn, D5=warn, D6=pass]
fired_conditions: [F2, F3, F5]
da_critical_adjudications: []
editorial_decision=major_revision

---

# Editorial Decision Letter

## Manuscript Information
- **Title**: A decoder branch for the cardiac component of lung EIT: a preregistered, parameter-matched evaluation across measurement-noise levels
- **Manuscript**: `manuscript/32_SUBMISSION_scirep.md` (Sci Rep deliverable of `29_DRAFT_v3.md`, round-2 revision of 2026-10-06)
- **Decision date**: 2026-10-06 · **Review round**: 2 (first full panel after the Physiol Meas desk reject; round 1 of 2026-09-23 and the re-review of 2026-09-26 targeted TMI)
- **Target venue read by the Journal-Fit seat**: Scientific Reports (technical soundness and scientific validity; `refs/01_JOURNAL_REQUIREMENTS_SCIREP.md`); `criteria_binding_unavailable` (no #684 ReviewTargetContext)

## Decision

### Major Revision

Mechanical result of contract `reviewer/reviewer_full/v2`: the Devil's Advocate seat scored D3 (argumentative coherence) `block`, class `repairable`; F2 fired. No fatal block, no DA CRITICAL, no dissent. The three other mandatory dimensions are `warn` (D1, D2) and `pass` (D6). Every seat that gives a recommendation gives Minor Revision; the contract's F2 outranks that, and the panel agrees the block is repairable by rewriting, not by new data.

## Blocking Issues (immutable source order)

| Transport ref | Blocking issue | Source reviewer(s) | Evidence anchor | Resolving roadmap item |
|---|---|---|---|---|
| R1 | The sample size covers only the p-condition of the registered rule; the effect-size floor (one seed-SD) had essentially no power at the anticipated effect, and the paper presents n = 58 as if it powered the whole rule | R1-W1 | text: §2.4 "Scaling Study 1's heart effect by that variance gave dz ≈ 0.376, and 80% power at that effect size requires 58 seeds." | REV-2 |
| R2 | The addendum removed the training–evaluation mismatch and, by the paper's own operational definition of "under threat" (control-arm loss), the threat at the same time; the attribution "most of the benefit is mismatch tolerance" is not licensed by a design that co-varied the two | R1-W2, DA-M1 | text: §4.1 "The design that can distinguish them found that most of the effect is the latter." | REV-1 |
| R3 | The phantom's cardiac component is spatially disjoint from the lung inclusions, while the Introduction motivates the problem with cardiac-related changes inside the lung field and with spatial overlap; the manuscript does not say the overlap difficulty is absent by construction | R2-W1 | text: §2.3 "two lung inclusions at 0.5 S/m and one heart inclusion at 2.0 S/m" | REV-3 |

## Reviewer Summary

| Seat | Configured identity | Scores | Recommendation | Confidence |
|---|---|---|---|---|
| Journal-Fit (eic) | Scientific Reports Editorial Board Member, biomedical engineering / medical imaging | D5 warn, D6 pass | Minor Revision | 4 |
| R1 (methodology) | Statistician-engineer, ML evaluation methodology | D1 warn, D3 warn | Minor Revision | 4 |
| R2 (domain) | Thoracic EIT physiologist/engineer | D2 warn | Minor Revision | 4 |
| R3 (perspective) | Multi-task learning / medical image analysis | D4 warn | Minor Revision | 4 |
| Devil's Advocate | fixed seat | D3 block (repairable) | findings only | per finding |

## Consensus Analysis

Sub-claim inventory over the four non-DA seats (DA tracked separately). Severity and confidence transported from the cards.

| sub_claim | parent weakness | EIC | R1 | R2 | R3 | disposition | severity |
|---|---|---|---|---|---|---|---|
| SC-1 attribution of the 20 dB benefit to mismatch tolerance is not licensed | R1-W2 (DA-M1 corroborates outside the count) | silent | raised | silent | disputed-in-direction (R3-W5 says the shift-tolerance result is undersold) | SPLIT → arbitrated for R1 (below) | Major |
| SC-2 registered rule under-powered at the floor | R1-W1 | silent | raised | silent | silent | single-reviewer finding, evidence anchored | Major |
| SC-3 phantom spatially disjoint, framing silent on it | R2-W1 | silent | silent | raised | silent | single-reviewer finding, evidence anchored | Major |
| SC-4 closing sentence / practical implication generalises beyond the tested cell | R3-W4, R1-W11 (onset without descriptive label), EIC-W2 (reviewer-facing paragraph) | raised | raised | silent | raised | CONSENSUS-3 (R2 silent) | Minor |
| SC-5 checkpoints on request rather than deposited | EIC-W6, R1-W10 | raised | raised | silent | silent | corroborated finding | Minor |
| SC-6 citation sentences overstate or mis-attribute (Graf posture; quarter-amplitude set is GREIT's; Murphy is bioimpedance; bolus cited second-hand) | R2-W2–W5 | silent | silent | raised | silent | single-reviewer findings | Minor |
| SC-7 statistical-reporting gaps (continuity correction, dz derivation, multiplicity, unregistered contrasts, floor SE, ratio-of-means) | R1-W3–W8 | silent | raised | silent | silent | single-reviewer findings | Minor |
| SC-8 venue-format departures (figure order, references, Table 2 LaTeX, companion-studies sentence, abstract sentence 3, structure) | EIC-W1, W3–W5, W7, W8 | raised | silent | silent | silent | single-reviewer findings | Minor |
| SC-9 accessibility for the adjacent reader (Dice points undefined; interference locus; task relatedness) | R3-W1–W3 | silent | silent | silent | raised | single-reviewer findings | Minor |

### Points of agreement
- **CONSENSUS-3 (SC-4)**: EIC, R1 and R3 each find a place where the stated implication outruns the tested cell (§5 closing sentence; Abstract/Conclusion onset without the descriptive label; the Introduction paragraph that addresses reviewers). R2 is silent.
- **Corroborated (SC-5)**: EIC-W6 and R1-W10 both ask for the rule-bearing checkpoints or per-seed predictions to be deposited (Zenodo/OSF/figshare) rather than offered on request.
- **DA corroboration (outside the count)**: DA-M1 and R1-W2 state the same defect from two angles; DA-M3 (§3.1 calls 0.22 points a chance residual, §3.5 treats it as reproducible) is uncontradicted by any seat.

### Points of disagreement
**Disagreement 1 — direction of the mismatch reading (SC-1).** R1-W2 and DA-M1: the addendum co-varied threat and mismatch; the manuscript's "most of the benefit is mismatch tolerance" (Abstract, §4.1, §5) apportions what the design cannot apportion, and the §1 thesis receives no verdict. R3-W5: the same result is undersold to the robustness reader and should be framed as a shift-tolerance finding. Type: direction disagreement. **Resolution for R1/DA**, on evidence and expertise: the addendum's registered reading (§2.7) is "attributable in whole or in part to distribution-shift tolerance", and the manuscript's own operational definition of threat (control-arm loss, §4.1) makes the 20|20 condition one in which the threat is also gone. Both readings predict the falsified H5. The sentences that say "most", "the larger part" and "mainly" must return to the registered wording and state that the two readings were not dissociated; R3's framing can be served inside that wording (the result is a shift-tolerance finding at least in part) without the apportionment.

**Disagreement 2 — task relatedness (SC-9, R3-W3) versus the paper's interference framing.** R3 reads the two targets as near-complementary decompositions of one input, hence maximally related tasks; the paper frames the branch question through task interference. Type: perspective difference. **Resolution**: author autonomy. One sentence in §1 or §4.3 stating why interference is still the right frame for complementary targets (or conceding that it is not) is enough; the registered design does not depend on it.

### Devil's Advocate adjudication
No CRITICAL rows. The four MAJOR rows are adjudicated for visibility: M1 validated (corroborated by R1-W2; enters REV-1); M2 (width as an unexcluded rival at 20|40, and the sweep reports no B, C or C_wide rows) is a re-analysis of existing per-seed files, not new training, and is placed as should_fix (REV-6); M3 validated as a wording inconsistency (REV-4); M4 (the positive clause of the headline names a regime practitioners avoid by augmentation, and the abstract leads with it) is a framing point placed as should_fix (REV-7). None of the four is a veto; the block on D3 is repairable by text.

## Decision Rationale

The panel reads a preregistered, candidly reported study whose registered verdicts (H1, H2, H5 falsified; H3 confirmed; the 9.2-fold shrinkage under matched training) no seat disputes, whose numbers are internally consistent across Tables 1 to 3 (R1-S6, four arithmetic receipts consistent, one minor mismatch on a continuity correction), and whose literature coverage is now judged correct and primary-sourced by the domain seat (R2-S1 to S5). The decision is Major Revision because one mandatory dimension carries a repairable block: the Devil's Advocate and the methodology seat, from different angles, find that the manuscript's headline attribution of the 20 dB benefit to mismatch tolerance claims an apportionment the registered addendum cannot deliver, since retraining at 20 dB removed the mismatch and the operationally defined threat together. The fix is to return the three places that say "most" or "mainly" to the registered reading and to give the §1 thesis its verdict in the matched condition. Two further Major items are textual: the power paragraph must say what the registered rule's floor demands and that n = 58 was sized for the p-condition only, and the phantom section and Limitation 3 must say that the in-vivo spatial-overlap difficulty is absent from this phantom by construction. No seat asks for new data; the one re-analysis requested (sweep rows for the other arms) uses files the authors already hold. The panel chose Major over Minor because the contract fires F2 on a mandatory block and because REV-1 touches the Abstract, §4.1 and §5 at once; it chose Major over Reject because every seat independently recommended Minor Revision, the venue-fit dimension passed, and nothing found reaches the Critical band. Re-review after revision is required.

## Required Revisions (must_fix)

| Item | Source | Severity | What to change | Cost | Targets (v3 block ids; `insert_after` where new text is needed) |
|---|---|---|---|---|---|
| REV-1 | R1-W2, DA-M1 (DA-M3 shares the surface) | Major | Replace "most of that benefit is mismatch tolerance" (Abstract), "the larger part of the evaluation-only advantage is distribution-shift tolerance" and "most of the effect is the latter" (§4.1), "most of what it was worth … was tolerance of noise the network had not seen" (§5), and the §3.5 closing paragraph with the registered reading: the benefit does not survive matched training; the addendum removed the mismatch and the operationally defined threat together, so the design cannot say how much belongs to each; the §1 statement is therefore untested in the matched condition, not refuted and not confirmed | section | B0005 (abstract file 31_), B0051, B0052, B0125, B0064, B0050 (§4.1 heading) |
| REV-2 | R1-W1, R1-W4 | Major | §2.4 sample-size paragraph: state that n = 58 was sized for the p-condition; state what the floor demands (a paired effect of about one seed-SD, dz near 1) and that the registered rule therefore had little power to confirm at the anticipated effect; re-derive and correct the dz ≈ 0.376 and the 29% figures from the preregistration, or state the calculation; add one sentence to §4.2 | sentence | B0029, B0055 |
| REV-3 | R2-W1 | Major | §2.3 and Limitation 3 (§4.4), and the §1 motivation sentence: state that the heart inclusion is spatially separate from the lung inclusions, so the spatial-overlap difficulty the Introduction cites is absent by construction and the weak-component difficulty here is amplitude and reconstruction blur | sentence | B0023, B0062, B0009 |
| REV-4 | DA-M3 | Major (D3) | §3.1 last paragraph: remove "a near-zero residual whose sign happened to be positive" or reconcile it with §3.5's reproducible 0.22-point contrast whose geometry-level interval excludes zero; say what the two intervals do and do not establish | sentence | B0038 |

## Suggested Revisions (should_fix)

| Item | Source | What to change | Cost | Targets |
|---|---|---|---|---|
| REV-5 | SC-4: R3-W4, R1-W11, EIC-W2 | Scope the §5 closing sentence to the tested cell; attach the descriptive label to the onset in Abstract and §5; drop or rewrite the "better to answer them here than to leave them to a reviewer" paragraph for readers | sentence | B0064, B0005, B0012 |
| REV-6 | DA-M2 | Report the evaluation-only sweep for arms B, C and C_wide (Table 2 or Supplementary) from the existing per-seed files; comment on width as a rival at 20\|40 | re_analysis (existing data) | B0041, B0082, B0083 |
| REV-7 | DA-M4 | Reorder the abstract's and §5's conclusion to lead with the matched-training result; argue or drop the significance of the fixed-level-training regime | sentence | B0005, B0064 |
| REV-8 | R1-W3 (AR1) | Check which Wilcoxon procedure the scoring code used; make §2.4's continuity-correction statement and Table 3's p = 0.0983 agree | sentence | B0028, Table 3 |
| REV-9 | R1-W5, W6, W7, W8 | Add a multiplicity statement for the seven levels and four rules; list the unregistered contrasts in §2.6; report the floor's SE beside the H5 verdict; define the relative-error-reduction statistic as a mean of per-seed ratios and note its divergence from the ratio of means at high SNR | sentence | B0028, B0034, B0122, B0042 |
| REV-10 | R2-W2, W3, W4, W5 | Graf 2017: body posture, not position in the thorax; attribute the quarter-amplitude set to GREIT, not to the ROI paper; Murphy 2019: bioimpedance cardiac output, not EIT; add Frerichs 2002 as the bolus primary source via `cite.py` (R12d) | sentence | B0009, B0027, B0062, B0075 |
| REV-11 | EIC-W1, W3, W4, W5, W8 | Renumber figures by first citation; delete or make true "the companion studies … are cited accordingly"; fix reference rendering (article numbers, LNCS volume, stray glyph, title case); replace the LaTeX in the Table 2 caption; rewrite abstract sentence 3 | sentence | B0009, B0013, B0075, B0082, 31_ |
| REV-12 | R3-W1, W2 | Define "Dice points" (hundredths of Dice) at first use; state where the hypothesised interference acts in a design that shares the encoder | sentence | B0005, B0011 |

## Consider

| Item | Source | Note |
|---|---|---|
| REV-13 | SC-5: EIC-W6, R1-W10; R1-W9 | Deposit rule-bearing checkpoints or per-seed predictions (Zenodo/OSF); state MPS determinism; report FLOPs/activation footprint beside parameter count |
| REV-14 | EIC-W7, EIC-W2 | Venue-suggested order (Results before Methods, Discussion without subheadings) and the 4,500-word recommendation are advisory; the authors decide |
| REV-15 | R3-W3, R3-W5 | One sentence on why interference is the frame for complementary targets; optional reframing of the shift-tolerance result for the robustness reader, inside the REV-1 wording |

## Revision Roadmap

Items REV-1 … REV-15 above, in immutable source order (seat, ordinal); `R<n>` and `REV-<n>` are transport references, not a work order. Severity transported from the cards; obligation class is the editorial gate; targets name v3 block ids of `29_DRAFT_v3.md` (the Abstract lives in `31_ABSTRACT_SCIREP_bilingual.md` for the deliverable and in B0005 of the working draft). The machine-readable `revision-roadmap/1.0` is built by the round-3 authority script when revision starts (same chain as rounds 1 and 2); author triage (`will_address` / `wont_address` / `not_on_point`) is collected in the separate sidecar and never inferred here.

## Response Letter Template

For each REV item: (1) the panel's point in one sentence, (2) what changed and where (block id / section), (3) what did not change and why. Items declined must say so.

## Notes for the PI (outside the letter)

- REV-1 is the one that changes a sentence the PI has read many times: the registered reading is "in whole or in part", and the manuscript drifted to "most" in three places. The panel is right that the addendum cannot apportion; the practical conclusion ("a network trained at its operating level gains 0.22–0.23 points at both levels") stands unchanged.
- REV-2 is a disclosure, not a redesign: the floor was registered as the seed-to-seed SD, which is about one SD of the paired difference, so the rule asked for dz near 1 while the sample was sized for dz 0.376 at p < 0.05. Say it; do not revise the rule.
- REV-8 is an execution check on `tools/` (scipy `wilcoxon` defaults to no continuity correction); whichever the code did, the text must match.
- REV-6 needs no training; the sweep per-seed files for B, C and C_wide exist if the registered sweep scored all arms. If they do not, say so in the response.
- Panel provenance this round: five seats in separate contexts, blind to one another (axes in the header); same model family throughout, so recurring findings corroborate an angle, not an independent error process. The PI's own read and the real Sci Rep review remain the independent checks.

---

## Attachment: Acronym Check (advisory, #849)

### Acronym check (advisory; no reply needed)
Coverage: body (partial)
Not in this input: English abstract, Chinese abstract.
Not checked:
- Body, line 62: SNR (the initials before its parentheses do not spell it)
- Body, line 70: EIDORS (the initials before its parentheses do not spell it)
- Body, line 106: HD95 (the initials before its parentheses do not spell it)

| Scope | Line | Rule | Acronym | Uses |
|---|---|---|---|---|
| Body | 20 | Not defined | GREIT | 11 |
| Body | 34 | Not defined | CT | 1 |
| Body | 36 | Not defined | MRI | 2 |
| Body | 48 | Not defined | SHA | 4 |
| Body | 64 | Not defined | RMS | 1 |
| Body | 96 | Not defined | MATLAB | 1 |
| Body | 146 | Not defined | FFDNet | 1 |
| Body | 174 | Not defined | GB | 1 |
| Body | 288 | Not defined | NSTC | 3 |
