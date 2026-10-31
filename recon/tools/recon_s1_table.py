"""S1 Table for the RECON tier-3 paper: per-seed heart- and lung-channel Dice for every cell of the design, the
registered-path and secondary-path values, E1, M3' and L3' in full (caption: 20_DRAFT_v6.md, S1 Table).

Reads only results_recon/<cell>/per_seed.csv (seeds 0-29, arms B_wide and D) and writes
  RECON_paper/manuscript/si/S1_Table.csv   long format, one row per (cell, path, arm, seed): heart_dsc, lung_dsc
  RECON_paper/manuscript/si/S1_Table_derived.csv  per-seed derived quantities: E1 DoD, registered DoD, M3', L3'
  RECON_paper/manuscript/si/S1_Table.xlsx  both sheets + a README sheet
Every number is copied from the per-seed files; nothing is typed. Means are cross-checked against results_recon/recon_results.json.
"""
import csv, json, sys
from pathlib import Path
import numpy as np
ROOT = Path(__file__).resolve().parents[1]; R = ROOT / "results_recon"; OUT = ROOT / "RECON_paper/manuscript/si"; OUT.mkdir(exist_ok=True)
SEEDS = list(range(30)); ARMS = ("B_wide", "D"); RECON = ("greit", "gn", "bp"); NAME = {"greit": "GREIT", "gn": "GN", "bp": "BP"}

def load(cell, arm, channel):
    got = {}
    with open(R / cell / "per_seed.csv") as fh:
        for r in csv.DictReader(fh):
            if r["arm"] == arm and r["channel"] == channel: got[int(r["seed"])] = float(r["dsc"])
    missing = [s for s in SEEDS if s not in got]; assert not missing, (cell, arm, channel, missing)
    return np.array([got[s] for s in SEEDS])

# ---- cell inventory: (dir, row label, evaluation reconstructor, path, standing)
cells = []
for y in RECON: cells.append((f"{y}__{y}", NAME[y], NAME[y], "registered (training set's affine)", "ref (re-scored companion networks)" if y == "greit" else "R (R1)"))
for x in RECON:
    for y in RECON:
        if x == y: continue
        cells.append((f"{x}__{y}", NAME[x], NAME[y], "registered (training set's affine)", "R (R3)"))
        cells.append((f"{x}__{y}_ownaffine", NAME[x], NAME[y], "registered secondary (evaluation set's affine; listed, not read)", "R (secondary path)"))
        cells.append((f"{x}__{y}_e1", NAME[x], NAME[y], "E1 (evaluation set's affine for input, training set's for output)", "A1 (exploratory, no verdict)"))
for y in RECON:
    cells.append((f"mixed__{y}", "mixed", NAME[y], "registered (single pooled affine)", "R (M1)"))
    cells.append((f"mixed__{y}_ownaffine", "mixed", NAME[y], "registered secondary (evaluation set's affine)", "R (secondary path)"))
    cells.append((f"mixedps__{y}", "mixed-ps", NAME[y], "per-source affine", "A1 (M1', M2', M3')"))
for h in RECON:
    for y in RECON:
        cells.append((f"loro_{h}__{y}", f"loro-{NAME[h]}", NAME[y], "per-source affine", "A2 (held-out cell: L1, L2)" if h == y else "A2 (in-pool comparison cell, no hypothesis)"))
assert len(cells) == 3 + 18 + 9 + 9 == 39 and len({c[0] for c in cells}) == 39

rows = []
for d, row, ev, path, standing in cells:
    for arm in ARMS:
        hh, ll = load(d, arm, "heart"), load(d, arm, "lung")
        for s in SEEDS: rows.append(dict(cell=d, training_row=row, evaluated_on=ev, path=path, standing=standing, arm=arm, seed=s, heart_dice=f"{hh[s]:.6f}", lung_dice=f"{ll[s]:.6f}"))
with open(OUT / "S1_Table.csv", "w", newline="") as fh:
    w = csv.DictWriter(fh, fieldnames=list(rows[0])); w.writeheader(); w.writerows(rows)

# ---- derived per-seed quantities (points = 100 x Dice)
der = []
def add(kind, cell, arm, vals, note):
    for s, v in zip(SEEDS, vals): der.append(dict(quantity=kind, cell=cell, arm=arm, seed=s, value_points=f"{100*v:.4f}", definition=note))
for x in RECON:
    for y in RECON:
        if x == y: continue
        dxx = load(f"{x}__{x}", "D", "heart") - load(f"{x}__{x}", "B_wide", "heart")
        dxy = load(f"{x}__{y}", "D", "heart") - load(f"{x}__{y}", "B_wide", "heart")
        de1 = load(f"{x}__{y}_e1", "D", "heart") - load(f"{x}__{y}_e1", "B_wide", "heart")
        add("R3 DoD (registered path)", f"{x}__{y}", "D-B_wide", dxy - dxx, "Delta(X->Y) - Delta(X->X), Delta = D - B_wide, registered path")
        add("E1 DoD", f"{x}__{y}_e1", "D-B_wide", de1 - dxx, "Delta(X->Y under E1) - Delta(X->X)")
        for arm in ARMS:
            add("M3'", f"mixedps__{y} vs {x}__{y}", arm, load(f"mixedps__{y}", arm, "heart") - load(f"{x}__{y}", arm, "heart"), "Dice(mixed-ps->Y) - Dice(X->Y, registered path)")
for y in RECON:
    for arm in ARMS:
        add("L3' vs specialised", f"loro_{y}__{y} vs {y}__{y}", arm, load(f"loro_{y}__{y}", arm, "heart") - load(f"{y}__{y}", arm, "heart"), "Dice(loro-Y->Y) - Dice(Y->Y)")
        for x in RECON:
            if x == y: continue
            add("L3' vs no-retraining", f"loro_{y}__{y} vs {x}__{y}", arm, load(f"loro_{y}__{y}", arm, "heart") - load(f"{x}__{y}", arm, "heart"), "Dice(loro-Y->Y) - Dice(X->Y, registered path)")
    add("L1 (B_wide)", f"loro_{y}__{y} vs mixedps__{y}", "B_wide", load(f"loro_{y}__{y}", "B_wide", "heart") - load(f"mixedps__{y}", "B_wide", "heart"), "B_wide: Dice(loro-Y->Y) - Dice(mixed-ps->Y)")
    add("M2'", f"mixedps__{y} vs {y}__{y}", "B_wide", load(f"mixedps__{y}", "B_wide", "heart") - load(f"{y}__{y}", "B_wide", "heart"), "B_wide: Dice(mixed-ps->Y) - Dice(Y->Y)")
    add("M2'", f"mixedps__{y} vs {y}__{y}", "D", load(f"mixedps__{y}", "D", "heart") - load(f"{y}__{y}", "D", "heart"), "D: Dice(mixed-ps->Y) - Dice(Y->Y)")
with open(OUT / "S1_Table_derived.csv", "w", newline="") as fh:
    w = csv.DictWriter(fh, fieldnames=list(der[0])); w.writeheader(); w.writerows(der)

# ---- cross-check against the aggregated results file
RES = json.load(open(R / "recon_results.json")); chk = 0
for k, v in list(RES["R1"].items()) + [("GREIT ref", RES["greit_diagonal_reference"]["seeds_0_29"])] + list(RES["M1"].items()) + list(RES["addendum_11"]["M1p"].items()):
    for arm in ARMS:
        m = load(v["cell"], arm, "heart").mean(); assert abs(m - v[f"{arm}_mean"]) < 1e-9, (k, arm, m, v[f"{arm}_mean"]); chk += 1
for k, v in RES["R3"].items():   # R3-(X->Y): dod = mean Delta(X->Y) - mean Delta(X->X)
    x, y = [s.strip().lower() for s in k[4:-1].split("->")]
    dxy = (load(f"{x}__{y}", "D", "heart") - load(f"{x}__{y}", "B_wide", "heart")).mean(); dxx = (load(f"{x}__{x}", "D", "heart") - load(f"{x}__{x}", "B_wide", "heart")).mean()
    assert abs(dxy - v["delta_XY"]) < 1e-9 and abs((dxy - dxx) - v["dod"]) < 1e-9, (k, dxy, v["delta_XY"], dxy - dxx, v["dod"]); chk += 2
for cell, v in RES["addendum_12"]["absolute_heart"].items():
    for arm in ARMS:
        h = load(cell, arm, "heart"); assert abs(h.mean() - v[arm][0]) < 1e-9 and abs(h.std(ddof=1) - v[arm][1]) < 1e-9, (cell, arm); chk += 1
print(f"S1 Table: {len(rows)} per-seed rows over {len(cells)} cells; {len(der)} derived rows; {chk} means cross-checked against recon_results.json")

# ---- xlsx
import openpyxl
wb = openpyxl.Workbook(); ws = wb.active; ws.title = "README"
for line in ["S1 Table. Per-seed heart- and lung-channel Dice for every cell of the design (RECON tier-3 paper).",
             "Sheet 'per_seed': one row per cell x path x arm x seed; heart_dice and lung_dice on the test split (360 frames), quarter-amplitude set, image units; seeds 0-29.",
             "Sheet 'derived': per-seed values of the R3 difference of differences (registered path), the E1 difference of differences, M3', L3' (both forms), L1 (B_wide) and M2', in Dice points (0.01 Dice = 1 point).",
             "Standing: R = registered (hash 4b4c7a6d...), A1 = first addendum (0060eedf...), A2 = second addendum (9589b298...), ref = GREIT reference row re-scored from the companion study's networks (no hypothesis).",
             "Generated by tools/recon_s1_table.py from results_recon/<cell>/per_seed.csv; nothing typed."]:
    ws.append([line])
for name, data in (("per_seed", rows), ("derived", der)):
    w2 = wb.create_sheet(name); w2.append(list(data[0]))
    for r in data: w2.append([float(x) if k in ("heart_dice", "lung_dice", "value_points") else (int(x) if k == "seed" else x) for k, x in r.items()])
wb.save(OUT / "S1_Table.xlsx"); print("wrote", OUT / "S1_Table.csv", OUT / "S1_Table_derived.csv", OUT / "S1_Table.xlsx")
