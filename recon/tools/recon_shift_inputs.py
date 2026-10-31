"""Diagnostic for RESULTS_RECON.md sections 2 and 5(c): what the network sees, and what
its heart output looks like in image units, in each cross-reconstructor cell under the
two affines (registered = training set's; own = evaluation set's).

    python3 tools/recon_shift_inputs.py <ckpt-root>
        <ckpt-root>/{greit,gn,bp}/{D,B_wide}_seed0.{pt,json}
    -> results_recon/shift_inputs.json, results_recon/figs/shift_inputs_D_seed0.png

Facts only, seed 0 only. It computes no D - B_wide contrast and no DSC: per arm it
reports the input range, the fraction of the field of view covered by the
quarter-amplitude set of the prediction and of the target, and the level of the
predicted background in image units (RESEARCH_PRIMER 2.1b: compare mask coverage with
the object's size; 2.1c: plot the intermediate products).
"""
import json
import sys
from pathlib import Path

import numpy as np
import torch
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

sys.path.insert(0, str(Path(__file__).parent))
from arms import build_arm
from train_arms import load_dataset, normalise
from evaluate import qa_mask

CK = Path(sys.argv[1])
DATA = {"greit": "v2_full_snr20", "gn": "v2_full_snr20_gn", "bp": "v2_full_snr20_bp"}
SRC = list(DATA)

ds = {}
for s in SRC:
    mixed, lung, heart, idx, mask = load_dataset(Path(f"data/{DATA[s]}/dataset.mat"))
    mu, sd, _ = normalise(mixed[idx["train"]], mask, mixed[:1])
    te = idx["test"]
    ds[s] = {"mixed": mixed[te], "heart": heart[te], "mask": mask, "mu": mu, "sd": sd}


def predict(model, xin):
    x = torch.from_numpy(xin.astype(np.float32)).unsqueeze(1)
    with torch.no_grad():
        return torch.cat([model(x[i:i + 32]) for i in range(0, len(x), 32)]).numpy()[:, 1]


def describe(xin, pred_img, gt_img, fov):
    """Medians over the test frames. Background = field of view outside the target's
    quarter-amplitude set; its level is given as a fraction of the target's peak."""
    cov_p, cov_g, bg, peak_ratio = [], [], [], []
    for p, g in zip(pred_img, gt_img):
        pm, gm = qa_mask(p, fov), qa_mask(g, fov)
        cov_p.append(pm.sum() / fov.sum()); cov_g.append(gm.sum() / fov.sum())
        gpk = np.abs(g * fov).max()
        bg.append(np.median(p[fov & ~gm]) / gpk)
        peak_ratio.append(np.abs(p * fov).max() / gpk)
    v = xin[:, fov]
    return {"input_min": float(np.median(v.min(1))), "input_max": float(np.median(v.max(1))),
            "input_frame_sd": float(np.median(v.std(1))),
            "pred_qa_cover": float(np.mean(cov_p)), "target_qa_cover": float(np.mean(cov_g)),
            "pred_background_over_target_peak": float(np.median(bg)),
            "pred_peak_over_target_peak": float(np.median(peak_ratio))}


out, panels = {}, {}
for arm in ("D", "B_wide"):
    for X in SRC:
        meta = json.loads((CK / X / f"{arm}_seed0.json").read_text())
        model = build_arm(arm, width_mult=meta["width_mult"])
        model.load_state_dict(torch.load(CK / X / f"{arm}_seed0.pt", map_location="cpu"))
        model.eval()
        for Y in SRC:
            e = ds[Y]; fov = e["mask"]
            affines = {"registered": (ds[X]["mu"], ds[X]["sd"])}
            if X != Y:
                affines["own"] = (e["mu"], e["sd"])
            for name, (mu, sd) in affines.items():
                xin = (e["mixed"] - mu) / sd * fov
                pred_img = predict(model, xin) * sd + mu
                out[f"{arm}|{X}->{Y}|{name}"] = {"mu": mu, "sd": sd,
                                                 **describe(xin, pred_img, e["heart"], fov)}
                if arm == "D":
                    panels[(X, Y, name)] = (xin[0], pred_img[0])

Path("results_recon/figs").mkdir(parents=True, exist_ok=True)
Path("results_recon/shift_inputs.json").write_text(json.dumps(out, indent=1))

cells = [(X, Y) for X in SRC for Y in SRC if X != Y]
fig, ax = plt.subplots(len(cells), 5, figsize=(15, 3 * len(cells)))
for r, (X, Y) in enumerate(cells):
    fov = ds[Y]["mask"]
    shows = [(panels[(X, Y, "registered")][0], "input, registered affine"),
             (panels[(X, Y, "registered")][1], "D heart output, registered\n(image units)"),
             (panels[(X, Y, "own")][0], "input, own affine"),
             (panels[(X, Y, "own")][1], "D heart output, own\n(image units)"),
             (ds[Y]["heart"][0], "target (image units)")]
    for c, (img, title) in enumerate(shows):
        a = np.where(fov, img, np.nan)
        im = ax[r, c].imshow(a, cmap="RdBu_r")
        ax[r, c].set_title(f"{X}->{Y}: {title}\nrange {np.nanmin(a):.3g}..{np.nanmax(a):.3g}", fontsize=8)
        ax[r, c].axis("off"); fig.colorbar(im, ax=ax[r, c], fraction=0.046)
fig.suptitle("Cross-reconstructor cells, D seed 0, first test frame (each panel on its own colour scale)")
fig.tight_layout()
fig.savefig("results_recon/figs/shift_inputs_D_seed0.png", dpi=110)

print(f"{'cell':28s} {'in min':>9s} {'in max':>9s} {'in sd':>8s} {'cov pred':>9s} {'cov tgt':>8s} {'bg/peak':>8s} {'pk/peak':>8s}")
for k, v in out.items():
    print(f"{k:28s} {v['input_min']:9.3g} {v['input_max']:9.3g} {v['input_frame_sd']:8.3g} "
          f"{v['pred_qa_cover']:9.3f} {v['target_qa_cover']:8.3f} "
          f"{v['pred_background_over_target_peak']:8.3f} {v['pred_peak_over_target_peak']:8.3g}")
