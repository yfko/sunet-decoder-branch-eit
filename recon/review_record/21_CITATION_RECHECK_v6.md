# Citation Re-check (scoped) — RECON paper, draft v6

| | |
|---|---|
| Date | 2026-10-31 |
| Mode | ARS 3.23.0 `academic-paper` **citation-check**, strict `citation_existence`, strict retraction policy, **scoped** re-check after revision round 1e (follows `16_CITATION_AUDIT_v3.md` and `16b_CITATION_RECHECK_v4.md`); installed ARS version checked = 3.23.0 = calibration baseline |
| Model | Opus-class (Opus 5.5). Checks 1–4 and 6 are execution-class; Check 5 (claim–source context) is a judgment-class reading, so the PI may want it re-read on Fable |
| Target | `RECON_paper/manuscript/20_DRAFT_v6.md`, sha256 `ab11b87add5c6f9f83d42db8583e5f1544adaf163259f4285a2393c6d8be29b1` (prefix ab11b87add5c, matches the brief and `20_DRAFT_v6.md.apply-report.json` `output_draft_hash`); `20_DRAFT_v6.as-applied.md` is byte-identical |
| Base | `19_DRAFT_v5.md`, sha256 `bf252f799a3a489d8dc1a7531ab51cfcd43e28820c4af15ade33daf6a441c732` |
| Patch | `revision-authority-round1e/revision_patch_round1e.json`: 23 `replace_block` ops (roadmap items REV-M1e-1 … REV-M1e-11); apply report 23 touched / 137 byte-identical of 160 blocks |
| Scope | (1) diff scope; (2) reference list B0092: 70 shared strings, 2 new strings field by field, numbering, counts; (3) retraction/concern for the 2 new entries; (4) quote anchors in the 11 changed blocks that carry citations; (5) claim–source context for the new Barber and Zhang 2022a clauses, the nine reworded m-items, the a/b letter pairs; (6) PLoS One citability. Strings, retraction status and anchors of the 70 carried entries in untouched blocks are inherited from `16_` / `16b` |
| Fresh lookups (2026-10-31) | Crossref REST `api.crossref.org/works/<DOI>` for the 46 DOIs cited in the changed blocks (both new DOIs included); NCBI E-utilities: esearch by DOI for all 46 (35 PMIDs), efetch PubMed XML for the 35, esummary PMID 36265475 (Zhang 2022a) and PMID 11540235, esummary `db=nlmcatalog&id=1276760` (J Phys E); OpenAlex works for both new DOIs (+ 4 abstract fallbacks); Semantic Scholar for Barber 1984 and 4 abstract fallbacks; arXiv API 2404.09556 (Isensee abstract); Europe PMC full-text XML PMC7853495 (Ko and Cheng 2021b); local EIDORS v3.8 distribution (`~/Documents/MATLAB/eidors-v3.8`: `htdocs/data_contrib/db_backproj_matrix/db_backproj_matrix-s.html`, `eidors/models/mk_common_gridmdl.m`). Raw responses kept in the session scratchpad only |
| Files written | This report only. The draft, registry, rendered strings and every other file were not modified |

---

## Summary

| Check | Result |
|---|---|
| 1. Diff scope | **PASS**: block-level comparison of v5 and v6 (160 blocks, same order) finds exactly 23 changed blocks, and they are the 23 the patch names; 137 blocks byte-identical; `# PIPELINE INTERNAL` section unchanged |
| 2a. 70 shared strings | **PASS**: 70/70 byte-identical to v5's lines (number ignored); 72/72 v6 strings occur verbatim in today's Vancouver render `refs/prior_works_recon_strings.md`; registry keys = list keys (72); 72/72 registry DOIs present in their line |
| 2b. Two new strings | **PASS**: Barber1984JPhysE and Zhang2022PhysiolMeas match fresh Crossref in every field (authors, title, journal, year, volume, pages, DOI); Zhang also matches PubMed (PMID 36265475); Barber's journal "J Phys E" = NLM MedlineTA of NLM Catalog UID 1276760 (ISSN 0022-3735); Barber is not in PubMed |
| 2c. Numbering | **PASS**: numbers 1–72 contiguous and equal to the order of first `<!--ref:KEY-->` in the manuscript part; Zhang2022PhysiolMeas = 11 (first cited B0013), Barber1984JPhysE = 32 (first cited B0024); 60 v5 entries renumbered (v5 11–30 → 12–31, v5 31–70 → 33–72); 0 ref markers in the abstract or after `## References` |
| 2d. Counts (`check_recon_draft.py`) | **PASS**: 84 instances / 72 distinct / 84 quote anchors / 0 slugs outside corpus / **0 orphans** / 72 list entries / 0 cited-but-unlisted / 0 listed-but-uncited |
| 3. Retraction / concern (2 new) | **PASS**: Crossref `update-to` and `updated-by` absent, `relation` empty for both; OpenAlex `is_retracted` = false for both; PubMed (Zhang only): publication types Journal Article + Research Support, Non-U.S. Gov't, no CommentsCorrections. Coverage note on a conflated OpenAlex/Semantic Scholar record for Barber (§3) |
| 4. Quote anchors (11 blocks) | **PASS**: 49/49 VERIFIED (2 new, 47 unchanged from v5), 0 NOT FOUND, 0 PARAPHRASE; max 16 words. Overall 84/84 (35 pairs in untouched blocks carried from 16_/16b) |
| 5. Claim–source context | New Barber clause (B0024) **SUPPORTED** (EIDORS's attribution requirement for the distributed matrix names exactly this paper); new Zhang 2022a clause (B0013) **SUPPORTED** by the Crossref/PubMed abstract; m1, m2, m3, m5, m6, m7, m8, m10, m12 **RESOLVED** (9/9); a/b letter pairs consistent (4/4); 0 new claim–source flags |
| 6. PLoS One citability | **PASS**: companion core paper has no registry key, no marker, no list entry; no preprint, unaccepted or unpublished work in the list |
| Housekeeping | **1 advisory flag (F1, B0091)**: the bracket above the list still dates the strings 2026-10-17; they were re-rendered 2026-10-31 |

**Scoped verdict: `citation_check=PASS WITH FLAGS`.** The strict layer passes outright: no unresolvable entry, no string, key or DOI mismatch, no unverifiable anchor, no retraction, and the v5 lone-letter and orphan items are closed. The one flag is a stale date in a pipeline bracket (B0091), not a citation error; it can be fixed with a one-token edit or left to format-convert, which replaces that bracket.

---

## 1. Diff scope (v5 → v6)

Method: both drafts were split on `<!--block:BNNNN-->` markers. Both have 160 blocks in the same order. 23 bodies differ, and the set equals the 23 `block_id`s of `revision_patch_round1e.json` (and of the apply report's `ops_applied`). A plain `diff` gives 25 hunks, all inside these 23 blocks (B0116 and B0158 are multi-line tables, B0092 is the 72-line list). Nothing after line 500 differs, so the `# PIPELINE INTERNAL` section (line 522 on) is unchanged.

| v6 line(s) | Block | Roadmap item(s) | Carries citations |
|---|---|---|---|
| 44 | B0013 | REV-M1e-7, REV-M1e-9 | 7 (1 new: Zhang 2022a) |
| 53 | B0016 | REV-M1e-10 (m6) | 5 |
| 77 | B0024 | REV-M1e-1 | 5 (1 new: Barber and Brown 1984) |
| 86 | B0027 | REV-M1e-10 (m3) | 3 |
| 89 | B0028 | REV-M1e-10 (m7, m8) | 5 |
| 95 | B0030 | REV-M1e-10 (m1) | 1 |
| 104 | B0033 | REV-M1e-10 (m12) | 1 |
| 113 | B0036 | REV-M1e-5 | 0 |
| 131 | B0042 | REV-M1e-7 | 0 |
| 152 | B0049 | REV-M1e-2 | 0 |
| 176 | B0057 | REV-M1e-8 | 0 |
| 182 | B0059 | REV-M1e-3 | 0 |
| 212 | B0069 | REV-M1e-6 | 3 (not in the brief's list; checked here as well) |
| 221 | B0072 | REV-M1e-10 (m2) | 4 |
| 230 | B0075 | REV-M1e-10 (m10) | 8 |
| 236 | B0077 | REV-M1e-10 (m5) | 7 |
| 239 | B0078 | REV-M1e-4 | 0 |
| 278 | B0150 | REV-M1e-7 | 0 |
| 299–370 | B0092 | REV-M1e-1, REV-M1e-9 | reference list |
| 450 | B0112 | REV-M1e-3 | 0 |
| 460 | B0114 | REV-M1e-3 | 0 |
| 466–472 | B0116 | REV-M1e-3 | 0 |
| 481–500 | B0158 | REV-M1e-11 | 0 |

Across the whole manuscript part, the (key, anchor) pairs of v6 are those of v5 plus exactly two: (Zhang2022PhysiolMeas, "Deep feature-domain matching for cardiac-related component separation") and (Barber1984JPhysE, "Applied potential tomography"). No pair was removed or altered. The 12 changed blocks without citations were not read for citation content.

---

## 2. Reference list (B0092)

### 2a. The 70 shared strings

All 70 keys of v5's list are in v6's list, and for each the string (the line minus its number) is **byte-identical** to v5's. All 72 v6 strings also occur verbatim in the Vancouver section of today's render `refs/prior_works_recon_strings.md`. Against the previous render (`prior_works_recon_strings.pre-round1e-20261031.md`) the only differences are the two removed registry entries (Rusak 2020, Zhang L 2020) and the added Barber 1984; the patched `cite.py` re-render changed no other string. Field-level verification of the 70 is therefore inherited from `16_CITATION_AUDIT_v3.md` §1 (Check A, 70/70).

Registry: `refs/refs_in_recon.json` has 72 entries, and its key set equals the list's key set. Compared with `refs_in_recon.pre-round1e-20261031.json` (73), Rusak2020ECCV and Zhang2020TMI were removed and Barber1984JPhysE was added. Each of the 72 lines contains `doi:` + its registry DOI.

### 2b. The two new strings, field by field

**No. 32, Barber1984JPhysE**: `Barber DC, Brown BH. Applied potential tomography. J Phys E. 1984;17:723-733. doi:10.1088/0022-3735/17/9/002`

| Field | v6 string | Crossref (fresh) | Other source | Result |
|---|---|---|---|---|
| Authors | Barber DC, Brown BH | Barber, D C (first); Brown, B H (additional) | Semantic Scholar: D. Barber, B. Brown | match (2 authors, no et al.) |
| Title | Applied potential tomography | "Applied potential tomography" (no subtitle) | — | exact |
| Journal | J Phys E | container "Journal of Physics E: Scientific Instruments"; short "J. Phys. E: Sci. Instrum." | NLM Catalog UID 1276760: `medlineta` "J Phys E", title "Journal of physics E: Scientific instruments.", ISSN 0022-3735 (Print), serial v. 3–22, 1970–1989, ISO abbreviation empty | match to MedlineTA, via override logged in `refs/overrides.json` (source and date recorded) |
| Year | 1984 | issued 1984-09 (published-print 1984-09; published-online 2000-11-29 = digitisation) | — | match |
| Volume | 17 | 17 (issue 9) | — | match |
| Pages | 723-733 | 723-733 | OpenAlex biblio 723–733 | match |
| DOI | 10.1088/0022-3735/17/9/002 | same; type journal-article; IOP Publishing | — | match |
| PubMed | — | — | not indexed: DOI search 0 hits, author+year search 0 hits; the journal's NLM indexing status is "N". Registry `pmid` = null (correct) | n/a |

**No. 11, Zhang2022PhysiolMeas**: `Zhang K, Li M, Liang H, Wang J, Yang F, Xu S, et al. Deep feature-domain matching for cardiac-related component separation from a chest electrical impedance tomography image series: proof-of-concept study. Physiol Meas. 2022;43:125005. doi:10.1088/1361-6579/ac9c44`

| Field | v6 string | Crossref (fresh) | PubMed (PMID 36265475) | Result |
|---|---|---|---|---|
| Authors | Zhang K, Li M, Liang H, Wang J, Yang F, Xu S, et al. | Zhang Ke; Li Maokun; Liang Haiqing; Wang Juan; Yang Fan; Xu Shenheng; Abubakar Aria (7) | Zhang K, Li M, Liang H, Wang J, Yang F, Xu S, Abubakar A | match (first six + et al., the list's rule for >6) |
| Title | Deep feature-domain matching … proof-of-concept study | identical (no subtitle field) | identical + final full stop | exact |
| Journal | Physiol Meas | "Physiological Measurement" / "Physiol. Meas." | MedlineTA "Physiol Meas" | match |
| Year | 2022 | issued 2022-12-28 (print 2022-12-30) | 2022 Dec 28 | match |
| Volume | 43 | 43 (issue 12) | 43 (12) | match |
| Article no. | 125005 | page "125005" | ELocationID doi only | match |
| DOI | 10.1088/1361-6579/ac9c44 | same; type journal-article | same (articleids) | match |

### 2c. Numbering and order

Numbers run 1–72 without gaps. The order of first appearance of `<!--ref:KEY-->` in the manuscript part (before `# PIPELINE INTERNAL`) equals the list order at all 72 positions:
- Zhang2022PhysiolMeas is 11: first cited in B0013, after Ko 2025 (10) and before Vandenhende 2021 (12).
- Barber1984JPhysE is 32: first cited in B0024. It precedes Adler2006EIDORS within the sentence, but Adler and Lionheart 2006 was already cited earlier (no. 28), so 32 is correct.

60 entries moved: v5 11–30 → v6 12–31, and v5 31–70 → v6 33–72. No ref marker in the abstract (B0006) and none after `## References`.

### 2d. Counts

`python3 -X utf8 tools/check_recon_draft.py RECON_paper/manuscript/20_DRAFT_v6.md`, run from the project root. The script reads `refs/refs_in_recon.json` relatively, so it fails from the manuscript directory. Citation block:

```
== citations ==
  instances: 84; distinct: 72; anchors: {'quote': 84}
  slugs outside corpus: []
  corpus entries never cited (orphans, 0): []
  reference-list entries: 72; cited-but-unlisted: []; listed-but-uncited: []
```

The same script on v5 gives 82 / 70 / 82 with 2 orphans (Barber1984JPhysE, Zhang2022PhysiolMeas), so the round adds exactly the two instances. Independent recount: 84 markers, 84 anchors, every marker paired, 72 distinct. In the 11 citing changed blocks: B0013 7, B0016 5, B0024 5, B0027 3, B0028 5, B0030 1, B0033 1, B0069 3, B0072 4, B0075 8, B0077 7, total 49 (v5 47).

Outside citation scope, for the PI: the script reports **7,998 main-text words against the 8,000 ceiling** (abstract 296/300). Two words of headroom, so any F1 fix must not add prose words (F1 is inside the References section).

---

## 3. Retraction, correction, expression of concern (new entries)

| Source (queried 2026-10-31) | Barber1984JPhysE | Zhang2022PhysiolMeas |
|---|---|---|
| Crossref `update-to` / `updated-by` (carries Retraction Watch data) | absent / absent | absent / absent |
| Crossref `relation` | {} | {} |
| OpenAlex `is_retracted` | false (W2278331350; see note) | false |
| PubMed publication types | not indexed | Journal Article; Research Support, Non-U.S. Gov't |
| PubMed CommentsCorrections | not indexed | none (no RetractionIn / ErratumIn / ExpressionOfConcernIn / UpdateIn) |

**0 retractions, 0 corrections, 0 expressions of concern.**

Coverage note, Barber (no flag): OpenAlex W2278331350 and Semantic Scholar CorpusId 27174973 both merge the J Phys E 1984 paper with a different PubMed record, PMID 11540235. That record has the same title and authors but is "J Br Interplanet Soc 1989;42(7):391-3". Semantic Scholar gives venue JBIS, year 1989. The OpenAlex abstract (about space-based measurement and simulated weightlessness) belongs to the 1989 item.

Consequences:
- The Barber retraction check rests on Crossref, which is DOI-exact and clean. The OpenAlex flag is corroborating only.
- Neither aggregator's abstract may be used as a witness for the 1984 paper.
- The registry correctly has `pmid: null`. If `tools/cite.py` is ever changed to take PMIDs from OpenAlex, this key would pick up the wrong one.

---

## 4. Anchor table, 11 changed blocks that carry citations

Method:
- Each anchor was URL-decoded and searched as an exact substring of the fresh Crossref title (+ subtitle) and abstract, then of the PubMed title and abstract (efetch) where indexed.
- For Ko2021PLOSONE it was also searched in the PMC7853495 full text.
- Unicode normalisation (NBSP, U+2010, curly quotes, NFKC) was tried only after an exact miss. It was needed for one anchor, the same as in 16_.

| # | Block | Key | DOI | Anchor (decoded) | Words | v5→v6 | Result |
|---|---|---|---|---|---|---|---|
| 1 | B0013 | Leathard1994PhysiolMeas | 10.1088/0967-3334/15/2a/018 | ventilatory and cardiac related changes in EIT images | 8 | unchanged | VERIFIED: Crossref title, exact |
| 2 | B0013 | Graf2017PLOSONE | 10.1371/journal.pone.0188313 | highly position dependent | 3 | unchanged | VERIFIED: Crossref title, exact |
| 3 | B0013 | Ko2021PhysiolMeas | 10.1088/1361-6579/abe021 | U-Net-based approach for automatic lung segmentation | 6 | unchanged | VERIFIED: Crossref title, exact |
| 4 | B0013 | Ko2021PLOSONE | 10.1371/journal.pone.0246071 | Semi-Siamese U-Net for separation of lung and heart bioimpedance images | 10 | unchanged | VERIFIED: Crossref title, exact |
| 5 | B0013 | Ko2025CurrMedImaging | 10.2174/0115734056408077250610070821 | Reconstruction of Heart-related Imaging from Lung Electrical Impedance Tomography | 9 | unchanged | VERIFIED: Crossref title, exact |
| 6 | B0013 | Zhang2022PhysiolMeas | 10.1088/1361-6579/ac9c44 | Deep feature-domain matching for cardiac-related component separation | 7 | **new** | VERIFIED: Crossref title, exact |
| 7 | B0013 | Ko2021PLOSONE | 10.1371/journal.pone.0246071 | the separation effect of the EIT image obtained by the different reconstruction algorithms will be investigated | 16 | unchanged | VERIFIED: PMC7853495 full text (Discussion, last paragraph), exact; not in title or abstract, as in 16b |
| 8 | B0016 | Zech2018PLoSMed | 10.1371/journal.pmed.1002683 | Variable generalization performance of a deep learning model | 8 | unchanged | VERIFIED: Crossref title, exact |
| 9 | B0016 | AlBadawy2018MedPhys | 10.1002/mp.12752 | Impact of cross-institutional training and testing | 6 | unchanged | VERIFIED: PubMed title (PMID 29356028), exact (Crossref title has U+2010), as in 16_ |
| 10 | B0016 | Liu2020TMI | 10.1109/tmi.2020.2974574 | Multi-Site Network for Improving Prostate Segmentation With Heterogeneous MRI Data | 10 | unchanged | VERIFIED: Crossref title, exact |
| 11 | B0016 | HoangThi2021DIII | 10.1016/j.diii.2021.10.001 | Which reconstruction kernel should be used? | 6 | unchanged | VERIFIED: Crossref title, exact |
| 12 | B0016 | Zeng2022MedPhys | 10.1002/mp.15430 | Generalizability over dose, reconstruction kernel, and slice thickness | 8 | unchanged | VERIFIED: Crossref title, exact |
| 13 | B0024 | Adler2009GREIT | 10.1088/0967-3334/30/6/s03 | GREIT: a unified approach to 2D linear EIT reconstruction of lung images | 12 | unchanged | VERIFIED: Crossref title, exact |
| 14 | B0024 | Adler1996TMI | 10.1109/42.491418 | regularized imaging and contrast detection | 5 | unchanged | VERIFIED: Crossref title, exact |
| 15 | B0024 | Barber1984JPhysE | 10.1088/0022-3735/17/9/002 | Applied potential tomography | 3 | **new** | VERIFIED: Crossref title, exact |
| 16 | B0024 | Adler2006EIDORS | 10.1088/0967-3334/27/5/s03 | an extensible software base for EIT | 6 | unchanged | VERIFIED: Crossref title, exact |
| 17 | B0024 | Thurk2019PhysiolMeas | 10.1088/1361-6579/ab248e | Influence of reconstruction settings | 4 | unchanged | VERIFIED: Crossref title, exact |
| 18 | B0027 | Ronneberger2015UNet | 10.1007/978-3-319-24574-4_28 | U-Net: Convolutional Networks for Biomedical Image Segmentation | 7 | unchanged | VERIFIED: Crossref title, exact |
| 19 | B0027 | Vandenhende2020Branched | 10.5244/c.34.59 | Deciding what layers to share | 5 | unchanged | VERIFIED: Crossref title, exact |
| 20 | B0027 | Isensee2024nnUNetRevisited | 10.1007/978-3-031-72114-4_47 | A Call for Rigorous Validation in 3D Medical Image Segmentation | 10 | unchanged | VERIFIED: Crossref title after NBSP→space (U+00A0 twice in the Crossref title), as in 16_ |
| 21 | B0028 | Caruana1997MTL | 10.1023/a:1007379606734 | Multitask Learning | 2 | unchanged | VERIFIED: Crossref title, exact |
| 22 | B0028 | Kurin2022Unitary | 10.52202/068431-0884 | In Defense of the Unitary Scalarization for Deep Multi-Task Learning | 10 | unchanged | VERIFIED: Crossref title, exact |
| 23 | B0028 | Xin2022MTOHelp | 10.52202/068431-0988 | Do Current Multi-Task Optimization Methods in Deep Learning Even Help? | 10 | unchanged | VERIFIED: Crossref title, exact |
| 24 | B0028 | Kendall2018 | 10.1109/cvpr.2018.00781 | Multi-task Learning Using Uncertainty to Weigh Losses | 7 | unchanged | VERIFIED: Crossref title, exact |
| 25 | B0028 | Renard2020SciRep | 10.1038/s41598-020-69920-0 | Variability and reproducibility in deep learning for medical image segmentation | 10 | unchanged | VERIFIED: Crossref title, exact |
| 26 | B0030 | Pulletz2006ROI | 10.1088/0967-3334/27/5/s10 | 20-35% of the maximum standard deviation or regression coefficient | 9 | unchanged | VERIFIED: PubMed abstract (PMID 16636403), exact |
| 27 | B0033 | Jeschke2025Sensors | 10.3390/s25216543 | Robustness to Electrode Displacement | 4 | unchanged | VERIFIED: Crossref title, exact |
| 28 | B0069 | Holzschuh2024RadiatOncol | 10.1186/s13014-024-02491-w | multicentric datasets | 2 | unchanged | VERIFIED: Crossref title, exact |
| 29 | B0069 | Lakens2017SPPS | 10.1177/1948550617697177 | Equivalence Tests | 2 | unchanged | VERIFIED: Crossref title, exact |
| 30 | B0069 | Venkatesh2026MedPhys | 10.1002/mp.70414 | Performance benchmarking of deep learning models | 6 | unchanged | VERIFIED: Crossref title, exact |
| 31 | B0072 | Grychtol2014PhysiolMeas | 10.1088/0967-3334/35/6/1035 | Choice of reconstructed tissue properties | 5 | unchanged | VERIFIED: Crossref title, exact |
| 32 | B0072 | Albert2023ApplSci | 10.3390/app13158923 | Comparison of Image Normalization Methods for Multi-Site Deep Learning | 9 | unchanged | VERIFIED: Crossref title, exact |
| 33 | B0072 | Karani2018MICCAI | 10.1007/978-3-030-00928-1_54 | Across Scanners and Protocols | 4 | unchanged | VERIFIED: Crossref title, exact |
| 34 | B0072 | Delisle2021MedIA | 10.1016/j.media.2021.102191 | Realistic image normalization for multi-Domain segmentation | 6 | unchanged | VERIFIED: Crossref title, exact |
| 35 | B0075 | Martensson2020MedIA | 10.1016/j.media.2020.101714 | clinical out-of-distribution MRI data: A multicohort study | 7 | unchanged | VERIFIED: Crossref title, exact |
| 36 | B0075 | Zech2018PLoSMed | 10.1371/journal.pmed.1002683 | Variable generalization performance | 3 | unchanged | VERIFIED: Crossref title, exact |
| 37 | B0075 | Castro2020NatCommun | 10.1038/s41467-020-17478-w | Causality matters | 2 | unchanged | VERIFIED: Crossref title, exact |
| 38 | B0075 | Zeng2022MedPhys | 10.1002/mp.15430 | reconstruction kernel, and slice thickness | 5 | unchanged | VERIFIED: Crossref title, exact |
| 39 | B0075 | Kamann2021IJCV | 10.1007/s11263-020-01383-2 | Robustness of Semantic Segmentation Models with Respect to Common Corruptions | 10 | unchanged | VERIFIED: Crossref title, exact |
| 40 | B0075 | Boone2023NeuroImage | 10.1016/j.neuroimage.2023.120289 | out-of-distribution and corrupted data in MRI | 6 | unchanged | VERIFIED: Crossref title, exact |
| 41 | B0075 | Du2022EurRadiol | 10.1007/s00330-022-09229-w | harmonization of CT reconstruction kernels | 5 | unchanged | VERIFIED: Crossref title, exact |
| 42 | B0075 | Billot2023MedIA | 10.1016/j.media.2023.102789 | any contrast and resolution without retraining | 6 | unchanged | VERIFIED: Crossref title, exact |
| 43 | B0077 | Scheel2021AMPPS | 10.1177/25152459211007467 | Comparing the Standard Psychology Literature With Registered Reports | 8 | unchanged | VERIFIED: Crossref title, exact |
| 44 | B0077 | McGreivy2024NatMachIntell | 10.1038/s42256-024-00897-5 | Weak baselines and reporting biases | 5 | unchanged | VERIFIED: Crossref title, exact |
| 45 | B0077 | Borji2018ImaVisComput | 10.1016/j.imavis.2017.10.001 | Negative results in computer vision | 5 | unchanged | VERIFIED: Crossref title, exact |
| 46 | B0077 | Varoquaux2022NPJDigitMed | 10.1038/s41746-022-00592-y | methodological failures and recommendations | 4 | unchanged | VERIFIED: Crossref title, exact |
| 47 | B0077 | Nosek2018Prereg | 10.1073/pnas.1708274114 | The preregistration revolution | 3 | unchanged | VERIFIED: Crossref title, exact |
| 48 | B0077 | Chambers2021NatHumBehav | 10.1038/s41562-021-01193-7 | Registered Reports | 2 | unchanged | VERIFIED: Crossref title, exact |
| 49 | B0077 | Pawel2023BiomJ | 10.1002/bimj.202200091 | Questionable research practices in comparative simulation studies | 7 | unchanged | VERIFIED: Crossref title, exact |

Tally:
- 49/49 VERIFIED, 0 NOT FOUND, 0 PARAPHRASE.
- By witness: 45 exact Crossref-title substrings; 1 exact PubMed-title substring (AlBadawy); 1 exact PubMed-abstract substring (Pulletz); 1 Crossref title after NBSP normalisation (Isensee); 1 exact full-text substring (Ko and Cheng 2021b, non-title).
- 47 pairs are byte-identical to v5 and were re-verified today. 2 are new.

**The two new anchors.**

| Key | Block | Anchor | Result | Remark |
|---|---|---|---|---|
| Barber1984JPhysE | B0024 | "Applied potential tomography" (3 words) | **VERIFIED**: the whole Crossref title, exact | A title-only witness. No abstract exists in Crossref or PubMed, and the aggregators' abstract belongs to another record (§3). The attribution itself is verified against EIDORS (§5.1), not against this anchor |
| Zhang2022PhysiolMeas | B0013 | "Deep feature-domain matching for cardiac-related component separation" (7 words) | **VERIFIED**: Crossref title and PubMed title (PMID 36265475), exact | The title supports "cardiac-related component separation". The Siamese network and the feature-matching constraint are in the abstract (§5.2). Optional, no flag: anchor on "the Siamese network is used as a feature-matching constraint" (8 words, exact in the Crossref and PubMed abstract), so the anchor witnesses the clause directly, as 16b did for E1–E5 |

---

## 5. Claim–source context (ADVISORY)

### 5.1 B0024, the new Barber clause. **SUPPORTED**

v6: "Back-projection (BP) used the Sheffield back-projection matrix (Barber and Brown, 1984) distributed with EIDORS (Adler and Lionheart, 2006), with no free parameter (noise figure 0.831); …"

Evidence:
- **EIDORS v3.8 data-contribution page for the matrix** (`htdocs/data_contrib/db_backproj_matrix/db_backproj_matrix-s.html`, authors listed as David C Barber, Brian H Brown, June 2008). It states that the matrix "is the version distributed with the Sheffield Mk I system". Under "Attribution Requirement" it names exactly "D.C. Barber and B.H. Brown (1984), Applied Potential Tomography, J. Phys. E: Sci. Instrum., 17:723-733". The distributor's required citation for this matrix is therefore the cited work.
- `eidors/models/mk_common_gridmdl.m` (`'backproj'` → `get_Sheffield_Backproj`, loading `Sheffield_Backproj_Matrix.mat`) carries the copyright notice "copyright DC Barber and BH Brown at University of Sheffield". S1 Appendix (B0158, line 488) names the same call, `mk_common_gridmdl('backproj')`.

Judgment:
- The clause cites the paper the matrix's own documentation requires, and "distributed with EIDORS" stays with Adler and Lionheart 2006. Supported.
- Two points, neither needing action:
  1. The same EIDORS page says the paper that "probably best describes this algorithm" is Santosa and Vogelius 1990 (SIAM J Appl Math 50:216–243).
  2. `inv_solve_backproj.m` cites Barber and Brown 1987, "Fast reconstruction of resistance images" (Clin Phys Physiol Meas 8 Suppl A:47–54; Crossref lists doi 10.1088/0143-0815/8/4a/006 with authors Barber and Seagar, unverified here). That reference is for the filtered algorithm, which that function does not implement.

  Neither is needed for the attribution the sentence makes. Adding either would cost words against a 2-word headroom.
- The cited paper is from 1984, before 2016. As a seminal method reference it falls under the same role as the other pre-2016 method references in 16_ §8.

### 5.2 B0013, the new Zhang 2022a clause. **SUPPORTED**

v6: "Elsewhere, a Siamese network supplied the feature-matching constraint of an unsupervised cardiac-signal separation from chest EIT image series (Zhang et al., 2022a)."

Source (Crossref abstract = PubMed abstract, PMID 36265475), Approach: "We propose an unsupervised deep-learning method called deep feature-domain matching (DFDM) … In the first step, a novel Siamese network is designed and trained to learn common features of breath-holding signals; in the second step, the Siamese network is used as a feature-matching constraint between the separated signals and the breath-holding signals." The title has "cardiac-related component separation from a chest electrical impedance tomography image series".

Judgment:
- "Siamese network", "feature-matching constraint", "unsupervised" and "from chest EIT image series" are each in the title or abstract.
- "cardiac-signal separation" condenses the abstract's "cardiac-related signal separation". Acceptable.
- The clause claims nothing about accuracy or validation (synthetic data plus a qualitative check on three patients with pulmonary embolism), so it does not overstate.
- "Elsewhere" correctly separates it from the authors' own three studies.

### 5.3 The nine reworded m-items (16_ §5 "Minor items")

| ID | Block | Key | v5 wording (16_ point) | v6 wording | Source check (fresh) | Status |
|---|---|---|---|---|---|---|
| m1 | B0030 | Pulletz2006ROI | "the 20–35% band that clinical region-of-interest methods recommend" | "the 20–35% band recommended for region-of-interest definition on functional EIT images, a band defined on per-pixel statistics rather than on a reconstructed amplitude" | PubMed abstract: "The definition of the ROI contour as 20-35% of the maximum standard deviation or regression coefficient is recommended"; ten patients | **RESOLVED**: follows 16_'s suggestion; the band is no longer attributed to "clinical methods" in general; the per-pixel caveat is kept |
| m2 | B0072 | Albert2023ApplSci | "whose unitless intensities differ by far less than two orders of magnitude" (not in source) | "whose unitless intensities we take to differ by far less than two orders of magnitude, the choice among normalisation methods changes Dice by less than 0.02" | Crossref abstract: "a difference in Dice of less than 0.02 between the best and worst performing networks"; six centres, multimodal MRI | **RESOLVED**: the magnitude premise is marked as the authors' ("we take to"), and the cited part is in the source |
| m3 | B0027 | Isensee2024nnUNetRevisited | "capacity-matched" glosses the source | "an adequately configured baseline at comparable compute is the control whose absence lets a new architecture appear to beat a U-Net" | arXiv 2404.09556 abstract (no Crossref/PubMed abstract): claims "fail to hold up when scrutinized for … inadequate baselines, insufficient datasets, and neglected computational resources"; "a properly configured U-Net" | **RESOLVED**: follows 16_'s suggestion word for word |
| m5 | B0077 | McGreivy / Borji / Varoquaux | "the kind of result most exposed to under-reporting" (superlative not in sources) | "a kind of result exposed to under-reporting in computational fields" | McGreivy (S2 abstract): "reporting biases lead to under-reporting of negative results"; Borji (S2): negative results "often overlooked"; Varoquaux (Crossref): incentives "such as optimizing for publication" | **RESOLVED**: superlative removed. McGreivy is the direct witness, the other two support it in general terms |
| m6 | B0016 | Liu2020TMI | "needed site-specific normalisation" | "used site-specific normalisation" | PubMed: "Domain-Specific Batch Normalization layers … perform feature normalization for each site separately" | **RESOLVED** |
| m7 | B0028 | Caruana1997MTL | "The second decoder is hard parameter sharing" | "Sharing one encoder between two decoders is hard parameter sharing" | title only (no abstract in Crossref, OpenAlex or S2; seminal method reference, as in 16_) | **RESOLVED**: the sharing is now attributed to the encoder, as 16_ suggested |
| m8 | B0028 | Renard2020SciRep | "of the order of the effects at stake" was the authors' inference | "seed-to-seed variability can be large (Renard et al., 2020), and here it is of the order of the effects at stake" | Crossref/PubMed: these techniques "can have a high range of variability" | **RESOLVED**: follows 16_'s optional wording exactly; the inference now sits outside the citation |
| m10 | B0075 | Du2022EurRadiol | outperformance was for radiomics, not segmentation | "learned harmonisation, which outperformed the location-scale baseline this fixed affine amounts to for CT radiomics" | PubMed key points: CNN harmonisation "performed better than location-scale (ComBat and centering-scaling) and matrix factorization harmonization methods … in both clinical tasks"; aim: "improve performance of radiomics models" | **RESOLVED**: residual note under the table |
| m12 | B0033 | Jeschke2025Sensors | "EIT cross-condition designs" (plural, one study) | "follows an EIT cross-condition design" | Crossref/PubMed: four training and four testing datasets at four electrode-displacement levels | **RESOLVED** |

Residual note, m10 (no flag): in Du's abstract the CNN's advantage is significant for the LC-versus-TB task (p = 0.0001–0.0003 for CNNa) but not for lymph-node-metastasis prediction (p = 0.07–0.40). "Outperformed" matches the abstract's key-point summary. If the author wants it exact: "…which outperformed location-scale harmonisation for CT radiomics, significantly in one of two tasks". That adds words, and the 2-word headroom argues against it.

### 5.4 Other citing changes in the changed blocks (no flag)

- **B0013**: "Three studies of ours" → "Three of our studies"; the companion's gap marker becomes "[MATERIAL GAP: preprint DOI, see Related manuscript]". Leathard, Graf and both Ko and Cheng 2021 clauses are unchanged. E2's wording, RESOLVED in 16b, is intact.
- **B0016**: only m6.
- **B0024**: GN parametrisation reworded with no citation impact. "Because reconstruction settings strongly influence a reconstructor's output (Thürk et al., 2019)" still matches the abstract's "strong influence". Adler 2009, Adler and Guardo 1996 and Adler and Lionheart 2006 are unchanged.
- **B0027**: architecture sentence reworded. Ronneberger and Vandenhende 2020 clauses unchanged.
- **B0028**: Kurin/Xin/Kendall clause unchanged in substance ("a defensible default" → "defensible").
- **B0069** (changed but not in the brief's list): Holzschuh clause and Lakens sentence unchanged. Venkatesh clause "it is not a convention" → "it is no convention of the field". Same meaning, and the claim is a search-scoped statement of the authors'.
- **B0072**: apart from m2, the Grychtol 2014b, Karani and Delisle clauses are unchanged.
- **B0075**: apart from m10, "where a network's tolerance differs" → "where tolerance differs" for Kamann/Boone. Still matches Kamann's "depends strongly on the type of image corruption".
- **B0077**: apart from m5, the Scheel figures (44% vs 96%), Nosek/Chambers and Pawel are unchanged.

### 5.5 a/b letter pairs

The visible author-year form was extracted for every marker (parenthesis immediately before the marker run, split on ";"). For every key, every instance carries the same visible form.

| Pair | "a" | "b" | Mentions | Letter order = order of first citation | Result |
|---|---|---|---|---|---|
| Zhang et al., 2022 | Zhang2022PhysiolMeas (no. 11; Zhang **K** et al.) | Zhang2022FBB (no. 17; Zhang **T** et al.) | a ×1 (B0013), b ×1 (B0014) | yes | consistent. The v5 lone "2022b" (16_ G, v1 A13) is now paired |
| Grychtol 2014 | Grychtol2014PLOSONE (no. 3; "Grychtol et al.") | Grychtol2014PhysiolMeas (no. 54; "Grychtol and Adler") | a ×1 (B0011), b ×1 (B0072) | yes | consistent |
| Ko and Cheng 2021 | Ko2021PhysiolMeas (no. 8) | Ko2021PLOSONE (no. 9) | a ×1, b ×2 (all B0013) | yes | consistent |
| Yu et al., 2024 | Yu2024CMPB (no. 14) | Yu2024CVPR (no. 44) | a ×1 (B0014), b ×1 (B0034) | yes | consistent |

Note (no flag): the two Zhang works have different first authors (Zhang K vs Zhang T), and the two Grychtol works have different author lists. Under an author-year style they would be told apart by initials or co-authors rather than by letters. All letters disappear when format-convert applies citation-sequence numbers (PLoS One Vancouver), so no action is needed unless author-year survives to submission.

---

## 6. PLoS One citability (inherited rule from 16_ §6)

| Item | Result |
|---|---|
| Companion core paper in `refs_in_recon.json` | **no key** (no registry entry matches companion, core, SUNet or a 2026+ Ko key) |
| Companion in the reference list (B0092) | **absent**. 72 published works, all DOIs resolving today (the 46 in changed blocks fetched fresh; the rest inherited) |
| Ref marker in any sentence that names the companion | none. The companion is named in the same 12 blocks as in v5 (B0001 comment, B0013, B0028, B0036, B0046, B0049, B0057, B0089, B0105, B0107, B0116, B0158); no sentence naming it carries a marker |
| `[MATERIAL GAP: preprint …]` markers | B0013 (now "…preprint DOI, see Related manuscript") and B0089, unchanged in role |
| Preprints / arXiv / medRxiv / "submitted" / "in press" / "unpublished" in the list | none. Both new entries are published journal articles (Crossref type journal-article) |
| "data not shown", "personal communication" in the manuscript part | none |
| Citations in the abstract | none |

**Result: PASS.** The round added only published, DOI-resolving journal articles, and the companion stays uncited.

---

## 7. Flags and notes raised by this re-check

**F1 — B0091 (line 296), provenance bracket above the reference list. FLAG (advisory, housekeeping).**
- Text: "[Vancouver strings generated by `tools/cite.py` from Crossref and PubMed metadata (`refs/prior_works_recon_strings.md`, 2026-10-17), listed below in order of first citation; …]".
- The strings in v6 come from the 2026-10-31 re-render (`cite.py` + `apply_ref_overrides.py`, overrides applied 17:31). Barber's journal field comes from the NLM Catalog, through the override.
- Fix: "2026-10-17" → "2026-10-31", or leave it to format-convert, which replaces this bracket with the numbered list. The block is unchanged in this round, so it is a stale carry-over, not a patch error.

Notes (no flag):
- **n1 (§3)**: OpenAlex/Semantic Scholar conflate the Barber DOI with PMID 11540235 (JBIS 1989). The registry is correct; keep `pmid: null`.
- **n2 (§4)**: optional abstract anchor for Zhang 2022a.
- **n3 (§5.3)**: Du significance in one of two tasks.
- **n4 (§5.5)**: letters become moot at format-convert.

No claim–source flag in the 11 citing changed blocks.

---

## 8. Items carried, not in this scope

- **N1 of 16b** (B0074 comparison clause) and **m4** (B0014, Denker 2025 Post-UNet vs Deep D-bar in the Elsevier chapter): B0074 and B0014 are byte-identical to v5 and were not re-read here. Their status is whatever round 1d / the re-review recorded.
- m9, m11, m13: "none required" in 16_. Blocks B0013 (m9) and B0075 (m11) changed elsewhere, and the Leathard and Zeng clauses are unchanged. B0023 (m13) is unchanged.
- 16_ §10 action 11 (Karani LNCS volume, author-name forms, Wang 2024 article number) and action 12 (format-convert items F1–F11 of 16_ §1) remain format-convert work. The 70 carried strings are byte-identical, so nothing there changed.
- 16_ §10 action 13 still applies: immediately before submission, re-run `tools/cite.py` + `apply_ref_overrides.py` for a fresh retraction check of all 72.
- Registry orphans (16_ §7): closed. 0 orphans; Rusak2020ECCV and Zhang2020TMI removed from the registry, Zhang2022PhysiolMeas now cited.

---

## 9. Verdict

| Item | Verdict |
|---|---|
| 1. Diff scope | PASS: 23/23 blocks, exactly the patch's |
| 2a. 70 shared strings | PASS: 70/70 byte-identical to v5; 72/72 in today's render |
| 2b. Barber1984JPhysE string | PASS: all fields = Crossref; journal = NLM MedlineTA "J Phys E" (UID 1276760) |
| 2b. Zhang2022PhysiolMeas string | PASS: all fields = Crossref = PubMed 36265475 |
| 2c. Numbering 1–72 = first-citation order | PASS |
| 2d. Counts | PASS: 84 / 72 / 84 anchors / 0 orphans / 72 entries / 0 / 0 |
| 3. Retraction (2 new) | PASS: 0 / 0 / 0 |
| 4. Anchors (11 blocks) | PASS: 49/49 VERIFIED (Barber VERIFIED, Zhang 2022a VERIFIED); 84/84 overall |
| 5. Claim–source | Barber SUPPORTED; Zhang 2022a SUPPORTED; m1 m2 m3 m5 m6 m7 m8 m10 m12 RESOLVED; letters consistent |
| 6. PLoS One citability | PASS |
| Flags | 1: F1 (B0091 stale render date), advisory |

Strict layer: unresolvable 0; string, key or DOI mismatches 0; anchors NOT FOUND / PARAPHRASE 0 / 0; retractions, corrections, expressions of concern 0 / 0 / 0.

`citation_check=PASS WITH FLAGS` (scoped, v6 `ab11b87add5c`)
