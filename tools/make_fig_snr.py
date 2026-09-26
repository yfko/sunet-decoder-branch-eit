"""Figure 3: the registered SNR sweep, and the gain with the ceiling taken out.

H3 asked whether branching's advantage GROWS as SNR falls -- the mechanism's
sharpest prediction, since a branch that specialises in the weak component
should matter most when that component is most threatened. By its registered
rule (PREREGISTRATION_HEART.md section 3) H3 is confirmed.

Panel (b) is NOT a registered analysis. It divides each seed's paired gain by
the control arm's own remaining error at that level, (D - B_wide)/(1 - B_wide),
so the DSC ceiling cancels. It exists because a reader can take panel (a)'s
flat top at 60/50/40 dB for ceiling compression rather than an onset; (b) shows
which it is. It also carries the post-hoc channel comparison: section 3 makes
the lung channel "reported, not tested", so the heart-versus-lung contrast is
descriptive and can neither confirm nor falsify H3. Both are labelled as such
on the figure. Definition and numbers: tools/rel_err_sweep.py,
RESULTS_STUDY2.md section 3-3.

Rewritten 2026-09-22: the earlier panel (b) showed the 20 dB channel contrast
only; the plan-stage stress test asked for every level.
"""
import sys
sys.path.insert(0, "tools")

import matplotlib.pyplot as plt
import numpy as np

from figstyle import (HEART, INK, LUNG, MUTE, apply_style, boot_ci, footnote,
                      per_seed, save)

apply_style()
LV = [60, 50, 40, 35, 30, 25, 20]   # 35/25 added 2026-09-24 per PREREGISTRATION_HEART.md section 9.3 (descriptive)
X = np.arange(len(LV))                    # even spacing; SNR falls left to right


def arms(level, ch):
    # per_seed.csv holds BOTH channels, so one directory per level suffices.
    d = f"results_v2_snr{level}_heart_fix"
    return per_seed(d, "D", ch), per_seed(d, "B_wide", ch)


def diff(level, ch):
    t, c = arms(level, ch)
    return (t - c) * 100                  # DSC points


def rel(level, ch):
    t, c = arms(level, ch)
    return (t - c) / (1 - c) * 100        # % of the control arm's own error


# computed, never typed: a figure whose annotation disagrees with its own data
# is the defect the ARS review logged as B W4 against the withdrawn Fig. 2
_d = diff(20, "heart") - diff(60, "heart")
_dod = _d.mean()
_dlo, _dhi = boot_ci(_d)

fig, ax = plt.subplots(1, 2, figsize=(10.6, 3.9),
                       gridspec_kw={"width_ratios": [1.25, 1]})

# ---- (a) the sweep -------------------------------------------------------
a = ax[0]
for ch, col, name in (("heart", HEART, "heart  (registered endpoint)"),
                      ("lung", LUNG, "lung  (H4: no difference expected)")):
    m = np.array([diff(L, ch).mean() for L in LV])
    ci = np.array([boot_ci(diff(L, ch)) for L in LV])
    a.fill_between(X, ci[:, 0], ci[:, 1], color=col, alpha=.16, lw=0)
    a.plot(X, m, "o-", color=col, lw=1.9, ms=5.5, label=name, zorder=3)
a.axhline(0, color=INK, lw=1.1, zorder=2)
a.axvline(2, color=MUTE, lw=1.0, ls=(0, (4, 3)), zorder=1)
a.annotate("40 dB — registered\nprimary level", (1.92, .47), ha="right",
           va="top", fontsize=7.6, color=MUTE)
a.annotate("branching helps", (4, .30), ha="right", fontsize=8.2, color=MUTE,
           style="italic")
a.annotate("branching hurts", (4, -.19), ha="right", fontsize=8.2, color=MUTE,
           style="italic")
a.set_xticks(X); a.set_xticklabels([f"{L}" for L in LV])
a.set_xlabel("measurement SNR (dB)   —   noise increases to the right")
a.set_ylabel("D − B_wide  (DSC percentage points)")
a.set_title(f"(a)  registered sweep  →  H3 confirmed\n"
            f"D(20)−D(60) = {_dod:+.2f} pts, CI [{_dlo:+.2f}, {_dhi:+.2f}]",
            fontsize=9.3, color=INK, pad=8, loc="left", linespacing=1.5)
a.legend(loc="upper left", fontsize=8.2)

# ---- (b) the ceiling taken out, every level --------------------------------
b = ax[1]
excl = {}
for ch, col, name in (("heart", HEART, "heart"), ("lung", LUNG, "lung")):
    vals = [rel(L, ch) for L in LV]
    m = np.array([v.mean() for v in vals])
    ci = np.array([boot_ci(v) for v in vals])
    b.fill_between(X, ci[:, 0], ci[:, 1], color=col, alpha=.16, lw=0)
    b.plot(X, m, "o-", color=col, lw=1.9, ms=5.5, label=name, zorder=3)
    # which levels' intervals exclude zero is READ OFF the intervals
    excl[ch] = [L for L, (lo, hi) in zip(LV, ci) if lo > 0 or hi < 0]
    if ch == "heart":
        for x, (lo, hi), mm in zip(X, ci, m):
            if lo > 0:
                b.annotate(f"{mm:.1f}%", (x, hi), xytext=(0, 4), textcoords="offset points",
                           ha="center", fontsize=7.6, color=col)
b.axhline(0, color=INK, lw=1.1, zorder=2)
b.axvline(2, color=MUTE, lw=1.0, ls=(0, (4, 3)), zorder=1)
h20, l20 = rel(20, "heart"), rel(20, "lung")
d20 = h20 - l20
lo, hi = boot_ci(d20)
b.set_xticks(X); b.set_xticklabels([f"{L}" for L in LV])
b.set_xlabel("measurement SNR (dB)")
b.set_ylabel("gain as % of the control arm's own error")
hx = ", ".join(str(L) for L in excl["heart"]) or "none"
b.set_title(f"(b)  post-hoc: ceiling divided out\nheart CI excludes zero at {hx} dB only",
            fontsize=9.3, color=INK, pad=8, loc="left", linespacing=1.5)
b.legend(loc="upper left", fontsize=8.2)
b.annotate(f"20 dB: heart − lung = {d20.mean():+.2f} pp, 95% CI [{lo:+.2f}, {hi:+.2f}]\n"
           + ("excludes zero" if lo > 0 or hi < 0 else "contains zero"),
           (.98, .04), xycoords="axes fraction", ha="right", va="bottom",
           fontsize=7.8, color=INK)

# The onset bracket is COMPUTED, never typed. Two thresholds, both read off the data:
#   detectable  -- the highest-SNR level whose ceiling-corrected CI excludes zero
#   clears floor -- the highest-SNR level meeting BOTH registered-rule conditions
#                   (mean difference > control's seed SD, and Wilcoxon p < 0.05)
# Applying the rule's FORM away from the registered 40 dB is descriptive, not H1.
from scipy.stats import wilcoxon as _wx
_det = _flo = None
for _i, _L in enumerate(LV):
    _t, _c = arms(_L, "heart")
    _raw = (_t - _c) * 100
    _rlo, _rhi = boot_ci(rel(_L, "heart"))
    if _det is None and (_rlo > 0 or _rhi < 0):
        _det = (LV[_i - 1], _L) if _i else (None, _L)
    if _flo is None and _raw.mean() > _c.std(ddof=1) * 100 and float(_wx(_t, _c).pvalue) < .05:
        _flo = (LV[_i - 1], _L) if _i else (None, _L)
fig.suptitle(f"The advantage becomes detectable between {_det[0]} and {_det[1]} dB and clears the "
             f"registered effect-size floor between {_flo[0]} and {_flo[1]} dB, on the suppressed channel",
             fontsize=10.2, color=INK, y=1.04)
footnote(fig,
         "(a) Paired across the 58 registered seeds; bands are 95% percentile "
         "bootstrap CIs. Difference-of-differences D(20 dB) − D(60 dB) = "
         f"{_dod:+.3f} points, CI [{_dlo:+.3f}, {_dhi:+.3f}], which is the "
         "registered H3 statistic.\n"
         "(b) Each seed's gain divided by B_wide's own remaining error at that "
         "level, so the two ceilings cancel. Not preregistered: descriptive, and "
         "the heart-versus-lung contrast cannot confirm or falsify the mechanism.\n"
         "Lung values at 60–40 dB divide by an error under 0.7 points and are not "
         "interpretable; their intervals all contain zero.", y=-.20)
save(fig, "fig_snr_sweep")
