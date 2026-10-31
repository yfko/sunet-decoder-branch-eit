# -*- coding: utf-8 -*-
"""Render RESULTS_RECON.md section 11 (PREREGISTRATION_RECON.md section 12: L1, L2, L3', in-pool
references, lung, figure) from the JSON files only, so no number in that section is typed by hand.

    python3 tools/render_recon_add12.py > /path/to/section11.md

Inputs: results_recon/recon_results.json["addendum_12"], results_recon/loro_preds_seed0.json,
results_recon/loro_mask_check_seed0.json, results_recon/run_meta_loro_*.json, results_recon/loro_gate.json.
"""
import json
from pathlib import Path

R = Path("results_recon")
res = json.loads((R / "recon_results.json").read_text())
A = res["addendum_12"]
preds = json.loads((R / "loro_preds_seed0.json").read_text())
mask = json.loads((R / "loro_mask_check_seed0.json").read_text())
gate = json.loads((R / "loro_gate.json").read_text())
meta = {y: json.loads((R / f"run_meta_loro_{y}.json").read_text()) for y in ("greit", "gn", "bp")}
sec_d = res["sec_d_absolute_heart"]
m1p = res["addendum_11"]["M1p"]
Y3 = ("greit", "gn", "bp")
U = {"greit": "GREIT", "gn": "GN", "bp": "BP"}


def pt(x, nd=3):
    return f"{100 * x:+.{nd}f}"


def ci(c, nd=3):
    return f"[{pt(c[0], nd)}, {pt(c[1], nd)}]"


def pr(p):
    return f"{p:.2g}" if p < 0.01 else f"{p:.2f}"


L = []
w = L.append
margin = A["L1_margin_points"]

w("## §11 Addendum §12：leave-one-reconstructor-out 三列（L1、L2、L3′ 與池內參考；2026-10-17 計分讀回，Fable 5.1）")
w("")
w(f"**本節是 §12 addendum 的結果（雜湊 `{meta['greit']['prereg_sha256'][:8]}…{meta['greit']['prereg_sha256'][-4:]}`，`PREREGISTRATION_RECON.sha256` 第四筆；§12.1：在 §11 結果讀過之後寫、標準同 §11、低於 §§1–9；規則與邊界在開跑前雜湊）。§0–§10 一個字都沒改（舊檔 `RESULTS_RECON.pre-add12_20261017.md`）。** 本節只寫數字與 §12.5 的機械判定；L3′ 與池內參考依 §12.5 **沒有判定**。§12.5 的效度規則：閘門（§12.4）已過，三列無論結果都讀，沒有任何一格因結果被擱置。解讀交 `RESULTS_RECON_判讀_Fable.md` 第三部分。")
w("")
w(f"執行紀錄：mini 2026-10-11 14:05:29 手動開跑（`tools/run_recon_loro_mini.sh`；三列依序 loro-GREIT → loro-GN → loro-BP，各兩行程）；`results_recon/run_meta_loro_{{greit,gn,bp}}.json`：prereg 雜湊三列皆 `{meta['greit']['prereg_sha256'][:8]}…`，資料集 `{meta['greit']['data_sha256'][:8]}…`（loro-GREIT）／`{meta['gn']['data_sha256'][:8]}…`（loro-GN）／`{meta['bp']['data_sha256'][:8]}…`（loro-BP），與 §12.4 相符；合併仿射 mu {meta['greit']['norm']['mu']:.1e}／{meta['gn']['norm']['mu']:.1e}／{meta['bp']['norm']['mu']:.1e}、sd {meta['greit']['norm']['sd']:.8f}／{meta['gn']['norm']['sd']:.8f}／{meta['bp']['norm']['sd']:.8f}（恆等，§12.4）；裝置 mps。三列各 60 個 checkpoint：loro-GREIT 10-13 03:50:18 齊（37.7 h）、loro-GN 10-14 16:44:59（36.9 h）、loro-BP 10-16 04:14:44（35.5 h；§12.6 估每列約 39 h），`tools/eval_recon_loro.sh` 接著計分九格至 04:21:40（`results_recon/recon_loro_train.log`）。train 與六份 A／B log 無 error、無 traceback。**§12.4 第六列（計分腳本 dry run）的收據（審查 REV-P3-7 補記）**：2026-10-11 14:05 之前在 mini（bash 3.2.57）跑 `DRY=1 bash tools/eval_recon_loro.sh ~/work/sunet_sweep`，印出九個 `evaluate.py` 呼叫——三個留出格（標 L1/L2，`--data <Y>/dataset.mat --runs runs_recon_loro_<Y> --out results_recon/loro_<Y>__<Y> --primary D B_wide --channel heart`，與 §12.3 逐字一致）與六個池內參考格，無 `--affine-from-data`；紀錄在 `NOTES_2026-09-22.txt` 2026-10-11 中午節 [14:05]，訓練 14:05:29 在此之後啟動。2026-10-17 13:03 在 Air 以同一腳本（SHA-256 `a801152c…`，與 mini 上的檔逐位元相同）重現，九個呼叫輸出存 `results_recon/eval_recon_loro_dryrun_20261017.txt`。九格 `per_seed.csv`／`per_image.csv`／`summary.json` 共 27 檔於 2026-10-17 拉回 Air，SHA-256 與 mini 逐檔相符；每格 D／B_wide × heart／lung × 種子 0–29，無缺。Air 與 mini 的 `evaluate.py` 雜湊 b96f33b1… 相同。")
w(f"統計：`tools/recon_results.py` 加 `addendum_12()`（舊版 `tools/recon_results.pre-add12_20261017.py`），在所有註冊量與 `addendum_11()` 之後才算；重跑後 `recon_results.json` 原有 14 個鍵逐值相同（`recon_results.pre-add12_20261017.json` 對照），新增鍵 `addendum_12`。**本節數字全取自 `recon_results.json[\"addendum_12\"]`。** bootstrap 設定同 §2（{res['n_boot']:,} 次、種子 {res['boot_seed']}、重抽種子不重抽影像）。計分路徑 §12.3：輸入與輸出都用評估集 Y 自己的訓練集仿射（無 `--affine-from-data`），**網路從未見過 Y 的影像**。單位：Dice 點（×100），與 §9 一致。")
w("")

# ---------------- L1 ----------------
w(f"### (a) L1：B_wide 在未見重建器上相對 mixed-ps 列的等價檢定（三格；邊界 ±{margin:.1f} 點事前寫死，§12.5）")
w("")
w(f"量：DSC_heart(B_wide, loro-Y→Y) − DSC_heart(B_wide, mixed-ps→Y)，種子 s 對種子 s 配對（30 對），95% percentile bootstrap CI。**整段 CI 落在 [−{margin:.1f}, +{margin:.1f}] 點內 → 成立；否則否證。** D 的同一量並列、不受測。每格分開報告，不合併。")
w("")
w("| 格 | 臂 | loro-Y→Y DSC（平均 ± SD） | mixed-ps→Y DSC | 差（點） | 95% CI（點） | 配對差 SD（點） | n | CI 全在 ±1.0 內 | 機械判定 |")
w("|---|---|---|---|---|---|---|---|---|---|")
for y in Y3:
    cell = A["L1"][f"L1-(LORO-{U[y]}->{U[y]})"]
    for arm in ("B_wide", "D"):
        q = cell[arm]
        lo_abs = A["absolute_heart"][f"loro_{y}__{y}"][arm]
        mp = m1p[f"M1'-(MIXED-PS->{U[y]})"]
        mp_abs = (mp[f"{arm}_mean"], mp[f"{arm}_sd"])
        name = f"**L1-(LORO-{U[y]}→{U[y]})**" if arm == "B_wide" else f"　（D 並列，不受測）"
        w(f"| {name} | {arm} | {lo_abs[0]:.4f} ± {lo_abs[1]:.4f} | {mp_abs[0]:.4f} ± {mp_abs[1]:.4f} | {pt(q['mean'])} | {ci(q['ci95'])} | {100*q['sd']:.3f} | {q['n']} | {'是' if q['within_margin'] else '否'} | **{q['verdict']}** |")
w("")
l1b = [A["L1"][f"L1-(LORO-{U[y]}->{U[y]})"]["B_wide"] for y in Y3]
w(f"**機械判定：三格全部否證**（B_wide 的差 {pt(l1b[0]['mean'],1)}／{pt(l1b[1]['mean'],1)}／{pt(l1b[2]['mean'],1)} 點，三個 CI 整段在 −{margin:.1f} 點以下，上限 {pt(l1b[0]['ci95'][1],1)}／{pt(l1b[1]['ci95'][1],1)}／{pt(l1b[2]['ci95'][1],1)} 點）。§12.5 寫死的預期是「loro-GREIT 否證、loro-GN 與 loro-BP 不確定；誠實的預期是三格否證、相對 mixed-ps 的損失 5–30 點」；實得損失 {-100*l1b[0]['mean']:.1f}／{-100*l1b[1]['mean']:.1f}／{-100*l1b[2]['mean']:.1f} 點（GREIT 與 BP 超出預期範圍的上緣，GN 在範圍內）。§12.5 固定的讀法（否證）：「配方對該重建器維持只限池內，損失報告為部署在未見重建器上的代價」。**L1 不改 R1、R3、M1、M1′ 的任何紀錄（§12.1、§12.5）。**")
w("")

# ---------------- L2 ----------------
w("### (b) L2：未見重建器上的分支效益（三格；規則同 R1，§12.5）")
w("")
w("規則：Δ ＝ D − B_wide 超過 B_wide 種子間 SD **且** Wilcoxon（雙尾、常態近似、連續性校正）p < 0.05 才成立；任一不符或符號反轉即否證。n = 30（種子 0–29）。Δ 的 95% CI、W 與「D > B_wide 種子數」照 RESULTS §10(a) 的欄位並列。")
w("")
w("| 格 | B_wide DSC（平均 ± SD） | D DSC | Δ（點） | 95% CI（點） | 地板＝B_wide SD（點） | 配對差 SD（點） | dz | W | Wilcoxon p | D > B_wide | Δ > 地板 | p < 0.05 | 機械判定 |")
w("|---|---|---|---|---|---|---|---|---|---|---|---|---|---|")
for y in Y3:
    q = A["L2"][f"L2-(LORO-{U[y]}->{U[y]})"]
    w(f"| **L2-(LORO-{U[y]}→{U[y]})** | {q['B_wide_mean']:.4f} ± {q['B_wide_sd']:.4f} | {q['D_mean']:.4f} ± {q['D_sd']:.4f} | {pt(q['diff'])} | {ci(q['diff_ci95'])} | {100*q['B_wide_sd']:.3f} | {100*q['diff_sd']:.3f} | {q['dz']:+.2f} | {q['W']:.0f} | {pr(q['p_wilcoxon'])} | {q['D_gt_B_wide_seeds']}/{q['n']} | {'是' if q['exceeds_sd'] else '否'} | {'是' if q['p_lt_05'] else '否'} | **{q['verdict']}** |")
w("")
l2 = [A["L2"][f"L2-(LORO-{U[y]}->{U[y]})"] for y in Y3]
w(f"**機械判定：三格全部否證（符號反轉）**：Δ {pt(l2[0]['diff'])}／{pt(l2[1]['diff'])}／{pt(l2[2]['diff'])} 點；loro-GN→GN 的 CI 不含零且 p {pr(l2[1]['p_wilcoxon'])}（D 低於 B_wide），另外兩格 CI 含零（p {pr(l2[0]['p_wilcoxon'])}、{pr(l2[2]['p_wilcoxon'])}）。§12.5 寫死的預期是「三格否證、差距在所有匹配格的量級（−0.02 到 +0.63 點）、在地板之下」；實得判定三格都中（3/3），幅度與方向都不在預期範圍（三格為負、−2.5 到 −3.9 點）。§12.5 固定的讀法（否證）：「匹配訓練的 null 延伸到網路未曾見過的重建器」。**L2 不改 R1、R3、M1、M1′ 的任何紀錄。**")
w("")

# ---------------- L3' ----------------
w("### (c) L3′：從未見過 Y 的代價、兩來源合併消掉多少單來源非對角損失（只報告，不判定，§12.5）")
w("")
w("DSC(loro-Y→Y) − DSC(Y→Y)，配對種子，Y→Y 是 §1 的對角格（GREIT 對角取種子 0–29）：")
w("")
w("| 量 | 平均（點） | 95% CI（點） |")
w("|---|---|---|")
for y in Y3:
    for arm in ("B_wide", "D"):
        q = A["L3p_vs_specialised"][f"{arm}: loro-{y}->{y} - {y}->{y}"]
        w(f"| {arm}: loro-{y}→{y} − {y}→{y} | {pt(q['mean'])} | {ci(q['ci95'])} |")
w("")
w("DSC(loro-Y→Y) − DSC(X→Y)，X ≠ Y，X→Y 是 §2 的註冊不重訓格（訓練集仿射；跨 GREIT 的四格帶 §11.2 的「退化／超出範圍」註記，依 §12.5 照附、**不描述為「重建器偏移的大小」**）：")
w("")
w("| 量 | 平均（點） | 95% CI（點） | 註冊格 X→Y 的輸入（§11.2） |")
w("|---|---|---|---|")
note = {"degenerate input": "退化（近常數）", "over-range input": "超出訓練範圍", "in-range input": "在訓練範圍內"}
for y in Y3:
    for x in Y3:
        if x == y:
            continue
        for arm in ("B_wide", "D"):
            q = A["L3p_vs_no_retraining"][f"{arm}: loro-{y}->{y} - {x}->{y}"]
            w(f"| {arm}: loro-{y}→{y} − {x}→{y} | {pt(q['mean'])} | {ci(q['ci95'])} | {note[q['registered_cell_input']]} |")
w("")
inr = [(k, v) for k, v in A["L3p_vs_no_retraining"].items() if v["registered_cell_input"] == "in-range input"]
w(f"十二個量中，相對專門訓練（上表）六個全負、CI 全不含零；相對單來源不重訓（下表）的符號依格而異：兩個輸入在範圍內的註冊格（BP→GN、GN→BP）對應的四個量為 " + "、".join(f"{pt(v['mean'],1)} {ci(v['ci95'],1)}" for _, v in inr) + "（三個 CI 含零、一個為負不含零）。")
w("")

# ---------------- in-pool refs + absolute ----------------
w("### (d) 每格心臟 DSC 絕對值，三列 × 三個評估集（種子 0–29，平均 ± SD；對角＝留出格 L1／L2，非對角＝兩來源池內參考，只報告）")
w("")
w("| 訓練 ↓ ／評估 → | GREIT | GN | BP |")
w("|---|---|---|---|")
for ho in Y3:
    cells = []
    for ev in Y3:
        q = A["absolute_heart"][f"loro_{ho}__{ev}"]
        s = f"D {q['D'][0]:.4f} ± {q['D'][1]:.4f}<br>B_wide {q['B_wide'][0]:.4f} ± {q['B_wide'][1]:.4f}"
        cells.append(f"**{s}**（留出）" if ho == ev else s)
    w(f"| **LORO-{U[ho]}**（池＝{'、'.join(U[z] for z in Y3 if z != ho)}） | " + " | ".join(cells) + " |")
w("")
refs = [A["absolute_heart"][f"loro_{ho}__{ev}"] for ho in Y3 for ev in Y3 if ho != ev]
bw = [r["B_wide"][0] for r in refs]; dd = [r["D"][0] for r in refs]
w("每格每臂的種子 min–max（種子 0–29；只報告；審查 REV-P3-3 補記，`recon_results.json[\"addendum_12\"][\"seed_range_heart\"]`）：")
w("")
w("| 格 | D min–max | B_wide min–max |")
w("|---|---|---|")
for ho in Y3:
    for ev in Y3:
        q = A["seed_range_heart"][f"loro_{ho}__{ev}"]
        tag = "（留出）" if ho == ev else ""
        w(f"| loro_{ho}__{ev}{tag} | {q['D'][0]:.3f}–{q['D'][1]:.3f} | {q['B_wide'][0]:.3f}–{q['B_wide'][1]:.3f} |")
w("")
w(f"六個池內參考格 B_wide {min(bw):.4f}–{max(bw):.4f}、D {min(dd):.4f}–{max(dd):.4f}（對照 §9(e) mixed-ps 三格 B_wide 0.9579–0.9662、D 0.9610–0.9682；§5(d) 對角 B_wide 0.9565–0.9639、D 0.9602–0.9672）。三個留出格的種子間 SD：B_wide {A['absolute_heart']['loro_greit__greit']['B_wide'][1]:.4f}／{A['absolute_heart']['loro_gn__gn']['B_wide'][1]:.4f}／{A['absolute_heart']['loro_bp__bp']['B_wide'][1]:.4f}、D {A['absolute_heart']['loro_greit__greit']['D'][1]:.4f}／{A['absolute_heart']['loro_gn__gn']['D'][1]:.4f}／{A['absolute_heart']['loro_bp__bp']['D'][1]:.4f}（對角與池內參考 0.0014–0.0063）。")
w("")

# ---------------- lung ----------------
w("### (e) 肺通道，三個留出格（同 §5(b) 的報法；H4 的預期是沒有差異）")
w("")
w("| 格 | B_wide 肺 DSC（平均 ± SD） | D 肺 DSC | Δ（點） | 地板（點） | Wilcoxon p |")
w("|---|---|---|---|---|---|")
for y in Y3:
    q = A["L2_lung"][f"loro_{y}__{y}"]
    w(f"| loro_{y}__{y} | {q['B_wide_mean']:.4f} ± {q['B_wide_sd']:.4f} | {q['D_mean']:.4f} ± {q['D_sd']:.4f} | {pt(q['diff'])} | {100*q['B_wide_sd']:.3f} | {pr(q['p_wilcoxon'])} |")
w("")
lg = [A["L2_lung"][f"loro_{y}__{y}"] for y in Y3]
w(f"肺通道在未見重建器上也掉（B_wide {lg[0]['B_wide_mean']:.3f}／{lg[1]['B_wide_mean']:.3f}／{lg[2]['B_wide_mean']:.3f}，對照 §5(b)、§9(a) 的池內格 0.985–0.988）；兩臂的 Δ 在 ±0.8 點內，loro-GN→GN 的 p {pr(lg[1]['p_wilcoxon'])} 但 Δ {pt(lg[1]['diff'])} 未超過地板 {100*lg[1]['B_wide_sd']:.3f}。")
w("")

# ---------------- figure ----------------
w("### (f) 圖（PRIMER 二.1c、五.3b／3c）：`results_recon/figs/loro_preds_seed0.png`、`results_recon/loro_preds_seed0.json`、`results_recon/loro_mask_check_seed0.json`")
w("")
w("`tools/recon_loro_preds.py`（照 `recon_mixed_ps_preds.py`；種子 0、§12.3 計分路徑、每列只畫留出的評估集）。看過。測試切分中位數：")
w("")
w("| 格（seed 0） | 輸入幀內 SD | 輸入範圍 | 預測 QA 覆蓋 | 目標 QA 覆蓋 | 預測背景／目標峰值 | 預測峰值／目標峰值 |")
w("|---|---|---|---|---|---|---|")
for y in Y3:
    for arm in ("D", "B_wide"):
        q = preds[f"{arm}|loro-{y}->{y}|own"]
        w(f"| {arm}: loro-{y}→{y} | {q['input_frame_sd']:.3f} | {q['input_min']:.2f} 到 {q['input_max']:.2f} | {q['pred_qa_cover']:.3f} | {q['target_qa_cover']:.3f} | {q['pred_background_over_target_peak']:+.3f} | {q['pred_peak_over_target_peak']:.2f} |")
w("")
sds = [preds[f"D|loro-{y}->{y}|own"]["input_frame_sd"] for y in Y3]
w(f"- **輸入**：三個留出集在自己的仿射下幀內 SD {min(sds):.3f}–{max(sds):.3f}，與訓練池同尺度（§12.4 閘門 max/min {gate['loro_greit']['input_frame_sd_max_over_min_incl_heldout']:.2f}；§9 mixed-ps 的 0.81–0.85 相同），不是 §3／§11.2 那種退化或超出範圍的輸入。")
g = {arm: preds[f"{arm}|loro-greit->greit|own"] for arm in ("D", "B_wide")}
n = {arm: preds[f"{arm}|loro-gn->gn|own"] for arm in ("D", "B_wide")}
b = {arm: preds[f"{arm}|loro-bp->bp|own"] for arm in ("D", "B_wide")}
w(f"- **輸出，三格三種型態**（圖上可見）：loro-GREIT→GREIT 的心臟輸出峰值只有目標的 {g['B_wide']['pred_peak_over_target_peak']:.2f}／{g['D']['pred_peak_over_target_peak']:.2f} 倍（B_wide／D）且在空間上散開，預測的四分之一振幅集覆蓋視野 {g['B_wide']['pred_qa_cover']:.2f}／{g['D']['pred_qa_cover']:.2f}（目標 {g['D']['target_qa_cover']:.3f}）；loro-GN→GN 的輸出形狀對、位置對，但峰值是目標的 {n['B_wide']['pred_peak_over_target_peak']:.1f}／{n['D']['pred_peak_over_target_peak']:.1f} 倍、背景抬到目標峰值的 {n['B_wide']['pred_background_over_target_peak']:+.2f}／{n['D']['pred_background_over_target_peak']:+.2f}，預測集比目標集小（{n['B_wide']['pred_qa_cover']:.3f}／{n['D']['pred_qa_cover']:.3f} 對 {n['D']['target_qa_cover']:.3f}；GN 的心臟目標本身帶一圈環狀暈）；loro-BP→BP 的輸出形狀對，峰值 {b['B_wide']['pred_peak_over_target_peak']:.2f}／{b['D']['pred_peak_over_target_peak']:.2f} 倍、背景為負（{b['B_wide']['pred_background_over_target_peak']:+.2f}／{b['D']['pred_background_over_target_peak']:+.2f}）。")
mg = {arm: mask[f"{arm}|loro-greit->greit|own"] for arm in ("D", "B_wide")}
mb = {arm: mask[f"{arm}|loro-bp->bp|own"] for arm in ("D", "B_wide")}
mn = {arm: mask[f"{arm}|loro-gn->gn|own"] for arm in ("D", "B_wide")}
w(f"- **與 §5(c) 的區分**（`tools/recon_loro_mask_check.py`，seed 0、探索性、不改計分）：§5(c) 的缺陷在 `evaluate.py` 用別的集合的仿射還原輸出，背景離開零、遮罩填滿視野。這裡還原用的是 Y 自己的仿射（§12.3，與 Y→Y、mixed-ps→Y、六個池內參考格同一路徑，那些格都是 0.96）。把每幀預測減去自己的背景中位數之後：loro-GREIT→GREIT 的覆蓋仍 {mg['B_wide']['pred_qa_cover_after_median_offset_removal']:.2f}／{mg['D']['pred_qa_cover_after_median_offset_removal']:.2f}（目標 0.086）、DSC 從 {mg['B_wide']['dsc_as_scored']:.3f}／{mg['D']['dsc_as_scored']:.3f} 只回到 {mg['B_wide']['dsc_after_median_offset_removal']:.3f}／{mg['D']['dsc_after_median_offset_removal']:.3f}——大遮罩主要是網路輸出本身在空間上散開（負瓣佔遮罩 {mg['B_wide']['mask_share_from_negative_pixels']:.2f}／{mg['D']['mask_share_from_negative_pixels']:.2f}），不是零點。loro-BP→BP 的遮罩有 {mb['B_wide']['mask_share_from_negative_pixels']:.2f}／{mb['D']['mask_share_from_negative_pixels']:.2f} 來自負背景，只取正值部分 DSC 從 {mb['B_wide']['dsc_as_scored']:.3f}／{mb['D']['dsc_as_scored']:.3f} 回到 {mb['B_wide']['dsc_positive_part_only']:.3f}／{mb['D']['dsc_positive_part_only']:.3f}——這格的損失有一部分是網路在未見重建器上輸出的負背景（網路自己的輸出，不是 `evaluate.py` 的還原）。loro-GN→GN 減背景後 DSC 反而降（{mn['B_wide']['dsc_as_scored']:.3f} → {mn['B_wide']['dsc_after_median_offset_removal']:.3f}），無零點成分。這些是描述；三格的計分照 §12.3 路徑、§12.5 效度規則不動。")
w("")

# ---------------- verdict table ----------------
w("### (g) §12 的機械判定總表（補 §7、§9(f)）")
w("")
w("| 假說 | 格 | 判定 |")
w("|---|---|---|")
w(f"| L1（等價，±{margin:.1f} 點） | loro-GREIT→GREIT、loro-GN→GN、loro-BP→BP | 三格都否證（B_wide 相對 mixed-ps {pt(l1b[0]['mean'],1)}／{pt(l1b[1]['mean'],1)}／{pt(l1b[2]['mean'],1)} 點，CI 整段在邊界之外） |")
w(f"| L2（R1 規則） | 同三格 | 三格都否證（符號反轉；Δ {pt(l2[0]['diff'],1)}／{pt(l2[1]['diff'],1)}／{pt(l2[2]['diff'],1)} 點，GN 格 p {pr(l2[1]['p_wilcoxon'])}） |")
w("| L3′、池內參考 | — | 只報告，無判定（§12.5） |")
w("")

w("### (h) 交給判斷類（Fable／PI）的事項，本檔不回答")
w("")
w(f"1. §12.5 固定讀法的套用：三格 L1 否證 → 成像篇的部署配方對三個重建器全部維持「只限池內」，損失（GREIT {-100*l1b[0]['mean']:.0f}／GN {-100*l1b[1]['mean']:.0f}／BP {-100*l1b[2]['mean']:.0f} 點）以「部署在未見重建器上的代價」報告；三格 L2 否證 → 「匹配訓練的 null 延伸到網路未曾見過的重建器」。")
w("2. L2 三格符號反轉、loro-GN→GN 的 CI 不含零：與 §9(d) E1 六格差中差五負的型態並列怎麼描述（§12.7：L3′ 與池內參考不能當判定；任何結果不改 R1、R3、M1、M1′）。")
w("3. (f) 三種失效型態（GREIT 散開、GN 過振幅、BP 負背景；**seed 0 一個種子的描述性診斷、不是 30 種子的格層級事實**，只有「不是計分缺陷」那一點由九格同路徑 0.96 支撐）與 BP 格的大種子 SD，在成像篇的硬體預註冊與第三級篇的 Limitations 裡怎麼放、帶什麼限定；GN 格的「目標是重建器自己的心臟影像、帶環狀暈」怎麼寫進 DSC 的定義但書（目標樣式對損失的貢獻未測）。")
w("4. 與 §12.5 事前預期的對照（L1 判定 3/3 中、幅度 1/3 在範圍內；L2 判定 3/3 中、幅度與方向 0/3）要照實寫。")
w("5. 文獻底 phase3 §三的缺口分析依「L1 否證」那一套寫（AlBadawy 2018、Yan 2020、Mårtensson 2020）；對照時要寫明那些留一來源研究的標籤不隨領域變（解剖），而本研究的 DSC 參考是留出重建器自己的單器官影像、隨重建器變，所以 16–62 點是輸入端推廣失敗的上界，不能與文獻的留一站點損失直接比大小（審查 REV-P3-13）。")
w("")
print("\n".join(L))
