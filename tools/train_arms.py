"""Train every arm under one protocol.

    python tools/train_arms.py --data data/v1/dataset.mat \
        --arms A B B_wide C D --seeds 0 1 2 3 4 5 6 7 8 9 --out runs/

Nothing here is tunable per arm. Optimizer, schedule, batch size, epoch cap,
early-stopping rule, loss weighting and normalisation are fixed constants
below, and every arm and seed sees the same split. That is the whole point:
the previous study trained the baseline for 1 epoch with augmentation through
fit_generator, one variant for 50 epochs with loss weights 1.0/1.5, and another
for 30 epochs with 1.0/1.0 on a different task.

Protocol: Nov142025/ARS_Review_2026-08-27/09_Step3_Training_Protocol.md section 4.
"""

from __future__ import annotations

import argparse
import json
import hashlib
import math
import time
from pathlib import Path

import numpy as np
import torch
import torch.nn as nn

from arms import build_arm, count_params, match_width

# ---- fixed protocol; identical for every arm ---------------------------
LR = 1e-3
LR_MIN = 1e-5
BATCH = 16
MAX_EPOCHS = 200
PATIENCE = 20
LOSS_W = (1.0, 1.0)          # lung, heart -- equal, fixed, disclosed


def sha256_file(p: Path) -> str:
    h = hashlib.sha256()
    with open(p, "rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def load_dataset(path: Path):
    """Read the .mat written by tools/gen_dataset.m (HDF5 / -v7.3).

    GREIT reconstructs a circular field of view into a square raster, so ~21%
    of pixels are NaN and carry no data. They are returned as a boolean FOV
    mask and zeroed in the arrays; every loss and metric is restricted to the
    mask, so the network is never asked to predict pixels that do not exist.
    """
    import h5py

    with h5py.File(path, "r") as f:
        mixed = np.array(f["recon_mixed"]).astype(np.float32)
        lung = np.array(f["recon_lung"]).astype(np.float32)
        heart = np.array(f["recon_heart"]).astype(np.float32)
        idx = {k: np.atleast_1d(
                   np.array(f[f"D/idx_{k}"]).astype(int).ravel()) - 1
               for k in ("train", "val", "test")}
    # MATLAB is column-major; h5py hands back (N, W, H).
    mixed, lung, heart = (a.transpose(0, 2, 1) for a in (mixed, lung, heart))

    mask = np.isfinite(mixed).all(axis=0)
    for a in (mixed, lung, heart):
        np.nan_to_num(a, copy=False, nan=0.0)
    for k, v in idx.items():
        if v.size == 0 or v.min() < 0:
            raise ValueError(f"split '{k}' is empty -- N too small?")
    return mixed, lung, heart, idx, mask


def normalise(train_x, mask, *arrays):
    """ONE dataset-wide affine, computed on the training split only, over the
    field of view only.

    Never per-image. Per-image min-max is what destroyed the conductivity scale
    in the previous pipeline (see 08 section 2), making MAE uninterpretable.
    """
    vals = train_x[:, mask]
    mu = float(vals.mean())
    sd = float(vals.std()) or 1.0
    out = []
    for a in arrays:
        b = (a - mu) / sd
        b[:, ~mask] = 0.0
        out.append(b)
    return mu, sd, out


def make_loader(x, y, idx, batch, shuffle, gen=None):
    xt = torch.from_numpy(x[idx]).unsqueeze(1)
    yt = torch.from_numpy(y[idx])
    ds = torch.utils.data.TensorDataset(xt, yt)
    return torch.utils.data.DataLoader(
        ds, batch_size=batch, shuffle=shuffle, generator=gen, drop_last=False)


def run_one(arm, seed, data, device, outdir, width_mult=None):
    # Resume guard: a completed run is never redone. This sweep is ~60 runs over
    # many hours; a crash or interrupt must not restart it from the beginning,
    # and must not silently retrain a run under a different RNG history.
    tag0 = f"{arm}_seed{seed}"
    if (outdir / f"{tag0}.json").exists() and (outdir / f"{tag0}.pt").exists():
        print(f"  {tag0}: already complete, skipped")
        return json.loads((outdir / f"{tag0}.json").read_text())

    mixed, lung, heart, idx, mask = data
    torch.manual_seed(seed)
    np.random.seed(seed)
    torch.use_deterministic_algorithms(True, warn_only=True)

    n_out = 1 if arm == "A" else 2
    y = lung[..., None] if arm == "A" else np.stack([lung, heart], axis=-1)
    y = y.transpose(0, 3, 1, 2).copy()

    gen = torch.Generator().manual_seed(seed)
    tr = make_loader(mixed, y, idx["train"], BATCH, True, gen)
    va = make_loader(mixed, y, idx["val"], BATCH, False)

    model = build_arm(arm, width_mult=width_mult).to(device)
    opt = torch.optim.Adam(model.parameters(), lr=LR)
    sched = torch.optim.lr_scheduler.CosineAnnealingLR(
        opt, T_max=MAX_EPOCHS, eta_min=LR_MIN)
    w = torch.tensor(LOSS_W[:n_out], device=device).view(1, n_out, 1, 1)
    fov = torch.from_numpy(mask.astype(np.float32)).to(device).view(1, 1, *mask.shape)
    denom = float(mask.sum()) * n_out

    def loss_fn(pred, targ):
        # mean over FOV pixels only: out-of-FOV pixels carry no data
        return (w * (pred - targ).abs() * fov).sum() / (denom * pred.shape[0])

    best, best_ep, bad, hist = math.inf, -1, 0, []
    best_state = None
    t0 = time.time()
    for ep in range(MAX_EPOCHS):
        model.train()
        tl = 0.0
        for xb, yb in tr:
            xb, yb = xb.to(device), yb.to(device)
            opt.zero_grad(set_to_none=True)
            l = loss_fn(model(xb), yb)
            l.backward()
            opt.step()
            tl += l.item() * xb.size(0)
        tl /= len(tr.dataset)

        model.eval()
        vl = 0.0
        with torch.no_grad():
            for xb, yb in va:
                xb, yb = xb.to(device), yb.to(device)
                vl += loss_fn(model(xb), yb).item() * xb.size(0)
        vl /= len(va.dataset)
        sched.step()
        hist.append({"epoch": ep, "train": tl, "val": vl})

        if vl < best - 1e-6:
            best, best_ep, bad = vl, ep, 0
            best_state = {k: v.detach().cpu().clone()
                          for k, v in model.state_dict().items()}
        else:
            bad += 1
            if bad >= PATIENCE:
                break

    model.load_state_dict(best_state)
    tag = f"{arm}_seed{seed}"
    torch.save(model.state_dict(), outdir / f"{tag}.pt")
    meta = {
        "arm": arm, "seed": seed, "width_mult": width_mult or 1.0,
        "params": count_params(model), "best_val": best, "best_epoch": best_ep,
        "epochs_run": len(hist), "minutes": (time.time() - t0) / 60,
        "protocol": {"lr": LR, "lr_min": LR_MIN, "batch": BATCH,
                     "max_epochs": MAX_EPOCHS, "patience": PATIENCE,
                     "loss": "L1", "loss_weights": list(LOSS_W[:n_out]),
                     "augmentation": None},
        "history": hist,
    }
    (outdir / f"{tag}.json").write_text(json.dumps(meta, indent=2))
    print(f"  {tag}: val {best:.5f} @ epoch {best_ep} "
          f"({len(hist)} run, {meta['minutes']:.1f} min, "
          f"{meta['params']:,} params)")
    return meta


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--data", required=True,
                    help="path to dataset.mat — REQUIRED. There is no default: a\n                         default silently trains on whatever old dataset\n                         happens to sit at that path, and the run looks normal.")
    ap.add_argument("--arms", nargs="+", default=["A", "B", "B_wide", "C", "D"])
    ap.add_argument("--seeds", nargs="+", type=int,
                    default=list(range(10)))  # 10: see 09 section 5
    ap.add_argument("--out", default="runs")
    ap.add_argument("--prereg", default="PREREGISTRATION.md",
                    help="hashed into every run record")
    args = ap.parse_args()

    outdir = Path(args.out)
    outdir.mkdir(parents=True, exist_ok=True)

    device = ("cuda" if torch.cuda.is_available()
              else "mps" if torch.backends.mps.is_available() else "cpu")
    print(f"device: {device}")

    mixed, lung, heart, idx, mask = load_dataset(Path(args.data))
    mu, sd, (mixed, lung, heart) = normalise(
        mixed[idx["train"]], mask, mixed, lung, heart)
    print(f"dataset: {mixed.shape[0]} samples, "
          f"{len(idx['train'])}/{len(idx['val'])}/{len(idx['test'])} split")
    print(f"FOV: {mask.sum()}/{mask.size} px ({100*mask.mean():.1f}%)")
    print(f"normalisation: dataset-wide over FOV, mu={mu:.4f} sd={sd:.4f}")

    # Solve the width match once and reuse, so every seed of B_wide is the
    # same architecture.
    wm = {}
    for a in ("B_wide", "C_wide"):
        if a in args.arms:
            m, n_t, n_c = match_width("D", a)
            wm[a] = m
            print(f"width match {a}: mult={m:.4f}  D={n_t:,}  {a}={n_c:,}  "
                  f"({100*(n_c-n_t)/n_t:+.2f}%)")

    prereg = Path(args.prereg)
    run_meta = {
        "data": str(args.data),
        "data_sha256": sha256_file(Path(args.data)),
        "prereg_sha256": sha256_file(prereg) if prereg.exists() else None,
        "norm": {"mu": mu, "sd": sd},
        "fov_px": int(mask.sum()),
        "device": device,
    }
    if run_meta["prereg_sha256"] is None:
        print("WARNING: no PREREGISTRATION.md found. Write and hash it BEFORE "
              "running the real sweep -- see 09 section 6.")
    (outdir / "run_meta.json").write_text(json.dumps(run_meta, indent=2))

    data = (mixed, lung, heart, idx, mask)
    for arm in args.arms:
        print(f"\n=== {arm} ===")
        for seed in args.seeds:
            run_one(arm, seed, data, device, outdir, wm.get(arm))


if __name__ == "__main__":
    main()
