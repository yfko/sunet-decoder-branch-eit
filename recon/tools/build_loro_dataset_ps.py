"""Leave-one-reconstructor-out pooled dataset with a PER-SOURCE affine, for PREREGISTRATION_RECON.md section 12.

Same construction as tools/build_mixed_dataset_ps.py (section 11): every in-pool source is standardised with
its OWN training-split affine (the (mu, sd) its single-reconstructor row was trained with, computed by the same
train_arms.normalise) and then concatenated with the same splits and frame-to-source map. The difference is
that only TWO of the three reconstructors enter the pool; the third is held out and never seen in training.
train_arms.py is fixed by the preregistration and is not edited.

    python3 tools/build_loro_dataset_ps.py --hold-out <greit|gn|bp> <greit.mat> <gn.mat> <bp.mat> <out.mat>
"""
import sys, json, hashlib, argparse
from pathlib import Path
import h5py, numpy as np
sys.path.insert(0, str(Path(__file__).parent))
from train_arms import load_dataset, normalise

ap = argparse.ArgumentParser()
ap.add_argument("--hold-out", required=True, choices=["greit", "gn", "bp"])
ap.add_argument("greit"); ap.add_argument("gn"); ap.add_argument("bp"); ap.add_argument("out")
a = ap.parse_args()
names = [n for n in ("greit", "gn", "bp") if n != a.hold_out]
srcs = [getattr(a, n) for n in names]
RECON = ("recon_mixed", "recon_lung", "recon_heart")
arrays = {k: [] for k in RECON + ("true_lung", "true_heart")}
idx = {k: [] for k in ("train", "val", "test")}
src_of_frame, offset, src_hash, affine = [], 0, {}, {}
for name, path in zip(names, srcs):
    src_hash[name] = hashlib.sha256(open(path, "rb").read()).hexdigest()
    mixed, _, _, sidx, mask = load_dataset(Path(path))
    mu, sd, _ = normalise(mixed[sidx["train"]], mask, mixed[:1])
    affine[name] = {"mu": mu, "sd": sd}
    del mixed
    with h5py.File(path, "r") as f:
        n = f["recon_mixed"].shape[0]
        for k in arrays:
            arr = np.array(f[k])
            arrays[k].append((arr - mu) / sd if k in RECON else arr)
        for k in idx:
            v = np.array(f[f"D/idx_{k}"]).astype(int).ravel()
            idx[k].append(v + offset)
        assert n == 3600, (path, n)
    src_of_frame += [name] * n
    offset += n
with h5py.File(a.out, "w") as g:
    for k, parts in arrays.items():
        g.create_dataset(k, data=np.concatenate(parts, axis=0), compression="gzip", compression_opts=1)
    D = g.create_group("D")
    for k, parts in idx.items():
        D.create_dataset(f"idx_{k}", data=np.concatenate(parts).astype(np.float64).reshape(1, -1))
    D.create_dataset("N", data=np.array([[offset]], dtype=np.float64))
    D.create_dataset("snr_db", data=np.array([[20.0]])); D.create_dataset("imgsz", data=np.array([[64.0]]))
    D.attrs["note"] = (f"leave-one-reconstructor-out pool ({'+'.join(names)}, held out: {a.hold_out}) at 20 dB, each source "
                       "standardised with its own training-split affine, for PREREGISTRATION_RECON.md section 12")
    D.attrs["hold_out"] = a.hold_out
    D.attrs["sources"] = json.dumps(src_hash); D.attrs["per_source_affine"] = json.dumps(affine)
    g.create_dataset("src_of_frame", data=np.array(src_of_frame, dtype="S5"))
print("wrote", a.out, "hold-out", a.hold_out, "N =", offset, "| train/val/test =", [len(np.concatenate(idx[k])) for k in ("train", "val", "test")])
print(json.dumps({"sources": src_hash, "per_source_affine": affine}, indent=1))
