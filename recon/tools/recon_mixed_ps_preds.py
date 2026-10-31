"""RESEARCH_PRIMER 2.1c for the mixed-ps row (PREREGISTRATION_RECON.md section 11): draw what
the network saw and what it produced, so a wrong endpoint shows to the eye before it is read.

    python3 tools/recon_mixed_ps_preds.py <ckpt-dir>
        <ckpt-dir>/{D,B_wide}_seed0.{pt,json}   (runs_recon_mixed_ps on the mini)
    -> results_recon/figs/mixed_ps_preds_seed0.png, results_recon/mixed_ps_preds_seed0.json

Scoring path of 11.3: input and output under the evaluation set's own training-split affine,
which for this row is the affine the frames were trained under. Seed 0 only, first test frame,
plus medians over the test split of the quarter-amplitude coverage of prediction and target
and of the predicted background level (fraction of the target peak). No contrast, no DSC.
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


def predict(model, xin):
    x = torch.from_numpy(xin.astype(np.float32)).unsqueeze(1)
    with torch.no_grad():
        return torch.cat([model(x[i:i + 32]) for i in range(0, len(x), 32)]).numpy()[:, 1]


def describe(xin, pred_img, gt_img, fov):
    cov_p, cov_g, bg, pk = [], [], [], []
    for p, g in zip(pred_img, gt_img):
        pm, gm = qa_mask(p, fov), qa_mask(g, fov)
        cov_p.append(pm.sum() / fov.sum()); cov_g.append(gm.sum() / fov.sum())
        gpk = np.abs(g * fov).max()
        bg.append(np.median(p[fov & ~gm]) / gpk); pk.append(np.abs(p * fov).max() / gpk)
    v = xin[:, fov]
    return {"input_min": float(np.median(v.min(1))), "input_max": float(np.median(v.max(1))),
            "input_frame_sd": float(np.median(v.std(1))),
            "pred_qa_cover": float(np.mean(cov_p)), "target_qa_cover": float(np.mean(cov_g)),
            "pred_background_over_target_peak": float(np.median(bg)),
            "pred_peak_over_target_peak": float(np.median(pk))}


models = {}
for arm in ("D", "B_wide"):
    meta = json.loads((CK / f"{arm}_seed0.json").read_text())
    m = build_arm(arm, width_mult=meta["width_mult"])
    m.load_state_dict(torch.load(CK / f"{arm}_seed0.pt", map_location="cpu")); m.eval()
    models[arm] = m

out, panels = {}, {}
for Y in SRC:
    mixed, lung, heart, idx, fov = load_dataset(Path(f"data/{DATA[Y]}/dataset.mat"))
    mu, sd, _ = normalise(mixed[idx["train"]], fov, mixed[:1])
    te = idx["test"]
    xin = (mixed[te] - mu) / sd * fov
    panels[(Y, "input")] = xin[0]; panels[(Y, "target")] = heart[te][0]
    for arm, m in models.items():
        pred_img = predict(m, xin) * sd + mu
        out[f"{arm}|mixed-ps->{Y}|own"] = {"mu": float(mu), "sd": float(sd), **describe(xin, pred_img, heart[te], fov)}
        panels[(Y, arm)] = pred_img[0]
    panels[(Y, "fov")] = fov

Path("results_recon/figs").mkdir(parents=True, exist_ok=True)
Path("results_recon/mixed_ps_preds_seed0.json").write_text(json.dumps(out, indent=1))

fig, ax = plt.subplots(len(SRC), 4, figsize=(12.5, 3.2 * len(SRC)))
for r, Y in enumerate(SRC):
    fov = panels[(Y, "fov")]
    shows = [(panels[(Y, "input")], "input (own affine, normalised units)"),
             (panels[(Y, "D")], "D heart output (image units)"),
             (panels[(Y, "B_wide")], "B_wide heart output (image units)"),
             (panels[(Y, "target")], "target (image units)")]
    for c, (img, title) in enumerate(shows):
        a = np.where(fov, img, np.nan)
        im = ax[r, c].imshow(a, cmap="RdBu_r")
        ax[r, c].set_title(f"mixed-ps->{Y}: {title}\nrange {np.nanmin(a):.3g}..{np.nanmax(a):.3g}", fontsize=8)
        ax[r, c].axis("off"); fig.colorbar(im, ax=ax[r, c], fraction=0.046)
fig.suptitle("mixed-ps row (section 11), seed 0, first test frame, scoring path of 11.3 (each panel on its own colour scale)")
fig.tight_layout()
fig.savefig("results_recon/figs/mixed_ps_preds_seed0.png", dpi=110)

print(f"{'cell':26s} {'in min':>8s} {'in max':>8s} {'in sd':>7s} {'cov pred':>9s} {'cov tgt':>8s} {'bg/peak':>8s} {'pk/peak':>8s}")
for k, v in out.items():
    print(f"{k:26s} {v['input_min']:8.3g} {v['input_max']:8.3g} {v['input_frame_sd']:7.3g} "
          f"{v['pred_qa_cover']:9.3f} {v['target_qa_cover']:8.3f} {v['pred_background_over_target_peak']:8.3f} {v['pred_peak_over_target_peak']:8.3g}")
