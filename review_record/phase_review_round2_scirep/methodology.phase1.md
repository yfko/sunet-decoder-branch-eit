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
