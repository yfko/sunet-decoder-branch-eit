"""How much does 40 -> 20 dB actually move the GREIT input, over the whole test
split -- and what does that cost the control arm?

    python3 tools/noise_perturbation.py

Motivation: FIGURES.md and NOTES_2026-09-18 quote "5.4% of peak" for ONE
geometry (the median heart radius, used in fig_task_and_noise). The manuscript
needs the dataset-level statement, traceable to a file (MANUSCRIPT_RULES R10c).

For every test-split frame i, with m40 and m20 the mixed GREIT reconstructions
at the two levels (same geometry, same noise seed, amplitude scaled):

    peak_frac_i = max|m20 - m40| / max|m40|            (% of that frame's peak)
    rms_frac_i  = ||m20 - m40||_2 / ||m40||_2           (% of that frame's norm)

reported as median and IQR over the 360 test frames. The cost is B_wide's mean
heart DSC at 40 dB minus at 20 dB over the 58 seeds. Reads the sweep datasets
in ~/work/sunet_sweep (same files the figure scripts read).
"""
import sys
sys.path.insert(0, "tools")

import json
from pathlib import Path

import h5py
import numpy as np

from figstyle import per_seed

SWEEP = Path.home() / "work/sunet_sweep"

with h5py.File("data/v2/dataset.mat", "r") as f:
    test = np.array(f["D/idx_test"]).astype(int).ravel() - 1
with h5py.File(SWEEP / "v2_snr40/dataset.mat", "r") as f40, \
     h5py.File(SWEEP / "v2_snr20/dataset.mat", "r") as f20:
    peak, rms = [], []
    for i in test:
        a = np.array(f40["recon_mixed"][int(i)]).T
        b = np.array(f20["recon_mixed"][int(i)]).T
        fov = np.isfinite(a) & np.isfinite(b)
        d = b[fov] - a[fov]
        peak.append(100 * np.max(np.abs(d)) / np.max(np.abs(a[fov])))
        rms.append(100 * np.linalg.norm(d) / np.linalg.norm(a[fov]))
peak, rms = np.array(peak), np.array(rms)

c40 = per_seed("results_v2_snr40_heart_fix", "B_wide", "heart")
c20 = per_seed("results_v2_snr20_heart_fix", "B_wide", "heart")
l40 = per_seed("results_v2_snr40_heart_fix", "B_wide", "lung")
l20 = per_seed("results_v2_snr20_heart_fix", "B_wide", "lung")

out = dict(
    n_test_frames=int(len(test)),
    peak_fraction_pct=dict(median=float(np.median(peak)), q1=float(np.percentile(peak, 25)),
                           q3=float(np.percentile(peak, 75)), min=float(peak.min()), max=float(peak.max())),
    rms_fraction_pct=dict(median=float(np.median(rms)), q1=float(np.percentile(rms, 25)),
                          q3=float(np.percentile(rms, 75)), min=float(rms.min()), max=float(rms.max())),
    Bwide_heart_dsc=dict(at40=float(c40.mean()), at20=float(c20.mean()),
                         drop_pts=float((c40.mean() - c20.mean()) * 100)),
    Bwide_lung_dsc=dict(at40=float(l40.mean()), at20=float(l20.mean()),
                        drop_pts=float((l40.mean() - l20.mean()) * 100)),
    definition="per test frame: max|m20-m40|/max|m40| and ||m20-m40||/||m40|| within the field of view",
)
Path("results").mkdir(exist_ok=True)
json.dump(out, open("results/noise_perturbation_40_to_20.json", "w"), indent=2)
print(json.dumps(out, indent=2))
