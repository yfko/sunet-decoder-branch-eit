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
