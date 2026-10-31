"""Pooled dataset with a PER-SOURCE affine, for PREREGISTRATION_RECON.md section 11.

tools/build_mixed_dataset.py concatenates the three reconstructors' images in their own
units, and train_arms.py then applies ONE pooled affine. GREIT's amplitude is 161x GN's
and 188x BP's, so that affine flattens the GN and BP frames to near-constants
(RESULTS_RECON.md section 3). train_arms.py is fixed by the preregistration and is not
edited; instead each source is standardised here with its OWN training-split affine --
the same (mu, sd) its single-reconstructor row was trained with, computed by the same
train_arms.normalise -- before concatenation. The pooled affine train_arms.py then
estimates is the identity up to rounding; the gate (tools/recon_mixed_ps_gate.py)
measures how close.

    python3 tools/build_mixed_dataset_ps.py <greit.mat> <gn.mat> <bp.mat> <out.mat>
"""
import sys, json, hashlib
from pathlib import Path
import h5py, numpy as np

sys.path.insert(0, str(Path(__file__).parent))
from train_arms import load_dataset, normalise

srcs = sys.argv[1:4]; out = sys.argv[4]
names = ["greit", "gn", "bp"]
RECON = ("recon_mixed", "recon_lung", "recon_heart")
arrays = {k: [] for k in RECON + ("true_lung", "true_heart")}
idx = {k: [] for k in ("train", "val", "test")}
src_of_frame, offset, src_hash, affine = [], 0, {}, {}
for name, path in zip(names, srcs):
    src_hash[name] = hashlib.sha256(open(path, "rb").read()).hexdigest()
    mixed, _, _, sidx, mask = load_dataset(Path(path))
    mu, sd, _ = normalise(mixed[sidx["train"]], mask, mixed[:1])   # the affine that source's own row used
    affine[name] = {"mu": mu, "sd": sd}
    del mixed
    with h5py.File(path, "r") as f:
        n = f["recon_mixed"].shape[0]
        for k in arrays:
            a = np.array(f[k])                        # raw (N, W, H) layout, as MATLAB wrote it
            arrays[k].append((a - mu) / sd if k in RECON else a)   # NaN outside the field of view stays NaN
        for k in idx:
            v = np.array(f[f"D/idx_{k}"]).astype(int).ravel()   # 1-based
            idx[k].append(v + offset)
        assert n == 3600, (path, n)
    src_of_frame += [name] * n
    offset += n
with h5py.File(out, "w") as g:
    for k, parts in arrays.items():
        g.create_dataset(k, data=np.concatenate(parts, axis=0), compression="gzip", compression_opts=1)
    D = g.create_group("D")
    for k, parts in idx.items():
        D.create_dataset(f"idx_{k}", data=np.concatenate(parts).astype(np.float64).reshape(1, -1))
    D.create_dataset("N", data=np.array([[offset]], dtype=np.float64))
    D.create_dataset("snr_db", data=np.array([[20.0]]))
    D.create_dataset("imgsz", data=np.array([[64.0]]))
    D.attrs["note"] = ("pooled GREIT+GN+BP at 20 dB, each source standardised with its own training-split "
                       "affine, for PREREGISTRATION_RECON.md section 11; frame i belongs to source src_of_frame[i]")
    D.attrs["sources"] = json.dumps(src_hash)
    D.attrs["per_source_affine"] = json.dumps(affine)
    g.create_dataset("src_of_frame", data=np.array(src_of_frame, dtype="S5"))
print("wrote", out, "N =", offset, "| train/val/test =", [len(np.concatenate(idx[k])) for k in ("train", "val", "test")])
print(json.dumps({"sources": src_hash, "per_source_affine": affine}, indent=1))
