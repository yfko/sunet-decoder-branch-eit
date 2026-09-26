"""Figure: no architecture differs from any other at the registered noise level.

Answers ARS review item B W4 / M13 directly. The withdrawn manuscript's Fig. 2
put a heart metric on 0.991-0.999 beside a total-accuracy metric on
0.9825-0.9975, so two panels that invited comparison could not be compared.
Here both channels are drawn on ONE shared axis in DSC points relative to the
capacity-matched control, which makes the comparison the point rather than an
accident of scaling.
"""
import sys
sys.path.insert(0, "tools")

import matplotlib.pyplot as plt
import numpy as np

from figstyle import (ARMS, HEART, LUNG, INK, MUTE, GRID, PARAMS,
                      apply_style, boot_ci, footnote, per_seed, save)

# Two short lines: the arm name, then what distinguishes it. Long labels
# collided at this figure width.
SHORT = {"B": "B\n1 dec.", "C": "C\n2 dec., late",
         "C_wide": "C_wide\n2 dec. late,\nwide", "D": "D\n2 dec., early"}

apply_style()
CTRL = "B_wide"
OTHER = [a for a in ARMS if a != CTRL]

fig, ax = plt.subplots(1, 2, figsize=(9.6, 4.1), sharey=True)

for k, (ch, colour, dirn, title) in enumerate([
        ("heart", HEART, "results_v2_fix", "(a)  heart — the registered primary endpoint"),
        ("lung",  LUNG,  "results_v2_fix", "(b)  lung — recorded, not tested (H4)")]):
    a = ax[k]
    c = per_seed(dirn, CTRL, ch)
    for i, arm in enumerate(OTHER):
        d = (per_seed(dirn, arm, ch) - c) * 100          # DSC points
        lo, hi = boot_ci(d)          # d is already in points
        a.errorbar(i, d.mean(), yerr=[[d.mean() - lo], [hi - d.mean()]],
                   fmt="o", ms=6, color=colour, ecolor=colour,
                   elinewidth=1.6, capsize=4, zorder=3)
        a.annotate(f"{d.mean():+.3f}", (i, hi), xytext=(0, 7),
                   textcoords="offset points", ha="center", fontsize=7.4,
                   color=colour)
    a.axhline(0, color=INK, lw=1.1, zorder=2)
    a.set_xticks(range(len(OTHER)))
    a.set_xticklabels([SHORT[x] for x in OTHER], fontsize=8.0)
    a.set_xlim(-.6, len(OTHER) - .4)
    a.set_title(title, fontsize=9.5, color=INK, pad=10, loc="left")
    if k == 0:
        a.set_ylabel(f"DSC difference from {CTRL}  (percentage points)")

ax[0].set_ylim(-.55, .55)
# NOT annotated as "all cross zero" any more: after the 2026-09-18 re-scoring
# the heart D contrast does not. The annotation is derived, never asserted.
for k, (ch, dirn) in enumerate((("heart", "results_v2_fix"),
                                ("lung", "results_v2_fix"))):
    c = per_seed(dirn, CTRL, ch)
    crosses = all(lo <= 0 <= hi for lo, hi in
                  (boot_ci((per_seed(dirn, a_, ch) - c) * 100) for a_ in OTHER))
    ax[k].annotate("every 95% CI crosses zero" if crosses
                   else "not every 95% CI crosses zero",
                   xy=(1.5, -.45), fontsize=8.8, color=MUTE, style="italic",
                   ha="center")

fig.suptitle("At the registered noise level the only arm that separates from "
             "the control is D, and only on the heart", fontsize=10.6,
             color=INK, y=1.035, x=.5)
footnote(fig,
         "Paired across the 58 registered seeds; reference is B_wide, the "
         "capacity-matched single-decoder control (10,743,738 parameters "
         "against D's 10,811,298, a 0.62% difference).\n"
         "Error bars are 95% percentile bootstrap CIs over seeds (100,000 "
         "resamples). Both panels share one y axis, so the two channels are "
         "directly comparable.",
         y=-.10)
save(fig, "fig_null_40db")
