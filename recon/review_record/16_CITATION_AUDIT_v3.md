# Citation Audit Report — RECON paper, draft v3

| | |
|---|---|
| Date | 2026-10-31 |
| Mode | ARS 3.23.0 `academic-paper` **citation-check** (Phase 5a, citation_compliance_agent checklist); installed version checked = 3.23.0 = calibration baseline |
| Policy | `citation_existence` = **strict**; retraction policy **strict** |
| Model | Opus-class (Opus 5.5), execution-tier pass. Check E (claim–source context) is a judgment-class reading; the PI may want it re-read on Fable |
| Citation style | Vancouver, PLoS One variant (citation-sequence; first six authors then et al.; NCBI abbreviations; DOI at the end as `doi:10.xxxx`). In-text author-year with `<!--ref:KEY--><!--anchor:quote:…-->` is the pre-format-convert form and is **not** treated as a format error |
| Target | `RECON_paper/manuscript/15_DRAFT_v3.md`, sha256 `aed5252125fd96c0dfc86c01f3d6689805d7ef89e03bd2775b27e250f628a2b8` (prefix aed5252125fd, matches the brief). Manuscript part = everything before `# PIPELINE INTERNAL` (line 520); References = B0092 |
| Registry (the only allowed corpus) | `refs/refs_in_recon.json` (73 entries: key / doi / why; 2026-10-17 15:17) |
| Generated strings | `refs/prior_works_recon_strings.md`, Vancouver section, 73 strings (`tools/cite.py` + `tools/apply_ref_overrides.py`, 2026-10-17 15:21); override log at the end of that file = `refs/overrides.json` (2026-10-11) |
| Fresh lookups made in this pass (2026-10-31) | Crossref REST `api.crossref.org/works/<DOI>` for all 73 registry DOIs (sequential, 0.3 s apart); NCBI E-utilities esummary (50 PMIDs, journal abbreviation and PMID↔DOI) and efetch (50 abstracts, publication types, CommentsCorrections); OpenAlex (`is_retracted` for all 73; abstracts for 15 records with no Crossref/PubMed abstract); Semantic Scholar (5 abstracts); arXiv API (2404.09556, 2508.06281); Europe PMC full text of Ko and Cheng 2021b (PMC7853495). Raw responses kept in the session scratchpad only |
| Not available | Full texts other than PMC7853495; the Elsevier chapter of Denker et al. 2025; IEEE full text of Wang et al. 2024 |
| Files written | This report only. The draft was **not** modified (the agent definition's auto-correct step was not run, by instruction); every correction is an author action in §9 |

---

## Summary

| Check | Result | Counts |
|---|---|---|
| A. String fidelity (70 reference lines) | **PASS** | 70/70 lines byte-identical to the generated Vancouver string for the same DOI; 70/70 also identical to a string re-rendered today from fresh Crossref (+ NCBI abbreviation) metadata with the logged overrides; 0 author, 0 title, 0 journal, 0 year, 0 volume, 0 pages, 0 DOI divergences; 50/50 PMID↔DOI pairs confirmed; 11 entries rely on logged overrides (all still needed: fresh Crossref still differs in each overridden field) |
| B. Instances ↔ list | **PASS** | 82 instances (82 ref markers, 82 anchors, every marker paired), 70 distinct keys; 0 cited keys missing from the list; 0 list keys uncited; 0 keys outside the registry; numbering 1–70 = order of first citation; 0 ref markers in the abstract or after `## References`; 82/82 visible author-year forms match the entry (surnames, et al. rule, year) |
| C. Quote anchors | **PASS** | 82/82 VERIFIED, 0 NOT FOUND, 0 PARAPHRASE; max 16 words. 75 exact title substrings; 2 exact PubMed-abstract substrings (the two anchors changed tonight: Zhao 2014, Pulletz 2006); 2 PubMed-title substrings (AlBadawy, Crossref title has U+2010); 2 title substrings after stated normalisation (Isensee NBSP; Lange curly quotes); 1 non-title anchor (Ko and Cheng 2021b) verified verbatim in the primary full text for the first time |
| D. Retraction / concern | **PASS** | 70/70 cited (73/73 registry): Crossref `update-to` = [] and `updated-by` = [] (Crossref carries the Retraction Watch data in `updated-by`); OpenAlex `is_retracted` = false 73/73; PubMed: 0 Retracted Publication / Expression of Concern publication types, 0 RetractionIn / ErratumIn / ExpressionOfConcernIn links for the 50 indexed records. 0 retractions, 0 corrections, 0 expressions of concern |
| E. Claim–source context (advisory) | **FLAGS** | 82 instances read against the source abstract (or title only for 5 seminal method/software/review entries; full text for Ko 2021b): 67 OK (five with a note), 9 minor or unverified, **6 FLAG** (E1–E6, §5) |
| F. PLoS One citability | **PASS** (+ note) | Companion core paper has no registry key, no ref marker, no list entry; named with `[MATERIAL GAP: preprint DOI…]` in B0013 and B0089. It is also named, without marker and without citation, as the provenance of the reused GREIT networks in eight further places (§6) — not a citation, but not "only in the Related manuscript statement" either |
| G. Registry orphans | reported, not decided | 3: Rusak2020ECCV, Zhang2020TMI, Zhang2022PhysiolMeas (§7) |
| Self-citation | PASS | 3/70 entries = 4.3%; 4/82 instances = 4.9% (threshold 15%) |
| Currency | ADVISORY | 16/70 (22.9%) before 2016 (13 seminal/standard method, software, statistics or physiology; 3 primary EIT findings with stated roles); 34/70 (48.6%) from 2021–2026 |

**Strict verdict: `citation_check=PASS WITH FLAGS`.** Nothing fails the strict policy (no unresolvable entry, no DOI/author mismatch, no unverifiable anchor, no retraction). The six context flags (E1–E6) are claim–source divergences the author must decide before submission; E1 (Yu 2024a, a restored reference) is a factual contradiction of the cited abstract, E3 (Yan 2020) is a number pair not reported in the source.

---

## 1. Check A — reference strings, field by field

**Method.** (a) Each of the 70 numbered lines in B0092 (`N. <string> <!--key:KEY-->`) was compared byte-for-byte with the Vancouver string in `refs/prior_works_recon_strings.md` that carries the same DOI as the key's registry entry: **70/70 identical**. (b) Each string was then re-rendered from today's Crossref record with `tools/cite.py`'s own rules (author = family + initials of given names, original order; title + subtitle; year = published-print → published-online → issued; `page` or `article-number`; journal = NCBI esummary `source` when the DOI is in PubMed, otherwise Crossref `short-container-title`), the logged overrides applied, and the six-then-et-al rule applied: **70/70 equal to the draft line**. So no field changed at the source between 2026-10-17 and today. (c) For the 50 PubMed records the esummary DOI list contains the registry DOI (50/50). ✓ = equal.

| # | Key | Authors: DB n → rendered | Journal (source) | Year | Vol | Pages / art. no. | DOI | Draft line = generated string | Fresh Crossref/PubMed render = draft | Override applied (logged in strings file) |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | Frerichs2017TREND | 20 → 6 + et al. ✓ | Thorax (NCBI) ✓ | 2017 ✓ | 72 ✓ | 83-93 ✓ | 10.1136/thoraxjnl-2016-208357 ✓ | identical | yes | — |
| 2 | Zhao2014PhysiolMeas | 5 → 5 (all) ✓ | Physiol Meas (NCBI) ✓ | 2014 ✓ | 35 ✓ | 1083-1093 ✓ | 10.1088/0967-3334/35/6/1083 ✓ | identical | yes | — |
| 3 | Grychtol2014PLOSONE | 6 → 6 (all) ✓ | PLoS One (NCBI) ✓ | 2014 ✓ | 9 ✓ | e103045 ✓ | 10.1371/journal.pone.0103045 ✓ | identical | yes | — |
| 4 | Zhou2023TPAMI | 5 → 5 (all) ✓ | IEEE Trans Pattern Anal Mach Intell (NCBI) ✓ | 2023 ✓ | 45 ✓ | 4396-4415 ✓ | 10.1109/tpami.2022.3195549 ✓ | identical | yes | year 2022→2023, vol —→45, pages 1-20→4396-4415 (PMID 35914036) |
| 5 | Yoon2024ProcIEEE | 5 → 5 (all) ✓ | Proc. IEEE (Crossref) ✓ | 2024 ✓ | 112 ✓ | 1583-1609 ✓ | 10.1109/jproc.2024.3507831 ✓ | identical | yes | — |
| 6 | Leathard1994PhysiolMeas | 6 → 6 (all) ✓ | Physiol Meas (NCBI) ✓ | 1994 ✓ | 15 ✓ | A137-A146 ✓ | 10.1088/0967-3334/15/2a/018 ✓ | identical | yes | — |
| 7 | Graf2017PLOSONE | 2 → 2 (all) ✓ | PLoS One (NCBI) ✓ | 2017 ✓ | 12 ✓ | e0188313 ✓ | 10.1371/journal.pone.0188313 ✓ | identical | yes | — |
| 8 | Ko2021PhysiolMeas | 2 → 2 (all) ✓ | Physiol Meas (NCBI) ✓ | 2021 ✓ | 42 ✓ | 025002 ✓ | 10.1088/1361-6579/abe021 ✓ | identical | yes | — |
| 9 | Ko2021PLOSONE | 2 → 2 (all) ✓ | PLoS One (NCBI) ✓ | 2021 ✓ | 16 ✓ | e0246071 ✓ | 10.1371/journal.pone.0246071 ✓ | identical | yes | — |
| 10 | Ko2025CurrMedImaging | 3 → 3 (all) ✓ | Curr Med Imaging (NCBI) ✓ | 2025 ✓ | 21 ✓ | e15734056408077 ✓ | 10.2174/0115734056408077250610070821 ✓ | identical | yes | — |
| 11 | Vandenhende2021 | 6 → 6 (all) ✓ | IEEE Trans Pattern Anal Mach Intell (NCBI) ✓ | 2022 ✓ | 44 ✓ | 3614-3633 ✓ | 10.1109/tpami.2021.3054719 ✓ | identical | yes | year 2021→2022, vol —→44, pages 1-1→3614-3633 (PMID 33497328) |
| 12 | Wang2024TIM | 4 → 4 (all) ✓ | IEEE Trans. Instrum. Meas. (Crossref) ✓ | 2024 ✓ | 73 ✓ | 1-16 ✓ | 10.1109/tim.2024.3369160 ✓ | identical | yes | — |
| 13 | Yu2024CMPB | 5 → 5 (all) ✓ | Comput Methods Programs Biomed (NCBI) ✓ | 2024 ✓ | 243 ✓ | 107861 ✓ | 10.1016/j.cmpb.2023.107861 ✓ | identical | yes | — |
| 14 | Hamilton2018TMI | 2 → 2 (all) ✓ | IEEE Trans Med Imaging (NCBI) ✓ | 2018 ✓ | 37 ✓ | 2367-2377 ✓ | 10.1109/tmi.2018.2828303 ✓ | identical | yes | — |
| 15 | Herzberg2023PhysiolMeas | 3 → 3 (all) ✓ | Physiol Meas (NCBI) ✓ | 2023 ✓ | 44 ✓ | 125008 ✓ | 10.1088/1361-6579/ad0b3d ✓ | identical | yes | title: trailing ⋆ removed |
| 16 | Zhang2022FBB | 8 → 6 + et al. ✓ | Front Bioeng Biotechnol (NCBI) ✓ | 2022 ✓ | 10 ✓ | 1019531 ✓ | 10.3389/fbioe.2022.1019531 ✓ | identical | yes | — |
| 17 | Denker2025HandbNumerAnal | 8 → 6 + et al. ✓ | Handbook of Numerical Analysis (Crossref) ✓ | 2025 ✓ | — ✓ | 127-175 ✓ | 10.1016/bs.hna.2025.09.003 ✓ | identical | yes | — |
| 18 | Zech2018PLoSMed | 6 → 6 (all) ✓ | PLoS Med (NCBI) ✓ | 2018 ✓ | 15 ✓ | e1002683 ✓ | 10.1371/journal.pmed.1002683 ✓ | identical | yes | — |
| 19 | AlBadawy2018MedPhys | 3 → 3 (all) ✓ | Med Phys (NCBI) ✓ | 2018 ✓ | 45 ✓ | 1150-1158 ✓ | 10.1002/mp.12752 ✓ | identical | yes | — |
| 20 | Liu2020TMI | 4 → 4 (all) ✓ | IEEE Trans Med Imaging (NCBI) ✓ | 2020 ✓ | 39 ✓ | 2713-2724 ✓ | 10.1109/tmi.2020.2974574 ✓ | identical | yes | — |
| 21 | HoangThi2021DIII | 6 → 6 (all) ✓ | Diagn Interv Imaging (NCBI) ✓ | 2021 ✓ | 102 ✓ | 691-695 ✓ | 10.1016/j.diii.2021.10.001 ✓ | identical | yes | — |
| 22 | Zeng2022MedPhys | 7 → 6 + et al. ✓ | Med Phys (NCBI) ✓ | 2022 ✓ | 49 ✓ | 836-853 ✓ | 10.1002/mp.15430 ✓ | identical | yes | — |
| 23 | Hamilton2019PhysiolMeas | 4 → 4 (all) ✓ | Physiol Meas (NCBI) ✓ | 2019 ✓ | 40 ✓ | 074002 ✓ | 10.1088/1361-6579/ab21b2 ✓ | identical | yes | — |
| 24 | Karani2018MICCAI | 4 → 4 (all) ✓ | Lecture Notes in Computer Science (Crossref) ✓ | 2018 ✓ | — ✓ | 476-484 ✓ | 10.1007/978-3-030-00928-1_54 ✓ | identical | yes | — |
| 25 | Holzschuh2024RadiatOncol | 17 → 6 + et al. ✓ | Radiat Oncol (NCBI) ✓ | 2024 ✓ | 19 ✓ | 106 ✓ | 10.1186/s13014-024-02491-w ✓ | identical | yes | — |
| 26 | Lange2025StatMed | 5 → 5 (all) ✓ | Stat Med (NCBI) ✓ | 2025 ✓ | 44 ✓ | e70303 ✓ | 10.1002/sim.70303 ✓ | identical | yes | — |
| 27 | Adler2006EIDORS | 2 → 2 (all) ✓ | Physiol Meas (NCBI) ✓ | 2006 ✓ | 27 ✓ | S25-S42 ✓ | 10.1088/0967-3334/27/5/s03 ✓ | identical | yes | — |
| 28 | Gagnon2010TBME | 4 → 4 (all) ✓ | IEEE Trans Biomed Eng (NCBI) ✓ | 2010 ✓ | 57 ✓ | 2257-2266 ✓ | 10.1109/tbme.2010.2052618 ✓ | identical | yes | — |
| 29 | Adler2009GREIT | 19 → 6 + et al. ✓ | Physiol Meas (NCBI) ✓ | 2009 ✓ | 30 ✓ | S35-S55 ✓ | 10.1088/0967-3334/30/6/s03 ✓ | identical | yes | — |
| 30 | Adler1996TMI | 2 → 2 (all) ✓ | IEEE Trans Med Imaging (NCBI) ✓ | 1996 ✓ | 15 ✓ | 170-179 ✓ | 10.1109/42.491418 ✓ | identical | yes | — |
| 31 | Thurk2019PhysiolMeas | 7 → 6 + et al. ✓ | Physiol Meas (NCBI) ✓ | 2019 ✓ | 40 ✓ | 094003 ✓ | 10.1088/1361-6579/ab248e ✓ | identical | yes | — |
| 32 | Ronneberger2015UNet | 3 → 3 (all) ✓ | Lecture Notes in Computer Science (Crossref) ✓ | 2015 ✓ | 9351 ✓ | 234-241 ✓ | 10.1007/978-3-319-24574-4_28 ✓ | identical | yes | vol —→9351 |
| 33 | Vandenhende2020Branched | 4 → 4 (all) ✓ | Proceedings of the British Machine Vision Conference 2020 (Crossref) ✓ | 2020 ✓ | — ✓ | 59 ✓ | 10.5244/c.34.59 ✓ | identical | yes | authors: Gool LV/Brabandere BD → Van Gool L/De Brabandere B |
| 34 | Isensee2024nnUNetRevisited | 7 → 6 + et al. ✓ | Lecture Notes in Computer Science (Crossref) ✓ | 2024 ✓ | 15009 ✓ | 488-498 ✓ | 10.1007/978-3-031-72114-4_47 ✓ | identical | yes | vol —→15009 |
| 35 | Caruana1997MTL | 1 → 1 (all) ✓ | Machine Learning (Crossref) ✓ | 1997 ✓ | 28 ✓ | 41-75 ✓ | 10.1023/a:1007379606734 ✓ | identical | yes | — |
| 36 | Kurin2022Unitary | 5 → 5 (all) ✓ | Advances in Neural Information Processing Systems 35 (Crossref) ✓ | 2022 ✓ | — ✓ | 12169-12183 ✓ | 10.52202/068431-0884 ✓ | identical | yes | authors: Palma AD → De Palma A |
| 37 | Xin2022MTOHelp | 5 → 5 (all) ✓ | Advances in Neural Information Processing Systems 35 (Crossref) ✓ | 2022 ✓ | — ✓ | 13597-13609 ✓ | 10.52202/068431-0988 ✓ | identical | yes | — |
| 38 | Kendall2018 | 3 → 3 (all) ✓ | 2018 IEEE/CVF Conference on Computer Vision and Pattern Recognition (Crossref) ✓ | 2018 ✓ | — ✓ | 7482-7491 ✓ | 10.1109/cvpr.2018.00781 ✓ | identical | yes | authors: Crossref order reversed → Kendall A, Gal Y, Cipolla R |
| 39 | Renard2020SciRep | 4 → 4 (all) ✓ | Sci Rep (NCBI) ✓ | 2020 ✓ | 10 ✓ | 13724 ✓ | 10.1038/s41598-020-69920-0 ✓ | identical | yes | — |
| 40 | Pulletz2006ROI | 8 → 6 + et al. ✓ | Physiol Meas (NCBI) ✓ | 2006 ✓ | 27 ✓ | S115-S127 ✓ | 10.1088/0967-3334/27/5/s10 ✓ | identical | yes | — |
| 41 | Jeschke2025Sensors | 6 → 6 (all) ✓ | Sensors (Basel) (NCBI) ✓ | 2025 ✓ | 25 ✓ | 6543 ✓ | 10.3390/s25216543 ✓ | identical | yes | — |
| 42 | Yu2024CVPR | 6 → 6 (all) ✓ | 2024 IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR) (Crossref) ✓ | 2024 ✓ | — ✓ | 21897-21908 ✓ | 10.1109/cvpr52733.2024.02068 ✓ | identical | yes | — |
| 43 | Willroth2024AMPPS | 2 → 2 (all) ✓ | Advances in Methods and Practices in Psychological Science (Crossref) ✓ | 2024 ✓ | 7 ✓ | 25152459231213802 ✓ | 10.1177/25152459231213802 ✓ | identical | yes | — |
| 44 | Wilcoxon1945 | 1 → 1 (all) ✓ | Biometrics Bulletin (Crossref) ✓ | 1945 ✓ | 1 ✓ | 80 ✓ | 10.2307/3001968 ✓ | identical | yes | — |
| 45 | Schuirmann1987JPharmacokinet | 1 → 1 (all) ✓ | J Pharmacokinet Biopharm (NCBI) ✓ | 1987 ✓ | 15 ✓ | 657-680 ✓ | 10.1007/bf01068419 ✓ | identical | yes | — |
| 46 | Lakens2017SPPS | 1 → 1 (all) ✓ | Soc Psychol Personal Sci (NCBI) ✓ | 2017 ✓ | 8 ✓ | 355-362 ✓ | 10.1177/1948550617697177 ✓ | identical | yes | — |
| 47 | Lakens2018AMPPS | 3 → 3 (all) ✓ | Advances in Methods and Practices in Psychological Science (Crossref) ✓ | 2018 ✓ | 1 ✓ | 259-269 ✓ | 10.1177/2515245918770963 ✓ | identical | yes | — |
| 48 | Lakens2013EffectSize | 1 → 1 (all) ✓ | Front Psychol (NCBI) ✓ | 2013 ✓ | 4 ✓ | 863 ✓ | 10.3389/fpsyg.2013.00863 ✓ | identical | yes | pages —→863 (PMID 24324449) |
| 49 | Christodoulou2024MICCAI | 22 → 6 + et al. ✓ | Lecture Notes in Computer Science (Crossref) ✓ | 2024 ✓ | 15010 ✓ | 124-132 ✓ | 10.1007/978-3-031-72117-5_12 ✓ | identical | yes | vol —→15010 |
| 50 | Myronenko2019AEReg | 1 → 1 (all) ✓ | Lecture Notes in Computer Science (Crossref) ✓ | 2019 ✓ | 11384 ✓ | 311-320 ✓ | 10.1007/978-3-030-11726-9_28 ✓ | identical | yes | vol —→11384 |
| 51 | Venkatesh2026MedPhys | 4 → 4 (all) ✓ | Med Phys (NCBI) ✓ | 2026 ✓ | 53 ✓ | e70414 ✓ | 10.1002/mp.70414 ✓ | identical | yes | — |
| 52 | Grychtol2014PhysiolMeas | 2 → 2 (all) ✓ | Physiol Meas (NCBI) ✓ | 2014 ✓ | 35 ✓ | 1035-1050 ✓ | 10.1088/0967-3334/35/6/1035 ✓ | identical | yes | — |
| 53 | Albert2023ApplSci | 8 → 6 + et al. ✓ | Applied Sciences (Crossref) ✓ | 2023 ✓ | 13 ✓ | 8923 ✓ | 10.3390/app13158923 ✓ | identical | yes | — |
| 54 | Delisle2021MedIA | 4 → 4 (all) ✓ | Med Image Anal (NCBI) ✓ | 2021 ✓ | 74 ✓ | 102191 ✓ | 10.1016/j.media.2021.102191 ✓ | identical | yes | — |
| 55 | Yan2020RadiolAI | 7 → 6 + et al. ✓ | Radiol Artif Intell (NCBI) ✓ | 2020 ✓ | 2 ✓ | e190195 ✓ | 10.1148/ryai.2020190195 ✓ | identical | yes | — |
| 56 | Martensson2020MedIA | 25 → 6 + et al. ✓ | Med Image Anal (NCBI) ✓ | 2020 ✓ | 66 ✓ | 101714 ✓ | 10.1016/j.media.2020.101714 ✓ | identical | yes | — |
| 57 | Castro2020NatCommun | 3 → 3 (all) ✓ | Nat Commun (NCBI) ✓ | 2020 ✓ | 11 ✓ | 3673 ✓ | 10.1038/s41467-020-17478-w ✓ | identical | yes | — |
| 58 | Kamann2021IJCV | 2 → 2 (all) ✓ | Int J Comput Vis (Crossref) ✓ | 2021 ✓ | 129 ✓ | 462-483 ✓ | 10.1007/s11263-020-01383-2 ✓ | identical | yes | — |
| 59 | Boone2023NeuroImage | 13 → 6 + et al. ✓ | Neuroimage (NCBI) ✓ | 2023 ✓ | 278 ✓ | 120289 ✓ | 10.1016/j.neuroimage.2023.120289 ✓ | identical | yes | — |
| 60 | Du2022EurRadiol | 7 → 6 + et al. ✓ | Eur Radiol (NCBI) ✓ | 2022 ✓ | 33 ✓ | 2426-2438 ✓ | 10.1007/s00330-022-09229-w ✓ | identical | yes | — |
| 61 | Billot2023MedIA | 8 → 6 + et al. ✓ | Med Image Anal (NCBI) ✓ | 2023 ✓ | 86 ✓ | 102789 ✓ | 10.1016/j.media.2023.102789 ✓ | identical | yes | — |
| 62 | Scheel2021AMPPS | 3 → 3 (all) ✓ | Advances in Methods and Practices in Psychological Science (Crossref) ✓ | 2021 ✓ | 4 ✓ | 25152459211007467 ✓ | 10.1177/25152459211007467 ✓ | identical | yes | — |
| 63 | McGreivy2024NatMachIntell | 2 → 2 (all) ✓ | Nat Mach Intell (Crossref) ✓ | 2024 ✓ | 6 ✓ | 1256-1269 ✓ | 10.1038/s42256-024-00897-5 ✓ | identical | yes | — |
| 64 | Borji2018ImaVisComput | 1 → 1 (all) ✓ | Image and Vision Computing (Crossref) ✓ | 2018 ✓ | 69 ✓ | 1-8 ✓ | 10.1016/j.imavis.2017.10.001 ✓ | identical | yes | — |
| 65 | Varoquaux2022NPJDigitMed | 2 → 2 (all) ✓ | NPJ Digit Med (NCBI) ✓ | 2022 ✓ | 5 ✓ | 48 ✓ | 10.1038/s41746-022-00592-y ✓ | identical | yes | — |
| 66 | Nosek2018Prereg | 4 → 4 (all) ✓ | Proc Natl Acad Sci U S A (NCBI) ✓ | 2018 ✓ | 115 ✓ | 2600-2606 ✓ | 10.1073/pnas.1708274114 ✓ | identical | yes | — |
| 67 | Chambers2021NatHumBehav | 2 → 2 (all) ✓ | Nat Hum Behav (NCBI) ✓ | 2021 ✓ | 6 ✓ | 29-42 ✓ | 10.1038/s41562-021-01193-7 ✓ | identical | yes | — |
| 68 | Pawel2023BiomJ | 3 → 3 (all) ✓ | Biom J (NCBI) ✓ | 2024 ✓ | 66 ✓ | 2200091 ✓ | 10.1002/bimj.202200091 ✓ | identical | yes | — |
| 69 | Boyle2011PhysiolMeas | 2 → 2 (all) ✓ | Physiol Meas (NCBI) ✓ | 2011 ✓ | 32 ✓ | 745-754 ✓ | 10.1088/0967-3334/32/7/s02 ✓ | identical | yes | — |
| 70 | Boulesteix2013PLOSONE | 3 → 3 (all) ✓ | PLoS One (NCBI) ✓ | 2013 ✓ | 8 ✓ | e61562 ✓ | 10.1371/journal.pone.0061562 ✓ | identical | yes | — |

**Overrides.** Eleven cited entries depend on `refs/overrides.json`; every one is logged with source and date in the strings file. In each case today's Crossref record still differs in the overridden field (Zhou and Vandenhende 2021 still early-access records; Kendall order still reversed; Kurin and Vandenhende 2020 particles still split; Herzberg title still ends in ⋆; LNCS volumes and Lakens 2013 article number still absent), so all overrides remain necessary. The issue overrides (Zhou, Vandenhende 2021) are not rendered by the Vancouver template and have no effect.

**The six references restored after the v1 audit** (strings, fresh lookups):

| Key | Ref | DOI | Result |
|---|---|---|---|
| Leathard1994PhysiolMeas | 6 | 10.1088/0967-3334/15/2a/018 | ✓ 6 authors, Physiol Meas (NCBI) 1994;15:A137-A146, PMID 8087036 |
| Yu2024CMPB | 13 | 10.1016/j.cmpb.2023.107861 | ✓ 5 authors, Comput Methods Programs Biomed (NCBI) 2024;243:107861, PMID 37931580 |
| Jeschke2025Sensors | 41 | 10.3390/s25216543 | ✓ 6 authors, Sensors (Basel) (NCBI) 2025;25:6543, PMID 41228767 |
| Kamann2021IJCV | 58 | 10.1007/s11263-020-01383-2 | ✓ 2 authors, Int J Comput Vis (Crossref short title; not in PubMed) 2021;129:462-483 |
| Boone2023NeuroImage | 59 | 10.1016/j.neuroimage.2023.120289 | ✓ 13 authors → 6 + et al., Neuroimage (NCBI) 2023;278:120289, PMID 37495197 |
| Boyle2011PhysiolMeas | 69 | 10.1088/0967-3334/32/7/s02 | ✓ 2 authors, Physiol Meas (NCBI) 2011;32:745-754, PMID 21646710 |

**Rendering / format items carried from v1 (ADVISORY; each string is faithful to the database, so none is a fidelity mismatch).** Still open in v3: F1 Crossref short titles instead of NLM abbreviations for the non-PubMed containers (e.g. "Applied Sciences", "Machine Learning", "Image and Vision Computing", "Biometrics Bulletin", "Advances in Methods and Practices in Psychological Science" ×3, "Proc. IEEE", "IEEE Trans. Instrum. Meas."); F2 double period "IEEE Trans. Instrum. Meas.." (Wang 2024); F3 "?." after question-mark titles (Hoang-Thi, Xin, Christodoulou); F4 proceedings and the Denker chapter in journal form; **F5 Karani2018MICCAI still has no LNCS volume** (no override yet); F6 `doi:` vs `doi: `; F7 online vs issue year (Chambers 2021 with vol 6; Du 2022 with vol 33); F8 unverified particle/initial forms "Genderingen HRv" (Pulletz), "Palma ND" (Renard), "Boulesteix A" (Lange) vs "Boulesteix AL"; F9 Wang 2024 pages "1-16" instead of an article number; F10 title capitalisation as deposited; F11 U+2010 hyphens in AlBadawy, Zeng, Venkatesh, Du ("learning–based" uses U+2013). New in v3: none (the six restored strings add no new item class; Kamann's container is a Crossref short title, class F1).

---

## 2. Check B — instances, list, order, visible forms

| Item | Result |
|---|---|
| Ref markers / anchor markers in the manuscript part | 82 / 82, each `ref` immediately followed by its `anchor` |
| Distinct cited keys | 70 |
| Reference-list lines (`<!--key:…-->`) | 70, numbered 1–70 without gaps, no duplicate key |
| Cited keys not in the list / list keys never cited | **0 / 0** |
| Keys outside `refs_in_recon.json` | **0** |
| List order = order of first citation | **yes**, all 70 positions |
| Ref markers in the abstract (B0006) or after `## References` (supporting information, captions, tables) | 0 |
| Most-cited keys | Karani2018MICCAI ×4; Ko2021PLOSONE, Zech2018PLoSMed, AlBadawy2018MedPhys, Liu2020TMI, Zeng2022MedPhys, Holzschuh2024RadiatOncol, Adler2006EIDORS, Thurk2019PhysiolMeas, Lakens2017SPPS ×2; all others ×1 |
| Largest group in one parenthesis | 3 (no over-citation > 5) |

**Visible author-year forms** (parsed from the parenthesis or narrative form immediately before each marker group; expected form from the reference string's author count: 1 → "A"; 2 → "A and B"; ≥ 3 → "A et al."; year = rendered year):

| # | Block | Key | Visible form | Entry (first author(s), year) | Match |
|---|---|---|---|---|---|
| 1 | B0011 | Frerichs2017TREND | Frerichs et al., 2017 | Frerichs et al., 2017 | ✓ |
| 2 | B0011 | Zhao2014PhysiolMeas | Zhao et al., 2014 | Zhao et al., 2014 | ✓ |
| 3 | B0011 | Grychtol2014PLOSONE | Grychtol et al., 2014a | Grychtol et al., 2014 | ✓ (suffix) |
| 4 | B0011 | Zhou2023TPAMI | Zhou et al., 2023 | Zhou et al., 2023 | ✓ |
| 5 | B0011 | Yoon2024ProcIEEE | Yoon et al., 2024 | Yoon et al., 2024 | ✓ |
| 6 | B0013 | Leathard1994PhysiolMeas | Leathard et al., 1994 | Leathard et al., 1994 | ✓ |
| 7 | B0013 | Graf2017PLOSONE | Graf and Riedel, 2017 | Graf and Riedel, 2017 | ✓ |
| 8 | B0013 | Ko2021PhysiolMeas | Ko and Cheng, 2021a | Ko and Cheng, 2021 | ✓ (suffix) |
| 9 | B0013 | Ko2021PLOSONE | Ko and Cheng, 2021b | Ko and Cheng, 2021 | ✓ (suffix) |
| 10 | B0013 | Ko2025CurrMedImaging | Ko et al., 2025 | Ko et al., 2025 | ✓ |
| 11 | B0013 | Ko2021PLOSONE | Ko and Cheng, 2021b | Ko and Cheng, 2021 | ✓ (suffix) |
| 12 | B0014 | Vandenhende2021 | Vandenhende et al., 2022 | Vandenhende et al., 2022 | ✓ |
| 13 | B0014 | Wang2024TIM | Wang et al., 2024 | Wang et al., 2024 | ✓ |
| 14 | B0014 | Yu2024CMPB | Yu et al., 2024a | Yu et al., 2024 | ✓ (suffix) |
| 15 | B0014 | Hamilton2018TMI | Hamilton and Hauptmann, 2018 | Hamilton and Hauptmann, 2018 | ✓ |
| 16 | B0014 | Herzberg2023PhysiolMeas | Herzberg et al., 2023 | Herzberg et al., 2023 | ✓ |
| 17 | B0014 | Zhang2022FBB | Zhang et al., 2022b | Zhang et al., 2022 | ✓ (suffix) |
| 18 | B0014 | Denker2025HandbNumerAnal | Denker et al., 2025 | Denker et al., 2025 | ✓ |
| 19 | B0016 | Zech2018PLoSMed | Zech et al., 2018 | Zech et al., 2018 | ✓ |
| 20 | B0016 | AlBadawy2018MedPhys | AlBadawy et al., 2018 | AlBadawy et al., 2018 | ✓ |
| 21 | B0016 | Liu2020TMI | Liu et al., 2020 | Liu et al., 2020 | ✓ |
| 22 | B0016 | HoangThi2021DIII | Hoang-Thi et al., 2021 | Hoang-Thi et al., 2021 | ✓ |
| 23 | B0016 | Zeng2022MedPhys | Zeng et al., 2022 | Zeng et al., 2022 | ✓ |
| 24 | B0017 | Hamilton2019PhysiolMeas | Hamilton et al., 2019 | Hamilton et al., 2019 | ✓ |
| 25 | B0017 | Karani2018MICCAI | Karani et al., 2018 | Karani et al., 2018 | ✓ |
| 26 | B0017 | Holzschuh2024RadiatOncol | Holzschuh et al., 2024 | Holzschuh et al., 2024 | ✓ |
| 27 | B0019 | Lange2025StatMed | Lange et al., 2025 | Lange et al., 2025 | ✓ |
| 28 | B0023 | Adler2006EIDORS | Adler and Lionheart, 2006 | Adler and Lionheart, 2006 | ✓ |
| 29 | B0023 | Gagnon2010TBME | Gagnon et al., 2010 | Gagnon et al., 2010 | ✓ |
| 30 | B0024 | Adler2009GREIT | Adler et al., 2009 | Adler et al., 2009 | ✓ |
| 31 | B0024 | Adler1996TMI | Adler and Guardo, 1996 | Adler and Guardo, 1996 | ✓ |
| 32 | B0024 | Adler2006EIDORS | Adler and Lionheart, 2006 | Adler and Lionheart, 2006 | ✓ |
| 33 | B0024 | Thurk2019PhysiolMeas | Thürk et al., 2019 | Thürk et al., 2019 | ✓ |
| 34 | B0027 | Ronneberger2015UNet | Ronneberger et al., 2015 | Ronneberger et al., 2015 | ✓ |
| 35 | B0027 | Vandenhende2020Branched | Vandenhende et al., 2020 | Vandenhende et al., 2020 | ✓ |
| 36 | B0027 | Isensee2024nnUNetRevisited | Isensee et al., 2024 | Isensee et al., 2024 | ✓ |
| 37 | B0028 | Caruana1997MTL | Caruana, 1997 | Caruana, 1997 | ✓ |
| 38 | B0028 | Kurin2022Unitary | Kurin et al., 2022 | Kurin et al., 2022 | ✓ |
| 39 | B0028 | Xin2022MTOHelp | Xin et al., 2022 | Xin et al., 2022 | ✓ |
| 40 | B0028 | Kendall2018 | Kendall et al., 2018 | Kendall et al., 2018 | ✓ |
| 41 | B0028 | Renard2020SciRep | Renard et al., 2020 | Renard et al., 2020 | ✓ |
| 42 | B0030 | Pulletz2006ROI | Pulletz et al., 2006 | Pulletz et al., 2006 | ✓ |
| 43 | B0033 | Jeschke2025Sensors | Jeschke et al., 2025 | Jeschke et al., 2025 | ✓ |
| 44 | B0034 | Yu2024CVPR | Yu et al., 2024b | Yu et al., 2024 | ✓ (suffix) |
| 45 | B0037 | Willroth2024AMPPS | Willroth and Atherton, 2024 | Willroth and Atherton, 2024 | ✓ |
| 46 | B0039 | Wilcoxon1945 | Wilcoxon, 1945 | Wilcoxon, 1945 | ✓ |
| 47 | B0039 | Schuirmann1987JPharmacokinet | Schuirmann, 1987 | Schuirmann, 1987 | ✓ |
| 48 | B0039 | Lakens2017SPPS | Lakens, 2017 | Lakens, 2017 | ✓ |
| 49 | B0039 | Lakens2018AMPPS | Lakens et al., 2018 | Lakens et al., 2018 | ✓ |
| 50 | B0040 | Lakens2013EffectSize | Lakens, 2013 | Lakens, 2013 | ✓ |
| 51 | B0040 | Christodoulou2024MICCAI | Christodoulou et al., 2024 | Christodoulou et al., 2024 | ✓ |
| 52 | B0067 | Karani2018MICCAI | Karani et al., 2018 | Karani et al., 2018 | ✓ |
| 53 | B0067 | Liu2020TMI | Liu et al., 2020 | Liu et al., 2020 | ✓ |
| 54 | B0067 | Myronenko2019AEReg | Myronenko, 2019 | Myronenko, 2019 | ✓ |
| 55 | B0069 | Holzschuh2024RadiatOncol | Holzschuh et al., 2024 | Holzschuh et al., 2024 | ✓ |
| 56 | B0069 | Lakens2017SPPS | Lakens, 2017 | Lakens, 2017 | ✓ |
| 57 | B0069 | Venkatesh2026MedPhys | Venkatesh et al., 2026 | Venkatesh et al., 2026 | ✓ |
| 58 | B0070 | Thurk2019PhysiolMeas | Thürk et al., 2019 | Thürk et al., 2019 | ✓ |
| 59 | B0072 | Grychtol2014PhysiolMeas | Grychtol and Adler, 2014b | Grychtol and Adler, 2014 | ✓ (suffix) |
| 60 | B0072 | Albert2023ApplSci | Albert et al., 2023 | Albert et al., 2023 | ✓ |
| 61 | B0072 | Karani2018MICCAI | Karani et al., 2018 | Karani et al., 2018 | ✓ |
| 62 | B0072 | Delisle2021MedIA | Delisle et al., 2021 | Delisle et al., 2021 | ✓ |
| 63 | B0074 | Yan2020RadiolAI | Yan et al., 2020 | Yan et al., 2020 | ✓ |
| 64 | B0074 | AlBadawy2018MedPhys | AlBadawy et al., 2018 | AlBadawy et al., 2018 | ✓ |
| 65 | B0075 | Martensson2020MedIA | Mårtensson et al., 2020 | Mårtensson et al., 2020 | ✓ |
| 66 | B0075 | Zech2018PLoSMed | Zech et al., 2018 | Zech et al., 2018 | ✓ |
| 67 | B0075 | Castro2020NatCommun | Castro et al., 2020 | Castro et al., 2020 | ✓ |
| 68 | B0075 | Zeng2022MedPhys | Zeng et al., 2022 | Zeng et al., 2022 | ✓ |
| 69 | B0075 | Kamann2021IJCV | Kamann and Rother, 2021 | Kamann and Rother, 2021 | ✓ |
| 70 | B0075 | Boone2023NeuroImage | Boone et al., 2023 | Boone et al., 2023 | ✓ |
| 71 | B0075 | Du2022EurRadiol | Du et al., 2022 | Du et al., 2022 | ✓ |
| 72 | B0075 | Billot2023MedIA | Billot et al., 2023 | Billot et al., 2023 | ✓ |
| 73 | B0077 | Scheel2021AMPPS | Scheel et al., 2021 | Scheel et al., 2021 | ✓ |
| 74 | B0077 | McGreivy2024NatMachIntell | McGreivy and Hakim, 2024 | McGreivy and Hakim, 2024 | ✓ |
| 75 | B0077 | Borji2018ImaVisComput | Borji, 2018 | Borji, 2018 | ✓ |
| 76 | B0077 | Varoquaux2022NPJDigitMed | Varoquaux and Cheplygina, 2022 | Varoquaux and Cheplygina, 2022 | ✓ |
| 77 | B0077 | Nosek2018Prereg | Nosek et al., 2018 | Nosek et al., 2018 | ✓ |
| 78 | B0077 | Chambers2021NatHumBehav | Chambers and Tzavella, 2021 | Chambers and Tzavella, 2021 | ✓ |
| 79 | B0077 | Pawel2023BiomJ | Pawel et al., 2024 | Pawel et al., 2024 | ✓ |
| 80 | B0080 | Boyle2011PhysiolMeas | Boyle and Adler, 2011 | Boyle and Adler, 2011 | ✓ |
| 81 | B0081 | Boulesteix2013PLOSONE | Boulesteix et al., 2013 | Boulesteix et al., 2013 | ✓ |
| 82 | B0083 | Karani2018MICCAI | Karani et al., 2018 | Karani et al., 2018 | ✓ |

**Suffixes.** Ko and Cheng 2021a/b: needed and consistent. Yu et al. 2024a (Yu2024CMPB, first cited B0014) / 2024b (Yu2024CVPR, B0034): now both cited, needed (same visible form), assigned in first-citation order — the v1 "lone b" item for Yu is resolved. **Zhang et al. 2022b** (Zhang2022FBB): still a lone "b" — its "a" partner Zhang2022PhysiolMeas is an orphan (check G). Grychtol et al. 2014a / Grychtol and Adler 2014b: consistent, but the two visible forms already differ, so author-year rules do not need the letters. Both items vanish under citation-sequence numbering.

---

## 3. Check C — quote anchors

**Method.** Each `anchor:quote:` value was URL-decoded and searched in the fresh Crossref title (+ subtitle) and abstract, then in the PubMed title and abstract (efetch), first exactly, then after Unicode normalisation (NFKC, hyphen and dash variants to ASCII, curly quotes), then case-insensitively, then with punctuation dropped. Ko and Cheng 2021b's anchor was searched in the Europe PMC full-text XML.

| # | Block | Key | Anchor (decoded) | Words | Result |
|---|---|---|---|---|---|
| 1 | B0011 | Frerichs2017TREND | consensus statement of the TRanslational EIT developmeNt stuDy group | 9 | VERIFIED — exact substring of title |
| 2 | B0011 | Zhao2014PhysiolMeas | No significant differences were found in all examined indices among the four reconstruction algorithms | 14 | VERIFIED — exact substring of PubMed abstract |
| 3 | B0011 | Grychtol2014PLOSONE | Functional Validation and Comparison Framework for EIT Lung Imaging | 9 | VERIFIED — exact substring of title |
| 4 | B0011 | Zhou2023TPAMI | Domain Generalization: A Survey | 4 | VERIFIED — exact substring of title |
| 5 | B0011 | Yoon2024ProcIEEE | Domain Generalization for Medical Image Analysis: A Review | 8 | VERIFIED — exact substring of title |
| 6 | B0013 | Leathard1994PhysiolMeas | ventilatory and cardiac related changes in EIT images | 8 | VERIFIED — exact substring of title |
| 7 | B0013 | Graf2017PLOSONE | highly position dependent | 3 | VERIFIED — exact substring of title |
| 8 | B0013 | Ko2021PhysiolMeas | U-Net-based approach for automatic lung segmentation | 6 | VERIFIED — exact substring of title |
| 9 | B0013 | Ko2021PLOSONE | Semi-Siamese U-Net for separation of lung and heart bioimpedance images | 10 | VERIFIED — exact substring of title |
| 10 | B0013 | Ko2025CurrMedImaging | Reconstruction of Heart-related Imaging from Lung Electrical Impedance Tomography | 9 | VERIFIED — exact substring of title |
| 11 | B0013 | Ko2021PLOSONE | the separation effect of the EIT image obtained by the different reconstruction algorithms will be investigated | 16 | VERIFIED — exact substring of the primary full text (PMC7853495, Discussion, last paragraph); not in title/abstract |
| 12 | B0014 | Vandenhende2021 | Multi-Task Learning for Dense Prediction Tasks: A Survey | 8 | VERIFIED — exact substring of title |
| 13 | B0014 | Wang2024TIM | Dual-Branch U-Net Based on Deformable Convolution and Hyper-Convolution | 8 | VERIFIED — exact substring of title |
| 14 | B0014 | Yu2024CMPB | structure-aware hybrid-fusion learning | 3 | VERIFIED — exact substring of title |
| 15 | B0014 | Hamilton2018TMI | Deep D-Bar: Real-Time Electrical Impedance Tomography Imaging | 7 | VERIFIED — exact substring of title |
| 16 | B0014 | Herzberg2023PhysiolMeas | Domain independent post-processing with graph U-nets | 6 | VERIFIED — exact substring of title |
| 17 | B0014 | Zhang2022FBB | Advances of deep learning in electrical impedance tomography image reconstruction | 10 | VERIFIED — exact substring of title |
| 18 | B0014 | Denker2025HandbNumerAnal | Deep learning based reconstruction methods for electrical impedance tomography | 9 | VERIFIED — exact substring of title |
| 19 | B0016 | Zech2018PLoSMed | Variable generalization performance of a deep learning model | 8 | VERIFIED — exact substring of title |
| 20 | B0016 | AlBadawy2018MedPhys | Impact of cross-institutional training and testing | 6 | VERIFIED — exact substring of PubMed title (Crossref title uses U+2010) |
| 21 | B0016 | Liu2020TMI | Multi-Site Network for Improving Prostate Segmentation With Heterogeneous MRI Data | 10 | VERIFIED — exact substring of title |
| 22 | B0016 | HoangThi2021DIII | Which reconstruction kernel should be used? | 6 | VERIFIED — exact substring of title |
| 23 | B0016 | Zeng2022MedPhys | Generalizability over dose, reconstruction kernel, and slice thickness | 8 | VERIFIED — exact substring of title |
| 24 | B0017 | Hamilton2019PhysiolMeas | domain-independent deep D-bar learning | 4 | VERIFIED — exact substring of title |
| 25 | B0017 | Karani2018MICCAI | Across Scanners and Protocols | 4 | VERIFIED — exact substring of title |
| 26 | B0017 | Holzschuh2024RadiatOncol | The impact of multicentric datasets | 5 | VERIFIED — exact substring of title |
| 27 | B0019 | Lange2025StatMed | Confirmatory Methodological Research in Statistics and Related Fields | 8 | VERIFIED — title substring after dropping the curly quotes around “Confirmatory” |
| 28 | B0023 | Adler2006EIDORS | Uses and abuses of EIDORS | 5 | VERIFIED — exact substring of title |
| 29 | B0023 | Gagnon2010TBME | A Resistive Mesh Phantom for Assessing the Performance of EIT Systems | 11 | VERIFIED — exact substring of title |
| 30 | B0024 | Adler2009GREIT | GREIT: a unified approach to 2D linear EIT reconstruction of lung images | 12 | VERIFIED — exact substring of title |
| 31 | B0024 | Adler1996TMI | regularized imaging and contrast detection | 5 | VERIFIED — exact substring of title |
| 32 | B0024 | Adler2006EIDORS | an extensible software base for EIT | 6 | VERIFIED — exact substring of title |
| 33 | B0024 | Thurk2019PhysiolMeas | Influence of reconstruction settings | 4 | VERIFIED — exact substring of title |
| 34 | B0027 | Ronneberger2015UNet | U-Net: Convolutional Networks for Biomedical Image Segmentation | 7 | VERIFIED — exact substring of title |
| 35 | B0027 | Vandenhende2020Branched | Deciding what layers to share | 5 | VERIFIED — exact substring of title |
| 36 | B0027 | Isensee2024nnUNetRevisited | A Call for Rigorous Validation in 3D Medical Image Segmentation | 10 | VERIFIED — title substring after NBSP→space |
| 37 | B0028 | Caruana1997MTL | Multitask Learning | 2 | VERIFIED — exact substring of title |
| 38 | B0028 | Kurin2022Unitary | In Defense of the Unitary Scalarization for Deep Multi-Task Learning | 10 | VERIFIED — exact substring of title |
| 39 | B0028 | Xin2022MTOHelp | Do Current Multi-Task Optimization Methods in Deep Learning Even Help? | 10 | VERIFIED — exact substring of title |
| 40 | B0028 | Kendall2018 | Multi-task Learning Using Uncertainty to Weigh Losses | 7 | VERIFIED — exact substring of title |
| 41 | B0028 | Renard2020SciRep | Variability and reproducibility in deep learning for medical image segmentation | 10 | VERIFIED — exact substring of title |
| 42 | B0030 | Pulletz2006ROI | 20-35% of the maximum standard deviation or regression coefficient | 9 | VERIFIED — exact substring of PubMed abstract |
| 43 | B0033 | Jeschke2025Sensors | Robustness to Electrode Displacement | 4 | VERIFIED — exact substring of title |
| 44 | B0034 | Yu2024CVPR | Rethinking the Evaluation Protocol of Domain Generalization | 7 | VERIFIED — exact substring of title |
| 45 | B0037 | Willroth2024AMPPS | A Guide to Reporting Preregistration Deviations | 6 | VERIFIED — exact substring of title |
| 46 | B0039 | Wilcoxon1945 | Individual Comparisons by Ranking Methods | 5 | VERIFIED — exact substring of title |
| 47 | B0039 | Schuirmann1987JPharmacokinet | Two One-Sided Tests Procedure | 4 | VERIFIED — exact substring of title |
| 48 | B0039 | Lakens2017SPPS | Equivalence Tests: A Practical Primer | 5 | VERIFIED — exact substring of title |
| 49 | B0039 | Lakens2018AMPPS | Equivalence Testing for Psychological Research: A Tutorial | 7 | VERIFIED — exact substring of title |
| 50 | B0040 | Lakens2013EffectSize | Calculating and reporting effect sizes | 5 | VERIFIED — exact substring of title |
| 51 | B0040 | Christodoulou2024MICCAI | Confidence Intervals Uncovered | 3 | VERIFIED — exact substring of title |
| 52 | B0067 | Karani2018MICCAI | A Lifelong Learning Approach to Brain MR Segmentation | 8 | VERIFIED — exact substring of title |
| 53 | B0067 | Liu2020TMI | Multi-Site Network | 2 | VERIFIED — exact substring of title |
| 54 | B0067 | Myronenko2019AEReg | Autoencoder Regularization | 2 | VERIFIED — exact substring of title |
| 55 | B0069 | Holzschuh2024RadiatOncol | multicentric datasets | 2 | VERIFIED — exact substring of title |
| 56 | B0069 | Lakens2017SPPS | Equivalence Tests | 2 | VERIFIED — exact substring of title |
| 57 | B0069 | Venkatesh2026MedPhys | Performance benchmarking of deep learning models | 6 | VERIFIED — exact substring of title |
| 58 | B0070 | Thurk2019PhysiolMeas | reconstruction settings | 2 | VERIFIED — exact substring of title |
| 59 | B0072 | Grychtol2014PhysiolMeas | Choice of reconstructed tissue properties | 5 | VERIFIED — exact substring of title |
| 60 | B0072 | Albert2023ApplSci | Comparison of Image Normalization Methods for Multi-Site Deep Learning | 9 | VERIFIED — exact substring of title |
| 61 | B0072 | Karani2018MICCAI | Across Scanners and Protocols | 4 | VERIFIED — exact substring of title |
| 62 | B0072 | Delisle2021MedIA | Realistic image normalization for multi-Domain segmentation | 6 | VERIFIED — exact substring of title |
| 63 | B0074 | Yan2020RadiolAI | MRI Manufacturer Shift and Adaptation | 5 | VERIFIED — exact substring of title |
| 64 | B0074 | AlBadawy2018MedPhys | cross-institutional training and testing | 4 | VERIFIED — exact substring of PubMed title (Crossref title uses U+2010) |
| 65 | B0075 | Martensson2020MedIA | clinical out-of-distribution MRI data: A multicohort study | 7 | VERIFIED — exact substring of title |
| 66 | B0075 | Zech2018PLoSMed | Variable generalization performance | 3 | VERIFIED — exact substring of title |
| 67 | B0075 | Castro2020NatCommun | Causality matters | 2 | VERIFIED — exact substring of title |
| 68 | B0075 | Zeng2022MedPhys | reconstruction kernel, and slice thickness | 5 | VERIFIED — exact substring of title |
| 69 | B0075 | Kamann2021IJCV | Robustness of Semantic Segmentation Models with Respect to Common Corruptions | 10 | VERIFIED — exact substring of title |
| 70 | B0075 | Boone2023NeuroImage | out-of-distribution and corrupted data in MRI | 6 | VERIFIED — exact substring of title |
| 71 | B0075 | Du2022EurRadiol | harmonization of CT reconstruction kernels | 5 | VERIFIED — exact substring of title |
| 72 | B0075 | Billot2023MedIA | any contrast and resolution without retraining | 6 | VERIFIED — exact substring of title |
| 73 | B0077 | Scheel2021AMPPS | Comparing the Standard Psychology Literature With Registered Reports | 8 | VERIFIED — exact substring of title |
| 74 | B0077 | McGreivy2024NatMachIntell | Weak baselines and reporting biases | 5 | VERIFIED — exact substring of title |
| 75 | B0077 | Borji2018ImaVisComput | Negative results in computer vision | 5 | VERIFIED — exact substring of title |
| 76 | B0077 | Varoquaux2022NPJDigitMed | methodological failures and recommendations | 4 | VERIFIED — exact substring of title |
| 77 | B0077 | Nosek2018Prereg | The preregistration revolution | 3 | VERIFIED — exact substring of title |
| 78 | B0077 | Chambers2021NatHumBehav | Registered Reports | 2 | VERIFIED — exact substring of title |
| 79 | B0077 | Pawel2023BiomJ | Questionable research practices in comparative simulation studies | 7 | VERIFIED — exact substring of title |
| 80 | B0080 | Boyle2011PhysiolMeas | electrode area, contact impedance and boundary shape | 7 | VERIFIED — exact substring of title |
| 81 | B0081 | Boulesteix2013PLOSONE | A Plea for Neutral Comparison Studies | 6 | VERIFIED — exact substring of title |
| 82 | B0083 | Karani2018MICCAI | Across Scanners and Protocols | 4 | VERIFIED — exact substring of title |

**The two anchors changed tonight.**

| Key | Anchor | Source | Result |
|---|---|---|---|
| Zhao2014PhysiolMeas (B0011) | "No significant differences were found in all examined indices among the four reconstruction algorithms" | PubMed PMID 24845059 (efetch; DOI 10.1088/0967-3334/35/6/1083 confirmed in ArticleIdList) | **VERIFIED**, exact substring; the abstract continues "(p > 0.2, Kruskal-Wallis test)", which the draft reproduces |
| Pulletz2006ROI (B0030) | "20-35% of the maximum standard deviation or regression coefficient" | PubMed PMID 16636403 (DOI 10.1088/0967-3334/27/5/S10 confirmed) | **VERIFIED**, exact substring (ASCII hyphen in both); full sentence: "The definition of the ROI contour as 20-35% of the maximum standard deviation or regression coefficient is recommended." |

**The non-title anchor (Ko and Cheng 2021b, B0013).** Exact substring of PMC7853495 (Europe PMC full-text XML of doi:10.1371/journal.pone.0246071, PMID 33529234), last paragraph of the **Discussion** section: "…and the separation effect of the EIT image obtained by the different reconstruction algorithms will be investigated, notably, Shield back-projection algorithm, FEM-based linearized Newton-Raphson algorithm, and Graz consensus reconstruction algorithm (GREIT)." The v1 audit could check this only against project files; it is now verified against the primary source. Two wording points follow (flag E2).

---

## 4. Check D — retraction, correction, expression of concern

| Source (queried 2026-10-31) | Coverage | Result |
|---|---|---|
| Crossref `update-to` / `updated-by` (includes Retraction Watch records) | 73/73 registry DOIs (70 cited) | all empty |
| Crossref `relation` | 73/73 | only benign types: has-preprint (Lakens 2017, Nosek 2018), has-review (Willroth 2024, Frerichs 2017), is-referenced-by (Ronneberger 2015) |
| OpenAlex `is_retracted` | 73/73 | false for all |
| PubMed publication types + CommentsCorrections | 50 indexed records | no Retracted Publication, Retraction of Publication, Expression of Concern, Erratum; no RetractionIn / ErratumIn / ExpressionOfConcernIn / UpdateIn links |

**0 retractions, 0 corrections, 0 expressions of concern.** Coverage limit: 23 registry works are not in PubMed (proceedings, IEEE/MDPI/AMPPS titles, the Denker chapter); for them the check rests on Crossref and OpenAlex.

---

## 5. Check E — claim–source context (ADVISORY)

**Method and limits.** Each citing sentence was read against the abstract named in the "Basis" column, retrieved today (no project notes were used as the source of truth in this pass). An abstract cannot show that a claim is absent from the full text; where the claim goes beyond the abstract, the row says so. Legend: **OK** = supported as worded; **minor** = wording or scope point; **FLAG** = the sentence contradicts, or states a number or attribution not found in, the source.

| # | Block | Key | Claim as worded (abridged) | Basis (retrieved 2026-10-31) | Assessment |
|---|---|---|---|---|---|
| 1 | B0011 | Frerichs2017TREND | Clinical use rests on regional ventilation indices | PubMed abstract (PMID 27596161) | OK — TREND consensus on examination, analysis, clinical use |
| 2 | B0011 | Zhao2014PhysiolMeas | Four algorithms, five indices, none differed significantly (p > 0.2, Kruskal–Wallis) | PubMed abstract (PMID 24845059) | OK as to the clause (exact abstract numbers); **FLAG E6** for the topic clause "insensitive" |
| 3 | B0011 | Grychtol2014PLOSONE | Twelve reconstructions: appearance differences not negligible, clinical parameters close | PubMed abstract (PMID 25110887) | **FLAG E5** — abstract restricts closeness to "the advanced algorithms" |
| 4 | B0011 | Zhou2023TPAMI | DG literature cited only where compared | PubMed abstract (PMID 35914036) | OK |
| 5 | B0011 | Yoon2024ProcIEEE | same | title only | OK (title only; review) |
| 6 | B0013 | Leathard1994PhysiolMeas | Cardiac change several times smaller than ventilation change | PubMed abstract (PMID 8087036) | OK — 9% vs −0.9 to −2.6% (m9) |
| 7 | B0013 | Graf2017PLOSONE | …and highly position dependent | PubMed abstract (PMID 29145478) | OK — title; posture changes cardiac amplitudes |
| 8 | B0013 | Ko2021PhysiolMeas | U-Net for lung segmentation in EIT | PubMed abstract (PMID 33498021) | OK — title |
| 9 | B0013 | Ko2021PLOSONE | Semi-Siamese U-Net, one encoder, two parallel decoders | PubMed abstract + PMC7853495 full text | OK — abstract and full text |
| 10 | B0013 | Ko2025CurrMedImaging | Heart-related reconstruction from GREIT frames with optimised loss weights | PubMed abstract (PMID 40611416) | OK — abstract |
| 11 | B0013 | Ko2021PLOSONE | Quoted plan, "conclusions state", "naming GREIT, Gauss–Newton and back-projection" | PubMed abstract + PMC7853495 full text | Quote verbatim (full text); **FLAG E2** — section is Discussion; algorithms named differently |
| 12 | B0014 | Vandenhende2021 | Decoder-side branch belongs to the branched multi-task family | PubMed abstract (PMID 33497328) | OK — survey covers MTL architectures |
| 13 | B0014 | Wang2024TIM | EIT relative: dual-branch reconstructor | OpenAlex abstract | OK as "dual-branch" (abstract: two-branch U-Net); "downstream of a reconstruction operator" **unverified** (part of E1) |
| 14 | B0014 | Yu2024CMPB | Multi-branch network built for noise tolerance; downstream of a reconstruction operator | PubMed abstract (PMID 37931580) | **FLAG E1** — network maps measurement voltages to conductivity; aim is resolution + robustness to noise and modelling errors |
| 15 | B0014 | Hamilton2018TMI | Post-processing networks for EIT | PubMed abstract (PMID 29994023) | OK — CNN after D-bar |
| 16 | B0014 | Herzberg2023PhysiolMeas | same | PubMed abstract (PMID 37944184) | OK — graph U-net post-processing |
| 17 | B0014 | Zhang2022FBB | same (review) | PubMed abstract (PMID 36588934) | OK — review of DL in EIT reconstruction |
| 18 | B0014 | Denker2025HandbNumerAnal | Same U-Net after linearised reconstruction or D-bar performs differently | arXiv 2508.06281 abstract (preprint, not chapter) | Not in the arXiv abstract (which compares fully-learned, post-processing, learned iterative methods); m4, chapter unverified |
| 19 | B0016 | Zech2018PLoSMed | Pneumonia detection generalised variably across hospitals | PubMed abstract (PMID 30399157) | OK — abstract |
| 20 | B0016 | AlBadawy2018MedPhys | Cross-institutional tumour segmentation lost Dice | PubMed abstract (PMID 29356028) | OK — significant decrease, P < 0.0001 |
| 21 | B0016 | Liu2020TMI | Multi-site segmentation needed site-specific normalisation | PubMed abstract (PMID 32078543) | minor m6 — source proposes domain-specific BN |
| 22 | B0016 | HoangThi2021DIII | CT kernel training-by-evaluation matrix with a pooled row | PubMed abstract (PMID 34686464) | OK — LK, MK, LK+MK × LK, MK |
| 23 | B0016 | Zeng2022MedPhys | Cross-evaluation varying kernel, slice thickness, dose one at a time | PubMed abstract (PMID 34954845) | OK — "changing only one parameter in each pair" |
| 24 | B0017 | Hamilton2019PhysiolMeas | Nearest EIT study broadens the training domain in geometry | PubMed abstract (PMID 31091516) | OK — boundary-shape-independent training |
| 25 | B0017 | Karani2018MICCAI | Per-source normalisation in batch-normalisation layers | Semantic Scholar abstract | OK — "domain-specific batch normalization layers" |
| 26 | B0017 | Holzschuh2024RadiatOncol | Leave-one-centre-out comparison concluded from a non-significant p | PubMed abstract (PMID 39113123) | OK — p = 0.18, "mostly generalize well" |
| 27 | B0019 | Lange2025StatMed | Vocabulary of confirmatory methodological research | PubMed abstract (PMID 41213159) | OK — wording credits the vocabulary (v1 A7 done) |
| 28 | B0023 | Adler2006EIDORS | EIDORS toolbox v3.8 | PubMed abstract (PMID 16636416) | OK (m13) |
| 29 | B0023 | Gagnon2010TBME | An EIT system's SNR depends on its operating conditions | PubMed abstract (PMID 20550982) | OK — indicators depend on frame rate, frequency, current, strategy |
| 30 | B0024 | Adler2009GREIT | GREIT, Graz consensus reconstruction algorithm | PubMed abstract (PMID 19491438) | OK — title |
| 31 | B0024 | Adler1996TMI | Noise figure = image relative noise / measurement relative noise | PubMed abstract (PMID 18215899) | OK — abstract: figure of merit for noise amplification (v1 A8 done) |
| 32 | B0024 | Adler2006EIDORS | Sheffield back-projection matrix distributed with EIDORS | PubMed abstract (PMID 16636416) | OK |
| 33 | B0024 | Thurk2019PhysiolMeas | Reconstruction settings strongly influence output | PubMed abstract (PMID 31125984) | OK — "strong influence on the resulting FoM" |
| 34 | B0027 | Ronneberger2015UNet | U-Net encoder | title only | OK (title only; seminal) |
| 35 | B0027 | Vandenhende2020Branched | Fixed-budget comparison of branch structures | OpenAlex abstract | OK — "given a specific budget, i.e. number of learnable parameters" |
| 36 | B0027 | Isensee2024nnUNetRevisited | Adequately configured, capacity-matched baseline is the missing control | arXiv 2404.09556 abstract | minor m3 — source: inadequate baselines, neglected compute |
| 37 | B0028 | Caruana1997MTL | Hard parameter sharing | title only | minor m7 — wording (the shared encoder is the sharing) |
| 38 | B0028 | Kurin2022Unitary | Unit weights matched specialised MT optimisers | OpenAlex abstract | OK — "unitary scalarization … matches or improves upon" |
| 39 | B0028 | Xin2022MTOHelp | …or tuned fixed weights | OpenAlex abstract | OK — "weighted average of the task losses" |
| 40 | B0028 | Kendall2018 | Learned weighting not tested | title only | OK (title only) |
| 41 | B0028 | Renard2020SciRep | Seed variability of the order of the effects at stake | PubMed abstract (PMID 32792540) | minor m8 — authors' inference |
| 42 | B0030 | Pulletz2006ROI | 25% inside the 20–35% band recommended for ROI definition, on per-pixel statistics | PubMed abstract (PMID 16636403) | Anchor verified; caveat accurate; minor m1 (one study, not "methods") |
| 43 | B0033 | Jeschke2025Sensors | Training-by-evaluation crossing follows EIT cross-condition designs | PubMed abstract (PMID 41228767) | OK — 4 training × 4 testing displacement levels; m12 |
| 44 | B0034 | Yu2024CVPR | Nothing selected on the held-out reconstructor | OpenAlex abstract | OK — oracle model selection as leakage |
| 45 | B0037 | Willroth2024AMPPS | Deviation reporting structure | Crossref abstract | OK |
| 46 | B0039 | Wilcoxon1945 | Signed-rank test | title only | OK (title only; seminal) |
| 47 | B0039 | Schuirmann1987JPharmacokinet | 95% CI inside margin ≡ TOST at α 0.025 | PubMed abstract (PMID 3450848) | OK — TOST origin |
| 48 | B0039 | Lakens2017SPPS | 90% interval usual in equivalence testing | PubMed abstract (PMID 28736600) | OK |
| 49 | B0039 | Lakens2018AMPPS | same | Crossref abstract | OK |
| 50 | B0040 | Lakens2013EffectSize | Cohen's dz | PubMed abstract (PMID 24324449) | OK |
| 51 | B0040 | Christodoulou2024MICCAI | Intervals rarely reported in segmentation studies | Semantic Scholar abstract | OK — 1 of 221 MICCAI 2023 papers (v1 A4 done) |
| 52 | B0067 | Karani2018MICCAI | Source-specific normalisation layers not tested | Semantic Scholar abstract | OK |
| 53 | B0067 | Liu2020TMI | same | PubMed abstract (PMID 32078543) | OK |
| 54 | B0067 | Myronenko2019AEReg | Second decoder as regulariser | Semantic Scholar abstract | OK — VAE branch "to regularize" |
| 55 | B0069 | Holzschuh2024RadiatOncol | Median Dice 0.76 pooled vs 0.74 held out, p = 0.18 | PubMed abstract (PMID 39113123) | OK — exact abstract numbers |
| 56 | B0069 | Lakens2017SPPS | Non-significance cannot establish equivalence; a margin can | PubMed abstract (PMID 28736600) | OK |
| 57 | B0069 | Venkatesh2026MedPhys | One precedent (within the search) for equivalence testing on segmentation Dice | PubMed abstract (PMID 41933401) | OK — TOST on DSC between models; scoped (v1 A6 done) |
| 58 | B0070 | Thurk2019PhysiolMeas | Settings alone change output substantially | PubMed abstract (PMID 31125984) | OK |
| 59 | B0072 | Grychtol2014PhysiolMeas | Within one algorithm amplitude changes with the reconstructed quantity | PubMed abstract (PMID 24844670) | OK — same algorithm, resistivity vs conductivity, large differences |
| 60 | B0072 | Albert2023ApplSci | Normalisation choice changes Dice by < 0.02 | Crossref abstract | OK for the number; minor m2 for the intensity premise |
| 61 | B0072 | Karani2018MICCAI | Per-source step can live in BN layers | Semantic Scholar abstract | OK |
| 62 | B0072 | Delisle2021MedIA | …or be learned across datasets | PubMed abstract (PMID 34509168) | OK — learned common normalizer |
| 63 | B0074 | Yan2020RadiolAI | LV segmentation fell from Dice 0.89 to 0.60 | PubMed abstract (PMID 33937833) | **FLAG E3** — no such pair in the abstract |
| 64 | B0074 | AlBadawy2018MedPhys | Cross-institutional tumour segmentation at 0.59 to 0.68 | PubMed abstract (PMID 29356028) | Levels correct; **FLAG E4** for the loss comparison that follows |
| 65 | B0075 | Martensson2020MedIA | Training-source diversity improves OOD performance | PubMed abstract (PMID 33007638) | OK — "more heterogeneous training data makes the model generalize better" |
| 66 | B0075 | Zech2018PLoSMed | Pooled models strong internally, weak externally | PubMed abstract (PMID 30399157) | OK — AUC 0.931 internal vs 0.815 external |
| 67 | B0075 | Castro2020NatCommun | Reconstructor change is one kind of acquisition shift | PubMed abstract (PMID 32699250) | OK — causal categorisation of dataset mismatch; the classification is the authors' |
| 68 | B0075 | Zeng2022MedPhys | Kernel changes costly, slice-thickness changes not | PubMed abstract (PMID 34954845) | OK — m11 |
| 69 | B0075 | Kamann2021IJCV | Tolerance differs by corruption type | Crossref abstract | OK — "depends strongly on the type of image corruption" |
| 70 | B0075 | Boone2023NeuroImage | same | PubMed abstract (PMID 37495197) | OK — "susceptibility to particular classes of transforms" |
| 71 | B0075 | Du2022EurRadiol | Learned harmonisation outperforms location-scale baseline | PubMed abstract (PMID 36355196) | OK — CNN > ComBat / centering-scaling; m10 (radiomics) |
| 72 | B0075 | Billot2023MedIA | Training-distribution randomisation | PubMed abstract (PMID 36857946) | OK — domain randomisation |
| 73 | B0077 | Scheel2021AMPPS | Positive results 44% vs 96% | Crossref abstract | OK — exact abstract numbers |
| 74 | B0077 | McGreivy2024NatMachIntell | Nulls against matched baselines exposed to under-reporting | Semantic Scholar abstract | OK in substance; minor m5 ("most") |
| 75 | B0077 | Borji2018ImaVisComput | same | Semantic Scholar abstract | OK — value of negative results in CV |
| 76 | B0077 | Varoquaux2022NPJDigitMed | same | PubMed abstract (PMID 35413988) | OK — methodological failures (abstract via PubMed) |
| 77 | B0077 | Nosek2018Prereg | Preregistration makes such results reportable | PubMed abstract (PMID 29531091) | OK |
| 78 | B0077 | Chambers2021NatHumBehav | same | PubMed abstract (PMID 34782730) | OK — Registered Reports remedy reporting biases |
| 79 | B0077 | Pawel2023BiomJ | Simulation comparisons can favour any method unless rules fixed | PubMed abstract (PMID 36890629) | OK — title |
| 80 | B0080 | Boyle2011PhysiolMeas | Electrode and boundary-shape errors produce structured artefacts | PubMed abstract (PMID 21646710) | OK — ringing / distributed / structured artefacts |
| 81 | B0081 | Boulesteix2013PLOSONE | Not a neutral comparison in Boulesteix's sense | PubMed abstract (PMID 23637855) | OK |
| 82 | B0083 | Karani2018MICCAI | Per-source affine needs a domain label at test time, as domain-specific BN does | Semantic Scholar abstract | OK — domain-specific BN requires the domain at test time |

### Flags (exact sentence, finding, recommended fix)

**E1 — B0014, Yu et al. 2024a (Yu2024CMPB), restored reference. FLAG: contradicted by the source.**
Sentence: "The branch is a decoder-side branch serving one target each, of the branched multi-task family (Vandenhende et al., 2022), with EIT relatives in a dual-branch reconstructor (Wang et al., 2024) and a multi-branch network built for noise tolerance (Yu et al., 2024a). All sit downstream of a reconstruction operator, as do the post-processing networks for EIT (…)"
Source (PubMed PMID 37931580 abstract): SA-HFL "aims to mine the deep feature information from measurement voltages … to reconstruct the high-resolution conductivity distribution"; its segmentation and reconstruction branches "extract different feature information from the measurement voltage". It is a voltage-to-conductivity network, i.e. it replaces the reconstruction operator rather than sitting downstream of it. Its stated aim is high resolution plus "robustness against the measurement noise and modeling errors", not noise tolerance alone. For Wang et al. 2024 (DHU-Net) the abstract does not say whether the input is voltages or a preliminary image, so "downstream" is unverified for it too.
Fix: "…with EIT relatives in a dual-branch U-Net (Wang et al., 2024) and a multi-branch network that reconstructs conductivity directly from boundary voltages, built for resolution and robustness to noise and modelling errors (Yu et al., 2024a). The branch tested here sits downstream of a reconstruction operator, as do the post-processing networks for EIT (…)". Confirm Wang's input domain from the IEEE full text before saying which side of the operator it sits.

**E2 — B0013, Ko and Cheng 2021b (second instance). FLAG: attribution wording.**
Sentence: "The semi-Siamese study's conclusions state that "the separation effect of the EIT image obtained by the different reconstruction algorithms will be investigated" (Ko and Cheng, 2021b), naming GREIT, Gauss–Newton and back-projection; this paper answers it."
Source (PMC7853495): the sentence is in the last paragraph of the **Discussion**, not in the Conclusions section, and it names "Shield back-projection algorithm, FEM-based linearized Newton-Raphson algorithm, and Graz consensus reconstruction algorithm (GREIT)". "Gauss–Newton" is the authors' mapping of the linearised Newton–Raphson (carried from v1 A10, still open); B0024 then calls the three reconstructors "those the original study named".
Fix: "The semi-Siamese study closes its discussion with the plan that "…will be investigated" (Ko and Cheng, 2021b), naming back-projection, a linearised Newton–Raphson algorithm and GREIT; this paper answers it, with one-step Gauss–Newton as the linearised Newton–Raphson." Optionally adjust B0024 to "the three algorithm families the original study named".

**E3 — B0074, Yan et al. 2020. FLAG: number pair not in the source.**
Sentence: "The nearest clinical analogues are a left-ventricle segmentation network that fell from Dice 0.89 to 0.60 when the MRI manufacturer changed (Yan et al., 2020)…"
Source (PubMed abstract): Dice fell from 89.7% to 68.7%, from 90.6% to 59.5%, and from 89.2% to 64.1% for manufacturers 1, 2 and 3. No pair is 0.89 → 0.60 (0.60 belongs to the 0.906 baseline; 0.89 to the other two).
Fix: "…that fell from Dice 0.91 to 0.60 (and by 21 to 31 points across the three manufacturers) when the MRI manufacturer changed (Yan et al., 2020)".

**E4 — B0074, AlBadawy et al. 2018 and the magnitude comparison (Section 4.4). FLAG: levels reported as if they were losses; comparison overstated.**
Sentence: "…and cross-institutional tumour segmentation at 0.59 to 0.68 (AlBadawy et al., 2018); the 16 to 62 points lost here and the exploratory 19 to 33 points are of that order, but two differences forbid a comparison of magnitudes…"
Source (PubMed abstract): 0.68 and 0.59 are the cross-institution Dice **levels**; the same-institution values were 0.72 and 0.76, so the losses were about 4 and 17 points (pairing the values in the order the abstract gives them). With Yan (21–31 points) the analogues lost 4 to 31 points; this study's 16 to 62 points overlap the upper part of that range and reach twice it, so "of that order" is generous, and it sits uneasily with the same sentence's "forbid a comparison of magnitudes". Separately, "19 to 33 points" contradicts the "19 to 34 points" stated in the abstract (B0006), B0051, B0066 and B0070 (not a citation item, but in this sentence).
Fix: "…and cross-institutional tumour segmentation that fell from 0.72–0.76 to 0.59–0.68 (AlBadawy et al., 2018). Those losses, 4 to 31 points, and the 16 to 62 points lost here (19 to 34 exploratory) are at least of the same kind, but two differences forbid a comparison of magnitudes: …". Reconcile 33/34 against Table 2.

**E5 — B0011, Grychtol et al. 2014a. FLAG (scope): restriction in the source dropped.**
Sentence: "…and twelve reconstructions differed in appearance by amounts that were not negligible while the clinical parameters derived from them were close (Grychtol et al., 2014a)."
Source (PubMed abstract): "clinically relevant parameters do not vary considerably **among the advanced algorithms**", and "some others are significantly worse". The closeness is not stated for all twelve.
Fix: "…while the clinical parameters derived from the advanced algorithms among them were close (Grychtol et al., 2014a)."

**E6 — B0011, Zhao et al. 2014, topic clause. FLAG (internal consistency): non-significance read as insensitivity.**
Sentence: "Those indices are insensitive to which linear reconstructor produced the image: four algorithms applied to the same recordings gave five ventilation indices none of which differed significantly between algorithms (p > 0.2, Kruskal–Wallis) (Zhao et al., 2014)…"
Source: the second clause is now exact (v1 A3 done), and the source itself concludes the algorithms "do not influence the selected indices" (8 patients). But the draft's own B0069 says "Non-significance cannot establish equivalence", and the topic clause "insensitive" is that inference. The section heading (1.1) repeats it.
Fix: "Those indices have shown little sensitivity to which linear reconstructor produced the image: …" (or "were not detectably affected by"); keep the heading or soften it in the same way.

### Minor items (no flag; wording)

| ID | Block | Key | Point | Suggestion |
|---|---|---|---|---|
| m1 | B0030 | Pulletz2006ROI | "the 20–35% band that clinical region-of-interest methods recommend" — the band is one study's recommendation (10 patients) | "the 20–35% band recommended for functional-image ROI definition (Pulletz et al., 2006)"; the per-pixel-statistics caveat is accurate and should stay |
| m2 | B0072 | Albert2023ApplSci | "whose unitless intensities differ by far less than two orders of magnitude" is not in the source; Dice < 0.02 is | Mark it as the authors' premise ("which we take to differ by…") or drop the clause |
| m3 | B0027 | Isensee2024nnUNetRevisited | "capacity-matched" glosses the source's "inadequate baselines … neglected computational resources" | "an adequately configured baseline at comparable compute is the control whose absence…" |
| m4 | B0014 | Denker2025HandbNumerAnal | Post-UNet vs Deep D-bar statement is not in the arXiv abstract; only the arXiv full text was read (registry); chapter not checked (v1 A11 open) | Confirm in the Elsevier chapter, pp 127–175 |
| m5 | B0077 | McGreivy / Borji / Varoquaux | "the kind of result most exposed to under-reporting" — the superlative is not in the sources (McGreivy: weak baselines and under-reporting of negative results) | "a kind of result exposed to under-reporting" |
| m6 | B0016 | Liu2020TMI | "needed site-specific normalisation" — the source proposes and benefits from domain-specific BN | "used site-specific normalisation" |
| m7 | B0028 | Caruana1997MTL | "The second decoder is hard parameter sharing" — sharing the encoder is | "Sharing one encoder between the two decoders is hard parameter sharing" |
| m8 | B0028 | Renard2020SciRep | "of the order of the effects at stake" is the authors' inference from a variability review | Optional: "seed-to-seed variability can be large (Renard et al., 2020), and here it is of the order of the effects at stake" |
| m9 | B0013 | Leathard1994PhysiolMeas | "several times smaller" — source: 9% vs −0.9 to −2.6% (3.5 to 10×) in 10 normal subjects: supported; note that it is resistivity change in Sheffield Mk2 images | none required |
| m10 | B0075 | Du2022EurRadiol | outperformance shown for radiomics models, not segmentation | "which outperformed location-scale harmonisation for CT radiomics" |
| m11 | B0075 | Zeng2022MedPhys | a denoising, not segmentation, network — "CT analogue" wording is fine | none required |
| m12 | B0033 | Jeschke2025Sensors | "EIT cross-condition designs" (plural) rests on one study | "follows an EIT cross-condition design (Jeschke et al., 2025)" |
| m13 | B0023 | Adler2006EIDORS | v3.8 software cited by the 2006 paper — standard EIDORS practice | none required |

**Blocks named in the brief.** Section 1.1 (B0011): Frerichs OK; Zhao E6; Grychtol E5. Methods 2.1 (B0023–B0024): Adler and Lionheart 2006 OK ×2; Gagnon OK (abstract: performance indicators depend on frame rate, frequency, current…); Adler 2009 OK; Adler and Guardo 1996 OK — the noise-figure definition is now cited where it is used (v1 A8 done) and matches the paper's noise-amplification figure of merit; Thürk OK ("strong influence" is the abstract's wording). Section 2.3 (B0030): Pulletz anchor verified, m1. Section 4.4 (B0074–B0075): E3, E4; Mårtensson, Zech, Castro, Zeng, Kamann, Boone, Billot OK; m10. Restored references: Leathard OK (m9), Yu 2024a **E1**, Jeschke OK (m12), Kamann OK ("depends strongly on the type of image corruption"), Boone OK ("robustness susceptibility to particular classes of transforms"), Boyle OK (contact-impedance and boundary-shape errors give ringing, distributed or structured artefacts).

**v1 actions now closed in the text:** A3 (Zhao "did not differ"), A4 (Christodoulou attached to the CI clause), A5 partly (Isensee "most often" removed; m3 remains), A6 (Venkatesh search scope), A7 (Lange vocabulary), A8 (Adler 1996 moved), A9 (Wang "encoder-side" dropped), A12 partly (Grychtol, Herzberg, Xin, Dice scale fixed; but see E5), A1 (the noise-sweep reading is now explicitly disowned in B0049). Still open: A10 (→ E2), A11 (→ m4), A13 (Zhang lone b), A14 (Karani volume), A15 (particles), A16 (Wang article number), A17 (format-convert), A18 (re-run before submission).

---

## 6. Check F — PLoS One citability

Rule source: `refs/01_JOURNAL_REQUIREMENTS_PLOSONE.md` (no submitted-but-unaccepted manuscripts in the reference list; no "data not shown").

| Item | Result |
|---|---|
| Companion core paper in `refs_in_recon.json` | **no key** |
| Companion core paper in the reference list (B0092) | **absent** (70 published works, all resolving DOIs today) |
| Ref marker pointing at it | none |
| Related manuscript statement (B0089) | present: "…is under review elsewhere and is declared as a related submission; a copy accompanies this submission. The present manuscript relies on none of its reported findings…" + `[MATERIAL GAP: preprint DOI, to be inserted when the companion study is posted as a preprint; until then it is not cited and the accompanying copy is the reference.]` ✓ |
| Other mentions | B0013 (Introduction; ends with `[MATERIAL GAP: preprint DOI]`), and **without** marker as the provenance of the reused GREIT networks in B0028 (2.2), B0036 (2.5), B0046 and B0049 (3.1–3.2), B0057 (3.4), B0105 and B0107 (Table 1 caption and note), B0116 (Table 4). B0001 holds an HTML comment (not rendered). None is a citation or relies on the companion's findings; B0049 explicitly says the registered reading's "noise sweep … is the companion study's, whose result this paper does not use" |
| "data not shown", "unpublished", "personal communication" | none |
| Preprints / arXiv in the list | none (Denker is cited as the Elsevier chapter) |
| Citations in the abstract | none |

**Result: PASS.** The literal rule is met. Note for the PI: the brief's expectation ("appears only in the Related manuscript statement") is not literally true; the companion is named in ten blocks, two of them with the `[MATERIAL GAP]` marker. The eight unmarked mentions are data-provenance statements that the reuse disclosure requires, so I do not recommend removing them; if a single cross-reference is preferred, add "(see Related manuscript)" at the first unmarked mention (B0028).

---

## 7. Check G — registry orphans (in `refs_in_recon.json`, never cited; fate = PI decision)

| Key | DOI | Registry note (abridged) | Consequence if it stays uncited |
|---|---|---|---|
| Rusak2020ECCV | 10.1007/978-3-030-58580-8_4 | §4 Gaussian-noise training changes generalisation to unseen corruptions; the core paper's noise-axis comparison | none for this draft |
| Zhang2020TMI | 10.1109/tmi.2020.2973595 | §4 pooled vs dedicated (BigAug), peer practice for the M2′/L1 reporting frame | none for this draft |
| Zhang2022PhysiolMeas | 10.1088/1361-6579/ac9c44 | §1 Siamese network for cardiac-related component separation (PM 2022) | it is the "a" partner of the cited "Zhang et al., 2022b" (Zhang2022FBB); uncited, the lone "b" should be dropped if author-year survives anywhere |

All three resolve today (Crossref 200, no retraction/update relation). Not decided here.

---

## 8. Self-citation and currency

| Measure | Count | Ratio | Threshold | Result |
|---|---|---|---|---|
| Entries authored by Ko YF (Ko2021PhysiolMeas, Ko2021PLOSONE, Ko2025CurrMedImaging) | 3/70 | 4.3% | 15% | PASS |
| Instances | 4/82 | 4.9% | 15% | PASS |

No other entry lists Ko YF, Chen CW or Wang TC in its author list.

Before 2016 (16/70): Wilcoxon 1945, Schuirmann 1987, Caruana 1997 (seminal methods); Adler and Guardo 1996, Adler and Lionheart 2006, Pulletz 2006, Adler 2009, Gagnon 2010, Boyle 2011, Lakens 2013, Boulesteix 2013, Ronneberger 2015 (standard method/software/concept references); Leathard 1994 (classic physiology amplitude data; no newer equivalent in the registry); Zhao 2014, Grychtol 2014a, Grychtol 2014b (primary EIT findings, roles stated in the text). 2016–2020: 20; 2021–2026: 34 (48.6%). ADVISORY only.

---

## 9. Verdict

Under the strict policy (FAIL on any unresolvable entry, any mismatched DOI or author list, any unverifiable anchor, or any retracted source):

- unresolvable entries: 0 (73/73 DOIs resolve on Crossref today)
- string mismatches (any field): 0/70
- DOI or author-list mismatches: 0 (three author lists match only through their logged overrides: Kendall2018, Kurin2022Unitary, Vandenhende2020Branched)
- anchors VERIFIED / NOT FOUND / PARAPHRASE: 82 / 0 / 0
- retractions / corrections / expressions of concern: 0 / 0 / 0
- context flags (advisory, not strict): 6 (E1–E6); minor items: 13

`citation_check=PASS WITH FLAGS`

---

## 10. Actions for the author

None was applied; the draft is unchanged. Ordered by weight.

1. **E1 (before submission).** B0014: rewrite the Yu 2024a clause — SA-HFL reconstructs from voltages, so "All sit downstream of a reconstruction operator" is false for it; restrict "downstream" to the branch tested here and the post-processing networks. Check Wang 2024 (DHU-Net) input domain in the IEEE full text.
2. **E3 (before submission).** B0074: replace "0.89 to 0.60" with a pair the abstract reports (0.91 → 0.60, or the 21–31-point range).
3. **E4 (before submission).** B0074: report AlBadawy as 0.72–0.76 → 0.59–0.68 (4–17-point losses), restate "of that order" against losses of 4–31 points, and reconcile "19 to 33" with the "19 to 34" used elsewhere (check Table 2).
4. **E2.** B0013: "conclusions state" → the plan is in the Discussion; name the algorithms as the source does (Sheffield back-projection, linearised Newton–Raphson, GREIT) and state that one-step Gauss–Newton is this study's linearised Newton–Raphson; align B0024 "those the original study named".
5. **E5.** B0011: add "among the advanced algorithms" to the Grychtol 2014a closeness clause.
6. **E6.** B0011 (and the 1.1 heading): soften "insensitive" so it does not read non-significance as equivalence, consistent with B0069.
7. **Minor wording m1–m3, m5–m8, m10, m12** (§5 table), at the author's discretion.
8. **m4 / v1 A11.** Confirm the Denker 2025 Post-UNet vs Deep D-bar statement in the Elsevier chapter.
9. **G (PI decision).** Decide the three orphans (Rusak2020ECCV, Zhang2020TMI, Zhang2022PhysiolMeas). If Zhang2022PhysiolMeas stays uncited, drop the "b" from "Zhang et al., 2022b"; the Grychtol a/b letters are also unnecessary under author-year.
10. **F (optional).** Add "(see Related manuscript)" at the first unmarked companion mention (B0028) if a cross-reference is wanted.
11. **Metadata.** Add the Karani2018MICCAI LNCS volume via `refs/overrides.json` from the Springer chapter page and re-render; verify "Genderingen HRv", "Palma ND", "Boulesteix A" against publisher bylines; replace Wang 2024 "1-16" with the article number if the publisher gives one (v1 A14–A16).
12. **Format-convert.** F1–F4, F6, F7, F10, F11 (§1).
13. **Re-run.** After the E1–E6 edits (a revision round, per lab rule R16 / 流程優先), re-run this citation-check; immediately before submission re-run `tools/cite.py` + `apply_ref_overrides.py` for a fresh retraction check.
