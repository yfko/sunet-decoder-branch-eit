"""Shared figure style, so every figure in the paper looks like the same paper.

Both Scientific Reports referees raised figure quality independently (R1-6
"low visual quality... lack proper annotations, scale bars, or visual
explanation"; R2-2 "not effectively integrated into the text and lack adequate
explanation"), and the Editage letter records that the figures could not be
modified there. So this is rebuilt from scratch: vector output, explicit
annotation, and -- the specific defect the ARS review caught as B W4 -- axes
that are identical wherever two panels invite comparison.

Everything renders to PDF (vector, for submission) and PNG (for reading here).
"""
from __future__ import annotations

import csv
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

INK, MUTE, GRID = "#22303f", "#7c8a99", "#dfe4ea"
HEART, LUNG = "#c0392b", "#2e6da4"
NULLC, ACCENT = "#95a5a6", "#b8860b"

ARMS = ["B", "B_wide", "C", "C_wide", "D"]
PARAMS = {"A": 7_762_465, "B": 7_762_498, "B_wide": 10_743_738,
          "C": 7_798_498, "C_wide": 10_817_706, "D": 10_811_298}
LABEL = {"B": "B\n1 decoder", "B_wide": "B_wide\n1 decoder, wide",
         "C": "C\n2 decoders, late", "C_wide": "C_wide\n2 dec. late, wide",
         "D": "D\n2 decoders, early"}
SEEDS58 = list(range(58))

_RNG = np.random.default_rng(20260904)
_IDX58 = _RNG.integers(0, 58, (100_000, 58))


def apply_style() -> None:
    plt.rcParams.update({
        "font.family": "DejaVu Sans", "font.size": 9,
        "axes.edgecolor": GRID, "axes.labelcolor": INK, "text.color": INK,
        "xtick.color": MUTE, "ytick.color": MUTE,
        "axes.spines.top": False, "axes.spines.right": False,
        "axes.grid": True, "grid.color": GRID, "grid.linewidth": .6,
        "legend.frameon": False, "figure.facecolor": "white",
    })


def per_seed(results_dir: str | Path, arm: str, channel: str,
             metric: str = "dsc", n: int = 58) -> np.ndarray:
    """One value per seed, in seed order. Raises if any seed is missing --
    a silently short vector would quietly change every CI in the figure."""
    got: dict[int, float] = {}
    with open(Path(results_dir) / "per_seed.csv") as fh:
        for r in csv.DictReader(fh):
            if r["arm"] == arm and r["channel"] == channel:
                got[int(r["seed"])] = float(r[metric])
    missing = [s for s in range(n) if s not in got]
    if missing:
        raise SystemExit(f"{results_dir}/{arm}/{channel}: missing seeds {missing}")
    return np.array([got[s] for s in range(n)])


def boot_ci(x: np.ndarray, n_boot: int = 100_000, seed: int = 20260904):
    """Percentile bootstrap over SEEDS -- the unit of replication in this
    design, and the same resampling the registered H3 rule uses."""
    if len(x) == 58:
        bs = x[_IDX58].mean(axis=1)
    else:
        rng = np.random.default_rng(seed)
        bs = x[rng.integers(0, len(x), (n_boot, len(x)))].mean(axis=1)
    return tuple(np.percentile(bs, [2.5, 97.5]))


def norm_affine(meta: str | Path = "runs_v2/run_meta.json"):
    """The dataset-wide affine the models were trained under, read from the run
    metadata rather than recomputed -- that file is the authority."""
    import json
    n = json.loads(Path(meta).read_text())["norm"]
    return float(n["mu"]), float(n["sd"])


def qa_mask(img: np.ndarray, fov: np.ndarray, mu: float = 0.0, sd: float = 1.0,
            qa: float = 0.25) -> np.ndarray:
    """Quarter-amplitude set, taken in IMAGE units.

    Anything stored in normalised units must be un-normalised first: the
    quarter-amplitude set is not affine-invariant, and taking it after the
    dataset affine is the defect found on 2026-09-18 (the heart mask covered
    94.8% of the field of view instead of 8.7%). Pass mu/sd from norm_affine().
    """
    a = np.abs(img * sd + mu) * fov
    m = a.max()
    return a > qa * m if m > 0 else np.zeros_like(a, bool)


def dsc(a: np.ndarray, b: np.ndarray) -> float:
    s = a.sum() + b.sum()
    return 1.0 if s == 0 else 2.0 * (a & b).sum() / s


def save(fig, stem: str, outdir: str | Path = "figures") -> None:
    outdir = Path(outdir)
    outdir.mkdir(exist_ok=True)
    for ext, kw in (("pdf", {}), ("png", {"dpi": 200})):
        fig.savefig(outdir / f"{stem}.{ext}", bbox_inches="tight", **kw)
    plt.close(fig)
    print(f"  wrote {outdir}/{stem}.pdf + .png")


def footnote(fig, text: str, y: float = 0.005) -> None:
    """A figure must be readable without the caption -- R1-6 and R2-2 both
    said the figures do not stand on their own."""
    fig.text(.5, y, text, ha="center", va="bottom", fontsize=7.4, color=MUTE)
