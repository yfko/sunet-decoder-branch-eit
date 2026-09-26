"""Pack the SNR sweep down to what actually changed, for transfer.

    python3 tools/pack_sweep_delta.py ~/work/sunet_sweep sweep_delta.npz

Each sweep level is a 288 MB file, but gen_snr_sweep.m only rewrites the TEST
split's recon_mixed -- 360 frames, ~12 MB. Everything else is copied verbatim
from data/v2/dataset.mat, which the evaluating machine already has. Shipping the
whole set moves 1.4 GB to deliver about 47 MB of new information.

This writes just the changed frames, in the source file's own on-disk layout
(sample, W, H) so no transposition convention has to be re-derived on the far
side. tools/unpack_sweep_delta.py rebuilds the full files from v2 + this.
"""
from __future__ import annotations

import argparse
import hashlib
from pathlib import Path

import h5py
import numpy as np


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("sweep_root", type=Path)
    ap.add_argument("out", type=Path)
    ap.add_argument("--levels", nargs="+", type=float,
                    default=[60, 50, 40, 30, 20])
    a = ap.parse_args()

    payload: dict[str, np.ndarray] = {}
    for snr in a.levels:
        f = a.sweep_root / f"v2_snr{snr:g}" / "dataset.mat"
        if not f.exists():
            raise SystemExit(f"missing {f}")
        with h5py.File(f, "r") as h:
            idx = np.array(h["D/idx_test"]).astype(int).ravel() - 1
            # native layout, no transpose: unpack writes it straight back
            block = np.array(h["recon_mixed"][idx, :, :])
        payload[f"snr{snr:g}"] = block.astype(np.float64)
        payload[f"idx{snr:g}"] = idx
        p = f.parent / "PROVENANCE.txt"
        if p.exists():
            payload[f"prov{snr:g}"] = np.frombuffer(p.read_bytes(), dtype=np.uint8)
        print(f"  {snr:5g} dB  {block.shape}  {block.nbytes/1e6:6.1f} MB")

    np.savez_compressed(a.out, **payload)
    h = hashlib.sha256(a.out.read_bytes()).hexdigest()
    print(f"\nwrote {a.out}  {a.out.stat().st_size/1e6:.1f} MB")
    print(f"sha256 {h}")


if __name__ == "__main__":
    main()
