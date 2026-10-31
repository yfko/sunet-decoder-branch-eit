"""Shared helpers for the RECON paper figures (PLoS One submission).

Reuses the palette and conventions of tools/figstyle.py, with the PLoS figure
rules applied on top:

* font: Arial (PLoS accepts Arial, Times, Symbol only), every text 8-12 pt;
* width 13.2 cm (one text column) or at most 19.05 cm, height at most 22 cm;
* no figure title or number inside the image, multi-panel as one file;
* 2 pt white margin;
* TIFF, LZW compression, 600 dpi, flattened RGB (no alpha), next to PDF + PNG.

Every number a figure prints is computed from the result files at plot time.
Only numpy / matplotlib / h5py / PIL / csv / json are used, so the scripts run
without the training stack (tools/train_arms.py imports torch).
"""
from __future__ import annotations

import csv
import json
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image

from figstyle import INK, MUTE, GRID, HEART, LUNG, NULLC, ACCENT  # noqa: F401  (house palette)

ROOT = Path(__file__).resolve().parents[1]
RES = ROOT / "results_recon"
OUT = ROOT / "figures" / "recon"

CM = 1 / 2.54
W1, WMAX, HMAX = 13.2, 19.05, 22.0            # cm
SEEDS = list(range(30))
N_BOOT, BOOT_SEED = 100_000, 20260904

# Datasets: GREIT, GN and BP share geometry and noise-seed splits (test index i is
# the same geometry in all three).
DATASETS = {
    "GREIT": Path("/Users/yfko/work/sunet_sweep/v2_full_snr20/dataset.mat"),
    "GN": ROOT / "data/v2_full_snr20_gn/dataset.mat",
    "BP": ROOT / "data/v2_full_snr20_bp/dataset.mat",
}
SCALE_KEY = {"GREIT": "v2_full_snr20", "GN": "v2_full_snr20_gn", "BP": "v2_full_snr20_bp"}
LONG = {"GREIT": "GREIT", "GN": "Gauss–Newton (GN)", "BP": "back-projection (BP)"}
RECONS = ["GREIT", "GN", "BP"]
ARM_COL = {"B_wide": INK, "D": ACCENT}


def apply_style() -> None:
    plt.rcParams.update({
        "font.family": "Arial", "font.size": 8,
        "axes.titlesize": 9, "axes.labelsize": 8.5,
        "xtick.labelsize": 8, "ytick.labelsize": 8, "legend.fontsize": 8,
        "axes.edgecolor": GRID, "axes.labelcolor": INK, "text.color": INK,
        "xtick.color": MUTE, "ytick.color": MUTE,
        "axes.spines.top": False, "axes.spines.right": False,
        "axes.grid": True, "grid.color": GRID, "grid.linewidth": .6,
        "legend.frameon": False, "figure.facecolor": "white",
        "savefig.facecolor": "white",
        "pdf.fonttype": 42, "ps.fonttype": 42,     # embed TrueType, keep text as text
        "mathtext.fontset": "custom", "mathtext.rm": "Arial",
        "axes.unicode_minus": True,
    })


# ---- data ---------------------------------------------------------------
def load_cell(cell: str, arm: str, channel: str = "heart", seeds=SEEDS) -> np.ndarray:
    """Per-seed Dice in seed order, as tools/recon_results.py load(). Raises on a gap."""
    got: dict[int, float] = {}
    with open(RES / cell / "per_seed.csv") as fh:
        for r in csv.DictReader(fh):
            if r["arm"] == arm and r["channel"] == channel:
                got[int(r["seed"])] = float(r["dsc"])
    missing = [s for s in seeds if s not in got]
    if missing:
        raise SystemExit(f"{cell}: arm {arm} {channel} missing seeds {missing}")
    return np.array([got[s] for s in seeds])


def boot(x: np.ndarray, n_boot: int = N_BOOT, seed: int = BOOT_SEED) -> tuple[float, float]:
    """95% percentile bootstrap over seeds; identical to tools/recon_results.py boot()
    (fresh generator per quantity, seed 20260904, 100,000 resamples)."""
    rng = np.random.default_rng(seed)
    idx = rng.integers(0, x.size, (n_boot, x.size))
    lo, hi = np.percentile(x[idx].mean(axis=1), [2.5, 97.5])
    return float(lo), float(hi)


def results() -> dict:
    return json.loads((RES / "recon_results.json").read_text())


def delta_ci() -> dict:
    return json.loads((RES / "recon_delta_ci.json").read_text())


def scale_check() -> dict:
    return json.loads((RES / "scale_check.json").read_text())


def agree(label: str, got: float, ref: float, nd: int = 4) -> None:
    if round(got, nd) != round(ref, nd):
        raise SystemExit(f"CROSS-CHECK FAILED {label}: plotted {got:.6f} vs file {ref:.6f}")


def read_split(name: str):
    """Split indices (0-based, stored order) of one dataset."""
    import h5py
    with h5py.File(DATASETS[name], "r") as f:
        return {k: np.atleast_1d(np.array(f[f"D/idx_{k}"]).astype(int).ravel()) - 1
                for k in ("train", "val", "test")}


def read_frame(name: str, i: int):
    """One frame (mixed, heart) in image orientation, plus the FOV mask, exactly as
    tools/train_arms.py load_dataset(): transpose (0,2,1), mask = finite in every
    mixed frame. NaN is kept outside the FOV here (it is drawn white)."""
    import h5py
    with h5py.File(DATASETS[name], "r") as f:
        allm = np.array(f["recon_mixed"])                     # (N, W, H)
        mask = np.isfinite(allm).all(axis=0).T
        mixed = np.array(f["recon_mixed"][i]).T.astype(float)
        heart = np.array(f["recon_heart"][i]).T.astype(float)
    for a in (mixed, heart):
        a[~mask] = np.nan
    return mixed, heart, mask


def train_pixels(name: str) -> np.ndarray:
    """Training-split mixed-image pixel values inside the FOV, drawn the way
    tools/recon_scale_check.py computed scale_check.json (sorted training indices,
    every 12th frame, finite values), so the plotted SD is the file's SD."""
    import h5py
    with h5py.File(DATASETS[name], "r") as f:
        tr = np.sort(np.array(f["D/idx_train"]).astype(int).ravel() - 1)
        a = np.array(f["recon_mixed"][tr[::12]])
    return a[np.isfinite(a)].astype(float)


# ---- output -------------------------------------------------------------
def save(fig, stem: str, max_w_cm: float = W1, png_dpi: int = 300) -> dict:
    """PDF (vector) + PNG (reading) + TIFF (LZW, 600 dpi, RGB). 2 pt white margin.
    Returns and prints the rendered size; refuses a figure outside the PLoS limits."""
    OUT.mkdir(parents=True, exist_ok=True)
    kw = dict(bbox_inches="tight", pad_inches=2 / 72, facecolor="white")
    fig.savefig(OUT / f"{stem}.pdf", **kw)
    fig.savefig(OUT / f"{stem}.png", dpi=png_dpi, **kw)
    tif = OUT / f"{stem}.tif"
    fig.savefig(tif, dpi=600, format="tiff", pil_kwargs={"compression": "tiff_lzw"}, **kw)
    plt.close(fig)
    im = Image.open(tif)
    im.load()
    if im.mode != "RGB":                                    # flatten onto white, drop alpha
        rgba = im.convert("RGBA")
        flat = Image.new("RGB", rgba.size, (255, 255, 255))
        flat.paste(rgba, mask=rgba.split()[3])
        flat.save(tif, compression="tiff_lzw", dpi=(600, 600))
    chk = Image.open(tif)
    w_cm, h_cm = chk.size[0] / 600 * 2.54, chk.size[1] / 600 * 2.54
    png = Image.open(OUT / f"{stem}.png")
    info = {"tif_px": chk.size, "tif_mode": chk.mode,
            "tif_compression": chk.info.get("compression"),
            "png_px": png.size, "png_dpi": png_dpi,
            "w_cm": round(w_cm, 2), "h_cm": round(h_cm, 2)}
    print(f"  wrote {OUT.relative_to(ROOT)}/{stem}.pdf/.png/.tif  {info}")
    if chk.mode != "RGB" or w_cm > max_w_cm + 0.01 or h_cm > HMAX + 0.01:
        raise SystemExit(f"{stem}: outside PLoS limits {info} (max width {max_w_cm} cm)")
    return info
