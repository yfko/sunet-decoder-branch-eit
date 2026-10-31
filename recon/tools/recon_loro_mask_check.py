"""Diagnostic for RESULTS_RECON.md section 11 (section 12 rows), seed 0, test split, exploratory, no verdict.
    python3 tools/recon_loro_mask_check.py <ckpt-root>  ->  results_recon/loro_mask_check_seed0.json
Is the large quarter-amplitude set of the held-out GREIT cell a zero-level (affine) artefact as in
section 5(c), or the network's own output?  Seed 0, test split.  For each held-out cell: coverage as scored;
coverage after subtracting each frame's median background (removes any constant offset); fraction of
the mask that comes from NEGATIVE pixels (|pred| counts); DSC as scored vs DSC after offset removal."""
import json, sys
from pathlib import Path
import numpy as np, torch
sys.path.insert(0, "tools")
from arms import build_arm
from train_arms import load_dataset, normalise
from evaluate import qa_mask, dsc
ROOT = Path(sys.argv[1]); DATA = {"greit": "v2_full_snr20", "gn": "v2_full_snr20_gn", "bp": "v2_full_snr20_bp"}
OUT = {}
for Y, dn in DATA.items():
    mixed, lung, heart, idx, fov = load_dataset(Path(f"data/{dn}/dataset.mat"))
    mu, sd, _ = normalise(mixed[idx["train"]], fov, mixed[:1]); te = idx["test"]
    xin = (mixed[te] - mu) / sd * fov
    for arm in ("D", "B_wide"):
        meta = json.loads((ROOT / f"loro_{Y}" / f"{arm}_seed0.json").read_text())
        m = build_arm(arm, width_mult=meta["width_mult"]); m.load_state_dict(torch.load(ROOT / f"loro_{Y}" / f"{arm}_seed0.pt", map_location="cpu")); m.eval()
        x = torch.from_numpy(xin.astype(np.float32)).unsqueeze(1)
        with torch.no_grad(): pred = torch.cat([m(x[i:i+32]) for i in range(0, len(x), 32)]).numpy()[:, 1] * sd + mu
        cov, cov0, neg, d_as, d_0, dpos = [], [], [], [], [], []
        for p, g in zip(pred, heart[te]):
            gm = qa_mask(g, fov); pm = qa_mask(p, fov)
            p0 = (p - np.median(p[fov & ~gm])) * fov; pm0 = qa_mask(p0, fov)
            cov.append(pm.sum()/fov.sum()); cov0.append(pm0.sum()/fov.sum()); neg.append((pm & (p < 0)).sum()/max(pm.sum(),1))
            d_as.append(dsc(pm, gm)); d_0.append(dsc(pm0, gm)); dpos.append(dsc(qa_mask(np.clip(p,0,None)*fov, fov), gm))
        OUT[f"{arm}|loro-{Y}->{Y}|own"] = {"pred_qa_cover": float(np.mean(cov)), "pred_qa_cover_after_median_offset_removal": float(np.mean(cov0)), "mask_share_from_negative_pixels": float(np.mean(neg)), "dsc_as_scored": float(np.mean(d_as)), "dsc_after_median_offset_removal": float(np.mean(d_0)), "dsc_positive_part_only": float(np.mean(dpos))}
        print(f"loro-{Y}->{Y} {arm:7s} cover {np.mean(cov):.3f} | after median-offset removal {np.mean(cov0):.3f} | share of mask from negative pixels {np.mean(neg):.3f} | DSC as scored {np.mean(d_as):.3f} | after offset removal {np.mean(d_0):.3f} | positive part only {np.mean(dpos):.3f}")

Path("results_recon/loro_mask_check_seed0.json").write_text(json.dumps(OUT, indent=1))
