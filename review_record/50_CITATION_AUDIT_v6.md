# Citation audit v6 — `49_DRAFT_v6.md` (academic-paper citation-check, delta audit, 2026-10-08, Fable 5.1)

**Draft**: `manuscript/49_DRAFT_v6.md` (sha256 `88e888906638…`), produced from `41_DRAFT_v5.md` (sha256 `3c0451dfbfd5…`) by `phase6_revision/revision_patch_round5.json` (3 `replace_block` ops: B0127, B0028, B0066; apply report `49_DRAFT_v6.md.apply-report.json`: witness PASS, 3 of 127 blocks replaced, 124 byte-identical, touched ratio 0.0236). **Deliverable**: `manuscript/51_SUBMISSION_scirep_v6.md` (sha256 `7cfc209292ef…`) + `51_SUBMISSION_scirep_v6.docx`; previous deliverable `43_SUBMISSION_scirep_v5.md` used for the diff. **Registry**: `refs/prior_works.json` (54 keys; `refs/refs_in.json` 54 entries) with `refs/overrides.json` (10 entries, unchanged since 2026-10-07) and `refs/prior_works_strings.md` (Nature section). **Previous audit**: `42_CITATION_AUDIT_v5.md` (baseline for every metric below). **Scope**: existence/retraction of the 54 entries is NOT re-verified here (strict pass recorded in `35_` from `tools/cite.py`, Crossref + PubMed, `refs/prior_works_table.md`; no re-fetch in this round); the mechanical checks were re-run on the whole v6 draft and on both deliverables; the sentence-level comparison is limited to the 3 changed blocks.

## 0. Verdict

**PASS — no blocker.** 0 dangling, 0 orphan, 0 markers moved/dropped/duplicated, 0 numbering defects in the deliverable, reference list byte-identical to v5, 3 overrides render as intended. One citation-carrying sentence (Lakens 2013, B0028) was edited this round, but only in the clause after the marker (the intended Table S9 resample-count edit); the attribution clause and the marker are byte-identical to v5. One of the two non-blocking observations carried from `42_` §3.4 (Isensee NBSP) no longer reproduces in the deliverable md or docx; the other (Wilcoxon single-page field) is unchanged and still non-blocking.

| Metric | v6 | v5 (42_) |
|---|---|---|
| Reference entries (registry keys) | 54 | 54 |
| In-text `<!--ref:-->` instances | 67 | 67 |
| Distinct slugs cited | 54 | 54 |
| Dangling slugs (in text, not in registry) | 0 | 0 |
| Orphan references (in registry, not cited) | 0 | 0 |
| Self-citation (Ko2021PhysiolMeas, Ko2021PLOSONE, Ko2025CurrMedImaging) | 3/54 = 5.6% (carried; list unchanged) | 5.6% |
| Anchors | 67 (55 `none`, 12 `quote`) | 67 (55/12) |
| Sources 2022–2025 | 13/54 = 24% (carried; list unchanged) | 24% |
| Sources older than 10 years (<2016) | 19/54 = 35% (carried; list unchanged) | 35% |
| Changed blocks carrying citations | 1 of 3 (B0028: Wilcoxon1945, Lakens2013EffectSize) | 2 of 11 |
| Citation sentences altered in those blocks | 1 of 2 (Lakens sentence: post-marker clause only, intended edit; attribution clause byte-identical) | 0 of 4 |
| Markers moved / dropped / duplicated | 0 | 0 |
| Deliverable list entries / numbering | 54, numbered 1–54, first-appearance order, no gaps or duplicates | same |
| Deliverable in-text brackets | 66 instances, 67 numbers, 54 distinct, max 54 | 66 / 67 / 54 |
| Deliverable reference list vs previous deliverable | byte-identical to `43_` | — |
| Deliverable paragraphs differing from `43_` | 3 (lines 70, 100, 120 = B0028, B0066, B0127); none in `## References` | 11 |
| Format defects, blocking | 0 | 0 |
| Format observations, non-blocking | 1 still open (Wilcoxon), 1 no longer reproduces in the deliverable (Isensee NBSP), 1 unchanged optional (Vandenhende paper number) | 2 + 1 optional |

## 1. Mechanical (whole v6 draft)

Method: regex over `49_DRAFT_v6.md` for `<!--ref:SLUG-->` and `<!--anchor:KIND:…-->` against the `key` field of `refs/prior_works.json`; the same pass was re-run on `41_DRAFT_v5.md` to confirm the baseline.

| Check | v6 | v5 (re-run) |
|---|---|---|
| Every `<!--ref:SLUG-->` resolves to a registry key | 67/67 — dangling: none | 67/67 |
| Every registry key cited at least once | 54/54 — orphans: none | 54/54 |
| Anchors | 67 (55 `none`, 12 `quote`) | 67 (55/12) |
| Most-cited | Ko2021PLOSONE ×3, Wang2024TIM ×3; Nguyen2012PhysiolMeas ×2, Borges2012JAP ×2 … | identical |
| Self-citation ratio | 3/54 = 5.6% (threshold 15%) | 5.6% |
| Draft line count | 428 | 428 |
| Lines differing v5 → v6 (`diff`) | 3 (lines 95, 158, 242) | — |

The two censuses are identical in every count, as expected for a round that touched no marker.

## 2. Delta — the 3 replaced blocks

Source of truth for "what changed": `diff 41_DRAFT_v5.md 49_DRAFT_v6.md` (3 differing lines, one per block) cross-checked against `41_DRAFT_v5.md.block-manifest.json` (block ids and `old_hash` for lines 95 = B0028 `27761b6615ec`, 158 = B0127 `59ceb1f711f9`, 242 = B0066 `68ecfd66a8a6`, matching the patch's `old_hash` fields). The other 124 blocks are byte-identical (apply report `blocks_preserved_byte_identical: 124`; confirmed by the line diff, which shows no other difference). Sentence-level comparison (split on sentence punctuation) was done for all three lines; the marker sequence `<!--ref:…--><!--anchor:…-->` was extracted from each line in v5 and v6 and compared in order.

| Block | Line | Citations in block | Marker sequence v5 = v6? | Sentence carrying the citation changed? | What changed in the block |
|---|---|---|---|---|---|
| B0028 | 95 | Wilcoxon1945; Lakens2013EffectSize | **Yes** (2 markers, same order, same anchors `none`) | Wilcoxon sentence: **No** (byte-identical). Lakens sentence: **Yes, after the marker only** — see §2.1 | REV-R5-2: the closing clause now distinguishes 100,000 resamples (main contrasts) from 20,000 (Table S9 and the §3.2 width contrasts), naming `tools/make_table_s9.py` |
| B0127 | 158 | none | Yes (0 = 0) | — | REV-R5-1: ASCII hyphen-minus → U+2212 minus sign before negative Dice values and CI bounds (glyphs only; no number changed) |
| B0066 | 242 | none | Yes (0 = 0) | — | REV-R5-3: AI-use statement — "Fable 5.1 and Opus 5, accessed September 2026" → "Fable 5.1, Opus 5 and Opus 5.5, accessed August to October 2026" |

### 2.1 The one altered citation sentence (B0028, Lakens 2013)

v5: `Effect sizes are reported as Cohen's dz for paired differences (Lakens, 2013) <!--ref:Lakens2013EffectSize--><!--anchor:none:-->, and all bootstrap intervals use 100,000 resamples of the 58 seeds.`

v6: `Effect sizes are reported as Cohen's dz for paired differences (Lakens, 2013) <!--ref:Lakens2013EffectSize--><!--anchor:none:-->, and the bootstrap intervals use 100,000 resamples of the 58 seeds, except those of Table S9 and of the width contrasts in Section 3.2 drawn from it, which use 20,000 (\`tools/make_table_s9.py\`).`

- Everything up to and including the marker pair is byte-identical. The change is confined to the second, citation-free clause ("and all bootstrap intervals use…" → "and the bootstrap intervals use…, except those of Table S9…, which use 20,000 (…)"), which is the edit the patch authorises (REV-R5-2).
- The attribution to Lakens (Cohen's dz for paired differences) is unchanged and matches the registry `why` ("C8b Methods 2.4：配對設計的 Cohen's dz 定義與報告"). The bootstrap clause was already a separate clause in v5 and was never attributed to Lakens; the edit does not move that boundary.
- The Wilcoxon sentence (H1 rule) is byte-identical to v5; the registry `why` for Wilcoxon1945 is unaffected.

**Finding**: round 5 moved, dropped and duplicated no marker or anchor. The only citation-carrying sentence touched is the Lakens sentence, and only in its post-marker clause, exactly as the task expected. B0127 and B0066 carry no citation. The 124 untouched blocks are byte-identical, so the `35_`/`42_` attribution findings for all 54 sources carry over unchanged.

### 2.2 The `tools/make_table_s9.py` mention (check 5)

- In the draft (line 95, B0028) and in B0127 (line 158, already present in v5) the path appears only in backticks; it carries no `<!--ref:-->` marker, matches no registry key, and does not appear in `refs/prior_works.json` or `refs/refs_in.json` (0 hits). It is a code/path mention, not a citation, and needs no list entry.
- Deliverable md `51_`: rendered as a code span (`` `tools/make_table_s9.py` ``) — 2 occurrences (line 70 = §2.4, line 120 = §3.2); `43_` had 1 (§3.2 only). No `<!--ref:` or `<!--anchor` residue in `51_`.
- Deliverable docx `51_…v6.docx`: `tools/make_table_s9.py` present 2× in `word/document.xml` (1× in the v5 docx), the §2.4 occurrence in a run styled `VerbatimChar` (Pandoc's code-span style); the surrounding text "which use 20,000" is present.

## 3. Rendering — `51_SUBMISSION_scirep_v6.md` (Nature style, Sci Rep)

### 3.1 List structure

| Check | v6 | v5 (43_, re-run) |
|---|---|---|
| Entries in `## References` | 54 | 54 |
| Numbered 1–54, no gap, no duplicate | Yes | Yes |
| Order = first appearance in text | Yes (first-appearance sequence of bracket numbers equals 1…54) | Yes |
| In-text bracket instances / numbers / distinct / max | 66 / 67 / 54 / 54 | 66 / 67 / 54 / 54 |
| Each entry matched to exactly one registry key by title | 54/54 (a 60-character title-prefix heuristic flagged five multi-task entries as double hits because Caruana 1997's short title "Multitask Learning" is a substring of theirs; each of the five has exactly one true match: 28 Vandenhende2021, 29 Misra2016CrossStitch, 31 Kendall2018, 32 Liu2019MTAN, 33 Kurin2022Unitary) | 54/54 |
| `## References` section byte-identical to `43_` | **Yes** | — |
| Paragraphs differing from `43_` (whole file `diff`) | 3: line 70 (§2.4, B0028), line 100 (AI-use statement, B0066), line 120 (§3.2, B0127). Nothing else; nothing in the reference list. | — |

### 3.2 DOI, volume, pages (re-counted; list unchanged)

| Check | Result |
|---|---|
| Journal entries with an article number carrying `; DOI` | 18 (entries 2, 5, 13, 15, 17, 18, 19, 20, 21, 24, 26, 37, 42, 43, 45, 46, 47, 52) — same set as v5 |
| Entries with `et al.` | 19 — same as v5 (all ≥6 authors per `42_` §3.2) |
| Stray punctuation (`..`, `,.`, ` ,`, `()`, double space) | none found |
| `⋆` glyph anywhere in `51_` | 0 |
| U+00A0 anywhere in `51_` | 0 |
| docx: `; 10.` DOI count / `(YYYY).` entry terminators in the References section / `et al.` | 18 / 54 / 19 — same as the v5 docx |

### 3.3 The three overrides (and Vandenhende order)

| Entry | Rendered in 51_ (md) | In 51_ docx | Intended | OK |
|---|---|---|---|---|
| 46 Lakens 2013 | `*Front. Psychol.* **4**, 863; 10.3389/fpsyg.2013.00863 (2013).` | `4, 863; 10.3389/fpsyg.2013.00863 (2013)` present | article number 863 (+ DOI per online-only rule) | ✔ |
| 44 Ronneberger 2015 | `In *Lecture Notes in Computer Science* **9351**, 234–241 (2015).` | `9351, 234–241 (2015)` present | volume 9351, pages 234–241 | ✔ |
| 24 Herzberg 2023 | `… applications to electrical impedance tomographic imaging. *Physiol. Meas.* **44**, 125008; 10.1088/1361-6579/ad0b3d (2023).` | title without ⋆ present; `⋆` count in docx = 0 | title without trailing ⋆ | ✔ |
| 30 Vandenhende 2020 | `Vandenhende, S., Georgoulis, S., Van Gool, L. & De Brabandere, B. Branched Multi-Task Networks: … *Proceedings of the British Machine Vision Conference 2020* 59 (2020).` | same author order present (after `&amp;` unescaping) | BMVC accepted-papers order | ✔ unchanged |

`refs/overrides.json` (mtime 2026-10-07 00:48) still lists the 10 keys recorded in `42_`, including `Lakens2013EffectSize {pages: 863}`, `Ronneberger2015UNet {volume: 9351}`, `Herzberg2023PhysiolMeas {title: …}`, `Vandenhende2020Branched {authors: …}`.

### 3.4 Observations carried from `42_` §3.4 (non-blocking)

| # | Entry | 42_ observation | State in v6 | Still non-blocking? |
|---|---|---|---|---|
| 1 | 35 Isensee et al. 2024 | Two U+00A0 in the title, inherited from Crossref into `prior_works.json`, said to be carried into `43_` md and docx | **Registry**: still 2 NBSP in `prior_works.json` (`A Call for⍽Rigorous Validation in⍽3D`). **Deliverables**: 0 NBSP in `51_` md; the title is plain-spaced in the `51_` docx (and, on re-check, already in the `43_` md/docx as rebuilt 2026-10-07 11:36, after `42_` was written). The 25 NBSP the docx does hold are all the converter's "et al.⍽[N]" / "et al.⍽Title" non-breaking spaces (identical set and count in the v5 docx), not the Isensee title. **Draft**: the 2 NBSP (line 289) and the Herzberg `⋆` (line 288) persist only in the draft's own `## References` working list (Vancouver strings, lines 263 ff.), which is byte-identical to v5 and is not the source of the deliverable. | Yes — no longer reaches the submission files; the registry title could still be normalised by a sourced `title` override for hygiene. Cosmetic, optional. |
| 2 | 45 Wilcoxon 1945 | Registry `pages` = `80` (first page only); renders as `**1**, 80; 10.2307/3001968 (1945)` in article-number form | Unchanged: entry 45 renders identically in `51_` md and docx. Range not re-verified online (delta audit). | Yes — incomplete rather than wrong; optional sourced override `pages: "80-83"` if the PI wants the range. |
| 3 | 30 Vandenhende 2020 | "59" (BMVC paper number) printed in the page position, no DOI (proceedings) | Unchanged. | Yes — acceptable under the journal's no-copy-edit rule; optional. |

One further non-citation observation, for the record only: the v5 deliverable `43_` line 100 read "accessed September and October 2026" while the v5 draft (B0066) read "accessed September 2026", i.e. the v5 deliverable had been edited after conversion. In v6 the draft and both deliverables agree ("Fable 5.1, Opus 5 and Opus 5.5, accessed August to October 2026"). No reference is involved.

## 4. Not re-run in this delta audit (state recorded in 35_/42_)

- Existence and retraction of all 54 entries (strict pass, `tools/cite.py` 2026-10-06 23:19; `refs/prior_works_table.md`). No Crossref/PubMed re-fetch this round.
- Claim faithfulness of the 54 sources: the 124 byte-identical blocks carry over `35_`/`42_` findings; the three changed blocks are covered in §2.
- Self-citation ratio, ≥10-year share and 2022–2025 share: the reference list is byte-identical to v5, so the `42_` values (5.6%, 35%, 24%) are carried over unchanged (re-derived from registry years: 19/54 < 2016, 13/54 in 2022–2025, 3 `Ko20*` keys).
- `tools/check_draft.py` watch-term scan (not a citation check).

## 5. Conclusion

Round 5 touched three blocks and no marker. The only citation-carrying sentence it edited (Lakens 2013 in §2.4) changed after the marker, in the clause the roadmap item authorises, leaving the attribution and the marker byte-identical. Mechanical correspondence is intact both ways (67 uses, 54 slugs, 0/0 orphans), the deliverable's Nature list is byte-identical to v5 — 54 entries, first-appearance order, 18 style-required DOIs, 3 overrides and the Vandenhende order intact — and the deliverable diff is exactly the three edited paragraphs. The `tools/make_table_s9.py` mention is a code span, not a reference. Of the two `42_` observations, the Isensee NBSP no longer reaches the submission files (it persists only in the registry title and the draft's internal working list); the Wilcoxon single-page field is unchanged and optional. Nothing blocks submission. Next citation-check: after the next major change, as R12 requires.
