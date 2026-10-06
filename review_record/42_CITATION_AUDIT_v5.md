# Citation audit v5 — `41_DRAFT_v5.md` (academic-paper citation-check, delta audit, 2026-10-07, Fable 5.1)

**Draft**: `manuscript/41_DRAFT_v5.md`, produced from `34_DRAFT_v4.md` by `phase6_revision/revision_patch_round4.json` (apply report: witness PASS, 11 of 127 blocks replaced, 116 byte-identical, touched ratio 0.087). **Deliverable**: `manuscript/43_SUBMISSION_scirep_v5.md` (+ `.docx`). **Registry**: `refs/prior_works.json` (54 keys) with `refs/overrides.json` (10 entries; three added 2026-10-07) and `refs/prior_works_strings.md` (Nature section). **Previous full audit**: `35_CITATION_AUDIT_v4.md`. **Scope**: existence/retraction of the 54 entries is NOT re-verified here (strict pass recorded in 35_ from `tools/cite.py`, Crossref + PubMed, `refs/prior_works_table.md`); the mechanical checks were re-run on the whole v5 draft; the claim-faithfulness check is limited to the 11 changed blocks.

## 0. Verdict

**PASS — no blocker.** 0 dangling, 0 orphan, 0 altered citation sentences, 0 numbering defects in the deliverable, 3 overrides render as intended. Two non-blocking rendering observations carried to the PI (§3.4): a non-breaking-space pair inside the Isensee 2024 title (inherited from Crossref, also present in v4 and in the v5 .docx), and the Wilcoxon 1945 page field held as a single number (`80`) so that it renders in the article-number form with a DOI.

| Metric | v5 | v4 (35_) |
|---|---|---|
| Reference entries (registry keys) | 54 | 54 |
| In-text `<!--ref:-->` instances | 67 | 67 |
| Distinct slugs cited | 54 | 54 |
| Dangling slugs (in text, not in registry) | 0 | 0 |
| Orphan references (in registry, not cited) | 0 | 0 |
| Self-citation (Ko2021PhysiolMeas, Ko2021PLOSONE, Ko2025CurrMedImaging) | 3/54 = 5.6% | 5.6% |
| Anchors | 67 (55 `none`, 12 `quote`) | 67 (55/12) |
| Sources 2022–2025 | 13/54 = 24% | — |
| Sources older than 10 years (<2016) | 19/54 = 35% (Wilcoxon 1945, Caruana 1997, Adler 1996, Eyuboglu 1988, Zadehkoochak 1992, Leathard 1994 etc.: seminal or EIT-foundational) | — |
| Changed blocks carrying citations | 2 of 11 (B0028, B0056) | — |
| Citation sentences altered in those blocks | 0 of 4 | — |
| Deliverable list entries / numbering | 54, numbered 1–54, first-appearance order, no gaps or duplicates | same |
| Deliverable in-text brackets | 66 instances, 67 numbers, 54 distinct | 66 / 54 |
| Format defects, blocking | 0 | — |
| Format observations, non-blocking | 2 (§3.4) | 4 carried (3 now resolved by overrides, Pulletz moot under `et al.`) |

## 1. Mechanical (whole v5 draft)

Method: regex over `41_DRAFT_v5.md` for `<!--ref:SLUG-->` against the `key` field of `refs/prior_works.json`.

| Check | Result |
|---|---|
| Every `<!--ref:SLUG-->` resolves to a registry key | 67/67 — dangling: none |
| Every registry key cited at least once | 54/54 — orphans: none |
| Most-cited | Ko2021PLOSONE ×3, Wang2024TIM ×3; ten slugs ×2; the rest ×1 |
| Self-citation ratio | 3/54 = 5.6% (threshold 15%) |
| Reference count stated in text | "fifty-four" ×2 (B0060, B0070) — now equals the registry count; v4 still said "fifty-three" after Frerichs 2002 was added, so this round corrected a stale count |

## 2. Delta — the 11 replaced blocks

Source of truth for "what changed": `diff 34_DRAFT_v4.md 41_DRAFT_v5.md` (11 differing lines, one per block; anchors stripped before comparison). Sentence-level comparison was done for the two blocks that carry citations.

| Block | Line | Citations in block | Sentence carrying the citation changed? | What changed in the block |
|---|---|---|---|---|
| B0013 | 50 | none | — | §1: companion conditions spelled out ("other reconstructors and noise models, the weighted loss …, measured data") instead of "named in Section 4.4" |
| B0028 | 95 | Wilcoxon1945; Lakens2013EffectSize | **No** — both sentences byte-identical to v4 | One sentence inserted before the Lakens sentence: Bonferroni reference value for the seven-level onset (35 dB, p = 0.0011 < 0.05/7) |
| B0034 | 113 | none | — | two more unregistered analyses listed (D vs B at 40 dB; per-seed slope 40→20 dB) |
| B0037 | 137 | none | — | D vs B at 40 dB labelled descriptive; "shrinks by only 0.03" corrected to "grows by 0.03 points, to +0.223" |
| B0122 | 179 | none | — | one sentence added: shrinkage Δ_20|20 vs Δ_20|40 does not depend on the floor |
| B0127 | 158 | none | — | Table S9 provenance; CI values re-stated from the per-seed files; closing clause reworded |
| B0051 | 197 | none | — | "prediction does not hold" → "condition of this prediction is absent …, so the prediction is not tested there" |
| B0056 | 212 | Gagnon2010TBME; Kamann2021IJCV + Boone2023NeuroImage | **No** — both sentences byte-identical to v4 | one earlier sentence reworded: "attributed to the branch what belongs mostly to the training condition" → "a benefit that did not survive training at the heavier level" |
| B0060 | 224 | none | — | fifty-three → fifty-four |
| B0070 | 254 | none | — | fifty-three → fifty-four |
| B0072 | 260 | none | — | checkpoints: reason for non-deposit added |

### 2.1 Attribution check for the five sources inside changed blocks

Even though the citation sentences did not change, the adjacent edits were read against what the registry records for each source (`why` field, written at corpus entry; 35_ §3 listed these as "unchanged attributions" without a per-source line).

| Source | Sentence in v5 attributes | Registry `why` (verbatim) | Adjacent edit alters the attribution? |
|---|---|---|---|
| Wilcoxon 1945 | the signed-rank test used in the H1 rule | "C8a Methods 2.4：Wilcoxon signed-rank，註冊判定規則的檢定（seminal，1945）" | No. The inserted Bonferroni sentence cites nothing and makes no claim about Wilcoxon. |
| Lakens 2013 | Cohen's dz for paired differences | "C8b Methods 2.4：配對設計的 Cohen's dz 定義與報告" | No. |
| Gagnon et al. 2010 | SNR of an EIT system depends on frame rate, frequency, current and measurement strategy; performance figures should be reported with those parameters | "L4 §4.2、§2.4：EIT 系統 SNR 取決於操作條件，報告效能指標時須一併註明" | No. The reworded sentence precedes "The lesson has precedents…" and concerns this study's own addendum, not the source. |
| Kamann and Rother 2021 | corruption tolerance differs between architectures and depends on corruption type | "L4 §1 第四段、§4.2：…架構差異在干擾下才顯現且取決於干擾類型" | No. |
| Boone et al. 2023 | MRI segmentation networks highly sensitive to simulated distribution shifts incl. SNR | "L4 §1 第四段、§4.2：ROOD-MRI，醫學影像分割網路在受控 SNR 偏移與干擾下的基準" | No. |

**Finding**: the expectation stated in the task holds. No sentence carrying a citation was altered in round 4; the only edits near a citation are (a) one new citation-free sentence inserted into B0028 and (b) one reworded citation-free sentence earlier in B0056. The 9 other replaced blocks contain no citation. The 116 untouched blocks are byte-identical to v4 (apply report), so the 35_ attribution findings for the remaining 49 sources carry over unchanged.

## 3. Rendering — `43_SUBMISSION_scirep_v5.md` (Nature style, Sci Rep)

### 3.1 List structure

| Check | Result |
|---|---|
| Entries in `## References` | 54 |
| Numbered 1–54, no gap, no duplicate | Yes |
| Order = first appearance in text | Yes (first-appearance sequence of bracket numbers equals 1…54) |
| In-text bracket instances / numbers / distinct | 66 / 67 / 54 (one multi-cite `[36, 37]`-type instance), max 54 |
| Each entry matched to exactly one registry key by full title | 54/54 |

### 3.2 DOI, volume, pages

The journal's recorded rule (`refs/01_JOURNAL_REQUIREMENTS_SCIREP.md` §參考文獻格式, verified 2026-10-06) and the renderer (`tools/cite.py::render_nature`) put a DOI only on online-only journal items — article number followed by `; DOI` — and no DOI on page-range articles, proceedings or chapters ("We don't copy edit your references").

| Check | Result |
|---|---|
| Journal entries with an article number (single-token page field) | 18 — all 18 carry `; DOI` (entries 2, 5, 13, 15, 17, 18, 19, 20, 21, 24, 26, 37, 42, 43, 45, 46, 47, 52) |
| DOI string equals registry `doi` | 18/18 |
| Page-range journal entries carrying a DOI (would be off-style) | 0 |
| Proceedings/chapters carrying a DOI (would be off-style) | 0 |
| Volume present where the registry has one | 54/54 (bold) |
| Pages present where the registry has them | 54/54 (en dash ranges) |
| Entries listing ≥6 authors without `et al.` | 0 |
| Entries with `et al.` whose registry author count is <6 | 0 (19 `et al.` entries, all ≥6) |
| Stray punctuation (`..`, `,.`, ` ,`, `()`, double space, trailing `.` after DOI) | none found |
| v4 → v5 difference in the DOI-bearing set | +1: entry 46 Lakens (pages `''` → `863` by override makes it an article-number item and the DOI is now printed, as intended) |

### 3.3 The three overrides added 2026-10-07

| Entry | Rendered in 43_ | Intended | OK |
|---|---|---|---|
| 46 Lakens 2013 | `*Front. Psychol.* **4**, 863; 10.3389/fpsyg.2013.00863 (2013).` | article number 863 (+ DOI per online-only rule) | ✔ |
| 44 Ronneberger 2015 | `In *Lecture Notes in Computer Science* **9351**, 234–241 (2015).` | volume 9351, pages 234–241 | ✔ (same container form as the other three LNCS chapters, entries 35, 49, 54) |
| 24 Herzberg 2023 | `… applications to electrical impedance tomographic imaging. *Physiol. Meas.* **44**, 125008; 10.1088/1361-6579/ad0b3d (2023).` | title without trailing ⋆ | ✔ |
| 30 Vandenhende 2020 (re-verified order) | `Vandenhende, S., Georgoulis, S., Van Gool, L. & De Brabandere, B. … In *Proceedings of the British Machine Vision Conference 2020* 59 (2020).` | BMVC accepted-papers order | ✔ — closes 35_ §4 item 1 |

35_ §4 item 2 (Pulletz given-name form) is moot in Nature style: entry 9 prints `Pulletz, S. et al.` only.

### 3.4 Remaining observations (non-blocking, for the PI)

| # | Entry | Observation | Suggested handling |
|---|---|---|---|
| 1 | 35 Isensee et al. 2024 | Title contains two U+00A0 non-breaking spaces ("A Call for Rigorous Validation in 3D"), inherited from the Crossref title into `prior_works.json`; present in 36_ (v4) too, and carried into `43_SUBMISSION_scirep_v5.docx` (`word/document.xml`). Renders as ordinary spaces on screen; could affect line-breaking in the typeset proof. | Add a sourced `title` override (Springer chapter page) replacing NBSP with space, or normalise ` ` → space in `cite.py` title handling; then re-run format-convert. Cosmetic. |
| 2 | 45 Wilcoxon 1945 | Registry `pages` = `80` (Crossref first-page only); the printed article occupies pp. 80–83 of *Biometrics Bulletin* 1(6). Because the field is a single token the renderer treats it as online-only and prints `**1**, 80; 10.2307/3001968 (1945)`. The DOI resolves; the page field is incomplete rather than wrong. Range not re-verified online in this audit. | If the PI wants the range: sourced override `pages: "80-83"` (JSTOR record) → renders as `**1**, 80–83 (1945)` without DOI. Optional. |
| 3 | 30 Vandenhende 2020 | `… Conference 2020* 59 (2020).` — "59" is the BMVC paper number, printed where a page range would go; no DOI because the renderer gives none to proceedings. Carried from v4; acceptable under the journal's no-copy-edit rule. | Leave, or override `pages` to "paper 59" if preferred. Optional. |

None of the three affects existence, attribution, numbering or the in-text ↔ list correspondence.

## 4. Not re-run in this delta audit (state recorded in 35_)

- Existence and retraction of all 54 entries (strict pass, `tools/cite.py` 2026-10-06 23:19; `refs/prior_works_table.md`).
- Claim faithfulness of the 49 sources whose sentences are in the 116 byte-identical blocks (35_ §3 and earlier audits).
- `tools/check_draft.py` watch-term scan (not a citation check).

## 5. Conclusion

Round 4 touched no citation sentence. Mechanical correspondence is intact both ways (67 uses, 54 slugs, 0/0 orphans), self-citation 5.6%, the deliverable's Nature list is complete and in first-appearance order with every style-required DOI present, and the three 2026-10-07 overrides render as intended. Two cosmetic registry items (NBSP in Isensee title; Wilcoxon single-page field) go to the PI; neither blocks submission. Next citation-check: after the next major change, as R12 requires.
