"""Pre-training gate for PREREGISTRATION_RECON.md section 12 (leave-one-reconstructor-out rows).

    python3 tools/recon_loro_gate.py
    -> results_recon/loro_gate.json, results_recon/figs/loro_inputs.png

Data only: no arm is trained, no checkpoint is opened, no contrast is computed. Per row: the pooled affine
train_arms.py will estimate is the identity; every in-pool frame equals the frame its single-source row saw;
the held-out source, normalised with its OWN training-split affine (the deployment path of section 12.3),
sits on the same scale as the pool (within-frame SD within a factor 2); fields of view identical; picture.
"""
import json, sys
from pathlib import Path
import numpy as np
import matplotlib; matplotlib.use("Agg"); import matplotlib.pyplot as plt
sys.path.insert(0, str(Path(__file__).parent))
from train_arms import load_dataset, normalise

SRC = {"greit": "v2_full_snr20", "gn": "v2_full_snr20_gn", "bp": "v2_full_snr20_bp"}
N = 3600; out = {}
own = {}
for s, d in SRC.items():
    mixed, lung, heart, idx, mask = load_dataset(Path(f"data/{d}/dataset.mat"))
    mu, sd, (m_n, h_n) = normalise(mixed[idx["train"]], mask, mixed, heart)
    own[s] = {"mu": mu, "sd": sd, "m_n": m_n, "h_n": h_n, "idx": idx, "mask": mask, "raw": mixed}
fig, ax = plt.subplots(3, 3, figsize=(9.5, 9))
for r, ho in enumerate(SRC):
    pool = [s for s in SRC if s != ho]
    pm, pl, ph, pidx, pmask = load_dataset(Path(f"data/v2_full_snr20_loro_{ho}/dataset.mat"))
    mu_p, sd_p, (pm_n,) = normalise(pm[pidx["train"]], pmask, pm)
    row = {"pool": pool, "pooled_affine": {"mu": mu_p, "sd": sd_p}, "splits": {k: int(v.size) for k, v in pidx.items()},
           "fov_masks_identical": bool(all((own[s]["mask"] == pmask).all() for s in SRC))}
    for j, s in enumerate(pool):
        te = own[s]["idx"]["test"]; o = j * N
        assert (pidx["test"][j * te.size:(j + 1) * te.size] == te + o).all()
        row[f"max_abs_input_difference_vs_own_row_{s}"] = float(np.abs(pm_n[te + o] - own[s]["m_n"][te]).max())
        row[f"input_frame_sd_median_{s}"] = float(np.median(pm_n[te + o][:, pmask].std(1)))
    te = own[ho]["idx"]["test"]
    xh = own[ho]["m_n"][te][:, pmask]          # held-out frames under their own affine (section 12.3 deployment path)
    row[f"heldout_{ho}_input_frame_sd_median"] = float(np.median(xh.std(1)))
    row[f"heldout_{ho}_input_range_median"] = [float(np.median(xh.min(1))), float(np.median(xh.max(1)))]
    sds = [row[f"input_frame_sd_median_{s}"] for s in pool] + [row[f"heldout_{ho}_input_frame_sd_median"]]
    row["input_frame_sd_max_over_min_incl_heldout"] = max(sds) / min(sds)
    out[f"loro_{ho}"] = row
    i = te[0]
    panels = [(pm_n[own[pool[0]]["idx"]["test"][0]], f"pool {pool[0].upper()} (affine of pool row)"),
              (pm_n[own[pool[1]]["idx"]["test"][0] + N], f"pool {pool[1].upper()} (affine of pool row)"),
              (own[ho]["m_n"][i], f"HELD-OUT {ho.upper()} (own affine)")]
    for c, (img, title) in enumerate(panels):
        a = np.where(pmask, img, np.nan); im = ax[r, c].imshow(a, cmap="RdBu_r", vmin=-5, vmax=1)
        ax[r, c].set_title(f"loro_{ho}: {title}\nrange {np.nanmin(a):.3g}..{np.nanmax(a):.3g}", fontsize=8); ax[r, c].axis("off"); fig.colorbar(im, ax=ax[r, c], fraction=0.046)
fig.suptitle("Section-12 leave-one-out rows: what the network sees in training (cols 1-2) and at deployment on the held-out reconstructor (col 3)")
fig.tight_layout(); Path("results_recon/figs").mkdir(parents=True, exist_ok=True); fig.savefig("results_recon/figs/loro_inputs.png", dpi=110)
Path("results_recon/loro_gate.json").write_text(json.dumps(out, indent=1)); print(json.dumps(out, indent=1))
