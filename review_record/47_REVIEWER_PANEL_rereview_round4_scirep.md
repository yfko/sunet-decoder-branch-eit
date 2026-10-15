[LEGACY-NO-CONTRACT]

# Verification Review Report — academic-paper-reviewer · re-review · revision round 4 (Sci Rep) · `41_DRAFT_v5.md` (sha256 3c0451dfbfd5…) · 2026-10-08

**Why this round was run.** The round-3 re-review (`38_`) judged v4. Round 4 changed 11 blocks of v4 into v5 and no independent review of v5 existed afterwards, only the authors' own `44_`. Under the lab rule that an independent review follows every substantive change before readiness is declared, the PI decided on 2026-10-08 to run this re-review before submission. Object: v4 → v5 against the round-4 roadmap (REV-R4-1…7, transcribed from `38_` §Residual Issues and NEW-1…4; 0 must_fix, 6 should_fix, 1 consider).

**Why legacy.** Same reason as `38_`: the current 1.1 contract hard-requires a `revision-evidence-bundle/1.0` chained from an `integrity-pass-receipt/1.0` issued by `integrity_verification_agent` (pipeline Stage 2.5). This project never ran Stage 2.5; its reference integrity is carried by the R12d pipeline (`tools/cite.py`, Crossref/PubMed field-by-field) and by `academic-paper` citation-check (`42_` for v5), neither of which issues that receipt. The receipt was not fabricated and Stage 2.5 was not run retrospectively (a separate, unrequested job), so `scripts/revision_roadmap.py validate-bundle` was not run and the 1.1 checker would abort at G0. What WAS run, under `ARS_RE_REVIEW_LEGACY=1`: the three-gate discipline in three separate fenced sub-agent calls (Phase 1 revision-blind → Phase 2A letter-blind → Phase 2B letter-revealed), the legacy 1.0 artifact family (`shared/contracts/re_review/legacy/v1_0/`), and the legacy checker `scripts/legacy/check_re_review_synthesis_v1_0.py`, which hash-chains manifest → precommitment → verdict record → traceability, replays the apply-chain witness and recomputes the §6 decision. Its output (`phase_rereview_round4_scirep/checker_output.txt`): `re-review synthesis ok: round 'sunet-core-rereview-round4-scirep-20261008', revision 1, decision_state 'Minor Revision', apply_chain_witness 'pass'`, exit 0.

## Judge Record (#539)

- **Verification judge**: Claude Fable 5.1 (the session's own model), executed as three separate sub-agent contexts dispatched by the main session (the orchestrating layer), one per gate. Each saw only what the withholding matrix allows (Phase 1: no manuscript, no patch, no letter; Phase 2A: manuscripts, patch and apply report, no letter; Phase 2B: everything including `44_`). The main session wrote none of the verdicts; it emitted the manifest, validated each gate's artifact against the legacy schema and bindings before dispatching the next, ran the checker, and wrote this header.
- **Round-1 panel provenance**: `review-panel-provenance/1.0`, `phase_review_round2_scirep/provenance_artifact.json`, raw artifact sha256 `dc8fea76b4f22f52fe6d37bd33f84f285081de4201e23ef68a1962d6df04f3ed`; normalized_manifest_sha256 `e31b4ae4039d9ea3be36f6a89a5affc829a131d6430e490063fbccb2cbc9db6a`; execution_topology_sha256 `5f6b97561e1c1c6cfd9621d5a99af9285aa22e1caba6452d974528f4612285b0`; six axes: role_separated true, fresh_context true (within_panel_attempt_only), blind_to_peer_outputs true, model_family_distinct false, provider_distinct false, human_distinct false. Digests re-read from the carrier on 2026-10-08 and equal to those recorded in `38_`; the replay validator was run by the round-2 session on 2026-10-06 (`33_` header), not re-run here.
- **Blind cross-model pass**: not_configured — single-family disclosure below applies to the whole run (no must_fix rows exist to carry the per-row marker).
- **Pre-committed criteria**: precommitment JCS sha256 `55655305a45a71c2f99538a8d7dc7472cbfcdd05942f27b24f0555a2dea526c9` (`phase_rereview_round4_scirep/precommitment.json`; input_manifest_hash `59e392ca349a391363dadd0cb2b19d27fecde18d53a4c6c5e35da1d2562b87d0`). Verdict record JCS sha256 `671b5a8a6f287cdb5a19aede036a6664a616628116425f6d243cd8c579b50d6a`. Traceability JCS sha256 `ef2755ae2b3aa8c739d378c273fd286548b652897efbc13944d82ab0e2c4c789`.
- **Prompt/rubric surfaces**: `references/re_review_mode_protocol.md` §§ Three-Gate Orchestration, Phase 1/2A/2B, Decision Derivation, New-Issue Attribution, Verifier Routing, Output Format; legacy 1.0 schemas; ARS 3.23.0.
- **Reviewer configuration**: `round1_cards_reused` — the five round-2 Phase 1 cards (`phase_rereview_round4_scirep/round2_config_cards.md`, byte-identical copy of the file used by `38_`); `field_analyst_agent` not re-run; target venue unchanged (Scientific Reports).
- **Routing**: `card_mapped` — REV-R4-1/3/4 → R1 (methodology); REV-R4-2/5/6 → EIC (Journal-Fit); consider REV-R4-7 → EIC by definition. DA seat not a verification persona.
- **Apply-report chain**: `pass` — one report (`41_DRAFT_v5.md.apply-report.json`, format 1.3, patch_digest `7ec1ea11…` = sha256 of `phase6_revision/revision_patch_round4.json`), base `67570787bd55` = sha256 prefix of `34_DRAFT_v4.md`, output `3c0451dfbfd5` = sha256 prefix of `41_DRAFT_v5.md`; authorization witness PASS; 116/127 blocks byte-identical (re-diffed by the 2A seat).
- **Criteria layer**: `[CRITERIA-LAYER-ABSENT: no Required Item Details blocks]` — the "letter" of this round is `38_` (a re-review report), which carries no R<n> blocks; level 1 (roadmap `verification_criteria`, verbatim) governed every record. The checker printed the corresponding NOTE.
- **Evidence seen by the judge**: Phase 1: legacy-form roadmap, `38_`, cards, manifest. Phase 2A: + `34_DRAFT_v4.md`, `41_DRAFT_v5.md`, patch, apply report, `43_`, `42_`, Table S9 and `tools/make_table_s9.py` (replayed `--check` read-only), `refs/overrides.json`, per-seed CSVs as needed. Phase 2B: + `44_RESPONSE_TO_REREVIEW_round4.md` (untrusted persuasion). No gate read `NOTES_*`, `45_`, `46_`, `47_`, `48_` or the author sidecar.
- **Orchestrator interventions after commitment**: none. Each artifact passed schema validation and binding checks as emitted; the checker passed on the first run. (The 2A seat disclosed that it reordered its own records to roadmap source order before committing, with content asserted byte-identical; that happened inside the 2A call, before `[EVIDENCE-COMMITTED]`.)
- **Judging budget**: three sub-agent calls, about 123k + 216k + 205k tokens (Phase 1 / 2A / 2B), separate from the revision.

This verification round ran on the same model family that drove the revisions; over-optimization to this judge's latent biases is possible (Ren et al. 2026, arXiv:2607.13104 §8.1.2). The Phase 1/2A/2B calls were separate contexts from the session that wrote the round-4 patch and `44_`, but not a different model family; the PI's own read and the real Sci Rep review remain the independent checks.

---

# Re-review report — SUnet core paper, round-2 panel (Sci Rep), revision round 4 (Phase 2B body, as emitted)

Round `sunet-core-rereview-round4-scirep-20261008`, #576 three-gate contract, legacy v1.0 artifact family. Phase 2B integration by the Journal-Fit seat (EIC) over the committed Phase 2A record (JCS sha256 `671b5a8a…`; precommitment `55655305…`). Original manuscript `34_DRAFT_v4.md`; revised manuscript `41_DRAFT_v5.md`; deliverable `43_SUBMISSION_scirep_v5.md`; response letter `44_RESPONSE_TO_REREVIEW_round4.md` (read as data, used to fill the author-claim column and to look for evidence 2A might have missed; nothing in it changed a verdict).

## Decision

**Minor Revision** (rule B5).

No must_fix items in this roadmap. Six should_fix items: all FULLY_ADDRESSED. One consider item: FULLY_ADDRESSED. Five new issues, all minor: one attributed to the revision (NEW-1, the minus-sign glyph in the rewritten §3.2 paragraph), four previously missed (NEW-2…5). No MADE_WORSE, NOT_ADDRESSED or CANNOT_VERIFY; no adjustment, no dissent, no escalation. The single minor regression is the only operand that keeps the decision off Accept.

## Revision Response Checklist

Author triage: every item `will_address` (letter header, PI 2026-10-07). Concern numbers follow the roadmap's source order.

### must_fix — Required Revisions

None in this roadmap (obligation_counts.must_fix = 0). The must_fix table, the per-item decision operands and the cross-model column are therefore empty; B2 cannot trigger.

### should_fix — Suggested Revisions

| Transport ref | Original Review Comment | Author triage | Author's Claim | Response Status | Revision Location | Verified? | Quality Assessment |
|---|---|---|---|---|---|---|---|
| S1 REV-R4-2 (EIC) | Residual of REV-R3-6 + NEW-1: C_wide − C without an interval; 35–25 dB values only in S9; "the capacity control removes 0.12 points of it at most" is direction-reversed | will_address | B0127 rewritten from the script-generated S9: C_wide − C +0.034 (CI −0.387 to +0.452, 28/58) with a pointer to S9 for 35–25 dB; reversed sentence replaced by "adds between 0.01 and 0.12 points to it … and removes none of it"; script cited; 37_'s S9 intervals superseded | FULLY_ADDRESSED | §3.2 B0127 (op 5); Table S9 and B0083 comparison surfaces | YES | Letter matches the text sentence for sentence and the quoted interval matches B0127 and Table S9 row 20 dB. Two letter-vs-text discrepancies, neither verdict-bearing: the letter writes U+2212 where the text has ASCII hyphens (NEW-1); "differ in the third decimal" understates the regenerated endpoints, which move by up to 0.013. No adjustment. |
| S2 REV-R4-5 (EIC) | NEW-3 of round 3: "Three of the fifty-three" in §4.3 and Competing interests against a 54-entry list | will_address | B0060, B0070: fifty-three → fifty-four | FULLY_ADDRESSED | §4.3 B0060; Competing interests B0070 | YES | Both blocks say fifty-four; list B0075 has 54 entries; 43_ lines 164 and 300 agree; 42_ records 54 keys, self-citation 3/54. No adjustment. |
| S3 REV-R4-6 (EIC) | NEW-4 of round 3: §1 "named in Section 4.4" points at a list §4.4 does not contain | will_address | B0013 sentence replaced by one naming the three untested conditions with a parenthetical pointer to §4.4 | FULLY_ADDRESSED | §1 B0013; §4.4 B0062 unchanged | YES | The letter's replacement sentence is verbatim in B0013; route (a) of the committed pattern met; the pointer now resolves to the first three limitations §4.4 discusses. No adjustment. |
| S4 REV-R4-1 (R1) | Residual of REV-R3-1: §4.2 B0056 apportions ("belongs mostly to the training condition"); §4.1 B0051 "this prediction does not hold once … matched" reads as a matched-condition refutation | will_address | B0056 tail → "a benefit that did not survive training at the heavier level"; B0051 clause → "the condition of this prediction is absent once training and evaluation are matched, so the prediction is not tested there" | FULLY_ADDRESSED | §4.1 B0051; §4.2 B0056; B0050, B0052–B0055 byte-identical | YES | Both before/after pairs are exact quotations of v4 and v5. 2A's three tests over every sentence of §4.1–4.2 pass on the same text. The letter is silent on B0053's "decided most of what happened" (NEW-3, previously missed). No adjustment. |
| S5 REV-R4-3 (R1) | Residual of REV-R3-9: Bonferroni reference for the 35 dB onset; D − B and the per-seed slope in the §2.6 unregistered list; D − B marked descriptive in §3.1; floor-independence of the 9.2-fold shrinkage in §3.5 | will_address | B0028 Bonferroni sentence (p = 0.0011 < 0.05/7 = 0.0071); B0034 D − B at 40 dB and the per-seed slope added; B0037 "descriptive, not a registered rule"; B0122 shrinkage "does not depend on the floor" | FULLY_ADDRESSED | §2.4 B0028; §2.6 B0034; §3.1 B0037; §3.5 B0122 | YES | All four statements present at the stated blocks; 2A recomputed 0.05/7 and 2.097/0.229. The letter's "D − B at 40 dB" is accurate and, beside its own S1 row, exposes the sweep-level gap NEW-4 names. No adjustment. |
| S6 REV-R4-4 (R1) | NEW-2 of round 3: "shrinks by only 0.03 points when the 38% larger B_wide replaces B" has the wrong direction | will_address | B0037: "shrinks by only 0.03 points" → "grows by 0.03 points, to +0.223"; 38% (B_wide/B) and S9's +39% (D/B) are different ratios, both correct, neither changed | FULLY_ADDRESSED | §3.1 B0037 one clause | YES | Replacement clause verbatim in B0037, agreeing with Table 1 and S9 (+0.191, +0.223). The ratio claim recomputes from Table 1's parameter counts: 10,743,738/7,762,498 = 1.384 and 10,811,298/7,762,498 = 1.393. No adjustment. |

should_fix_addressed_rate = 6/6 = 100%.

### consider — Nice to Fix

| # | Original Review Comment | Author triage | Author's Claim | Response Status | Revision Location | Verified? | Quality Assessment |
|---|---|---|---|---|---|---|---|
| N1 REV-R4-7 (EIC) | Residual of REV-R3-13: deposit decision for the rule-bearing checkpoints not recorded in Data Availability | will_address | B0072: checkpoints "are not deposited in a public archive because of their size and are available from the corresponding author on request"; PI decision 2026-10-07, no Zenodo deposit | FULLY_ADDRESSED | Availability B0072 one sentence | YES | Sentence present in B0072 and 43_ line 176; states decision, reason and route. Criterion applied as not_precommitted at 2A (consider item); decision-inert. No adjustment. |

## Adjustments (Phase 2A → final)

None. Every final verdict equals its Phase 2A verdict; the letter located no evidence 2A had missed (all seven items were already FULLY_ADDRESSED), contained no rebuttal, and revealed no misidentified target, so no basis in the closed set applies. `adjustments: []`.

## Dissent records (Phase 2A)

None. All six precommitted criteria applied as written; REV-R4-7 ran as not_precommitted (consider item, inherited roadmap text).

## New Issues (Discovered During Revision)

Copied unchanged from the committed Phase 2A record (byte-identical in the sidecar; checker-witnessed).

| # | Attribution | Severity | Location | Description |
|---|---|---|---|---|
| NEW-1 | regression (B0127, op 5, REV-R4-2) | minor | §3.2 "B_wide led B by between -0.12 and -0.01 points … (-0.124 points at 20 dB, CI -0.510 to +0.240 …)" | The rewritten paragraph writes its five negative numbers with ASCII hyphen-minus while every other block uses U+2212 (v4 B0127 did too); 43_ line 120 carries the hyphens. D5 typographic consistency; no number or conclusion affected. |
| NEW-2 | previously_missed (B0028 resample sentence unchanged; S9 caption said 20,000 on 2026-10-06) | minor | §2.4 "all bootstrap intervals use 100,000 resamples of the 58 seeds" | Table S9 and the §3.2 intervals quoted from it are 20,000-resample values (`make_table_s9.py`, default_rng(0)); D − B_wide at 20 dB therefore appears with two seed-level intervals (+1.642/+2.543 in §3.2, §3.5, Tables 2–3; +1.639/+2.539 in S9). Third-decimal differences; the Methods sentence is not true of every interval. |
| NEW-3 | previously_missed (B0053 byte-identical v4→v5) | minor | §4.1 "the training level, not the architecture, decided most of what happened" | Licensed as a statement about the control arm's 8.8-point loss and recovery; readable as a ranking of the two readings of the 2.097-point benefit, which §4.1 says the design cannot make. Not apportionment under REV-R4-1 test (a); the ambiguity the panel removed elsewhere. |
| NEW-4 | previously_missed (v4 B0127 already reported sweep-level D − B; B0034 listed none) | minor | §2.6 "the contrast of D against the unwidened arm B at 40 dB (Section 3.1)" | §3.2 and Table S9 report D − B across the whole sweep with intervals; §2.6 lists it only at 40 dB, whereas the neighbouring B, C, C_wide contrasts are listed "at 40 dB and across the sweep". One-phrase completeness gap. |
| NEW-5 | previously_missed (B0004, B0066, B0068, B0081 and the untouched part of B0072, all byte-identical v4→v5) | minor | Availability "[REPOSITORY URL AND TAG: to be frozen at submission]" and six other bracketed fields | Author-supplied placeholders in the draft body (affiliation, e-mail, funding, roles, caption, URL/tag, "accessed September 2026"). Known pre-submission fill-ins, not scientific defects. |

## Decision Rationale

Gates: G0 — manifest complete, hashes bound (original, revised, roadmap, letter, patch, apply report, decision letter, cards), apply_chain_witness pass; not fired. G1 — no row with final_verdict ≠ phase2a_verdict; not fired. G2 — no dissent, no cross-model divergence (cross_model_active false), no pending escalation, no CANNOT_VERIFY reapplication; not fired.

Base decision, rules in order, first match:

- B1: no must_fix MADE_WORSE; no critical regression (NEW-1 is minor) — not fired.
- B2: zero must_fix items — does not trigger by definition.
- B3: no must_fix in {NOT_ADDRESSED, MADE_WORSE, CANNOT_VERIFY}; no major regression — not fired.
- B4: no PARTIALLY_ADDRESSED row with a must_fix residual — not fired.
- **B5 fires** on one operand: a regression-attributed new issue with severity minor (NEW-1). The other operands are inert: no must_fix PARTIALLY_ADDRESSED; should_fix_addressed_rate = 6/6 = 100%; no should_fix MADE_WORSE.
- B6 not reached.

Floors: no approved escalation exception; decision_state = base = Minor Revision. reject_recommended false.

Verdict counts over final verdicts — must_fix 0/0/0/0/0, should_fix 6/0/0/0/0, consider 1/0/0/0/0 (FULLY/PARTIALLY/NOT/WORSE/CANNOT). Residual-magnitude counts all zero. Zero adjustments. Regressions: NEW-1 (minor). Non-regression new issues: NEW-2, NEW-3, NEW-4, NEW-5 (goalpost guard: decision-inert). apply_chain_witness pass (`41_DRAFT_v5.md.apply-report.json`, 11 ops, 116/127 blocks byte-identical, authorization witness PASS, no structural flag).

## Commitment Ledger Verification (Kong A1)

The roadmap carries no `commitment_extracted` list on any item and the letter is a seven-row change table without commitment objects, so the ledger is empty: nothing to verify, no `fulfillment_status` to assign, and no `COMMITMENT_GAP` or `EVIDENCE_TYPE_UNSPECIFIED` advisory can arise. The verdict axis above is the whole of this round's verification.

## Residual Issues

In the authors' terms, patch-ready. Item 1 is the one regression and the only thing between the manuscript and Accept on the committed criteria; items 2–5 are previously-missed and decision-inert (they would enter a next roadmap as consider items, or can be taken now at the authors' discretion); items 6–7 are outside the scored criteria.

1. **NEW-1, B0127 (§3.2), five glyphs.** Replace the ASCII hyphen-minus with U+2212 (−) in exactly five places: "between −0.12 and −0.01 points", "(−0.124 points at 20 dB, CI −0.510 to +0.240", and "CI −0.387 to +0.452". That restores the convention v4's B0127 used ("−0.12 and −0.01", "−0.124", "CI −0.499") and the rest of the paper uses (§3.1 "CI −0.011", §3.5 "Δ = −0.002", "−1.868"). B0127 is the only block of 41_ with an ASCII minus before a digit; the same five glyphs sit on 43_SUBMISSION_scirep_v5.md line 120 and will follow on re-render. (The table rows of 43_, lines 330–377, also print ASCII hyphens because results/tables/*.md do; that is a table-file convention 2A did not raise and is not part of this item.) Closing this item alone moves the decision to Accept under B6.
2. **NEW-2, B0028 (§2.4), one clause.** "all bootstrap intervals use 100,000 resamples of the 58 seeds" is not true of Table S9 or of the four §3.2 width-contrast intervals quoted from it (20,000 resamples, `tools/make_table_s9.py`, default_rng(0)). Either qualify the sentence ("… except Table S9 and the §3.2 contrasts drawn from it, which use 20,000") or set N_BOOT = 100000 in the script, regenerate S9, and re-quote B0127. Decision-inert; previously missed.
3. **NEW-3, B0053 (§4.1), one sentence.** "the training level, not the architecture, decided most of what happened" — tie it to the measured quantity so it cannot be read as apportioning the 2.097-point benefit, e.g. "decided most of the control arm's loss and recovery" or "decided most of what happened to the control arm". Decision-inert; previously missed.
4. **NEW-4, B0034 (§2.6), one phrase.** "the contrast of D against the unwidened arm B at 40 dB (Section 3.1)" → "the contrast of D against the unwidened arm B at 40 dB and across the sweep (Sections 3.1 and 3.2, Supplementary S9)". Decision-inert; previously missed.
5. **NEW-5, 41_ back matter.** The bracketed placeholders in B0004, B0066, B0068, B0072 and B0081 are filled in the deliverable 43_ (lines 11–13, 96, 100, 176, 292, 296, 321) but not in the draft; either carry AUTHOR_FIELDS into 41_ or record that 43_ is the submission surface and 41_ the hashed draft. Decision-inert; previously missed. Note 41_ B0066 "accessed September 2026" against 43_ "September and October 2026".
6. **Outside the scored criteria — reference renderings and AI statement.** All five items the letter reports done are visible in 43_: Lakens 2013 article number 863 (line 270); Ronneberger 2015 LNCS 9351 (line 266); Herzberg 2023 title without "⋆" (line 226); Xin 2022 full title (line 246); Vandenhende 2020 author order Van Gool, De Brabandere (line 238, sourced in refs/overrides.json to the BMVC accepted-papers list, Crossref and Semantic Scholar). AI-use statement "accessed September and October 2026" (line 100). Nothing to do.
7. **Outside the scored criteria — repository tag.** 43_ lines 96 and 176 print "tag v1.1-submission"; by the letter the tag is still to be pushed by the PI. The deliverable asserts a tag that does not yet exist; push it before submission.

## Post-letter observations

- Letter header vs apply report: 11 ops, 116/127 byte-identical, no structural flag, 67570787bd55 → 3c0451dfbfd5, witness PASS — all match. The report also carries `unregistered_claim_drift_review_required: true` (0 registered claim surfaces checked), which the letter does not mention; the ops declare no claim-strength changes and the verdicts were made on the text, so this is a provenance note.
- Table S9 regeneration: "means and lead counts identical" is exact (35/35 cells); "intervals differ in the third decimal" understates it — endpoints move by up to 0.013 (B_wide − B at 20 dB −0.499 → −0.510; C_wide − C −0.385/+0.445 → −0.387/+0.452; C_wide − B_wide +0.003/+0.851 → +0.005/+0.862). §3.2 quotes the script values throughout, so no manuscript number is affected. The 38_ Residual Issue 3 reference values inherited into the Phase-1 operationalization are the superseded ones; 2A scored under equivalence, so the letter's "superseded" note changes nothing.
- REV-R4-2 / NEW-1: the letter writes its negative numbers with U+2212 ("CI −0.387 to +0.452") while the sentence it describes uses ASCII hyphens; the letter is right and the text is not, and the authors evidently did not notice the glyph change.
- NEW-1 scope: ASCII hyphens are confined to B0127 in 41_ (v4 had none), but 43_'s table rows (lines 330–377) also print them from the results/tables sources; the B0127 fix aligns the prose, the tables are a separate convention, noted not scored.
- NEW-2: the letter's header documents the discrepancy NEW-2 names without noticing it — S9 from the script (20,000 resamples), "the script's values are the ones cited in §3.2", while §2.4 still promises 100,000.
- NEW-3: the letter does not mention B0053; its REV-R4-1 row treats the two named blocks as the whole residual.
- NEW-4: the letter's REV-R4-3 row ("D − B at 40 dB … added") and REV-R4-2 row (D − B "level for level" in B0127) together show the gap without connecting them.
- NEW-5: every placeholder is filled in 43_ (affiliation, e-mail with ORCID, NSTC grant numbers, CRediT roles for all three authors, Fig. 4 caption, repository URL and tag) but not in 41_; "accessed September and October 2026" likewise exists only in 43_. The draft and the deliverable diverge in the back matter.
- Reference renderings and the Xin note: all five visible in 43_ as the letter says; refs/overrides.json carries the three new overrides with sources. The claim that the round-3 Xin note "rested on a truncated line" is consistent with the full title now visible; 36_ was not re-read to confirm.
- Repository tag: asserted in 43_, "to be pushed by the PI" per the letter; outside scoring, cannot be checked from these inputs.
- "28 pages": the PDF has 28 pages. "The 2025 reviewer-comment mapping table is not attached to the cover letter" concerns 40_, not an input here, not checked.
- The letter cites `revision-authority-round4/roadmap.json`; this phase used the legacy transcription `roadmap_legacy_v1_0.json` (sha256 53a67534…) of the same seven items. The patch and apply report bind the revision-authority roadmap (959765cb…), covered by the manifest's apply_chain_witness pass; the directory was not read.
- Commitment ledger empty (see above).
- No sentence in 44_ is directed at the reviewer or instructs an action; "to be pushed by the PI" describes the authors' own pending step.


## Attachment: Acronym Check (advisory, #849)

Not re-run for this re-review (the protocol reads the round-2 attachment as input 7; it adds no criterion). The round-2 attachment in `33_` stands; the 11 round-4 ops introduced no new acronym (2A collateral check).

## Orchestrator notes (main session, 2026-10-08; not part of any verdict)

- **Residual item 7 (repository tag)** is already closed: the PI pushed `v1.1-submission` → `058731e` on 2026-10-07 (recorded in `NOTES_2026-09-22.txt`, verified by `tools/ready_gate_scirep.py` against GitHub). The 2B seat could not know this because the notes were withheld; `44_` was written before the push.
- **NEW-5 (placeholders in `41_`)** is the pipeline's design, not an omission: `41_` is the hashed draft with `AUTHOR_FIELDS.json` placeholders, and `tools/format_convert_scirep.py` fills them when producing `43_` (the submission surface). The seat's alternative "record that 43_ is the submission surface and 41_ the hashed draft" is exactly the standing arrangement. Decision-inert either way.
- **NEW-1 scope**: confirmed by the main session — v4's B0127 used U+2212 in all four places; v5's B0127 uses ASCII hyphen-minus in five; no other block of `41_` has an ASCII minus before a digit. The table rows of `43_` (lines 330–377) carry ASCII hyphens in both the v4 and v5 deliverables (9 and 10 lines respectively), from `results/tables/*.md`; pre-existing, outside this item.
- All text changes implied by the Residual Issues go to the PI as triage; nothing in the manuscript, the deliverable or the cover letter was changed by this session.


---

## Addendum (2026-10-08): scoped re-verification of revision round 5 (v5 → v6)

The PI took NEW-1, NEW-2 and the `48_` §5(b) correction in a round-5 patch (`revision-authority-round5/`, `phase6_revision/revision_patch_round5.json`, `49_DRAFT_v6.md` sha256 `88e888906638…`, apply witness PASS, 124/127 byte-identical). Because the change is three blocks, the orchestrating session dispatched one scoped seat-verifier call (Phase 2B′ shape, fresh context, read-only) instead of a full three-gate round; the full round above remains the review of record for v5. Machine record: `phase_rereview_round4_scirep/addendum_v6.json` (canonical sha256 `6cef901912ccd4154084fe008a300485e8a74021aeee0c7b2ba7fd86e6fc3390`), binding original `3c0451dfbfd5…` and revised `88e888906638…`. Result: **Accept** — REV-R5-1, -2, -3 FULLY_ADDRESSED, no new issue. The readiness gate reads this addendum when the current draft is no longer the v5 the full round judged.

# Addendum to the round-4 re-review: verification of revision round 5 (v5 → v6)

Addendum for round `sunet-core-rereview-round4-scirep-20261008`. Scoped seat-verifier call (Phase 2B′ shape), fresh context, 2026-10-08. Judge: Claude Fable 5.1. Read-only on the manuscript; this call emits only `addendum_v6.json` (canonical sha256 `6cef901912ccd4154084fe008a300485e8a74021aeee0c7b2ba7fd86e6fc3390`) and this file.

Object: `41_DRAFT_v5.md` (sha256 `3c0451dfbfd5dce97ae9dac88a0273d9c39943752f5c6f05adfe0b6be50d6b9d`) → `49_DRAFT_v6.md` (sha256 `88e888906638e42218070ad45a9acc7617f5538024cd4a3e80736ffa42fc1ea2`), judged against `revision-authority-round5/roadmap.json` (three items: REV-R5-1 B0127, REV-R5-2 B0028, REV-R5-3 B0066). Patch `phase6_revision/revision_patch_round5.json` sha256 `8c8951fc8a1b977f0b7d0ec8575c7a36ee37d90dbd9eedb847e69509b2c13a07`; apply report `49_DRAFT_v6.md.apply-report.json` sha256 `005044f0c8b486ed65197c869f636e72fc74a86c7585538d89a13f84f6434f28`.

## Decision

**Accept.** All three roadmap items are FULLY_ADDRESSED and the three operations introduced no regression. Rule fired: the Accept rule of the round-4 re-review (47_ §Residual Issues: closing NEW-1 alone moves the decision to Accept under B6); Minor Revision (B5) is not triggered. Verdict counts: FULLY 3 / PARTIALLY 0 / NOT 0 / WORSE 0 / CANNOT 0.

## Per-item verdicts

| Item | Block | Verified by | Verdict | What changed | Evidence in v6 |
|---|---|---|---|---|---|
| REV-R5-1 (should_fix) | B0127 §3.2 | EIC | FULLY_ADDRESSED | Exactly five `-` → `−` (U+2212) replacements before digits; nothing else in the block changed. | "between −0.12 and −0.01 points … (−0.124 points at 20 dB, CI −0.510 to +0.240 …" and "CI −0.387 to +0.452". Regex `-\d` finds 0 matches in v6 B0127; U+2212 count is 5 (v5: 0); the digit string of B0127 is identical between v5 and v6. The five values match Table S9 row 20 dB. |
| REV-R5-2 (consider) | B0028 §2.4 | R1 | FULLY_ADDRESSED | "all bootstrap intervals use 100,000 resamples of the 58 seeds" → "the bootstrap intervals use 100,000 resamples of the 58 seeds, except those of Table S9 and of the width contrasts in Section 3.2 drawn from it, which use 20,000 (`tools/make_table_s9.py`)". | `tools/make_table_s9.py` line 20: `N_BOOT, SEED = 20000, 0`; Table S9 caption: "(20,000 resamples)". The four S9-derived intervals in B0127 (−0.124 [−0.510, +0.240]; +0.034 [−0.387, +0.452]; +1.973 [+1.616, +2.327]; +0.425 [+0.005, +0.862]) equal the table's row 20 dB. The other three sentences in v6 that mention resampling (H3 rule, §3.5 geometry-level interval at 100,000, §3.5 Δ_20\|20 − Δ_20\|40 "seeds resampled in pairs") are unchanged from v5 and do not contradict the clause. |
| REV-R5-3 (should_fix) | B0066 §2.9 | EIC | FULLY_ADDRESSED | Parenthetical "Fable 5.1 and Opus 5, accessed September 2026" → "Fable 5.1, Opus 5 and Opus 5.5, accessed August to October 2026" (option (i) of 48_ §5(b), PI's choice). Character diff is confined to the parenthetical; the remaining four sentences and the FUNDING placeholder are byte-identical to v5. | Opus 5.5: `NOTES_2026-09-22.txt` L611 (2026-10-03 RECON scoring) and L914 (2026-10-07 submission day). August: `NOTES_2026-09-01.txt` L60 (`Nov142025/ARS_Review_2026-08-27/`) and `NOTES_2026-09-18.txt` L11, L14 (preregistrations 2026-08-28 and 2026-08-29). October: the 10-03 and 10-07 sessions above. |

Note on REV-R5-3: the "Opus 5" label rests on the PI's attestation under option (i). NOTES record "Opus 5" only as a planning principle (L76) and a hand-off header (L262), not as a post-hoc session record; 48_ §5(b) stated this and offered option (ii) for the case it cannot be confirmed. The roadmap criterion asks for the chosen labels and period, and they are present verbatim. This is not a residual gap of the item.

## New issues

None. The three replace_block operations are confined to the glyphs, one clause and one parenthetical named in the roadmap; no number, claim or reference changed.

Two observations, decision-inert, not recorded as issues:

- §2.4 B0028 calls all four S9-derived §3.2 intervals "width contrasts"; two of them (D − B, C_wide − B_wide) are the branch and late-split contrasts of the same width paragraph. The wording follows the roadmap and 47_ NEW-2 and the paragraph's own framing ("Decoder width on its own does not reproduce the advantage"); the statement of which intervals use 20,000 is accurate.
- The registered D − B_wide interval at 20 dB is quoted in §3.5 as +1.642 to +2.543 (100,000 resamples) while Table S9 prints +1.639 to +2.539 (20,000). B0127 quotes only the point estimate +2.097 from S9, so the amended clause describes both correctly.

## What was checked

1. Hashes: sha256 of `41_` and `49_` match the apply report's `base_draft_hash` (3c0451dfbfd5) and `output_draft_hash` (88e888906638); sha256 of the patch file equals the report's `patch_digest`; `roadmap_sha256` in the report equals the sha256 of the roadmap file in the witness.
2. Block diff (markers `<!--block:BNNNN-->`): 127 blocks in both files, same order, no duplicate ids, identical preamble; exactly B0028, B0066 and B0127 differ; 124 blocks byte-identical. The patch's three `new_text` payloads equal the corresponding v6 blocks.
3. REV-R5-1: regex for ASCII hyphen-minus before a digit over B0127 (0 hits) and over the whole of v6 outside code spans and paths (0 hits); U+2212 count; digit-string equality v5 vs v6; difflib opcodes.
4. REV-R5-2: `N_BOOT` in `tools/make_table_s9.py`; Table S9 caption and row 20 dB; every sentence in v6 containing "resampl", "100,000" or "20,000"; the four B0127 intervals against the table; §3.5's registered interval.
5. REV-R5-3: exact parenthetical string; difflib opcodes of B0066; NOTES greps for "Opus 5.5", "Fable", "Opus 5" in `NOTES_2026-09-22.txt` and for "08-27", "08-28", "08-29" in `NOTES_2026-09-01.txt` and `NOTES_2026-09-18.txt`; 48_ §5(b) option (i); 47_ §Residual Issues items 1–2.
6. Not read, by instruction: `52_*`, `50_*`, `51_*`, `45_*`, `46_*`, `NEXT_SESSION_PROMPT_*`. Previously-missed issues (47_ NEW-3, NEW-4, NEW-5) were out of scope and were not re-examined.

## Disclosure

This verification round ran on the same model family that drove the revisions; over-optimization to this judge's latent biases is possible (Ren et al. 2026, arXiv:2607.13104 §8.1.2).

