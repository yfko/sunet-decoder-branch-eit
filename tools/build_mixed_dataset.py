"""Pooled (mixed-reconstructor) dataset for PREREGISTRATION_RECON.md section 9.

Concatenates the GREIT, GN and BP 20 dB datasets frame-wise (same geometries and
noise seeds in each) into one HDF5 file that tools/train_arms.py reads like any
gen_dataset.m output. Splits are the union of the three sources' splits, offset
by source; a frame-to-source map is recorded so that no frame's origin is lost.

    python3 tools/build_mixed_dataset.py <greit.mat> <gn.mat> <bp.mat> <out.mat>
"""
import sys, json, hashlib
import h5py, numpy as np

srcs = sys.argv[1:4]; out = sys.argv[4]
names = ["greit", "gn", "bp"]
arrays = {k: [] for k in ("recon_mixed", "recon_lung", "recon_heart", "true_lung", "true_heart")}
idx = {k: [] for k in ("train", "val", "test")}
src_of_frame, offset, src_hash = [], 0, {}
for name, path in zip(names, srcs):
    src_hash[name] = hashlib.sha256(open(path, "rb").read()).hexdigest()
    with h5py.File(path, "r") as f:
        n = f["recon_mixed"].shape[0]
        for k in arrays:
            arrays[k].append(np.array(f[k]))          # raw (N, W, H) layout, as MATLAB wrote it
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
    D.attrs["note"] = "pooled GREIT+GN+BP at 20 dB for PREREGISTRATION_RECON.md section 9; frame i belongs to source src_of_frame[i]"
    D.attrs["sources"] = json.dumps(src_hash)
    g.create_dataset("src_of_frame", data=np.array(src_of_frame, dtype="S5"))
print("wrote", out, "N =", offset, "| train/val/test =", [len(np.concatenate(idx[k])) for k in ("train", "val", "test")])
print(json.dumps(src_hash, indent=1))
