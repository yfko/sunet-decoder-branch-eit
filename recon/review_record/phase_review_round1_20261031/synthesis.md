# Editorial Decision Package

ARS academic-paper-reviewer v3.23.0 · reviewer_full · v3.6.2 sprint contract `reviewer/reviewer_full/v2` · panel `sunet-recon-tier3-manuscript-review-round1-20261031` · synthesized 2026-10-31

## Mechanical Audit (v3.6.2 Sprint Contract Synthesizer Protocol)

Role-scoped scoring matrix（只計入 `eligible_roles` 內已評分的席次；`not_assessed` 不進分子也不進分母）：

| Dimension | Priority | Eligible seats | Assessed scores | Audit verdict |
|---|---|---|---|---|
| D1 methodology_rigor | mandatory | methodology | methodology = warn | warn |
| D2 domain_accuracy | mandatory | domain | domain = warn | warn |
| D3 argumentative_coherence | mandatory | da, methodology | da = block (repairable); methodology = warn | block |
| D4 cross_disciplinary_relevance | high | perspective | perspective = warn | warn |
| D5 writing_and_structure | normal | eic | eic = pass | pass |
| D6 venue_fit_and_contribution | mandatory | eic | eic = block (repairable) | block |

Failure-condition evaluation（closed vocabulary；two-stage quantifier）：

| Condition | Severity | Quantifier | Expression | Fired | Basis |
|---|---|---|---|---|---|
| F1 | 95 | any | any mandatory dimension has a fatal block | no | both blocks are `block_class: repairable` |
| F2 | 90 | any | any mandatory dimension scores 'block' | yes | D3 (da block), D6 (eic block) |
| F3 | 70 | majority | two or more mandatory dimensions score 'warn' or worse | yes | D1 (1/1), D2 (1/1), D3 (2/2), D6 (1/1) all at or above warn under majority |
| F4 | 60 | any | any high-priority dimension scores 'block' | no | D4 = warn |
| F5 | 40 | any | any dimension scores 'warn' or worse | yes | D1, D2, D3, D4, D6 |
| F0 | 10 | all | every dimension scores 'pass' | no | only D5 passes |

Precedence：fired 中 severity 最高者為 F2 (90) → `major_revision`。DA 的 `#### CRITICAL` 表為空，故 DA line 為 `[]`，無 rejection rationale，無 `[DA-CRITICAL-VS-ACCEPT]` marker。

```
dimension_verdicts: [D1=warn, D2=warn, D3=block, D4=warn, D5=pass, D6=block]
fired_conditions: [F2, F3, F5]
da_critical_adjudications: []
editorial_decision=major_revision
```

#684 criteria binding：五張 card 皆揭露 `criteria_binding_unavailable`。本信**不作任何 venue-alignment claim**；下文提到的 PLoS One 僅是 `metadata.json` 記載的目標期刊名稱，不是對其 criteria 的對齊判定。Binding conformance 不是分數、不是 failure condition、不是 severity，也不是 editorial verdict。

#518 cross-model blind decision check：`ARS_CROSS_MODEL` 未設定，無行為變更。

## Calibration Resolution

`calibration_status: NOT_CALIBRATED`

Current runtime boundary: do not upgrade this package from a candidate or prose-named profile. `PROFILE_MEASURED` remains unavailable until a closed profile artifact and replay validator bind the exact target fields to the actual completed-panel `execution_topology_sha256`.

---

## Part 1: Editorial Decision Letter

### Manuscript Information

- **Title**: Does a decoder branch for the cardiac component of lung EIT survive a change of reconstructor? A preregistered, parameter-matched study with leave-one-reconstructor-out training
- **Review object**: `RECON_paper/manuscript/06_DRAFT_v1.md`（完整手稿；bundle `manuscript_bundle.md` 帶相同的 `BNNNN` block ids）
- **Manuscript ID**: none（內部五席審查，非期刊系統編號）
- **Configured venue (name only, no alignment claim)**: PLoS One（研究論文，IMRaD，Vancouver）
- **Decision Date**: 2026-10-31
- **Review Round**: Round 1 of the five-seat panel on the manuscript（先前的 panel 審的是 results-interpretation record，不是手稿）

### Review Panel Provenance (#540/#740)

- **Typed artifact**: `RECON_paper/manuscript/phase_review_round1_20261031/provenance_artifact.json`（`schema_version: review-panel-provenance/1.0`；dispatching layer 回報 replay-validated，本 synthesizer 未重跑 replay）
- **Artifact SHA-256**: `fdfd333a727124137c8794926105c86b5bff8a4deacee3fb9ef0e7ef5594be15`（raw bytes）
- **Panel ID**: `sunet-recon-tier3-manuscript-review-round1-20261031`
- **Contract SHA-256**: `e9712090d2469fea15a37b8e22d4e137afbcb2bf38d5789939c5df56738ef7af`
- **Normalized manifest SHA-256**: `ce2d7087424355d8105fcdde7d8d804a8a550d858a9912bab25793a6f7b998fd`
- **Execution topology SHA-256**: `5f6b97561e1c1c6cfd9621d5a99af9285aa22e1caba6452d974528f4612285b0`
- **Fresh-context scope**: `within_panel_attempt_only`（不比較 retries 或先前 rounds）
- **Independence claim**: `not_computed_from_personas`

| Seat | Role ID | Actor type | Context ID | Peer outputs visible | Model family | Provider | Human reviewer ID |
|---|---|---|---|---|---|---|---|
| EIC | eic | model | subagent-eic-20261031 | false | claude-fable-5-1 | anthropic | null |
| R1 | methodology | model | subagent-methodology-20261031 | false | claude-fable-5-1 | anthropic | null |
| R2 | domain | model | subagent-domain-20261031 | false | claude-fable-5-1 | anthropic | null |
| R3 | perspective | model | subagent-perspective-20261031 | false | claude-fable-5-1 | anthropic | null |
| DA | da | model | subagent-da-20261031 | false | claude-fable-5-1 | anthropic | null |

| Provenance axis | Status (`true` / `false` / `unknown`) |
|---|---|
| Role-separated | true |
| Within-panel invocation-context separation | true |
| Blind to peer outputs | true |
| Model-family distinct | false |
| Provider distinct | false |
| Human-reviewer distinct | false |

- **Binary independence claim**: Not computed. Persona or role diversity proves only `role_separated`; do not relabel the panel as independent.
- **Correlated-error disclosure** (`required: true`, reason `same_model_family`): All model-executed review seats used one model family; role separation does not remove correlated-error risk.

---

Dear Author(s),

感謝您將題為「Does a decoder branch for the cardiac component of lung EIT survive a change of reconstructor? A preregistered, parameter-matched study with leave-one-reconstructor-out training」的手稿交付審查。本稿由五個 role-separated review seats 審閱（Journal-Fit Reviewer／EIC、methodology、domain、perspective、Devil's Advocate）。五席的執行 provenance 如上表所列，六個軸分別呈現，不化約為單一的 independence claim；五席使用同一 model family，correlated-error risk 已揭露。

### Decision: Major Revision

決定由 sprint contract 的機械規則得出：D3 (argumentative_coherence) 與 D6 (venue_fit_and_contribution) 兩個 mandatory dimension 各有一個 repairable block，F2 觸發；D1、D2、D3、D6 四個 mandatory dimension 全部 warn 或更差，F3 觸發。兩個 block 都是 repairable、都是 textual，沒有任何席次要求重跑任何 run 或重新分析 per-seed data。

### Reviewer Summary

Schema 13.2 的 card 沒有 report-level recommendation，也沒有 report-level confidence；下表呈現各席的 role-scoped dimension score，confidence 只存在於 per-finding 層（已逐項轉錄到 Part 2 的 roadmap）。

| Reviewer | Role | Role-scoped score(s) | Trigger (verbatim from the seat's Phase 1 commitment) | Findings |
|---|---|---|---|---|
| Journal-Fit Reviewer (EIC) | handling academic editor for a preregistered simulation study with negative results | D5 = pass; D6 = block (repairable) | "present a post-unblinding addendum result with the same confirmatory standing as a preregistered result" | S1–S7; W1–W6 (2 Major, 4 Minor); 3 questions |
| Reviewer 1 (methodology) | methodology/statistics referee for preregistered deep-learning simulation studies | D1 = warn; D3 = warn | D1: "a registered rule is applied correctly but the registered wording is paraphrased rather than quoted"; D3: "Verdict wording differs in strength between Abstract, Results and Discussion without contradicting the registered outcome" | S1–S6; W1–W12 (3 Major, 9 Minor); AR1–AR12 all `consistent`; 4 questions |
| Reviewer 2 (domain) | EIDORS-based thoracic EIT reconstruction specialist | D2 = warn | "the Methods omit a detail a domain reader needs to interpret a reported quantity" | S1–S6; W1–W9 (2 Major, 7 Minor); 5 questions |
| Reviewer 3 (perspective) | medical-image domain generalisation / multi-source training | D4 = warn | "the confirmatory or exploratory standing is left for the reader to infer rather than stated alongside the implication" | S1–S7; W1–W9 (1 Major, 8 Minor); 2 questions |
| Devil's Advocate | fixed adversarial seat | D3 = block (repairable) | "a post-unblinding or exploratory result is presented with confirmatory standing in the abstract or conclusions" | CRITICAL: none; MAJOR: 7; prose minors: 7 |

### 五席共同確認的優點（供作者保留，不要在修訂中改掉）

五席各自、彼此不可見地指出了同一組優點：Table 4 的四個 hashed states 讓 preregistration 的 provenance 可以從一張表稽核（EIC-S1、R1-S3、R3-S4）；held-out loss 在幾乎每一處都帶 upper-bound qualification（EIC-S2、R2-S2、R3-S2）；deviations 與 expectation hit rates 照實報告（EIC-S3、R1-S4、DA 開頭段）；per-cell 統計報告完整且 R1 以 AR1–AR12 重算了全部十二個 Wilcoxon p 值皆一致（R1-S1、R1-S5、EIC-S5）；三個 absence statements 有 database、日期與 string counts 綁定（EIC-S6、R2-S6）；equivalence 以 pre-fixed margin 檢定而非由 non-significance 推論（R1-S2、R3-S3）；amplitude-scale finding 是真實的 EIT pipeline 知識且以網路實際輸入作圖診斷（R2-S3、R3-S7）；對 companion manuscript 的獨立性有陳述且確實遵守（EIC-S4、R2 結尾段）；通訊作者對架構的利益已揭露（EIC-S7、DA 開頭段）。R1 的總結是「Numbers are not the weakness of this manuscript」；R2 稱 domain content「accurate and unusually disciplined」；R3 稱 framing「unusually readable for an outsider」。本輪所有 blocking issues 都是文字層的 standing 與措辭問題，不是 soundness 問題。

### Consensus Analysis

Consensus 以四個 non-DA 席（EIC、R1、R2、R3）為分母，逐 sub-claim 計算（Step 1b 的 sub-claim inventory 在 Part 2 的每一列都帶 `SC-n`）。`not-mentioned` 是沉默，不是反對；DA 的 findings 另行追蹤，不進 consensus count。

#### Points of Agreement

**[CONSENSUS-4]**：無。沒有任何一個 sub-claim 被四席都提出。這與五席的 role scoping 一致：每席只審自己 eligible 的 dimension。

**[CONSENSUS-3]**：無。SC-3（「could not be separated at 0.4 points」）由 EIC、R1、R3 三席提出、R2 沉默，但三席對 severity 的標記不一致（EIC Minor、R1 Minor、R3 Major），依 disposition precedence 歸入 SPLIT，不是 CONSENSUS-3。

**Corroborated findings（2/4，無衝突）**：
- **SC-2** Conclusion（B0085）與 Section 4.1（B0066）的 number-bearing sentences 沒有 standing label；EIC-W2（Major）提出，R3-W1（Major）corroborated；DA MAJOR 1 另行 corroborated。R1、R2 沉默。這是 D6 block 與 D3 block 共同的 anchor。
- **SC-22** 「19 to 33 points」漏掉自己的最大值 33.8 → 34；「14 to 58」對 13.9／57.5 的 rounding 不一致；R2-W4 提出，DA minor (1) corroborated。EIC、R1、R3 沉默。此為 manuscript transcription 的查核，對照 `results_recon/recon_results.json`，不是對 RESULTS_RECON.md 的爭議。

**Single-reviewer findings（1/4，無衝突；依 named criterion 與 anchored evidence 評估，不帶 consensus label）**：其餘所有 sub-claims。其中由 DA 另行 corroborated 的有 SC-1（EIC-W1 ↔ DA MAJOR 5）、SC-5（EIC-W4 ↔ DA minor 6）、SC-8 與 SC-9（R1-W1、R1-W2 ↔ DA MAJOR 3）、SC-11（R1-W5 ↔ DA 的 strongest counter-argument 段）、SC-16（R1-W10 ↔ DA minor 2）、SC-18（R1-W12 ↔ DA 的 strongest counter-argument 段）。單席 finding 不因 DA corroboration 升格為 consensus，但 DA 的 corroboration 在 roadmap 的 Source 欄保留。

#### Points of Disagreement

**Disagreement 1 — SC-3「two remedies that could not be separated at 0.4 points」的 severity**
- **EIC view**（W3，Minor，confidence 4）：M2′ 是「reported, not tested」，0.4 既非最大 point estimate (+0.360) 也非 interval bound（六個 interval 落在 [−0.32, +0.50]）；改成 licensed 的「never worse」形式。
- **R1 view**（W6，Minor，confidence 4）：同一句旁邊有兩個 interval 排除零、一個上界 +0.50；句子應描述而非結論；刪去或改以最寬 interval 陳述。
- **R3 view**（W1，Major，confidence 4）：這是 equivalence-shaped statement，adjacent-field 讀者會引為「pooling equals retraining」；此句與 Conclusion 缺 standing labels 同屬 D4 的 warn trigger。
- **Disagreement type**：Severity disagreement（remedy 相容，三席都要求改為 descriptive 形式）。
- **Editor's Resolution**：保留三席各自 transported 的 severity；obligation class 定為 `must_fix`。
- **Resolution Rationale**：obligation 不是從 severity 導出的 work rank，而是 decision contract 的 gate。此句是 DA 的 D3 block（MAJOR 1）直接 anchor 的句子、是 R3 的 D4 warn trigger 的實例、也坐落在 EIC 所說「讀者會引用的兩個 surface」之一。不論 Minor 或 Major，F2 與 F3 要清除，此句必須改。R3 的 Major 標記來自 cross-disciplinary 讀者的引用風險，EIC 與 R1 的 Minor 來自「不改變任何 verdict」；兩者都對，衡量的對象不同。

**Disagreement 2 — SC-4「adds nothing measurable」／「no measurable effect at any of the three layers」的 severity**
- **EIC view**（W4，Minor，confidence 4）：Table 3 與 Section 3.6 在 GN 報了一個 measured negative difference（−3.9 points，CI −5.3 to −2.4，p 0.00012）；「nothing measurable」不準確，且是手稿他處避免的「no effect」形式。
- **R1 view**（W3，Major，confidence 5）：heading（B0062）與 Abstract 宣稱 absence，表格顯示 presence；L2 verdict 不受影響，但措辭強度在 Abstract／Results／Discussion 間不一致（D3 warn trigger）。
- **DA view**（MAJOR 4，confidence 4，不計入 consensus）：B0067「no measurable effect at any of the three layers」與 Section 3.1 自己的「below the floor, not zero」（B0047，四個 cell 的 p < 0.05 且 interval 排除零）矛盾。
- **Disagreement type**：Severity disagreement（remedy 相同：改為「no measurable benefit」／「below the registered floor」／「sign reversed」，GN deficit 保持 described, not tested）。
- **Editor's Resolution**：保留各席 transported severity；obligation `must_fix`。
- **Resolution Rationale**：Expertise first——data–text consistency of statistical statements 屬 methodology seat 的 remit，R1 的 Major 標記以 Table 3 的數字為據，confidence 5；且此項正是 R1 在 D3 上宣告的 warn trigger，不清除則 D3 不能回到 pass。

**Disagreement 3 — SC-12「pooled training was never worse than retraining」的替代措辭（direction）**
- **R1 view**（W6，Minor，confidence 4）：M2′ 有一個負的 point estimate（D on BP，−0.083，CI −0.32 to +0.13）、四個 interval 跨零；「never worse」只對 interval 下界（約 0.3 points）為真，對 point estimate 不為真；建議「never worse than retraining by more than 0.3 points in any cell, and in two of six cells was better by a small amount」。
- **DA view**（MAJOR 2，confidence 4，不計入 consensus）：universal descriptive claim 對一個 verdict-free quantity 等於 verdict in disguise；defensible 的摘要是「no interval below −0.32 points and no point estimate below −0.08」。
- **R3 view**（W1 的 remedy，confidence 4）：為修 SC-3 提出的替代句**保留**「never worse」並加括號「(first addendum; descriptive, −0.08 to +0.36 points, two of six intervals favouring pooling and confounded with optimisation steps)」；R3 並認為 Abstract 現有的「never worse」寫法是 careful 的。
- **Disagreement type**：Direction disagreement（R3 未評估「never worse」對 point estimates 是否成立，其 remedy 若照抄會保留 R1 與 DA 所指的問題；R3 的 position 記為 `disputed`，屬 action conflict，不是 existence conflict）。
- **Editor's Resolution**：採 R1 的 bound 形式為措辭核心，併入 R3 的 standing label 與 confound 括號；未加限定的「never worse」不被授權。obligation `must_fix`。
- **Resolution Rationale**：Evidence first——Table 1 的 M2′ block（B0108）印有 −0.083 的 point estimate，這是手稿自己的數字；Expertise first——descriptive-statistics 措辭屬 methodology seat。R3 的 remedy 對 SC-3 的 labelling 部分是正確的，被採納；對「never worse」一詞 R3 沒有以 M2′ 的六個值為據，因此在這一點上不優先。DISPATCH 規則「pooled training is 'never worse', never 'equivalent'」是對 equivalence 的禁令，不是對 universal 措辭的授權；R1 的 bound 形式同時滿足該規則與 Table 1。

**無法由 evidence 或 expertise 裁決、保留為 unresolved dissent 的爭點**：無。上述三項都已裁決；DA 的 MAJOR 6（SC-37）與 MAJOR 7（SC-38、SC-39）不是 SPLIT（DA 不在四席之內），其 editorial assessment 見下節。

### Devil's Advocate Findings（adjudication and visibility，非 veto）

DA 的 `#### CRITICAL` 表為空，無需 C-line adjudication。DA 的七個 MAJOR 與七個 prose minors 全部進入 roadmap；每一項都要求作者回應。各項是否被其他席 corroborated、以及 editor 的評估：

| DA item | Corroborated by | Editor's assessment | Roadmap |
|---|---|---|---|
| MAJOR 1 — Conclusion no standing labels; 0.4-point inseparability; "every verdict followed a rule" levels standings; Abstract's "never worse" labelled addendum, not descriptive | EIC-W2, R3-W1 (labels); EIC-W3, R1-W6, R3-W1 (0.4 points) | Validated on the page（B0085 逐句對照 Section 1.4 與 B0044 的 standing rule）。D3 block 的 trigger 成立。 | REV-M1-2, REV-M1-3 |
| MAJOR 2 — "never worse" universal vs −0.083 point estimate | R1-W6 | Validated（Table 1 B0108）。措辭裁決見 Disagreement 3。 | REV-M1-12 |
| MAJOR 3 — selective application of fixed interpretation; withheld sentence never quoted; absent from deviation record | R1-W1, R1-W2 | Validated for the record-keeping part（R1 獨立指出同兩個 post-read decisions）。「both asymmetric choices favour the narrative」是 DA 的 reading，手稿須以一句話說明為何 R3 degenerate cells 套用 fixed reading 而 M1 degenerate cells 不套用，或一致處理；panel 不預設方向。 | REV-M1-8, REV-M1-9, REV-M1-36 |
| MAJOR 4 — "nothing measurable" / "no measurable effect at any of the three layers" vs Table 3 and B0047 | EIC-W4, R1-W3 | Validated。見 Disagreement 2。 | REV-M1-4 |
| MAJOR 5 — Table 1 GREIT → GREIT "ref, not tested" carries verdict "falsified"; Abstract "every reconstructor" | EIC-W1 | Validated（EIC 將此列為 D6 block 的 trigger）。R2 在 W2 亦稱「the GREIT diagonal is a reference cell and no hypothesis is tested on it」，與 EIC/DA 一致。作者須在兩個 textual repair 中擇一（見 R1 item）。 | REV-M1-1 |
| MAJOR 6 — "upper bound on the input-side generalisation loss" is unlicensed; should read "not decomposed" | R1-W9 (weaker form: the non-negativity assumption is unstated) | **Not adopted as relabelling.** R2-S2（domain seat，owns the endpoint）、R3-S2、EIC-S2 三席各自把 upper-bound qualification 列為 strength，R2 稱其為「the correct reading of the task」。Expertise first：endpoint 的定義屬 domain seat。但 DA 指出 bound 的方向依賴一個未陳述的假設，這點與 R1-W9 一致，必須補上（state the assumption once in 2.3, next to the existing "was not measured" sentence）。作者須回應 DA 的 position。 | REV-M1-15 (must state assumption), REV-M1-37 (DA position, consider) |
| MAJOR 7 — 4.5 "both addenda went against the authors' own recipe" vs Table 4 (3/3 verdict hits each); "turned the pooled recipe from generalises into in-pool only" presupposes a prior claim; title attaches "preregistered" to a second-addendum design | none（EIC-S3、R1-S4 讚許 hit-rate reporting，但未評估 B0078 這一句） | 4.5 的辯護句：Table 4 的 hit rates 確實顯示 verdicts 符合 addenda 的 expectations，「went against the recipe」與「went against expectations」是兩件事，手稿須寫清楚它主張的是前者，並刪去預設先前 generalisation claim 的措辭。Title：EIC 與 R2 都檢查過 title（字數、無 exploratory number）未提出異議；LORO 是 pre-hashed 的 second addendum，在手稿自己的 double-standing 定義下「preregistered」可辯護，但 DA 的 reading（讀者會以為 LORO 是 registered part）是真實風險；panel 不要求改 title，要求作者回應。 | REV-M1-38 (should_fix), REV-M1-39 (consider) |
| minor 1 — 19 to 33 omits 33.8 | R2-W4 | Validated（arithmetic from Tables 1–2） | REV-M1-22 |
| minor 2 — M3′ definition and registered-path Dice not recomputable from main tables | R1-W10 | Validated（R1 reproduces the values from the registered path; the caption must say so） | REV-M1-16 |
| minor 3 — 2.5 "no setting or rule changed" beside "the change of matching rule" without timing | none（EIC-S3 與 R2-S1 把 matching-rule change 讀為兩個已記錄、dated、pre-read deviations 之一） | 記錄本身被三席讀為完整；DA 的點是該句的 timing 不自明。One clause. | REV-M1-40 (consider) |
| minor 4 — "reconstructor-agnostic is falsified" falsifies a term nobody claimed | none | Logic-of-argument point；作者可指出誰提過該詞，或改為「any source-aware statement must read…」。 | REV-M1-41 (consider) |
| minor 5 — loss order explained as pool coverage in the indicative | none | 手稿自己在同節稍後說 mechanisms untested；一句改為 conditional 即可。 | REV-M1-42 |
| minor 6 — Conclusion opening "does not appear" is a no-effect form | EIC-W4 | Validated（與 Section 3.1「below the floor, not zero」不一致） | REV-M1-5 |
| minor 7 — contribution one "extends" presupposes a prior null | none（與 SC-1 相連：prior null 只能來自 companion study 或 Table 1 的 ref cell） | Validated as a logic point；repair 隨 REV-M1-1 的選擇而定。 | REV-M1-43 |

### Decision Rationale

本輪的決定是 Major Revision，由 contract 的算術得出，不是 editor 的裁量：D3 與 D6 各有一個 repairable block（F2），四個 mandatory dimension 全部 warn 或更差（F3）。但要說清楚這個決定的性質：五席沒有任何一席質疑數據、設計或統計。R1 重算了 Tables 1 到 3 可重算的每一個量與全部十二個 p 值，全部一致；R2 核對了每一個引用的數字，只有一處 rounding；DA 自己承認「None of this overturns the data」。兩個 block 都是 textual、都是 repairable：EIC 的 D6 block 綁在 GREIT reference cell 帶 verdict（SC-1）與 Conclusion 缺 standing labels（SC-2）；DA 的 D3 block 綁在同一個 Conclusion 段（SC-2、SC-3）、Abstract 的「never worse」（SC-12）與「nothing measurable」（SC-4）。四席與 DA 彼此不可見地指向同一組句子，這是本輪最強的訊號：手稿為自己設下的 standing discipline（Section 1.4、B0044）在 Abstract 與 Conclusion 這兩個讀者會引用的 surface 上鬆脫了。

為何不是 Minor Revision：F2 與 F3 都已觸發，contract 不允許 post-hoc 軟化；且 D1 的 warn（registered rules 只以 paraphrase 出現，SC-8）與 D2 的 warn（forward model 與 reconstructor settings 不自足，SC-19）各需要一張 supplementary table 或一段新的 Methods 內容，不是逐句改字。為何不是 Reject：沒有 fatal block，沒有任何席次認為結論不被數據支持。三個 SPLIT 全部是 severity 或 direction 的分歧，remedy 彼此相容，已依 evidence-first 與 expertise-first 原則裁決；沒有 unresolved dissent。

F3 的清除條件要特別說明：D1、D2、D3、D6 四個 mandatory dimension 都必須回到 pass，F3 才不會再觸發。因此除了 Blocking Issues 表列的三項，REV-M1-4（R1 的 D3 warn trigger）、REV-M1-8（R1 的 D1 warn trigger）與 REV-M1-12 也必須在 re-review 前完成。修訂稿將進入 re-review。

### Blocking Issues (0–3, immutable source order)

| Transport ref | Blocking issue | Source reviewer(s) | Evidence anchor | Resolving roadmap item |
|---|---|---|---|---|
| R1 | The GREIT matched cell is coded "ref = reference, not tested" in Table 1 yet carries the verdict "falsified", and the Abstract, the Section 3.1 heading and the Conclusion count it under "every reconstructor" / "all three reconstructors" against the registered floor | EIC (W1); DA (MAJOR 5) | text: B0006 "Under matched training the branch stayed below the registered floor on every reconstructor" | REV-M1-1 |
| R2 | The Conclusion (B0085), Section 4.1 (B0066) and the Abstract's "never worse" sentence carry registered, first-addendum, second-addendum and descriptive quantities without a standing label per clause, and close with "Every verdict followed a rule", levelling the standings | EIC (W2); R3 (W1); DA (MAJOR 1) | text: B0085 "leaving one reconstructor out cost 62, 16 and 36 points on GREIT, Gauss–Newton and back-projection" | REV-M1-2 |
| R8 | Section 2.1 does not give the stimulation/measurement pattern, electrode model, mesh, geometry ranges, GREIT training-target settings, GN parametrisation, BP interpolation or the linear SNR definition, so a domain reader cannot judge that the three operators saw the same data | R2 (W1) | absence: Section 2.1, blocks B0023 to B0024 — expected stimulation and measurement pattern, electrode model and contact impedance, mesh dimensionality and density, cylinder and inclusion size ranges, GREIT training-target settings, GN pixel-grid parametrisation, BP upsampling interpolation and the linear SNR definition; checked Sections 2.1 to 2.4, Table 4, the S1 to S2 Table and S1 Appendix captions, and the Fig 1 to Fig 3 captions | REV-M1-19 |

### Questions for the authors（五席轉交，請在 response letter 中逐題回答）

1. (EIC) GREIT matched cell 要讀作 reference 還是 verdict cell？若為後者，受哪一個 hashed state 管轄？
2. (EIC) Sections 4.1 與 5 的「0.4 points」是最大 M2′ point estimate 的 rounding，還是 interval bound 的 rounding？會改為 licensed 的「never worse」形式嗎？
3. (EIC) GREIT training row 能否只從本文的 deposit 重現，或需要 companion study 的 checkpoints？
4. (R1) 「n = 30 gives at least 0.89 power for a floor-sized effect」的 SD 與 test 是什麼？計算在 S2 Table 嗎？
5. (R1) Wilcoxon p 值是否全程以 normal approximation with continuity correction 計算（Table 1 所述，AR1–AR12 重現），或部分 cell 為 exact？
6. (R1) 六個 no-retraining cells 的 R-path Dice 是否在 S1 Table？M3′ 依賴它，正文只引 E1 Dice。
7. (R1) 任何 row 是否有 seeds 被排除或重跑？
8. (R2) GREIT seeds 0 到 29 是在 2026-09-26 之前還是之後訓練？R3 註冊時其 GREIT → GREIT heart Dice 是否已知？
9. (R2) One-step GN「on GREIT's grid」是在 64 × 64 pixel grid 上經 coarse-to-fine mapping 參數化，還是在 FEM 上解後 rasterised？
10. (R2) Gaussian noise 是否只加在 inhomogeneous frame、homogeneous reference 無噪聲？20 dB 是 amplitude (norm) ratio 10 嗎？
11. (R2) 請對照原文確認 Holzschuh et al. (2024)（0.76 vs 0.74，p = 0.18）與 Yan et al. (2020)（0.89 to 0.60）所引數字。
12. (R2) Section 3.2 的 131／154 與 Section 3.3 的 1/132／1/156：加半句說明是 seed 0 上不同 affine 的值，以免讀作 discrepancy。
13. (R3) 在規劃中的 hardware study 所針對的臨床 EIT 系統上，reconstructor identity 是否總是在 deployment 時可得，使 per-source affine 無需推論即可選取？
14. (R3) mixed-ps row 中 GREIT heart targets 在 loss 中的權重可達 GN 的 1.7 倍；作者是否視 target-scale weighting 為未來 per-source normalisation 問題的一部分，或在本文範圍之外？

---

## Part 2: Revision Roadmap

> Roadmap items are keyed to Step 1b `sub_claim_id`s (`SC-n`); REV-M1-n and SC-n share the same ordinal. Order is immutable source order (seat order EIC, R1, R2, R3, DA; then finding order of the first seat that raised the sub-claim). Severity and Confidence are TRANSPORTED from the driving finding (first-listed source), never re-derived; where a corroborating seat tagged a different severity it is noted in the Source column. `obligation_class` is an editorial gate under the decision contract, not a work rank. Cost scope is typed (`sentence | section | re_analysis | new_data | other` + locator). Targets are proposals naming manuscript block ids (and `tools/recon_draft_tables.py` where a table is at issue); proposal is not write authority. Hashed preregistration text and RESULTS_RECON.md are never targets; a number dispute is a transcription check against `results_recon/recon_results.json`. No author triage is emitted here; the PI collects it separately.

### Required Revisions (Must Fix)

> **Ordinal contract (#576/#670):** `R<n>` follows immutable roadmap source order filtered to `obligation_class == must_fix`; blocks are exactly R1..R10.

| Transport ref | Roadmap id | Revision Item | Sub-Claim(s) | Severity | Evidence Anchor | Confidence | Source | Obligation class | Cost scope | Bounded consequence |
|---|---|---|---|---|---|---|---|---|---|---|
| R1 | REV-M1-1 | Resolve the standing of the GREIT → GREIT matched cell: EITHER keep it as a reference (Verdict cell becomes a dash in Table 1; Abstract B0006, Section 3.1 heading B0045 and Conclusion B0085 say the two registered cells were falsified and the GREIT reference, re-scored here, showed the same pattern) OR give it a verdict and state its standing (whose rule, fixed when, read when) in Section 2.5 (B0036) and Table 4 (B0116) | SC-1 | Major | text: B0006 "Under matched training the branch stayed below the registered floor on every reconstructor" | 4 — editorial reading of standing labels against the manuscript's own Table 1 legend and Section 1.4 | EIC (W1); corroborated DA (MAJOR 5) | must_fix | section: B0006, B0045, B0085, Table 1 via tools/recon_draft_tables.py (B0106), B0036, B0116 | standing_mismatch → D6 block trigger cleared; author chooses which repair |
| R2 | REV-M1-2 | Give every number-carrying clause of the Conclusion (B0085) and Section 4.1 (B0066) its standing label ("registered", "first addendum", "second addendum", "exploratory", "descriptive") as the Abstract already does; label the Abstract's "never worse" sentence as descriptive (first addendum; reported, not tested); reword the closing "Every verdict followed a rule…" so that it does not lend verdict standing to descriptive and addendum quantities | SC-2 | Major | text: B0085 "leaving one reconstructor out cost 62, 16 and 36 points on GREIT, Gauss–Newton and back-projection" | 4 — direct comparison of the Conclusion's sentences with the standing rules stated in Sections 1.4 and 3 | EIC (W2); corroborated R3 (W1, Major), DA (MAJOR 1) | must_fix | section: B0085, B0066, B0006 | standing_mismatch → D6 and D3 block triggers cleared; D4 warn trigger cleared |
| R3 | REV-M1-3 | Replace "two remedies that could not be separated at 0.4 points" (B0085) and "could not be separated at 0.4 points" (B0066) with a descriptive, licensed form compatible with REV-M1-12 (e.g. the six M2′ differences between −0.08 and +0.36 points, two of six intervals favouring pooling, confounded with optimisation steps); do not state a bound that is in no table | SC-3 | Minor | text: B0085 "two remedies that could not be separated at 0.4 points" | 4 — the manuscript's own standing rules and Table 1's M2′ block supply the check | EIC (W3); corroborated R1 (W6, Minor), R3 (W1, Major), DA (MAJOR 1) — SPLIT on severity, arbitrated | must_fix | sentence: B0085, B0066 | equivalence_overclaim → removed; D3/D4 triggers cleared |
| R4 | REV-M1-4 | Reword "adds nothing measurable" (Section 3.6 heading B0062; Abstract B0006) and "no measurable effect at any of the three layers" (B0067) to the registered vocabulary: "no measurable benefit" / "below the registered floor" / "sign reversed"; keep the GN held-out deficit (−3.9 points, CI −5.3 to −2.4) as described, not tested | SC-4 | Minor | text: B0006 "and the branch added nothing measurable there" | 4 — text-against-table reading within the manuscript | EIC (W4); corroborated R1 (W3, Major, confidence 5), DA (MAJOR 4) — SPLIT on severity, arbitrated | must_fix | sentence: B0062, B0006, B0067 | data_text_mismatch → removed; R1's D3 warn trigger cleared |
| R5 | REV-M1-8 | Add a supplementary table with one row per hypothesis (R1, R3, M1, M1′, L1, L2) quoting verbatim the registered decision rule and both fixed outcome-interpretation sentences, with the governing hash state; in Results (B0046–B0063) mark the interpretation sentences as quotations so the reader can tell quotation from paraphrase | SC-8 | Major | absence: Sections 2.5, 2.6 and 3.1 to 3.6 — expected the verbatim registered decision rule and both fixed interpretation sentences for each of R1, R3, M1, M1′, L1 and L2; checked Methods 2.5 and 2.6, every Results subsection, Table 4 and the S1 Appendix caption | 4 — preregistration reporting practice; the gap is visible on the manuscript's surface | R1 (W1); partially corroborated DA (MAJOR 3: "the withheld interpretation sentence is never quoted") | must_fix | section: new S-table (Supporting information B0093–B0097) + B0039, B0046–B0063 | verification_gap → D1 warn trigger cleared |
| R6 | REV-M1-9 | Add the two post-read decisions (withholding the registered interpretation of a falsified M1 for the GN and BP cells, B0053; listing but not reading the registered secondary scoring path, B0049/B0111) to the deviation record in Section 2.5 (B0036–B0037), Table 4 (B0116) and S2 Table (B0095), each with timing "after reading the cell", rationale and consequence; quote the registered M1 interpretation and state in one sentence why it is not applied | SC-9 | Major | text: block B0053 "the registered interpretation of a falsified M1 is not applied to them" | 4 — preregistration deviation reporting; the timing is stated in the manuscript itself | R1 (W2); corroborated DA (MAJOR 3) | must_fix | section: B0036, B0037, B0053, B0049, B0116, B0095, B0111 | deviation_record_incomplete → completed |
| R7 | REV-M1-12 | Replace the universal "never worse than retraining" (Abstract B0006; contribution B0020; heading B0055; B0056; Conclusion B0085) with a bounded descriptive form: never worse by more than 0.3 points (interval lower bound) in any cell, point estimates −0.08 to +0.36, two of six intervals favouring pooling, confounded with threefold optimisation steps; carry the first-addendum/descriptive label (arbitrated: R1's bound + R3's label) | SC-12 | Minor | text: block B0056 "Pooled training was never worse than retraining on any reconstructor" | 4 — descriptive-statistics wording against Table 1's M2′ footnote | R1 (W6); corroborated DA (MAJOR 2, Major); R3 (W1) disputed on remedy — SPLIT on direction, arbitrated | must_fix | sentence: B0006, B0020, B0055, B0056, B0085 | descriptive_overclaim → removed; D3 block trigger (Abstract) cleared |
| R8 | REV-M1-19 | Add to Section 2.1 (B0023–B0024) or S2 Table one paragraph giving the stimulation and measurement pattern, electrode model and contact impedance, mesh dimensionality and density (and any coarser inverse mesh), cylinder radius and the inclusion radius/centre ranges behind "randomised", the meaning of "heterogeneous conductivity", GREIT training-target settings (target radius, distribution, desired-image width), the one-step GN parametrisation "on GREIT's grid", the interpolation used to upsample BP's 32 × 32 raster, and the SNR definition (amplitude or power; which frame noise was added to) | SC-19 | Major | absence: Section 2.1, blocks B0023 to B0024 — expected stimulation and measurement pattern, electrode model and contact impedance, mesh dimensionality and density, cylinder and inclusion size ranges, GREIT training-target settings, GN pixel-grid parametrisation, BP upsampling interpolation and the linear SNR definition; checked Sections 2.1 to 2.4, Table 4, the S1 to S2 Table and S1 Appendix captions, and the Fig 1 to Fig 3 captions | 4 — EIDORS user; the absent items are the ones needed to rebuild the three reconstruction matrices | R2 (W1) | must_fix | section: B0023, B0024 (or S2 Table B0095) | methods_not_self_contained → D2 warn trigger cleared |
| R9 | REV-M1-20 | State in Section 2.2 (B0028) and in Table 4's "Written after reading" cell (B0116) the training date of the reused companion-study GREIT networks (seeds 0–29) relative to hash 4b4c7a6d; if they predate the registration, record a deviation and correct "no arm trained, no contrast computed"; if they postdate it, say so with the date | SC-20 | Major | text: block B0116 "Nothing: no arm trained, no contrast computed" and block B0028 "The GREIT row reuses seeds 0 to 29 of the companion study's 20 dB training" | 3 — the tension is on the page; which way it resolves is not | R2 (W2); adjacent R1 (W7), EIC (question 3) | must_fix | sentence: B0028, B0116 (+ deviation record B0036/B0095 if applicable) | preregistration_statement_inexact → made exact |
| R10 | REV-M1-21 | Correct the Abstract sentence that assigns the global-affine collapse to the addendum: the collapse is the registered M1 row (Table 1, standing R); the addendum is the per-source re-run (e.g. "The registered pooled row, with a single global normalisation, collapsed two reconstructors …; in a post-unblinding, pre-hashed addendum with a per-source affine, pooled training was …") | SC-21 | Minor | text: block B0006 "In a post-unblinding, pre-hashed addendum, a single global normalisation collapsed two reconstructors" | 4 — standing of each row is given in Table 1 and Table 4 | R2 (W3) | must_fix | sentence: B0006 | standing_mismatch (Abstract) → corrected |

### Required Item Details

**R1: GREIT matched cell — reference or verdict**
- **Problem**: Table 1 (B0106) codes GREIT → GREIT as "ref = reference, not tested" yet its Verdict column reads "falsified"; the Abstract (B0006), the Section 3.1 heading (B0045) and the Conclusion (B0085) count it under "every reconstructor"/"all three reconstructors"; Section 1.4 states the registered R1 covered GN and BP only; the cell is not among the twenty verdict cells counted at B0077.
- **Source**: EIC W1 (D6 block trigger); DA MAJOR 5; R2 W2 reads the cell the same way ("a reference cell and no hypothesis is tested on it").
- **Requirement**: Choose one repair and apply it consistently across Table 1 (regenerate via tools/recon_draft_tables.py), B0006, B0045, B0085 and, if the verdict is kept, B0036 and B0116. Also reconcile contribution one's "extends" (B0020; REV-M1-43).
- **Acceptance criteria**: Table 1's Standing and Verdict columns for the GREIT → GREIT row are mutually consistent with the caption's legend, and no sentence in the Abstract, Section 3.1 heading or Conclusion counts a reference cell under the registered floor; or the cell's hashed standing is stated in Section 2.5 and Table 4.

**R2: Standing labels in the Conclusion, Section 4.1 and the Abstract**
- **Problem**: B0085 carries registered, first-addendum, second-addendum and descriptive quantities in one unlabelled run of sentences and closes with "Every verdict followed a rule…"; B0066 does the same for the three signs; the Abstract's "never worse" sentence is labelled addendum but not descriptive.
- **Source**: EIC W2; R3 W1; DA MAJOR 1.
- **Requirement**: A standing label per number-carrying clause, as the Abstract does for the registered and addendum results; reword the closing sentence so that it does not level the standings.
- **Acceptance criteria**: Every clause in B0085 and B0066 that carries a number names its standing; the Abstract's M2′ sentence carries "reported, not tested" or an equivalent descriptive label; the closing sentence distinguishes verdict cells from descriptive quantities.

**R3: "could not be separated at 0.4 points"**
- **Problem**: An equivalence-shaped statement about M2′, which the manuscript declares "reported, not tested"; 0.4 is neither the largest point estimate (+0.360) nor an interval bound; two intervals exclude zero in pooling's favour.
- **Source**: EIC W3; R1 W6; R3 W1; DA MAJOR 1 (severity SPLIT arbitrated; remedies compatible).
- **Requirement**: Replace in B0085 and B0066 with the descriptive form adopted under R7, carrying the first-addendum/descriptive label and the optimisation-steps confound.
- **Acceptance criteria**: The phrase "could not be separated" (or any equivalence-shaped phrase) no longer appears for M2′, and every number stated for M2′ is a value or bound printed in Table 1 (B0108).

**R4: "nothing measurable" / "no measurable effect"**
- **Problem**: The heading B0062, the Abstract B0006 and B0067 state an absence where Table 3 (B0113) shows a measured deficit on GN (−3.9 points, CI −5.3 to −2.4, p 0.00012) and Section 3.1 (B0047) insists the matched differences are "below the floor, not zero".
- **Source**: EIC W4; R1 W3 (D3 warn trigger); DA MAJOR 4.
- **Requirement**: Use "no measurable benefit", "below the registered floor" or "sign reversed"; describe the GN deficit without testing it.
- **Acceptance criteria**: "nothing measurable" and "no measurable effect" no longer appear; the L2 verdict (falsified) and the described GN deficit are both stated, each with its standing.

**R5: Verbatim registered rules and interpretation sentences**
- **Problem**: Section 2.6 states the rules in the authors' words and every Results subsection reports the fixed reading in indirect speech; the only checkable surface is the deposit, which is a placeholder at this stage.
- **Source**: R1 W1 (D1 warn trigger); DA MAJOR 3 (withheld interpretation never quoted).
- **Requirement**: One supplementary table, one row per hypothesis (R1, R3, M1, M1′, L1, L2), quoting the decision rule and both interpretation sentences verbatim with the governing hash state; quotation marks on the interpretation sentences in Results.
- **Acceptance criteria**: Each of the six hypotheses has a verbatim rule and two verbatim interpretation sentences in a supplementary table, and each Results subsection's fixed reading is visibly a quotation of that table.

**R6: Deviation record completeness**
- **Problem**: Two post-read decisions about registered analyses (M1 interpretation withheld for GN and BP; registered secondary path listed but not read) are disclosed in place but absent from the deviation record that lists only two pre-read deviations.
- **Source**: R1 W2; DA MAJOR 3.
- **Requirement**: Add both to Section 2.5, Table 4 and S2 Table with timing, rationale and consequence; quote the registered M1 interpretation and state why it is not applied (see also REV-M1-36 for the R3/M1 asymmetry).
- **Acceptance criteria**: The deviation record enumerates four items, two pre-read and two post-read, each with timing, rationale and consequence, and the registered M1 interpretation appears verbatim.

**R7: "never worse than retraining"**
- **Problem**: One of six M2′ point estimates is negative (D on BP, −0.083, CI −0.32 to +0.13) and four intervals span zero; a universal descriptive claim about a verdict-free quantity reads as a verdict.
- **Source**: R1 W6; DA MAJOR 2; R3 W1 disputed on remedy (direction SPLIT arbitrated for R1's bound + R3's label).
- **Requirement**: Bounded descriptive form (never worse by more than 0.3 points in any cell; point estimates −0.08 to +0.36; two of six intervals favour pooling; confounded with threefold steps) with the first-addendum/descriptive label, applied in B0006, B0020, B0055, B0056 and B0085.
- **Acceptance criteria**: No unqualified "never worse" remains; every M2′ statement gives the bound or the range as printed in Table 1 and its standing.

**R8: Self-contained forward model and reconstructor settings**
- **Problem**: Section 2.1 omits the items a domain reader needs to judge that the three operators saw the same data and were configured defensibly.
- **Source**: R2 W1 (D2 warn trigger); R3 W6 adjacent (noise figure not self-contained, REV-M1-32).
- **Requirement**: One paragraph (2.1 or S2 Table) listing pattern, electrode model, mesh, geometry ranges, GREIT training parameters, GN parametrisation, BP interpolation and the SNR definition in linear terms.
- **Acceptance criteria**: Each of the ten items named in R2 W1's absence anchor is stated in the manuscript or its supporting information without recourse to the code.

**R9: Training date of the reused GREIT networks vs the registration**
- **Problem**: Table 4 says "no arm trained, no contrast computed" when the registered state was written; Section 2.2 says the GREIT row reuses companion-study networks; the order is not stated.
- **Source**: R2 W2; R1 W7 and EIC question 3 adjacent.
- **Requirement**: State the date relative to hash 4b4c7a6d in B0028 and B0116; record a deviation if the networks predate the registration.
- **Acceptance criteria**: The reader can tell from the manuscript whether any trained arm existed when the registered state was hashed, and the deviation record is consistent with that fact.

**R10: Abstract mislabels the global-affine collapse**
- **Problem**: The collapse belongs to the registered M1 row; the Abstract attributes it to the addendum.
- **Source**: R2 W3.
- **Requirement**: Rewrite the sentence so the registered collapse and the addendum's per-source re-run each carry their own standing.
- **Acceptance criteria**: The Abstract's collapse sentence names the registered row, and the addendum clause names only the per-source result.

### Suggested Revisions (Should Fix / Consider)

| Transport ref | Roadmap id | Revision Item | Sub-Claim(s) | Severity | Evidence Anchor | Confidence | Source | Obligation class | Cost scope | Bounded consequence |
|---|---|---|---|---|---|---|---|---|---|---|
| S1 | REV-M1-5 | Rewrite the Conclusion's opening "does not appear under a change of reconstructor" in the registered vocabulary (below the registered floor under matched training; no evidence of growing under the shift; sign reversed held-out), and do not bundle matched-training cells on other reconstructors under "a change of reconstructor" | SC-5 | Minor | text: B0085 "does not appear under a change of reconstructor" | 4 — text-against-table reading within the manuscript | EIC (W4); corroborated DA (minor 6) | should_fix | sentence: B0085 | no_effect_wording → removed |
| S2 | REV-M1-6 | Fill the three material placeholders (Zenodo DOI for the minimal dataset and the four preregistration states; repository release tag; companion preprint DOI) or reword the related-manuscript statement to say a copy accompanies the submission | SC-6 | Minor | text: B0042 "Zenodo DOI, to be minted at submission" | 5 — visible placeholders | EIC (W5) | should_fix | other: submission package — B0042, B0089, B0097 (pre-submission gate; cannot be closed in a revision draft before minting) | placeholder_unresolved → resolved at submission |
| S3 | REV-M1-7 | Add the venue's required separate statements: Data Availability, Funding, Competing Interests (carrying the corresponding author's authorship of the architecture, already disclosed at B0081) and Ethics (simulation; no human or animal data; not applicable) | SC-7 | Minor | absence: front matter and Section 2.7 (B0042) — expected separate Data Availability, Funding, Competing Interests and Ethics statements; checked title page, Section 2.7, Acknowledgments, Related manuscript, Supporting information | 4 — venue requirements as the editor applies them; the submission system may collect some of these outside the manuscript file | EIC (W6) | should_fix | section: front/back matter near B0086–B0089 | required_statement_missing → added |
| S4 | REV-M1-10 | Add the reporting elements Section 2.6 promises for every cell: paired-difference SD per cell (Tables 1 and 3, or S1 Table with a pointer), MDE80 for the six E1 cells (Table 2), lung-channel Dice for every cell (or S1 Table), and replace "exact p values" with the normal approximation with continuity correction actually used | SC-10 | Minor | absence: Tables 1, 2 and 3 and their footnotes — expected the paired-difference SD per cell, MDE80 for the six E1 cells and the lung-channel Dice for every cell promised in Sections 2.3 and 2.6; checked Table 1, Table 2, Table 3, their footnotes and the S1 Table caption | 4 — statistical reporting completeness | R1 (W4) | should_fix | section: tools/recon_draft_tables.py (B0106, B0110, B0113), B0040, B0030, S1 Table caption B0094 | promised_elements_missing → reported |
| S5 | REV-M1-11 | State in Section 4.5 (B0077) that twelve verdict cells were informative and eight (four R3, two M1, two L2) were falsified in cells the design did not succeed in posing; carry the count into the contribution list (B0020) and the Abstract if the "mostly falsified" framing is kept | SC-11 | Minor | text: block B0077 "Of twenty verdict cells, twenty were falsified." | 4 — the eight cells are each identified as such in Sections 3.2, 3.3 and 3.6 | R1 (W5); corroborated DA (strongest counter-argument paragraph) | should_fix | sentence: B0077, B0020 | strength_mismatch → qualified |
| S6 | REV-M1-13 | State the training dates, library versions and code tag of the companion GREIT campaign (or retrain the GREIT row in this campaign); at minimum add the two-campaign confound to Section 3.4's qualifications (B0057) for the GREIT M2′ and GREIT-trained R3 cells | SC-13 | Minor | text: block B0028 "The GREIT row reuses seeds 0 to 29 of the companion study's 20 dB training" | 3 — deep-learning reproducibility; the effect is small relative to the stated confounds | R1 (W7) | should_fix | sentence: B0057, B0028 (retraining would be new_data; not required) | confound_unstated → stated |
| S7 | REV-M1-14 | Add one sentence in Section 2.2 or 2.7 stating whether deterministic kernels were enforced on the Apple-silicon/PyTorch 2.8.0 backend and, if not, how far a repeated seed moves (one re-run of one seed suffices) | SC-14 | Minor | absence: Sections 2.2 and 2.7 — expected a statement of whether deterministic kernels were enforced or how far a single seed reproduces run to run on the stated hardware; checked Sections 2.2, 2.6, 2.7 and the S2 Table caption | 3 — deep-learning reproducibility practice | R1 (W8) | should_fix | sentence: B0027/B0028 or B0042 (one seed re-run would be re_analysis: minimal) | reproducibility_statement_missing → added |
| S8 | REV-M1-15 | State once in Section 2.3 (B0031) the assumption under which the held-out loss is an upper bound (a change of reference style can only lower Dice relative to the held-out reconstructor's own cardiac image), next to the existing sentence that the attribution was not measured | SC-15 | Minor | text: block B0031 "is reported as an upper bound on the input-side generalisation loss, because the reference moves with the reconstructor" | 3 — reasoning about the endpoint; the direction is likely but unproven | R1 (W9); DA (MAJOR 6) argues the stronger position, not adopted (see REV-M1-37) | should_fix | sentence: B0031 | assumption_unstated → stated |
| S9 | REV-M1-16 | State in the Table 2 caption (B0109) and Section 3.4 (B0057) which no-retraining path M3′ is computed against (the registered path X→Y, as the printed values reproduce) and whether it is in points or a fraction; make the registered-path absolute Dice of the six no-retraining cells available (Table 2 or S1 Table with a pointer) | SC-16 | Minor | table: Table 2, M3′ B_wide / D (A1) column and its caption | 4 — derived from the printed values | R1 (W10); corroborated DA (minor 2) | should_fix | sentence: B0109, B0057; table via tools/recon_draft_tables.py (B0110) | definition_unstated → stated and recomputable |
| S10 | REV-M1-17 | Confirm against the per-seed file (results_recon/recon_results.json) that B_wide's held-out SD is 0.0949 on both the GREIT and BP cells of Table 3; if one value is a transcription error, correct it and the 9.49 floor that depends on it | SC-17 | Minor | table: Table 3, B_wide Dice (mean ± SD) column, GREIT and BP rows | 2 — a pattern check, not an error found | R1 (W11) | should_fix | other: transcription check — tools/recon_draft_tables.py (B0113), B0063 | transcription_unverified → verified or corrected |
| S11 | REV-M1-18 | In the Abstract (B0006) and the Section 4.1 heading or first sentence (B0065/B0066), state that the three signs of "the reconstructor behaves as a domain" are of exploratory (E1), descriptive (M2′) and tested (L1) standing respectively | SC-18 | Minor | text: block B0066 "All three signs named in Section 1.1 appeared." | 3 — standing of evidence; the labels are present in the body | R1 (W12); corroborated DA (strongest counter-argument paragraph) | should_fix | sentence: B0006, B0065, B0066 | standing_unqualified → qualified |
| S12 | REV-M1-22 | Correct the exploratory no-retraining range: the D arm on GN → BP under E1 loses 0.9672 − 0.629 = 33.8 points, so "19 to 33" (B0006, B0051, B0066, B0070) becomes "about 19 to 34" or is stated as the control arm's range; round "14 to 58 points outside the margin" (B0040, B0070) consistently with 13.9 and 57.5; check against results_recon/recon_results.json | SC-22 | Minor | table: Table 2 (block B0110) row GN → BP, E1 Dice 0.647 / 0.629, against Table 1 (block B0106) row R1-GN, D Dice 0.9672 | 4 — arithmetic from the printed tables | R2 (W4); corroborated DA (minor 1) | should_fix | sentence: B0006, B0051, B0066, B0070, B0040 (transcription check) | rounding_inconsistent → corrected |
| S13 | REV-M1-23 | Add one sentence giving, per reconstructor, the ratio of heart-only to lung-only amplitude in the difference frame or the reconstructed image, so that "weak cardiac component" is shown for this simulation (heart +1.0 contrast vs lungs −0.5) and not only motivated clinically | SC-23 | Minor | text: block B0023 "two lung inclusions at 0.5 S/m and one heart inclusion at 2.0 S/m" | 3 — the needed quantity is computable from the deposited data but not printed | R2 (W5) | should_fix | re_analysis: one descriptive quantity from deposited data; sentence at B0023 or B0013 | framing_unsupported_locally → supported |
| S14 | REV-M1-24 | Rephrase Section 4.3's "sources are already on comparable scales, as in multi-centre MRI" (B0072): MRI intensities are unitless and differ across scanners, which is why normalisation is studied there; the surviving point is that MRI site differences are far smaller than the two orders of magnitude seen here | SC-24 | Minor | text: block B0072 "Where sources are already on comparable scales, as in multi-centre magnetic resonance imaging (MRI)" | 3 — adjacent-field knowledge; the cited paper's own framing should be checked by the authors | R2 (W6) | should_fix | sentence: B0072 | adjacent_field_inaccuracy → corrected |
| S15 | REV-M1-25 | Add the original Sheffield attribution for back-projection beside the EIDORS toolbox citation (B0024); [UNVERIFIED] search lead: Barber and Brown, mid-1980s — verify through the R12d citation pipeline before adding | SC-25 | Minor | text: block B0024 "Back-projection (BP) used the Sheffield back-projection matrix distributed with EIDORS (Adler and Lionheart, 2006)" | 3 — origin of the method is well known; exact metadata not grounded in session materials | R2 (W7) [FIELD-NORM UNVERIFIED] | consider | sentence: B0024 + reference list B0092 (citation to be verified) | attribution_incomplete → completed if verified |
| S16 | REV-M1-26 | Verify the threshold Pulletz et al. (2006) actually used for the functional ROI; if it is 20%, change B0030 to "a threshold of the kind clinical region-of-interest methods apply" and either keep 25% as the registered choice with a reason or cite the source of 25% | SC-26 | Minor | text: block B0030 "the threshold clinical region-of-interest methods apply to EIT images (Pulletz et al., 2006)" | 2 — recollection of the cited paper's threshold, not verified here | R2 (W8) | should_fix | sentence: B0030 (verification first; the registered endpoint is unaffected) | attribution_unverified → verified or amended |
| S17 | REV-M1-27 | Verify against Zhao et al. (2014) whether all five ventilation indices showed no significant difference across the four algorithms; if any index differed, amend B0011 accordingly (the argument of Section 1.1 survives either way) | SC-27 | Minor | text: block B0011 "four algorithms applied to the same recordings gave five ventilation indices with no significant difference between them (Zhao et al., 2014)" | 2 — recollection of the cited paper's results, not verified here | R2 (W9) | should_fix | sentence: B0011 (verification first) | attribution_unverified → verified or amended |
| S18 | REV-M1-28 | Reconcile Section 4.1's "the benefit of pooling is one of inclusion, not of diversity" (B0067) with Section 4.4's "neither supported nor contradicted" (B0075), e.g. "two-source pooling showed no evidence of helping on a third source, so the benefit demonstrated here is one of inclusion; whether diversity adds anything was not resolved (Section 4.4)" | SC-28 | Minor | text: B0067 "within this study the benefit of pooling is one of inclusion, not of diversity" | 4 — the two sentences are compared within the manuscript; the field's reading of such a sentence is my competence | R3 (W2) | should_fix | sentence: B0067 | internal_inconsistency → reconciled |
| S19 | REV-M1-29 | Add the upper-bound qualification to the Section 3.5 heading (B0058; or remove the numbers from it) and a one-clause note to the Table 3 caption (B0112), so the manuscript's own rule that every held-out loss carries it holds on headings and tables too | SC-29 | Minor | text: B0058 "Pooled training does not generalise to a reconstructor outside the pool: 62, 16 and 36 points" | 4 — the rule is stated in the manuscript; locating the exceptions is a reading task | R3 (W3) | should_fix | sentence: B0058, B0112 (caption via tools/recon_draft_tables.py if generated) | qualification_missing → added |
| S20 | REV-M1-30 | Add, outside the fixed R3 interpretation sentence (B0049), a neutral clause stating the design fact that the shift tested here is a change of reconstructor and that other kinds (e.g. measurement-noise level) were not tested in this study; do not alter the fixed sentence | SC-30 | Minor | text: B0049 "whatever shift tolerance the branch has is specific to the kind of shift" | 3 — I can judge the reader's experience but not what the registration permits around the fixed sentence | R3 (W4) | consider | sentence: B0049 (clause adjacent to, not inside, the fixed sentence) | opacity_for_outside_reader → reduced |
| S21 | REV-M1-31 | Define "affine" at first use (B0028) as a fixed per-dataset location–scale standardisation (subtract the training-split mean, divide by its SD), "referred to below as that dataset's affine" | SC-31 | Minor | text: B0028 "one dataset-wide normalisation affine estimated from that dataset's training split and applied to inputs and targets" | 4 — terminology accessibility to the adjacent field is my remit | R3 (W5) | should_fix | sentence: B0028 | term_undefined → defined |
| S22 | REV-M1-32 | Add one clause at B0024 saying what ratio the noise figure is and why matching it makes two regularised linear reconstructors comparable (R2 confirms the setting is defensible, R2-S1) | SC-32 | Minor | text: B0024 "noise figure after Adler and Guardo (1996)" | 3 — I can report the gap for an outside reader but not the field's convention | R3 (W6); overlaps R2 (W1) | should_fix | sentence: B0024 | term_defined_by_citation_only → self-contained |
| S23 | REV-M1-33 | Disambiguate "reference": keep it for the target image (the reconstructor's own single-organ reconstruction) and rename the untested cells ("ref" in Table 1, "in-pool reference cells" in 3.5) e.g. "comparison cells" or "in-pool anchors" | SC-33 | Minor | text: B0059 "The six in-pool reference cells of the same rows scored 0.957 to 0.967" | 4 — a reading-clarity observation within my remit | R3 (W7) | consider | section: B0059, B0114, Table 1 legend (B0105/B0106 via tools/recon_draft_tables.py), B0046 | term_ambiguity → resolved (interacts with REV-M1-1's choice) |
| S24 | REV-M1-34 | Add one sentence in Section 4.7 (B0083) stating that the per-source affine requires the reconstructor identity at deployment (a domain label at test time; Karani et al., 2018 is the anchor already cited), whether that identity is available in the targeted clinical EIT systems, and that "the same reconstructor" must be defined as algorithm, implementation and hyperparameters (as 4.2 already says) | SC-34 | Minor | absence: Section 4.7 (B0083) — expected a statement of whether the reconstructor identity needed to select the per-source affine is available at deployment and what that requires; checked Sections 2.4, 4.2, 4.7 and the Conclusion | 4 — the test-time domain-label question is a standard one in my field; whether the identity is always available in EIT practice is for the authors to confirm | R3 (W8) | should_fix | sentence: B0083 | implication_unstated → stated |
| S25 | REV-M1-35 | Add a parenthetical pointer at B0078 ("a simulated review round") to the Acknowledgments (B0087) and the repository record, so the phrase is explained where it is first used | SC-35 | Minor | text: B0078 "the second addendum's rows were those a simulated review round, recorded in the repository before the addendum was written, had asked for" | 3 — accessibility observation; the editorial seat may have a view on where such disclosure belongs | R3 (W9) | consider | sentence: B0078 | forward_reference_unexplained → pointed |
| S26 | REV-M1-36 | State in one sentence (Section 3.3 B0053 or 2.5) why the fixed reading is applied to the four unreadable R3 cells (counted as falsified in the Abstract) but withheld for the two unreadable M1 cells, or treat the two cases alike; the panel does not presume which direction | SC-36 | Major | text: B0053 "the registered interpretation of a falsified M1 is not applied to them" | 4 — preregistration deviation reporting and logic of the stated rules | DA (MAJOR 3); R1 (W2) adjacent | should_fix | sentence: B0053, B0049 | asymmetric_application_unexplained → explained or removed |
| S27 | REV-M1-37 | Respond to the DA's position that "upper bound on the input-side generalisation loss" is unlicensed because the bounded quantity has no reconstructor-independent reference and the decomposition was not measured; the panel does not adopt relabelling (R2-S2, R3-S2, EIC-S2 regard the qualification as correct) but requires the assumption to be stated (REV-M1-15) | SC-37 | Major | text: B0031 "How much of a given loss is attributable to the reference style was not measured." | 3 — logic of the stated endpoint; domain mechanisms left to the domain seat | DA (MAJOR 6); disputed by R2 (S2), R3 (S2), EIC (S2) as strengths | consider | sentence: B0031 (response required; relabelling not required) | da_position_recorded → author response |
| S28 | REV-M1-38 | Rewrite Section 4.5's defence (B0078): Table 4 shows each addendum expected the falsifications that occurred (3/3 verdict hits), so the results met the authors' expectations; if the intended claim is that the results went against the authors' recipe, say exactly that, and drop "turned the pooled recipe from generalises into in-pool only" unless a prior generalisation claim is cited | SC-38 | Major | text: B0078 "Both addenda went against the authors' own recipe" | 3 — logic of the argument against Table 4; title reading | DA (MAJOR 7) | should_fix | sentence: B0078 | argument_overreach → corrected |
| S29 | REV-M1-39 | Respond to the DA's reading that the title (B0002) attaches "preregistered" to a leave-one-reconstructor-out design that exists only in the second addendum; EIC and R2 checked the title without objection (no exploratory number; within character limit); the panel does not require a title change but requires a response | SC-39 | Major | text: B0002 "A preregistered, parameter-matched study with leave-one-reconstructor-out training" | 3 — logic of the argument against Table 4; title reading | DA (MAJOR 7); not raised by EIC or R2, who checked the title | consider | sentence: B0002, B0003 (response required) | da_position_recorded → author response |
| S30 | REV-M1-40 | Make explicit in Section 2.5 (B0036) that the change of matching rule from GREIT's nominal to its realised noise figure is one of the two dated, pre-read deviations (as EIC-S3 and R2-S1 read it), so that "no setting or rule changed" and "the change of matching rule" do not sit side by side without timing | SC-40 | Minor | text: B0036 "the change of matching rule from GREIT's nominal to its realised value" | 3 — reading of the deviation record | DA (minor 3) | consider | sentence: B0036 | timing_implicit → explicit |
| S31 | REV-M1-41 | Either name who has claimed "reconstructor-agnostic" for this pipeline or reword B0069 so that it does not falsify a term nobody is shown to have claimed (e.g. keep only "any source-aware statement must read…") | SC-41 | Minor | text: B0069 "is falsified, and any source-aware statement must read" | 3 — logic of the argument | DA (minor 4) | consider | sentence: B0069 | straw_man_wording → removed or sourced |
| S32 | REV-M1-42 | Put the explanation of the held-out loss order as "the two-source pool's coverage of the held-out reconstructor" (B0059) in the conditional, consistent with the same section's later statement that mechanisms are untested | SC-42 | Minor | text: B0059 "is the two-source pool's coverage of the held-out reconstructor, not a ranking of reconstructors" | 3 — logic of the argument | DA (minor 5) | should_fix | sentence: B0059 | mechanism_stated_as_fact → conditional |
| S33 | REV-M1-43 | Reword contribution one (B0020): a null can only "extend" from a prior null, which is either the companion study (not relied on) or the GREIT reference cell (not tested); make the sentence consistent with the choice taken under REV-M1-1 | SC-43 | Minor | text: B0020 "the matched-training null of the branch extends to the two other conventional reconstructors" | 3 — logic of the argument | DA (minor 7); linked to EIC (W1) | should_fix | sentence: B0020 | presupposition_unsupported → removed |

> Transported metadata reaches every row (#574 A2/A3): Severity and Confidence are the first-listed source's per-finding tags (DA table rows carry the section band as severity and the table's Confidence cell); no fallback tags were needed — every card carries per-finding Severity and Confidence. Where a corroborating seat tagged a different severity, the Source column says so and the Consensus Analysis records the arbitration.

### Source-Traceability Checklist

> Immutable source order. No work order is suggested. The author chooses `will_address`, `wont_address` or `not_on_point` later in the separate author-adjudication checkpoint (collected by the PI, not emitted here).

- [ ] R1 (REV-M1-1) — obligation `must_fix`: GREIT matched cell — reference or verdict, applied consistently across Table 1, Abstract, 3.1 heading, Conclusion (and 2.5/Table 4 if verdict)
- [ ] R2 (REV-M1-2) — obligation `must_fix`: standing label per number-carrying clause in Conclusion, 4.1 and the Abstract's M2′ sentence; closing sentence does not level standings
- [ ] R3 (REV-M1-3) — obligation `must_fix`: remove "could not be separated at 0.4 points" (B0085, B0066); descriptive licensed form
- [ ] R4 (REV-M1-4) — obligation `must_fix`: remove "nothing measurable" / "no measurable effect" (B0062, B0006, B0067); registered vocabulary; GN deficit described
- [ ] R5 (REV-M1-8) — obligation `must_fix`: supplementary table quoting verbatim rules and interpretation sentences for R1, R3, M1, M1′, L1, L2; quotation marks in Results
- [ ] R6 (REV-M1-9) — obligation `must_fix`: add the two post-read decisions to the deviation record; quote the withheld M1 interpretation
- [ ] R7 (REV-M1-12) — obligation `must_fix`: bounded descriptive form for "never worse" in B0006, B0020, B0055, B0056, B0085
- [ ] R8 (REV-M1-19) — obligation `must_fix`: self-contained forward model and reconstructor settings in 2.1 or S2 Table
- [ ] R9 (REV-M1-20) — obligation `must_fix`: training date of reused GREIT networks relative to hash 4b4c7a6d; deviation if they predate it
- [ ] R10 (REV-M1-21) — obligation `must_fix`: Abstract attributes the global-affine collapse to the registered M1 row
- [ ] S1 (REV-M1-5) — obligation `should_fix`: Conclusion opening "does not appear" → registered vocabulary
- [ ] S2 (REV-M1-6) — obligation `should_fix`: fill Zenodo DOI, release tag, preprint DOI placeholders (pre-submission gate)
- [ ] S3 (REV-M1-7) — obligation `should_fix`: separate Data Availability, Funding, Competing Interests, Ethics statements
- [ ] S4 (REV-M1-10) — obligation `should_fix`: paired-difference SD, E1 MDE80, lung Dice per cell; "exact p" → approximation used
- [ ] S5 (REV-M1-11) — obligation `should_fix`: twelve informative / eight uninformative cells stated in 4.5 and contributions
- [ ] S6 (REV-M1-13) — obligation `should_fix`: two-campaign confound for GREIT row stated (dates, versions, tag)
- [ ] S7 (REV-M1-14) — obligation `should_fix`: determinism statement for the stated hardware/backend
- [ ] S8 (REV-M1-15) — obligation `should_fix`: non-negativity assumption behind the upper bound stated once in 2.3
- [ ] S9 (REV-M1-16) — obligation `should_fix`: M3′ path and unit stated; registered-path Dice recomputable
- [ ] S10 (REV-M1-17) — obligation `should_fix`: confirm identical 0.0949 SDs against recon_results.json
- [ ] S11 (REV-M1-18) — obligation `should_fix`: three signs' standings named in Abstract and 4.1
- [ ] S12 (REV-M1-22) — obligation `should_fix`: "19 to 33" → includes 33.8; margin distances rounded consistently
- [ ] S13 (REV-M1-23) — obligation `should_fix`: heart-to-lung amplitude ratio per reconstructor stated
- [ ] S14 (REV-M1-24) — obligation `should_fix`: multi-centre MRI "comparable scales" rephrased
- [ ] S15 (REV-M1-25) — obligation `consider`: original Sheffield BP attribution (verify first)
- [ ] S16 (REV-M1-26) — obligation `should_fix`: verify Pulletz 2006 threshold; amend attribution if 20%
- [ ] S17 (REV-M1-27) — obligation `should_fix`: verify Zhao 2014 "no significant difference" for all five indices
- [ ] S18 (REV-M1-28) — obligation `should_fix`: 4.1 "inclusion, not diversity" reconciled with 4.4
- [ ] S19 (REV-M1-29) — obligation `should_fix`: upper-bound qualification on 3.5 heading and Table 3 caption
- [ ] S20 (REV-M1-30) — obligation `consider`: neutral design-fact clause beside the fixed R3 sentence
- [ ] S21 (REV-M1-31) — obligation `should_fix`: define "affine" at first use
- [ ] S22 (REV-M1-32) — obligation `should_fix`: one clause defining noise figure and why matching it is fair
- [ ] S23 (REV-M1-33) — obligation `consider`: disambiguate "reference" (target image vs untested cells)
- [ ] S24 (REV-M1-34) — obligation `should_fix`: domain label at test time stated in 4.7
- [ ] S25 (REV-M1-35) — obligation `consider`: pointer for "a simulated review round" at B0078
- [ ] S26 (REV-M1-36) — obligation `should_fix`: explain or remove the R3/M1 asymmetry in applying the fixed reading
- [ ] S27 (REV-M1-37) — obligation `consider`: respond to DA's "upper bound unlicensed" position (relabelling not required)
- [ ] S28 (REV-M1-38) — obligation `should_fix`: 4.5 defence rewritten against Table 4's hit rates; no presupposed prior claim
- [ ] S29 (REV-M1-39) — obligation `consider`: respond to DA's reading of "preregistered … leave-one-reconstructor-out" in the title
- [ ] S30 (REV-M1-40) — obligation `consider`: timing of the matching-rule change explicit in 2.5
- [ ] S31 (REV-M1-41) — obligation `consider`: "reconstructor-agnostic is falsified" sourced or reworded
- [ ] S32 (REV-M1-42) — obligation `should_fix`: pool-coverage explanation in the conditional
- [ ] S33 (REV-M1-43) — obligation `should_fix`: contribution one's "extends" reconciled with REV-M1-1

Obligation counts: must_fix 10 · should_fix 25 · consider 8 · total 43.

### Journal-Supplied Deadline (Optional Transport)

- **Exact deadline from source letter**: NOT PROVIDED（內部 panel，無期刊來信）
- Do not infer a deadline, duration, or work estimate.

### Response Letter Template

請依 `templates/revision_response_template.md` 的格式逐項回應：每一個 Required Revision 的回應與修改說明；每一個 Suggested Revision 的回應（採納，或不採納的理由）；修訂稿的 change markup；新舊段落的 cross-reference table。上列 14 個 Questions for the authors 也請逐題回答。修訂後請重跑 citation-check（REV-M1-25、-26、-27 涉及引用內容），再進入 re-review。

### Closing

We encourage you to carefully consider the reviewers' comments and submit a substantially revised manuscript. Please note that the revised manuscript will undergo another round of review.

五席都認為這份手稿的數據、設計與統計站得住，blocking issues 全部是文字層的 standing 與措辭，而且全部可由改寫與一到兩張 supplementary table 解決；請在修訂時保留上文列出的優點，特別是 Table 4、upper-bound qualification 的全程攜帶、deviations 與 hit rates 的如實報告，以及對 companion manuscript 的獨立性。

---

## Part 3: Reviewer Report Summary (Appendix)

完整的五張 Phase 2 cards 與五張 Phase 1 commitments 在同目錄：`eic.phase2.md`、`methodology.phase2.md`、`domain.phase2.md`、`perspective.phase2.md`、`da.phase2.md`（及對應的 `*.phase1.md`）。

### Journal-Fit Review Report Summary (EIC)
- Role-scoped score: D5 = pass; D6 = block (repairable) | Confidence: per-finding only (W1–W6: 4, 4, 4, 4, 5, 4)
- Key Point: Within scope and in most surfaces exemplary at keeping the four standings apart; the D6 block is textual and repairable, bound to the GREIT reference cell carrying a verdict and the Conclusion dropping its standing labels — the two surfaces a reader quotes.

### Reviewer 1 (Methodology) Summary
- Role-scoped score: D1 = warn; D3 = warn | Confidence: per-finding only (W1–W12: 4, 4, 5, 4, 4, 4, 3, 3, 3, 4, 2, 3); AR1–AR12 all consistent
- Key Point: "Numbers are not the weakness of this manuscript"; the weaknesses are of verification (rules and interpretation sentences only paraphrased; two post-read decisions missing from the deviation record) and of wording ("nothing measurable" against a measured deficit).

### Reviewer 2 (Domain) Summary
- Role-scoped score: D2 = warn | Confidence: per-finding only (W1–W9: 4, 3, 4, 4, 3, 3, 3, 2, 2)
- Key Point: Domain content accurate and unusually disciplined; the warn rests on the forward model and reconstructor settings not being self-contained, plus a factual tension between Table 4's "no arm trained" and the reuse of companion-study GREIT networks.

### Reviewer 3 (Perspective) Summary
- Role-scoped score: D4 = warn | Confidence: per-finding only (W1–W9: 4, 4, 4, 3, 4, 3, 4, 4, 3)
- Key Point: Framing unusually readable for an outsider and the multi-source comparison fair; the weaknesses concentrate where the manuscript synthesises across its three evidence standards (Section 4.1 and the Conclusion), where labels drop away and M2′ drifts toward an equivalence reading.

### Devil's Advocate Summary
- Recommendation: N/A — findings only | D3 = block (repairable)
- Key Challenge: No CRITICAL issue. Seven MAJOR issues, all on the distance between what the registered rules license and what the Abstract and Conclusion say; "None of this overturns the data; all of it means the paper's claims about its own epistemic standing are not yet true of the text."
