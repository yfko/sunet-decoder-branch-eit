"""Figure 1 for the core paper: the five arms (top) and the task (bottom).

Merges fig_arms and fig_task_and_noise into one double-column figure so that
the TMI 10-page limit holds four figures in the main text (OUTLINE section
"圖表計畫"). The two source scripts are left untouched; their drawing code is
reproduced here as functions. Everything printed on the figure is computed
from the data at plot time: the parameter counts come from figstyle.PARAMS
(which mirrors the frozen tools/arms.py), the noise-perturbation percentage and
the DSC cost from the sweep files and per_seed.csv.

Panel (a): only two things move between arms -- where the decoder splits and
how wide it is -- and the wide arms exist so that splitting is not confounded
with capacity. Panels (b)-(g): the mixed input, the two targets on the lung's
scale and the heart on its own, the 20 dB input, and the amplified difference:
GREIT is a regularised inverse, so 40 -> 20 dB moves the image by a few percent
of peak yet costs the control arm several DSC points on the heart channel.

Scale bars are in MODEL UNITS (ng_mk_cyl_models radius 2, no physical size
declared); 1 unit = 16 px on the 64-px grid.
"""
import sys
sys.path.insert(0, "tools")

from pathlib import Path

import h5py
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.colors import TwoSlopeNorm
from matplotlib.patches import FancyBboxPatch

from figstyle import HEART, INK, LUNG, MUTE, PARAMS, apply_style, footnote, per_seed, save

apply_style()
SWEEP = Path.home() / "work/sunet_sweep"
PX_PER_UNIT = 16.0
ENC, SPLIT, RULE, BOT, DEC, DECW = "#8fa8bd", "#b8860b", "#cfd6dd", "#5d7d99", "#c8b48a", "#b39a63"
ARMS = [
    ("B",      "one decoder, two output heads",                    "single", False),
    ("B_wide", "one decoder widened ×1.5312 — capacity control",   "single", True),
    ("C",      "splits at the last block",                         "late",   False),
    ("C_wide", "splits at the last block, widened",                "late",   True),
    ("D",      "splits at the bottleneck — earliest possible",     "early",  True),
]


# ------------------------------------------------------------------ (a) arms
def draw_arms(ax):
    ax.set_axis_off(); ax.set_xlim(0, 100); ax.set_ylim(0, 100)
    ROW_H, TOP = 17.0, 90.0
    XE, XB, XD, DW = 13.0, 34.0, 41.0, 41.0

    def block(x, y, w, h, colour, label=None, fs=6.6):
        ax.add_patch(FancyBboxPatch((x, y - h / 2), w, h, boxstyle="round,pad=0,rounding_size=.6",
                                    fc=colour, ec="none", zorder=3))
        if label:
            ax.text(x + w / 2, y, label, ha="center", va="center", fontsize=fs, color="white", zorder=4)

    for i, (name, note, layout, wide) in enumerate(ARMS):
        yc = TOP - i * ROW_H
        ax.text(1.0, yc, name, fontsize=10, color=INK, va="center", fontweight="bold", family="DejaVu Sans Mono")
        ax.text(1.0, yc - 5.0, note, fontsize=7.0, color=MUTE, va="center")
        for k in range(4):
            block(XE + k * 4.6, yc, 4.0, 4.0 + k * 1.1, ENC)
        block(XB, yc, 4.5, 9.0, BOT)
        dcol, dh = (DECW if wide else DEC), (1.42 if wide else 1.0)
        split_x = None
        if layout == "single":
            for k in range(4):
                block(XD + k * 7.4, yc, 6.2, (8.0 - k * 1.1) * dh, dcol)
            for j, (col, lab) in enumerate(((LUNG, "lung"), (HEART, "heart"))):
                yy = yc + (2.6 if j == 0 else -2.6)
                block(XD + DW - 6.6, yy, 4.6, 3.6, col, lab, fs=6.2)
                ax.plot([XD + 3 * 7.4 + 6.2, XD + DW - 6.6], [yc, yy], color=MUTE, lw=1.0, zorder=2)
        elif layout == "late":
            for k in range(3):
                block(XD + k * 7.4, yc, 6.2, (8.0 - k * 1.1) * dh, dcol)
            split_x = XD + 3 * 7.4 - 0.6
            for j, (col, lab) in enumerate(((LUNG, "lung"), (HEART, "heart"))):
                yy = yc + (3.4 if j == 0 else -3.4)
                block(XD + 3 * 7.4, yy, 6.2, 4.4 * dh, dcol)
                block(XD + DW - 6.6, yy, 4.6, 3.6, col, lab, fs=6.2)
                ax.plot([split_x, XD + 3 * 7.4], [yc, yy], color=MUTE, lw=1.0, zorder=2)
                ax.plot([XD + 3 * 7.4 + 6.2, XD + DW - 6.6], [yy, yy], color=MUTE, lw=1.0, zorder=2)
        else:
            split_x = XD - 1.4
            for j, (col, lab) in enumerate(((LUNG, "lung"), (HEART, "heart"))):
                yy = yc + (3.8 if j == 0 else -3.8)
                for k in range(4):
                    block(XD + k * 7.4, yy, 6.2, (5.0 - k * .7) * dh, dcol)
                block(XD + DW - 6.6, yy, 4.6, 3.6, col, lab, fs=6.2)
                ax.plot([XD + 3 * 7.4 + 6.2, XD + DW - 6.6], [yy, yy], color=MUTE, lw=1.0, zorder=2)
                ax.plot([split_x, XD], [yc, yy], color=MUTE, lw=1.0, zorder=2)
        if split_x is not None:
            ax.plot([split_x, split_x], [yc - 7.6, yc + 7.6], color=SPLIT, lw=1.4, ls=(0, (3, 2)), zorder=5)
            ax.text(split_x, yc + 8.4, "split", ha="center", fontsize=6.6, color=SPLIT, zorder=5)
        ax.text(99, yc, f"{PARAMS[name]:,}", ha="right", va="center", fontsize=8.4, color=INK, family="DejaVu Sans Mono")
        ax.text(99, yc - 4.2, "parameters", ha="right", va="center", fontsize=6.4, color=MUTE)
    for x, t in ((XE + 7, "encoder"), (XB + 2.2, "bottleneck"), (XD + 16, "decoder")):
        ax.text(x, TOP + 8.2, t, ha="center", fontsize=8.4, color=MUTE)
    ax.text(99, TOP + 8.2, "capacity", ha="right", fontsize=8.4, color=MUTE)
    ax.annotate("", xy=(XB + 4.5, TOP + 6.4), xytext=(XE, TOP + 6.4),
                arrowprops=dict(arrowstyle="|-|,widthA=.3,widthB=.3", color=RULE, lw=1))
    ax.text((XE + XB + 4.5) / 2, TOP + 4.4, "identical in all five arms", ha="center", fontsize=6.8, color=MUTE, style="italic")
    pd = 100 * (PARAMS["D"] - PARAMS["B_wide"]) / PARAMS["B_wide"]
    ax.text(50, 2.0,
            f"Held constant: encoder, block structure, L1 loss with 1.0/1.0 weights, Adam 1e-3 cosine to 1e-5, batch 16, "
            "≤200 epochs with early stopping,\nno augmentation, one dataset-wide normalisation, the same 58 seeds on the same data. "
            f"Primary contrast D − B_wide: {pd:+.2f}% parameters, identical supervision.",
            ha="center", va="bottom", fontsize=7.2, color=INK)
    ax.set_title("(a)  five arms: only the split position and the decoder width change",
                 fontsize=9.6, color=INK, loc="left", pad=4)


# ------------------------------------------------------------ (b)-(g) task
def mixed(level, idx):
    with h5py.File(SWEEP / f"v2_snr{level}/dataset.mat", "r") as f:
        return np.array(f["recon_mixed"][idx]).T


with h5py.File("data/v2/dataset.mat", "r") as f:
    test = np.array(f["D/idx_test"]).astype(int).ravel() - 1
    rh = np.array([f[r][()].ravel()[0] for r in f["D/geom/r_heart"][()].ravel()])
    pick = int(test[np.argsort(np.abs(rh[test] - np.median(rh[test])))[0]])
    lung = np.array(f["recon_lung"][pick]).T
    heart = np.array(f["recon_heart"][pick]).T
m40, m20 = mixed(40, pick), mixed(20, pick)
d = m20 - m40
peak = float(np.nanmax(np.abs(m40)))
frac = 100 * float(np.nanmax(np.abs(d))) / peak
dsc40 = per_seed("results_v2_snr40_heart_fix", "B_wide", "heart").mean()
dsc20 = per_seed("results_v2_snr20_heart_fix", "B_wide", "heart").mean()
hlim, dlim = float(np.nanmax(np.abs(heart))), float(np.nanmax(np.abs(d)))
print(f"  geometry {pick}; 20 dB differs from 40 dB by {frac:.1f}% of peak; heart DSC {dsc40:.4f} -> {dsc20:.4f}")

fig = plt.figure(figsize=(15.8, 10.2))
gs = fig.add_gridspec(2, 1, height_ratios=[5.6, 4.4], hspace=.02)
axA = fig.add_subplot(gs[0])
draw_arms(axA)
gsb = gs[1].subgridspec(1, 6, wspace=.08)
ax = [fig.add_subplot(gsb[k]) for k in range(6)]
norm = TwoSlopeNorm(0, -peak, peak)
im = ax[0].imshow(m40, cmap="RdBu_r", norm=norm)
ax[0].set_title("(b)  input, 40 dB\nlung + heart, registered level", fontsize=9.0, color=INK, pad=7, linespacing=1.5)
ax[1].imshow(lung, cmap="RdBu_r", norm=norm)
ax[1].set_title("(c)  lung reconstruction\ntarget, shared scale", fontsize=9.0, color=INK, pad=7, linespacing=1.5)
ax[2].imshow(heart, cmap="RdBu_r", norm=norm)
ax[2].set_title("(d)  heart reconstruction\nSAME scale as (b),(c)", fontsize=9.0, color=INK, pad=7, linespacing=1.5)
ax[2].annotate("almost invisible beside\nthe lung — the premise", (32, 47), ha="center", va="center",
               fontsize=7.2, color=HEART, style="italic", zorder=6)
imh = ax[3].imshow(heart, cmap="RdBu_r", norm=TwoSlopeNorm(0, -hlim, hlim))
ax[3].set_title("(e)  heart reconstruction\nits OWN scale", fontsize=9.0, color=INK, pad=7, linespacing=1.5)
ax[3].annotate(f"peak {hlim:.1f} vs the lung's\n{np.nanmax(np.abs(lung)):.1f} — {100*hlim/np.nanmax(np.abs(lung)):.0f}% of it",
               (32, 47), ha="center", va="center", fontsize=7.2, color=HEART, style="italic", zorder=6)
ax[4].imshow(m20, cmap="RdBu_r", norm=norm)
ax[4].set_title("(f)  input, 20 dB\nlowest level of the sweep", fontsize=9.0, color=INK, pad=7, linespacing=1.5)
imd = ax[5].imshow(d, cmap="PuOr_r", norm=TwoSlopeNorm(0, -dlim, dlim))
ax[5].set_title(f"(g)  (f) − (b)\npeak {frac:.1f}% of (b)", fontsize=9.0, color=INK, pad=7, linespacing=1.5)
for a in ax:
    a.set_xticks([]); a.set_yticks([])
    for sp in a.spines.values():
        sp.set_edgecolor("#e8ecf0")
    a.plot([3.0, 3.0 + PX_PER_UNIT], [60.0, 60.0], color=INK, lw=2.6, solid_capstyle="butt", zorder=5)
    a.text(3.0 + PX_PER_UNIT / 2, 58.0, "1 model unit", ha="center", va="bottom", fontsize=6.8, color=INK, zorder=5)
cb = fig.colorbar(im, ax=[ax[0], ax[1], ax[2]], fraction=.030, pad=.015, location="bottom")
cb.set_label("reconstructed conductivity change (GREIT units) — shared scale", fontsize=7.2)
cb.ax.tick_params(labelsize=7)
for mappable, axis in ((imh, ax[3]), (im, ax[4]), (imd, ax[5])):
    c = fig.colorbar(mappable, ax=[axis], fraction=.062, pad=.015, location="bottom")
    c.ax.tick_params(labelsize=7)

footnote(fig,
         f"(b)–(g): one test-split geometry (index {pick}), the median heart radius of the test split; every panel is an "
         "EIDORS GREIT reconstruction (three forward and three inverse solves per sample: mixed, lung only, heart only).\n"
         "(d) and (e) are the SAME reconstruction on two scales; that gap is what the decoder branch is meant to address, "
         "and heart DSC is the registered primary endpoint.\n"
         f"(g) GREIT is a regularised inverse and suppresses measurement noise before image space: 40 → 20 dB changes this "
         f"input by {frac:.1f}% of peak yet costs {100*(dsc40-dsc20):.1f} heart-DSC points (arm B_wide, 58 seeds). "
         "Scale bars are model units; 64 px = 4 units.", y=-.045)
save(fig, "fig1_arms_and_task")
