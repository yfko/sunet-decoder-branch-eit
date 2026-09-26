# Citation audit v2 — `15_DRAFT_v2.md` (academic-paper citation-check, 2026-09-26)

**Draft**: `manuscript/15_DRAFT_v2.md` (patch apply of 2026-09-26). **Corpus**: `refs/refs_in.json` → `refs/prior_works.json` (`tools/cite.py`, Crossref REST + PubMed E-utilities, 2026-09-23 01:29, 19 entries). **Policy**: existence strict, retraction strict. **Scanner**: `tools/check_draft.py`. Run after a major revision, as R12 requires; the v1 audit is `07_CITATION_AUDIT_v1.md`.

## 1. Existence and retraction (strict)

| Item | Result |
|---|---|
| Reference entries | 19 (14 in v1 + Deibele 2008, Frerichs 2009, Grant 2011, Cipolla/Gal/Kendall 2018, Vandenhende 2021) |
| Resolved by DOI (Crossref) | 19/19 (`refs/prior_works_strings.md` 核對聲明) |
| PubMed-indexed | 13/19 (the five non-indexed are the engineering/CS entries; journal abbreviation from Crossref short-container-title, marked in `prior_works_table.md`); the three new EIT entries were re-fetched from PubMed on 2026-09-26 (PMIDs 18544813, 19147986, 21266025) for the claim check below |
| Retracted | 0 |
| Corrected (`updated-by`) | 0 |
| Hand-typed strings | 0 (the reference block was written by `emit_patch.py` reading the Vancouver section of `prior_works_strings.md`) |

**Verdict: strict existence passes; no blocker.**

## 2. In-text ↔ reference list

| Item | Result |
|---|---|
| In-text instances | 24 |
| Distinct sources | 19 |
| Slugs outside corpus | 0 |
| Orphan references | 0 (v1 had five reserved entries uncited; all five are now cited once) |
| Cited but unlisted | 0 |
| Self-citation | 3/19 = 15.8% (ARS flag at 15%). Structural: the architecture under test is the authors' own; stated in Conflicts of Interest. **Not diluted, by PI decision.** |

Distribution: Ko2021PLOSONE 3, Wang2024TIM 3, Ko2025CurrMedImaging 2, all others 1.

## 3. Claim faithfulness of the five new citations (checked against the abstracts, PubMed 2026-09-26)

| Manuscript sentence (B0115 / B0011) | Source | Basis in source | Verdict |
|---|---|---|---|
| "The impedance changes synchronous with the heart rate are of very small amplitude" | Frerichs 2009 (doi:10.1159/000193994) | abstract, verbatim | ✔ quote anchor |
| methods "breath holding, electrocardiogram-gated averaging over cardiac cycles, and frequency-domain filtering at the respiratory and heart rates" | Grant 2011 (doi:10.1186/cc9985) | abstract: "breath holding, electrocardiograph (ECG) gating and frequency filtering"; "filtering at the respiratory and heart rate" | ✔ quote anchor |
| "template fitting that combines principal component analysis with frequency filtering to give a beat-by-beat cardiac signal after a short set-up period" | Deibele 2008 (doi:10.1088/0967-3334/29/6/S01) | abstract: PCA-estimated templates + frequency-domain filtering; "beat-by-beat after a one-time setup period of 20 s"; lists ECG-gated averaging, frequency filtering, breath holding as previous attempts | ✔ quote anchor |
| shared encoder + task-specific decoders as the standard encoder-focused dense-prediction design; task interference as the known failure mode | Vandenhende 2021 survey (doi:10.1109/tpami.2021.3054719) | survey's taxonomy of encoder-focused architectures and its treatment of task interference / negative transfer; **full text not read in this session**, general attribution to a survey | ✔ (general attribution; anchor `none`) |
| loss weighting "by hand or by a learned per-task uncertainty" | Cipolla/Gal/Kendall 2018 CVPR (doi:10.1109/cvpr.2018.00781) | the paper's title and method (uncertainty-weighted multi-task losses) | ✔ (title-level; anchor `none`) |

No new sentence attributes a specific finding to a source beyond what its abstract or title states. The Introduction's absence claim is unchanged and remains search-bounded (R12).

## 4. Metadata defects to resolve before submission (do not hand-edit; fix at the registry or at format-convert)

1. **Author order of the CVPR 2018 entry.** Crossref returns "Cipolla R, Gal Y, Kendall A" for 10.1109/cvpr.2018.00781, and the in-text form follows it ("Cipolla et al., 2018"). The paper as published is commonly cited as Kendall, Gal and Cipolla. **PI to verify against the paper's first page**; if Crossref is wrong, correct `refs/prior_works.json` at the registry step with a recorded note, then regenerate strings with `cite.py`. IEEE numbering hides the in-text form, but the reference entry itself must be right.
2. **Vandenhende 2021** renders as "IEEE Trans Pattern Anal Mach Intell. 2021:1-1" (Crossref early-access record, no volume/pages). The final volume, issue and pages must be fetched from the registry (re-run `cite.py`, which reads the current Crossref record) before the IEEE reference is rendered.
3. Carried from v1 (§5 of `07_CITATION_AUDIT_v1.md`): Pulletz 2006 given-name rendering ("Genderingen HRv"), Lakens 2013 missing article number 863, Ronneberger 2015 missing LNCS volume 9351 / MICCAI 2015, Wang 2024 double full stop in the abbreviation. All for format-convert.

## 5. Anchor locators (v3.7.3)

12/24 instances carry `anchor:none:` (the ten from v1 plus Vandenhende 2021 and Cipolla 2018, both method/tool attributions). The three new EIT citations carry quote anchors taken from the retrieved abstracts. PI decides whether to fill the twelve; if not, format-convert strips anchor markers.

## 6. Watch-term scan (R12 / boundary clauses)

`check_draft.py` on v2: no "first to", "no previous stud", "novel", "first time", "noisy", "divided branch"; "the first " ×3, all "the first draft" or "the first paragraph"-type uses, none a priority claim. Pipeline-leak scan on the manuscript part: clean.

## 7. Conclusion

Strict existence and retraction pass. Zero orphans, zero out-of-corpus slugs. Two registry-level metadata items (§4.1, §4.2) and four rendering items go to the PI / format-convert; none blocks re-review. Next citation-check: after the next major change.

## 8. Resolution of §4 items 1–2 (2026-09-26 15:40)

- **CVPR 2018 author order**: verified on the CVF Open Access page (byline Kendall, Gal, Cipolla; Crossref reversed). Corrected through `refs/overrides.json` → `tools/apply_ref_overrides.py` → re-rendered strings (log appended to `prior_works_strings.md`). In-text form in the deliverable is now rendered from the registry ("Kendall et al 2018"); the working draft's visible text still reads "Cipolla et al., 2018" and will be corrected in the next patch round.
- **Vandenhende 2021 → 2022;44(7):3614–3633**: from PubMed PMID 33497328 (doi:10.1109/TPAMI.2021.3054719); same mechanism. In-text year is now 2022.
