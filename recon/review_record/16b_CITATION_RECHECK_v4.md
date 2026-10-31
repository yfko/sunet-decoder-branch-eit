# Citation Re-check (scoped) — RECON paper, draft v4

| | |
|---|---|
| Date | 2026-10-31 |
| Mode | ARS 3.23.0 `academic-paper` **citation-check**, strict policy, **scoped** re-check after revision round 1c (follows `16_CITATION_AUDIT_v3.md`) |
| Model | Opus-class (Opus 5.5). Checks (a) and (b) are execution-class; Check (c), claim–source context, is a judgment-class reading, so the PI may want it re-read on Fable |
| Target | `RECON_paper/manuscript/17_DRAFT_v4.md`, sha256 `6379490727ef0fe5a2452a1d10f8e5693c091a0839a333e32f1b57e90aeaeb66` (prefix 6379490727ef, matches the brief and `17_DRAFT_v4.md.apply-report.json` `output_draft_hash`) |
| Base | `15_DRAFT_v3.md`, sha256 `aed5252125fd96c0dfc86c01f3d6689805d7ef89e03bd2775b27e250f628a2b8` |
| Patch | `revision-authority-round1c/revision_patch_round1c.json`: 6 `replace_block` ops (B0010, B0011, B0013, B0014, B0024, B0074) |
| Scope | The six changed blocks only. Strings (Check A), retraction status (Check D), PLoS One citability (F) and orphans (G) are inherited from `16_CITATION_AUDIT_v3.md`, since the reference list is byte-identical (§1) |
| Fresh lookups (2026-10-31) | Crossref REST `api.crossref.org/works/<DOI>` for the 23 DOIs cited in the six blocks; NCBI efetch (PubMed XML) for PMIDs 25110887, 37931580, 33937833, 29356028, 24845059, 33529234; Europe PMC full-text XML of PMC7853495 (Ko and Cheng 2021b); OpenAlex abstract of doi:10.1109/tim.2024.3369160 (Wang 2024, no Crossref abstract). Raw responses kept in the session scratchpad only |
| Files written | This report only. No other file was modified |

---

## Summary

| Check | Result |
|---|---|
| 1. Diff scope | **PASS**: exactly six lines differ between v3 and v4 (lines 35, 38, 44, 47, 77, 227 = B0010, B0011, B0013, B0014, B0024, B0074 in the v4 block manifest); `## References` to end of file is byte-identical (both sha256 `1e06025e8469…`, same line 293) |
| 2a. Key resolution | **PASS**: the 82 ref markers appear in the same key order in v3 and v4, so the first-citation numbering 1–70 is unchanged; every key in the six blocks resolves to the same reference-list entry and the same registry DOI as in v3 |
| 2b. Quote anchors (six blocks) | **PASS**: 24/24 VERIFIED (4 changed, 20 unchanged), 0 NOT FOUND, 0 PARAPHRASE; maximum 16 words |
| 2c. Claim–source context | E1 RESOLVED, E2 RESOLVED, E3 RESOLVED, **E4 PARTIALLY RESOLVED**, E5 RESOLVED, E6 RESOLVED, slip RESOLVED; **1 new flag (N1)**, from the rewrite of the E4 comparison clause |
| 3. Counts | **PASS**: 82 instances, 70 distinct keys, 82 quote anchors; 0 slugs outside corpus; 0 cited-but-unlisted; 0 listed-but-uncited; orphans unchanged (3: Rusak2020ECCV, Zhang2020TMI, Zhang2022PhysiolMeas) |

**Scoped verdict: `citation_check=PASS WITH FLAGS`.** The strict layer still passes: no unresolvable entry, no key or DOI change, no unverifiable anchor, and the reference list is unchanged. Five of the six v3 flags and the 33/34 slip are resolved. E4's numbers are now correct, but the clause that replaced "of that order" makes a new magnitude comparison that does not hold (N1, advisory).

---

## 1. Diff scope (v3 → v4)

`diff 15_DRAFT_v3.md 17_DRAFT_v4.md` prints six changed lines and nothing else:

| Line | Block | Section | Change |
|---|---|---|---|
| 35 | B0010 | 1.1 heading | "Clinical indices are insensitive to the reconstructor; a pixel-level network is not" → "Clinical indices have not been found to depend on the reconstructor; a pixel-level network does" |
| 38 | B0011 | 1.1 | topic clause softened (E6); Grychtol clause and anchor (E5) |
| 44 | B0013 | 1.2 | Ko and Cheng 2021b section and algorithm names (E2) |
| 47 | B0014 | 1.2 | Yu 2024a clause and anchor; "downstream" restricted to the branch tested here (E1) |
| 77 | B0024 | 2.1 | parenthesis "(Section 1.2; Gauss–Newton stands for its linearised Newton–Raphson)" added (E2 alignment) |
| 227 | B0074 | 4.4 | Yan and AlBadawy numbers and anchors (E3, E4); "19 to 33" → "19 to 34" |

The block-id mapping comes from `17_DRAFT_v4.md.block-manifest.json` (160 blocks; the `first_line_excerpt` of each of the six ids matches its v4 line). This agrees with the apply report (6 ops, 154/160 blocks byte-identical). The `## References` section through end of file hashes identically in both versions (`1e06025e846973bc50661b24637e1bc0f891ec5833cac6b4718131e74a49dcfc`).

Only four anchors changed across the whole manuscript. All other 78 (key, anchor) pairs are identical in v3 and v4:

| Key | v3 anchor | v4 anchor |
|---|---|---|
| Grychtol2014PLOSONE | Functional Validation and Comparison Framework for EIT Lung Imaging | clinically relevant parameters do not vary considerably among the advanced algorithms |
| Yu2024CMPB | structure-aware hybrid-fusion learning | enhance the robustness against the measurement noise and modeling errors |
| Yan2020RadiolAI | MRI Manufacturer Shift and Adaptation | Dice reduced from 89.7% |
| AlBadawy2018MedPhys | cross-institutional training and testing | dice coefficients: 0.68 ± 0.19 and 0.59 ± 0.19 |

---

## 2. Anchor table, six changed blocks

Method: each anchor was URL-decoded and searched as an exact substring of the fresh Crossref title (+ subtitle) and abstract, then the PubMed title and abstract (efetch). For Ko2021PLOSONE it was also searched in the PMC7853495 full text. Unicode normalisation was not needed for any of the 24. B0010 (the heading) contains no citation.

| # | Block | Key | DOI | Anchor (decoded) | Words | Result |
|---|---|---|---|---|---|---|
| 1 | B0011 | Frerichs2017TREND | 10.1136/thoraxjnl-2016-208357 | consensus statement of the TRanslational EIT developmeNt stuDy group | 9 | VERIFIED: Crossref title, exact |
| 2 | B0011 | Zhao2014PhysiolMeas | 10.1088/0967-3334/35/6/1083 | No significant differences were found in all examined indices among the four reconstruction algorithms | 14 | VERIFIED: PubMed abstract (PMID 24845059), exact |
| 3 | B0011 | Grychtol2014PLOSONE | 10.1371/journal.pone.0103045 | **clinically relevant parameters do not vary considerably among the advanced algorithms** (changed) | 11 | VERIFIED: PubMed abstract (PMID 25110887), Results and Conclusions, exact |
| 4 | B0011 | Zhou2023TPAMI | 10.1109/tpami.2022.3195549 | Domain Generalization: A Survey | 4 | VERIFIED: Crossref title, exact |
| 5 | B0011 | Yoon2024ProcIEEE | 10.1109/jproc.2024.3507831 | Domain Generalization for Medical Image Analysis: A Review | 8 | VERIFIED: Crossref title, exact |
| 6 | B0013 | Leathard1994PhysiolMeas | 10.1088/0967-3334/15/2a/018 | ventilatory and cardiac related changes in EIT images | 8 | VERIFIED: Crossref title, exact |
| 7 | B0013 | Graf2017PLOSONE | 10.1371/journal.pone.0188313 | highly position dependent | 3 | VERIFIED: Crossref title, exact |
| 8 | B0013 | Ko2021PhysiolMeas | 10.1088/1361-6579/abe021 | U-Net-based approach for automatic lung segmentation | 6 | VERIFIED: Crossref title, exact |
| 9 | B0013 | Ko2021PLOSONE | 10.1371/journal.pone.0246071 | Semi-Siamese U-Net for separation of lung and heart bioimpedance images | 10 | VERIFIED: Crossref and PubMed title (PMID 33529234), exact |
| 10 | B0013 | Ko2025CurrMedImaging | 10.2174/0115734056408077250610070821 | Reconstruction of Heart-related Imaging from Lung Electrical Impedance Tomography | 9 | VERIFIED: Crossref title, exact |
| 11 | B0013 | Ko2021PLOSONE | 10.1371/journal.pone.0246071 | the separation effect of the EIT image obtained by the different reconstruction algorithms will be investigated | 16 | VERIFIED: PMC7853495 full text, section **Discussion** (last paragraph), exact; not in the title or abstract (as in v3) |
| 12 | B0014 | Vandenhende2021 | 10.1109/tpami.2021.3054719 | Multi-Task Learning for Dense Prediction Tasks: A Survey | 8 | VERIFIED: Crossref title, exact |
| 13 | B0014 | Wang2024TIM | 10.1109/tim.2024.3369160 | Dual-Branch U-Net Based on Deformable Convolution and Hyper-Convolution | 8 | VERIFIED: Crossref title, exact |
| 14 | B0014 | Yu2024CMPB | 10.1016/j.cmpb.2023.107861 | **enhance the robustness against the measurement noise and modeling errors** (changed) | 10 | VERIFIED: PubMed abstract (PMID 37931580), Objectives, exact |
| 15 | B0014 | Hamilton2018TMI | 10.1109/tmi.2018.2828303 | Deep D-Bar: Real-Time Electrical Impedance Tomography Imaging | 7 | VERIFIED: Crossref title, exact |
| 16 | B0014 | Herzberg2023PhysiolMeas | 10.1088/1361-6579/ad0b3d | Domain independent post-processing with graph U-nets | 6 | VERIFIED: Crossref title, exact |
| 17 | B0014 | Zhang2022FBB | 10.3389/fbioe.2022.1019531 | Advances of deep learning in electrical impedance tomography image reconstruction | 10 | VERIFIED: Crossref title, exact |
| 18 | B0014 | Denker2025HandbNumerAnal | 10.1016/bs.hna.2025.09.003 | Deep learning based reconstruction methods for electrical impedance tomography | 9 | VERIFIED: Crossref title, exact |
| 19 | B0024 | Adler2009GREIT | 10.1088/0967-3334/30/6/s03 | GREIT: a unified approach to 2D linear EIT reconstruction of lung images | 12 | VERIFIED: Crossref title, exact |
| 20 | B0024 | Adler1996TMI | 10.1109/42.491418 | regularized imaging and contrast detection | 5 | VERIFIED: Crossref title, exact |
| 21 | B0024 | Adler2006EIDORS | 10.1088/0967-3334/27/5/s03 | an extensible software base for EIT | 6 | VERIFIED: Crossref title, exact |
| 22 | B0024 | Thurk2019PhysiolMeas | 10.1088/1361-6579/ab248e | Influence of reconstruction settings | 4 | VERIFIED: Crossref title, exact |
| 23 | B0074 | Yan2020RadiolAI | 10.1148/ryai.2020190195 | **Dice reduced from 89.7%** (changed) | 4 | VERIFIED: PubMed abstract (PMID 33937833), Results, exact |
| 24 | B0074 | AlBadawy2018MedPhys | 10.1002/mp.12752 | **dice coefficients: 0.68 ± 0.19 and 0.59 ± 0.19** (changed) | 9 | VERIFIED: PubMed abstract (PMID 29356028), Results, exact |

The four new anchors move from title phrases to the abstract phrases that carry the claim. That makes each anchor a direct witness for its sentence, which a title phrase could not be.

---

## 3. Claim–source context: E1–E6 and the slip

### E1 — B0014, Yu et al. 2024a (and Wang et al. 2024). **RESOLVED**

v4 sentence: "The branch is a decoder-side branch serving one target each, of the branched multi-task family (Vandenhende et al., 2022), with EIT relatives among reconstructors: a dual-branch reconstructor (Wang et al., 2024) and a multi-branch network that reconstructs conductivity from the measured voltages, its branches fused to resist measurement noise and modelling errors (Yu et al., 2024a). The branch tested here sits downstream of a reconstruction operator, as do the post-processing networks for EIT (Hamilton and Hauptmann, 2018; Herzberg et al., 2023; Zhang et al., 2022b)…"

Source, Yu 2024a (PMID 37931580). Objectives: "This study aims to mine the deep feature information from measurement voltages, acquired from the EIT sensor, to reconstruct the high-resolution conductivity distribution and enhance the robustness against the measurement noise and modeling errors". Methods: the branches "extract different feature information from the measurement voltage, which is then fused to reconstruct the conductivity distribution".

Source, Wang 2024 (OpenAlex abstract): a "two-branch U-Net deep imaging architecture, named DHU-Net, for the accurate and sharp reconstruction of EIT images".

Judgment:
- The v3 contradiction is gone. Yu is now described correctly, as a voltage-to-conductivity network, and the "downstream" claim is limited to "the branch tested here" and the post-processing networks.
- Wang is now placed "among reconstructors" and called a dual-branch reconstructor, which its abstract supports. The sentence no longer says which side of the operator Wang's network sits on, so the v3 "unverified" item for Wang no longer arises.
- Residual note (no flag): "fused to resist measurement noise and modelling errors" gives only one of the two stated aims; the other is high resolution. The Conclusions credit the fusion with accuracy ("fusing feature information from different branches enhances the accuracy"). The wording is supported as a statement of aim. If the author wants it complete: "…its branches fused for resolution and robustness to measurement noise and modelling errors".

### E2 — B0013, Ko and Cheng 2021b (second instance). **RESOLVED**

v4 sentence: "The semi-Siamese study's discussion states that "the separation effect of the EIT image obtained by the different reconstruction algorithms will be investigated" (Ko and Cheng, 2021b), naming the Sheffield back-projection algorithm, a finite-element linearised Newton–Raphson algorithm and GREIT; this paper answers it, with one-step Gauss–Newton as its linearised Newton–Raphson member."

Source (PMC7853495, section titled "Discussion", last paragraph): "…the separation effect of the EIT image obtained by the different reconstruction algorithms will be investigated, notably, Shield back-projection algorithm, FEM-based linearized Newton-Raphson algorithm, and Graz consensus reconstruction algorithm (GREIT)."

Judgment:
- The section is now correctly named.
- The three algorithms are named as the source names them. "FEM-based" becomes "finite-element", and the source's "Shield" becomes "Sheffield". "Shield" is the source's typo, and the draft paraphrases rather than quotes, so the correction is appropriate.
- The Gauss–Newton mapping is now explicitly the authors' own ("with one-step Gauss–Newton as its linearised Newton–Raphson member"), not attributed to the source.
- Observation (no flag, unchanged since v3): in the source, the same sentence starts by saying the network "will be further applied to real human EIT data". The draft quotes only the algorithm clause and this paper is a simulation study, so "this paper answers it" is accurate for the quoted clause.

**B0024 consistency with B0013. CONSISTENT.** B0024 reads: "The three reconstructors are those the original study named (Section 1.2; Gauss–Newton stands for its linearised Newton–Raphson), each at one fixed setting…".
- B0013 is in Section 1.2 (heading at line 41, B0013 at line 44), so the cross-reference is correct.
- "stands for its linearised Newton–Raphson" matches B0013's "as its linearised Newton–Raphson member".
- The rest of B0024 matches B0013's names: BP is the "Sheffield back-projection matrix distributed with EIDORS", and GREIT is named.

### E3 — B0074, Yan et al. 2020. **RESOLVED**

v4 sentence: "The nearest clinical analogues are a left-ventricle segmentation network that fell by 21 to 31 Dice points, from 0.89–0.91 to 0.60–0.69, when the MRI manufacturer changed (Yan et al., 2020)…"

Source (PMID 33937833, Results): "Dice reduced from 89.7% ± 2.3 [standard deviation] to 68.7% ± 10.8, P < .05, from 90.6% ± 2.1 to 59.5% ± 13.3, P < .05, from 89.2% ± 2.3 to 64.1% ± 12.0, P < .05, for manufacturer 1, 2, and 3, respectively".

Arithmetic:
- Losses: 89.7 − 68.7 = 21.0, 90.6 − 59.5 = 31.1, 89.2 − 64.1 = 25.1. This gives "21 to 31 points".
- Baselines 0.892–0.906 round to "0.89–0.91". Shifted values 0.595–0.687 round to "0.60–0.69".

Every number is now reported in or derived from the source, and the v3 pair 0.89 → 0.60, which was not in the source, is gone.

Residual note (no flag, pre-existing): the source trained three CNNs, one per manufacturer, while the draft says "a … network". Optional: "left-ventricle segmentation networks that fell…".

### E4 — B0074, AlBadawy et al. 2018 and the magnitude comparison. **PARTIALLY RESOLVED**

v4 sentence: "…and cross-institutional tumour segmentation that lost 4 and 17 points, from 0.72 and 0.76 to 0.68 and 0.59 (AlBadawy et al., 2018); the 16 to 62 points lost here and the exploratory 19 to 34 points start where that range ends, but two differences forbid a comparison of magnitudes: …"

Source (PMID 29356028, Results): "Performance of the model significantly decreased (P < 0.0001) when it was trained on data from a different institution (dice coefficients: 0.68 ± 0.19 and 0.59 ± 0.19) as compared to training with data from the same institution (dice coefficients: 0.72 ± 0.17 and 0.76 ± 0.12)."

Judgment:
- **Resolved part.** Levels and losses are now separated. Pairing the two lists in the order the abstract gives them, 0.72 → 0.68 and 0.76 → 0.59, gives losses of 4 and 17 points, as stated. The abstract does not label the pairs, so pairing by order is the reading the v3 audit used and is reasonable.
- **Not resolved: the comparison clause, recorded as N1 below.** It replaces "are of that order" with "start where that range ends". The new wording is still a magnitude comparison, it is not accurate, and it still sits beside "forbid a comparison of magnitudes".

### E5 — B0011, Grychtol et al. 2014a. **RESOLVED**

v4 clause: "…and twelve reconstructions differed in appearance by amounts that were not negligible while the clinical parameters derived from them did not vary considerably among the advanced algorithms (Grychtol et al., 2014a)."

Source (PMID 25110887, Results and Conclusions): "while variation in appearance of images reconstructed from the same data is not negligible, clinically relevant parameters do not vary considerably among the advanced algorithms. Among the analysed algorithms, several advanced algorithms perform well, while some others are significantly worse."

The source's restriction is restored word for word, and the anchor is now that phrase. "Twelve" matches "compare twelve 2D EIT reconstruction algorithms" (Methods).

### E6 — B0011 topic clause and 1.1 heading. **RESOLVED**

v4 heading: "### 1.1 Clinical indices have not been found to depend on the reconstructor; a pixel-level network does".

v4 topic clause: "Where reconstructors were compared, those indices did not depend detectably on which linear reconstructor produced the image: four algorithms applied to the same recordings gave five ventilation indices none of which differed significantly between algorithms (p > 0.2, Kruskal–Wallis) (Zhao et al., 2014)…".

Source, Zhao 2014 (PMID 24845059): "No significant differences were found in all examined indices among the four reconstruction algorithms (p > 0.2, Kruskal-Wallis test)".

Judgment:
- Both the heading and the topic clause now report an absence of detected dependence ("have not been found", "did not depend detectably"), not an equivalence. This is consistent with B0069 (line 212): "Non-significance cannot establish equivalence; a margin can (Lakens, 2017)".
- The v3 audit's suggested wording ("were not detectably affected by") has been followed in substance.
- Residual note (no flag): the topic clause covers both Zhao and Grychtol, but Grychtol's abstract also says "some others are significantly worse". "Where reconstructors were compared" plus the "advanced algorithms" restriction in the Grychtol clause keeps the paragraph accurate. If the author wants the topic clause airtight, append "…at least among the advanced algorithms" or keep the topic clause as Zhao's alone.

### Slip — "19 to 33" → "19 to 34" (B0074). **RESOLVED**

"19 to 34" now appears in all five places: the abstract (B0006, line 23), lines 158 (twice), 203, 215 and 227. I recomputed it from the tables: E1 Dice in Table 2 against the diagonal Dice in Table 1 (GREIT 0.9575 / 0.9602, GN 0.9639 / 0.9672, BP 0.9565 / 0.9628, B_wide / D). The smallest loss is BP → GN B_wide (0.9565 − 0.767 = 18.95) and the largest is GN → BP D (0.9672 − 0.629 = 33.8), so the range is 19 to 34. v3's "33" was a rounding slip.

---

## 4. New flag introduced by the rewrite

**N1 — B0074, the analogue comparison clause. FLAG (advisory): the comparison is inaccurate and conflicts with its own sentence.**

v4 text: "…the 16 to 62 points lost here and the exploratory 19 to 34 points start where that range ends, but two differences forbid a comparison of magnitudes…"

Finding:
- Across the two analogues the losses span 4 to 31 points: AlBadawy 4 and 17, Yan 21 to 31. This study's 16 to 62 points start inside that span, at 16 rather than at 31.
- The exploratory 19 to 34 points almost contain Yan's 21 to 31 entirely.
- The clause holds only if "that range" means AlBadawy's 4 to 17 alone. Grammatically that is the nearest antecedent, but a reader who has just read Yan's 21 to 31 points will not take it that way.
- The clause also ranks magnitudes in the same sentence that says magnitudes cannot be compared, which is the tension E4 raised in v3.
- The cited numbers themselves are correct. The flag is about the authors' comparison, not a citation error.

Fix (author's choice), either of:
- "…the 16 to 62 points lost here and the exploratory 19 to 34 points overlap the upper part of the 4 to 31 points lost there and extend beyond it, but two differences forbid a comparison of magnitudes: …"
- Drop the ranking: "…the 16 to 62 points lost here (19 to 34 exploratory) are losses of the same kind, but two differences forbid a comparison of magnitudes: …"

The 4.4 heading ("The held-out losses resemble those of multi-source studies, and are not directly comparable to them") fits either fix.

No other new claim–source issue was found in the six blocks:
- B0010: heading only.
- B0011: the "Where reconstructors were compared" hedge is supported.
- B0013: names verified against the full text.
- B0014: "among reconstructors" is supported for both Wang and Yu.
- B0024: cross-reference verified.

---

## 5. Counts (`tools/check_recon_draft.py`)

`python3 -X utf8 tools/check_recon_draft.py RECON_paper/manuscript/17_DRAFT_v4.md`, citation block:

```
== citations ==
  instances: 82; distinct: 70; anchors: {'quote': 82}
  slugs outside corpus: []
  corpus entries never cited (orphans, 3): ['Rusak2020ECCV', 'Zhang2020TMI', 'Zhang2022PhysiolMeas']
  reference-list entries: 70; cited-but-unlisted: []; listed-but-uncited: []
```

This is identical to the same script on v3: 82 / 70 / 82 quote anchors, the same 3 orphans, 0 dangling keys. Instances in the six blocks: B0010 0, B0011 5, B0013 6, B0014 7, B0024 4, B0074 2, total 24, the same as in v3.

Outside citation scope, for the PI: the same script reports total main text **7,996 words against the 8,000 ceiling** (v3 7,925; the round added 71 words, 47 of them in Section 1, now 1,171 / 950, +23%). The ceiling has 4 words of headroom, so any N1 fix should not lengthen the sentence.

---

## 6. Items carried from the v3 audit, not in this scope

- m4 (B0014, Denker 2025): the post-UNet vs Deep D-bar statement still needs checking in the Elsevier chapter (pp 127–175). The sentence did not change in v4.
- m9 (B0013, Leathard 1994): no action required. Unchanged.
- The other minor items m1–m3, m5–m8 and m10–m13 are in blocks this round did not touch. They stay open as listed in `16_CITATION_AUDIT_v3.md` §5.
- Action 13 of that audit still applies: immediately before submission, re-run `tools/cite.py` + `apply_ref_overrides.py` for a fresh retraction check.

---

## 7. Verdict

| Item | Verdict |
|---|---|
| E1 (Yu 2024a / Wang 2024, B0014) | RESOLVED |
| E2 (Ko and Cheng 2021b, B0013; B0024 aligned) | RESOLVED |
| E3 (Yan 2020, B0074) | RESOLVED |
| E4 (AlBadawy 2018 and comparison, B0074) | PARTIALLY RESOLVED (numbers fixed; comparison clause → N1) |
| E5 (Grychtol 2014a, B0011) | RESOLVED |
| E6 (1.1 heading and B0011 topic clause) | RESOLVED |
| Slip 19 to 33 → 19 to 34 | RESOLVED (consistent in 5 places; recomputed from Tables 1–2) |
| New flags | 1: N1 (B0074 "start where that range ends") |

Strict layer: unresolvable 0; key or DOI change 0; anchors 24/24 VERIFIED in scope (82/82 overall, 78 unchanged pairs carried); reference list byte-identical; retraction status inherited.

`citation_check=PASS WITH FLAGS` (scoped, v4 `6379490727ef`)
