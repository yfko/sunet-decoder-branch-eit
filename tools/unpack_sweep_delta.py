"""Rebuild the full SNR sweep files from data/v2 + the packed delta.

    python3 tools/unpack_sweep_delta.py sweep_delta.npz data/v2/dataset.mat ~/work/sweep

Run on the machine that holds the trained weights. Each output is a byte-for-byte
copy of data/v2/dataset.mat with two things changed: the TEST split's recon_mixed
frames, and D.snr_db. Copying rather than reconstructing means the MATLAB -v7.3
struct layout (D, #refs#, the geom struct array) is preserved exactly without
this script needing to understand any of it.

Every output is verified before it is accepted: the training split must come out
byte-identical to the source, because tools/train_arms.py:normalise() derives the
one dataset-wide affine from it. If that affine moved, every model would be fed a
different input scale than it was trained on and the SNR sweep would be
uninterpretable.
"""
from __future__ import annotations

import argparse
import shutil
from pathlib import Path

import h5py
import numpy as np


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("delta", type=Path)
    ap.add_argument("source", type=Path, help="data/v2/dataset.mat")
    ap.add_argument("outroot", type=Path)
    a = ap.parse_args()

    z = np.load(a.delta)
    levels = sorted({k[3:] for k in z.files if k.startswith("snr")},
                    key=float, reverse=True)
    a.outroot.mkdir(parents=True, exist_ok=True)

    with h5py.File(a.source, "r") as h:
        src_train_idx = np.array(h["D/idx_train"]).astype(int).ravel() - 1
        src_train = np.array(h["recon_mixed"][src_train_idx, :, :])

    for lv in levels:
        out = a.outroot / f"v2_snr{lv}"
        out.mkdir(exist_ok=True)
        dst = out / "dataset.mat"
        print(f"=== {lv} dB -> {dst}")
        shutil.copy(a.source, dst)

        idx = z[f"idx{lv}"]
        block = z[f"snr{lv}"]
        with h5py.File(dst, "r+") as h:
            h["recon_mixed"][idx, :, :] = block
            h["D/snr_db"][...] = float(lv)
            train_idx = np.array(h["D/idx_train"]).astype(int).ravel() - 1
            train_now = np.array(h["recon_mixed"][train_idx, :, :])
            test_now = np.array(h["recon_mixed"][idx, :, :])

        # equal_nan: GREIT reconstructs a circular field of view into a
        # square raster, so ~21% of every frame is NaN by construction. Without
        # this, NaN != NaN makes an exact copy compare as different.
        ok_train = np.array_equal(train_now, src_train, equal_nan=True)
        ok_test = np.array_equal(test_now, block, equal_nan=True)
        print(f"    training split byte-identical to source : {ok_train}")
        print(f"    test frames written back exactly        : {ok_test}")
        if not (ok_train and ok_test):
            raise SystemExit(f"{dst}: verification FAILED -- do not use this file")

        if f"prov{lv}" in z.files:
            (out / "PROVENANCE.txt").write_bytes(z[f"prov{lv}"].tobytes())

    print("\nall levels rebuilt and verified.")


if __name__ == "__main__":
    main()
