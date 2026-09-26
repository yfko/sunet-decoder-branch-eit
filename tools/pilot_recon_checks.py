"""PREREGISTRATION_RECON.md section 6: the data-only pilot. Trains nothing,
computes no arm contrast. Writes results_recon/pilot_checks.json.

    python3 tools/pilot_recon_checks.py [data root, default data/]

Checks: (ii) quarter-amplitude organ fraction of the single-organ targets per
reconstructor (GREIT reference: heart 0.087 mean); (iii) noise figures recorded by
gen_recon_full.m; (iv) image-domain perturbation 40 -> 20 dB per reconstructor on
the test split (same definition as tools/noise_perturbation.py); (v) BP/GN raster
alignment against GREIT: peak-pixel offset of the heart target on ten test frames;
(vi) GREIT replay self-check recorded by gen_recon_full.m.
"""
import sys, json
from pathlib import Path
import h5py, numpy as np
sys.path.insert(0, "tools")
from evaluate import qa_mask  # image-space quarter-amplitude set, the registered quantity

root = Path(sys.argv[1] if len(sys.argv) > 1 else "data")
out = {}

def load(path, keys):
    with h5py.File(path, "r") as f:
        d = {k: np.array(f[k]) for k in keys}
        d["idx_test"] = np.array(f["D/idx_test"]).astype(int).ravel() - 1
        try:
            d["recon_info"] = {k: np.array(f["D/recon_info"][k]).ravel().tolist() for k in f["D/recon_info"].keys()}
        except Exception:
            d["recon_info"] = None
    return d

sets = {"greit": root / "v2_full_snr20/dataset.mat", "gn": root / "v2_full_snr20_gn/dataset.mat", "bp": root / "v2_full_snr20_bp/dataset.mat"}
data = {k: load(p, ["recon_mixed", "recon_lung", "recon_heart"]) for k, p in sets.items()}
te = data["greit"]["idx_test"]
fov = np.isfinite(data["greit"]["recon_mixed"][0]).T

# (ii) organ fraction of the QA set on the targets
for k, d in data.items():
    fr = {}
    for ch in ("recon_heart", "recon_lung"):
        fracs = [qa_mask(np.nan_to_num(d[ch][i].T), fov).mean() for i in te]
        fr[ch] = {"mean": float(np.mean(fracs)), "median": float(np.median(fracs)), "max": float(np.max(fracs))}
    out[f"qa_fraction_{k}"] = fr

# (iii) noise figures and (vi) replay self-check, as recorded
for k in ("gn", "bp"):
    out[f"recon_info_{k}"] = data[k]["recon_info"]

# (v) alignment: heart-target peak pixel, GN and BP vs GREIT, ten test frames
for k in ("gn", "bp"):
    offs = []
    for i in te[:10]:
        a = np.nan_to_num(data["greit"]["recon_heart"][i].T); b = np.nan_to_num(data[k]["recon_heart"][i].T)
        pa = np.unravel_index(np.argmax(np.abs(a)), a.shape); pb = np.unravel_index(np.argmax(np.abs(b)), b.shape)
        offs.append([int(pa[0] - pb[0]), int(pa[1] - pb[1])])
    out[f"heart_peak_offset_vs_greit_{k}"] = {"offsets_rc": offs, "max_abs": int(np.max(np.abs(offs)))}

# (iv) image-domain perturbation 40 -> 20 dB, per reconstructor, test split
for k in ("gn", "bp"):
    with h5py.File(root / f"v2_test_snr40_{k}/test40.mat", "r") as f:
        m40 = np.array(f["recon_mixed_test40"]); it = np.array(f["idx_test"]).astype(int).ravel() - 1
    assert np.array_equal(it, te)
    peak, rms = [], []
    for j, i in enumerate(te):
        a = np.nan_to_num(m40[j].T); b = np.nan_to_num(data[k]["recon_mixed"][i].T)
        peak.append(100 * np.abs(b - a).max() / np.abs(a).max()); rms.append(100 * np.linalg.norm(b - a) / np.linalg.norm(a))
    out[f"perturbation_40_to_20_{k}"] = {"peak_fraction_pct": {"median": float(np.median(peak)), "q1": float(np.percentile(peak, 25)), "q3": float(np.percentile(peak, 75))},
                                         "rms_fraction_pct": {"median": float(np.median(rms)), "q1": float(np.percentile(rms, 25)), "q3": float(np.percentile(rms, 75))}}
try:
    out["perturbation_40_to_20_greit"] = json.load(open("results/noise_perturbation_40_to_20.json"))
except Exception:
    pass
Path("results_recon").mkdir(exist_ok=True)
Path("results_recon/pilot_checks.json").write_text(json.dumps(out, indent=1))
print(json.dumps(out, indent=1))
