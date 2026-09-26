"""Measure this machine's training speed for the divided-branch sweep.

    python3 tools/bench.py

Needs only torch and numpy — no dataset, no EIDORS. Copy this file plus
tools/arms.py to the machine you are considering, run it, and it prints the
projected wall-clock for the full 170-run study on that machine.

Synthetic data of exactly the study's shape (2880 training samples, 64x64,
batch 16), arm D (the largest, 10.8M parameters), so the number is directly
comparable across machines. Runs three epochs after a warm-up epoch, which is
enough to be stable and takes about a minute.

Reference measured on a MacBook Air M5 (8 GPU cores, fanless): 17.8 s/epoch
cold, settling to ~21 s/epoch under sustained load once it throttles; 24 min
per run averaged over 60 real runs; 68 h projected for 170 runs.
"""

from __future__ import annotations

import platform
import subprocess
import sys
import time
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

import numpy as np
import torch

from arms import build_arm, count_params

N_TRAIN = 2880          # the study's training split
BATCH = 16              # registered constant
EPOCHS_TIMED = 3
RUNS = 170              # 5 arms x 34 seeds
EPOCHS_PER_RUN = 75     # median epochs to early stopping, measured in study 1


def chip() -> str:
    try:
        out = subprocess.run(["sysctl", "-n", "machdep.cpu.brand_string"],
                             capture_output=True, text=True, timeout=5)
        name = out.stdout.strip()
    except Exception:
        name = platform.processor() or "unknown"
    try:
        mem = subprocess.run(["sysctl", "-n", "hw.memsize"],
                             capture_output=True, text=True, timeout=5)
        gb = int(mem.stdout.strip()) / 1024**3
        name += f", {gb:.0f} GB"
    except Exception:
        pass
    return name


def main() -> None:
    dev = ("cuda" if torch.cuda.is_available()
           else "mps" if torch.backends.mps.is_available() else "cpu")
    print(f"machine : {chip()}")
    print(f"python  : {platform.python_version()}   torch {torch.__version__}")
    print(f"device  : {dev}")
    if dev == "cpu":
        print("\nWARNING: no GPU backend. On CPU this study is not viable —\n"
              "         expect 10-20x the times below.")

    rng = np.random.default_rng(0)
    x = torch.from_numpy(rng.normal(size=(N_TRAIN, 1, 64, 64)).astype(np.float32))
    y = torch.from_numpy(rng.normal(size=(N_TRAIN, 2, 64, 64)).astype(np.float32))
    loader = torch.utils.data.DataLoader(
        torch.utils.data.TensorDataset(x, y), batch_size=BATCH, shuffle=True)

    model = build_arm("D").to(dev)
    opt = torch.optim.Adam(model.parameters(), lr=1e-3)
    print(f"model   : arm D, {count_params(model):,} parameters")
    print(f"workload: {N_TRAIN} samples, batch {BATCH}, "
          f"{len(loader)} batches/epoch\n")

    def one_epoch() -> float:
        model.train()
        t0 = time.time()
        for xb, yb in loader:
            xb, yb = xb.to(dev), yb.to(dev)
            opt.zero_grad(set_to_none=True)
            (model(xb) - yb).abs().mean().backward()
            opt.step()
        if dev == "mps":
            torch.mps.synchronize()
        elif dev == "cuda":
            torch.cuda.synchronize()
        return time.time() - t0

    print("warm-up epoch ...", flush=True)
    one_epoch()

    times = []
    for i in range(EPOCHS_TIMED):
        dt = one_epoch()
        times.append(dt)
        print(f"  epoch {i+1}: {dt:.1f} s", flush=True)

    spe = float(np.median(times))
    per_run_min = spe * EPOCHS_PER_RUN / 60
    total_h = per_run_min * RUNS / 60

    print(f"\n  {spe:.1f} s/epoch  ->  {per_run_min:.0f} min/run "
          f"(at {EPOCHS_PER_RUN} epochs)  ->  {total_h:.0f} h for {RUNS} runs "
          f"= {total_h/24:.1f} days")
    print(f"\n  reference, MacBook Air M5: 17.8 s/epoch cold, 68 h projected")
    print(f"  this machine is {spe/17.8:.2f}x the M5's cold epoch time")
    print("\nNote: these epochs are back to back but brief. A fanless machine "
          "will throttle further\nover a multi-day run — the M5 lost about 20% "
          "between its first run and its steady state.")


if __name__ == "__main__":
    main()
