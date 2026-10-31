"""Pre-training gate for PREREGISTRATION_RECON.md section 11 (per-source-affine pooled row).

    python3 tools/recon_mixed_ps_gate.py
    -> results_recon/mixed_ps_gate.json, results_recon/figs/mixed_ps_inputs.png

Data only: no arm is trained, no checkpoint is opened, no contrast is computed. It checks
what the network WILL see (RESEARCH_PRIMER 2.1b/2.1c), which is the check the registered
mixed row did not have.
"""
import json
import sys
from pathlib import Path

import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

sys.path.insert(0, str(Path(__file__).parent))
from train_arms import load_dataset, normalise
from evaluate import qa_mask

SRC = {"greit": "v2_full_snr20", "gn": "v2_full_snr20_gn", "bp": "v2_full_snr20_bp"}
N = 3600
out = {}

pm, pl, ph, pidx, pmask = load_dataset(Path("data/v2_full_snr20_mixed_ps/dataset.mat"))
mu_p, sd_p, (pm_n, ph_n) = normalise(pm[pidx["train"]], pmask, pm, ph)
out["pooled_affine"] = {"mu": mu_p, "sd": sd_p}
out["splits"] = {k: int(v.size) for k, v in pidx.items()}

fig, ax = plt.subplots(3, 3, figsize=(9, 9))
masks_equal, per = True, {}
for r, (s, d) in enumerate(SRC.items()):
    mixed, lung, heart, idx, mask = load_dataset(Path(f"data/{d}/dataset.mat"))
    masks_equal &= bool((mask == pmask).all())
    mu, sd, (m_n, h_n) = normalise(mixed[idx["train"]], mask, mixed, heart)
    te = idx["test"]; o = r * N
    assert (pidx["test"][r * te.size:(r + 1) * te.size] == te + o).all()
    xin = pm_n[te + o][:, pmask]          # what train_arms.py will feed the network
    tgt = ph_n[te + o][:, pmask]
    cov = [qa_mask(h, mask).sum() / mask.sum() for h in heart[te]]
    cov_rt = [qa_mask(h * sd_p * sd + (mu_p * sd + mu), pmask).sum() / pmask.sum() for h in ph_n[te + o]]
    per[s] = {
        "own_affine": {"mu": mu, "sd": sd},
        # the single-source row fed (x - mu)/sd; the pooled row feeds ((x - mu)/sd - mu_p)/sd_p
        "max_abs_input_difference_vs_own_row": float(np.abs(pm_n[te + o] - m_n[te]).max()),
        "input_frame_sd_median": float(np.median(xin.std(1))),
        "input_min_median": float(np.median(xin.min(1))), "input_max_median": float(np.median(xin.max(1))),
        "heart_target_frame_range_median": float(np.median(tgt.max(1) - tgt.min(1))),
        "heart_target_sd_train": float(ph_n[idx["train"] + o][:, pmask].std()),
        "heart_qa_cover_original": float(np.mean(cov)),
        "heart_qa_cover_after_round_trip": float(np.mean(cov_rt)),
    }
    i = te[0]
    for c, (img, title) in enumerate([(mixed[i], "raw input"), (pm_n[i + o], "input after section-11 affine"),
                                      (ph_n[i + o], "heart target after section-11 affine")]):
        a = np.where(pmask, img, np.nan)
        kw = {} if c == 0 else {"vmin": -5, "vmax": 1}
        im = ax[r, c].imshow(a, cmap="RdBu_r", **kw)
        ax[r, c].set_title(f"{s.upper()} {title}\nrange {np.nanmin(a):.3g}..{np.nanmax(a):.3g}", fontsize=8)
        ax[r, c].axis("off"); fig.colorbar(im, ax=ax[r, c], fraction=0.046)
out["fov_masks_identical"] = masks_equal
out["per_source"] = per
sds = [v["input_frame_sd_median"] for v in per.values()]
hts = [v["heart_target_sd_train"] for v in per.values()]
out["input_frame_sd_max_over_min"] = max(sds) / min(sds)
out["heart_target_sd_max_over_min"] = max(hts) / min(hts)
fig.suptitle("Section-11 pooled row: what the network sees (same geometry; col 2-3 on the colour scale of mixed_affine_inputs.png)")
fig.tight_layout()
Path("results_recon/figs").mkdir(parents=True, exist_ok=True)
fig.savefig("results_recon/figs/mixed_ps_inputs.png", dpi=110)
Path("results_recon/mixed_ps_gate.json").write_text(json.dumps(out, indent=1))
print(json.dumps(out, indent=1))
