"""Supplementary figure S3: the three branching contrasts on one axis, with the
registered floor drawn in.

Replaces fig_effect_bound for the manuscript. That figure was built around the
withdrawn manuscript's 9.24-point claim as a reference line; the manuscript does
not name that figure (decision 2026-09-22), so the reference line goes and what
remains is the thing the paper actually needs to show: where each interval sits
relative to zero and relative to the registered effect-size floor.

The floor is B_wide's seed-to-seed SD on the heart channel at 40 dB -- the
"difference must exceed the control's seed SD" condition of the registered H1
rule (PREREGISTRATION_HEART.md section 3). Drawing it makes the rule-versus-
interval disagreement visible: the 40 dB interval excludes zero and lies
entirely below the floor. The floor is computed here, not typed.

Study 1's contrast is D - A on the lung channel (arm A exists only there);
study 2's are D - B_wide on the heart channel at the registered 40 dB and at
20 dB. They are labelled as different contrasts because they are.
"""
import sys
sys.path.insert(0, "tools")

import matplotlib.pyplot as plt
import numpy as np

from figstyle import (ACCENT, HEART, INK, MUTE, NULLC, apply_style, boot_ci,
                      footnote, per_seed, save)

apply_style()

ctrl40 = per_seed("results_v2_fix", "B_wide", "heart")
floor = float(ctrl40.std(ddof=1) * 100)                 # registered floor, pts
d40 = (per_seed("results_v2_fix", "D", "heart") - ctrl40) * 100
d20 = (per_seed("results_v2_snr20_heart_fix", "D", "heart")
       - per_seed("results_v2_snr20_heart_fix", "B_wide", "heart")) * 100
d1 = (per_seed("results_v1_lung_fix", "D", "lung", n=10)
      - per_seed("results_v1_lung_fix", "A", "lung", n=10)) * 100
rows = [
    (2, "study 1 — D − A, lung\nn = 10 seeds, homogeneous, no noise", d1, NULLC),
    (1, "study 2 — D − B_wide, heart\n40 dB, the registered endpoint (n = 58)", d40, HEART),
    (0, "study 2 — D − B_wide, heart\n20 dB, lowest level of the registered sweep", d20, HEART),
]

fig, ax = plt.subplots(figsize=(8.6, 3.6))
ax.axvline(0, color=INK, lw=1.1, zorder=2)
ax.axvline(floor, color=ACCENT, lw=1.2, ls=(0, (4, 3)), zorder=2)
ax.annotate(f"registered floor for H1:\nB_wide seed SD = {floor:.3f} pts",
            (floor, 2.62), xytext=(5, 0), textcoords="offset points", ha="left", va="bottom", fontsize=7.6, color=ACCENT)
for y, lab, d, col in rows:
    lo, hi = boot_ci(d)
    ax.plot([lo, hi], [y, y], color=col, lw=2.4, solid_capstyle="butt", zorder=3)
    ax.plot([lo, lo, np.nan, hi, hi], [y - .11, y + .11, np.nan, y - .11, y + .11],
            color=col, lw=1.6, zorder=3)
    ax.plot([d.mean()], [y], "o", ms=7, color=col, zorder=4)
    # read off the interval, never typed
    tag = ("excludes zero" if lo > 0 or hi < 0 else "contains zero")
    ax.annotate(f"{d.mean():+.3f} [{lo:+.3f}, {hi:+.3f}]  ·  {tag}",
                (hi, y), xytext=(6, 0), textcoords="offset points",
                va="center", fontsize=8.0, color=col)
ax.set_yticks([r[0] for r in rows]); ax.set_yticklabels([r[1] for r in rows], fontsize=8.4)
ax.set_ylim(-.6, 3.1)
lo1, _ = boot_ci(d1); _, hi2 = boot_ci(d20)
ax.set_xlim(min(-.25, lo1 - .1), hi2 + 1.55)
ax.set_xlabel("DSC advantage of the branched decoder  (percentage points)")
fig.suptitle("The 40 dB interval excludes zero and lies below the registered floor; "
             "the 20 dB interval does not overlap it", fontsize=10.2, color=INK, y=1.02)
footnote(fig,
         "Markers are means; bars are 95% percentile bootstrap CIs over seeds. "
         "The registered H1 rule requires the 40 dB difference to exceed the floor "
         "AND Wilcoxon p < 0.05; it meets neither.\nStudy 1's interval is wider "
         "because n = 10 and its endpoint is the lung channel at ceiling; it is shown "
         "for completeness, not as a comparable estimate.", y=-.16)
save(fig, "fig_s3_effect_sizes")
