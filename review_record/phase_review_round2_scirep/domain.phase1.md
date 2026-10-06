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
