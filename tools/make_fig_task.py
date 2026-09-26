"""Figure: the task, and why 20 dB matters even though it does not look like it.

R1-6 asked for scale bars and "visual explanation"; R2-2 said the figures do not
explain themselves. This one shows the task directly and settles a question the
results raise on their own.

WHAT THIS FIGURE HAD TO BE REWRITTEN TO SAY. The first version claimed 20 dB is
a regime "where the reconstruction is visibly breaking down". Its own panels
refuted that: the 40 dB and 20 dB inputs are indistinguishable by eye. GREIT is
a regularised inverse, so it suppresses measurement noise before it ever reaches
image space -- the 20 dB input differs from the 40 dB one by 5.4% of peak signal
(RMS 0.257 against 4.811). Yet that 5.4% costs the heart channel 4.8 DSC points
(0.989 -> 0.940). So the difference gets its own amplified panel, and the figure
says the true thing instead of the expected one.

SCALE. The phantom is ng_mk_cyl_models with radius 2 in model units and no
declared physical size, so bars are in MODEL UNITS -- labelling them in
centimetres would mean inventing a body size for a synthetic cylinder. Verified:
the field of view is the inscribed circle (3228 of 4096 px against pi/4 =
0.7854), so 64 px spans 4 units and 1 unit = 16 px.
"""
import sys
sys.path.insert(0, "tools")

from pathlib import Path

import h5py
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.colors import TwoSlopeNorm

from figstyle import HEART, INK, LUNG, MUTE, apply_style, footnote, per_seed, save

apply_style()
SWEEP = Path.home() / "work/sunet_sweep"
PX_PER_UNIT = 16.0


def mixed(level, idx):
    with h5py.File(SWEEP / f"v2_snr{level}/dataset.mat", "r") as f:
        return np.array(f["recon_mixed"][idx]).T


with h5py.File("data/v2/dataset.mat", "r") as f:
    test = np.array(f["D/idx_test"]).astype(int).ravel() - 1
    # D.geom is a MATLAB struct ARRAY: -v7.3 stores one object reference per
    # sample rather than a plain vector, so each has to be dereferenced.
    rh = np.array([f[r][()].ravel()[0] for r in f["D/geom/r_heart"][()].ravel()])
    pick = int(test[np.argsort(np.abs(rh[test] - np.median(rh[test])))[0]])
    lung = np.array(f["recon_lung"][pick]).T
    heart = np.array(f["recon_heart"][pick]).T

m40, m20 = mixed(40, pick), mixed(20, pick)
d = m20 - m40
fov = np.isfinite(m40)
peak = np.nanmax(np.abs(m40))
frac = 100 * np.nanmax(np.abs(d)) / peak

# the DSC cost of that perturbation, from the capacity-matched control arm
dsc40 = per_seed("results_v2_snr40_heart_fix", "B_wide", "heart").mean()
dsc20 = per_seed("results_v2_snr20_heart_fix", "B_wide", "heart").mean()
print(f"  geometry {pick}; 20 dB differs from 40 dB by {frac:.1f}% of peak; "
      f"heart DSC {dsc40:.4f} -> {dsc20:.4f}")

fig, ax = plt.subplots(1, 6, figsize=(15.8, 3.9))
lim = float(peak)
norm = TwoSlopeNorm(0, -lim, lim)
dlim = float(np.nanmax(np.abs(d)))

hlim = float(np.nanmax(np.abs(heart)))

im = ax[0].imshow(m40, cmap="RdBu_r", norm=norm)
ax[0].set_title("(a)  input, 40 dB\nlung + heart, registered level",
                fontsize=9.3, color=INK, pad=7, linespacing=1.5)

ax[1].imshow(lung, cmap="RdBu_r", norm=norm)
ax[1].set_title("(b)  lung reconstruction\ntarget, shared scale",
                fontsize=9.3, color=INK, pad=7, linespacing=1.5)

ax[2].imshow(heart, cmap="RdBu_r", norm=norm)
ax[2].set_title("(c)  heart reconstruction\nSAME scale as (a),(b)",
                fontsize=9.3, color=INK, pad=7, linespacing=1.5)
ax[2].annotate("almost invisible beside\nthe lung — the premise",
               (32, 47), ha="center", va="center", fontsize=7.4, color=HEART,
               style="italic", zorder=6)

imh = ax[3].imshow(heart, cmap="RdBu_r", norm=TwoSlopeNorm(0, -hlim, hlim))
ax[3].set_title("(d)  heart reconstruction\nits OWN scale", fontsize=9.3,
                color=INK, pad=7, linespacing=1.5)
ax[3].annotate(f"peak {hlim:.1f} vs the lung's\n{np.nanmax(np.abs(lung)):.1f} "
               f"— {100*hlim/np.nanmax(np.abs(lung)):.0f}% of it",
               (32, 47), ha="center", va="center", fontsize=7.4, color=HEART,
               style="italic", zorder=6)

ax[4].imshow(m20, cmap="RdBu_r", norm=norm)
ax[4].set_title("(e)  input, 20 dB\nwhere H3 appears", fontsize=9.3,
                color=INK, pad=7, linespacing=1.5)

imd = ax[5].imshow(d, cmap="PuOr_r", norm=TwoSlopeNorm(0, -dlim, dlim))
ax[5].set_title(f"(f)  (e) − (a)\npeak {frac:.1f}% of (a)",
                fontsize=9.3, color=INK, pad=7, linespacing=1.5)

for a in ax:
    a.set_xticks([]); a.set_yticks([])
    for sp in a.spines.values():
        sp.set_edgecolor("#e8ecf0")
    a.plot([3.0, 3.0 + PX_PER_UNIT], [60.0, 60.0], color=INK, lw=2.6,
           solid_capstyle="butt", zorder=5)
    a.text(3.0 + PX_PER_UNIT / 2, 58.0, "1 model unit", ha="center",
           va="bottom", fontsize=7.0, color=INK, zorder=5)

cb = fig.colorbar(im, ax=[ax[0], ax[1], ax[2]], fraction=.030, pad=.015,
                  location="bottom")
cb.set_label("reconstructed conductivity change (GREIT units) — shared scale",
             fontsize=7.4)
cb.ax.tick_params(labelsize=7)
cbh = fig.colorbar(imh, ax=[ax[3]], fraction=.062, pad=.015, location="bottom")
cbh.ax.tick_params(labelsize=7)
cb2 = fig.colorbar(im, ax=[ax[4]], fraction=.062, pad=.015, location="bottom")
cb2.ax.tick_params(labelsize=7)
cbd = fig.colorbar(imd, ax=[ax[5]], fraction=.062, pad=.015, location="bottom")
cbd.ax.tick_params(labelsize=7)

fig.suptitle("The heart reconstruction is the endpoint, and on the lung's "
             "scale you can barely see it",
             fontsize=10.6, color=INK, y=1.00)
footnote(fig,
         f"One test-split geometry (index {pick}), the median heart radius of "
         "the test split. Every panel is an EIDORS GREIT reconstruction: "
         "gen_dataset.m runs three forward and three inverse solves per sample "
         "(mixed, lung only, heart only).\n"
         "(c) and (d) are the SAME reconstruction on two scales — that gap is "
         "what the architecture claims to address, and heart DSC is the "
         "registered primary endpoint of study 2.\n"
         "(f) GREIT is a regularised inverse and suppresses measurement noise "
         f"before image space: 40 dB to 20 dB changes the input by {frac:.1f}% "
         f"of peak yet costs {100*(dsc40-dsc20):.1f} DSC points (arm B_wide, 58 "
         "seeds). Bars are model units; 64 px = 4 units.",
         y=-.30)
save(fig, "fig_task_and_noise")
