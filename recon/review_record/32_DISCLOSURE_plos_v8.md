# 32_ AI 使用揭露與投稿政策查核：PLoS One，round 1g 交付檔 v8 重跑（ARS `academic-paper` disclosure 模式）

## 1. 標頭

| 項目 | 值 |
|---|---|
| 日期 | 2026-10-31 |
| ARS | 3.23.0（`installed_plugins.json` 讀出，與校準基準一致）；skill `academic-research-skills:academic-paper`，mode `disclosure`，selector `--venue=PLOS ONE`；`references/disclosure_mode_protocol.md` 全文已載入並依序執行，`agents/formatter_agent.md` 的 standalone disclosure 分支也照做（第 28–58 行：只回 protocol 產出的結果，不用 full-pipeline 的固定揭露句）。沒有打任何 slash command |
| 執行者 | Opus 5.5 子代理。disclosure 屬「紀錄」類，依分派表用 Opus 5 以上。**本檔之外不改任何檔案** |
| 前一版 | `26_DISCLOSURE_plos.md`（2026-10-31，CHANGE REQUIRED，綁 v7 `ed42a4db7204…`）。因為交付檔雜湊變了，26_ 的判定已失效，由本檔取代 |
| 受測交付檔 | `submission_PLOS_20261031/Manuscript.md` sha256 **`8260dd14af3f8717c332d6f472ba680808f473b2f1ed635edf48563f07982290`**（本次用 `shasum -a 256` 自己算）；`Manuscript.docx` sha256 **`246813834c6f424607c51bd761f200e177d1418dca8d58c945b83ea9fd68a4b1`** |
| 交付檔與 docx、紀錄稿的一致性 | `Manuscript.md` 和 `31_SUBMISSION_plos_v8.md` 逐位元相同（`cmp`）。docx 用 `textutil` 抽文字：Acknowledgments 段把直撇號換成彎撇號（pandoc 的排版轉換），換回來以後和 md 逐字相同；`MATERIAL GAP` 6 處；"competing" 0 處；"funding" 0 處 |
| 工作稿 | `30_DRAFT_v8.md` sha256 `9085e617e4532cd23d5f493abe1185ed2697c46bf3c4656de4a9ecc8b163e147`；Acknowledgments 句逐字包含在內 |
| v7 → v8 差異 | `diff 24_SUBMISSION_plos_v7.md 31_SUBMISSION_plos_v8.md` 只有兩處：刪掉 "Funding and competing interests" 節（標題＋內文），以及換掉 Acknowledgments 那一段。第 1–5 節、所有表格、圖說、參考文獻都逐位元沒變 |
| 揭露受測文字 | 交付檔 L252，Acknowledgments 唯一的一段（下稱 ACK）。逐字和 26_ §6.1 的提案相同（逐字串比對結果：True） |
| 作者輸入 | `revision-authority-round1g/author_event_20261031g.txt` 的 "Decisions applied" 第 1–4 項 |

## 2. 政策錨點與現行頁比對

**錨點：`refs/01_JOURNAL_REQUIREMENTS_PLOSONE.md`「AI 政策」節（2026-10-11 抄錄）。ARS 快取的 PLOS 列沒有拿來當依據。**

**現行頁重讀（2026-10-31，WebFetch `https://journals.plos.org/plosone/s/ethical-publishing-practice`，"Artificial Intelligence Tools and Technologies" 節加 FAQ，讀了兩次）：讀取成功，和 refs/01 一致，沒有漂移。** 頁面沒有標更新日期。FAQ 共八題，題目依序為：語言修飾或翻譯；cover letter；分析腳本或程式碼；"Does PLOS allow AI use in figure preparation?"；為什麼要揭露；"Will AI use disclosures negatively affect my article's review or editorial decision?"；PLOS 是否例行篩檢；編輯與審查人為何不得上傳。

| 要點 | refs/01（10-11） | 現行頁（10-31） | ARS 快取（`venue_disclosure_policies.md` PLOS 列，access 2026-08-01） |
|---|---|---|---|
| 揭露範圍 | 任何用 AI 產生或修訂內容、或支援研究的使用 | 同 | 同義 |
| 三要素 | 工具名稱、怎麼用／影響哪些部分、作者怎麼驗證 | 同（tool name(s)；how used 與影響研究或文章的哪些部分；how the user checked validity） | 同義（四欄） |
| 放在哪裡 | 正文：Methods 專節、Acknowledgments 或圖說 | 同（"in a dedicated section of the Methods, in the Acknowledgement section, or in the relevant figure legend(s)"） | ⚠️ **較窄**：Methods 優先，Acknowledgements 只限沒有 Methods 的文類 |
| AI 作者 | 不可 | 同（"AI tools cannot be listed as authors"） | ⚠️ 記為「頁面無明文」 |
| 語言修飾／翻譯 | 不必／建議 | 同 | — |
| 程式碼 | 要揭露 | 同（FAQ 答 Yes） | 未列 |
| 圖 | AI 做圖可以，但要在圖說揭露 | 同。FAQ 開頭是 "Yes, provided AI-generated content is not used to misrepresent primary research outputs"，並提到 "AI-generated figures for illustrative purposes" 和授權／著作權。**頁面沒有定義 "AI-generated figures"，也沒有區分 AI 寫的繪圖程式和 AI 生成的影像內容**（和 26_ 的觀察相同） | 未列 |
| 主張歸屬 | 作者對內容全責 | 假說、解讀、結果、結論的陳述要是作者自己的想法 | 同義 |
| 揭露影響決定 | 不影響 | 同（FAQ 答 "No"） | — |
| PLOS 用 AI 檢查 | 有 | 同（"AI use by PLOS" 節） | — |

**結論**：現行頁沒有漂移。ARS 快取在放置位置和 AI 作者兩欄仍然過時（26_ §2 已記錄）。以下一律照錨點判定。

## 3. ARS venue 軌結果信封（照 protocol 據實記錄）

- Selector `--venue=PLOS ONE`：依別名表正規化為 `PLOS`，資料庫有這一列，所以走 venue 軌。
- **Phase 2 的外部使用清單**：`external_use_inventory_confirmed = KNOWN(none)`。依據是 author_event 第 4 項：PI 接受 26_ 時沒有列出 ARS 紀錄以外的 AI 使用，紀錄為 none declared。brief 指示把它當作作者的回答。
- **`OTHER / UNCLASSIFIED`**：NOT USED（外部清單為 none），所以不觸發 halt。
- **Phase 2a**：`disclosure_outcome = REQUIRED`。
- **Phase 2a.1**：
  - `ai_listed_or_proposed_as_author = KNOWN(false)`：作者欄是三位人類（L5）。快取列沒有 AI 作者規則，protocol 對 PLOS 不強制這一項，但錨點有，所以照錄。
  - `ai_fabricated_or_misrepresented_primary_research_data = KNOWN(false)`。依據有兩項：(a) PI 接受了 ACK，而 ACK 寫明每個數字都由倉庫中的程式產生，並且用另一支檢查腳本從 per-seed 檔回推過；author_event 第 1 項說 PI 以接受該段確認 A7–A9 為事實。(b) NOTES 10-31 R10c 的回推紀錄（321 個數字，0 個無法回推）。（這是由接受段落推得的確認，不是另外寫的一句聲明；見 §7 第 5 點。）
- **Phase 2b 事實帳**：

| 欄位 | 狀態 | 值與證據 |
|---|---|---|
| tool name | KNOWN | Claude（Anthropic）；Fable 5.1、Opus 5、Opus 5.5（選項 (i)，author_event 第 1 項） |
| how used | KNOWN | ACK 第 2 句（PI 逐項確認） |
| how validated | KNOWN | ACK 第 4 句（A9，PI 確認） |
| affected parts | KNOWN | 程式碼、所有數字、圖、表、補充檔、參考文獻、預註冊與兩份 addendum、解讀、正文、模擬審查、引用查核 |
| `article_has_methods_section` | KNOWN(true) | 第 2 節 "Materials and Methods" |
| placement（快取的封閉列舉） | → `METHODS` | ⚠️ 交付檔放在 Acknowledgments，Methods 2.7 有指標句 |

- **`execution_status = HALTED`，`halt_reason = CONTRACT_GAP`**。protocol ledger rule 9 規定，無法和現行政策調和時要報 contract gap，這裡就是這種情形：快取列的封閉列舉 `true → METHODS`，比現行頁的三個通道窄。ARS 照它的可執行表不會把文字渲染到 Acknowledgments，但現行政策明文接受 Acknowledgments。這一項和 26_ 記的是同一個 CONTRACT_GAP；26_ 的 UNRESOLVED_INPUT 已由作者輸入解除，剩下的 halt 只有這一個。外掛快取不改（上層 CLAUDE.md 規定）。**合規性照錨點判定，不照快取列。**
- 本檔不渲染新的揭露文字：受測文字由 PI 定稿，本檔只判定它是否合規。

## 4. Phase 2 分類與使用紀錄（只算 RECON 這篇；照 26_ §4，作者已確認）

| 類別 | 狀態 | ACK 是否涵蓋 |
|---|---|---|
| Research assistance（文獻檢索、篩選、選文建議） | USED | 有："searched for and screened literature and proposed the references, which the authors selected" |
| Citation checking | USED | 有："carried out the citation verification recorded there" |
| Drafting（預註冊、addendum、解讀、正文） | USED | 有："drafted the preregistration, its two addenda and the written interpretation … for the authors' decision; drafted and revised the manuscript text" |
| Revision | USED | 有："revised the manuscript text" |
| Editing（含轉 Vancouver） | USED | 有：涵蓋於 "revised the manuscript text" 和程式碼（cite.py）；語言修飾依 PLOS 免揭露 |
| Analysis（模擬、資料產生、訓練、計分、執行管線） | USED | 有："wrote the simulation, data-generation, training, analysis, scoring and figure code … and ran it under the authors' direction" |
| Visual（繪圖程式；沒有生成式影像模型） | USED（只有程式碼） | 有："figure code"＋"No image was produced by a generative image model; every figure was plotted from the result files by the code described above" |
| Peer review simulation | USED | 有："ran the simulated peer-review panels recorded in the repository"（§4.5 的 "(Acknowledgments)" 指回這裡） |
| Other / unclassified | NOT USED | 外部清單 KNOWN(none) |

**模型**：Fable 5.1、Opus 5（10-11 書目 agent）、Opus 5.5（10-03 計分 session；本次 disclosure 子代理也是）。round 1g 是 Fable 5.1，10-31 執行。**期間**從 2026-08（沿用的 AI 撰寫程式碼）到 2026-10-31（本次執行）。到本檔為止沒有 11 月的 session。

## 5. 逐項判定

### 5A. AI 揭露（ACK）

**受測文字（交付檔 L252，全文）**：

> The authors used Claude (Anthropic; Fable 5.1, Opus 5 and Opus 5.5, accessed August to October 2026) throughout this work. The assistant wrote the simulation, data-generation, training, analysis, scoring and figure code in the project repository that produced every reported number, figure, table and supporting file, and ran it under the authors' direction; searched for and screened literature and proposed the references, which the authors selected; drafted the preregistration, its two addenda and the written interpretation of the results for the authors' decision; drafted and revised the manuscript text; ran the simulated peer-review panels recorded in the repository; and carried out the citation verification recorded there. The authors defined the research questions, decided the hypotheses, decision rules, sample size and analysis rows, approved the preregistration and each addendum before the runs they govern were started, took or approved every design decision, and approved every interpretation and conclusion. The outputs were checked by re-deriving every reported number from the per-seed result files with a separate checking script, by the authors' inspection of plots of the network's inputs and outputs, and by the authors' reading and correction of the text. No image was produced by a generative image model; every figure was plotted from the result files by the code described above.

**PLOS 三要素逐項**：
1. **工具名稱**：有。"Claude (Anthropic; Fable 5.1, Opus 5 and Opus 5.5 …)"，含提供者、各模型與使用期間。
2. **怎麼用／影響哪些部分**：有。程式碼及其產出（每個數字、圖、表、補充檔）、執行管線、文獻與參考文獻、預註冊與兩份 addendum、解讀、正文、模擬審查、引用查核，研究與文章兩個層次都涵蓋了。作者保留的部分也列了：研究問題、假說、判定規則、樣本數、分析列、核可、設計決定、解讀與結論。這對應頁面要求的「假說、解讀、結論是作者自己的想法」。
3. **怎麼驗證**：有。三種方法：用另一支檢查腳本從 per-seed 檔回推每個數字；作者檢視網路輸入與輸出的圖；作者逐句閱讀並修正。

| # | 要求（錨點） | 交付檔證據 | 判定 |
|---|---|---|---|
| A1 | AI 不可為作者 | 作者欄："Yen-Fen Ko¹\*, Chang-Wen Chen², Tang-Chuan Wang³" | **COMPLIANT** |
| A2 | 放在正文：Methods、Acknowledgments 或圖說 | ACK 在 Acknowledgments；Methods 2.7（L133）有指標句 "artificial-intelligence use is disclosed in the Acknowledgments" | **COMPLIANT**（照錨點；快取的較窄規則是 §3 的 CONTRACT_GAP） |
| A3 | 工具名稱 | "Fable 5.1, Opus 5 and Opus 5.5" | **COMPLIANT**：補上了 Opus 5；PI 採選項 (i)。本次 Opus 5.5 執行也在標籤內 |
| A4 | 期間 | "accessed August to October 2026" | **COMPLIANT（截至 2026-10-31）**：起點 August 涵蓋沿用的程式碼；終點 October 涵蓋 round 1g 和本次執行。⚠️ **11 月若有 round 1h 或任何 AI session 動到本稿，要改成 "August to November 2026"**（author_event 第 1 項已記載） |
| A5 | 影響範圍：程式碼 | "simulation, data-generation, training, analysis, scoring and figure code … and ran it under the authors' direction" | **COMPLIANT**：和 2.7 的 "data-generation, training, scoring and figure code" 一致，比它更完整；滿足 PLOS 的程式碼 FAQ |
| A6 | 影響範圍：文獻 | "searched for and screened literature and proposed the references, which the authors selected" | **COMPLIANT** |
| A7 | 預註冊與解讀的起草者 | "drafted the preregistration, its two addenda and the written interpretation … for the authors' decision"；"approved the preregistration and each addendum before the runs they govern were started" | **COMPLIANT**：和 NOTES 的紀錄一致，PI 確認（author_event 第 1 項） |
| A8 | 設計決定 | "took or approved every design decision" | **COMPLIANT**：涵蓋 09-26 事前授權下的 GN／BP 改法，以及 §12 的 ±1.0 邊界；PI 確認 |
| A9 | 驗證方式 | "re-deriving … with a separate checking script, by the authors' inspection of plots …, and by the authors' reading and correction of the text" | **COMPLIANT**：前兩種歸給作者的只有可以照實歸給她的兩項（看圖、讀稿）；回推寫成由檢查腳本做，沒有說是作者親手回推。檢查腳本由誰執行沒有寫，但上一句已說程式碼由助理撰寫並執行，所以不會誤導。PI 確認 |
| A10 | 圖句 | "No image was produced by a generative image model; every figure was plotted from the result files by the code described above." | **COMPLIANT**：這句和前一句（助理寫的 figure code）一致，不再自相矛盾，也符合紀錄：六個圖檔由助理撰寫的 Python 腳本畫出；Fig 1、3、4、S1 Fig 的影像內容是 EIDORS（MATLAB）的重建輸出與網路輸出；沒有用到生成式影像模型 |
| A11 | 圖說揭露 | 六個圖說（Fig 1–5、S1 Fig）沒有 AI 相關文字 | **ADVISORY（作者決定：讀法 (a)）**。PI 的決定記在 author_event：「圖是用Matlab和EIDORS完成的 不是AI製圖」→「不加」，採窄讀，圖說規則管的是 AI 生成的影像內容。助理在她決定前已告知圖檔是助理寫的 Python 腳本畫的。26_ §5A 明文說「PI 若明確採 (a)，A11 可降為 ADVISORY」。現行頁 FAQ 的措辭（"AI-generated content"、"AI-generated figures for illustrative purposes"、授權與著作權）支持 (a)，頁面也沒有明文把繪圖程式納入圖說規則。殘餘風險：編輯照字面讀 (b)。但 ACK 已明寫 "figure code" 由助理撰寫，資訊沒有被隱藏，只是放在 Acknowledgments 而不是圖說；若編輯要求，加一句圖說即可（26_ §6.2 的句子可直接用） |

### 5B. 投稿政策項目（refs/01）

| # | 要求 | 交付檔證據 | 判定 |
|---|---|---|---|
| P1 | 經費不得寫在稿件任何地方 | md 和 docx 都 grep 不到 "funding"、"grant"、"NSTC"；Acknowledgments 只有 ACK | **COMPLIANT** |
| P2 | 利益衝突不得寫在稿件裡 | "Funding and competing interests" 節已刪；md 和 docx 都 grep 不到 "competing"；"conflict of" 和 "financial" 也都是 0。"declare" 只出現在相關稿件聲明和預註冊沿用聲明（L30、62、80、86、240），都不是利益衝突聲明。§4.6 L227："The corresponding author is the original author of the semi-Siamese architecture, so this is not a neutral comparison in the sense of Boulesteix et al. [72]; preregistration of the rules before the data, and results that went against the authors' own architecture, are the study's answer to that." | **COMPLIANT**。§4.6 那句是科學限制陳述：它談的是比較的中立性（引用方法學文獻 [72]），並給了方法上的回應（預註冊、對作者不利的結果）。沒有聲明語氣，沒有 "competing／conflict／declare" 這類字，也不在聲明節裡，所以不會被讀成稿件內的 COI 聲明。利益衝突聲明只放系統欄（`27_` 和 `00_SYSTEM_FIELDS.md` §Competing Interests L42） |
| P3 | 相關稿件聲明，並附副本 | "Related manuscript" 節（L240）；套件 `08_Related_material/` | **COMPLIANT**（內容）；括號占位見 P5 |
| P4 | 不得引用已投稿未接受的稿件 | 參考文獻 8–10 是已出版的 Ko 2021（Physiol Meas）、Ko 2021（PLoS One）、Ko 2025（Curr Med Imaging）；伴隨研究沒有列入 | **COMPLIANT** |
| P4b | 「獨立單元，不依賴未接受的工作」 | 正文 L30、L240、2.2；cover letter `25_` L17："The present manuscript is an independent unit … re-uses only its trained GREIT networks, re-scored here and declared in the Methods" | **COMPLIANT**。26_ 的 ADVISORY（cover letter 要主動說明）已由 `25_` L17 處理 |
| P5 | 送出的檔案不得有占位符 | 6 個 `[MATERIAL GAP: …]`：L30（preprint DOI）、L133 ×2（Zenodo DOI、repository tag）、L240（preprint DOI）、L244 ×2（Zenodo DOI、repository tag）。docx 同樣 6 處 | **OPEN：投稿前必做，阻擋上傳**（round 1h）。這不是揭露問題，閘門 `tools/ready_gate_plos.py` 第 68 行另外追蹤，目前是 PENDING。處理方法照 26_ §6.4 |
| P6 | 最小資料集公開與 Data Availability Statement | L244 內容範圍符合 refs/01；Zenodo DOI 是占位 | **OPEN：投稿前必做**（同 P5）；內容 COMPLIANT |
| P7 | 統計：軟體與版本 | 2.6 "Python 3.9, PyTorch 2.8.0, NumPy 2.0.2 and SciPy 1.13.1"；2.1 "EIDORS toolbox, v3.8" | **COMPLIANT**；ADVISORY 照 26_：Python 寫成 3.9.6，並補 MATLAB 版本（author_event：留給 PI 決定是否放進 round 1h） |
| P8 | 統計：程式碼倉庫識別碼 | 2.7 和 Data availability 的 "[MATERIAL GAP: repository tag, set at submission]" | **OPEN：投稿前必做**（同 P5） |
| P9 | alpha、單雙尾、檢定類型 | 第 2.6 節沒有改動（和 v7 逐位元相同） | **COMPLIANT**（同 26_） |
| P10 | n 與功效計算的輸入 | 同上 | **COMPLIANT** |
| P11 | 多重比較 | 同上 | **COMPLIANT** |
| P12 | 檢定統計量、效應量與 CI、精確 p、分子分母 | 表 2–4 沒有改動 | **COMPLIANT** |

## 6. 剩下的提案

**沒有新的文字替換提案。** 26_ §6.1 與 §6.3 已原樣套用。§6.2 由 PI 拒絕，記為作者決定（A11 ADVISORY）。§6.4（占位）照 26_ 的做法，放到 round 1h。

## 7. ADVISORY 彙整（不阻擋）

1. **ARS 快取 PLOS 列過時**（放置位置、AI 作者兩欄；access 2026-08-01）。這造成 §3 的 CONTRACT_GAP。外掛快取不改；PLOS 一律以 refs/01 和現行頁為錨點。
2. **A11 讀法 (a) 的殘餘風險**：若編輯要求在圖說揭露，可以用 26_ §6.2 的句子回應。
3. **P7**：Python 寫 3.9.6，並補 MATLAB 版本。
4. **系統欄檔案的註記過時**：`27_SYSTEM_FIELDS_plos.md` 和 `00_SYSTEM_FIELDS.md` 的 §Competing Interests 標題括號寫「稿件內只留指標句」，但 round 1g 已把指標句刪了。這只是中文註記，不是要貼進系統的文字，貼上的英文段（L42）本身沒問題。下一次動這兩個檔時順手改成「稿件內不留」。兩檔的 AI disclosure 貼上句已和 ACK 逐字一致。
5. **兩項確認是由接受推得的**：外部使用清單（KNOWN(none)）和「沒有捏造資料」（KNOWN(false)），都是由「PI 接受 26_／接受 ACK」推得，PI 沒有另外各寫一句。依 brief 當作作者回答。若想讓紀錄更硬，下一次 author event 可以各寫一句。
6. **雜湊綁定**：本判定綁 v8 的位元組，round 1h 填占位後雜湊必然改變，到時要以新雜湊重跑本模式（scoped），閘門才認得。11 月動稿也要把 A4 改成 "November"。

## 8. 待 PI 確認

1. round 1h：P5、P6、P8 的六個占位（Zenodo DOI、repository tag、伴隨研究 preprint 的決定）。
2. round 1h 若在 11 月：ACK 的 "October" 改成 "November"。
3. （可選）P7 的版本細節。

26_ §8 的五項都已解決：外部清單 = none declared；A7–A9 已確認；模型標籤用選項 (i)；A10／A11 採讀法 (a)；截止月份 = October。

## 9. 判定

```
anchor            : refs/01_JOURNAL_REQUIREMENTS_PLOSONE.md（2026-10-11）；現行頁 2026-10-31 重讀 → 一致，沒有漂移
ARS venue envelope: REQUIRED / HALTED / CONTRACT_GAP（快取 PLOS 列的放置列舉 METHODS 比現行政策窄；合規性照錨點判定）；
                    UNRESOLVED_INPUT 已解除（external_use_inventory_confirmed = KNOWN(none)；A7–A9 由 PI 確認）
ai_listed_or_proposed_as_author : KNOWN(false)
ai_fabricated_or_misrepresented_primary_research_data : KNOWN(false)（PI 接受 ACK＋R10c 321/0）
COMPLIANT         : A1–A10、P1、P2、P3、P4、P4b、P7、P9–P12
ADVISORY          : A11（作者決定採讀法 (a)）、P7 版本細節、第 7 節
OPEN（投稿前必做，非揭露項）: P5／P6／P8 共 6 個 MATERIAL GAP（round 1h；閘門第 68 行另外追蹤）
otherwise         : 除了這三個占位項，其餘每一項都是 COMPLIANT
```

**FINAL VERDICT: COMPLIANT — bound to `submission_PLOS_20261031/Manuscript.md` sha256 `8260dd14af3f8717c332d6f472ba680808f473b2f1ed635edf48563f07982290` (docx `246813834c6f424607c51bd761f200e177d1418dca8d58c945b83ea9fd68a4b1`); pre-submission actions still open: P5/P6/P8 (six MATERIAL GAP placeholders, round 1h); verdict lapses on any hash change.**

AI 揭露（A1–A10）與稿件內的政策項目都合規。A11 是作者決定的 ADVISORY。這份位元組含 6 個占位，**不能照現狀上傳**。round 1h 填好占位後雜湊會變，本判定隨即失效，要以新雜湊重跑；若在 11 月動稿，A4 要改成 "November"。
