"""Figure: what this study excludes, against what was originally claimed.

A null result is only worth reading if it says how small an effect it rules
out. The withdrawn manuscript reported +9.24 DSC points for decoder branching.
Two preregistered studies with matched capacity, supervision, task and training
budget cannot reproduce it. The ratio is computed from the data at plot time and
printed on the figure, never typed into this docstring -- an earlier version of
this file carried a hardcoded "86x" that disagreed with its own plotted bound.

The contrasts shown are NOT interchangeable and are labelled as such. Study 1 has
an arm A (single output, plain U-Net), so D - A there is the closest analogue of
the withdrawn manuscript's own comparison. Study 2 dropped arm A (it has no heart
head and cannot be scored on the registered endpoint), so its contrast is
D - B_wide, the capacity-matched control. Both are shown, and the 20 dB level is
included because that is where study 2's effect is largest.

The axis is broken because that ratio is the finding: on one linear scale the
measured interval would be invisible.
"""
import sys
sys.path.insert(0, "tools")

import matplotlib.pyplot as plt
import numpy as np

from figstyle import (ACCENT, HEART, INK, MUTE, NULLC, apply_style, boot_ci,
                      footnote, per_seed, save)

apply_style()

d2 = (per_seed("results_v2_fix", "D", "heart")
      - per_seed("results_v2_fix", "B_wide", "heart")) * 100
lo2, hi2 = boot_ci(d2)
d3 = (per_seed("results_v2_snr20_heart_fix", "D", "heart")
      - per_seed("results_v2_snr20_heart_fix", "B_wide", "heart")) * 100
lo3, hi3 = boot_ci(d3)
# arm A exists only in study 1, so this is the closest analogue of the
# withdrawn manuscript's own contrast (branched against a plain U-Net)
d1 = (per_seed("results_v1_lung_fix", "D", "lung", n=10)
      - per_seed("results_v1_lung_fix", "A", "lung", n=10)) * 100
lo1, hi1 = boot_ci(d1)
CLAIM = 9.24

fig, (axL, axR) = plt.subplots(1, 2, figsize=(10.4, 4.0), sharey=True,
                               gridspec_kw={"width_ratios": [3.1, 1]})
rows = [
    (3, "withdrawn manuscript\nD vs plain U-Net, one hand-picked image", CLAIM,
     None, None, ACCENT),
    (2, "study 1 — D − A, lung\nn = 10 seeds", d1.mean(), lo1, hi1, NULLC),
    (1, "study 2 — D − B_wide, heart\n40 dB, the registered endpoint",
     d2.mean(), lo2, hi2, HEART),
    (0, "study 2 — D − B_wide, heart\n20 dB, where the effect is largest",
     d3.mean(), lo3, hi3, HEART),
]
for ax in (axL, axR):
    ax.axvline(0, color=INK, lw=1.1, zorder=2)
    for y, _, m, lo, hi, col in rows:
        if lo is not None:
            ax.plot([lo, hi], [y, y], color=col, lw=2.4, solid_capstyle="butt", zorder=3)
            ax.plot([lo, lo, np.nan, hi, hi], [y-.11, y+.11, np.nan, y-.11, y+.11],
                    color=col, lw=1.6, zorder=3)
        ax.plot([m], [y], "o", ms=7, color=col, zorder=4)

# Wide enough to CONTAIN study 1's n=10 interval. A clipped CI reads as a
# bounded one, which is the opposite of what an underpowered study shows.
axL.set_xlim(-.20, 2.75); axR.set_xlim(9.0, 9.5)
axL.set_yticks([r[0] for r in rows])
axL.set_yticklabels([r[1] for r in rows], fontsize=8.4)
axL.set_ylim(-.6, 3.6)
axL.spines["right"].set_visible(False)
axR.spines["left"].set_visible(False)
axR.tick_params(left=False)
axR.grid(axis="y")
for ax, xs in ((axL, [0, .5, 1.0, 1.5, 2.0, 2.5]), (axR, [9.24])):
    ax.set_xticks(xs)
axR.set_xticklabels(["9.24"])

# axis-break marks
for ax, xx in ((axL, 1.0), (axR, 0.0)):
    for yy in (0, 1):
        ax.plot([xx], [yy], transform=ax.transAxes, marker=[(-.5,-1.2),(.5,1.2)],
                ms=7, color=MUTE, mec=MUTE, mew=1.2, clip_on=False, ls="none")

# The ratio is COMPUTED from the plotted bound, never typed in: a figure
# whose annotation disagrees with its own data is the defect the ARS review
# logged as B W4 against the withdrawn Fig. 2.
for x, y, t, c in [(hi2, 1, f"upper bound +{hi2:.3f}", HEART),
                   (hi3, 0, f"upper bound +{hi3:.3f}", HEART),
                   (CLAIM, 3, f"{CLAIM/hi2:.0f}× the registered endpoint's "
                              f"bound, {CLAIM/hi3:.1f}× the 20 dB bound", ACCENT)]:
    lo_l, hi_l = axL.get_xlim()
    (axL if lo_l <= x <= hi_l else axR).annotate(
        t, (x, y), xytext=(0, 13), textcoords="offset points",
        ha="center", fontsize=8.2, color=c)

axL.set_xlabel("DSC advantage of the branched decoder  (percentage points)",
               x=.68)
fig.suptitle("Nowhere in either study does the reported effect reappear",
             fontsize=10.6, color=INK, y=1.03)
footnote(fig,
         "Markers are means; bars are 95% percentile bootstrap CIs over seeds. "
         "The 9.24-point value has no interval: it came from a single image "
         "scored by a 37-line script,\nwith the compared models trained for 1, "
         "50 and 30 epochs on three different tasks.\n"
         "Study 1's interval is wider because n = 10; study 2 registered n = 58. "
         "Study 1's row is D − A because arm A (plain U-Net, one output) exists "
         "only there;\nstudy 2 dropped it, so its reference is B_wide, the "
         "capacity-matched control. The axis is broken between "
         "2.75 and 9.0 points.", y=-.20)
save(fig, "fig_effect_bound")
