[LEGACY-NO-CONTRACT]

# Verification Review Report — academic-paper-reviewer · re-review · Round 1 → revision 1 · `15_DRAFT_v2.md` · 2026-09-26

Why legacy: the Round-1 panel (`12_REVIEWER_PANEL_round1.md`) was a standalone full review with markdown output, not a pipeline stage; no Material Passport, no integrity-PASS receipt and therefore no `revision-evidence-bundle/1.0` exist. The current contract hard-requires the bundle and forbids a silent fallback, so this re-review runs the documented single-pass path and says so. The revision itself was patch-applied under the current #670 authority chain (roadmap transcribed from the Round-1 letter, PI triage as explicit author sidecar, apply report 1.3 with authorization witness PASS), and that chain is what this report verifies against.

## Judge Record (#539)

- **Verification judge**: Claude Fable 5.1, the session's own model.
- **Round-1 panel provenance**: `review-panel-provenance/1.0` was not emitted by the standalone Round 1; the letter's own provenance table records role-separated = true, context separation = false, peer-blind = false, model-family distinct = false, provider distinct = false, human-reviewer distinct = false. Copied here as recorded; no digest to verify.
- **Blind cross-model pass**: not_configured — single-family disclosure applies to every row.
- **Pre-committed criteria**: none (legacy — no contract). The verification criteria used are the `verification_criteria` strings of the Round-1 roadmap items as transcribed in `revision-authority/roadmap.json`, which were fixed before this revision was written.
- **Prompt/rubric surfaces**: `references/re_review_mode_protocol.md` § Decision Derivation, § New-Issue Attribution, § Output Format; roadmap item verification criteria.
- **Reviewer configuration**: `round1_cards_reused` (Phase 0 table of `12_REVIEWER_PANEL_round1.md`; field_analyst not re-run).
- **Routing**: `card_mapped` — R1/R4/S1/S2 → methodology seat; R2/S3/S4 → domain seat; R3/S5 → Journal-Fit seat; R6/S6 → perspective seat; R1 (M1)/R5 (M2) → DA seat.
- **Apply-report chain**: pass — one report; `base_draft_hash e373aebf85a7` equals the SHA-256 prefix of `06_DRAFT_v1.md` (anchored), `output_draft_hash f5448863b24a` equals the SHA-256 prefix of the handed `15_DRAFT_v2.md`; authorization witness PASS; 86/114 blocks byte-identical; structural flags acknowledged (section_count_delta +2, five heading ops).
- **Evidence seen by the judge**: revised manuscript, original manuscript, roadmap JSON, apply report, `RESULTS_STUDY2.md` §十, `results/manuscript_numbers.json`, `results/tables/table3_retrained_20db.md`, `PREREGISTRATION_HEART.md` §9; the Response to Reviewers was written in the same session and offers no persuasion-blindness.
- **Judging budget**: one pass over the changed blocks and the unchanged blocks they reference; number checks delegated to `tools/verify_manuscript_numbers.py` (all reported values reproduced from per-seed files).

This verification round ran on the same model family that drove the revisions; over-optimization to this judge's latent biases is possible (Ren et al. 2026, arXiv:2607.13104 §8.1.2). Stronger than that: the judge is the same session that wrote the revision. This report is a structured self-audit; the PI's own read and the journal's review are the independent checks.

## Decision

**Minor Revision** — every must_fix item is FULLY_ADDRESSED and verified against the revised text; one regression introduced by the revision (manuscript length against TMI's ten-page rule) and the author-supplied fields remain.

## Revision Response Checklist

### must_fix — Required Revisions

| Transport ref | Original Review Comment | Author triage | Author's Claim | Response Status | Revision Location | Verified? | Cross-model (#539) | Quality Assessment |
|---|---|---|---|---|---|---|---|---|
| R1 | Evaluation-only sweep under 40 dB-trained models; distribution shift and "under threat" not separable; headline generalises beyond the tested condition (R1-W1, DA-M1) | will_address, option (b) | Retrained D and B_wide at 20 dB under a hashed addendum; H5 falsified (Δ_20\|20 = +0.229 vs floor 0.384); headline narrowed per the pre-fixed reading | FULLY_ADDRESSED | Title (B0002); Abstract (B0005); §1 (B0013); §2.3 (B0024); new §2.7 (B0116–B0120); §3.2 (B0040–B0043); new §3.5 (B0121–B0125); §4.1 (B0050–B0053); §4.2 (B0056); §4.4 (B0062); §5 (B0064); Table 3 | ✅ Yes | not_configured | The verification criterion ("retrained contrast reported as its own registered quantity, or claim narrowed") is met on both halves. §2.7 quotes both pre-fixed readings before the result; §3.5 applies the rule as written (falsified on the floor condition, p-condition met) and does not revise it; the secondary comparison (−1.868, CI −2.327 to −1.403) and absolute recovery (8.0 of 8.8 points) are in the registered "reported, not tested" register. Title, abstract, §4.1 and §5 say "trained at 40 dB and evaluated under heavier noise" (six occurrences) and "instrument-realistic" occurs zero times. The 4.1 rewrite states the DA's M1 was correct and names distribution-shift tolerance as the larger part; it does not overstate (keeps "in whole or in part", "mostly", "larger part"). Numbers in §3.5 match `manuscript_numbers.json` and Table 3 to the printed precision. |
| R2 | Temporal (frequency/ECG-gated) separation absent from the framing (R2-W1) | will_address | New §1 paragraph with three verified citations | FULLY_ADDRESSED | §1 second paragraph (B0115) | ✅ Yes | not_configured | Names the three time-series methods the field uses and the template-fitting variant, each sentence anchored to a quoted abstract phrase; scopes the frame-wise approach as neither replacement nor comparison. Claims stay at abstract level. Criterion met. |
| R3 | Contribution framed as an architecture verdict rather than measurement-chain sensitivity (EIC-W1, R3-W2) | will_address | Reframed in §1 last paragraph, §4.1 heading and first paragraph, §5 | FULLY_ADDRESSED | B0013, B0050, B0051, B0064 | ✅ Yes | not_configured | §1 now states "The contribution we claim is not a verdict on the architecture. It is a measurement of how sensitive a post-reconstruction stage is…"; §4.1's heading carries the mismatch framing; §5 closes on chain and training condition together. The reframing is strengthened, not weakened, by the addendum: the sensitivity is now decomposed into a chain part and a training-condition part. Criterion met. |
| R4 | Seed-level intervals describe training-run variability only (R1-W2) | will_address | Sentence in §2.4; geometry-level bootstrap registered in §9.4 and reported in §3.5, Table 3, S8 | FULLY_ADDRESSED | B0028; B0124; Table 3; B0083 | ✅ Yes | not_configured | §2.4 states the scope in one sentence; §3.5 gives both intervals for all three contrasts, correctly notes the geometry-level interval is narrower for the small contrasts and that the seed-level rule is the more conservative; Table 3 carries both columns. Criterion met. |
| R5 | Onset located at grid resolution (DA-M2) | will_address | 35 and 25 dB added; onset reported in two steps; dz peak at 25 dB disclosed | FULLY_ADDRESSED | B0042 (§3.2), B0041, B0045, B0080 (Fig. 3), B0005, B0064 | ✅ Yes | not_configured | Seven levels reported; the two thresholds (detectable 40–35, floor 35–30) are computed from the data (`manuscript_numbers.json` "onset") and the caption says Fig. 3's printed thresholds are computed. The manuscript pre-empts the dz question (peak at 25 dB, scatter doubling at 20 dB). Labelled descriptive throughout; H3 anchors unchanged. Criterion met. |
| R6 | Multi-task learning literature not engaged (R3-W1) | will_address | Sentences in §1 with Vandenhende 2021 and Cipolla/Gal/Kendall 2018; weighting scoped to companion study | FULLY_ADDRESSED | B0011 | ✅ Yes | not_configured | Places shared-encoder/task-specific-decoder design and task interference, names weighting as the remedy, states weighting and branching are two answers to one problem, and scopes weighting out. Criterion met. See NEW-2 on the CVPR entry's author order. |

### should_fix — Suggested Revisions

| # | Original Review Comment | Response Status | Notes |
|---|---|---|---|
| S1 | Report Wilcoxon W and computation method (R1-W3) | FULLY_ADDRESSED | §2.4 (B0028): two-sided, normal approximation with continuity correction, n = 58 > exact limit, no ties, W = smaller signed-rank sum. W given in text for H1 (642), H2 (665), D − B (591), 35 dB (433), H5 (427) and in Table 3. Tables 1–2 do not carry a W column; the text and Table 3 satisfy the request. |
| S2 | Floor rationale into §2.4 (R1-W4) | FULLY_ADDRESSED | B0028 has the rationale; §4.2 (B0055) now points to it. |
| S3 | Source the instrument-realistic 40 dB (R2-W2) | FULLY_ADDRESSED (by removal, with disclosure) | No source exists; the phrase is gone (0 occurrences). §2.3 and §4.1 state "registered primary level, a conservative operating point by the laboratory's convention, not tied to a particular instrument", and §4.1 states the direction of the result for a higher instrument SNR. The reviewer asked for a source or a range; the manuscript gives neither a source (none exists) nor a numeric range, but states the direction of the result, which is what the reader needs. Recorded as addressed on that basis. |
| S4 | Conductivity contrast provenance (R2-W3) | FULLY_ADDRESSED | §2.3 (B0023): registered round-number ratios, not calibrated tissue values; what the results depend on. |
| S5 | Defend simulation-only design (EIC-W2) | FULLY_ADDRESSED | §4.4 third limitation (B0062): registered rules need per-frame ground truth and an exactly settable noise level. |

### consider — Nice to Fix

| # | Original Review Comment | Response Status |
|---|---|---|
| S6 | Operational recipe (R3-W2) | FULLY_ADDRESSED — §4.1 (B0053): measure the reconstructor's image-domain perturbation at the operating SNR, compare with 8.5% median peak fraction, and check whether the deployed network was trained at that level. |

## New Issues (Discovered During Revision)

| # | Attribution | Severity | Location | Description |
|---|---|---|---|---|
| NEW-1 | regression | major | whole manuscript | Sections 1–5 grew from 5,380 to 7,769 words (+44%) with a third table and two new subsections. TMI returns initial submissions over ten pages including references without review. A two-column IEEE estimate for 7,800 words + 4 figures + 3 tables + 19 references is 11–12 pages. Fix: compile, then move material to Supplementary (candidates: Study 1 paragraphs in §2.1 and §3.1, the second half of §2.5, Fig. 4) or tighten §2.7/§3.5. Which material moves is an author decision (Journal-Fit seat). |
| NEW-2 | regression | minor | References, entry for doi:10.1109/cvpr.2018.00781; §1 in-text "Cipolla et al., 2018" | Crossref returns the author order Cipolla, Gal, Kendall; the paper is normally cited as Kendall, Gal, Cipolla. Verify against the paper's first page and correct the registry if Crossref is wrong (domain seat; also logged in `17_CITATION_AUDIT_v2.md` §4.1). |
| NEW-3 | regression | minor | References, Vandenhende 2021 | Rendered from an early-access Crossref record ("2021:1-1"); the final volume/issue/pages must be fetched before IEEE rendering (domain seat). |
| NEW-4 | previously_missed | minor | Keywords (B0006) | "distribution shift" and "training–evaluation mismatch" are now the paper's central concepts and are absent from the keyword list; "measurement noise" alone under-describes the revised paper (perspective seat). Cannot escalate the decision. |
| NEW-5 | previously_missed | minor | Title page, Acknowledgements, CRediT, Availability, Fig. 4 caption | Author-supplied fields still bracketed: corresponding author's affiliation and e-mail, grant numbers, CRediT roles for two authors, repository URL and tag, Fig. 4 printed values. Submission-blocking as a matter of completeness, not of science (Journal-Fit seat). |

Observations (non-defects), DA seat: (i) the matched-training contrasts at 40 dB and 20 dB share a magnitude (0.22–0.23 points) but not a reliability (p = 0.098, dz 0.27 vs p = 0.0009, dz 0.40); the manuscript reports both and applies the pre-registered floor to each, and §4.2's last sentence names the parallel, so the difference is disclosed rather than hidden. (ii) The 9.2-fold figure is a ratio of two means whose denominators are small; the CI on the difference (−2.327 to −1.403) is the load-bearing statistic and is given first. (iii) The title is 37 words; TMI states no limit, but a shorter title carrying the same restriction would read better. None of these is a required change.

## Decision Rationale

All six must_fix items are FULLY_ADDRESSED against their pre-fixed verification criteria; all five should_fix items and the one consider item are addressed. No item was declined. One regression of major severity (NEW-1, venue length rule) and four minor items (two citation-metadata regressions, two previously missed) remain. Under the derivation rules a Major-Revision manuscript whose must_fix set is fully verified and whose only new major item is a venue-conformance regression that needs no new science derives **Minor Revision**. The DA raised no CRITICAL finding.

## Residual Issues (If Any)

1. Manuscript length against TMI's ten-page rule (NEW-1) — author decision on what moves to Supplementary; verify on the compiled PDF.
2. Two reference-metadata corrections at the registry (NEW-2, NEW-3) before IEEE rendering.
3. Keywords (NEW-4) — author's call.
4. Author-supplied fields (NEW-5).
5. Acknowledged and already in Limitations: matched-training result known only at 40 and 20 dB; one reconstructor; one phantom; fixed weights; onset shape and channel specificity descriptive.

## Attachment: Acronym Check (advisory, #849)

`scripts/check_acronyms.py --input manuscript/15_DRAFT_v2.md --lang en` (2026-09-26): GREIT, SNR, EIDORS and HD95 are expanded but the initials do not spell the expansion (expected for these names); undefined in body: SHA (×4), RMS (×1), CMU, NSTC, PI, MATLAB, GB, TAG, CRediT, TMI (end matter and bracketed placeholders). MAE, IoU and ASSD are now expanded at first use in §2.4. Advisory only; no finding above derives from it.
