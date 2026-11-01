# 35_ AI 使用揭露與投稿政策查核：PLoS One，round 1h 交付檔 v9 重跑（ARS `academic-paper` disclosure 模式）

## 1. 標頭

| 項目 | 值 |
|---|---|
| 日期 | 2026-10-31 |
| ARS | 3.23.0（`installed_plugins.json` 讀出，與校準基準 3.23.0 一致）；skill `academic-research-skills:academic-paper`，mode `disclosure`，selector `--venue=PLOS ONE`；`references/disclosure_mode_protocol.md` 全文（478 行）已載入並依序執行，`agents/formatter_agent.md` 的 standalone disclosure 分支也照做（只回 protocol 的結果，不用 full-pipeline 的固定揭露句）。沒有打任何 slash command |
| 執行者 | Opus 5.5 子代理。disclosure 屬「紀錄」類，依分派表用 Opus 5 以上。**本檔之外不改任何檔案**；git 只用唯讀指令（`ls-remote`、`rev-parse`、`cat-file`、`ls-tree`、`hash-object`） |
| 前一版 | `32_DISCLOSURE_plos_v8.md`（COMPLIANT，綁 v8 `8260dd14af3f…`，只剩 P5／P6／P8 占位）。交付檔雜湊已變，32_ 的判定失效，由本檔取代 |
| 受測交付檔 | `../../submission_PLOS_20261031/Manuscript.md` sha256 **`c09208f04dfdec85970bd8d0535bf60fd7370fc92fc5777380058b477386e731`**；`Manuscript.docx` sha256 **`bfd5f5d8dee0b6ac7bafee7aa220f3d62a02dc895ae5fc5e9c5053de6ff62628`**（兩者都用 `shasum -a 256` 自己算，與 brief 相符） |
| 交付檔與紀錄稿、docx 的一致性 | `Manuscript.md` 和 `34_SUBMISSION_plos_v9.md` 逐位元相同（`cmp`）。docx 用 `textutil` 抽文字：ACK（彎撇號換回直撇號後）與 md L252 逐字相同；Data availability 句逐字相同；S1 Data 圖說在 docx 的 SI 清單內 |
| 工作稿 | `33_DRAFT_v9.md` sha256 `32cf6b27f35becff3abd97ae009f36337ef0b205950c28e16f733f2d9f6bd7a6`；交付檔 L133、L244、L252、L410（S1 Data 圖說）逐字包含在內 |
| v8 → v9 差異 | `diff 31_SUBMISSION_plos_v8.md 34_SUBMISSION_plos_v9.md` 只有六處：L30 與 L240 刪掉 preprint 占位；L133 與 L244 的資料句由 Zenodo 改成 S1 Data＋S1 Appendix＋GitHub tag；L252 ACK 最後一句改寫；L410 新增 S1 Data 圖說。第 1–5 節其餘文字、所有表格、圖說、參考文獻都沒變 |
| 揭露受測文字 | 交付檔 L252，Acknowledgments 唯一的一段（下稱 ACK） |
| 作者輸入 | `revision-authority-round1g/author_event_20261031g.txt`（外部使用 none declared；A7–A9 確認；圖說採讀法 (a)）；`revision-authority-round1h/author_event_20261031h.txt` 與 `answers.json`（S1 Data＋GitHub、不用 Zenodo；無 preprint；圖句改；月份 October） |

## 2. 政策錨點與現行頁比對

**錨點：`refs/01_JOURNAL_REQUIREMENTS_PLOSONE.md`（2026-10-11 抄錄）。ARS 快取的 PLOS 列沒有拿來當依據。**

### 2.1 AI 政策（ethical-publishing-practice）

**2026-10-31 重讀**（WebFetch，另用 curl 抓原始頁抽全文逐句對照）："Artificial Intelligence Tools and Technologies" 節加 FAQ。**和 refs/01 以及 32_ §2 的紀錄一致，沒有漂移。** 頁面沒有標更新日期。FAQ 仍是八題，題目與順序同 32_。

| 要點 | 現行頁原文（2026-10-31） | 與 32_／refs/01 |
|---|---|---|
| 揭露範圍 | "Any AI use to generate or revise content for a PLOS submission, or to support research reported in a PLOS article, must be clearly disclosed" | 同 |
| 三要素 | "the name(s) of any tools used," / "a description of how the tool(s) was/were used, and which aspects of the study, article contents, data, supporting files, review, or decision letter were affected, and" / "a description of how the user evaluated the validity of the tool's outputs." | 同 |
| 放在哪裡 | "disclosures should be in the body of the article, either in a dedicated section of the Methods, in the Acknowledgement section, or in the relevant figure legend(s)." | 同（ARS 快取較窄，見 §3） |
| AI 作者 | "AI tools cannot be listed as authors." | 同（ARS 快取記為頁面無明文） |
| 程式碼 | FAQ "Do I need to disclose AI use for generation or development of analysis scripts or software code?" → "Yes." | 同 |
| 圖 | FAQ 開頭 "Yes, provided AI-generated content is not used to misrepresent primary research outputs …"；"Any AI use for figure preparation should be clearly disclosed in the figure legend. Authors are responsible for checking the accuracy and validity of AI-generated figure content …" | 同。頁面仍沒有定義 "AI-generated figures"，也沒有區分 AI 寫的繪圖程式與 AI 生成的影像內容 |
| 主張歸屬 | "all statements in the article reporting hypotheses, interpretations, results, conclusions, limitations, and implications of the study represent the authors' own ideas." | 同 |
| 捏造資料 | "The use of AI tools and technologies to fabricate or otherwise misrepresent primary research data is unacceptable" | 同 |
| 揭露影響決定 | FAQ → "No." | 同 |

### 2.2 資料政策（round 1h 改了資料聲明，所以本次新讀）

讀了三頁：`/s/data-availability`（頁尾 "Webpage reorganized on December 5, 2019. The substance of the data policy has not changed unless otherwise noted."）、`/s/recommended-repositories`（無日期）、以及 data-availability 頁連到的 `/s/materials-software-and-code-sharing`（程式碼部分）。refs/01 的資料列寫「最小資料集必須公開；強烈建議存 repository（給 DOI）」，程式碼列寫「有程式碼要給 repository 識別碼」，**與現行頁一致，沒有漂移**。refs/01 末欄的作法建議（「存 Zenodo／OSF 給 DOI」「GitHub tag＋Zenodo DOI」）是當時的建議，不是 PLOS 的規定；PI 已於 10-31 改採 S1 Data＋GitHub。

**本次判定依據的原句（逐字）：**

1. 最小資料集的義務："Authors must share the “minimal data set” for their submission. PLOS defines the minimal data set to consist of the data required to replicate all study findings reported in the article, as well as related metadata and methods."
2. 公開的總要求："PLOS journals require authors to make all data necessary to replicate their study’s findings publicly available without restriction at the time of publication."
3. 最小資料集的例子："The values behind the means, standard deviations and other measures reported;" / "The values used to build graphs;" / "The points extracted from images for analysis."
4. repository 是強烈建議，不是唯一方法："PLOS strongly recommends sharing data in a repository whenever possible." 以及小節標題 "Deposition within data repository (strongly recommended)"。
5. **SI 是可接受的方法**（"Data in Supporting Information files" 小節）："Although authors are encouraged to directly deposit data in appropriate repositories, data can be included in Supporting Information files."
6. SI 的格式與大小："When including data in Supporting Information files, authors should submit data in file formats that are standard in their field and allow wide dissemination." / "Supporting Information files are published exactly as provided and are not copyedited. Each file should be less than 20 MB."
7. SI 會被 PLOS 存進 figshare："Upon publication, PLOS uploads all Supporting Information files associated with an article to the figshare repository to increase compliance with the FAIR principles (Findable, Accessible, Interoperable, Reusable)."
8. **PID 的要求附在 repository 存放這個方法底下**（同屬 "Deposition within data repository (strongly recommended)" 小節）："The Data Availability Statement must list the name of the repository or repositories as well as digital object identifiers (DOIs), accession numbers or codes, or other persistent identifiers for all relevant data."；repository 頁的準則："Repositories must assign a stable persistent identifier (PID) for each dataset at publication, such as a digital object identifier (DOI) or an accession number."
9. repository 頁的開頭句本身就允許「已隨文章提供」："All data, software and code underlying reported findings should be deposited in appropriate public repositories, unless already provided as part of the article."（data-availability 頁同義句："… unless already provided as part of a submitted article."）
10. 程式碼（code-sharing 頁）："We expect all researchers with submissions to PLOS in which author-generated code underpins the findings in the manuscript to make all author-generated code available without restrictions upon publication of the work." 以及 "Authors are encouraged to: Share their code via a repository that issues persistent identifiers, such as DOIs. … State how the code can be accessed in the Data Availability Statement of their manuscript."（PID 對程式碼是 encouraged，不是 must）
11. 不可接受的限制："Please note it is not acceptable for an author to be the sole named individual responsible for ensuring data access."

**對 brief 問題的回答**：
- **資料政策允許用 SI 檔提供最小資料集嗎？允許**（原句 5、6、9）。SI 每檔要 < 20 MB（原句 6）；`S1_Data.zip` 667,321 bytes（約 651 KB），符合。
- **除此之外，有沒有規定要求帶 PID 的 repository？沒有。** 帶 PID 的要求（原句 8）寫在「存 repository」這個方法（標為 strongly recommended）的小節裡：一旦用 repository 當資料的提供方法，DAS 就要列 repository 名稱與 PID。最小資料集若以 SI 提供，政策沒有另外要求 PID；而且 PLOS 出版時會把 SI 上傳 figshare（原句 7）。程式碼方面，帶 PID 的 repository 只是 "encouraged"（原句 10）。
- 殘餘風險見 §7 第 3 點：DAS 同時寫了 GitHub，而 GitHub 不發 PID。編輯若把 GitHub 讀成資料的存放處，可能會依原句 8 要 PID；回應方式是指出最小資料集在 S1 Data。

## 3. ARS venue 軌結果信封（照 protocol 據實記錄）

- Selector `--venue=PLOS ONE`：依別名表正規化為 `PLOS`，資料庫有這一列（`venue_disclosure_policies.md` "Venue: PLOS"，access 2026-08-01），走 venue 軌。
- **Phase 2 外部使用清單**：`external_use_inventory_confirmed = KNOWN(none)`（author_event_20261031g 第 4 項；round 1h 的 author event 沒有新增外部使用）。
- **`OTHER / UNCLASSIFIED`**：NOT USED，不觸發 halt。
- **Phase 2a**：`disclosure_outcome = REQUIRED`。
- **Phase 2a.1**：
  - `ai_listed_or_proposed_as_author = KNOWN(false)`：作者欄是三位人類（L5）。protocol 對 PLOS 不強制這一項（快取列沒有 AI 作者規則），但錨點與現行頁都有，所以照錄。
  - `ai_fabricated_or_misrepresented_primary_research_data = KNOWN(false)`：觸發條件成立（有使用紀錄影響主要資料、結果與 S1 Data 這個補充資料檔）。依據同 32_：PI 接受 ACK 時確認了 A7–A9（author_event 1g 第 1 項），加上 R10c 回推紀錄（321 個數字，0 個無法回推）。round 1h 的資料變動只是重新打包：S1 Data 由 `tools/pack_submission_plos.py` 從結果檔組成（README 寫 "nothing typed by hand"），且 101 檔中 97 檔與 GitHub tag 內的 blob 逐位元相同（§5B P6），沒有新的資料生成。
- **Phase 2b 事實帳**：

| 欄位 | 狀態 | 值與證據 |
|---|---|---|
| tool name | KNOWN | Claude（Anthropic）；Fable 5.1、Opus 5、Opus 5.5（author_event 1g 第 1 項，選項 (i)） |
| how used | KNOWN | ACK 第 2 句（PI 逐項確認） |
| how validated | KNOWN | ACK 第 4 句（A9，PI 確認） |
| affected parts | KNOWN | 程式碼、所有數字、圖、表、補充檔（含 S1 Data）、參考文獻、預註冊與兩份 addendum、解讀、正文、模擬審查、引用查核 |
| `article_has_methods_section` | KNOWN(true) | 第 2 節 "Materials and Methods"（L46） |
| placement（快取的封閉列舉） | → `METHODS` | ⚠️ 交付檔放在 Acknowledgments，Methods 2.7（L133）有指標句 |

- **`execution_status = HALTED`，`halt_reason = CONTRACT_GAP`**：和 26_／32_ 記的是同一個。依 protocol ledger rule 9，快取列的封閉列舉 `true → METHODS` 比現行頁的三個通道（Methods 專節、Acknowledgement、圖說）窄，可執行表和現行政策無法調和，所以報 contract gap。ARS 照它的表不會把文字渲染到 Acknowledgments，但現行政策明文接受。外掛快取不改（上層 CLAUDE.md 規定）。**合規性照錨點與現行頁判定，不照快取列。**
- 本檔不渲染新的揭露文字：受測文字由 PI 定稿，本檔只判定是否合規。

## 4. Phase 2 分類與使用紀錄（只算 RECON 這篇；與 32_ §4 相同，round 1h 沒有改變分類）

| 類別 | 狀態 | ACK 是否涵蓋 |
|---|---|---|
| Research assistance（文獻檢索、篩選、選文建議） | USED | 有："searched for and screened literature and proposed the references, which the authors selected" |
| Citation checking | USED | 有："carried out the citation verification recorded there" |
| Drafting（預註冊、addendum、解讀、正文） | USED | 有："drafted the preregistration, its two addenda and the written interpretation … for the authors' decision; drafted and revised the manuscript text" |
| Revision | USED | 有："revised the manuscript text"（round 1h 的資料句與圖句改寫也在此內） |
| Editing（含轉 Vancouver） | USED | 有：涵蓋於 "revised the manuscript text" 與程式碼；語言修飾依 PLOS 免揭露 |
| Analysis（模擬、資料產生、訓練、計分、執行管線；S1 Data 打包） | USED | 有："wrote the simulation, data-generation, training, analysis, scoring and figure code … that produced every reported number, figure, table and supporting file, and ran it under the authors' direction"。S1 Data 由助理寫的打包腳本組成，屬 "supporting file" |
| Visual（繪圖程式；沒有生成式影像模型） | USED（只有程式碼） | 有："figure code"＋"No image was produced by a generative image model; every figure was plotted by the code described above from the data, checkpoint and result files." |
| Peer review simulation | USED | 有："ran the simulated peer-review panels recorded in the repository" |
| Other / unclassified | NOT USED | 外部清單 KNOWN(none) |

**模型**：Fable 5.1、Opus 5、Opus 5.5（本次 disclosure 子代理也是 Opus 5.5，已在標籤內）。round 1h 是 Fable 5.1，10-31 執行。**期間**從 2026-08 到 2026-10-31（本次執行）。到本檔為止沒有 11 月的 session。

## 5. 逐項判定

### 5A. AI 揭露（ACK）

**受測文字（交付檔 L252，全文）**：

> The authors used Claude (Anthropic; Fable 5.1, Opus 5 and Opus 5.5, accessed August to October 2026) throughout this work. The assistant wrote the simulation, data-generation, training, analysis, scoring and figure code in the project repository that produced every reported number, figure, table and supporting file, and ran it under the authors' direction; searched for and screened literature and proposed the references, which the authors selected; drafted the preregistration, its two addenda and the written interpretation of the results for the authors' decision; drafted and revised the manuscript text; ran the simulated peer-review panels recorded in the repository; and carried out the citation verification recorded there. The authors defined the research questions, decided the hypotheses, decision rules, sample size and analysis rows, approved the preregistration and each addendum before the runs they govern were started, took or approved every design decision, and approved every interpretation and conclusion. The outputs were checked by re-deriving every reported number from the per-seed result files with a separate checking script, by the authors' inspection of plots of the network's inputs and outputs, and by the authors' reading and correction of the text. No image was produced by a generative image model; every figure was plotted by the code described above from the data, checkpoint and result files.

和 v8 相比只改最後一個子句（"plotted from the result files by the code described above" → "plotted by the code described above from the data, checkpoint and result files"），其餘逐字相同。

**PLOS 三要素**：工具名稱、怎麼用／影響哪些部分、怎麼驗證，三項都在（理由同 32_ §5A，文字沒變）。

| # | 要求（錨點） | 交付檔證據 | 判定 |
|---|---|---|---|
| A1 | AI 不可為作者 | 作者欄："Yen-Fen Ko¹\*, Chang-Wen Chen², Tang-Chuan Wang³" | **COMPLIANT** |
| A2 | 放在正文：Methods、Acknowledgments 或圖說 | ACK 在 Acknowledgments（L250–252）；Methods 2.7（L133）指標句 "artificial-intelligence use is disclosed in the Acknowledgments" 仍在（round 1h 改寫 L133 時保留了） | **COMPLIANT**（照錨點；快取較窄規則是 §3 的 CONTRACT_GAP） |
| A3 | 工具名稱 | "Fable 5.1, Opus 5 and Opus 5.5" | **COMPLIANT**：round 1h（Fable 5.1）與本次（Opus 5.5）都在標籤內 |
| A4 | 期間 | "accessed August to October 2026" | **COMPLIANT（截至 2026-10-31）**：round 1h 與本次都在 10-31。⚠️ 11 月若有任何 AI session 動到本稿，要改成 "August to November 2026"（answers.json `"month": "October"`） |
| A5 | 影響範圍：程式碼 | "simulation, data-generation, training, analysis, scoring and figure code … and ran it under the authors' direction" | **COMPLIANT**：滿足 PLOS 程式碼 FAQ。S1 Data 的打包腳本屬這段程式碼，其產物屬 "supporting file" |
| A6 | 影響範圍：文獻 | "searched for and screened literature and proposed the references, which the authors selected" | **COMPLIANT** |
| A7 | 預註冊與解讀的起草者 | 同 32_，文字未變 | **COMPLIANT**（PI 確認，author_event 1g 第 1 項） |
| A8 | 設計決定 | "took or approved every design decision" | **COMPLIANT**（同 32_） |
| A9 | 驗證方式 | 同 32_，文字未變 | **COMPLIANT**（同 32_） |
| A10 | 圖句 | "No image was produced by a generative image model; every figure was plotted by the code described above from the data, checkpoint and result files." | **COMPLIANT**。改寫照 addendum_v8 NEW-1g-1：該條指出 Fig 1 與 Fig 3 讀資料集檔（`data/*/dataset.mat`），Fig 4 與 S1 Fig 讀資料集與 seed-0 checkpoint、在畫圖時算網路預測，只有 Fig 2 與 Fig 5 讀結果檔。新句的 "data, checkpoint and result files" 三類正好涵蓋這三種來源，消除了 v8 的過度窄指。新句也沒有用 NEW-1g-1 建議中的 "deposited"，這反而更準：資料集檔與 checkpoint 沒有存放（checkpoint 是向通訊作者索取，L133／L244）。"the code described above" 仍指回前句助理寫的 figure code，所以和第二句一致，不會自相矛盾。和 `00_SYSTEM_FIELDS.md`／`27_` §AI disclosure 的貼上句逐字相同（兩檔逐位元相同） |
| A11 | 圖說揭露 | 六個圖說（Fig 1–5、S1 Fig）沒有 AI 相關文字 | **ADVISORY（作者決定：讀法 (a)）**。理由同 32_ §5A：PI 決定「圖是用Matlab和EIDORS完成的 不是AI製圖」→「不加」；現行頁 FAQ 的措辭（"AI-generated content"、"AI-generated figures for illustrative purposes"、"AI-generated figure content"）支持窄讀，頁面沒有明文把繪圖程式納入圖說規則。**改寫後的圖句仍符合讀法 (a)**：它明說沒有任何影像出自生成式影像模型，並如實寫出每張圖都是助理寫的程式從資料、checkpoint、結果檔畫出，所以 FAQ 擔心的 AI 生成影像內容不存在，而 AI 寫繪圖程式這件事在 Acknowledgments 公開了（程式碼 FAQ 要求的揭露）。殘餘風險不變：編輯若照字面讀 (b)，加一句圖說即可（26_ §6.2 的句子可用） |

### 5B. 投稿政策項目（refs/01，加上本次新讀的資料政策）

| # | 要求 | 交付檔證據 | 判定 |
|---|---|---|---|
| P1 | 經費不得寫在稿件任何地方 | md 與 docx 的 "funding"、"grant"、"NSTC" 都是 0 | **COMPLIANT** |
| P2 | 利益衝突不得寫在稿件裡 | md 與 docx 的 "competing"、"conflict of"、"financial" 都是 0；§4.6 L227 的科學限制句不變（理由同 32_ P2）。系統欄 `00_SYSTEM_FIELDS.md` L41 標題註記已改成「稿件內不寫，round 1g 已刪指標節」（32_ §7 第 4 點已處理） | **COMPLIANT** |
| P3 | 相關稿件聲明，並附副本 | "Related manuscript" 節（L240），preprint 占位已刪；套件 `08_Related_material/Companion_core_paper_SciRep_submission.docx` 存在；cover letter L17 "a copy is attached" | **COMPLIANT** |
| P4 | 不得引用已投稿未接受的稿件 | 參考文獻未變；伴隨研究沒有列入。L30 刪了 preprint 占位後，伴隨研究只以 "declared related submissions" 提及，沒有引用編號 | **COMPLIANT** |
| P4b | 「獨立單元，不依賴未接受的工作」 | 正文 L30、L240、2.2 未改語意；cover letter L17 "The present manuscript is an independent unit …" | **COMPLIANT** |
| P5 | 送出的檔案不得有占位符 | md 與 docx 的 "MATERIAL GAP" 都是 0、"Zenodo" 都是 0、"preprint" 都是 0。非引用編號的方括號只剩 95% 信賴區間（如 "[+0.07, +0.32]"、"[95% CI]"），md 與 docx 清單相同，沒有任何占位 | **COMPLIANT**（32_ 的 OPEN 已解除） |
| P6 | 最小資料集公開與 Data Availability Statement | L244（＝系統欄 `00_SYSTEM_FIELDS.md` L45 逐字）："The minimal dataset (per-seed Dice for every cell, the aggregated results file, gate and seed-0 diagnostic files) is supplied as S1 Data, and the four preregistration states with their hash file as S1 Appendix; the same data and the data-generation, training, scoring and figure code are in the project repository (github.com/yfko/sunet-decoder-branch-eit) under the tagged release v1.2-recon-submission. Model checkpoints are available from the corresponding author." 查核：(1) `S1_Data.zip` 存在，667,321 bytes（< 20 MB，§2.2 原句 6）；解開後 101 檔，與套件內 `S1_Data/` 目錄 `diff -r` 相同；內容有 per-seed CSV、`recon_results.json`、`recon_delta_ci.json`、三個閘門 JSON、seed-0 診斷、run 紀錄、預註冊四態與雜湊檔、README（逐檔 SHA-256），涵蓋 DAS 列的項目。(2) S1 Data 圖說在 SI 清單（md L410、docx 同）。(3) 101 檔中 97 檔在 tag `v1.2-recon-submission` 的樹內有逐位元相同的 blob（`git hash-object` 比對），沒有對上的 4 檔是 README 與 S3 Table 的三個副本（打包產物；S3 Table 本身另有 SI 檔）。(4) 格式是 CSV／JSON／Markdown，符合 "file formats that are standard in their field"。(5) 依 §2.2，SI 是可接受的最小資料集提供方法，政策沒有另外要求 PID | **COMPLIANT**（32_ 的 OPEN 已解除）。ADVISORY 見 §7 第 3、4 點 |
| P7 | 統計：軟體與版本 | 2.6 "Python 3.9, PyTorch 2.8.0, NumPy 2.0.2 and SciPy 1.13.1"；2.1 "EIDORS toolbox, v3.8"（未變） | **COMPLIANT**；ADVISORY 同 32_：Python 寫成 3.9.6、補 MATLAB 版本（PI 未選入 round 1h） |
| P8 | 統計：程式碼倉庫識別碼 | L133 與 L244："(github.com/yfko/sunet-decoder-branch-eit) under the tagged release v1.2-recon-submission"。`git ls-remote --tags origin v1.2-recon-submission` → `aa3feb7207f26c36ac8f81808274edbe04031e19 refs/tags/v1.2-recon-submission`（annotated tag），本地解引用到 commit `02c720ee76779e9df317c05135edc0337c01e9d3`，與 `origin/main` 及 answers.json 的 02c720e 相同。tag 頁與 tag zip 未登入 HTTP 200（公開，不需帳號，符合 code-sharing 頁 "without creating user accounts" 的精神）；tag 內有 `LICENSE` 與 `LICENSE-DATA` | **COMPLIANT**（32_ 的 OPEN 已解除）。帶 PID 的程式碼 repository 是 encouraged，不是 required（§2.2 原句 10） |
| P9 | alpha、單雙尾、檢定類型 | 第 2.6 節未變 | **COMPLIANT** |
| P10 | n 與功效計算的輸入 | 同上 | **COMPLIANT** |
| P11 | 多重比較 | 同上 | **COMPLIANT** |
| P12 | 檢定統計量、效應量與 CI、精確 p、分子分母 | 表 2–4 未變 | **COMPLIANT** |

## 6. 剩下的提案

**沒有文字替換提案。** 32_ 的 P5／P6／P8 已由 round 1h 處理；A10 圖句已照 NEW-1g-1 改寫；A11 維持作者決定。

## 7. ADVISORY 彙整（不阻擋）

1. **ARS 快取 PLOS 列過時**（放置位置、AI 作者兩欄；access 2026-08-01），造成 §3 的 CONTRACT_GAP。外掛快取不改；PLOS 一律以 refs/01 與現行頁為錨點。
2. **A11 讀法 (a) 的殘餘風險**：編輯若要求圖說揭露，可以用 26_ §6.2 的句子回應。
3. **DAS 中 GitHub 沒有 PID**：政策對以 SI 提供的最小資料集不要求 PID（§2.2），但 DAS 同時寫了 "the same data … are in the project repository"。編輯若把 GitHub 讀成資料的存放處，可能依原句 8 要求 DOI。到時有兩種回應：(a) 指出最小資料集是 S1 Data，PLOS 出版時會把它存進 figshare；(b) 把 tag 存檔到發 DOI 的 repository。(b) 與 PI 的「Zenodo 不使用」決定相反，所以只在編輯要求時才考慮。原句 9（"unless already provided as part of the article"）支持 (a)。
4. **圖的底層像素值不在 S1 Data**：Fig 1、3、4、S1 Fig 的影像是從模擬資料集檔與 seed-0 checkpoint 畫出的（NEW-1g-1），這些檔沒有放進 S1 Data（checkpoint 向通訊作者索取）。圖上印出的數字（標準差比、預測峰值與背景中位數）在 `scale_check.json`、`shift_inputs.json`、`loro_preds_seed0.json`、`mixed_ps_preds_seed0.json` 裡；所有報告的統計結果都可以從 per-seed 檔重現。資料集是模擬的，可以用 tag 內的程式重新產生。政策的例子有 "The values used to build graphs"，而且 "it is not acceptable for an author to be the sole named individual responsible for ensuring data access"（原句 11）。checkpoint 依 refs/01 不屬於最小資料集，這兩點目前都不構成不合規。但編輯若要影像圖的底層值，可能會問。這是資料政策的判斷，不是揭露項；要不要預先補，由 PI 決定。
5. **P7**：Python 寫成 3.9.6，並補 MATLAB 版本（同 32_）。
6. **兩項確認是由接受推得的**（外部清單 KNOWN(none)、沒有捏造資料 KNOWN(false)），同 32_ §7 第 5 點。
7. **雜湊綁定**：本判定綁 v9 的位元組；任何改動都會使雜湊改變，本判定隨即失效，要重跑。11 月動稿也要把 A4 改成 "November"。

## 8. 待 PI 確認

1. 投稿若在 11 月且有 AI session 動到稿：ACK 的 "October" 改成 "November"（屆時要重跑本模式）。
2. （可選）P7 版本細節。
3. （可選）§7 第 3、4 點：GitHub 的 PID 風險、影像圖底層值。現在不用處理，編輯問到再處理也可以。

32_ §8 的第 1 項（P5／P6／P8 占位）已由 round 1h 解決，第 2 項（月份）仍沿用 October。

## 9. 判定

```
anchor            : refs/01_JOURNAL_REQUIREMENTS_PLOSONE.md（2026-10-11）；現行頁 2026-10-31 重讀
                    → AI 政策頁沒有漂移；資料政策三頁（data-availability、recommended-repositories、
                      materials-software-and-code-sharing）與 refs/01 一致，沒有漂移
data policy       : SI 可作為最小資料集的提供方法（"data can be included in Supporting Information files"；
                    每檔 < 20 MB）；帶 PID 的要求只附在 repository 存放這個方法下；程式碼帶 PID 的 repository 是 encouraged
ARS venue envelope: REQUIRED / HALTED / CONTRACT_GAP（快取 PLOS 列的放置列舉 METHODS 比現行政策窄；合規性照錨點判定）
ai_listed_or_proposed_as_author : KNOWN(false)
ai_fabricated_or_misrepresented_primary_research_data : KNOWN(false)
COMPLIANT         : A1–A10、P1–P12（含 P4b；P5／P6／P8 已由 round 1h 解除）
ADVISORY          : A11（作者決定讀法 (a)，改寫後的圖句仍符合）、§7 第 1–7 點
OPEN              : 無
verification      : tag v1.2-recon-submission 在 origin（aa3feb72… → commit 02c720ee…）；S1_Data.zip 667,321 bytes；
                    S1 Data 圖說在 SI 清單；"Zenodo" 與 "MATERIAL GAP" 在 md 與 docx 都是 0 次
```

**FINAL VERDICT: COMPLIANT — bound to `submission_PLOS_20261031/Manuscript.md` sha256 `c09208f04dfdec85970bd8d0535bf60fd7370fc92fc5777380058b477386e731` (docx `bfd5f5d8dee0b6ac7bafee7aa220f3d62a02dc895ae5fc5e9c5053de6ff62628`); no open items; A11 advisory by author decision (reading (a)); verdict lapses on any hash change or on any November AI session that touches the manuscript.**

AI 揭露（A1–A10）與稿件內的政策項目（P1–P12）都合規，32_ 留下的三個占位項已解除。A11 是作者決定的 ADVISORY。本判定只涵蓋 AI 揭露與 refs/01 列出的稿件內政策項目，不等於整個投稿套件已經就緒；就緒要看閘門 `tools/ready_gate_plos.py` 的輸出。
