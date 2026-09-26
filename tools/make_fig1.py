"""Figure 1 — why the cardiac component cannot be taken from the image directly.

Four panels on one representative frame:
  (a) the mixed reconstruction, i.e. what an EIT device actually gives you
  (b) thresholding recovers the lung
  (c) the same thresholding does not recover the heart
  (d) what the two organs actually are

Threshold is the quarter-amplitude set, |img| > 0.25 max|img| — EIDORS'
calc_hm_set(img, 0.25), the basis of the GREIT figures of merit and the same
rule the study's DSC uses. Sign is used the way a clinical ROI method would:
lungs are less conductive than background so they reconstruct negative, the
heart is more conductive so it reconstructs positive.
"""
import sys
from pathlib import Path
import numpy as np, h5py
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.colors import TwoSlopeNorm

QA = 0.25
SRC = sys.argv[1] if len(sys.argv) > 1 else "data/v2/dataset.mat"
OUT = sys.argv[2] if len(sys.argv) > 2 else "figures/fig1_separability"

with h5py.File(SRC, "r") as f:
    g = lambda k: np.array(f[k]).transpose(0, 2, 1)
    M, L, H = g("recon_mixed"), g("recon_lung"), g("recon_heart")
fov = np.isfinite(M).all(axis=0)
for a in (M, L, H):
    np.nan_to_num(a, copy=False)

def qa(img):
    a = np.abs(img) * fov
    m = a.max()
    return a > QA * m if m > 0 else np.zeros_like(a, bool)

def dsc(a, b):
    s = a.sum() + b.sum()
    return 1.0 if s == 0 else 2.0 * (a & b).sum() / s

# pick a frame whose heart result sits at the median of the whole set
scores = []
for i in range(len(M)):
    thr = QA * (np.abs(M[i]) * fov).max()
    scores.append(dsc((M[i] > thr) & fov, qa(H[i])))
scores = np.array(scores)
i = int(np.argsort(np.abs(scores - np.median(scores)))[0])
print(f"frame {i}: heart-by-threshold DSC {scores[i]:.4f} "
      f"(set median {np.median(scores):.4f})")

mixed = M[i]
thr = QA * (np.abs(mixed) * fov).max()
lung_thr  = (mixed < -thr) & fov
heart_thr = (mixed >  thr) & fov
lung_true, heart_true = qa(L[i]), qa(H[i])
d_lung, d_heart = dsc(lung_thr, lung_true), dsc(heart_thr, heart_true)

# the field of view as a light ground, not a black disc: the organs are the
# information, the FOV is only where information could exist
bg = np.where(fov, 1.0, np.nan)
BG_CMAP = matplotlib.colors.ListedColormap(["#EDF0F3"])
lim = np.nanpercentile(np.abs(np.where(fov, mixed, np.nan)), 99.5)

INK, MUTE = "#171C22", "#77828F"
LUNG, HEART = "#2E6F9E", "#C1442E"
plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 9})

# Scale bar, added 2026-09-04. Referee R1-6 named scale bars specifically
# ("lack proper annotations, scale bars, or visual explanation"), and the first
# version of this figure had none. The phantom is ng_mk_cyl_models with radius 2
# in model units and no declared physical size, so the bar is in MODEL UNITS --
# labelling it in centimetres would mean inventing a body size for a synthetic
# cylinder. The field of view is the inscribed circle (3228 of 4096 px against
# pi/4 = 0.7854), so 64 px spans 4 units and 1 unit = 16 px.
PX_PER_UNIT = 16.0

def scalebar(a):
    a.plot([3.0, 3.0 + PX_PER_UNIT], [60.0, 60.0], color=INK, lw=2.6,
           solid_capstyle="butt", zorder=6)
    a.text(3.0 + PX_PER_UNIT / 2, 58.0, "1 model unit", ha="center",
           va="bottom", fontsize=7.0, color=INK, zorder=6)

fig, ax = plt.subplots(1, 4, figsize=(12.4, 3.5))
for a in ax:
    a.set_xticks([]); a.set_yticks([])
    for sp in a.spines.values():
        sp.set_color("#D8DDE3")

# (a) what you get
im = ax[0].imshow(np.where(fov, mixed, np.nan),
                  cmap="RdBu_r", norm=TwoSlopeNorm(0, -lim, lim))
ax[0].set_title("(a)  the image you get\nlung + heart, reconstructed",
                fontsize=9.5, color=INK, pad=8)
cb = fig.colorbar(im, ax=ax[0], fraction=.046, pad=.03)
cb.ax.tick_params(labelsize=7, colors=MUTE); cb.outline.set_edgecolor("#D8DDE3")
cb.set_label("reconstructed conductivity change (GREIT units)",
             fontsize=7.2, color=MUTE)

def overlay(a, got, truth, colour, title, d):
    a.imshow(bg, cmap=BG_CMAP)
    a.imshow(np.ma.masked_where(~got, got.astype(float)),
             cmap=matplotlib.colors.ListedColormap([colour]), alpha=.55)
    a.contour(truth.astype(float), levels=[.5], colors=[colour],
              linewidths=1.4, linestyles="--")
    a.set_title(title, fontsize=9.5, color=INK, pad=8)
    if not got.any():
        a.text(.5, .5, "nothing above\nthreshold", transform=a.transAxes,
               ha="center", va="center", fontsize=9.5, color=MUTE, style="italic")
    a.text(.5, -.07, f"DSC {d:.3f}", transform=a.transAxes, ha="center",
           va="top", fontsize=11, color=colour, family="DejaVu Sans Mono",
           fontweight="bold")

overlay(ax[1], lung_thr, lung_true, LUNG,
        "(b)  threshold → lung\nrecovered", d_lung)
overlay(ax[2], heart_thr, heart_true, HEART,
        "(c)  same threshold → heart\nnot recovered", d_heart)

# (d) truth
ax[3].imshow(bg, cmap=BG_CMAP)
for msk, col in ((lung_true, LUNG), (heart_true, HEART)):
    ax[3].imshow(np.ma.masked_where(~msk, msk.astype(float)),
                 cmap=matplotlib.colors.ListedColormap([col]), alpha=.55)
    ax[3].contour(msk.astype(float), levels=[.5], colors=[col], linewidths=1.4)
ax[3].set_title("(d)  what is actually there\nlung and heart", fontsize=9.5,
                color=INK, pad=8)
ax[3].text(.5, -.07, "the separation to be learned", transform=ax[3].transAxes,
           ha="center", va="top", fontsize=9, color=MUTE)

fig.text(.5, .005,
         "Filled = recovered by thresholding the mixed image at quarter amplitude.  "
         "Dashed = the organ's own reconstruction.  "
         "Lungs reconstruct negative, the heart positive.",
         ha="center", fontsize=8, color=MUTE)
for a in ax:
    scalebar(a)

fig.tight_layout(rect=[0, .045, 1, 1])
for ext in ("pdf", "png"):
    fig.savefig(f"{OUT}.{ext}", dpi=200, bbox_inches="tight")
print(f"lung {d_lung:.4f}   heart {d_heart:.4f}")
print(f"wrote {OUT}.pdf / .png")
