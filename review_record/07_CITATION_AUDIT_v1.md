# Phase 5a — Citation Audit Report（`citation_compliance_agent`）

**Draft**: `DRAFT_核心論文_v1.md`（Phase 4b, in-phase revision 1, 2026-09-23）
**Corpus**: `refs/refs_in.json` → `refs/prior_works.json`（`tools/cite.py`，Crossref REST + PubMed E-utilities，2026-09-23）
**Policy**: `citation_existence = strict`（投稿用）；`retraction` 政策 = strict。
**Scanner**: `tools/check_draft.py`（可重跑）。

## 1. 存在性與撤稿（strict）

| 項目 | 結果 |
|---|---|
| 參考文獻筆數 | 14 |
| 由 DOI 解析成功（Crossref） | 14/14 |
| PubMed 收錄 | 10/14（Caruana、Ronneberger、Wang、Wilcoxon 未收錄；期刊縮寫改用 Crossref `short-container-title`，逐筆表已標） |
| 撤稿 | 0 |
| 更正（`updated-by`） | 0 |
| 手打字串 | 0（全部由 `cite.py` 渲染，R12d） |

**判定：strict 政策通過，無擋件。**

## 2. 正文引用 ↔ 參考文獻表

| 項目 | 結果 |
|---|---|
| 正文引用實例 | 19 |
| 不同來源 | 14 |
| slug 不在語料庫內 | 0 |
| 孤兒參考文獻（列表有、正文無） | **0**（第一版有 1 筆 Frerichs 2017，修訂時引進 Introduction 首句） |
| 正文引了但列表沒有 | 0 |
| 自我引用 | 3/14 = **21%**（ARS 旗標 15%）；結構性，Conflicts of Interest 已交代；**不建議加引用稀釋** |

引用分布：Ko2021PLOSONE 3、Wang2024TIM 3、Ko2025CurrMedImaging 2、其餘各 1。

## 3. 年份與 seminal 標記（>10 年）

| 來源 | 年 | 處理 |
|---|---|---|
| Wilcoxon 1945 | 81 年 | seminal（檢定原著） |
| Caruana 1997 | 29 年 | seminal（多任務學習） |
| Adler & Lionheart 2006 | 20 年 | seminal（EIDORS 套件論文） |
| Pulletz 2006 | 20 年 | 方法依據（ROI 定義比較）；若審查人要更近的 ROI 比較，走 R12d 另找 |
| Adler 2009 | 17 年 | seminal（GREIT 共識） |
| Lakens 2013 | 13 年 | 方法依據（dz） |
| Ronneberger 2015 | 11 年 | seminal（U-Net） |

## 4. v3.7.3 anchor 定位（非 D2 範圍，交 PI 決定）

10/19 個引用實例為 `<!--anchor:none:-->`，原因是語料庫脈絡只提供三篇前作與 Wang 2024 的逐字原文（`refs/PRIOR_WORK_SCOPE.md`、`literature/Wang2024_TIM_DHU-Net_fulltext_ieeexplore.txt`）。清單：

| slug | 位置 | 引用的主張 | 建議的定位方式 |
|---|---|---|---|
| Frerichs2017TREND | §1 首句 | 胸腔 EIT 臨床應用共識 | `section:` 摘要或 "Clinical use" 節 |
| Pulletz2006ROI | §1 | 四分之一振幅 ROI 為臨床方法 | `section:` Methods（ROI 定義） |
| Ko2021PhysiolMeas | §1 | U-Net 肺分割 | `page:` 或 `section:` 摘要（`../publications_semi-SiamseseUN/` 有 PDF） |
| Caruana1997MTL | §1 | 第二監督標的為正則化 | `section:` 1 Introduction |
| Nosek2018Prereg | §2.1 | 預註冊的理由 | `page:` 2600（首頁） |
| Adler2006EIDORS | §2.3 | EIDORS 工具 | `section:` 摘要 |
| Adler2009GREIT | §2.3 | GREIT 重建器 | `section:` 摘要 |
| Ronneberger2015UNet | §2.4 | U-Net 骨幹 | `section:` 2 Network Architecture（`literature/Unet.pdf` 有） |
| Wilcoxon1945 | §2.4 | signed-rank 檢定 | `page:` 80 |
| Lakens2013EffectSize | §2.4 | 配對 dz | `section:` "Cohen's d for within-subjects designs" |

這些都是「工具／方法出處」型引用，主張是「某方法存在且如此定義」，不是把特定發現歸給來源，claim-faithfulness 風險低。PI 若要補定位，逐筆打開原文填 `section:`／`page:` 即可；不補則在 `format-convert` 時剝掉 anchor 標記，不影響投稿稿。

## 5. 渲染瑕疵（`cite.py`，`format-convert` 轉 IEEE 時處理）

1. Pulletz 2006：Crossref 給 given name "H R van" → 渲染成 "Genderingen HRv"；IEEE 應為 "H. R. van Genderingen"。
2. Lakens 2013：缺文章號 863（Crossref 無 page 欄）；IEEE 格式需 "vol. 4, art. no. 863"。
3. Ronneberger 2015：缺 LNCS 卷號 9351 與書名 MICCAI 2015；IEEE 格式需補。
4. Wang 2024：期刊縮寫末尾雙句點（`Meas..`）。

## 6. 主張—來源對應抽查（claim faithfulness，逐筆對原文）

| 正文句 | 來源 | 原文依據 | 判定 |
|---|---|---|---|
| "adding a branch from the end of the contracting path" | Ko2021PLOSONE | `PRIOR_WORK_SCOPE.md` §二 逐字 | ✔ |
| "interaction between branch structure and multi-task means" | Ko2021PLOSONE | 同上 | ✔ |
| conclusions list different reconstruction algorithms as future work | Ko2021PLOSONE | 同上第三段逐字 | ✔ |
| optimal loss weights determined；24 frames healthy adult | Ko2025CurrMedImaging | 同上 CMI 兩句逐字 | ✔ |
| encoder-side two branches, fusion decoder；tank；90→20 dB evaluation | Wang2024TIM | 全文 §II-A、§IV-B、§V-A | ✔ |
| cardiac impedance amplitude position dependent | Graf2017PLOSONE | 標題逐字 | ✔（僅標題層級） |
| second supervised target is a regulariser | Caruana1997MTL | 一般性歸屬 | ✔（未讀全文，屬常識級歸屬） |

## 7. 結論

- **strict 存在性：通過。** 撤稿 0、更正 0、孤兒 0、語料庫外 0。
- **交 PI 的決定**：(a) 10 個 anchor 是否補定位；(b) 自我引用 21% 維持不稀釋。
- **交 format-convert**：第 5 節四項。
- **下一次 citation-check 時機**：任何一次大改之後（MANUSCRIPT_RULES R12／RESEARCH_PRIMER §九），不是定稿前才跑一次。
