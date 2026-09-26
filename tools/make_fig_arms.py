"""Figure: the five arms on one page, with what is held constant made visible.

The existing figures/arm_*.pdf are six separate full-page PlotNeuralNet renders
with no parameter counts and overlapping channel labels. They show one network
in detail; this paper's argument is about what DIFFERS between networks and what
is held constant, so a comparison at a glance is the figure that is actually
needed. The detailed render of arm D remains available as supplementary.

Read off the figure: encoder, bottleneck, block structure, loss, optimiser,
schedule and data are identical across all five. Only two things move -- where
the decoder splits, and how wide it is -- and the wide arms exist precisely so
that splitting is not confounded with capacity.
"""
import sys
sys.path.insert(0, "tools")

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import FancyBboxPatch

from figstyle import HEART, INK, LUNG, MUTE, apply_style, footnote, save

apply_style()
ENC = "#8fa8bd"
SPLIT = "#b8860b"
RULE = "#cfd6dd"
BOT = "#5d7d99"
DEC = "#c8b48a"
DECW = "#b39a63"

# (name, params, note, decoder layout)
# layout: list of (stage_index, y_offset, wide?) ... described per arm below
ARMS = [
    ("B",      7_762_498, "one decoder, two output heads",        "single", False),
    ("B_wide", 10_743_738, "one decoder widened x1.5312 — CAPACITY CONTROL", "single", True),
    ("C",      7_798_498, "splits at the last block",             "late",   False),
    ("C_wide", 10_817_706, "splits at the last block, widened",   "late",   True),
    ("D",      10_811_298, "splits at the bottleneck — earliest possible", "early", True),
]

fig, ax = plt.subplots(figsize=(11.6, 6.4))
ax.set_axis_off()
ax.set_xlim(0, 100); ax.set_ylim(0, 100)

ROW_H, TOP = 17.0, 92.0
XE, XB, XD = 13.0, 34.0, 41.0     # encoder start, bottleneck, decoder start
DW = 41.0                          # decoder span


def block(x, y, w, h, colour, label=None, fs=6.8):
    ax.add_patch(FancyBboxPatch((x, y - h / 2), w, h,
                                boxstyle="round,pad=0,rounding_size=.6",
                                fc=colour, ec="none", zorder=3))
    if label:
        ax.text(x + w / 2, y, label, ha="center", va="center", fontsize=fs,
                color="white", zorder=4)


for i, (name, params, note, layout, wide) in enumerate(ARMS):
    yc = TOP - i * ROW_H
    ax.text(1.0, yc, name, fontsize=10.5, color=INK, va="center",
            fontweight="bold", family="DejaVu Sans Mono")
    ax.text(1.0, yc - 5.0, note, fontsize=7.2, color=MUTE, va="center")

    # encoder: identical in every arm
    for k in range(4):
        block(XE + k * 4.6, yc, 4.0, 4.0 + k * 1.1, ENC)
    block(XB, yc, 4.5, 9.0, BOT)

    dcol = DECW if wide else DEC
    dh = (1.42 if wide else 1.0)          # height carries width_mult, to scale

    if layout == "single":
        for k in range(4):
            block(XD + k * 7.4, yc, 6.2, (8.0 - k * 1.1) * dh, dcol)
        for j, (col, lab) in enumerate(((LUNG, "lung"), (HEART, "heart"))):
            yy = yc + (2.6 if j == 0 else -2.6)
            block(XD + DW - 6.6, yy, 4.6, 3.6, col, lab, fs=6.4)
        ax.plot([XD + 3 * 7.4 + 6.2, XD + DW - 6.6], [yc, yc + 2.6],
                color=MUTE, lw=1.0, zorder=2)
        ax.plot([XD + 3 * 7.4 + 6.2, XD + DW - 6.6], [yc, yc - 2.6],
                color=MUTE, lw=1.0, zorder=2)
        split_x = None
    elif layout == "late":
        for k in range(3):
            block(XD + k * 7.4, yc, 6.2, (8.0 - k * 1.1) * dh, dcol)
        split_x = XD + 3 * 7.4 - 0.6
        for j, (col, lab) in enumerate(((LUNG, "lung"), (HEART, "heart"))):
            yy = yc + (3.4 if j == 0 else -3.4)
            block(XD + 3 * 7.4, yy, 6.2, 4.4 * dh, dcol)
            block(XD + DW - 6.6, yy, 4.6, 3.6, col, lab, fs=6.4)
            ax.plot([split_x, XD + 3 * 7.4], [yc, yy], color=MUTE, lw=1.0, zorder=2)
            ax.plot([XD + 3 * 7.4 + 6.2, XD + DW - 6.6], [yy, yy],
                    color=MUTE, lw=1.0, zorder=2)
    else:                                  # early: split at the bottleneck
        split_x = XD - 1.4
        for j, (col, lab) in enumerate(((LUNG, "lung"), (HEART, "heart"))):
            yy = yc + (3.8 if j == 0 else -3.8)
            for k in range(4):
                block(XD + k * 7.4, yy, 6.2, (5.0 - k * .7) * dh, dcol)
            block(XD + DW - 6.6, yy, 4.6, 3.6, col, lab, fs=6.4)
            ax.plot([XD + 3 * 7.4 + 6.2, XD + DW - 6.6], [yy, yy],
                    color=MUTE, lw=1.0, zorder=2)
            ax.plot([split_x, XD], [yc, yy], color=MUTE, lw=1.0, zorder=2)

    if split_x is not None:
        ax.plot([split_x, split_x], [yc - 7.6, yc + 7.6], color=SPLIT,
                lw=1.4, ls=(0, (3, 2)), zorder=5)
        ax.text(split_x, yc + 8.4, "split", ha="center", fontsize=6.8,
                color=SPLIT, zorder=5)

    ax.text(99, yc, f"{params:,}", ha="right", va="center", fontsize=8.6,
            color=INK, family="DejaVu Sans Mono")
    ax.text(99, yc - 4.2, "parameters", ha="right", va="center", fontsize=6.6,
            color=MUTE)

# headers
for x, t in ((XE + 7, "encoder"), (XB + 2.2, "bottleneck"), (XD + 16, "decoder")):
    ax.text(x, TOP + 8.2, t, ha="center", fontsize=8.6, color=MUTE)
ax.text(99, TOP + 8.2, "capacity", ha="right", fontsize=8.6, color=MUTE)
ax.annotate("", xy=(XB + 4.5, TOP + 6.4), xytext=(XE, TOP + 6.4),
            arrowprops=dict(arrowstyle="|-|,widthA=.3,widthB=.3", color=RULE, lw=1))
ax.text((XE + XB + 4.5) / 2, TOP + 4.4, "identical in all five arms", ha="center",
        fontsize=7.0, color=MUTE, style="italic")

ax.text(50, 3.2,
        "Held constant across all five: encoder, block structure, L1 loss with "
        "1.0/1.0 weights, Adam 1e-3 cosine to 1e-5, batch 16,\n"
        "≤200 epochs with early stopping, no augmentation, one dataset-wide "
        "normalisation, and the same 58 seeds on the same data.",
        ha="center", va="bottom", fontsize=7.6, color=INK)

fig.suptitle("Five arms: only the split position and the decoder width change",
             fontsize=11, color=INK, y=.99)
footnote(fig,
         "Decoder block height is drawn proportional to width multiplier, so the "
         "wide arms are visibly wider. D against B_wide is the primary contrast: "
         "10,811,298 against 10,743,738 parameters, a 0.62% difference,\n"
         "identical supervision and identical data — so the only thing left to "
         "explain a difference would be whether the decoder is split. "
         "Arm A (one output, historical baseline) is dropped here: it has no "
         "heart head and cannot be scored on the primary endpoint.",
         y=-.04)
save(fig, "fig_arms")
