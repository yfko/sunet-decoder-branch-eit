# Ready gate — PLoS One submission of the RECON tier-3 paper (2026-10-31 21:08; tools/ready_gate_plos.py)

| Item | Result | Evidence |
|---|---|---|
| five-seat round-1 review on file | **PASS** | 12_REVIEWER_PANEL_round1.md (2026-10-31 11:57) |
| legacy re-review checker exit 0, decision Minor Revision | **PASS** | re-review synthesis ok: round 'sunet-recon-tier3-rereview-round1-20261031', revision 2, decision_state 'Minor Revision', |
| scoped re-verification of round 1e judged the v6 bytes: Accept (scoped), all FULLY | **PASS** | judged ab11b87add5c == v6 ab11b87add5c; Accept (scoped); 11 items |
| v6 -> v7 changed only the reference list and its bracket (no reviewed sentence changed after the scoped Accept) | **PASS** | changed blocks ['B0091', 'B0092'] |
| v7 -> v8 changed only the AI-disclosure paragraph and deleted the funding/COI section (round 1g; sections 1-5 byte-identical) | **PASS** | changed ['B0087']; removed ['B0153', 'B0154']; added [] |
| scoped re-verification of round 1g judged the v8 bytes: Accept (scoped), all FULLY | **PASS** | judged 9085e617e453 == v8 9085e617e453; Accept (scoped); 2 items |
| citation-check v3 (strict) on file | **PASS** | 16_CITATION_AUDIT_v3.md (2026-10-31 14:46); PASS WITH FLAGS |
| scoped citation re-check v6 on file | **PASS** | 21_CITATION_RECHECK_v6.md (2026-10-31 17:50); PASS WITH FLAGS |
| scoped citation re-check v7 (reference metadata + deliverable list + retraction refresh) on file | **PASS** | 25_CITATION_RECHECK_v7.md (2026-10-31 18:19); PASS WITH FLAGS |
| apply chain 19_DRAFT_v5.md -> 20_DRAFT_v6.md | **PASS** | base bf252f799a3a out ab11b87add5c witness pass |
| apply chain 20_DRAFT_v6.md -> 23_DRAFT_v7.md | **PASS** | base ab11b87add5c out d02ec9b62ff1 witness pass |
| apply chain 23_DRAFT_v7.md -> 30_DRAFT_v8.md | **PASS** | base d02ec9b62ff1 out 9085e617e453 witness pass |
| main text <= 8,000 (PCR), abstract <= 300, 0 orphans, R10b clean | **PASS** | 7998 words; abstract 296; orphans 0 |
| R10c: every number in the draft derivable from the result/registration files | **PASS** | numbers in prose: 375; not derivable from the result/registration files: 0 |
| package Manuscript.md == 31_ record copy (v8) | **PASS** | 8260dd14af3f |
| DOCX: continuous line numbers, page-number field, double spacing | **PASS** | lnNumType True; PAGE True; line=480 True; docx 2026-10-31 21:08 |
| title identical in deliverable md, docx, cover letter, system fields | **PASS** | 177 chars; docx True; letter True; fields True |
| abstract == draft abstract, <= 300 words, no citation | **PASS** | 296 words; identical True |
| author-supplied placeholders filled (repository tag, companion preprint DOI; Data availability names S1 Data, round 1h) | **PENDING** | 5 open:  Zenodo DOI, minted at submission; t;  Zenodo DOI, minted at submission];  preprint DOI, see Related manuscrip;  preprint DOI, to be inserted when t;  repository tag, set at submission] |
| no pipeline leak, no markers, no CJK in deliverable (md + docx) | **PASS** | leaks []; CJK 0 |
| tables and figures cited in ascending order of first appearance; captions follow the citing paragraph | **PASS** | tables [1, 2, 3, 4]; figs [1, 2, 3, 4, 5] |
| S-items numbered by type in order of first citation | **PASS** | ['S1 Table', 'S2 Table', 'S1 Appendix', 'S3 Table', 'S1 Fig'] |
| references 1..N contiguous, PLoS 'doi: ' form, all cited | **PASS** | 72 entries; cited 1..72 |
| end-matter order Acknowledgments < References < Supporting information captions; no funding or competing-interest statement in the file | **PASS** | positions [66931, 68363, 83333]; 'NSTC' in file: False; 'competing interest' in file: False |
| package files present | **PASS** | 20/20 |
| MANIFEST.sha256 matches every package file | **PASS** | 122 files |
| figure TIFFs: Figs 1/2/5 RGB 600 dpi within 6.68-19.05 cm; Figs 3/4/S1 from seed-0 diagnostics (PLoS waives format until acceptance) | **PASS** | Fig1 3113x2912@600dpi=13.2cm RGB; Fig2 3088x3475@600dpi=13.1cm RGB; Fig3 990x1980@300dpi=8.4cm RGB; Fig4 1375x1056@300dpi=11.6cm RGB; Fig5 4421x2658@600dpi=18.7cm RGB; S1_Fig 1650x3247@300dpi=14.0cm RGB |
| S1 Data zip present and under the PLoS 20 MB SI limit; manuscript Data availability names S1 Data | **PENDING** | 651 KB; 'S1 Data' in deliverable: False (round 1h) |
| disclosure check (PLoS AI policy) FINAL VERDICT COMPLIANT and bound to the deliverable bytes | **PASS** | 32_DISCLOSURE_plos_v8.md (2026-10-31 20:39); FINAL VERDICT: COMPLIANT — bound to `submission_PLOS_20261031/Manuscript.md` sha256 `8260d; bound True |
| cover letter: Academic Editors chosen by the PI (no 【】 left) | **PENDING** | 1 【 marks |
| CRediT roles for this paper confirmed by the PI | **PENDING** | system fields CRediT block |
| PI opened Manuscript.docx | **PENDING** | 29_PI_SIGNOFF_plos.json absent |
| repository tag pushed | **PENDING** | 29_PI_SIGNOFF_plos.json absent |
| submission-system fields entered | **PENDING** | 29_PI_SIGNOFF_plos.json absent |

**GATE: NOT READY — human items pending** — 27 PASS, 0 FAIL, 7 PENDING
