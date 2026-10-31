# Citation Re-check (scoped) — RECON paper, draft v7

| | |
|---|---|
| Date | 2026-10-31 (lookups 17:58–18:15 CST) |
| Mode | ARS 3.23.0 `academic-paper` **citation-check**, strict `citation_existence`, strict retraction policy, **scoped** re-check after revision round 1f (follows `16_CITATION_AUDIT_v3.md`, `16b_CITATION_RECHECK_v4.md`, `21_CITATION_RECHECK_v6.md`); installed ARS version checked = 3.23.0 = calibration baseline |
| Model | Opus-class (Opus 5.5). Every check in this scope is execution-class (byte comparison, field lookup, status lookup). No claim–source reading was needed, because no sentence changed |
| Target | `RECON_paper/manuscript/23_DRAFT_v7.md`, sha256 `d02ec9b62ff11cd5d7cbd4864842c6568b6f3a5d1a7ad523ac2f386f4f638e42` (prefix d02ec9b62ff1, matches the brief and `23_DRAFT_v7.md.apply-report.json` `output_draft_hash`); `23_DRAFT_v7.as-applied.md` is byte-identical |
| Base | `20_DRAFT_v6.md`, sha256 `ab11b87add5c6f9f83d42db8583e5f1544adaf163259f4285a2393c6d8be29b1` |
| Patch | `revision-authority-round1f/revision_patch_round1f.json`: 2 `replace_block` ops (B0091 ← REV-M1f-2, B0092 ← REV-M1f-1); `old_hash` values f14845a83858 / e5dad32cf56d equal the v6 block manifest |
| Deliverable | `submission_PLOS_20261031/Manuscript.md`, sha256 `ed42a4db7204…` = `24_SUBMISSION_plos_v7.md` (byte-identical) |
| Scope | (1) diff scope; (2) the 25 overrides dated 2026-10-31 against the primary source each names; (3) all 72 strings of B0092 field by field against fresh Crossref (+ PubMed where indexed), overrides applied, and against `tools/cite.render_vancouver` of the registry; (4) retraction/correction refresh for all 72 DOIs (16_ §10 action 13); (5) deliverable reference list and in-text brackets; (6) PLoS One Vancouver conformance. Quote anchors and claim–source context are inherited from 16_/16b/21_, because every block other than B0091/B0092 is byte-identical |
| Fresh lookups | Crossref REST `api.crossref.org/works/<DOI>` for all 72 DOIs; Crossref `.xml` (unixsd) for the 5 LNCS chapters, Denker 2025, Wang 2024, Wilcoxon 1945, Vandenhende 2020; Crossref book records for the 5 LNCS volumes; NCBI E-utilities: esearch by DOI for all 72 (49 PMIDs), esummary + efetch PubMed XML for the 49; efetch PMIDs 34782730, 36355196, 16636403, 41213159, 31274971, 40115537, 31573001, 31482151, 20287815; esummary `db=nlmcatalog` for the 13 UIDs the overrides name, plus ISSN searches (0099-4987, 0920-5691, 2522-5839, 1570-8659) and "Biometrics bulletin"; esearch/esummary of 2022 "Adv Neural Inf Process Syst"[ta] records; OpenAlex works by DOI for all 72; web pages: CVF Open Access (Kendall 2018), NeurIPS proceedings (Kurin 2022), BMVC 2020 accepted-papers list, nature.com article page (Renard 2020), Springer citation exports (RIS/BibTeX) for the 5 chapters, DNB SRU by ISBN, PLOS ONE submission guidelines. Raw responses kept in the session scratchpad (`recheck_v7/raw/`, 389 files) only |
| Not reachable | link.springer.com chapter pages, dblp, JSTOR: each served a bot challenge, which was not attempted. The LNCS volumes were confirmed from Crossref's own deposit instead (§2.2) |
| Files written | This report only. The draft, registry, overrides, rendered strings, deliverable and every other file were not modified |

---

## Summary

| Check | Result |
|---|---|
| 1. Diff scope | **PASS**: 160 blocks in both, same order; exactly B0091 and B0092 differ, the two blocks the patch names; 158 blocks byte-identical; `# PIPELINE INTERNAL` section byte-identical; B0092 key order unchanged (72 keys, same sequence as v6) |
| 1b. Changed lines in B0092 | **PASS**: all 72 lines change, but only through the two global renderer changes (`doi:` → `doi: `; no `.` after a `?` title: Hoang-Thi, Xin, Christodoulou), except for exactly 24 keys. Those 24 are the 25 keys of the 2026-10-31 overrides minus Barber1984JPhysE, whose override was already applied in v6. This meets REV-M1f-1's verification criterion |
| 2. 25 overrides (2026-10-31) | **25/25 VERIFIED** against the source each names: 13 NLM Catalog UIDs (MedlineTA) all match; 4 PubMed efetch records (Chambers and Du issue years; Pulletz, Lange author forms) match; 4 web bylines (CVF, NeurIPS, BMVC list, nature.com) match; 5 LNCS volumes (9351, 11070, 11384, 15009, 15010) match Crossref's own `book_series_metadata` deposit; the PubMed conventions the overrides cite (CVPR volume = year; MICCAI volume = LNCS volume; NeurIPS 2022 volume 35; Biometrics Bulletin indexed as Biometrics) all confirmed. 0 NOT CONFIRMED |
| 3. 72 strings, field by field | **PASS**: 72/72 lines equal `cite.render_vancouver` of an entry rebuilt today from fresh Crossref + PubMed esummary with the overrides applied; 72/72 equal `render_vancouver` of the registry entry (`refs/prior_works_recon.json`), so 0 registry drift; 72/72 occur verbatim in `refs/prior_works_recon_strings.md`; registry key set = `refs/refs_in_recon.json` key set = list key set (72). For the 49 PubMed records: the DOI is in the esummary article IDs (49/49) and the journal = efetch MedlineTA (49/49) |
| 3b. Counts (`check_recon_draft.py`) | **PASS**: 84 instances / 72 distinct / 84 quote anchors / 0 slugs outside corpus / 0 orphans / 72 list entries / 0 cited-but-unlisted / 0 listed-but-uncited (identical to v6) |
| 4. Retraction / correction (all 72) | **PASS**: Crossref `update-to` empty 72/72, `updated-by` absent 72/72, no retraction/correction/concern relation (5 records carry only `has-review`, `has-preprint` or `is-referenced-by`); OpenAlex `is_retracted` = false 72/72 (DOI-exact record 72/72); PubMed (49): no Retraction/Erratum/Concern publication type, no RetractionIn / ErratumIn / ExpressionOfConcernIn / UpdateIn link (only 2 CommentIn on Nosek 2018). **0 / 0 / 0** |
| 5. Deliverable | **PASS**: `## References` holds 72 lines numbered 1–72, each equal to the v7 string with the key marker removed (72/72); in-text brackets use 1–72 only, all 72 used, none missing, first appearance in order 1…72; the flattened sequence of 84 bracket citations equals the v7 marker sequence mapped to list numbers (84/84); 0 `<!--`, 0 `-->`; no bracket in the abstract |
| 6. PLoS One Vancouver | **PASS with advisories**: six-then-et-al. rule 72/72 (17 entries with >6 authors show 6 + et al.); `doi: <DOI>` as the last element 72/72; 0 URLs; 0 `..` or `?.`; journal = NLM MedlineTA for 69/72 (49 PubMed + 20 overrides); of the other 3, Int J Comput Vis and Nat Mach Intell equal their NLM MedlineTA, and Handbook of Numerical Analysis has no NLM record. Seven remaining deviations are listed as advisory flags A1–A7 (§6) |

**Scoped verdict: `citation_check=PASS WITH FLAGS`.** The strict layer passes outright: no unresolvable entry, no string, key, order or DOI mismatch, no unverified override, no retraction, correction or expression of concern, and the deliverable list and brackets equal the draft's. The flags are advisory style or metadata-completeness items in seven strings (A1–A7, §6). None is a fidelity error against the databases; each needs either a PI choice or a new logged override.

---

## 1. Diff scope (v6 → v7)

Method: both drafts were split on `<!--block:BNNNN-->` markers. Both have 160 blocks in the same order (161 parts including the preamble).

| Item | Result |
|---|---|
| Blocks that differ | B0091, B0092 (= the patch's two `block_id`s and the apply report's `ops_applied`) |
| Blocks byte-identical | 158 + preamble |
| `# PIPELINE INTERNAL` section | byte-identical |
| B0091, B0092 bodies = patch `new_text` | yes, both |
| B0092 keys, v6 vs v7 | 72 = 72, same sequence |

**B0091.** v6: "…(`refs/prior_works_recon_strings.md`, 2026-10-17), listed below…". v7: "…(`refs/prior_works_recon_strings.md`, re-rendered 2026-10-31 with the verified metadata overrides of `refs/overrides.json`), listed below…". This closes 21_ flag F1. No other wording changed. (The roadmap description also mentions a registry size "73"; that number is not in v6's B0091, so there was nothing to remove.)

**B0092, which lines changed and why.** Each v6/v7 line pair was compared after removing the two global renderer changes of `tools/cite.py` (`doi:` → `doi: `; `?.` → `?`).
- After that normalisation, 48 lines are identical and 24 differ.
- The 24 are exactly {2026-10-31 override keys} − {Barber1984JPhysE}. Barber's journal override was already in v6's string (21_ §2b).
- `?.` occurred in v6 for Hoang-Thi 2021, Xin 2022 and Christodoulou 2024, and occurs 0 times in v7.
- `doi: 10.` occurs 72 times in v7, `doi:10` 0 times.

The renderer diff (`tools/cite.pre-round1f-20261031.py` → `tools/cite.py`) touches only `render_vancouver`: the `tend` rule for `?` titles and the space after `doi:`. Harvard and Nature renderers are unchanged.

---

## 2. The 25 overrides dated 2026-10-31

`refs/overrides.json` holds 30 entries. 25 carry `verified: 2026-10-31`. Of the 25, 17 are new since `overrides.pre-round1f-20261031.json` and 7 were extended. Barber dates from round 1e and was verified in 21_. It is re-queried here because it carries the date.

### 2.1 Per key

| # | Key | Field(s) overridden | Value in v7 | Source named → re-queried 2026-10-31 | Result |
|---|---|---|---|---|---|
| 1 | Kendall2018 | authors; journal; volume | Kendall A, Gal Y, Cipolla R; Proc IEEE Comput Soc Conf Comput Vis Pattern Recognit; 2018 | CVF Open Access page: `citation_author` Kendall, Gal, Cipolla (Crossref still returns Cipolla, Gal, Kendall). NLM UID 101492446: MedlineTA "Proc IEEE Comput Soc Conf Comput Vis Pattern Recognit", ISSN 1063-6919. PMID 31274971: CVPR 2018 paper with volume "2018" | **VERIFIED** |
| 2 | Kurin2022Unitary | authors; journal; volume | Kurin V, De Palma A, Kostrikov I, Whiteson S, Mudigonda PK; Adv Neural Inf Process Syst; 35 | NeurIPS page (hash 4f301ae9…): `citation_author` "De Palma, Alessandro" (Crossref: given "Alessandro De", family "Palma"). NLM UID 9607483: MedlineTA "Adv Neural Inf Process Syst", ISSN 1049-5258. Crossref container "Advances in Neural Information Processing Systems 35". 5 PubMed 2022 NeurIPS records (e.g. PMID 38149289): vol 35 | **VERIFIED** |
| 3 | Isensee2024nnUNetRevisited | volume; journal | 15009; Med Image Comput Comput Assist Interv | Springer chapter page not reachable (bot challenge). Crossref unixsd deposit of the chapter: `book_series_metadata` "Lecture Notes in Computer Science", MICCAI 2024 Part IX, `<volume>15009</volume>`. NLM UID 101249582: MedlineTA "Med Image Comput Comput Assist Interv". PMID 31573001: MICCAI 2018 chapter as "2018;11073:47-54" | **VERIFIED** |
| 4 | Myronenko2019AEReg | volume; journal | 11384; Brainlesion | Crossref unixsd: LNCS, BrainLes 2018 Part II, `<volume>11384</volume>`. NLM UID 101749001: MedlineTA "Brainlesion". PMID 31482151: "2019;11383:239-250" (Part I, same convention) | **VERIFIED** |
| 5 | Vandenhende2020Branched | authors; journal | Vandenhende S, Georgoulis S, Van Gool L, De Brabandere B; BMVC | BMVC 2020 accepted-papers list, paper 79 [213]: "Simon Vandenhende, Stamatios Georgoulis, Luc Van Gool and Bert De Brabandere", DOI 10.5244/C.34.59. Crossref keeps this order with the particles in the given name. NLM UID 101766207: MedlineTA "BMVC" | **VERIFIED** |
| 6 | Ronneberger2015UNet | volume; journal | 9351; Med Image Comput Comput Assist Interv | Crossref unixsd: LNCS, MICCAI 2015 Part III, `<volume>9351</volume>`. DNB record (ISBN 9783319245737): series 490/830 "Lecture Notes in Computer Science $v 9351". NLM UID 101249582 as #3 | **VERIFIED** |
| 7 | Christodoulou2024MICCAI | volume; journal | 15010; Med Image Comput Comput Assist Interv | Crossref unixsd: LNCS, MICCAI 2024 Part X, `<volume>15010</volume>`. OpenAlex biblio volume "LNCS-15010". NLM UID 101249582 | **VERIFIED** |
| 8 | Barber1984JPhysE | journal | J Phys E | NLM UID 1276760: MedlineTA "J Phys E", ISSN 0022-3735 (= Crossref ISSN), serial v. 3–22, 1970–1989 | **VERIFIED** |
| 9 | Albert2023ApplSci | journal | Appl Sci (Basel) | NLM UID 101633495: MedlineTA "Appl Sci (Basel)", ISSN 2076-3417 (= Crossref) | **VERIFIED** |
| 10 | Borji2018ImaVisComput | journal | Image Vis Comput | NLM UID 101151810: MedlineTA "Image Vis Comput", ISSN 0262-8856 (= Crossref) | **VERIFIED** |
| 11 | Caruana1997MTL | journal | Mach Learn | NLM UID 9881780: MedlineTA "Mach Learn", ISSN 0885-6125 / 1573-0565 (= Crossref) | **VERIFIED** |
| 12 | Lakens2018AMPPS | journal | Adv Methods Pract Psychol Sci | NLM UID 101731526: MedlineTA "Adv Methods Pract Psychol Sci", ISSN 2515-2459 / 2515-2467 (= Crossref) | **VERIFIED** |
| 13 | Scheel2021AMPPS | journal | Adv Methods Pract Psychol Sci | as #12 | **VERIFIED** |
| 14 | Willroth2024AMPPS | journal | Adv Methods Pract Psychol Sci | as #12 | **VERIFIED** |
| 15 | Wang2024TIM | journal | IEEE Trans Instrum Meas | NLM UID 422676: MedlineTA "IEEE Trans Instrum Meas", ISSN 0018-9456 (= Crossref). The doubled full stop of the Crossref short title "IEEE Trans. Instrum. Meas." is gone | **VERIFIED** |
| 16 | Yoon2024ProcIEEE | journal | Proc IEEE Inst Electr Electron Eng | NLM UID 9879073: MedlineTA "Proc IEEE Inst Electr Electron Eng", ISSN 0018-9219 / 1558-2256 (= Crossref) | **VERIFIED** |
| 17 | Wilcoxon1945 | journal | Biometrics | NLM UID 370625: MedlineTA "Biometrics", alternate titles "Biometrics bulletin", "BIOMETR. BULL.", serial "v. 1- Feb. 1945-". A catalog search for "Biometrics bulletin" returns only 370625; Crossref's ISSN 0099-4987 has no NLM record. PMID 20287815 (Satterthwaite 1946, Biometrics Bulletin vol 2(6)) is indexed as "Biometrics" | **VERIFIED** (see A5 for the page range) |
| 18 | Karani2018MICCAI | journal; volume | Med Image Comput Comput Assist Interv; 11070 | Crossref unixsd: LNCS, MICCAI 2018 Part I, `<volume>11070</volume>`, print ISBN 978-3-030-00927-4 (= the override's 9783030009274). DNB record: Part I, series LNCS (no volume subfield). NLM UID 101249582 | **VERIFIED** |
| 19 | Xin2022MTOHelp | journal; volume | Adv Neural Inf Process Syst; 35 | as #2 (UID 9607483; Crossref container "… Systems 35"; PubMed 2022 convention vol 35) | **VERIFIED** |
| 20 | Yu2024CVPR | journal; volume | Proc IEEE Comput Soc Conf Comput Vis Pattern Recognit; 2024 | UID 101492446 as #1. PMID 40115537: CVPR 2024 paper (doi 10.1109/cvpr52733.2024.01115) with volume "2024" | **VERIFIED** |
| 21 | Chambers2021NatHumBehav | year | 2022 | PubMed efetch PMID 34782730: PubDate 2022 Jan, vol 6(1):29-42, ArticleDate 2021-11-15; Crossref has online 2021-11-15 only | **VERIFIED** |
| 22 | Du2022EurRadiol | year | 2023 | PubMed efetch PMID 36355196: PubDate 2023 Apr, vol 33(4):2426-2438, ArticleDate 2022-11-10; Crossref has online 2022-11-10 only | **VERIFIED** |
| 23 | Pulletz2006ROI | authors | … van Genderingen HR … (8 authors) | PubMed efetch PMID 16636403: LastName "van Genderingen", Initials "HR"; the other 7 forms are identical as well. Crossref: family "Genderingen", given "Huibert R van" | **VERIFIED** |
| 24 | Renard2020SciRep | authors | Renard F, Guedria S, De Palma N, Vuillerme N | nature.com article page: displayed author name "Noel De Palma" (`citation_author` "Palma, Noel De"). Crossref: family "Palma", given "Noel De"; PubMed efetch: "Palma N" | **VERIFIED** against the byline the override names (note n2) |
| 25 | Lange2025StatMed | authors | Lange FJD, Wilcke JC, Hoffmann S, Herrmann M, Boulesteix AL | PubMed efetch PMID 41213159: Boulesteix, ForeName "Anne-Laure", Initials "AL"; Crossref given "Anne‐Laure" with U+2010, which `cite.authors` splits only on U+002D, giving "A" | **VERIFIED** |

**Tally: 25/25 VERIFIED, 0 NOT CONFIRMED.**

### 2.2 How the LNCS volumes were confirmed

The brief names the Springer chapter page, or Crossref/ISBN data, as the source for Karani's LNCS 11070.
- **Not usable:** link.springer.com returned a client bot challenge for all five chapters. Springer's citation-export endpoint (RIS, BibTeX) carries no series volume. OpenLibrary has no series field. Of the five ISBNs, DNB has records for two.
- **Used:** Crossref's XML deposit (`api.crossref.org/works/<DOI>.xml`) of each chapter. Its `<book_series_metadata>` element names the series "Lecture Notes in Computer Science" (ISSN 0302-9743 / 1611-3349), the volume title with its Part number, and the volume.
- **Result:** all five overrides are confirmed by Springer's own registration with Crossref. Ronneberger is also confirmed by DNB.

Note for the tool, no flag: Crossref's JSON (`/works/<DOI>`), which `cite.py` reads, drops the series volume for book chapters. That is why these five needed overrides. Reading `<book_series_metadata><volume>` from the XML would remove them.

---

## 3. The 72 strings of B0092, field by field

**Method** (as in 16_ Check A, run on all 72 rather than a subset):
- (a) For each line `N. <string> <!--key:KEY-->`, an entry was rebuilt from today's raw Crossref record and PubMed esummary using `tools/cite.py`'s own functions:
  - `authors()`: family + initials, deposited order;
  - `clean()`: title + subtitle;
  - `year()`: published-print → published-online → issued;
  - `pages()`: `page` or `article-number`;
  - journal: esummary `source` when the DOI is in PubMed, else Crossref `short-container-title`, else `container-title`.
- (b) The overrides of `refs/overrides.json` were applied to that entry.
- (c) `cite.render_vancouver(entry, N)` was compared byte-for-byte with the line.
- (d) `render_vancouver` of the registry entry in `refs/prior_works_recon.json` was compared too.

**Results:**
- **72/72 equal on both counts.** No field changed at the source since the 2026-10-31 17:55 render, and the registry holds no hand edit.
- 72/72 lines end with `doi: ` + the registry DOI.
- Crossref returns the same DOI for 72/72.
- For the 49 PubMed records, the esummary DOI list contains the registry DOI (49/49) and the rendered journal equals efetch `MedlineTA` (49/49).

Column key: Authors = number in the database → number rendered. Journal source = PubMed MedlineTA, override (the NLM Catalog value, §2), or Crossref short title. "Fresh = line" = (a)–(c); "Reg = line" = (d). Override column = the fields that the override changes relative to today's fresh record, with the override's verification date ("—" = no override). Status = §4 (Crossref, OpenAlex, PubMed).

| # | Key | Authors | Journal (source) | Year | Vol | Pages / art. no. | DOI | PMID | Fresh = line | Reg = line | Override applied | Retraction / correction |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | Frerichs2017TREND | 20 → 6 + et al. ✓ | Thorax (PubMed) ✓ | 2017 ✓ | 72 ✓ | 83-93 ✓ | 10.1136/thoraxjnl-2016-208357 ✓ | 27596161 | yes | yes | —  | none |
| 2 | Zhao2014PhysiolMeas | 5 → 5 (all) ✓ | Physiol Meas (PubMed) ✓ | 2014 ✓ | 35 ✓ | 1083-1093 ✓ | 10.1088/0967-3334/35/6/1083 ✓ | 24845059 | yes | yes | —  | none |
| 3 | Grychtol2014PLOSONE | 6 → 6 (all) ✓ | PLoS One (PubMed) ✓ | 2014 ✓ | 9 ✓ | e103045 ✓ | 10.1371/journal.pone.0103045 ✓ | 25110887 | yes | yes | —  | none |
| 4 | Zhou2023TPAMI | 5 → 5 (all) ✓ | IEEE Trans Pattern Anal Mach Intell (PubMed) ✓ | 2023 ✓ | 45 ✓ | 4396-4415 ✓ | 10.1109/tpami.2022.3195549 ✓ | 35914036 | yes | yes | year: 2022 -> 2023; volume: None -> 45; issue: None -> 4; pages: 1-20 -> 4396-4415 [2026-10-11] | none |
| 5 | Yoon2024ProcIEEE | 5 → 5 (all) ✓ | Proc IEEE Inst Electr Electron Eng (override) ✓ | 2024 ✓ | 112 ✓ | 1583-1609 ✓ | 10.1109/jproc.2024.3507831 ✓ | not indexed | yes | yes | journal: Proc. IEEE -> Proc IEEE Inst Electr Electron Eng [2026-10-31] | none |
| 6 | Leathard1994PhysiolMeas | 6 → 6 (all) ✓ | Physiol Meas (PubMed) ✓ | 1994 ✓ | 15 ✓ | A137-A146 ✓ | 10.1088/0967-3334/15/2a/018 ✓ | 8087036 | yes | yes | —  | none |
| 7 | Graf2017PLOSONE | 2 → 2 (all) ✓ | PLoS One (PubMed) ✓ | 2017 ✓ | 12 ✓ | e0188313 ✓ | 10.1371/journal.pone.0188313 ✓ | 29145478 | yes | yes | —  | none |
| 8 | Ko2021PhysiolMeas | 2 → 2 (all) ✓ | Physiol Meas (PubMed) ✓ | 2021 ✓ | 42 ✓ | 025002 ✓ | 10.1088/1361-6579/abe021 ✓ | 33498021 | yes | yes | —  | none |
| 9 | Ko2021PLOSONE | 2 → 2 (all) ✓ | PLoS One (PubMed) ✓ | 2021 ✓ | 16 ✓ | e0246071 ✓ | 10.1371/journal.pone.0246071 ✓ | 33529234 | yes | yes | —  | none |
| 10 | Ko2025CurrMedImaging | 3 → 3 (all) ✓ | Curr Med Imaging (PubMed) ✓ | 2025 ✓ | 21 ✓ | e15734056408077 ✓ | 10.2174/0115734056408077250610070821 ✓ | 40611416 | yes | yes | —  | none |
| 11 | Zhang2022PhysiolMeas | 7 → 6 + et al. ✓ | Physiol Meas (PubMed) ✓ | 2022 ✓ | 43 ✓ | 125005 ✓ | 10.1088/1361-6579/ac9c44 ✓ | 36265475 | yes | yes | —  | none |
| 12 | Vandenhende2021 | 6 → 6 (all) ✓ | IEEE Trans Pattern Anal Mach Intell (PubMed) ✓ | 2022 ✓ | 44 ✓ | 3614-3633 ✓ | 10.1109/tpami.2021.3054719 ✓ | 33497328 | yes | yes | year: 2021 -> 2022; volume: None -> 44; issue: None -> 7; pages: 1-1 -> 3614-3633 [2026-09-26] | none |
| 13 | Wang2024TIM | 4 → 4 (all) ✓ | IEEE Trans Instrum Meas (override) ✓ | 2024 ✓ | 73 ✓ | 1-16 ✓ | 10.1109/tim.2024.3369160 ✓ | not indexed | yes | yes | journal: IEEE Trans. Instrum. Meas. -> IEEE Trans Instrum Meas [2026-10-31] | none |
| 14 | Yu2024CMPB | 5 → 5 (all) ✓ | Comput Methods Programs Biomed (PubMed) ✓ | 2024 ✓ | 243 ✓ | 107861 ✓ | 10.1016/j.cmpb.2023.107861 ✓ | 37931580 | yes | yes | —  | none |
| 15 | Hamilton2018TMI | 2 → 2 (all) ✓ | IEEE Trans Med Imaging (PubMed) ✓ | 2018 ✓ | 37 ✓ | 2367-2377 ✓ | 10.1109/tmi.2018.2828303 ✓ | 29994023 | yes | yes | —  | none |
| 16 | Herzberg2023PhysiolMeas | 3 → 3 (all) ✓ | Physiol Meas (PubMed) ✓ | 2023 ✓ | 44 ✓ | 125008 ✓ | 10.1088/1361-6579/ad0b3d ✓ | 37944184 | yes | yes | title: Domain independent post-processing with graph U-nets: applications to electrical impedance tomographic imaging⋆ -> Domain independent post-processing with graph U-nets: applications to electrical impedance tomographic imaging [2026-10-07] | none |
| 17 | Zhang2022FBB | 8 → 6 + et al. ✓ | Front Bioeng Biotechnol (PubMed) ✓ | 2022 ✓ | 10 ✓ | 1019531 ✓ | 10.3389/fbioe.2022.1019531 ✓ | 36588934 | yes | yes | —  | none |
| 18 | Denker2025HandbNumerAnal | 8 → 6 + et al. ✓ | Handbook of Numerical Analysis (Crossref) ✓ | 2025 ✓ | — ✓ | 127-175 ✓ | 10.1016/bs.hna.2025.09.003 ✓ | not indexed | yes | yes | —  | none |
| 19 | Zech2018PLoSMed | 6 → 6 (all) ✓ | PLoS Med (PubMed) ✓ | 2018 ✓ | 15 ✓ | e1002683 ✓ | 10.1371/journal.pmed.1002683 ✓ | 30399157 | yes | yes | —  | none |
| 20 | AlBadawy2018MedPhys | 3 → 3 (all) ✓ | Med Phys (PubMed) ✓ | 2018 ✓ | 45 ✓ | 1150-1158 ✓ | 10.1002/mp.12752 ✓ | 29356028 | yes | yes | —  | none |
| 21 | Liu2020TMI | 4 → 4 (all) ✓ | IEEE Trans Med Imaging (PubMed) ✓ | 2020 ✓ | 39 ✓ | 2713-2724 ✓ | 10.1109/tmi.2020.2974574 ✓ | 32078543 | yes | yes | —  | none |
| 22 | HoangThi2021DIII | 6 → 6 (all) ✓ | Diagn Interv Imaging (PubMed) ✓ | 2021 ✓ | 102 ✓ | 691-695 ✓ | 10.1016/j.diii.2021.10.001 ✓ | 34686464 | yes | yes | —  | none |
| 23 | Zeng2022MedPhys | 7 → 6 + et al. ✓ | Med Phys (PubMed) ✓ | 2022 ✓ | 49 ✓ | 836-853 ✓ | 10.1002/mp.15430 ✓ | 34954845 | yes | yes | —  | none |
| 24 | Hamilton2019PhysiolMeas | 4 → 4 (all) ✓ | Physiol Meas (PubMed) ✓ | 2019 ✓ | 40 ✓ | 074002 ✓ | 10.1088/1361-6579/ab21b2 ✓ | 31091516 | yes | yes | —  | none |
| 25 | Karani2018MICCAI | 4 → 4 (all) ✓ | Med Image Comput Comput Assist Interv (override) ✓ | 2018 ✓ | 11070 ✓ | 476-484 ✓ | 10.1007/978-3-030-00928-1_54 ✓ | not indexed | yes | yes | journal: Lecture Notes in Computer Science -> Med Image Comput Comput Assist Interv; volume: None -> 11070 [2026-10-31] | none |
| 26 | Holzschuh2024RadiatOncol | 17 → 6 + et al. ✓ | Radiat Oncol (PubMed) ✓ | 2024 ✓ | 19 ✓ | 106 ✓ | 10.1186/s13014-024-02491-w ✓ | 39113123 | yes | yes | —  | none |
| 27 | Lange2025StatMed | 5 → 5 (all) ✓ | Stat Med (PubMed) ✓ | 2025 ✓ | 44 ✓ | e70303 ✓ | 10.1002/sim.70303 ✓ | 41213159 | yes | yes | authors [2026-10-31] | none |
| 28 | Adler2006EIDORS | 2 → 2 (all) ✓ | Physiol Meas (PubMed) ✓ | 2006 ✓ | 27 ✓ | S25-S42 ✓ | 10.1088/0967-3334/27/5/s03 ✓ | 16636416 | yes | yes | —  | none |
| 29 | Gagnon2010TBME | 4 → 4 (all) ✓ | IEEE Trans Biomed Eng (PubMed) ✓ | 2010 ✓ | 57 ✓ | 2257-2266 ✓ | 10.1109/tbme.2010.2052618 ✓ | 20550982 | yes | yes | —  | none |
| 30 | Adler2009GREIT | 19 → 6 + et al. ✓ | Physiol Meas (PubMed) ✓ | 2009 ✓ | 30 ✓ | S35-S55 ✓ | 10.1088/0967-3334/30/6/s03 ✓ | 19491438 | yes | yes | —  | none |
| 31 | Adler1996TMI | 2 → 2 (all) ✓ | IEEE Trans Med Imaging (PubMed) ✓ | 1996 ✓ | 15 ✓ | 170-179 ✓ | 10.1109/42.491418 ✓ | 18215899 | yes | yes | —  | none |
| 32 | Barber1984JPhysE | 2 → 2 (all) ✓ | J Phys E (override) ✓ | 1984 ✓ | 17 ✓ | 723-733 ✓ | 10.1088/0022-3735/17/9/002 ✓ | not indexed | yes | yes | journal: J. Phys. E: Sci. Instrum. -> J Phys E [2026-10-31] | none |
| 33 | Thurk2019PhysiolMeas | 7 → 6 + et al. ✓ | Physiol Meas (PubMed) ✓ | 2019 ✓ | 40 ✓ | 094003 ✓ | 10.1088/1361-6579/ab248e ✓ | 31125984 | yes | yes | —  | none |
| 34 | Ronneberger2015UNet | 3 → 3 (all) ✓ | Med Image Comput Comput Assist Interv (override) ✓ | 2015 ✓ | 9351 ✓ | 234-241 ✓ | 10.1007/978-3-319-24574-4_28 ✓ | not indexed | yes | yes | volume: None -> 9351; journal: Lecture Notes in Computer Science -> Med Image Comput Comput Assist Interv [2026-10-31] | none |
| 35 | Vandenhende2020Branched | 4 → 4 (all) ✓ | BMVC (override) ✓ | 2020 ✓ | — ✓ | 59 ✓ | 10.5244/c.34.59 ✓ | not indexed | yes | yes | authors; journal: Proceedings of the British Machine Vision Conference 2020 -> BMVC [2026-10-31] | none |
| 36 | Isensee2024nnUNetRevisited | 7 → 6 + et al. ✓ | Med Image Comput Comput Assist Interv (override) ✓ | 2024 ✓ | 15009 ✓ | 488-498 ✓ | 10.1007/978-3-031-72114-4_47 ✓ | not indexed | yes | yes | volume: None -> 15009; journal: Lecture Notes in Computer Science -> Med Image Comput Comput Assist Interv [2026-10-31] | none |
| 37 | Caruana1997MTL | 1 → 1 (all) ✓ | Mach Learn (override) ✓ | 1997 ✓ | 28 ✓ | 41-75 ✓ | 10.1023/a:1007379606734 ✓ | not indexed | yes | yes | journal: Machine Learning -> Mach Learn [2026-10-31] | none |
| 38 | Kurin2022Unitary | 5 → 5 (all) ✓ | Adv Neural Inf Process Syst (override) ✓ | 2022 ✓ | 35 ✓ | 12169-12183 ✓ | 10.52202/068431-0884 ✓ | not indexed | yes | yes | authors; journal: Advances in Neural Information Processing Systems 35 -> Adv Neural Inf Process Syst; volume: None -> 35 [2026-10-31] | none |
| 39 | Xin2022MTOHelp | 5 → 5 (all) ✓ | Adv Neural Inf Process Syst (override) ✓ | 2022 ✓ | 35 ✓ | 13597-13609 ✓ | 10.52202/068431-0988 ✓ | not indexed | yes | yes | journal: Advances in Neural Information Processing Systems 35 -> Adv Neural Inf Process Syst; volume: None -> 35 [2026-10-31] | none |
| 40 | Kendall2018 | 3 → 3 (all) ✓ | Proc IEEE Comput Soc Conf Comput Vis Pattern Recognit (override) ✓ | 2018 ✓ | 2018 ✓ | 7482-7491 ✓ | 10.1109/cvpr.2018.00781 ✓ | not indexed | yes | yes | authors; journal: 2018 IEEE/CVF Conference on Computer Vision and Pattern Recognition -> Proc IEEE Comput Soc Conf Comput Vis Pattern Recognit; volume: None -> 2018 [2026-10-31] | none |
| 41 | Renard2020SciRep | 4 → 4 (all) ✓ | Sci Rep (PubMed) ✓ | 2020 ✓ | 10 ✓ | 13724 ✓ | 10.1038/s41598-020-69920-0 ✓ | 32792540 | yes | yes | authors [2026-10-31] | none |
| 42 | Pulletz2006ROI | 8 → 6 + et al. ✓ | Physiol Meas (PubMed) ✓ | 2006 ✓ | 27 ✓ | S115-S127 ✓ | 10.1088/0967-3334/27/5/s10 ✓ | 16636403 | yes | yes | authors [2026-10-31] | none |
| 43 | Jeschke2025Sensors | 6 → 6 (all) ✓ | Sensors (Basel) (PubMed) ✓ | 2025 ✓ | 25 ✓ | 6543 ✓ | 10.3390/s25216543 ✓ | 41228767 | yes | yes | —  | none |
| 44 | Yu2024CVPR | 6 → 6 (all) ✓ | Proc IEEE Comput Soc Conf Comput Vis Pattern Recognit (override) ✓ | 2024 ✓ | 2024 ✓ | 21897-21908 ✓ | 10.1109/cvpr52733.2024.02068 ✓ | not indexed | yes | yes | journal: 2024 IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR) -> Proc IEEE Comput Soc Conf Comput Vis Pattern Recognit; volume: None -> 2024 [2026-10-31] | none |
| 45 | Willroth2024AMPPS | 2 → 2 (all) ✓ | Adv Methods Pract Psychol Sci (override) ✓ | 2024 ✓ | 7 ✓ | 25152459231213802 ✓ | 10.1177/25152459231213802 ✓ | not indexed | yes | yes | journal: Advances in Methods and Practices in Psychological Science -> Adv Methods Pract Psychol Sci [2026-10-31] | none |
| 46 | Wilcoxon1945 | 1 → 1 (all) ✓ | Biometrics (override) ✓ | 1945 ✓ | 1 ✓ | 80 ✓ | 10.2307/3001968 ✓ | not indexed | yes | yes | journal: Biometrics Bulletin -> Biometrics [2026-10-31] | none |
| 47 | Schuirmann1987JPharmacokinet | 1 → 1 (all) ✓ | J Pharmacokinet Biopharm (PubMed) ✓ | 1987 ✓ | 15 ✓ | 657-680 ✓ | 10.1007/bf01068419 ✓ | 3450848 | yes | yes | —  | none |
| 48 | Lakens2017SPPS | 1 → 1 (all) ✓ | Soc Psychol Personal Sci (PubMed) ✓ | 2017 ✓ | 8 ✓ | 355-362 ✓ | 10.1177/1948550617697177 ✓ | 28736600 | yes | yes | —  | none |
| 49 | Lakens2018AMPPS | 3 → 3 (all) ✓ | Adv Methods Pract Psychol Sci (override) ✓ | 2018 ✓ | 1 ✓ | 259-269 ✓ | 10.1177/2515245918770963 ✓ | not indexed | yes | yes | journal: Advances in Methods and Practices in Psychological Science -> Adv Methods Pract Psychol Sci [2026-10-31] | none |
| 50 | Lakens2013EffectSize | 1 → 1 (all) ✓ | Front Psychol (PubMed) ✓ | 2013 ✓ | 4 ✓ | 863 ✓ | 10.3389/fpsyg.2013.00863 ✓ | 24324449 | yes | yes | pages:  -> 863 [2026-10-07] | none |
| 51 | Christodoulou2024MICCAI | 22 → 6 + et al. ✓ | Med Image Comput Comput Assist Interv (override) ✓ | 2024 ✓ | 15010 ✓ | 124-132 ✓ | 10.1007/978-3-031-72117-5_12 ✓ | not indexed | yes | yes | volume: None -> 15010; journal: Lecture Notes in Computer Science -> Med Image Comput Comput Assist Interv [2026-10-31] | none |
| 52 | Myronenko2019AEReg | 1 → 1 (all) ✓ | Brainlesion (override) ✓ | 2019 ✓ | 11384 ✓ | 311-320 ✓ | 10.1007/978-3-030-11726-9_28 ✓ | not indexed | yes | yes | volume: None -> 11384; journal: Lecture Notes in Computer Science -> Brainlesion [2026-10-31] | none |
| 53 | Venkatesh2026MedPhys | 4 → 4 (all) ✓ | Med Phys (PubMed) ✓ | 2026 ✓ | 53 ✓ | e70414 ✓ | 10.1002/mp.70414 ✓ | 41933401 | yes | yes | —  | none |
| 54 | Grychtol2014PhysiolMeas | 2 → 2 (all) ✓ | Physiol Meas (PubMed) ✓ | 2014 ✓ | 35 ✓ | 1035-1050 ✓ | 10.1088/0967-3334/35/6/1035 ✓ | 24844670 | yes | yes | —  | none |
| 55 | Albert2023ApplSci | 8 → 6 + et al. ✓ | Appl Sci (Basel) (override) ✓ | 2023 ✓ | 13 ✓ | 8923 ✓ | 10.3390/app13158923 ✓ | not indexed | yes | yes | journal: Applied Sciences -> Appl Sci (Basel) [2026-10-31] | none |
| 56 | Delisle2021MedIA | 4 → 4 (all) ✓ | Med Image Anal (PubMed) ✓ | 2021 ✓ | 74 ✓ | 102191 ✓ | 10.1016/j.media.2021.102191 ✓ | 34509168 | yes | yes | —  | none |
| 57 | Yan2020RadiolAI | 7 → 6 + et al. ✓ | Radiol Artif Intell (PubMed) ✓ | 2020 ✓ | 2 ✓ | e190195 ✓ | 10.1148/ryai.2020190195 ✓ | 33937833 | yes | yes | —  | none |
| 58 | Martensson2020MedIA | 25 → 6 + et al. ✓ | Med Image Anal (PubMed) ✓ | 2020 ✓ | 66 ✓ | 101714 ✓ | 10.1016/j.media.2020.101714 ✓ | 33007638 | yes | yes | —  | none |
| 59 | Castro2020NatCommun | 3 → 3 (all) ✓ | Nat Commun (PubMed) ✓ | 2020 ✓ | 11 ✓ | 3673 ✓ | 10.1038/s41467-020-17478-w ✓ | 32699250 | yes | yes | —  | none |
| 60 | Kamann2021IJCV | 2 → 2 (all) ✓ | Int J Comput Vis (Crossref) ✓ | 2021 ✓ | 129 ✓ | 462-483 ✓ | 10.1007/s11263-020-01383-2 ✓ | not indexed | yes | yes | —  | none |
| 61 | Boone2023NeuroImage | 13 → 6 + et al. ✓ | Neuroimage (PubMed) ✓ | 2023 ✓ | 278 ✓ | 120289 ✓ | 10.1016/j.neuroimage.2023.120289 ✓ | 37495197 | yes | yes | —  | none |
| 62 | Du2022EurRadiol | 7 → 6 + et al. ✓ | Eur Radiol (PubMed) ✓ | 2023 ✓ | 33 ✓ | 2426-2438 ✓ | 10.1007/s00330-022-09229-w ✓ | 36355196 | yes | yes | year: 2022 -> 2023 [2026-10-31] | none |
| 63 | Billot2023MedIA | 8 → 6 + et al. ✓ | Med Image Anal (PubMed) ✓ | 2023 ✓ | 86 ✓ | 102789 ✓ | 10.1016/j.media.2023.102789 ✓ | 36857946 | yes | yes | —  | none |
| 64 | Scheel2021AMPPS | 3 → 3 (all) ✓ | Adv Methods Pract Psychol Sci (override) ✓ | 2021 ✓ | 4 ✓ | 25152459211007467 ✓ | 10.1177/25152459211007467 ✓ | not indexed | yes | yes | journal: Advances in Methods and Practices in Psychological Science -> Adv Methods Pract Psychol Sci [2026-10-31] | none |
| 65 | McGreivy2024NatMachIntell | 2 → 2 (all) ✓ | Nat Mach Intell (Crossref) ✓ | 2024 ✓ | 6 ✓ | 1256-1269 ✓ | 10.1038/s42256-024-00897-5 ✓ | not indexed | yes | yes | —  | none |
| 66 | Borji2018ImaVisComput | 1 → 1 (all) ✓ | Image Vis Comput (override) ✓ | 2018 ✓ | 69 ✓ | 1-8 ✓ | 10.1016/j.imavis.2017.10.001 ✓ | not indexed | yes | yes | journal: Image and Vision Computing -> Image Vis Comput [2026-10-31] | none |
| 67 | Varoquaux2022NPJDigitMed | 2 → 2 (all) ✓ | NPJ Digit Med (PubMed) ✓ | 2022 ✓ | 5 ✓ | 48 ✓ | 10.1038/s41746-022-00592-y ✓ | 35413988 | yes | yes | —  | none |
| 68 | Nosek2018Prereg | 4 → 4 (all) ✓ | Proc Natl Acad Sci U S A (PubMed) ✓ | 2018 ✓ | 115 ✓ | 2600-2606 ✓ | 10.1073/pnas.1708274114 ✓ | 29531091 | yes | yes | —  | none |
| 69 | Chambers2021NatHumBehav | 2 → 2 (all) ✓ | Nat Hum Behav (PubMed) ✓ | 2022 ✓ | 6 ✓ | 29-42 ✓ | 10.1038/s41562-021-01193-7 ✓ | 34782730 | yes | yes | year: 2021 -> 2022 [2026-10-31] | none |
| 70 | Pawel2023BiomJ | 3 → 3 (all) ✓ | Biom J (PubMed) ✓ | 2024 ✓ | 66 ✓ | 2200091 ✓ | 10.1002/bimj.202200091 ✓ | 36890629 | yes | yes | —  | none |
| 71 | Boyle2011PhysiolMeas | 2 → 2 (all) ✓ | Physiol Meas (PubMed) ✓ | 2011 ✓ | 32 ✓ | 745-754 ✓ | 10.1088/0967-3334/32/7/s02 ✓ | 21646710 | yes | yes | —  | none |
| 72 | Boulesteix2013PLOSONE | 3 → 3 (all) ✓ | PLoS One (PubMed) ✓ | 2013 ✓ | 8 ✓ | e61562 ✓ | 10.1371/journal.pone.0061562 ✓ | 23637855 | yes | yes | —  | none |

Cross-check against PubMed beyond what the renderer uses (49 records, year / volume / pages / first six authors). Differences other than the logged overrides:
- Leathard 1994: PubMed volume "15 Suppl 2a" vs string "15" (advisory A6).
- Pawel 2024: PubMed pagination "e2200091" vs Crossref article number "2200091" (advisory A4).
- Initials only, no flag: Amato MBP vs PubMed "Amato MB" (Frerichs 2017), Lionheart WRB vs "Lionheart WR" (Adler 2006), Eugster MJA vs "Eugster MJ" (Boulesteix 2013). Crossref deposits the fuller given names, so both forms are correct initials of the same person (note n3).
- Renard 2020 "De Palma N" vs PubMed "Palma N": the logged override (§2, #24).

Counts, `python3 -X utf8 tools/check_recon_draft.py RECON_paper/manuscript/23_DRAFT_v7.md` from the project root:

```
== citations ==
  instances: 84; distinct: 72; anchors: {'quote': 84}
  slugs outside corpus: []
  corpus entries never cited (orphans, 0): []
  reference-list entries: 72; cited-but-unlisted: []; listed-but-uncited: []
```

Identical to v6. Outside citation scope: the same script reports 7,998 main-text words (ceiling 8,000) and an abstract of 296 words (≤300), unchanged, because B0091/B0092 are in the References section.

---

## 4. Retraction, correction, expression of concern (all 72; 16_ §10 action 13)

| Source (queried 2026-10-31) | Result |
|---|---|
| Crossref `update-to` (Retraction Watch and publisher notices) | empty for 72/72 |
| Crossref `updated-by` | absent for 72/72 |
| Crossref `relation` | 67/72 empty. 5 carry only non-adverse relations: Frerichs 2017 `has-review`, Willroth 2024 `has-review`, Lakens 2017 `has-preprint`, Nosek 2018 `has-preprint`, Ronneberger 2015 `is-referenced-by`. No `is-retracted-by`, `is-corrected-by`, `has-expression-of-concern` or erratum relation |
| OpenAlex `is_retracted` | false for 72/72; the OpenAlex record's DOI equals the registry DOI for 72/72 |
| PubMed publication types (49 indexed) | no "Retracted Publication", "Retraction of Publication", "Published Erratum" or "Expression of Concern" |
| PubMed CommentsCorrections (49) | no RetractionIn / ErratumIn / ExpressionOfConcernIn / UpdateIn / CorrectedandRepublishedIn; the only links are 2 × CommentIn on Nosek 2018 (PNAS commentary, not a correction) |
| Not in PubMed (23) | status rests on Crossref + OpenAlex: Albert 2023, Barber 1984, Borji 2018, Caruana 1997, Christodoulou 2024, Denker 2025, Isensee 2024, Kamann 2021, Karani 2018, Kendall 2018, Kurin 2022, Lakens 2018, McGreivy 2024, Myronenko 2019, Ronneberger 2015, Scheel 2021, Vandenhende 2020, Wang 2024, Wilcoxon 1945, Willroth 2024, Xin 2022, Yoon 2024, Yu 2024b (CVPR) |

**0 retractions, 0 corrections, 0 expressions of concern.** Barber 1984 coverage note from 21_ §3 stands: OpenAlex and Semantic Scholar conflate this DOI's record with a 1989 JBIS item, so the Crossref result is the operative one for Barber.

---

## 5. Deliverable `submission_PLOS_20261031/Manuscript.md`

| Check | Result |
|---|---|
| Identity | byte-identical to `RECON_paper/manuscript/24_SUBMISSION_plos_v7.md` (sha256 ed42a4db7204…) |
| `## References` | 72 non-empty lines, numbered `1.` … `72.` without gaps, between `## References` and `## Supporting information` |
| List strings vs v7 B0092 | 72/72 byte-identical after removing `N. ` and ` <!--key:KEY-->` |
| In-text brackets (text before `## References`) | 74 bracket groups, all of the form `[n]` or `[n, m, …]`, no ranges; numbers used = {1…72}, none outside 1–72, none missing |
| Order of first appearance | 1, 2, …, 72 (citation-sequence rule met) |
| Bracket sequence vs draft markers | the 84 citations, flattened in reading order, equal the 84 `<!--ref:KEY-->` markers of v7 mapped to their list numbers, position by position (84/84). So each bracket points to the right work |
| Abstract | no bracket (PLoS: no citations in abstracts) |
| After the list (Supporting information) | no numeric bracket |
| Comment markers | 0 `<!--`, 0 `-->`, 0 `ref:` / `key:` / `block:` tokens |

Outside citation scope, recorded for the package check: the deliverable renumbers tables and S-items (not checked here). It still carries six `[MATERIAL GAP: …]` placeholders: companion preprint DOI (lines 30, 240), Zenodo DOI (lines 133, 244), repository tag (lines 133, 244). None is a reference-list item. The companion stays uncited, as PLoS One requires for a manuscript under review (21_ §6).

---
## 6. PLoS One Vancouver conformance

The requirements are those of `refs/01_JOURNAL_REQUIREMENTS_PLOSONE.md` row "參考文獻". They were re-read today on the live PLOS ONE submission-guidelines page: citation-sequence numbering in square brackets; "first six authors, et al."; NCBI journal abbreviations; the DOI at the end as "doi: 10.xxxx", not shortened and not a URL; no citations in the abstract.

| Rule | Result |
|---|---|
| Six authors, then et al. | 72/72. The 17 entries with more than six authors show exactly six + ", et al."; the 55 with six or fewer show all, with no et al. |
| `doi: <DOI>` as the last element, full DOI, no URL | 72/72 end with `doi: ` + the registry DOI; 0 `http`, 0 `www.` |
| NLM journal abbreviation | 69/72 equal an NLM MedlineTA: 49 from PubMed (= efetch MedlineTA), 20 from overrides (= NLM Catalog, §2). Of the other 3, Kamann 2021 "Int J Comput Vis" (UID 101189508) and McGreivy 2024 "Nat Mach Intell" (UID 101740243) equal MedlineTA by coincidence of the Crossref short title. Denker 2025 "Handbook of Numerical Analysis" has no NLM record (A1) |
| Punctuation | 0 `..`, 0 `?.`, 0 doubled spaces |
| Numbered in order of first citation; brackets in text | yes (§5) |
| Citable sources | 72 published works (61 journal articles, 6 book chapters, 5 proceedings papers); no preprint, unaccepted manuscript or "in press"; the companion paper is not cited (21_ §6 unchanged) |

16_ §1 rendering items, status after round 1f:
- **Closed:** F1 (NLM abbreviations), F2 (doubled full stop, Wang), F3 (`?.`), F5 (Karani volume), F6 (`doi: `), F7 (issue years, Chambers and Du), F8 (particles and initials: van Genderingen HR, De Palma N, Boulesteix AL).
- **Still open, as advisories:** F4 (A1, A3), F9 (A2), F11 (A7).
- **F10** (title capitalisation as deposited): PLOS prescribes no title case, so no flag.

### Advisory flags (no fidelity error; each string equals the database record or a verified override)

**A1. Denker2025HandbNumerAnal (no. 18), book chapter in journal form.**
- v7: "Handbook of Numerical Analysis. 2025:127-175. doi: 10.1016/bs.hna.2025.09.003".
- Crossref XML: the chapter sits in volume **26**, "Machine Learning Solutions for Inverse Problems: Part A", of the book series *Handbook of Numerical Analysis* (ISSN 1570-8659).
- The NLM Catalog has no record for the series.
- PLOS's book-chapter model is "In: <editors>, editors. <Book>. <Place>: <Publisher>; <year>. pp. <pages>."
- Options:
  1. A logged override adding volume "26", which gives "Handbook of Numerical Analysis. 2025;26:127-175". This can be verified now.
  2. The chapter form. It needs the volume editors, place and publisher, which this check did not verify.

**A2. Wang2024TIM (no. 13), pages "1-16".**
- Crossref deposits `first_page` 1 / `last_page` 16, which is the article's own page count. IEEE TIM articles are identified by an article number.
- The Crossref `item_number` 10454092 is the IEEE Xplore document number, not the TIM article number.
- The article number was not verified here. It needs IEEE Xplore; if found, it goes in through a logged override. Otherwise "1-16" stays faithful to the deposit. (16_ F9.)

**A3. Proceedings and LNCS chapters in NLM journal form** (16_ F4):
- Kendall 2018 and Yu 2024b: "Proc IEEE Comput Soc Conf Comput Vis Pattern Recognit. 2018;2018:…", "…2024;2024:…".
- Kurin 2022 and Xin 2022: "Adv Neural Inf Process Syst. 2022;35:…".
- Vandenhende 2020: "BMVC. 2020:59". The 59 is the BMVC paper number, Crossref `item_number`.
- The 5 LNCS chapters: "Med Image Comput Comput Assist Interv. <year>;<LNCS vol>:…" and "Brainlesion. 2019;11384:…".

These are exactly PubMed's own forms (verified §2). PLOS gives no conference-paper model, so this is defensible. The overrides already record it as a PI choice against the proceedings or chapter form. No action unless the PI prefers that form.

**A4. Pawel2023BiomJ (no. 70), article number without the "e".**
- v7: "Biom J. 2024;66:2200091".
- PubMed PMID 36890629 MedlinePgn: "e2200091". Crossref `article-number`: "2200091".
- A logged override `pages: e2200091` (source PubMed efetch) would align it with NLM.

**A5. Wilcoxon1945 (no. 46), first page only.**
- v7: "Biometrics. 1945;1:80". Crossref `first_page` 80 with no last page; OpenAlex biblio 80–80.
- The article is usually cited as pp. 80–83, but JSTOR (the printed-issue source) served a bot challenge today, so the last page is **not verified** here.
- The journal override itself is VERIFIED (§2 #17). If the PI wants the range, check JSTOR stable/3001968 and log `pages: 80-83`.
- The PI may still prefer the printed title "Biometrics Bulletin" (the override's own note). NLM files it under "Biometrics".

**A6. Leathard1994PhysiolMeas (no. 6), supplement not shown.**
- v7: "1994;15:A137-A146". PubMed: volume "15 Suppl 2a", pages A137-46.
- The NLM form is "1994;15 Suppl 2a:A137-46". Optional override.

**A7. Non-ASCII hyphens in titles, as deposited** (16_ F11):
- U+2010 HYPHEN in AlBadawy 2018 ("cross‐institutional"), Zeng 2022 ("learning‐based") and Venkatesh 2026 ("real‐time").
- U+2013 EN DASH in Du 2023 ("learning–based"). PubMed's title has an ASCII hyphen ("Deep learning-based harmonization").
- Typesetting usually normalises these. Changing them in the string would need a title override, which R12d permits only with a logged source.

**A8. PLOS example punctuation (cosmetic).**
- PLOS's published-article example writes the pages after a space, "2011;10: 1576-1588", and ends with a full stop after the DOI ("doi: 10.1016/j.molimm.2014.11.005.").
- The strings use the NLM form "2011;10:1576-1588" and no final full stop.
- PLOS's text requires only "doi: " with the full DOI at the end. This is left to PLOS copyediting; a two-character renderer change would match the example exactly if the PI wants it.

---

## 7. Flags and notes raised by this re-check

**Flags (all advisory, §6):** A1 Denker 2025 chapter form / volume 26; A2 Wang 2024 article number; A3 proceedings and LNCS in NLM journal form (PI choice, already recorded); A4 Pawel 2024 "e2200091"; A5 Wilcoxon 1945 last page unverified; A6 Leathard 1994 "Suppl 2a"; A7 U+2010/U+2013 in four titles; A8 PLOS example spacing and final full stop.

No strict-layer flag:
- no string, order, key or DOI mismatch;
- no override NOT CONFIRMED;
- no retraction, correction or expression of concern;
- no deliverable mismatch.

21_ flag F1 (stale date in B0091) is **closed** by REV-M1f-2.

Notes (no flag):
- **n1 (§2.2)**: `cite.py` reads Crossref JSON, which drops the LNCS series volume. The volume is in Crossref XML `<book_series_metadata><volume>`, which would make the five volume overrides unnecessary.
- **n2 (§2 #24)**: Renard 2020: the byline "Noel De Palma" (override) differs from PubMed's "Palma N". The override follows the source it names and the treatment of Kurin's "De Palma A".
- **n3 (§3)**: three entries carry a third initial that PubMed omits (Amato MBP, Lionheart WRB, Eugster MJA). Crossref deposits the fuller given names; both are correct.
- **n4**: `refs/overrides.json` still holds `Rusak2020ECCV`, whose key is not in the RECON registry. `apply_ref_overrides.py` skips keys a registry lacks, so it has no effect.
- **n5 (§5)**: the deliverable carries six `[MATERIAL GAP]` placeholders: companion preprint DOI (lines 30, 240), Zenodo DOI (lines 133, 244), repository tag (lines 133, 244). They are outside citation scope but must be filled or confirmed before upload.
- **n6 (§3)**: Barber 1984: OpenAlex and Semantic Scholar conflation, as in 21_ §3; keep `pmid: null`.

---

## 8. Items carried, not in this scope

- Quote anchors (84/84 VERIFIED) and claim–source context: inherited from 16_ / 16b / 21_. All 158 citing and non-citing blocks outside B0091/B0092 are byte-identical to v6, so no anchor or clause can have changed.
- N1 of 16b (B0074) and m4 (B0014): unchanged blocks; status as recorded by round 1d and the re-review.
- 16_ §10 action 13 (pre-submission retraction re-run of all 72): **done here** (§4). If submission slips well past 2026-10-31, repeat §4 on the day of upload.
- Table and S-item renumbering in the deliverable: format-convert scope, not checked.

---

## 9. Verdict

| Item | Verdict |
|---|---|
| 1. Diff scope | PASS: exactly B0091 and B0092; 158 blocks byte-identical; 72 keys in unchanged order |
| 1b. Changed lines | PASS: 24 override keys + two global renderer changes, nothing else |
| 2. 25 overrides (2026-10-31) | PASS: 25/25 VERIFIED against the named primary sources |
| 3. 72 strings | PASS: 72/72 = render(fresh Crossref/PubMed + overrides) = render(registry); 49/49 PubMed DOI and MedlineTA matches |
| 3b. Counts | PASS: 84 / 72 / 84 anchors / 0 orphans / 72 entries / 0 / 0 |
| 4. Retraction / correction (72) | PASS: 0 / 0 / 0 |
| 5. Deliverable | PASS: list 72/72 = v7; brackets 1–72, no gaps, first-appearance order, 84/84 sequence match; 0 `<!--` |
| 6. PLoS One Vancouver | PASS with advisories A1–A8 |
| Flags | 8 advisory (A1–A8); 0 strict |

Strict layer:
- unresolvable entries 0;
- string, key, order or DOI mismatches 0;
- overrides not confirmed 0;
- retractions, corrections, expressions of concern 0 / 0 / 0;
- deliverable mismatches 0.

`citation_check=PASS WITH FLAGS` (scoped, v7 `d02ec9b62ff1`)
