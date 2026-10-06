# Citation audit v4 — `34_DRAFT_v4.md` (academic-paper citation-check, 2026-10-06 late, Fable 5.1)

**Draft**: `manuscript/34_DRAFT_v4.md` (round-3 patch apply; report `34_DRAFT_v4.md.apply-report.json`, witness PASS, 99/126 blocks byte-identical, new block B0127). **Corpus**: `refs/refs_in.json` (54) → `refs/prior_works.json` + `refs/prior_works_strings.md` (`tools/cite.py` re-run 2026-10-06 late for the one new entry, Crossref + PubMed; `refs/overrides.json` re-applied). **Policy**: existence strict, retraction strict (R12d). Previous audit: `30_CITATION_AUDIT_v3.md` (53 entries). Run after the round-3 revision, as R12 requires.

## 1. Existence and retraction (strict)

| Item | Result |
|---|---|
| Reference entries | 54 (53 + Frerichs 2002 TMI, added at the round-2 panel's request, R2-W5) |
| Resolved by DOI (Crossref) | 54/54 (`prior_works_strings.md` 核對聲明) |
| Retracted / corrected | 0 / 0 (Ren 2020 correction notice: typesetting only, see v3 audit) |
| Hand-typed strings | 0 (reference block written by `emit_patch_round3.py` from the Vancouver section; 54 lines asserted) |
| Overrides | unchanged from v3 (Kendall order, Vandenhende 2022 volume/pages, Kurin particle, three LNCS volumes, Vandenhende 2020 particles) |

**Verdict: strict existence passes; no blocker.**

## 2. In-text ↔ reference list

| Item | Result |
|---|---|
| In-text instances | 67 (v3: 65; +Frerichs 2002, +Adler 2009 second instance) |
| Distinct sources | 54; slugs outside corpus 0; orphan references 0; cited-but-unlisted 0 |
| Self-citation | 3/54 = 5.6% |
| Deliverable (`36_SUBMISSION_scirep_v4.md`) | 66 numbered instances (one multi-cite), numbers 1–54 all used, no gaps; Nature strings rendered from the registry in citation order |

## 3. Claim faithfulness of the sentences changed or added in round 3

| Block | Source | What the sentence now attributes | Basis | Verdict |
|---|---|---|---|---|
| B0009 | Graf and Riedel 2017 | amplitude "depends strongly on body position" | PubMed abstract 2026-10-06: posture study (lateral, prone, supine, upright), "significant differences in both cardiac and respiratory amplitudes between postures" | ✔ corrected from "position in the thorax" (R2-W2) |
| B0009 | Frerichs et al. 2002 (new) | regional perfusion measured from the first pass of a hypertonic saline bolus, compared against electron-beam CT | PubMed abstract 2026-10-06: three pigs, hypertonic saline boli, EIT vs EBCT, "EIT imaging of lung perfusion is feasible when an electrical impedance contrast agent is used" | ✔ (abstract level; anchor `none`) |
| B0009 / B0079 | Adler et al. 2009 (GREIT) + Pulletz et al. 2006 | quarter-amplitude set is GREIT's figure-of-merit convention; ROI methods use 20–35% of maximum | GREIT paper defines its figures of merit on the quarter-amplitude set (known convention, `calc_hm_set(…, 0.25)`); Pulletz 2006 full text (literature/ PDF) lines 83 and 990: "20–35% of the maximum standard deviation or regression" | ✔ corrected (R2-W3) |
| B0027 | Murphy et al. 2019 | training assumed poorly contacting electrodes without specifying which; cardiac-output estimation from thoracic EIT data | PubMed abstract 2026-10-06: "Machine learning (ML) algorithms trained on electrical-impedance tomography (EIT) data … databases that assumed the presence of poorly contacting electrodes without any assumptions of knowing which electrodes would be bad" | ✔; the panel's R2-W4 ("bioimpedance, not EIT") does not hold against the abstract and is not adopted |
| B0011 | Vandenhende 2022, Misra 2016, Vandenhende 2020, Kendall 2018, Liu 2019, Kurin 2022, Xin 2022, Isensee 2024, Kamann 2021, Boone 2023, Wang 2024, Yu 2024 | unchanged sentences; two new sentences carry no citation | — | ✔ unchanged |
| B0052, B0062, B0028, B0027 (other refs) | Castro, FFDNet, Rusak, Boyle, Borges, Myronenko, Wilcoxon, Lakens, Ren, Jeschke, Ronneberger | unchanged attributions | — | ✔ |

No new sentence attributes to a source more than its abstract states. The search-bounded absence claim in §1 is unchanged.

## 4. Metadata and rendering items (format-convert / registry)

1. **Vandenhende 2020 author order** still to be confirmed against the BMVC PDF (carried from v3 §4.1).
2. Rendering carried from v3: Pulletz given-name form, Lakens article number 863, Ronneberger LNCS volume, Herzberg title glyph "⋆". The deliverable's Nature strings show these as the registry holds them; fix at the registry with a sourced override if the PI wants them changed before submission.
3. Frerichs 2002: PubMed-indexed (PMID 12166861), journal abbreviation from PubMed.

## 5. Anchors

55/67 instances carry `anchor:none:`; quote anchors unchanged (three prior works, Wang 2024, Frerichs 2009, Grant 2011, Deibele 2008, Graf 2017). Format-convert strips anchors.

## 6. Watch-term and R8 scan (`tools/check_draft.py` on v4)

No "first to", "novel", "noisy", "divided branch", "robust"; "the first" ×4 (none a priority claim); em dashes 2 (headers); semicolons 14 (threshold 14). Pipeline-leak scan clean.

## 7. Conclusion

Strict existence and retraction pass; zero orphans both ways; self-citation 5.6%. One registry item (Vandenhende 2020 order) and the carried rendering details go to the PI before submission; none blocks re-review. Next citation-check: after the next major change.
