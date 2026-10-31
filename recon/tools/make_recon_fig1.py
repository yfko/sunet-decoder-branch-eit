"""Fig 1 of the RECON paper: three reconstructors, one geometry, three amplitude scales.

    python3 tools/make_recon_fig1.py   -> figures/recon/Fig1.{pdf,png,tif}

Top row: mixed input of the first test-split frame (same index, same geometry, in
all three datasets) under GREIT, GN and BP; middle row: its single-organ heart
target. Each panel has its OWN symmetric colour scale, printed, because the point
is that the scales differ. Bottom: training-split mixed-image pixel values inside
the FOV for the three reconstructors on one common axis, with the SDs of
results_recon/scale_check.json printed and the two ratios computed here.
"""
from __future__ import annotations

import numpy as np
import matplotlib.pyplot as plt
from matplotlib import colors

from recon_figstyle import (apply_style, save, scale_check, read_split, read_frame,
                            train_pixels, RECONS, LONG, SCALE_KEY, CM, W1,
                            INK, MUTE, GRID, HEART, LUNG, ACCENT)

HIST_COL = {"GREIT": INK, "GN": LUNG, "BP": ACCENT}


def sig(v: float) -> str:
    """Three significant figures, no trailing exponent."""
    return f"{v:.3g}"


def main() -> None:
    apply_style()
    sc = scale_check()
    sd = {r: sc[SCALE_KEY[r]]["recon_mixed"]["sd"] for r in RECONS}
    r_gn, r_bp = sd["GREIT"] / sd["GN"], sd["GREIT"] / sd["BP"]
    print(f"SD (training split, mixed): " + ", ".join(f"{r} {sd[r]:.6g}" for r in RECONS))
    print(f"ratios: GREIT/GN = {r_gn:.3f} -> {round(r_gn)}, GREIT/BP = {r_bp:.3f} -> {round(r_bp)}")
    if (round(r_gn), round(r_bp)) != (161, 188):
        raise SystemExit(f"caption mismatch: ratios round to {round(r_gn)}, {round(r_bp)}, not 161, 188")

    # the first test-split frame; same index in all three datasets (asserted)
    splits = {r: read_split(r) for r in RECONS}
    i0 = int(splits["GREIT"]["test"][0])
    for r in RECONS:
        for k in ("train", "val", "test"):
            if not np.array_equal(splits[r][k], splits["GREIT"][k]):
                raise SystemExit(f"{r}: split '{k}' differs from GREIT")
    print(f"test frame: dataset index {i0} (0-based; first entry of idx_test)")

    frames = {r: read_frame(r, i0) for r in RECONS}
    pix = {r: train_pixels(r) for r in RECONS}
    for r in RECONS:                      # the histogram must be the data the SD came from
        got = float(pix[r].std())
        if abs(got - sd[r]) > 1e-9 * max(1.0, abs(sd[r])):
            raise SystemExit(f"{r}: recomputed SD {got} != scale_check {sd[r]}")

    fig = plt.figure(figsize=(W1 * CM, 12.6 * CM))
    gs = fig.add_gridspec(6, 3, height_ratios=[3.3, 3.3, 0.05, 1.25, 1.25, 1.25],
                          hspace=0.30, wspace=0.62,
                          left=0.115, right=0.92, top=0.955, bottom=0.105)
    cmap = plt.get_cmap("RdBu_r").copy()
    cmap.set_bad("white")
    for c, r in enumerate(RECONS):
        mixed, heart, mask = frames[r]
        for row, (img, what) in enumerate(((mixed, "mixed input"), (heart, "heart target"))):
            ax = fig.add_subplot(gs[row, c])
            lim = float(np.nanmax(np.abs(img)))
            im = ax.imshow(img, cmap=cmap, norm=colors.Normalize(-lim, lim),
                           interpolation="nearest")
            ax.set_xticks([]); ax.set_yticks([]); ax.grid(False)
            for s in ax.spines.values():
                s.set_visible(False)
            cb = fig.colorbar(im, ax=ax, fraction=0.046, pad=0.04)
            cb.set_ticks([-lim, 0, lim])
            cb.set_ticklabels([f"−{sig(lim)}", "0", sig(lim)])
            cb.ax.tick_params(labelsize=8, length=2, color=MUTE)
            cb.outline.set_edgecolor(GRID)
            if row == 0:
                ax.set_title(LONG[r], fontsize=9, color=INK, pad=4)
            if c == 0:
                ax.set_ylabel("Mixed input" if row == 0 else "Heart target",
                              fontsize=8.5, color=INK, labelpad=4)
            print(f"  {r:5s} {what:12s}: range {np.nanmin(img):+.4g} .. {np.nanmax(img):+.4g}, "
                  f"colour scale ±{sig(lim)}, FOV pixels {int(mask.sum())}")

    # bottom: three training-split amplitude distributions on one common x axis
    lo = min(float(p.min()) for p in pix.values())
    hi = max(float(p.max()) for p in pix.values())
    edges = np.linspace(lo, hi, 241)
    axes = []
    for k, r in enumerate(RECONS):
        ax = fig.add_subplot(gs[3 + k, :], sharex=axes[0] if axes else None)
        axes.append(ax)
        h, _ = np.histogram(pix[r], bins=edges)
        frac = h / h.sum()
        ax.stairs(frac, edges, color=HIST_COL[r], lw=0, fill=True, alpha=.85, zorder=2)
        ax.set_yscale("log")
        ax.set_ylim(1e-6, 3)
        ax.set_yticks([1e-5, 1e-1])
        ax.minorticks_off()
        ax.grid(axis="x", visible=False)
        note = f"{r}   SD {sig(sd[r])}"
        if r == "GN":
            note += f";  GREIT SD = {round(r_gn)} × GN"
        if r == "BP":
            note += f";  GREIT SD = {round(r_bp)} × BP"
        ax.text(0.015, 0.95, note, transform=ax.transAxes, ha="left", va="top",
                fontsize=8, color=INK)
        if r != RECONS[-1]:
            ax.tick_params(labelbottom=False)
        print(f"  {r:5s} training-split pixels n = {pix[r].size}, range {pix[r].min():+.4g} .. "
              f"{pix[r].max():+.4g}, SD {sd[r]:.6g}, bins occupied {int((h > 0).sum())} of {h.size}")
    axes[0].set_xlim(lo, hi)
    axes[1].set_ylabel("Fraction of pixels")
    axes[-1].set_xlabel("Mixed-image pixel value inside the field of view (image units, "
                        f"training split)\none set of bins for all three, width {sig(edges[1] - edges[0])}",
                        linespacing=1.5)
    save(fig, "Fig1", max_w_cm=W1)


if __name__ == "__main__":
    main()
