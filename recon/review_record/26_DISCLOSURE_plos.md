# 26_ AI 使用揭露與投稿政策查核：PLoS One（ARS `academic-paper` disclosure 模式）

## 1. 標頭

| 項目 | 值 |
|---|---|
| 日期 | 2026-10-31 |
| ARS | 3.23.0（與基準一致）；skill `academic-research-skills:academic-paper`，mode `disclosure`；`references/disclosure_mode_protocol.md` 已載入並依序執行 |
| 執行者 | Opus 5.5 子代理（disclosure 屬「紀錄」類，依分派表用 Opus 5）。**本檔不改任何其他檔案** |
| 受測交付檔 | `submission_PLOS_20261031/Manuscript.md` sha256 **`ed42a4db720475c2f518d2c3279fb63f5f1ddcc14116aa76f057452ceef6ff7c`**；`Manuscript.docx` sha256 `1278eb094cfe6313ae589b098b8753924dc54a04370bccb51fe5af7f96f5de0f`（docx 抽出的文字與 md 的 Funding／Acknowledgments 段逐字相同，六個 `MATERIAL GAP` 都在） |
| 工作稿 | `RECON_paper/manuscript/23_DRAFT_v7.md`（Acknowledgments 句相同；`24_SUBMISSION_plos_v7.md` 也一樣） |
| 揭露受測文字 | 交付檔 Acknowledgments 第一段（下稱 ACK） |
| 事實來源 | `NOTES_2026-09-22.txt`（行號 L 標出）、`NOTES_2026-09-01.txt`、`tools/` 檔案時間、`manuscript/48_DISCLOSURE_scirep.md`（核心論文的前例與 PI 選項 (i)） |

## 2. 政策錨點與現行頁比對

**使用的錨點：`refs/01_JOURNAL_REQUIREMENTS_PLOSONE.md`「AI 政策」節（2026-10-11 從 journals.plos.org 查證）。ARS 快取的 PLOS 列沒有拿來當依據。**

**現行頁重讀（2026-10-31，WebFetch `https://journals.plos.org/plosone/s/ethical-publishing-practice`，"Artificial Intelligence Tools and Technologies" 節加 FAQ）：重讀成功，內容和 refs/01 一致，沒有漂移。** 頁面沒有標更新日期。

| 要點 | refs/01（10-11） | 現行頁（10-31） | ARS 快取（`venue_disclosure_policies.md` PLOS 列，access 2026-08-01） |
|---|---|---|---|
| 揭露範圍 | 任何用 AI 產生或修訂內容、或支援研究的使用 | 同（"Any AI use to generate or revise content for a PLOS submission"，也包括支援所報告的研究） | 同義 |
| 三要素 | 工具名稱、怎麼用／影響哪些部分、作者怎麼驗證輸出 | 同（影響範圍明列 study／article／data／supporting files；"how the user evaluated the validity of the tool's outputs"） | 四欄：tool、how used、how validated、affected parts（同義） |
| 放在哪裡 | 正文：Methods 專節、Acknowledgments 或圖說 | 同：dedicated Methods section、Acknowledgements 或 relevant figure legend(s) | ⚠️ **較窄**：Methods 優先，Acknowledgements 只限沒有 Methods 的文類 |
| AI 作者 | 不可 | 同（AI tools cannot be listed as authors） | ⚠️ 記為「頁面無明文」（2026-08-01） |
| 語言修飾 | 不必揭露；翻譯建議揭露 | 同 | — |
| 程式碼 | 產生或發展分析腳本／程式碼要揭露 | 同（FAQ "Do I need to disclose AI use for generation or development of analysis scripts or software code?" 答 Yes） | 未列 |
| 圖 | AI 做圖可以，但要在圖說揭露 | 同（FAQ "Does PLOS allow AI use in figure preparation?" 答 Yes；AI 用於製圖要在圖說清楚揭露）；**頁面沒有定義 "AI-generated figures"，也沒有區分「AI 寫的繪圖程式」和「AI 生成的影像」** | 未列 |
| 主張歸屬 | 作者對內容全責 | 假說、解讀、結論的陳述必須是作者自己的想法 | 同義 |

**結論**：ARS 快取在放置位置與 AI 作者兩點上過時或過窄，與 2026-10-08 在 Nature／Sci Rep 發現的情形同類。若照快取的封閉列舉 `article_has_methods_section=true → METHODS`，Acknowledgments 會被判不合；照錨點與現行頁則是合規。以下一律照錨點判。

## 3. ARS venue 軌結果信封（照 protocol 據實記錄）

- Selector `--venue=PLOS ONE` → 別名表正規化為 `PLOS`（資料庫有這一列）→ venue 軌。
- `disclosure_outcome = REQUIRED`（已證實的使用全都落在 PLOS 的揭露規則內）。
- `execution_status = HALTED`，`halt_reason = UNRESOLVED_INPUT`：(a) `external_use_inventory_confirmed = UNKNOWN`，ARS 紀錄之外的 AI 使用要作者親自證實，子代理不能代答；(b) 第 4 節的事實取自 NOTES，protocol 規定要作者確認後才算 `KNOWN`。另外記一個 **CONTRACT_GAP**：快取列的放置列舉比現行政策窄（第 2 節）。
- 所以第 6 節的替換句是**交給 PI 確認的提案**，不是 ARS 判定 READY 之後渲染出的定稿。
- `ai_listed_or_proposed_as_author = KNOWN(false)`：作者欄是三位人類（交付檔 L5）。
- PLOS 的禁止用途判別 `ai_fabricated_or_misrepresented_primary_research_data`：依紀錄為 **false**。資料是 AI 寫的模擬程式產生的，每個數字都可以從 per-seed 檔回推（NOTES 10-31 R10c：321 個數字、0 個無法回推），各狀態都有雜湊。這一項仍要 PI 確認。

## 4. Phase 2 分類與使用紀錄（只算 RECON 這篇）

| 類別 | 狀態 | 紀錄依據 |
|---|---|---|
| Research assistance（文獻檢索、書目） | **USED** | 10-11 RECON 文獻底：ARS deep-research lit-review，四個 bibliography_agent（**Opus 5**，L1149）加 Fable 綜整與選用建議；PI 勾選 |
| Citation checking | USED | 07_／16_／16b_／21_ citation-check（Opus 子代理） |
| Drafting | USED | outline、壓力測試、06_ 起草（Fable）；預註冊 §1–10（09-26 14:30「草稿」L520）、§11 草稿（10-03 L663）、§12 草稿（10-11 L1129，PI「照草稿」L1131）；判讀三部分（Fable，PI 核可） |
| Revision | USED | rounds 1–1f patch 鏈（Fable） |
| Editing（含轉 Vancouver） | USED | format-convert、cite.py 渲染 |
| Analysis | **USED** | 資料產生（`gen_recon_full.m`、`build_mixed_dataset*.py`、`build_loro_dataset_ps.py`）、訓練（`train_arms.py`，檔案時間 **Aug 30**；`arms.py`、`gen_dataset.m` 是 8/28–29 的凍結檔）、計分（`evaluate.py`、`recon_results.py`）、閘門與診斷腳本；助理也實際操作了管線（09-26 17:41 背景開跑） |
| Visual | USED | Fig 1／2／5：`tools/make_recon_fig{1,2,5}.py`；Fig 3／4／S1 Fig：`results_recon/figs/` 下的診斷 PNG（`recon_scale_check.py`、`recon_shift_inputs.py`、`recon_mixed_ps_gate.py`、`recon_loro_preds.py`）。**沒有任何生成式影像模型** |
| Peer review simulation | USED | phase_review_round1_20261031、phase_rereview_round1_20261031，以及判讀的五席審查 |
| Other／unclassified | UNCERTAIN | 外部使用清單未證實（第 3 節） |

**模型**：Fable 5.1（多數 session）、**Opus 5.5**（10-03 計分 session，L611）、**Opus 5**（10-11 書目 agent，L1149，這是事後紀錄，不是規劃句）。10-31 的「Opus 子代理」沒有記版本。起草輪紀錄為「不開 economy」，其他輪沒有紀錄。
**期間**：RECON 專屬的工作是 2026-09-26（預註冊草稿與雜湊）到 2026-10-31。但本篇的數字還靠兩樣更早的東西：沿用的 AI 撰寫程式碼（`train_arms.py` 8/30、`arms.py`、`gen_dataset.m` 8/28–29），以及 09-24 到 09-26 用同一套程式訓練的 GREIT 網路。

## 5. 逐項判定

### 5A. AI 揭露（ACK）

| # | 要求（錨點） | 交付檔證據 | 判定 |
|---|---|---|---|
| A1 | AI 不可為作者 | 作者欄："Yen-Fen Ko¹\*, Chang-Wen Chen², Tang-Chuan Wang³" | **COMPLIANT** |
| A2 | 放在正文：Methods、Acknowledgments 或圖說 | ACK 在 Acknowledgments；Methods 2.7 有指標句 "artificial-intelligence use is disclosed in the Acknowledgments" | **COMPLIANT**（照錨點；ARS 快取的較窄規則已在第 2 節說明） |
| A3 | 工具名稱 | "Claude (Anthropic; Fable 5.1 and Opus 5.5 …)" | **CHANGE REQUIRED**：漏了 **Opus 5**，NOTES L1149 記錄 RECON 文獻底的四個 bibliography_agent 是 Opus 5 |
| A4 | 期間 | "accessed September to October 2026" | **CHANGE REQUIRED**：本篇報告的每個數字都經過 AI 在八月底寫的訓練與架構程式（`train_arms.py` 8/30），GREIT 列則是 09-24 起用同一套程式訓練的網路。助理在 AI 使用期間內寫了這些程式，所以起點是 **August**。另外：runbook `NEXT_SESSION_PROMPT_20261101_收尾接手.md` 排了 11 月的 session（round 1e、format-convert、打包）。只要 11 月有任何 AI session 動到本稿，投稿時要改成 "August to November 2026" |
| A5 | 怎麼用／影響範圍：程式碼 | "wrote the analysis, scoring and figure scripts" | **CHANGE REQUIRED**：漏了**模擬資料產生與訓練程式碼**（2.7 自己寫 "the data-generation, training, scoring and figure code is in the project repository"），也漏了助理實際執行管線這件事。PLOS FAQ 明文要求揭露程式碼 |
| A6 | 影響範圍：文獻 | 沒有提到 | **CHANGE REQUIRED**：文獻檢索、篩選與選文建議（10-11 lit-review）是支援研究與內容的 AI 使用，參考文獻也是受影響的部分 |
| A7 | 影響範圍：預註冊與解讀 | "The authors … wrote and fixed the preregistration and both addenda" | **CHANGE REQUIRED（事實）**：NOTES 記錄三份都是助理起草：09-26 14:30「PREREGISTRATION_RECON.md 草稿（未確認、未雜湊）」、10-03「§11 草稿，未註冊、未附加、未雜湊」、10-11「草稿 …addendum12_DRAFT… 等 PI」→ PI「照草稿」。PI 做決定、核可、定案；"wrote" 不符合紀錄。判讀文件也是助理起草、PI 核可。PLOS 要求假說、解讀、結論是作者自己的想法，所以要寫成「助理起草，作者決定並核可」 |
| A8 | 「作者做了每個設計決定」 | "made every design decision" | **CHANGE REQUIRED（事實）**：09-26 那天在 PI 的事前授權（「檢查完直接雜湊開跑」，L527）下，助理在雜湊前改了 GN 的解法（GREIT 的 64×64 rec_model、二分法對齊 NF）和 BP 的運算子（`mk_common_gridmdl('backproj')`），當時沒有再問 PI（L578–583）。§12 的 ±1.0 邊界和它的理由也是助理在草稿裡提出、PI 照單核可的。建議寫成 "took or approved"；PI 若認為這兩項不算她核可，就要另寫 |
| A9 | 驗證方式 | "verified the outputs by re-deriving every reported number from the per-seed result files, by inspecting the plotted model inputs and outputs, and by reading and correcting the text" | **CHANGE REQUIRED（事實，除非 PI 親自回推過）**：紀錄中的逐數回推是 AI 寫的檢查腳本 `tools/check_recon_draft_numbers.py`，由助理執行（10-31 R10c），審查子代理也做了獨立重算。這三種驗證是真的，但前兩種的執行者不是作者本人。改寫時要說明是誰用什麼做的；圖的檢視（PI 10-03 指定的「先畫輸入」）和逐句閱讀可以照實歸給作者 |
| A10 | 圖 | "No figure was generated by an AI tool." | **CHANGE REQUIRED**（理由見下） |
| A11 | 圖說揭露 | 六個圖說（Fig 1–5、S1 Fig）都沒有 AI 相關文字 | **CHANGE REQUIRED（採保守讀法）** |

**A10／A11 採用的讀法與理由**。可能的讀法有兩種：(a) 窄讀：FAQ 的「AI 做圖」指 AI 生成的影像內容。它附帶的條件（不得扭曲原始研究輸出、"for illustrative purposes or to summarize results"、授權與著作權）都是在講生成的影像，AI 寫的繪圖程式則歸程式碼 FAQ 管。(b) 字面讀：現行頁的規則是「任何」AI 用於製圖都要在圖說揭露，而且沒有排除寫繪圖程式。**本檔採 (b)**，理由三個：頁面沒有定義、沒有排除；protocol 遇到不確定時要 fail closed；圖說加一句的成本近乎零。在 (a) 之下這句話字面為真，因為沒有任何影像出自生成式模型。但它緊接在 "the assistant wrote the … figure scripts … that produced every … figure" 之後，編輯照 (b) 讀，就會看到兩句互相矛盾。所以兩種讀法下這句都要換掉。只有在 (b) 之下，圖說才必須加註。PI 若明確採 (a)，A11 可降為 ADVISORY，A10 的替換句仍然需要。

### 5B. 投稿政策項目（refs/01）

| # | 要求 | 交付檔證據 | 判定 |
|---|---|---|---|
| P1 | 經費不得寫在稿件任何地方 | Acknowledgments 沒有經費；"Funding and competing interests" 節寫 "The journal collects funding and competing-interest statements in its submission system rather than in the manuscript file" | 經費：**COMPLIANT**（稿件沒有經費內容）。但見 P2 |
| P2 | 利益衝突不得寫在稿件裡 | 同一節的後半句："the corresponding author's authorship of the semi-Siamese architecture evaluated here (Section 4.6) is declared there" | **CHANGE REQUIRED：整節刪除。** refs/01 原文是 "This information should not be in your manuscript file"，經費則是 "anywhere else in the manuscript file"。這一節不只是指標，它在稿件裡陳述了利益衝突的內容，而且這個節名不在 PLOS 規定的結尾順序（Acknowledgments → References → SI captions）裡。系統欄 `27_` §Competing Interests 已經有完整聲明。§4.6 Limitations 的同一事實是科學上的限制陳述，可以保留 |
| P3 | 相關稿件聲明，並附副本 | "Related manuscript" 節："is declared as a related submission; a copy accompanies this submission"；`27_` 列出要上傳的副本 | **COMPLIANT**（內容）；括號占位見 P5 |
| P4 | 不得引用已投稿未接受的稿件 | 參考文獻 8–10 是已出版的 Ko 2021a/b、2025；伴隨研究沒有列入（"until then it is not cited"） | **COMPLIANT** |
| P4b | 「獨立單元，不依賴未接受的工作」 | "relies on none of its reported findings; its GREIT training row re-uses that study's trained networks"；2.2 自足交代訓練設定與時間 | **ADVISORY**：沿用網路屬於依賴「材料」，不是依賴「結果」，方法已經自足，處理方式合理。編輯仍可能把它讀成依賴，cover letter（`25_`）要主動說明 |
| P5 | 送出的檔案不得有占位符 | 6 個 `[MATERIAL GAP: …]`：L30、L240（preprint DOI）；L133、L244（Zenodo DOI、repository tag） | **CHANGE REQUIRED（投稿阻擋項，不是措辭問題）**：上傳前要填入或刪掉。preprint 若有 DOI 可以列為參考文獻，PLOS 收有 DOI 的 preprint；沒有的話，L30 刪掉括號、句子收在 "…declared related submissions."，L240 刪掉整個括號 |
| P6 | 最小資料集公開，並有 Data Availability Statement | "The minimal dataset (per-seed Dice for every cell, …) … deposited on Zenodo [MATERIAL GAP]" | **CHANGE REQUIRED**（同 P5：Zenodo DOI 要在投稿前取得，或提供審稿用私密連結）。內容範圍符合 refs/01（per-seed 數值、圖用數值；checkpoint 不算最小資料集，另外註明可索取） |
| P7 | 統計：軟體與版本 | 2.6 "Python 3.9, PyTorch 2.8.0, NumPy 2.0.2 and SciPy 1.13.1"；2.1 "EIDORS toolbox, v3.8" | **COMPLIANT**；ADVISORY：Python 寫完整的 3.9.6（環境紀錄 L543），並補上執行 EIDORS 的 MATLAB 版本 |
| P8 | 統計：程式碼倉庫識別碼 | 2.6 沒有；2.7 "[MATERIAL GAP: repository tag, set at submission]" | **CHANGE REQUIRED**（同 P5：填 GitHub tag 與 Zenodo 或軟體 DOI；可以在 2.6 末句加 "(code: Section 2.7)"） |
| P9 | alpha、單雙尾、檢定類型 | "two-sided Wilcoxon signed-rank test … p < 0.05"；"95% percentile bootstrap"；"two one-sided tests at α = 0.025" | **COMPLIANT** |
| P10 | n 與功效計算的輸入 | "n = 30 gives 0.89 power for a floor-sized effect at diagonal-cell variability (dz 0.60, paired, α 0.05; S1 Table)"；Table 2 MDE80 | **COMPLIANT** |
| P11 | 多重比較：校正或不校正的理由 | "No multiple-comparison correction was applied over the twenty verdicts: every verdict is of the form 'not confirmed' …" | **COMPLIANT** |
| P12 | 檢定統計量、效應量與 CI、p ≥ 0.001 報精確值、百分比給分子分母 | Table 3：W、dz、95% CI、p "0.0085"、"0.67"、"1.5e−04"；"27/30" | **COMPLIANT**（"to two significant figures" 是精確值；正文的 "p < 0.05" 是規則敘述，各格的精確值都在表裡） |

## 6. 提案替換文字（不改稿件，由 PI 確認後走 patch 鏈）

**6.1 Acknowledgments 第一段（處理 A3–A10）**：

> The authors used Claude (Anthropic; Fable 5.1, Opus 5 and Opus 5.5, accessed August to October 2026) throughout this work. The assistant wrote the simulation, data-generation, training, analysis, scoring and figure code in the project repository that produced every reported number, figure, table and supporting file, and ran it under the authors' direction; searched for and screened literature and proposed the references, which the authors selected; drafted the preregistration, its two addenda and the written interpretation of the results for the authors' decision; drafted and revised the manuscript text; ran the simulated peer-review panels recorded in the repository; and carried out the citation verification recorded there. The authors defined the research questions, decided the hypotheses, decision rules, sample size and analysis rows, approved the preregistration and each addendum before the runs they govern were started, took or approved every design decision, and approved every interpretation and conclusion. The outputs were checked by re-deriving every reported number from the per-seed result files with a separate checking script, by the authors' inspection of plots of the network's inputs and outputs, and by the authors' reading and correction of the text. No image was produced by a generative image model; every figure was plotted from the result files by the code described above.

- 只要 11 月有任何 AI session 動到本稿，"October" 就要改成 "November"。
- PI 若親自做過逐數回推，可以把第四句改回 "The authors verified the outputs by re-deriving …"。
- 可選（PLOS 不要求，核心論文版有）："The authors take full responsibility for the content of this article."
- `27_SYSTEM_FIELDS_plos.md` §AI disclosure 的貼上句要同步改。

**6.2 圖說加註（A11；Fig 1–5 與 S1 Fig 各加在圖說末尾）**：

> Plotted from the deposited result files by a script written with the AI assistant named in the Acknowledgments; no generative image model was used.

**6.3 刪除整節 "Funding and competing interests"（P2）**。利益衝突只放在系統欄（`27_` 已有）；§4.6 的限制句保留。

**6.4 占位（P5／P6／P8）**：
- L133 與 L244：填入 Zenodo DOI 與 repository tag。
- L30：preprint 有 DOI 就填入並列為參考文獻；沒有就刪括號，句子以 "…the two are declared related submissions." 結束。
- L240：沒有 preprint 時刪掉整個括號。
- `27_` L45、L74 同步。

## 7. ADVISORY 彙整（不阻擋）

1. ARS 快取 PLOS 列（2026-08-01）的放置位置與 AI 作者兩欄落後現行頁。這是外掛快取，不要改（上層 CLAUDE.md 規定）；以後 PLOS 一律以 refs/01 與現行頁為錨點。
2. Python 寫 3.9.6，並補 MATLAB 版本（P7）。
3. cover letter 要說明沿用伴隨研究的 GREIT 網路（P4b）。
4. 交付檔的 Data availability 節要和系統欄逐字一致（`27_` 已經以原句為準）。
5. 未證實的事實：10-31 那幾個「Opus 子代理」的版本；economy 是否開過（起草輪紀錄為沒開）；外部使用清單。

## 8. 待 PI 確認（protocol 必要輸入，子代理不能代答）

1. **外部使用清單**：ARS 紀錄之外是否用過任何 AI 工具（網頁版對話、翻譯、其他工具）。請答 `KNOWN(none)` 或列出清單。
2. 第 4 節的使用紀錄與事實是否無誤，特別是 A7（預註冊由助理起草）、A8（09-26 授權下的 GN／BP 改法）、A9（回推是腳本做的）。
3. 模型標籤是否照核心論文的選項 (i) 寫 "Fable 5.1, Opus 5 and Opus 5.5"。本篇的 Opus 5 有事後紀錄（L1149），比核心論文的依據更直接。
4. A10／A11 的讀法：採 (b)（本檔建議）或 (a)。
5. 截止月份：投稿前最後一個動到本稿的 AI session 落在哪個月。

## 9. 判定

```
anchor            : refs/01_JOURNAL_REQUIREMENTS_PLOSONE.md（2026-10-11）；現行頁 2026-10-31 重讀 → 一致，無漂移
ARS venue envelope: REQUIRED / HALTED / UNRESOLVED_INPUT（外部使用清單與紀錄事實待作者確認）；CONTRACT_GAP：快取 PLOS 列放置規則較窄
ai_listed_or_proposed_as_author : KNOWN(false)
ai_fabricated_or_misrepresented_primary_research_data : false（依紀錄；待 PI 確認）
CHANGE REQUIRED   : A3 模型標籤、A4 期間、A5 程式碼範圍、A6 文獻、A7 預註冊起草者、A8 設計決定措辭、A9 驗證執行者、A10 圖句、A11 圖說（保守讀法）、
                    P2 刪 Funding and competing interests 節、P5／P6／P8 六個 MATERIAL GAP
COMPLIANT         : A1、A2、P1、P3、P4、P7、P9–P12
ADVISORY          : P4b、P7 版本細節、第 7 節
```

**FINAL VERDICT: CHANGE REQUIRED — bound to `submission_PLOS_20261031/Manuscript.md` sha256 `ed42a4db720475c2f518d2c3279fb63f5f1ddcc14116aa76f057452ceef6ff7c`（docx `1278eb094cfe6313ae589b098b8753924dc54a04370bccb51fe5af7f96f5de0f`）。** 交付檔雜湊一變，本判定就失效；改稿後要以新雜湊做 scoped 重驗。
