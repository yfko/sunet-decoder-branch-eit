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
