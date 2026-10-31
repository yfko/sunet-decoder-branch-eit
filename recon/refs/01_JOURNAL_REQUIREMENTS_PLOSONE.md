# PLOS One — 投稿規範（R2 查證紀錄）

**查證日期 2026-10-11，來源為 journals.plos.org/plosone 官網各頁（內建瀏覽器逐頁讀取，原文引號內為頁面文字）**
- 稿件規格：`journals.plos.org/plosone/s/submission-guidelines`
- 發表判準：`journals.plos.org/plosone/s/criteria-for-publication`
- 審稿流程：`journals.plos.org/plosone/s/editorial-and-peer-review-process`
- 期刊資訊與時程：`journals.plos.org/plosone/s/journal-information`
- 圖檔：`journals.plos.org/plosone/s/figures`
- 資料政策：`journals.plos.org/plosone/s/data-availability`；程式碼：`…/s/materials-software-and-code-sharing`
- 出版倫理與 AI 政策：`journals.plos.org/plosone/s/ethical-publishing-practice`（Artificial Intelligence Tools and Technologies 節）
- APC：`plos.org/fees`

用途：第三級備案篇（純模擬 RECON 篇）的目標刊之一（界線條款 §三備案表：PM 45／PLoS One 60），也是核心論文的備援刊。**Physiological Measurement 不重查**，用上層 `JOURNAL_PhysiolMeas.md`（2026-09-17 查證）。

---

## 發表判準（criteria-for-publication，七條；決定不看「significance」）

1. 原創研究；2. 未在他處發表；3. 實驗與統計達高技術標準、描述足以重複；4. 結論被資料支持（「Submissions will be rejected if the interpretation of results is unjustified or inappropriate, so authors should avoid overstating their conclusions」）；5. 英文清楚（**不做 copyedit**，語言不合會退）；6. 倫理；7. 報告指引與資料可得性。

- **負面與 null 結果明文在範圍內**：「In keeping with our mission to publish all valid research, we consider negative and null results」；「replication studies, negative and null results are all in scope」。
- **重複研究要給理由**：「If a submitted study replicates or is very similar to previous work, authors must provide a sound scientific rationale … Submissions that replicate or are derivative of existing work will likely be rejected if authors do not provide adequate justification」。→ 第三級篇延伸核心論文到另外兩個重建器，開頭就要寫清楚它問的是原著點名而核心論文沒問的問題。
- 不收：review、假說／提案文、意見、方法以外的二手文獻。收 Registered Reports（Protocol 與 Research Article 兩種）、方法／軟體／工具文、系統性回顧、protocols。

## 硬規定與格式（submission-guidelines）

| 項目 | 規定 | 原文 | 本篇要注意 |
|---|---|---|---|
| **長度** | **無限制**（字數、圖數、補充材料都無上限） | "Manuscripts can be any length. There are no restrictions on word count, number of figures, or amount of supporting information." | 但「present and discuss your findings concisely」 |
| 檔案 | DOC／DOCX／RTF；LaTeX 要交 PDF | — | pandoc 出 docx 即可 |
| 排版 | **雙行距**；**頁碼＋連續行號**；最多 3 層標題；不可多欄；**不可腳註**；英文 | "Manuscript text should be double-spaced" / "Include page numbers and line numbers … continuous" | 轉檔程式要加雙行距與行號 |
| **標題** | 全標 **≤ 250 字元**；**短標 ≤ 100 字元**；句首大寫（sentence case）；避免專業縮寫 | "Full title 250 characters … Short title 100 characters" | 要另給短標 |
| **摘要** | **≤ 300 字**；寫目的、怎麼做（不含方法細節）、主要結果與意義；**不可引用**；盡量不用縮寫；系統另填一次 | "Not exceed 300 words" / "Abstracts should not include: Citations" | 比 Sci Rep 的 200 寬 |
| 結構 | 必要順序：Title page → Abstract → Introduction；中段 Methods／Results／Discussion／Conclusions 順序與名稱自由；結尾必要順序：**Acknowledgments → References → Supporting information captions** | "The following elements are required, in order" | IMRaD 合規；Methods 在前亦可 |
| 圖 | **不放進稿件檔**，每圖獨立檔；**圖說放在第一次引用的段落之後**（不是文末）；標 **"Fig 1"**（縮寫 Fig）；檔名對應 Fig1.tif | "Figure captions must be inserted … immediately following the paragraph in which the figure is first cited" | 與 Sci Rep（圖說集中在文末）相反 |
| 表 | **放在第一次引用的段落之後**（在稿件檔內）；標題在表上、註在表下 | "Place each table in your manuscript file directly after the paragraph in which it is first cited" | 同上 |
| 補充材料 | 另傳；每檔 **< 20 MB**；名稱含 "S" 與編號（S1 Table、S1 Appendix…）；說明列在稿件檔末；全部送審 | — | S9 類表格可放 S1 Table |
| 縮寫 | 首次出現定義；非標準縮寫至少出現三次才用 | — | — |
| 參考文獻 | **Vancouver（ICMJE）**；文內**方括號**編號；**前六位作者後 et al.**；期刊縮寫用 NCBI；DOI 寫在末尾 "doi: 10.xxxx"（不可縮寫、不可 URL） | "PLOS uses the numbered citation (citation-sequence) method and first six authors, et al." | **cite.py 要加 Vancouver 渲染**（現有 Nature 式）|
| **可引用的來源** | 已發表或已接受；**有 DOI 或 arXiv URL 的 preprint**。**不可引用已投稿未接受的稿件**（"Do not cite … manuscripts that have been submitted but not yet accepted"）；不可 "data not shown"；不可引用撤稿文（除非討論其歷史並註明） | — | ⚠️ **核心論文若仍在 Sci Rep 審查中，不能列入參考文獻**；要先掛 preprint（有 DOI）或等接受。見下「相關稿件」 |
| 統計 | Methods 要有統計分析一節：軟體名稱與版本、程序細節、**程式碼倉庫識別碼**；交代設計（within/between）、alpha、樣本數與其計算（功效、效應量、alpha 的輸入）、多重比較校正或不校正的理由、檢定單雙尾與類型；結果報檢定統計量與自由度、效應量與 CI、**p ≥ 0.001 報精確值**、百分比給分子分母；圖要忠實呈現分布、避免 3D | "Report exact p-values for all values greater than or equal to 0.001" | RESULTS §10 的 W／CI／SD 正好補這一條；地板規則的「功效」要照核心論文 §2.4 的寫法交代 |
| 資料 | **最小資料集必須公開**（平均值背後的數值、畫圖用的數值）；強烈建議存 repository（給 DOI）；Data Availability Statement 在投稿系統填 | "Authors must share the 'minimal data set'" | per_seed.csv 與 recon_results.json 存 Zenodo／OSF 給 DOI；checkpoint 不是最小資料集 |
| 程式碼 | 有程式碼要給 repository 識別碼；軟體為主的稿另有規定（開源授權、GitHub 等存檔） | "Provide the repository identifier for any code used" | GitHub tag ＋ Zenodo DOI |
| 作者 | 每位作者至少一項 **CRediT** 貢獻（系統填）；通訊作者 **ORCID** 必填；所有作者投稿時會收到確認信 | — | AUTHORS_registry 有 ORCID |
| **經費** | **不寫在稿件裡**，只在系統的 Financial Disclosure 填（含是否參與設計、分析、發表決定） | "Do not include funding sources in the Acknowledgments or anywhere else in the manuscript file" | 與 Sci Rep 相反 |
| **利益衝突** | **不寫在稿件裡**，系統填 | "This information should not be in your manuscript file" | 同上 |
| Cover letter | 另傳，**≤ 1 頁**：貢獻摘要、與既有文獻的關係、文章類型、與 PLOS 的先前互動、建議 Academic Editor、反對的審查人；**不可**在信裡要求減免 APC | — | — |
| 建議編輯 | 投稿時建議 Academic Editor；不可建議近期合作者或同機構 | — | — |
| Preprint | 鼓勵；不影響審稿；可從投稿系統轉 bioRxiv／medRxiv | — | 核心論文與本篇都可先掛 |

## 相關稿件與「分篇」（本篇最要小心的一條）

- 投稿時必須聲明有無相關稿件在審或已發表；**有的話要附一份副本**，審查人會評估重疊（"If related work has been submitted to PLOS One or elsewhere, authors must include a copy with the submitted article. Reviewers will be asked to comment on the overlap"）。
- **「每篇必須是獨立單元，不得依賴尚未被接受的工作」**（"Each submission to PLOS One must be written as an independent unit and should not rely on any work that has not already been accepted for publication"）；**不收分成 "parts" 的稿**；不必要的分篇會被要求合併。
- → 對第三級篇的意思：（a）核心論文（Sci Rep 審查中）要先成為 preprint 或已接受，才能引用與依賴；（b）本篇的方法要自足（訓練協定、端點、度量都要在本篇寫完，不能只寫「見核心論文」）；（c）cover letter 要主動說明與核心論文的關係與界線（界線條款 §二／§三 的句子）。
- 爭議稿（disputing published work）會邀被爭議作者署名審查——本篇不是。

## AI 政策（ethical-publishing-practice，Artificial Intelligence Tools and Technologies 節；2026-10-11 現行頁）

- AI 可用於撰寫或修訂，**不可列為作者**；作者對內容（含引用、方法描述）全責。
- **任何**用 AI 產生或修訂內容、或支援研究的使用都要揭露；揭露放在**正文**：Methods 的專節、Acknowledgments、或相關圖說。揭露三要素：**工具名稱、怎麼用／影響哪些部分、作者如何驗證輸出的有效性**。
- FAQ：語言修飾（拼字、文法、清晰化）**不必**揭露；翻譯建議揭露；cover letter 不必；**產生或發展分析腳本／程式碼要揭露**；AI 做圖可以但要在圖說揭露。
- 審查人與編輯**不得**把稿件上傳 AI 工具（保密）；AI 不得當審查人。
- 揭露不影響決定（FAQ 明文）。PLOS 自己用 AI 做投稿檢查。
- → 本篇的 §2.9 式聲明可沿用核心論文的寫法，但要加「如何驗證輸出」一句（核心論文 Sci Rep 版未必有），且分析腳本的 AI 參與要寫。

## 圖檔（figures；**接受前不強制**：「PLOS One waives all formatting requirements until your manuscript has received a provisional Editorial Accept decision」）

| 項目 | 規定 |
|---|---|
| 格式 | **TIFF 或 EPS**（TIFF 較穩） |
| 尺寸 | 寬 6.68–19.05 cm（789–2250 px @300 dpi）；高 ≤ 22.23 cm（2625 px）；對齊文欄寬 ≤ 13.2 cm |
| 解析度 | 300–600 dpi；小字多的圖用 600 |
| 檔案大小 | ≤ 10 MB；TIFF 用 LZW、攤平、無 alpha channel、單頁 |
| 字型 | 圖內只用 Arial、Times、Symbol，8–12 pt；EPS 要嵌字或轉外框 |
| 內容 | 圖內不放作者、標題、圖號；多面板合成單一檔；RGB 8-bit 或灰階；留 2 pt 白邊；方向照出版 |
| 工具 | PLOS 的 NAAS 可檢查與轉檔 |

→ 現有 figstyle.py 出 PDF＋PNG；投 PLOS 時要加 TIFF（LZW、300–600 dpi）輸出。

## 審稿流程與時程（editorial-and-peer-review-process；journal-information 的 Journal Timings）

- 流程：內部初檢（利益衝突、政策、經費、資料）→ Academic Editor 評估是否送外審 → 單盲外審（審查人 10 天）→ Reject／Major／Minor／Accept；兩層接受（editorial accept 後再做格式技術檢查才 formal accept）。
- 可選公開審稿歷程；審查人可署名；可要求轉 PLOS 其他刊；上訴只限事實錯誤或利益衝突，書面。
- **時程（中位數天數，2023 上半年欄）**：首次編輯決定 17、首次決定 45、最終決定 87、接受 188、刊出 204、接受到刊出 10。**未經外審退稿 30.8%，接受率 30.7%**（2020 年 48%→2023 年 31%，逐年下降）。
- 決定「不看新穎性」（"based on scientific rigor, regardless of novelty"）。

## APC 與授權（plos.org/fees，2026-10-11 頁面）

- 費用頁第一組（PLOS ONE）：**Research Article 類 "All other articles" USD 2,477**；Registered Report Protocol 1,852、Registered Report Article 1,088、Lab Protocols 1,536、Study Protocols 2,477。接受時付款，以投稿日費率計。⚠️ 頁面把各刊的費用疊在同一頁，USD 2,477 這一組的歸屬是依排版判讀，**投稿時在系統再確認**。
- 台灣不在 Research4Life；Publication Fee Assistance 要證明財務需要；機構合作夥伴可免——查 CMU 是否在 Institutional Partners 名單。
- CC BY；作者保留著作權。

## Registered Reports（submission-guidelines 的 Guidelines for Specific Study Types）

- PLOS One 收 **Registered Report Protocol**（先投設計，接受後才收資料）與 **Registered Report Research Article**（報告全部計畫內分析、說明所有偏離；可含探索性分析）。
- 本篇的預註冊是**實驗室內部的雜湊檔**，不是 PLOS 接受過的 RR Protocol，所以**以一般 Research Article 投**，在 Methods 寫預註冊（雜湊、日期、偏離、解盲後 addendum），和核心論文的做法一樣。RR 的格式要求（「report the results of all planned analyses and, if relevant, detail and justify all deviations from the protocol; may also contain exploratory, unplanned analyses」）是我們本來就在做的事，可在 cover letter 點出。

## 官網未明定的項目

- 關鍵詞數：投稿系統可能要填，頁面未寫。
- 參考文獻數：無上限。
- 圖表數：無上限。
- 主文結構的小標數：只限 3 層。
- Data Availability Statement 的字數：未限。

## 第三級篇投 PLOS One 前要做的清單（依序）

1. **核心論文的可引用性**：等 Sci Rep 接受，或先掛 preprint 取得 DOI；否則不能列入參考文獻、也不能「依賴」。
2. 方法自足：訓練協定、臂、端點、度量缺陷的修正、預註冊與兩個 addendum（§11、§12）都在本篇寫完整。
3. 標題 ≤ 250 字元＋短標 ≤ 100；摘要 ≤ 300 字、無引用；每句標註冊／addendum／探索性（判讀 REV-17）。
4. 參考文獻改 **Vancouver**（cite.py 加渲染器，前六作者 et al.、NCBI 縮寫、doi: 在末尾）。
5. 圖說移到首次引用段落後；表格插入首次引用段落後；圖另存 TIFF（LZW、300–600 dpi、Arial 8–12 pt）。
6. 雙行距、頁碼、連續行號；無腳註。
7. 經費與利益衝突**從稿件移到系統**；Acknowledgments 不含經費。
8. 統計一節照「Reporting of statistical methods」逐項：軟體版本、程式碼倉庫、alpha、n 的來源與功效、單雙尾、多重比較、p 精確值；RESULTS §10 的 W／CI／SD 進表。
9. Data Availability：per_seed.csv、recon_results.json、recon_delta_ci.json、閘門 JSON 存 Zenodo／OSF 取 DOI；程式碼 GitHub tag＋DOI；checkpoint 另述。
10. AI 揭露三要素寫在 Methods 專節（工具、用途與影響範圍、驗證方式）。
11. Cover letter ≤ 1 頁：貢獻、與核心論文的關係與界線、類型、建議 Academic Editor。
12. 投稿系統：CRediT 逐人、ORCID、相關稿件聲明並附核心論文副本。
