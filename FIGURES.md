# 圖表紀錄（實驗室紀錄，非手稿）

**caption 是發表書寫，走 ARS。** 這裡記的是每張圖畫了什麼、資料從哪來、
回應哪一條審查意見。圖內的事實性標註由腳本從資料算出，不手打。

樣式共用 `tools/figstyle.py`。全部輸出向量 PDF（投稿用）+ PNG 200 dpi（閱讀用）。

## 回應的審查意見

- **R1-6**（真實審稿人）「Figures are of low visual quality… lack proper
  annotations, scale bars, or visual explanation. Table legends and figure
  captions are often insufficient」
- **R2-2**（真實審稿人）「figures are not effectively integrated into the text
  and lack adequate explanation」
- **M9**（ARS 路線圖）從頭重建：向量輸出、標註、比例尺、一致座標軸、自足圖註
- **M13 / B W4** 舊 Fig. 2(a) 用 0.991–0.999、2(b) 用 0.9825–0.9975，
  兩個邀請比較的面板無法比較
- Editage 信件記載圖表被標記但「I was unable to modify」，所以 2025-10 至今未動

## 圖列表

| 檔名 | 內容 | 腳本 | 資料 |
|---|---|---|---|
| `fig_arms` | 五臂並排，分支位置與解碼器寬度是唯二變數，右側列參數量 | `make_fig_arms.py` | `tools/arms.py` |
| `fig1_separability` | 前提：四分之一振幅閾值切混合影像，肺 DSC 0.948、心臟 0.000 | `make_fig1.py` | `data/v2` |
| `fig_task_and_noise` | 任務輸入、40 dB 對 20 dB、差值面板、兩個標的 | `make_fig_task.py` | `data/v2` + `~/work/sunet_sweep` |
| `fig_null_40db` | 40 dB 下各臂對 B_wide 的差，心臟與肺共用一個 y 軸 | `make_fig_null.py` | `results_v2_fix` |
| `fig_effect_bound` | 撤回宣稱 9.24 點 對 研究一 D−A、研究二 40 dB 與 20 dB；斷軸 | `make_fig_bound.py` | `results_v1_lung_fix`, `results_v2_fix`, `results_v2_snr20_heart_fix` |
| `fig_snr_sweep` | (a) 註冊掃描 → H3 確認 (b) 事後對照 → **通道特異性** | `make_fig_snr.py` | `results_v2_snr*_heart_fix` |
| `fig_predictions` | 模型實際輸出；不同架構同種子 vs 同架構不同種子 | `make_fig_preds.py` | `preds.npz` + `runs_v2/run_meta.json` |

保留 `arm_*.pdf`（PlotNeuralNet 的單一架構細部圖）作為補充材料。

## 比例尺的依據

假體是 `ng_mk_cyl_models` 半徑 2 的圓柱，**沒有宣告物理尺寸**。所以比例尺標
**模型單位**，不標公分——替一個合成圓柱編造人體尺寸就是造假。

實測確認：視野是內接圓（3228 / 4096 像素，對照 π/4 = 0.7854），
故 64 px 跨 4 個單位，**1 單位 = 16 px**。

若要對應真實胸腔尺寸，需要一個依據，目前沒有。

## 製圖過程中修掉的自身錯誤（都是這次要修的那一類）

1. **CI 乘了兩次 100** —— 誤差棒長 100 倍衝出畫布
2. **研究一的 CI 被軸裁掉** —— 裁掉的區間看起來像有界的區間，
   正好是 n=10 檢定力不足的反面
3. **「86×」是手打的**，圖上畫的是 bootstrap 上界 +0.100，正確是 **92×**。
   圖與自己的標註打架 —— 就是 B W4 的同一種缺陷。現在倍數一律從畫出的資料計算
4. **`fig_task_and_noise` 第一版宣稱 20 dB「visibly breaking down」，
   被自己的面板推翻** —— GREIT 是正則化反解，40 dB 與 20 dB 的輸入肉眼無法區分。
   改成畫差值面板並說出真相：擾動只有峰值的 **5.4%**，卻讓心臟 DSC 掉 **4.8 點**
5. **色標與面板標題互相覆蓋**；架構圖中 C/C_wide/D 的輸出頭與解碼器**沒有連線**

第 4 點值得單獨記住：**一張圖的敘述被它自己的資料推翻時，要改的是敘述。**

---

## 2026-09-18 全部重建：度量缺陷連帶汙染了圖

`METRIC_DEFECT_2026-09-18.md` 的缺陷不只影響數字，也影響圖本身，因為
**`make_fig_preds.py` 自己也在正規化空間算遮罩**——它產生的第一版
「DSC 1.000、masks coincide exactly」是同一個缺陷。

修法：`figstyle.py` 新增 `norm_affine()`（從 `runs_v2/run_meta.json` 讀回
訓練時的仿射，不重算）與 `qa_mask(img, fov, mu, sd)`（先還原尺度再取
四分之一振幅）。所有腳本共用。

### 重建時抓到的四個錯誤

1. **只改了一半的目錄。** `make_fig_snr.py` 面板 (b) 我改了 `diff()` 的來源，
   卻沒改誤差基線，於是修正後的差值配上舊基線，算出 +35.26 pp（正確 +15.36）。
   **改資料來源要一次改完，半套比不改更危險，因為它看起來像是新算的。**
2. **寫死的判定文字。** 面板 (b) 印著「contains zero」，但區間是計算出來的——
   修正後 CI 變成 [+11.39, +19.28]，圖上仍寫著「含 0」。
   改成從區間讀出來：`"contains zero" if lo <= 0 <= hi else "excludes zero"`。
3. **過時的軸範圍判斷。** `make_fig_bound.py` 用 `x > 1` 決定標註放左軸或右軸，
   那個門檻是左軸還只到 0.42 時寫的；左軸放寬到 2.75 後，20 dB 的上界標註
   被送到斷軸的另一側，看不見。改成用實際的 `get_xlim()` 判斷。
4. **敘事寫死在標題與圖說裡。** `fig_snr_sweep` 的主標題是
   「the mechanism offered for it does not」、面板 (b) 是「not channel-specific」，
   `fig_predictions` 整張建立在「五分之四的影格是 1.0000」之上——
   修正後 0/6 影格飽和，那個敘事整個不存在。

**共同的形態**：數字改成計算的之後，**判定與敘事仍然是打字打上去的**。
第 1、3 點是資料來源，第 2、4 點是結論措辭。四個都是同一件事的不同層次：
**凡是會隨資料改變的東西，都要從資料算出來，包括那句「所以呢」。**

---

## 2026-09-22／23：核心論文的主文配置（plan／outline 定案後）

主文四圖兩表，補充材料另列。全部程式生成；舊腳本與舊圖保留不刪。

| 手稿編號 | 檔名 | 腳本 | 資料 | 說明 |
|---|---|---|---|---|
| **Fig. 1** | `fig1_arms_and_task` | `make_fig1_combined.py` | `tools/arms.py` 參數量、`data/v2`、`~/work/sunet_sweep` | `fig_arms` ＋ `fig_task_and_noise` 合併：(a) 五臂；(b)–(g) 任務與 40 vs 20 dB 差值面板。面板 (g) 的「5.4%」是該幾何（index 1945）自己的值，圖說寫明 "this input"；資料集層級見 `RESULTS_STUDY2.md` 三之四 |
| **Fig. 2** | `fig1_separability` | `make_fig1.py` | `data/v2` | 不變 |
| **Fig. 3** | `fig_snr_sweep` | `make_fig_snr.py`（**09-22 改寫**） | `results_v2_snr*_heart_fix` | (a) 註冊掃描＋H3；(b) **改為五層級相對誤差下降折線**（心臟／肺），標題印出「heart CI excludes zero at 30, 20 dB only」——哪些層級不含 0 是從區間讀出來的 |
| **Fig. 4** | `fig_predictions` | `make_fig_preds.py` | `preds.npz` | 不變；TMI 頁數超過時壓單欄 |
| **Table 1** | `results/tables/table1_arms_40db.{md,tex}` | `make_tables.py` | `results_v2_fix/per_seed.csv` | 五臂 40 dB；取代 `fig_null_40db`；表註印出 H1 規則的兩條件與 D − B |
| **Table 2** | `results/tables/table2_snr_sweep.{md,tex}` | `make_tables.py` | `results_v2_snr*_heart_fix`、`results_v2_rel_err_sweep` | 五層級 × 兩通道：原始點差、dz、p、相對誤差下降、種子勝出 |
| S3 | `fig_s3_effect_sizes` | `make_fig_s3_effects.py` | `results_v1_lung_fix`、`results_v2_fix`、`results_v2_snr20_heart_fix` | **取代 `fig_effect_bound`**：無 9.24 參考線；畫出註冊的 SD 地板（0.670 點，算出來的），讓「40 dB 區間不含 0 但整段在地板之下」看得見 |

其他補充材料（不是圖）：`arm_*.pdf`、研究一全表、層級間種子相關矩陣、預註冊 §8 全文、度量缺陷精簡版、超參數與環境。

### 這一輪抓到的錯

1. **`make_tables.py` 的 LaTeX 巨集寫成雙反斜線**（`$\\pm$`）——在 heredoc 裡多轉義了一層。`grep` 產物才看到，
   不是看腳本看到的。R10 那條：驗證要對著產物。
2. **「5.4%」是單一幾何的值，不是資料集的。** 手稿原本會沿用 FIGURES 與 NOTES 的這個數字；
   `noise_perturbation.py` 算了全部 360 幀：峰值比中位數 8.5%、RMS 比 7.1%。5.4% 在分布下緣。
3. Fig. 1 (a) 的參數差印成 `+0.63%`（D 對 B_wide），預註冊寫 `−0.62%`（B_wide 對 D）。同一件事、不同基準；
   手稿用一種寫法（建議「D has 0.6% more parameters」），起草時注意。

## 2026-09-24：掃描擴成七個層級（§9.3），Fig. 3 主標題改為算出來的

`tools/{rel_err_sweep,make_tables,make_fig_snr}.py` 的層級清單由 `[60 50 40 30 20]` 改為
`[60 50 40 35 30 25 20]`。35／25 dB 的資料由 `gen_snr_sweep.m` 生成、在 mini 上計分。

**又抓到一次「敘事寫死」**：`fig_snr_sweep` 的主標題原本印著 "The advantage appears between
40 and 30 dB"——那是 10 dB 格點下的結論，加了 35 dB 之後就不對了，但它是打字打上去的，
不會自己改。現在從資料算兩個門檻：

- **可偵測**＝消掉天花板後的 CI 第一次不含 0 的層級（現為 35 dB）→ 括在 40–35 dB 之間
- **跨過地板**＝同時滿足「差值 > 對照種子 SD」與「Wilcoxon p < 0.05」的第一個層級（現為 30 dB）→ 括在 35–30 dB 之間

標題字串由這兩個計算結果組出來。**這是 FIGURES.md 第 9 點的同一種錯，第二次犯。**
教訓補強：加一個資料層級、改一次分析範圍，就要問「哪些標題／圖說裡的數字或判定是打字打上去的」。

同時把面板 (a) 的註解「40 dB — registered, instrument-realistic」改為「40 dB — registered
primary level」——`instrument-realistic` 四路查證無來源（見 `RESEARCH_PRIMER` §十三之二）。
