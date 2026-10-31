"""RESULTS_RECON.md section 3: amplitude scale of the three reconstructors, and what the
mixed row's single pooled affine (PREREGISTRATION_RECON.md section 7) does to each.

    python3 tools/recon_scale_check.py   -> results_recon/scale_check.json, results_recon/figs/mixed_affine_inputs.png

Facts only. Training-split statistics use every 12th training frame (finite values);
the affine is re-estimated here the same way (mean/SD of the pooled training split), so
it is an approximation of the one train_arms.py stored, not a copy of it.
"""
import json
from pathlib import Path

import h5py
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

out = {}
for name in ["v2_full_snr20", "v2_full_snr20_gn", "v2_full_snr20_bp", "v2_full_snr20_mixed"]:
    with h5py.File(f"data/{name}/dataset.mat", "r") as f:
        tr = np.sort(np.array(f["D/idx_train"]).astype(int).ravel() - 1)
        row = {"n_train": int(tr.size)}
        for k in ("recon_mixed", "recon_heart", "recon_lung"):
            a = np.array(f[k][tr[::12]]); a = a[np.isfinite(a)]
            row[k] = {"mean": float(a.mean()), "sd": float(a.std())}
        out[name] = row

with h5py.File("data/v2_full_snr20_mixed/dataset.mat", "r") as f:
    tr = np.sort(np.array(f["D/idx_train"]).astype(int).ravel() - 1)
    te = np.array(f["D/idx_test"]).astype(int).ravel() - 1
    x = np.array(f["recon_mixed"][tr]); x = x[np.isfinite(x)]
    mu, sd = float(x.mean()), float(x.std())
    i0 = int(te[0])   # first GREIT test frame; the same geometry sits at +3600 (GN) and +7200 (BP)
    frames = {s: (np.array(f["recon_mixed"][i0 + o]).T, np.array(f["recon_heart"][i0 + o]).T)
              for s, o in (("GREIT", 0), ("GN", 3600), ("BP", 7200))}
out["pooled_affine"] = {"mu": mu, "sd": sd}
out["test_frame_after_pooled_affine"] = {}

fig, ax = plt.subplots(3, 3, figsize=(9, 9))
for r, (s, (m, h)) in enumerate(frames.items()):
    n, nh = (m - mu) / sd, (h - mu) / sd
    out["test_frame_after_pooled_affine"][s] = {
        "input": [float(np.nanmin(n)), float(np.nanmax(n))],
        "heart_target": [float(np.nanmin(nh)), float(np.nanmax(nh))]}
    for c, (img, t) in enumerate(((m, f"{s} raw input"),
                                  (n, f"{s} after pooled affine\nrange {np.nanmin(n):.3f}..{np.nanmax(n):.3f}"),
                                  (nh, f"{s} heart target after affine\nrange {np.nanmin(nh):.3f}..{np.nanmax(nh):.3f}"))):
        kw = {} if c == 0 else {"vmin": -5, "vmax": 1}
        im = ax[r, c].imshow(img, cmap="RdBu_r", **kw)
        ax[r, c].set_title(t, fontsize=8); ax[r, c].axis("off")
        plt.colorbar(im, ax=ax[r, c], fraction=0.046)
fig.suptitle("Mixed row: what the network sees (same geometry, three reconstructors; "
             "col 2-3 on a common colour scale)", fontsize=9)
fig.tight_layout()
Path("results_recon/figs").mkdir(parents=True, exist_ok=True)
fig.savefig("results_recon/figs/mixed_affine_inputs.png", dpi=110)
Path("results_recon/scale_check.json").write_text(json.dumps(out, indent=1))
print(json.dumps(out, indent=1))
