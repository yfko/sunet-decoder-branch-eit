"""Measure how much concurrency this machine's GPU actually buys.

    python3 tools/bench_parallel.py                 # tries 1, 2, 3 processes
    python3 tools/bench_parallel.py 1 2 3 4         # explicit

At batch 16 the study's model does not saturate the GPU — a measured 4x increase
in batch size cost only 3.3x the time, so a meaningful share of each step is
dispatch overhead rather than arithmetic. Running several training processes at
once can fill those gaps. How much it helps is machine-specific, so measure it
rather than guess.

Concurrency is safe here: each run is independent and seeded, so it changes
scheduling only, not results. (Splitting across *machines* is a different matter
and is not permitted for this study — see PREREGISTRATION_HEART.md section 6.)

Prints the projected wall-clock for the registered 290 runs at each level.
"""

from __future__ import annotations

import multiprocessing as mp
import sys
import time
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

import numpy as np
import torch

N_TRAIN = 2880
BATCH = 16
EPOCHS = 2
RUNS = 290              # 5 arms x 58 seeds, registered
EPOCHS_PER_RUN = 75


def worker(_):
    """One short training job, the same shape as a real run."""
    from arms import build_arm
    dev = ("cuda" if torch.cuda.is_available()
           else "mps" if torch.backends.mps.is_available() else "cpu")
    rng = np.random.default_rng(0)
    x = torch.from_numpy(rng.normal(size=(N_TRAIN, 1, 64, 64)).astype(np.float32))
    y = torch.from_numpy(rng.normal(size=(N_TRAIN, 2, 64, 64)).astype(np.float32))
    loader = torch.utils.data.DataLoader(
        torch.utils.data.TensorDataset(x, y), batch_size=BATCH, shuffle=True)
    model = build_arm("D").to(dev)
    opt = torch.optim.Adam(model.parameters(), lr=1e-3)
    t0 = time.time()
    model.train()
    for _ in range(EPOCHS):
        for xb, yb in loader:
            xb, yb = xb.to(dev), yb.to(dev)
            opt.zero_grad(set_to_none=True)
            (model(xb) - yb).abs().mean().backward()
            opt.step()
    if dev == "mps":
        torch.mps.synchronize()
    elif dev == "cuda":
        torch.cuda.synchronize()
    return (time.time() - t0) / EPOCHS


def main() -> None:
    levels = [int(a) for a in sys.argv[1:]] or [1, 2, 3]
    dev = ("cuda" if torch.cuda.is_available()
           else "mps" if torch.backends.mps.is_available() else "cpu")
    print(f"device: {dev}   workload: arm D, {N_TRAIN} samples, batch {BATCH}\n")
    print(f"{'procs':>6s} {'s/epoch each':>14s} {'epochs/hour':>13s} "
          f"{'speedup':>9s} {'290 runs':>12s}")

    base = None
    for k in levels:
        with mp.get_context("spawn").Pool(k) as pool:
            spe = pool.map(worker, range(k))
        per = float(np.mean(spe))          # each process's own s/epoch
        thr = 3600.0 / per * k             # epochs finished per hour, all procs
        if base is None:
            base = thr
        hours = RUNS * EPOCHS_PER_RUN / thr
        print(f"{k:6d} {per:14.1f} {thr:13.0f} {thr/base:8.2f}x "
              f"{hours:8.0f} h = {hours/24:.1f} d")

    print("\nPick the level where speedup stops improving. Beyond that the "
          "processes are\nqueueing on the same GPU and you gain nothing but "
          "memory pressure.")


if __name__ == "__main__":
    main()
