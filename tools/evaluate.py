"""Evaluate every trained arm on the held-out split and build the contrast table.

    python tools/evaluate.py --data data/v1/dataset.mat --runs runs/ --out results/

Replaces DICE.py, which computed a soft Dice on unnormalised 0-255 values with
axis=-1 (returning a per-row vector, not a scalar) from two hard-coded paths to
a single example image. This iterates the whole test split and saves per-image
distributions.

Metric definitions: 09_Step3_Training_Protocol.md section 3.
The DSC threshold is the quarter-amplitude set |img| > 0.25*max|img| -- EIDORS'
own calc_hm_set(img, 0.25), the basis of the GREIT figures of merit. It is a
community standard, not a threshold chosen here.
"""

from __future__ import annotations

import argparse
import json
from itertools import combinations
from pathlib import Path

import numpy as np
import torch

from arms import build_arm, count_params
from train_arms import load_dataset, normalise

QA = 0.25          # quarter-amplitude, EIDORS calc_hm_set default
BOOT = 10_000
CHANNELS = ("lung", "heart")


# ---- metrics -----------------------------------------------------------

def qa_mask(img: np.ndarray, fov: np.ndarray | None = None) -> np.ndarray:
    """Quarter-amplitude set of one image, restricted to the field of view."""
    a = np.abs(img) if fov is None else np.abs(img) * fov
    m = a.max()
    return a > QA * m if m > 0 else np.zeros_like(a, bool)


def dsc(a: np.ndarray, b: np.ndarray) -> float:
    s = a.sum() + b.sum()
    return 1.0 if s == 0 else 2.0 * (a & b).sum() / s


def iou(a: np.ndarray, b: np.ndarray) -> float:
    u = (a | b).sum()
    return 1.0 if u == 0 else (a & b).sum() / u


def sens_spec(pred: np.ndarray, gt: np.ndarray):
    tp = (pred & gt).sum(); fn = (~pred & gt).sum()
    tn = (~pred & ~gt).sum(); fp = (pred & ~gt).sum()
    se = tp / (tp + fn) if tp + fn else np.nan
    sp = tn / (tn + fp) if tn + fp else np.nan
    return float(se), float(sp)


def _edt(mask: np.ndarray) -> np.ndarray:
    from scipy.ndimage import distance_transform_edt
    return distance_transform_edt(~mask)


def boundary_distances(pred: np.ndarray, gt: np.ndarray):
    """ASSD and Hausdorff-95 between two binary masks, in pixels."""
    from scipy.ndimage import binary_erosion
    pe = pred & ~binary_erosion(pred)
    ge = gt & ~binary_erosion(gt)
    if pe.sum() == 0 or ge.sum() == 0:
        return np.nan, np.nan
    d_p, d_g = _edt(ge)[pe], _edt(pe)[ge]
    both = np.concatenate([d_p, d_g])
    return float(both.mean()), float(np.percentile(both, 95))


def per_image_metrics(pred: np.ndarray, gt: np.ndarray, sd: float,
                      fov: np.ndarray | None = None, mu: float = 0.0,
                      qa_space: str = "image") -> dict:
    """pred, gt: (H, W) in normalised units. MAE is rescaled back to the
    reconstruction's own physical units by multiplying by the dataset sd, and
    is averaged over the field of view only.

    `qa_space` decides where the quarter-amplitude set is taken, and it is not a
    cosmetic choice. PREREGISTRATION_HEART.md section 6 registers EIDORS
    `calc_hm_set(img, 0.25)`, which thresholds an image in its OWN units. The
    dataset-wide affine (x - mu)/sd is applied before the network sees anything,
    and the quarter-amplitude set is NOT affine-invariant: a shift changes which
    pixels clear the threshold.

    Measured on data/v2 (2026-09-18): thresholding in normalised space gave the
    heart a mask covering 94.8% of the field of view (median 100%) against a true
    organ fraction of 0.2% and a correct mask of 8.7%, because the heart's near-
    zero background moves to +0.481 while its peak moves to 1.135 -- so the
    background clears 0.25 x peak and the whole field enters the mask. Most
    frames then scored DSC exactly 1.0000 by comparing two whole-field masks.
    The lung was affected less (0.454 against 0.251) because its amplitude is
    several times larger.

        "image"       undo the affine first, so the threshold is taken on the
                      reconstruction in its own units. This is the registered
                      quantity and the default.
        "normalised"  the defective path, kept only to reproduce the numbers
                      reported before 2026-09-18 for the deviation record.

    MAE is unaffected either way: it is a difference, so the offset cancels, and
    it is already rescaled by sd.
    """
    if qa_space == "image":
        pm, gm = qa_mask(pred * sd + mu, fov), qa_mask(gt * sd + mu, fov)
    elif qa_space == "normalised":
        pm, gm = qa_mask(pred, fov), qa_mask(gt, fov)
    else:
        raise ValueError(f"unknown qa_space {qa_space!r}")
    se, sp = sens_spec(pm, gm)
    assd, hd95 = boundary_distances(pm, gm)
    return {
        "mae": float((np.abs(pred - gt)[fov] if fov is not None
                      else np.abs(pred - gt)).mean() * sd),
        "dsc": dsc(pm, gm), "iou": iou(pm, gm),
        "sens": se, "spec": sp, "assd": assd, "hd95": hd95,
    }


# ---- statistics --------------------------------------------------------

def boot_ci(x: np.ndarray, rng, n=BOOT):
    x = x[~np.isnan(x)]
    if x.size == 0:
        return (np.nan, np.nan)
    idx = rng.integers(0, x.size, size=(n, x.size))
    means = x[idx].mean(axis=1)
    return tuple(float(v) for v in np.percentile(means, [2.5, 97.5]))


def paired_test(a: np.ndarray, b: np.ndarray):
    """Paired comparison across seeds.

    Wilcoxon signed-rank is primary; a paired t-test is reported alongside.

    Discreteness floor: on n paired seeds the smallest two-sided p Wilcoxon can
    return is 2/2**n -- 0.0625 at n=5, 0.002 at n=10. A rule written at
    alpha=0.05 is therefore unsatisfiable with 5 seeds, which is why the
    protocol uses 10. `p_floor` is returned so the caller can check that the
    rule it is applying is attainable at all.
    """
    from scipy.stats import wilcoxon, ttest_rel
    n = len(a)
    floor = 2.0 / 2**n if n else float("nan")
    d = a - b
    sd = d.std(ddof=1) if n > 1 else 0.0
    if np.allclose(d, 0):
        return {"p": 1.0, "p_t": 1.0, "p_floor": floor,
                "mean_diff": 0.0, "cohen_dz": 0.0, "n": n}
    try:
        p = float(wilcoxon(a, b).pvalue)
    except ValueError:
        p = float("nan")
    try:
        p_t = float(ttest_rel(a, b).pvalue)
    except ValueError:
        p_t = float("nan")
    return {"p": p, "p_t": p_t, "p_floor": floor,
            "mean_diff": float(d.mean()),
            "cohen_dz": float(d.mean() / sd) if sd else float("inf"),
            "n": n}


# ---- main --------------------------------------------------------------

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--data", required=True,
                    help="path to dataset.mat — REQUIRED, must match the one "
                         "the runs were trained on")
    ap.add_argument("--runs", default="runs")
    ap.add_argument("--out", default="results")
    ap.add_argument("--primary", nargs=2, default=["D", "B_wide"],
                    help="the preregistered primary contrast")
    ap.add_argument("--qa-space", default="image",
                    choices=["image", "normalised"],
                    help="where the quarter-amplitude set is taken. 'image' "
                         "undoes the dataset affine first and is the registered "
                         "quantity (see per_image_metrics). 'normalised' "
                         "reproduces the defective pre-2026-09-18 numbers.")
    ap.add_argument("--channel", default="lung", choices=["lung", "heart"],
                    help="channel carrying the primary endpoint. Study 1 "
                         "registered lung (the default, so its results "
                         "reproduce byte-identically); study 2 registered "
                         "heart. Without this the tool cannot compute the "
                         "endpoint study 2 actually registered.")
    ap.add_argument("--affine-from-data", default=None,
                    help="dataset.mat whose TRAINING split supplies the "
                         "normalisation affine instead of --data's own. For "
                         "cross-reconstructor cells (PREREGISTRATION_RECON.md "
                         "R3) this is the dataset the runs were trained on, so "
                         "the network sees exactly what deployment would see. "
                         "Absent (default) the behaviour is unchanged.")
    args = ap.parse_args()

    runs, out = Path(args.runs), Path(args.out)
    out.mkdir(parents=True, exist_ok=True)
    rng = np.random.default_rng(0)
    device = ("cuda" if torch.cuda.is_available()
              else "mps" if torch.backends.mps.is_available() else "cpu")

    mixed, lung, heart, idx, mask = load_dataset(Path(args.data))
    if args.affine_from_data:
        tr_mixed, _, _, tr_idx, tr_mask = load_dataset(Path(args.affine_from_data))
        mu, sd, _ = normalise(tr_mixed[tr_idx["train"]], tr_mask, tr_mixed[:1])
        mixed, lung, heart = ((a - mu) / sd * mask for a in (mixed, lung, heart))
        print(f"normalisation affine taken from {args.affine_from_data} training split: mu={mu:.4f} sd={sd:.4f}")
    else:
        mu, sd, (mixed, lung, heart) = normalise(
            mixed[idx["train"]], mask, mixed, lung, heart)
    te = idx["test"]
    x = torch.from_numpy(mixed[te]).unsqueeze(1)
    gt = {"lung": lung[te], "heart": heart[te]}

    rows, per_image = [], []
    for meta_path in sorted(runs.glob("*_seed*.json")):
        meta = json.loads(meta_path.read_text())
        arm, seed = meta["arm"], meta["seed"]
        model = build_arm(arm, width_mult=meta["width_mult"]).to(device)
        model.load_state_dict(torch.load(
            meta_path.with_suffix(".pt"), map_location=device))
        model.eval()

        with torch.no_grad():
            pred = torch.cat([model(x[i:i + 32].to(device)).cpu()
                              for i in range(0, len(x), 32)]).numpy()

        chans = ("lung",) if arm == "A" else CHANNELS
        for ci, ch in enumerate(chans):
            ms = [per_image_metrics(pred[i, ci], gt[ch][i], sd, mask,
                                    mu=mu, qa_space=args.qa_space)
                  for i in range(len(te))]
            for i, m in enumerate(ms):
                per_image.append({"arm": arm, "seed": seed, "channel": ch,
                                  "index": int(te[i]), **m})
            agg = {k: float(np.nanmean([m[k] for m in ms])) for k in ms[0]}
            rows.append({"arm": arm, "seed": seed, "channel": ch,
                         "params": meta["params"],
                         "width_mult": meta["width_mult"], **agg})
            print(f"{arm:8s} seed{seed} {ch:6s} "
                  f"DSC {agg['dsc']:.4f}  MAE {agg['mae']:.5f}")

    import csv
    with open(out / "per_image.csv", "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=list(per_image[0]))
        w.writeheader(); w.writerows(per_image)
    with open(out / "per_seed.csv", "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0]))
        w.writeheader(); w.writerows(rows)

    # ---- Table 1: mean +/- SD across seeds -----------------------------
    arms = sorted({r["arm"] for r in rows})
    table = {}
    print(f"\n=== Table 1 ({args.channel} channel, mean +/- SD over seeds) ===")
    print(f"{'arm':9s} {'params':>12s} {'DSC':>16s} {'MAE':>16s}")
    for a in arms:
        sel = [r for r in rows if r["arm"] == a and r["channel"] == args.channel]
        if not sel:
            continue
        e = {k: (float(np.mean([r[k] for r in sel])),
                 float(np.std([r[k] for r in sel], ddof=1)))
             for k in ("dsc", "mae", "iou", "sens", "spec", "assd", "hd95")}
        e["params"] = sel[0]["params"]
        e["n_seeds"] = len(sel)
        table[a] = e
        print(f"{a:9s} {e['params']:12,d} "
              f"{e['dsc'][0]:8.4f}+/-{e['dsc'][1]:.4f} "
              f"{e['mae'][0]:8.5f}+/-{e['mae'][1]:.5f}")

    # ---- contrasts -----------------------------------------------------
    contrasts = {}
    for a, b in combinations(arms, 2):
        sa = sorted([r for r in rows if r["arm"] == a
                     and r["channel"] == args.channel], key=lambda r: r["seed"])
        sb = sorted([r for r in rows if r["arm"] == b
                     and r["channel"] == args.channel], key=lambda r: r["seed"])
        if len(sa) != len(sb) or not sa:
            continue
        va = np.array([r["dsc"] for r in sa])
        vb = np.array([r["dsc"] for r in sb])
        contrasts[f"{a}-{b}"] = paired_test(va, vb)

    prim = f"{args.primary[0]}-{args.primary[1]}"
    prim_rev = f"{args.primary[1]}-{args.primary[0]}"
    key = prim if prim in contrasts else prim_rev
    print(f"\n=== Contrasts ({args.channel} DSC, paired across seeds) ===")
    for k, v in sorted(contrasts.items()):
        mark = "  <== PRIMARY" if k == key else ""
        print(f"{k:20s} diff {v['mean_diff']:+.4f}  dz {v['cohen_dz']:+.2f}  "
              f"p {v['p']:.4f} (t {v['p_t']:.4f}){mark}")

    # ---- the preregistered decision rule -------------------------------
    verdict = None
    if key in contrasts and args.primary[1] in table:
        v = contrasts[key]
        ctrl_sd = table[args.primary[1]]["dsc"][1]
        diff = v["mean_diff"] if key == prim else -v["mean_diff"]
        if v["p_floor"] > 0.05:
            print(f"\nWARNING: {v['n']} seeds -- the smallest p Wilcoxon can "
                  f"return is {v['p_floor']:.4f}, so an alpha=0.05 rule is "
                  f"unsatisfiable. Use 10 seeds (09 section 5).")
        passed = bool(diff > ctrl_sd and v["p"] < 0.05)
        verdict = {"contrast": prim, "diff": diff, "control_seed_sd": ctrl_sd,
                   "p": v["p"], "branching_helps": passed}
        print(f"\nPrimary: {prim} = {diff:+.4f} DSC; "
              f"control seed SD = {ctrl_sd:.4f}; p = {v['p']:.4f}")
        print("VERDICT: branching improves on width-matched capacity"
              if passed else
              "VERDICT: branching does NOT improve on width-matched capacity")
        print("Whichever way this falls, it is the finding. Report it as it is.")

    (out / "summary.json").write_text(json.dumps(
        {"table": table, "contrasts": contrasts, "verdict": verdict,
         "qa_threshold": QA, "norm": {"mu": mu, "sd": sd}}, indent=2))
    print(f"\nwrote {out}/per_image.csv, per_seed.csv, summary.json")


if __name__ == "__main__":
    main()
