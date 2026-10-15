# 48_ AI 使用揭露查核（ARS `academic-paper` disclosure 模式，獨立分支）

## 1. 標頭

| 項目 | 值 |
|---|---|
| 模式 | `academic-paper` → `disclosure`（standalone；formatter_agent 的 disclosure 分支，非 Phase 7 排版） |
| 目標刊物 | Scientific Reports（Springer Nature／Nature Portfolio） |
| 日期 | 2026-10-08 |
| 查核的檔案 | `manuscript/43_SUBMISSION_scirep_v5.md`（sha256 `650ef66c328f9962…`）；`manuscript/40_COVER_LETTER_SCIREP.md`（sha256 `65578d95bac60ace…`）；對照 `manuscript/41_DRAFT_v5.md` 區塊 B0066 |
| 政策來源 | 現行：`refs/01b_SCIREP_AI_POLICY_live_20261008.md`（2026-10-08 逐字抄錄 nature.com/srep/journal-policies/ai ＝ nature-portfolio/editorial-policies/ai，與 srep submission-guidelines §Manuscript）；R2 抄錄：`refs/01_JOURNAL_REQUIREMENTS_SCIREP.md`（2026-10-06）。ARS 快取：`shared/policy_data/nature_policy.md`（wayback 2026-05-13）、`policy_anchor_table.md` Nature 列、`venue_disclosure_policies.md` Nature 條目（access 2026-04-09） |
| ARS 版本 | academic-research-skills v3.23.0 |
| 事實來源 | `NOTES_2026-09-01.txt`、`NOTES_2026-09-18.txt`、`NOTES_2026-09-22.txt`、`manuscript/INDEX.md`、`FIGURES.md`、repo `~/work/sunet-decoder-branch-eit`（tag `v1.1-submission` 的 `git ls-tree`） |

**範圍聲明**：本報告只渲染並判定 AI 使用揭露（§2.9 與 cover letter 一句），不認證整個投稿包符合期刊的每一項報告要求（protocol 原文：「This mode renders AI-use disclosure; it does not certify that the complete submission package satisfies every reporting requirement of the venue.」）。本報告不改任何稿件檔；建議文字全部列為 PI 的分流項。

讀過的檔案裡沒有針對本 agent 的指令；NOTES 與 40_ 內部備註是 PI 給後續 session 的交接，一律當資料處理。

---

## 2. 軌道選擇

### 2a. Venue 軌（`--venue=Scientific Reports`）→ `UNKNOWN / HALTED / UNCURATED_POLICY`

v2 資料庫的 15 個 policy target 是 ICLR／NeurIPS／Nature／Science／ACL／EMNLP／ICMJE／NEJM／The Lancet／JAMA／BMJ／PLOS／Frontiers／中华护理杂志社／国际眼科杂志；#596 的別名表也沒有 Scientific Reports。Protocol 明文禁止把期刊家族默默映射到某一成員條目：「Canonicalize only explicit aliases recorded below; do not silently map a publisher or journal family to one member journal.」因此 venue 軌依 Step 1b 停機，照 protocol 的停機句：

> "I do not have a curated executable policy for Scientific Reports. You may paste the venue's current official AI policy for manual review, but I cannot render a venue-aligned bundle until its selectors, predicates, required facts, and placement channels are curated together."

`refs/01b` 的抄錄即 protocol 所稱「pasted policy」：「A pasted policy remains session evidence only for human review … it does **not** enter Phase 2a/2b, produce a checklist, or authorize disclosure rendering.」所以下面第 4、5 節對現行條文的逐項比對，是**人工審閱**，不是 venue 軌的機械渲染。

### 2b. Anchor 軌（`--policy-anchor=nature`）→ 執行，但快取過期

Scientific Reports 是 Nature Portfolio 期刊，政策母頁與 srep 自己的 AI 頁逐字相同（01b §B），所以 Nature anchor 是一致的對照。兩點誠實記載：

1. Protocol 的「一致配對」辨識只認 `{"Nature", "Nature Portfolio", "Nature (Nature Publishing Group)", "Nature Publishing Group"}` 與前綴 `"Nature "`；「Scientific Reports」不符合任一條，**同時供兩個 selector 會被判為衝突而拒絕**。因此本報告只供 `--policy-anchor=nature` 一個 selector，走 Step 1c，不假裝 venue 字串被辨識。
2. ARS 快取的 Nature 文字是 wayback 2026-05-13；`refs/01b` §C 記錄快取引用的四句（copy-editing 豁免、「human accountability for the final version of the text」、生成式影像禁令、影像標示）**2026-10-08 已不在現行頁面**，該頁改為綠／橘／紅三級風險框架。依 PI 的指示，**現行文字優先**；ARS anchor 渲染的每個欄位在第 8 節逐一標示「快取句仍在／已不在」。

Anchor 軌的共享 intake 閘：外部使用清單未經作者證實（`external_use_inventory_confirmed = UNKNOWN`），依 protocol「The same intake-pending annotation applies when the shared external-use inventory is not author-confirmed」，anchor 軌輸出為 **intake-pending**；第 8 節仍依指示展示 `KNOWN(none)` 之下的渲染結果，供 PI 一次確認。

---

## 3. Phase 2 分類表與使用紀錄

### 3a. 分類表（protocol 全部九列）

| 類別 | 狀態 | 證據 |
|---|---|---|
| Research assistance | USED | `deep-research` lit-review 2026-10-06 → `literature/lit_review_20261006/`（NOTES_09-22 L722）；40 dB 出處追查（L248） |
| Citation checking | USED | R12d 管線 ＋ ARS citation-check：repo `review_record/07_,17_,30_,35_,42_CITATION_AUDIT_*.md`（tag v1.1-submission 內） |
| Drafting assistance | USED | `academic-paper` plan／outline（09-22 晚，Fable 5.1）、full（09-23 凌晨 → 草稿 v1） |
| Revision assistance | USED | revision round 1–4（15_、29_、34_、41_）；response 37_、44_ |
| Editing assistance | USED | abstract 模式、format-convert（32_）、Sci Rep 數字式引用轉換、docx 版面後處理（10-07） |
| Analysis assistance | USED | 助理寫並執行 `tools/` 的計分、掃描、bootstrap、統計與度量缺陷修正程式；MATLAB/EIDORS 資料產生腳本（§2.8）；`METRIC_DEFECT_2026-09-18.md` |
| Visual / artwork / media | USED（僅程式繪圖） | `FIGURES.md`：`make_fig_*.py` 向量 PDF；S1 架構圖 PlotNeuralNet（`tools/PlotNeuralNet/` 在 tag 內）；無生成式影像；43_ §2.1「No image in this paper was produced by any other means」 |
| Peer review simulation | USED | `academic-paper-reviewer` full／re-review：`review_record/12_,18_,33_,38_`；`phase_review_round2_scirep/`、`phase_rereview_round2_scirep/` |
| Other / unclassified | UNCERTAIN | 無已知未分類用途；UNCERTAIN 僅因外部使用清單未經作者證實（第 9 節） |

### 3b. 使用紀錄（tool × task；operations／targets 取自 protocol 封閉集）

| # | 工具 × 工作 | 性質 | operations[] | affected_targets[] |
|---|---|---|---|---|
| R1 | Claude（Fable 5.1）× plan／outline／full 起草，09-22～23 | 稿件準備 | SUBSTANTIVELY_DRAFTED | WHOLE_PAPER |
| R2 | Claude（Fable）× revision round 1–4、abstract，09-26、10-06、10-07 | 稿件準備 | SUBSTANTIVELY_DRAFTED | WHOLE_PAPER、ABSTRACT、TITLE |
| R3 | Claude（Fable）× 五席審查與 re-review，09-23、10-06、10-07（另 2026-08-27 對舊稿的 ARS review，見 §5b） | 稿件準備 | GENERATED | PEER_REVIEW_MATERIAL |
| R4 | Claude × 回覆信 37_、44_ | 稿件準備 | SUBSTANTIVELY_DRAFTED | PEER_REVIEW_MATERIAL |
| R5 | Claude（Opus 級）× citation-check ＋ R12d，五輪 | 稿件準備 | CHECKED_CITATIONS | REFERENCE_OR_CITATION |
| R6 | Claude（Fable）× lit-review 10-06 | 稿件準備 | SEARCHED | REFERENCE_OR_CITATION、INTRODUCTION_OR_BACKGROUND |
| R7 | Claude（9 月執行類 session，NOTES 未標模型）× 資料產生（MATLAB/EIDORS）、訓練、計分、掃描、bootstrap、度量缺陷修正 | **研究本身** | GENERATED、ANALYSED | CODE、ORIGINAL_RESEARCH_DATA（模擬資料，由腳本產生）、RESULTS、RESEARCH_PROCESS |
| R8 | Claude × `make_fig_*.py`、PlotNeuralNet 臂圖 | 研究本身 | GENERATED（程式） | RESEARCH_FIGURE_OR_MEDIA（註：圖是資料繪圖與程式畫的示意圖，不是生成式影像） |
| R9 | Claude（Fable；10-07 投稿日 **Opus 5.5**）× format-convert、docx 版面、頁碼行號、`09_SYSTEM_FIELDS`、就緒閘門 | 稿件準備 | FORMATTED_CITATIONS、EDITED | WHOLE_PAPER（僅版面）、OTHER_SUBMISSION_TEXT |
| R10 | Claude（Fable 起草；Opus 5.5 改末句）× cover letter 40_、檢查表 39_ | 稿件準備 | SUBSTANTIVELY_DRAFTED | OTHER_SUBMISSION_TEXT |

依 protocol「a rewrite that creates, replaces, or restructures substantive manuscript content is `SUBSTANTIVELY_DRAFTED` even when the category is Revision assistance」，R2 不降為 EDITED。`ai_listed_or_proposed_as_author = KNOWN(false)`：作者欄三位人類（43_ L8）。

---

## 4. 風險分級對映（現行政策 01b §B）

| 紀錄 | 分級 | 對應的例句（逐字） |
|---|---|---|
| R1、R2、R4、R10（起草／修訂／回覆信／cover letter） | **Amber** | "Extensive copy editing or writing support"；"Drafting explanatory summaries" |
| R3（模擬審查席） | **Amber** | Amber 期望："AI contributes to reasoning or critique"；綠級例 "Stress-testing research questions" 不足以涵蓋評價性輸出 |
| R6（文獻搜尋與比對） | **Amber** | "Comparing results to existing literature" |
| R7（分析程式的撰寫與執行） | **Amber**（最重的一筆，見下） | 最接近的例句："Suggesting analytical, experimental or methodological approaches"；"Recommending statistical tests or modelling approaches"；"Explaining outputs from statistical models in plain language" |
| R5（引用查核） | **Green** | 綠級期望 "AI use is likely to be reversible and verifiable; AI use does not introduce new intellectual content"；Crossref／PubMed 逐欄比對可逆可驗 |
| R8（繪圖程式） | **Green** | "Suggesting structure or formatting"；圖由資料經可重現腳本產生 |
| R9（排版、轉檔） | **Green** | "Suggesting structure or formatting of manuscript sections" |

**紅級逐項檢查**（結論：**無一筆落入紅級**，前提是揭露存在且作者的驗證為真）：

- "Generating hypotheses, analyses or conclusions and presenting them as human-derived" — 關鍵在 "presenting them as human-derived"。假設與判定規則是預註冊、由作者寫並雜湊（43_ §2.1、§2.9「wrote and fixed the preregistrations before any result existed」）；分析由助理寫的程式產生，**§2.9 明說**（「wrote the code in `tools/` that produced every reported number」），不是當作人寫的呈現。R7 比橘級例句重（不只建議方法，而是實作並執行），但紅級的構成要件是不透明或取代人的判斷；§2.9 的揭露加上預註冊的判定規則，使結論仍是人定、可驗。
- "Using an LLM to generate core research reasoning without disclosure" — 條件是 "without disclosure"；已揭露。核心推理（研究問題、臂的設計、地板、addendum 的決定）在 §2.9 歸於作者。
- "Delegating peer review to an LLM" — 這條在框架裡是對**審查人**角色講的（"applied consistently to authors, peer reviewers, and editors"；Peer reviewers 段未抄但主旨相同）：審查人不得把期刊委託給他的審查交給 LLM。作者端投稿前自辦的模擬審查席是作者自我批判的工具，期刊的同儕審查仍由期刊的人類審查人執行，沒有任何一方的責任被轉移；且已揭露並存於 repo。不是該項。
- "Fabricating data, citations or results" — 資料由 EIDORS 腳本產生、結果由 290＋116 次訓練產生、引用經五輪查核（R5）；AI 起草文字是捏造引用的典型來源，R5 正是對此的控制。無。
- "Assigning authorship or accountability to AI systems or tools" — 作者欄無 AI；§2.9 把 AI 稱為 "the assistant"，是工具。但 §2.9 **沒有**明示作者負全責的句子（見 §5d）。
- "Creating photorealistic images (deepfakes)" — 無影像生成。

---

## 5. §2.9 逐項合規

§2.9 現文（43_ L100）：

> The authors used Claude (Anthropic; Fable 5.1 and Opus 5, accessed September and October 2026) throughout this work. The assistant wrote the code in `tools/` that produced every reported number, figure and table, drafted and revised the manuscript text, ran the simulated peer-review panel recorded in the project repository, and carried out the citation verification reported in the same place. The authors defined the research questions, wrote and fixed the preregistrations before any result existed, made every design decision, and verified the results and the text.

**(a) 位置——符合。** 投稿指南（01b §A）："Use of an LLM should be properly documented in the Methods section (and if a Methods section is not available, in a suitable alternative part) of the manuscript." §2.9 在「2. Materials and Methods」之內、§2.8 Code availability 之後。R2 抄錄（refs/01 L86）當時記「現稿的 AI 聲明在 Acknowledgements，要搬到 Methods」——已搬；43_ Acknowledgements（L292）現無 AI 字樣。

**(b) 工具識別——名稱與開發者正確；版本標籤與期間需 PI 確認後修正。** NOTES 的逐 session 模型標籤：

| 日期 | session | 模型標籤（NOTES 原文） |
|---|---|---|
| 2026-08-27 | 對舊稿（Nov142025）的 ARS 審查 `Nov142025/ARS_Review_2026-08-27/`（NOTES_09-01 L60、134、309） | 未標 |
| 2026-08-28／29 | 兩份預註冊雜湊（NOTES_09-18 L11、14） | 未標 |
| 2026-09-01～09-18 | pilot、資料產生、訓練、度量缺陷、七張圖 | **未標模型**（NOTES_09-01 無任何模型字樣；NOTES_09-18 只在「切 Fable 之後做」規劃段出現 Fable） |
| 2026-09-22 | 規劃；同日晚間 plan／outline | 「本份在 Fable 5.1 上寫」（L7）；「Fable 5.1，晚間」（L122） |
| 2026-09-23 白天（計畫） | 執行類交接 | 「Opus 5」（L262，**是交接標題，不是事後紀錄**） |
| 2026-09-26 | revision round 1；PM 投稿包 | 「Fable」（L458） |
| 2026-10-03 12:30 | RECON 計分（另一篇），並以 `recon_results.py` 重算本稿 H5 的 +0.229／0.384 | **「Opus 5.5」**（L611） |
| 2026-10-03 下午 | RECON 判讀 | 「Fable 5.1」（L647） |
| 2026-10-06～10-07 凌晨 | revision 2–4、panel、re-review、cover letter、v5 交付 | 「Fable」（L710–864） |
| 2026-10-07 投稿日 | docx 版面後處理程式、頁碼行號、`09_SYSTEM_FIELDS`、閘門簽核、套用 40_ 末句修改 | **「Opus 5.5」**（L914） |

所以：**「Opus 5.5」確實出現在兩個 session**，其中 10-07 那個改了 `tools/format_convert_scirep.py`、新增 `tools/make_system_fields_scirep.py`、重產 43_ 的 docx（md 雜湊不變）並套用 cover letter 的修改——屬於本稿的投稿工作。「Opus 5」只出現在規劃句與交接標題，沒有任何 session 事後紀錄為 Opus 5；9 月 1 日到 18 日的 session 完全沒有模型標籤。另外，AI 使用**始於 2026-08-27**（對前身稿的 ARS 審查，43_ §2.1 與 cover letter 都把那次重建當本研究的起點），早於 §2.9 寫的 "September"。

本報告**不替 PI 決定**標籤。三個選項，由 PI 依記憶或帳號紀錄選：
- (i) `Fable 5.1, Opus 5 and Opus 5.5, accessed August to October 2026`（若 9 月執行類 session 確為 Opus 5）；
- (ii) `Fable 5.1 and Opus 5.5, accessed August to October 2026`（若 9 月 session 其實也是 5.5，或無法證實 Opus 5）；
- (iii) 保留 "Fable 5.1 and Opus 5" 但加 "and Opus 5.5"、期間改 "August to October 2026"。
另一個殘餘不確定：ARS 的 `ARS_MODEL_TIERING=economy` 若曾開啟，執行類 agent 會降一階（上層 CLAUDE.md 記載 R5 殘餘風險：讀到的是宣告模型，不是逐次證明）。PI 若從未開 economy，可不提。

**(c) 用途描述——涵蓋主要項目，漏一項。** §2.9 列了程式（數字／圖／表）、起草與修訂、模擬審查、引用查核。對照 §3a：**文獻搜尋（R6）未提**，而它是橘級例句 "Comparing results to existing literature" 的直接對應；cover letter／回覆信（R10、R4）不在稿件內，Methods 不必提。資料產生腳本可解讀為已含於「code in `tools/`」，但 §2.8 把 MATLAB/EIDORS 資料產生腳本與 Python 分開寫，§2.9 宜對齊。建議補兩個詞（第 8 節替換文）。

**(d) 人的問責——建議補一句（非現行條文的硬性欄位，但是框架的核心期望）。** 現行 Core expectations："Human accountability is non-transferable — Accountability for scholarly content, evaluation, and editorial decisions cannot be delegated to AI systems."；Authors 段："Remain fully accountable for originality, accuracy, and integrity."；橘級合規條件："accountability must remain clearly human-led and defensible"；綠級："Disclosure … clearly demonstrates human accountability." §2.9 以 "verified the results and the text" 示範了監督，但沒有一句把責任明說。ARS 快取（已過期）的 venue 列寫 "Must state authors verified and take responsibility for all content"，anchor 列 9／10 列為 explicit-mandate——現行頁沒有那句原文，所以這是**建議**而非必要。建議句：

> The authors take full responsibility for the content of this paper.

放在 §2.9 末句之後。十三個字，不影響字數上限。

**(e) 驗證／監督可示範（橘級要件）——符合。** 橘級："Permitted with human oversight, verification, and transparency through disclosure." §2.9："made every design decision, and verified the results and the text"；repo tag v1.1-submission 內有 `review_record/`（審查席、re-review、五輪引用查核、各輪 author-adjudication.json）與預註冊雜湊，是可查的監督紀錄。若 PI 願意，可把 "verified the results" 加上 "against the registered decision rules"，讓「驗證對什麼」有依據；可選。

**(f) 不把作者資格或問責歸給 AI——符合。** 投稿指南："Large Language Models (LLMs) … do not currently satisfy our authorship criteria." 作者欄三位人類；CRediT 無 AI；§2.9 稱 "the assistant"。

**(g) 保密——未知，列 PI 確認。** Core expectations："Manuscripts, peer review reports, and sensitive data must not be shared with unsecured or public AI systems." 稿件與模擬審查報告都經 Claude（Anthropic 的商業產品，Claude Code／API session）處理。條文沒有定義 "unsecured or public"；需 PI 確認的事實是**帳號類型與資料用途設定**（商業／API 條款預設不用於訓練，消費者方案則有需使用者選擇的訓練設定）。這是行為規範，不是揭露欄位，§2.9 不必寫；但 PI 應能在被問時答得出來。本報告不從記憶斷言 Anthropic 條款內容。

**(h) 影像規則——無須申報。** 現行頁沒有生成式影像條文（01b §C：image-integrity 頁 find "generative" 無命中）。本稿影像：EIDORS/GREIT 重建（43_ §2.1 "No image in this paper was produced by any other means"）、`make_fig_*.py` 由資料繪出的向量圖、S1 的 PlotNeuralNet 程式畫臂圖；Fig. 4 的網路輸出是受試模型的結果，不是影像工具。即使套用 ARS 過期的 row 16（"unable to permit its use for publication"、"labelled clearly as generated by AI"），也因無生成式影像而無物可標。

---

## 6. Cover letter

Sci Rep 現行來源**不要求** cover letter 提 AI：01b §A「cover letter 一節未提 AI」；refs/01 L90 列的 cover letter 必含五項（通訊作者、適刊理由、建議審查人、排除審查人、EBM 討論）無 AI。ICMJE anchor 才有「in both the cover letter and the submitted work」的要求，Sci Rep 不受其拘束；現有句子無論如何已滿足它。

現有句（40_）："The use of AI tools in drafting and revision is documented in the Methods (Section 2.9)."

判定：**COMPLIANT AS IS**。可選的改善：EBM 只看 cover letter、不看稿件之前，"in drafting and revision" 比 §2.9 的實際範圍（程式、分析、審查席、引用查核）窄，而框架的透明原則是 "removes ambiguity about how AI might have been used"。若 PI 要對齊，替換為：

> The use of AI tools in this work (analysis code, drafting and revision, a pre-submission simulated review and citation checking) is documented in the Methods (Section 2.9).

這是 PI 決定；不改也合規。

---

## 7. 一致性

| 位置 | 內容 | 與 §2.9 一致？ |
|---|---|---|
| Acknowledgements（43_ L292） | 只有 NSTC 經費與 EIDORS／Netgen 致謝，無 AI | 一致；舊的 Acknowledgements 放法已移除 |
| Author contributions（L296） | Software 歸 Yen-Fen Ko | **不矛盾**。CRediT 的角色只派給可問責的人類貢獻者，工具不列；Software 定義含設計、實作、測試，PI 規格、驗證、測試程式即符合。§2.9 已說明程式由助理所寫，兩處合讀即完整；不需加子句 |
| Additional Information（L300） | 利益衝突，無 AI | 一致 |
| Data Availability（L176） | repo、checkpoints、無人類資料 | 一致；§2.9 的 "recorded in the project repository" 經 `git ls-tree v1.1-submission` 證實：`review_record/` 含 12_、18_、33_、38_ 審查席與 07_～42_ 引用查核 |
| Figure legends、Tables、S1–S9（L302–382） | 無 AI 字樣 | 一致 |
| §2.1（L60） | "No image … produced by any other means" | 指重建影像的來源，與 §2.9 的繪圖程式不衝突 |
| **41_DRAFT_v5 B0066** | "accessed **September** 2026" ＋ `[FUNDING: … to be supplied by the PI.]` 佔位 | **與 43_ 不同**：43_ 已改 "September and October" 並移除佔位。43_ 的 md 雜湊是閘門豁免條件（46_ 簽核），所以 43_ 是權威；但若日後從 41_ 重產 43_，這兩處會倒退。列為檔案一致性提醒 |

---

## 8. 結果信封與判定

```
disclosure_outcome      : REQUIRED        （≥1 類 USED；橘級用途須揭露）
venue track             : execution_status=HALTED, halt_reason=UNCURATED_POLICY
                          （"Scientific Reports" 不在 v2 資料庫；禁止映射到 Nature 條目）
anchor track (nature)   : G10 row 4 fires（多類 USED）；shared intake gate →
                          INTAKE-PENDING（external_use_inventory_confirmed = UNKNOWN）；
                          Other/unclassified UNCERTAIN → per-facet annotation
ai_listed_or_proposed_as_author : KNOWN(false)
prohibited-use (live Red tier)  : none found（第 4 節）
```

**ARS anchor 渲染（Nature 列 9／10／14／15／16）在 `KNOWN(none)` 之下會長這樣**，每列標示快取句是否仍在現行頁：

| 列 | ARS 會渲染的內容 | 快取句狀態（01b §C） |
|---|---|---|
| 9 Human oversight（explicit-mandate） | 引 "In all cases, there must be human accountability for the final version of the text and agreement from the authors that the edits reflect their original work." | **已不在**；現行對應句 "Human accountability is non-transferable" |
| 10 Human responsibility（explicit-mandate） | 引 "an attribution of authorship carries with it accountability for the work, which cannot be effectively applied to LLMs" | 前半句**仍在**（srep 投稿指南 §A）；"final version of the text" 句已不在 |
| 14 Disclosure location（explicit-recommend） | "Methods section (and if a Methods section is not available, in a suitable alternative part)" → 放 Methods | **仍在**（§A） |
| 15 Copyediting carve-out（eliminate 語意） | 不適用：用途是實質起草，非 copy-editing-only；不產生豁免 | 快取句**已不在**；現行框架改以綠級處理，且綠級仍寫 "Disclosure enhances trust" |
| 16 Image rights（explicit-mandate） | `image_disclosure_instructions`：無生成式影像，無逐圖標示；不產生 patch | 快取句**已不在**；現行頁無生成式影像條文 |

### 判定

**§2.9：CHANGE REQUIRED（一處事實）＋ COMPLIANT, OPTIONAL IMPROVEMENT（兩處）。**

- 必改（事實準確，依 "Transparent declaration of AI … removes ambiguity about how AI might have been used"）：模型標籤漏 Opus 5.5、期間漏 8 月。**哪一組標籤是 PI 決定**（§5b 三選項）。
- 可選一：補文獻搜尋與資料產生（§5c）。
- 可選二：補問責句（§5d）。

替換全文（以選項 (i) 示範；標籤與期間由 PI 定）：

> The authors used Claude (Anthropic; Fable 5.1, Opus 5 and Opus 5.5, accessed August to October 2026) throughout this work. The assistant wrote the code in `tools/` that generated the simulated data and produced every reported number, figure and table, assisted the literature search, drafted and revised the manuscript text, ran the simulated peer-review panel recorded in the project repository, and carried out the citation verification reported in the same place. The authors defined the research questions, wrote and fixed the preregistrations before any result existed, made every design decision, and verified the results and the text against the registered decision rules. The authors take full responsibility for the content of this paper.

與現文相比多 27 字；改動不觸及任何數字或主張。改了就要同步 41_ B0066、重產 43_ 的 docx、重跑閘門（md 雜湊會變，46_ 的豁免條件失效，需 PI 重簽）。

**Cover letter 句：COMPLIANT AS IS**；第 6 節的擴寫是可選、PI 決定。

**Author contributions：COMPLIANT AS IS**（§7）。

---

## 9. 待 PI 確認

1. **外部使用清單**（protocol 必要輸入，本報告無法代答）：ARS 紀錄之外是否用過 AI——例如 Claude 以外的工具、網頁版對話、翻譯、投稿系統欄位草擬、`Nov142025` 舊稿時期的工具。答 `KNOWN(none)` 或列清單；答了 anchor 軌才從 intake-pending 轉為可渲染。
2. **模型版本標籤與期間**（§5b）：9 月 1–18 日與 9 月 23–26 日的執行類 session 是 Opus 5 還是 Opus 5.5；是否曾開 `ARS_MODEL_TIERING=economy`；期間是否改 "August to October 2026"（AI 使用始於 08-27 的舊稿審查與 08-28／29 預註冊前後）。
3. **預註冊 §9 addendum 的起草者**：§2.9 說作者 "wrote and fixed the preregistrations"；NOTES 只記 RECON 的 §11 addendum 由 Fable 起草（10-03），本稿 §9 addendum（09-24 開跑）的草稿是 PI 寫或助理起草、PI 定案，NOTES 未明。若是後者，"wrote" 仍成立（PI 定案並雜湊），但 PI 應知道這個事實。
4. **保密依據**（§5g）：使用的 Anthropic 帳號類型與資料用途設定，以便回答 "must not be shared with unsecured or public AI systems"。不必寫進稿件。
5. **三個文字決定**：§2.9 替換文採用與否（含標籤選項）；cover letter 句是否擴寫；41_ B0066 是否同步。

---

## 10. Orchestrator 核對（主 session，2026-10-08，加在子代理輸出之後；不改上面任何判定）

- **§5(b) 的模型標籤指控核過**：`NOTES_2026-09-22.txt` L611（2026-10-03 RECON 計分）與 L914（2026-10-07 投稿日）兩個 session 標「Opus 5.5」；「Opus 5」只在 L76（分類原則）與 L262（交接標題）。指控成立，CHANGE REQUIRED 維持。
- **§7／§9 把 `41_DRAFT_v5.md` B0066 的 "accessed September 2026" 與 `[FUNDING: …]` 列為與 43_ 的漂移——這一項不是漂移**：`manuscript/AUTHOR_FIELDS.json` 第 5、15 行就是這兩個字串的替換表，`tools/format_convert_scirep.py` 在產生 43_ 時填入；41_ 是填入前的草稿，依設計帶占位符（10-07 凌晨 NOTES：「AI 聲明：AUTHOR_FIELDS 加 accessed September 2026 → September and October 2026」）。**不需同步 41_**；若 PI 決定改 §2.9 的模型標籤，改法是改 AUTHOR_FIELDS.json 的替換值（或走 round-5 patch 改 B0066 正文），再重跑 format-convert。
- **2026-08-27 的 ARS 審查對象是前身稿**（`Nov142025/ARS_Review_2026-08-27/`）。它算不算「this work」的 AI 使用，是 PI 的判斷：43_ §2.1 與 cover letter 把那次重建當本研究起點，所以 §5(b) 建議期間改 "August to October 2026" 有依據；但也可以把起點定在預註冊（2026-08-28／29，同樣是八月）——兩種讀法都落在八月，結論一樣。
- 本報告的三個判定（§2.9 CHANGE REQUIRED＋兩項可選；cover letter 句 COMPLIANT AS IS；Author contributions COMPLIANT AS IS）照 R16 進 triage，由 PI 決定；本 session 不改正文、不改 cover letter。


---

## 11. Round-5 之後的重綁（2026-10-08，主 session）

PI 選 §5(b) 選項 (i)。round-5 patch 把 B0066 的括號改為「Fable 5.1, Opus 5 and Opus 5.5, accessed August to October 2026」，其餘 §2.9 逐位元不變（`49_DRAFT_v6.md`；獨立 scoped 核驗 `phase_rereview_round4_scirep/addendum_v6.json` REV-R5-3 FULLY_ADDRESSED，註明「Opus 5」依 PI 的選項 (i) 認定）。交付檔 `51_SUBMISSION_scirep_v6.md`（sha256 `7cfc209292ef…`）§2.9 現文：

> The authors used Claude (Anthropic; Fable 5.1, Opus 5 and Opus 5.5, accessed August to October 2026) throughout this work. The assistant wrote the code in `tools/` that produced every reported number, figure and table, drafted and revised the manuscript text, ran the simulated peer-review panel recorded in the project repository, and carried out the citation verification reported in the same place. The authors defined the research questions, wrote and fixed the preregistrations before any result existed, made every design decision, and verified the results and the text.

逐項重對 §5：(a) 位置 Methods 符合；(b) 工具名稱、開發者、版本標籤、期間——§5(b) 的事實問題已消除；(c) 用途描述——可選的兩個詞 PI 本輪未採，非合規欄位；(d) 問責句——可選，PI 本輪未採，現行條文無硬性欄位；(e)(f)(h) 不變、符合；(g) 保密依據仍待 PI 口頭確認，不是稿件欄位。Cover letter 句未改，維持 COMPLIANT AS IS。

FINAL VERDICT (deliverable 51_SUBMISSION_scirep_v6.md sha256 7cfc209292ef): COMPLIANT — §2.9 and the cover-letter sentence meet the live Scientific Reports / Nature Portfolio AI policy (refs/01b, accessed 2026-10-08); optional improvements of §5(c)(d) and §6 remain open PI choices.
