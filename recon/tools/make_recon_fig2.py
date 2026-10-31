"""Fig 2 of the RECON paper: the design matrix and its heart-Dice values.

    python3 tools/make_recon_fig2.py   -> figures/recon/Fig2.{pdf,png,tif}

8 training conditions x 3 evaluation reconstructors. Each cell prints the mean
heart Dice over seeds 0-29 of B_wide and of D, read from results_recon/<cell>/
per_seed.csv (registered path: the plain X__Y directory, not _e1 / _ownaffine),
and is coloured by B_wide. Matched-training (diagonal) cells of the single-source
rows are outlined; the held-out cells of the loro rows (loro_Y__Y) are marked.
Every printed mean is cross-checked against results_recon/recon_results.json to
4 decimals wherever the same cell is recorded there.
"""
from __future__ import annotations

import numpy as np
import matplotlib.pyplot as plt
from matplotlib import colors
from matplotlib.patches import Rectangle

from recon_figstyle import (apply_style, save, load_cell, results, agree, CM, W1,
                            INK, MUTE, GRID, ACCENT)

COLS = ["greit", "gn", "bp"]
COLNAME = {"greit": "GREIT", "gn": "GN", "bp": "BP"}
# (row key, label, sub-label, standing, group)
ROWS = [
    ("greit", "GREIT", "", "R", "single source"),
    ("gn", "GN", "", "R", "single source"),
    ("bp", "BP", "", "R", "single source"),
    ("mixed", "mixed", "single affine", "R", "pooled, all three"),
    ("mixedps", "mixed-ps", "per-source affine", "A1", "pooled, all three"),
    ("loro_greit", "loro-GREIT", "trained on GN + BP", "A2", "leave one out"),
    ("loro_gn", "loro-GN", "trained on GREIT + BP", "A2", "leave one out"),
    ("loro_bp", "loro-BP", "trained on GREIT + GN", "A2", "leave one out"),
]
GAP = 0.32          # vertical gap between row groups (cell units)


def file_refs(R: dict) -> dict:
    """cell -> (B_wide mean, D mean) wherever recon_results.json records the heart cell."""
    ref: dict[str, list[tuple[str, float, float]]] = {}

    def put(cell, src, b, d):
        ref.setdefault(cell, []).append((src, float(b), float(d)))

    g = R["greit_diagonal_reference"]["seeds_0_29"]
    put(g["cell"], "greit_diagonal_reference.seeds_0_29", g["B_wide_mean"], g["D_mean"])
    for k, v in R["R1"].items():
        put(v["cell"], f"R1.{k}", v["B_wide_mean"], v["D_mean"])
    for k, v in R["M1"].items():
        put(v["cell"], f"M1.{k}", v["B_wide_mean"], v["D_mean"])
    for k, v in R["sec_c_own_affine"].items():
        if "B_wide_registered_affine" in v:
            put(k, f"sec_c_own_affine.{k}", v["B_wide_registered_affine"], v["D_registered_affine"])
    for k, v in R["sec_d_absolute_heart"].items():
        put(k, f"sec_d_absolute_heart.{k}", v["B_wide"][0], v["D"][0])
    for k, v in R["addendum_11"]["M1p"].items():
        if k.startswith("M1'"):
            put(v["cell"], f"addendum_11.M1p.{k}", v["B_wide_mean"], v["D_mean"])
    for k, v in R["addendum_11"]["E1"].items():
        x, y = k[k.index("(") + 1:-1].lower().split("->")
        put(f"{x}__{y}", f"addendum_11.E1.{k}.registered", v["B_wide_registered"][0], v["D_registered"][0])
    for k, v in R["addendum_12"]["L2"].items():
        put(v["cell"], f"addendum_12.L2.{k}", v["B_wide_mean"], v["D_mean"])
    for k, v in R["addendum_12"]["absolute_heart"].items():
        put(k, f"addendum_12.absolute_heart.{k}", v["B_wide"][0], v["D"][0])
    return ref


def main() -> None:
    apply_style()
    R = results()
    refs = file_refs(R)

    vals: dict[str, tuple[float, float]] = {}
    n_checked = 0
    print("cell                     B_wide    D       (mean heart Dice, seeds 0-29)  cross-checks")
    for rk, *_ in ROWS:
        for c in COLS:
            cell = f"{rk}__{c}"
            b, d = load_cell(cell, "B_wide").mean(), load_cell(cell, "D").mean()
            vals[cell] = (b, d)
            for src, rb, rd in refs.get(cell, []):
                agree(f"{cell} B_wide vs {src}", b, rb)
                agree(f"{cell} D vs {src}", d, rd)
                n_checked += 1
            print(f"  {cell:22s} {b:.4f}  {d:.4f}   {len(refs.get(cell, []))} source(s)")
    unchecked = [c for c in vals if c not in refs]
    print(f"cross-checked {n_checked} (cell, source) pairs to 4 decimals; "
          f"cells with no record in recon_results.json: {unchecked or 'none'}")

    # ---- layout (data units: one cell = 1 x 1, rows run downward) ----------
    ys, y = [], 0.0
    for i, row in enumerate(ROWS):
        if i and row[4] != ROWS[i - 1][4]:
            y += GAP
        ys.append(y)
        y += 1
    y_end = y
    XL = -1.62                                   # left edge of the label area

    fig = plt.figure(figsize=((W1 - 0.2) * CM, 14.4 * CM))
    ax = fig.add_axes([0.0, 0.215, 0.995, 0.735])
    ax.set_xlim(XL, 3.0)
    ax.set_ylim(y_end + 0.02, -0.02)
    ax.axis("off")

    cmap = colors.LinearSegmentedColormap.from_list("dice", ["#f6f7f9", "#e3ecf5", "#9dbedf", "#6f9fcd"])
    norm = colors.Normalize(0.3, 1.0)
    bmin = min(v[0] for v in vals.values())
    if bmin < norm.vmin:
        raise SystemExit(f"colour scale floor {norm.vmin} above smallest B_wide mean {bmin}")

    for (rk, lab, sub, stand, grp), y0 in zip(ROWS, ys):
        for j, c in enumerate(COLS):
            cell = f"{rk}__{c}"
            b, d = vals[cell]
            ax.add_patch(Rectangle((j + .03, y0 + .04), .94, .92, fc=cmap(norm(b)), ec="white", lw=0))
            diag = rk == c
            held = rk == f"loro_{c}"
            tag = None
            if diag:
                ax.add_patch(Rectangle((j + .045, y0 + .055), .91, .89, fc="none", ec=INK, lw=1.5))
                tag = "matched, ref" if c == "greit" else "matched"
            if held:
                ax.add_patch(Rectangle((j + .045, y0 + .055), .91, .89, fc="none",
                                       ec=colors.to_rgba(ACCENT, .45), lw=0, hatch="///"))
                ax.add_patch(Rectangle((j + .045, y0 + .055), .91, .89, fc="none", ec=ACCENT,
                                       lw=1.6, ls=(0, (3, 1.6))))
                tag = "held out"
            box = dict(fc=cmap(norm(b)), ec="none", pad=1.2) if held else None
            yb, yd = (y0 + .52, y0 + .79) if tag else (y0 + .38, y0 + .66)
            ax.text(j + .5, yb, f"B_wide  {b:.4f}", ha="center", va="center", fontsize=8,
                    color=INK, fontweight="bold", bbox=box)
            ax.text(j + .5, yd, f"D  {d:.4f}", ha="center", va="center", fontsize=8,
                    color=INK, bbox=box)
            if tag:
                ax.text(j + .5, y0 + .245, tag, ha="center", va="center", fontsize=8,
                        color="#8a6508" if held else INK, style="italic", bbox=box)
        # row labels
        ax.text(-0.37, y0 + (.40 if sub else .5), lab, ha="right", va="center", fontsize=8.5, color=INK)
        if sub:
            ax.text(-0.37, y0 + .68, sub, ha="right", va="center", fontsize=8, color=MUTE)
        ax.text(-0.17, y0 + .5, stand, ha="center", va="center", fontsize=8.5, color=INK,
                fontweight="bold")
    # group brackets at the far left
    for grp in dict.fromkeys(r[4] for r in ROWS):
        yy = [y0 for r, y0 in zip(ROWS, ys) if r[4] == grp]
        top, bot = min(yy) + .08, max(yy) + .92
        ax.plot([XL + .13, XL + .13], [top, bot], color=MUTE, lw=.8)
        ax.text(XL + .07, (top + bot) / 2, grp, rotation=90, ha="center", va="center",
                fontsize=8, color=MUTE)

    # headers
    for j, c in enumerate(COLS):
        ax.text(j + .5, -.14, COLNAME[c], ha="center", va="bottom", fontsize=9, color=INK,
                fontweight="bold")
    ax.text(1.5, -.52, "Evaluation reconstructor", ha="center", va="bottom", fontsize=8.5, color=INK)
    ax.text(-0.37, -.14, "Training condition", ha="right", va="bottom", fontsize=8.5, color=INK)
    ax.text(-0.17, -.52, "Standing", ha="center", va="bottom", fontsize=8.5, color=INK)

    # colour bar and key
    cax = fig.add_axes([0.42, 0.172, 0.5, 0.017])
    cb = fig.colorbar(plt.cm.ScalarMappable(norm=norm, cmap=cmap), cax=cax, orientation="horizontal")
    cb.set_label("Cell colour: B_wide mean heart Dice", fontsize=8, color=INK, labelpad=2)
    cb.ax.xaxis.set_label_position("top")
    cb.ax.tick_params(labelsize=8, length=2, color=MUTE)
    cb.outline.set_edgecolor(GRID)
    key = ("R  registered    A1  first addendum    A2  second addendum\n"
           "ref  companion study's GREIT networks re-scored here; no hypothesis, no verdict\n"
           "Solid outline: matched training.  Dashed, hatched: reconstructor held out of training.\n"
           "Other single-source cells: no retraining, training set's affine.  n = 30 seeds per arm.")
    fig.text(0.02, 0.0, key, ha="left", va="bottom", fontsize=8, color=MUTE, linespacing=1.45)
    save(fig, "Fig2", max_w_cm=W1)


if __name__ == "__main__":
    main()
