"""Figure: what the two architectures actually output, on frames chosen by rule.

Every other figure shows data or statistics. A segmentation paper should show a
segmentation, and both referees said the figures do not explain themselves
(R1-6, R2-2).

HOW THE FRAMES WERE CHOSEN. The withdrawn manuscript reported a single
hand-picked image, so nothing here may be selected for how it makes an arm look.
The rule is fixed in advance: show the best- and worst-scoring frames of those
dumped, which brackets the range instead of implying a typical frame exists.

A NOTE ON WHAT THIS FIGURE USED TO SAY. Before 2026-09-18 it reported that five
of six frames scored exactly 1.0000 and that the endpoint was carried by the
sixth. That was the metric defect, not the data: the quarter-amplitude set was
taken in normalised units, where the heart mask covers 94.8% of the field of
view. Scored as registered, no frame is saturated.

Columns let the reader run the study's comparison by eye: B_wide seed 0 against
B_wide seed 1 is the same architecture with a different seed; B_wide against D is
a different architecture. Which of the two matters more depends on the noise
level, and that is the point -- at the registered 40 dB the within-arm seed SD
(0.43-0.67 DSC points) exceeds the D - B_wide difference (+0.223); at 20 dB the
difference (+2.097) exceeds it (1.08).
"""
import sys
sys.path.insert(0, "tools")

import argparse
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.colors import TwoSlopeNorm

from figstyle import (HEART, INK, MUTE, apply_style, dsc, footnote,
                      norm_affine, qa_mask, save)

apply_style()
# preds.npz holds arrays in NORMALISED units. The quarter-amplitude set is not
# affine-invariant, so it must be taken after undoing the dataset affine -- this
# file scored the first version of the figure in normalised space and produced
# "DSC 1.000, masks coincide exactly" on every panel, which was the defect, not
# the finding.
MU, SD = norm_affine()
COLS = [("B_wide\nseed 0", "pred_B_wide_s0_{lv}"),
        ("B_wide\nseed 1", "pred_B_wide_s1_{lv}"),
        ("D\nseed 0", "pred_D_s0_{lv}"),
        ("D\nseed 1", "pred_D_s1_{lv}")]


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--preds", type=Path, default=Path("preds.npz"))
    a = ap.parse_args()
    z = np.load(a.preds)
    fov = z["fov"]
    n = len(z["test_idx"])

    def scores(lv):
        return np.array([[dsc(qa_mask(z[k.format(lv=lv)][j, 1], fov, MU, SD),
                              qa_mask(z[f"true_heart_{lv}"][j], fov, MU, SD))
                          for _, k in COLS] for j in range(n)])

    s20 = scores(20)
    per_frame = s20.mean(axis=1)
    easy, hard = int(np.argmax(per_frame)), int(np.argmin(per_frame))
    print(f"  20 dB DSC across the {n} dumped frames: "
          f"{per_frame.min():.4f}–{per_frame.max():.4f}, "
          f"{int((per_frame >= 0.99995).sum())} saturated")
    print(f"  showing frame {easy} (best, {per_frame[easy]:.4f}) and "
          f"frame {hard} (worst, {per_frame[hard]:.4f})")

    ROWS = [(40, easy, "40 dB\nregistered level"),
            (20, easy, "20 dB\nbest frame"),
            (20, hard, "20 dB\nworst frame")]

    def show(a, img, norm, cmap="RdBu_r"):
        """Display with the non-FOV pixels blanked. GREIT reconstructs a circle
        into a square raster; the model still emits values in the corners, and
        they mean nothing."""
        return a.imshow(np.where(fov, img, np.nan), cmap=cmap, norm=norm)

    fig, ax = plt.subplots(3, 6, figsize=(14.4, 8.4))
    for r, (lv, j, rlab) in enumerate(ROWS):
        inp = z[f"input_{lv}"][j]
        gt = z[f"true_heart_{lv}"][j]
        gm = qa_mask(gt, fov, MU, SD)
        hlim = float(np.nanmax(np.abs(gt))) or 1.0
        hnorm = TwoSlopeNorm(0, -hlim, hlim)
        ilim = float(np.nanmax(np.abs(inp))) or 1.0

        show(ax[r, 0], inp, TwoSlopeNorm(0, -ilim, ilim))
        show(ax[r, 1], gt, hnorm)
        ax[r, 1].contour(gm.astype(float), levels=[.5], colors=[INK],
                         linewidths=1.1, linestyles="--")
        if r == 0:
            ax[r, 0].set_title("input\nlung + heart", fontsize=8.6, color=INK,
                               pad=6, linespacing=1.4)
            ax[r, 1].set_title("heart target\nquarter-amplitude set", fontsize=8.6,
                               color=INK, pad=6, linespacing=1.4)

        for c, (lab, key) in enumerate(COLS, start=2):
            p = z[key.format(lv=lv)][j, 1]           # channel 1 = heart
            pm = qa_mask(p, fov, MU, SD)
            d = dsc(pm, gm)
            show(ax[r, c], p, hnorm)
            ax[r, c].contour(gm.astype(float), levels=[.5], colors=[INK],
                             linewidths=1.0, linestyles="--")
            ax[r, c].contour(pm.astype(float), levels=[.5], colors=[HEART],
                             linewidths=1.2)
            if r == 0:
                ax[r, c].set_title(lab, fontsize=8.6, color=INK, pad=6,
                                   linespacing=1.4)
            ax[r, c].text(.5, .035, f"DSC {d:.3f}", transform=ax[r, c].transAxes,
                          ha="center", fontsize=8.4, color=HEART,
                          family="DejaVu Sans Mono", fontweight="bold")

        ax[r, 0].text(-.16, .5, rlab, transform=ax[r, 0].transAxes, rotation=90,
                      va="center", ha="center", fontsize=8.4, color=INK,
                      linespacing=1.4)

    for a_ in ax.ravel():
        a_.set_xticks([]); a_.set_yticks([])
        for sp in a_.spines.values():
            sp.set_edgecolor("#e8ecf0")
        a_.plot([3, 19], [60, 60], color=INK, lw=2.0, solid_capstyle="butt",
                zorder=5)

    fig.text(.472, .968, "← same architecture, different seed →", ha="center",
             fontsize=8.2, color=MUTE, style="italic")
    fig.text(.775, .968, "← same architecture, different seed →", ha="center",
             fontsize=8.2, color=MUTE, style="italic")
    fig.text(.624, .941, "└──────  different architecture  ──────┘",
             ha="center", fontsize=8.2, color=MUTE, style="italic")

    fig.suptitle("At the registered noise level the seed moves the output as "
                 "much as the architecture; at 20 dB it no longer does",
                 fontsize=11, color=INK, y=1.025)
    footnote(fig,
             "Heart channel. Dashed = the quarter-amplitude set of the heart's "
             "own reconstruction (the registered target); solid red = the "
             "model's own quarter-amplitude set, taken in image units. "
             "Bars are 1 model unit.\n"
             f"Frames are chosen by rule, not by eye: the best and the worst of "
             f"the {n} dumped test frames at 20 dB "
             f"({per_frame.min():.3f}–{per_frame.max():.3f}), which brackets the "
             "range rather than implying a typical frame.\n"
             "Over the registered 58 seeds, D − B_wide is +0.223 DSC points at "
             "40 dB (95% CI [+0.020, +0.441]) against a within-arm seed SD of "
             "0.43–0.67, and +2.097 points at 20 dB (CI [+1.642, +2.543]) "
             "against 1.08.",
             y=-.05)
    save(fig, "fig_predictions")


if __name__ == "__main__":
    main()
