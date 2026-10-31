"""Fig 5 of the RECON paper: the remedies tested for a reconstructor change, at
matched parameter count.

    python3 tools/make_recon_fig5.py   -> figures/recon/Fig5.{pdf,png,tif}

Four layers (columns), one point pair per deployed reconstructor:
  1 retraining on the deployed reconstructor, Y -> Y         (registered; GREIT cell = ref)
  2 pooled, deployed reconstructor in the pool, mixed-ps -> Y (first addendum)
  3 pooled, deployed reconstructor out of the pool, loro_Y -> Y (second addendum)
  4 single source, no retraining, the two in-range cells GN -> BP and BP -> GN
    (registered path, i.e. the plain X__Y directory)
Upper panel: heart Dice of B_wide with D beside, mean over seeds 0-29 with 95%
percentile bootstrap CI (100,000 resamples, seed 20260904, seeds resampled; the
same boot() as tools/recon_results.py). Lower panel: D - B_wide in Dice points,
paired by seed, with its bootstrap CI. Means and CIs are cross-checked to 4
decimals against recon_results.json / recon_delta_ci.json wherever recorded.
"""
from __future__ import annotations

import numpy as np
import matplotlib.pyplot as plt

from recon_figstyle import (apply_style, save, load_cell, boot, results, delta_ci, agree,
                            CM, WMAX, INK, MUTE, GRID, ACCENT, ARM_COL)

NAME = {"greit": "GREIT", "gn": "GN", "bp": "BP"}
LAYERS = [
    ("Retraining on the\ndeployed reconstructor\n(Y → Y)", "registered\n(GREIT cell: ref)",
     [("greit__greit", "GREIT"), ("gn__gn", "GN"), ("bp__bp", "BP")]),
    ("Pooled training, deployed\nreconstructor in the pool\n(mixed-ps → Y)", "first addendum",
     [("mixedps__greit", "GREIT"), ("mixedps__gn", "GN"), ("mixedps__bp", "BP")]),
    ("Pooled training, deployed\nreconstructor outside the pool\n(loro-Y → Y)", "second addendum",
     [("loro_greit__greit", "GREIT"), ("loro_gn__gn", "GN"), ("loro_bp__bp", "BP")]),
    ("Single source,\nno retraining (X → Y),\nthe two in-range cells", "registered",
     [("gn__bp", "GN→BP"), ("bp__gn", "BP→GN")]),
]


def file_refs(R: dict, C: dict) -> dict:
    """cell -> list of (source, field, value) recorded in the result files."""
    ref: dict[str, list] = {}

    def put(cell, src, **kv):
        for k, v in kv.items():
            ref.setdefault(cell, []).append((src, k, v))

    g = R["greit_diagonal_reference"]["seeds_0_29"]
    put(g["cell"], "recon_results.greit_diagonal_reference.seeds_0_29",
        B_wide=g["B_wide_mean"], D=g["D_mean"], delta=g["diff"])
    for k, v in R["R1"].items():
        put(v["cell"], f"recon_results.R1.{k}", B_wide=v["B_wide_mean"], D=v["D_mean"], delta=v["diff"])
    for k, v in R["addendum_11"]["M1p"].items():
        if k.startswith("M1'"):
            put(v["cell"], f"recon_results.addendum_11.M1p.{k}",
                B_wide=v["B_wide_mean"], D=v["D_mean"], delta=v["diff"])
    for k, v in R["addendum_12"]["L2"].items():
        put(v["cell"], f"recon_results.addendum_12.L2.{k}", B_wide=v["B_wide_mean"], D=v["D_mean"],
            delta=v["diff"], delta_lo=v["diff_ci95"][0], delta_hi=v["diff_ci95"][1])
    for cell in ("gn__bp", "bp__gn"):
        v = R["sec_c_own_affine"][cell]
        put(cell, f"recon_results.sec_c_own_affine.{cell}",
            B_wide=v["B_wide_registered_affine"], D=v["D_registered_affine"],
            delta=v["delta_registered_affine"])
        x, y = cell.split("__")
        r3 = R["R3"][f"R3-({x.upper()}->{y.upper()})"]
        put(cell, f"recon_results.R3.{x.upper()}->{y.upper()}", delta=r3["delta_XY"])
    for k, v in C["tested_cells"].items():
        if v["n"] == 30:
            put(v["cell"], f"recon_delta_ci.tested_cells.{k}", delta=v["delta_mean"],
                delta_lo=v["delta_ci95"][0], delta_hi=v["delta_ci95"][1])
    return ref


def main() -> None:
    apply_style()
    R, C = results(), delta_ci()
    refs = file_refs(R, C)

    stats = {}
    n_checked = 0
    print("cell                 B_wide mean [95% CI]       D mean [95% CI]            "
          "D-B_wide points [95% CI]   checks")
    for _, _, cells in LAYERS:
        for cell, _ in cells:
            b, d = load_cell(cell, "B_wide"), load_cell(cell, "D")
            dd = d - b
            s = {"B_wide": b.mean(), "B_lo_hi": boot(b), "D": d.mean(), "D_lo_hi": boot(d),
                 "delta": dd.mean(), "delta_lo_hi": boot(dd)}
            got = {"B_wide": s["B_wide"], "D": s["D"], "delta": s["delta"],
                   "delta_lo": s["delta_lo_hi"][0], "delta_hi": s["delta_lo_hi"][1]}
            for src, field, v in refs.get(cell, []):
                agree(f"{cell} {field} vs {src}", got[field], v)
                n_checked += 1
            stats[cell] = s
            print(f"  {cell:18s} {s['B_wide']:.4f} [{s['B_lo_hi'][0]:.4f}, {s['B_lo_hi'][1]:.4f}]  "
                  f"{s['D']:.4f} [{s['D_lo_hi'][0]:.4f}, {s['D_lo_hi'][1]:.4f}]  "
                  f"{100 * s['delta']:+7.3f} [{100 * s['delta_lo_hi'][0]:+7.3f}, "
                  f"{100 * s['delta_lo_hi'][1]:+7.3f}]  {len(refs.get(cell, []))}")
    print(f"cross-checked {n_checked} recorded values to 4 decimals")

    # ---- x positions ---------------------------------------------------------
    xs, x, bounds = {}, 0.0, []
    for _, _, cells in LAYERS:
        x0 = x
        for cell, _ in cells:
            xs[cell] = x
            x += 1
        bounds.append((x0 - .5, x - .5))
        x += 0.55
    off = 0.17

    fig = plt.figure(figsize=((WMAX - 0.25) * CM, 12.6 * CM))
    gs = fig.add_gridspec(2, 1, height_ratios=[1.55, 1], hspace=0.12,
                          left=0.085, right=0.995, top=0.80, bottom=0.19)
    a = fig.add_subplot(gs[0])
    b_ = fig.add_subplot(gs[1], sharex=a)

    for cell, s in stats.items():
        xc = xs[cell]
        for arm, dx, key in (("B_wide", -off, "B"), ("D", off, "D")):
            m = s["B_wide"] if arm == "B_wide" else s["D"]
            lo, hi = s[f"{key}_lo_hi"]
            a.errorbar(xc + dx, m, yerr=[[m - lo], [hi - m]], fmt="o" if arm == "B_wide" else "s",
                       ms=4.2, color=ARM_COL[arm], ecolor=ARM_COL[arm], elinewidth=1.1, capsize=2,
                       zorder=3, label=arm if cell == "greit__greit" else None)
        a.text(xc, min(s["B_lo_hi"][0], s["D_lo_hi"][0]) - .035, f"{s['B_wide']:.3f}\n{s['D']:.3f}",
               ha="center", va="top", fontsize=8, color=INK, linespacing=1.15)
        dm, (dlo, dhi) = 100 * s["delta"], (100 * s["delta_lo_hi"][0], 100 * s["delta_lo_hi"][1])
        b_.errorbar(xc, dm, yerr=[[dm - dlo], [dhi - dm]], fmt="D", ms=3.8, color=INK, ecolor=INK,
                    elinewidth=1.1, capsize=2, zorder=3)
        b_.text(xc, max(dhi, 0.0) + .9, f"{dm:+.2f}".replace("-", "\u2212"), ha="center",
                va="bottom", fontsize=8, color=INK)

    a.set_ylim(0.0, 1.0)
    a.set_yticks(np.arange(0, 1.01, .2))
    a.set_ylabel("Heart Dice (mean, 95% CI)")
    a.legend(loc="lower left", ncol=2, bbox_to_anchor=(0.0, 0.0), handletextpad=.3, columnspacing=1.2)
    a.tick_params(labelbottom=False)
    a.grid(axis="x", visible=False)

    b_.axhline(0, color=INK, lw=.9, zorder=2)
    lo_all = min(100 * s["delta_lo_hi"][0] for s in stats.values())
    hi_all = max(100 * s["delta_lo_hi"][1] for s in stats.values())
    b_.set_ylim(np.floor(lo_all - 1), np.ceil(hi_all + 4.5))
    b_.set_ylabel("D − B_wide\n(Dice points, 95% CI)")
    b_.grid(axis="x", visible=False)
    b_.set_xticks([xs[c] for _, _, cells in LAYERS for c, _ in cells])
    b_.set_xticklabels([lab for _, _, cells in LAYERS for _, lab in cells], fontsize=8, color=INK)
    b_.tick_params(axis="x", length=0, pad=3)
    b_.set_xlim(bounds[0][0] - .15, bounds[-1][1] + .15)

    for k, ((title, standing, _), (x0, x1)) in enumerate(zip(LAYERS, bounds)):
        xm = (x0 + x1) / 2
        a.text(xm, 1.04, title, transform=a.get_xaxis_transform(), ha="center", va="bottom",
               fontsize=8, color=INK, linespacing=1.25)
        b_.text(xm, -0.20, standing, transform=b_.get_xaxis_transform(), ha="center", va="top",
                fontsize=8, color=INK, fontweight="bold", linespacing=1.2)
        if k:
            for ax_ in (a, b_):
                ax_.axvline(x0 - .275, color=GRID, lw=1.0, zorder=1)
    fig.text(0.085, 0.004, "x axis: deployed reconstructor Y (last layer: training → evaluation). "
             "Printed under each pair: B_wide and D means.\n"
             "n = 30 seeds per arm; 95% percentile bootstrap over seeds, 100,000 resamples.",
             linespacing=1.4,
             ha="left", va="bottom", fontsize=8, color=MUTE)
    save(fig, "Fig5", max_w_cm=WMAX)


if __name__ == "__main__":
    main()
