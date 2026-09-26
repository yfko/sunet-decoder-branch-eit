| Trained | Evaluated | Contrast | B_wide heart DSC (mean ± SD) | D heart DSC (mean ± SD) | D − B_wide, pts [95% CI, seeds] | [95% CI, geometries] | dz | Wilcoxon W | p | Floor (B_wide seed SD), pts | Seeds D > B_wide | Rule |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 40 dB | 40 dB | H1 (registered primary) | 0.9657 ± 0.0067 | 0.9679 ± 0.0043 | +0.223 [+0.020, +0.441] | [+0.183, +0.266] | +0.27 | 642 | 0.0983 | 0.670 | 32/58 | falsified |
| 40 dB | 20 dB | H3 low end (evaluation only) | 0.8775 ± 0.0108 | 0.8985 ± 0.0110 | +2.097 [+1.642, +2.543] | [+1.714, +2.508] | +1.19 | 97 | <0.0001 | 1.078 | 50/58 | — (no rule) |
| 20 dB | 20 dB | H5 (registered addendum) | 0.9574 ± 0.0038 | 0.9597 ± 0.0041 | +0.229 [+0.081, +0.373] | [+0.184, +0.276] | +0.40 | 427 | 0.0009 | 0.384 | 41/58 | falsified |

Registered H5 rule: Δ_20|20 must exceed B_wide's seed-to-seed SD at 20|20 AND Wilcoxon p < 0.05. Secondary, reported not tested: Δ_20|20 − Δ_20|40 = -1.868 pts [-2.327, -1.403] (seeds resampled in pairs), a 9.2-fold shrinkage. Retraining at 20 dB raised B_wide's heart DSC by 8.0 pts and D's by 6.1 pts. Lung channel at 20|20: Δ = -0.002 pts [-0.040, +0.036], p = 0.9475. Geometry-level CIs resample the 360 test frames (100,000 resamples); seed-level CIs resample the 58 seeds.
