"""RECON matrix: the registered statistics of PREREGISTRATION_RECON.md, from per_seed.csv only.

    python3 tools/recon_results.py --results results_recon --out results_recon/recon_results.json

Every number in RESULTS_RECON.md comes from this script (R10c: recomputable from
per_seed). It applies the registered rules mechanically and interprets nothing.

Rules, verbatim from PREREGISTRATION_RECON.md:
  R1 / M1  confirmed if mean DSC_heart(D) - DSC_heart(B_wide) exceeds B_wide's
           seed-to-seed SD under that cell AND Wilcoxon signed-rank (two-sided,
           normal approximation with continuity correction) over paired seeds
           gives p < 0.05; falsified if either fails or the sign is reversed.
  R3       Delta(X->Y) - Delta(X->X) > 0 with a 95% percentile bootstrap CI over
           paired seeds (100,000 resamples) excluding zero; falsified if the CI
           contains zero or the difference is negative.
Registered n = 30 seeds (0-29) in every cell. The GREIT row reuses runs_20db,
which holds 58 seeds; only 0-29 enter a registered statistic, and the 58-seed
GREIT diagonal is printed beside it as the section 9.2 reference.

Section 11 addendum (2026-10-10, computed only when results_recon/mixedps__greit
exists; every registered quantity above is computed first and is unchanged):
  M1'      the R1 rule on the three mixed-ps cells (mixedps__<Y>, own affine).
  M2'      DSC(mixed-ps->Y) - DSC(Y->Y), per Y and arm, paired by seed, same CI.
  M3'      DSC(mixed-ps->Y) - DSC(X->Y), X != Y, per arm, same CI; the registered
           X->Y cell carries the 11.2 input note (degenerate / over-range / in-range).
  E1       exploratory re-scoring of the six R3 cells (<X>__<Y>_e1): Delta and the
           difference of differences against Delta(X->X), R3 bootstrap, NO verdict.

Section 12 addendum (2026-10-17, computed only when all nine results_recon/loro_*
directories exist; everything above is computed first and is unchanged):
  L1       TESTED, equivalence: DSC_heart(B_wide, loro-Y->Y) - DSC_heart(B_wide, mixed-ps->Y),
           paired by seed index, 95% percentile bootstrap CI (same B, same seed);
           CONFIRMED if the whole CI lies within [-1.0, +1.0] Dice points, FALSIFIED
           otherwise (12.5). The same quantity for D is reported beside it, not tested.
  L2       TESTED, the R1 rule on the three held-out cells loro_<Y>__<Y> (own affine).
  L3'      reported only: DSC(loro-Y->Y) - DSC(Y->Y) and DSC(loro-Y->Y) - DSC(X->Y) for
           the two registered no-retraining cells X->Y (11.2 input note), per arm, same CI.
  in-pool  reported only: the two in-pool references loro_<Y>__<X> as absolute DSC +/- seed SD.
  Nothing in section 12 re-reads R1, R3, M1 or M1' (12.1, 12.7).

Bootstrap: seeds are resampled, not images. Each bootstrapped quantity gets a
fresh generator seeded with --seed, so a number does not depend on the order in
which the others were computed. 20260904 is the seed h3_snr.py used for H3.
"""
from __future__ import annotations

import argparse
import csv
import json
from pathlib import Path

import numpy as np
from scipy.stats import wilcoxon

SEEDS = list(range(30))                 # registered n = 30
RECON = ["greit", "gn", "bp"]           # evaluation sets
TRAIN = ["greit", "gn", "bp", "mixed"]  # training sets


def load(results: Path, cell: str, arm: str, channel: str, seeds=SEEDS) -> np.ndarray:
    got: dict[int, float] = {}
    with open(results / cell / "per_seed.csv") as fh:
        for r in csv.DictReader(fh):
            if r["arm"] == arm and r["channel"] == channel:
                got[int(r["seed"])] = float(r["dsc"])
    missing = [s for s in seeds if s not in got]
    if missing:
        raise SystemExit(f"{cell}: arm {arm} {channel} missing seeds {missing}")
    return np.array([got[s] for s in seeds])


def all_seeds(results: Path, cell: str) -> list[int]:
    with open(results / cell / "per_seed.csv") as fh:
        return sorted({int(r["seed"]) for r in csv.DictReader(fh)})


def boot(x: np.ndarray, n_boot: int, seed: int) -> tuple[float, float]:
    rng = np.random.default_rng(seed)
    idx = rng.integers(0, x.size, (n_boot, x.size))
    lo, hi = np.percentile(x[idx].mean(axis=1), [2.5, 97.5])
    return float(lo), float(hi)


def r1_rule(results: Path, cell: str, channel: str = "heart", seeds=SEEDS) -> dict:
    d, b = load(results, cell, "D", channel, seeds), load(results, cell, "B_wide", channel, seeds)
    diff = d - b
    p = float(wilcoxon(d, b, correction=True, method="approx").pvalue)
    sd_b = float(b.std(ddof=1))
    m = float(diff.mean())
    out = {"cell": cell, "channel": channel, "n": len(seeds),
           "D_mean": float(d.mean()), "D_sd": float(d.std(ddof=1)),
           "B_wide_mean": float(b.mean()), "B_wide_sd": sd_b,
           "diff": m, "diff_sd": float(diff.std(ddof=1)),
           "dz": m / float(diff.std(ddof=1)), "p_wilcoxon": p,
           "exceeds_sd": m > sd_b, "p_lt_05": p < 0.05}
    if m <= 0:
        out["verdict"] = "FALSIFIED (sign reversed)"
    elif m > sd_b and p < 0.05:
        out["verdict"] = "CONFIRMED"
    else:
        fails = [w for w, ok in (("diff <= B_wide SD", m > sd_b), ("p >= 0.05", p < 0.05)) if not ok]
        out["verdict"] = "FALSIFIED (" + "; ".join(fails) + ")"
    return out


def delta(results: Path, cell: str, channel: str = "heart") -> np.ndarray:
    return load(results, cell, "D", channel) - load(results, cell, "B_wide", channel)


E1_INPUT_NOTE = {  # PREREGISTRATION_RECON.md 11.2, seed-0 pass of recon_shift_inputs.py
    ("greit", "gn"): "degenerate input", ("greit", "bp"): "degenerate input",
    ("gn", "greit"): "over-range input", ("bp", "greit"): "over-range input",
    ("gn", "bp"): "in-range input", ("bp", "gn"): "in-range input"}


def addendum_11(R: Path, B: int, S: int) -> dict:
    """M1', M2', M3', E1 of section 11. Same rules, same loaders, same bootstrap."""
    out: dict = {"note": "section 11 addendum (post-unblinding); M2', M3', E1 carry no verdict"}
    out["M1p"] = {f"M1'-(MIXED-PS->{y.upper()})": r1_rule(R, f"mixedps__{y}") for y in RECON}
    out["M1p_lung"] = {f"mixedps__{y}": r1_rule(R, f"mixedps__{y}", channel="lung") for y in RECON}
    out["M2p"] = {}
    for y in RECON:
        for arm in ("B_wide", "D"):
            x = load(R, f"mixedps__{y}", arm, "heart") - load(R, f"{y}__{y}", arm, "heart")
            out["M2p"][f"{arm}: mixed-ps->{y} - {y}->{y}"] = {"mean": float(x.mean()), "ci95": list(boot(x, B, S))}
    out["M3p"] = {}
    for x_ in RECON:
        for y in RECON:
            if x_ == y:
                continue
            for arm in ("B_wide", "D"):
                v = load(R, f"mixedps__{y}", arm, "heart") - load(R, f"{x_}__{y}", arm, "heart")
                out["M3p"][f"{arm}: mixed-ps->{y} - {x_}->{y}"] = {
                    "mean": float(v.mean()), "ci95": list(boot(v, B, S)),
                    "registered_cell_input": E1_INPUT_NOTE[(x_, y)]}
    out["E1"] = {}
    for x_ in RECON:
        dxx = delta(R, f"{x_}__{x_}")
        for y in RECON:
            if x_ == y:
                continue
            de1 = delta(R, f"{x_}__{y}_e1")
            dod = de1 - dxx
            row = {"delta_XY_e1": float(de1.mean()), "delta_XY_registered": float(delta(R, f"{x_}__{y}").mean()),
                   "delta_XX": float(dxx.mean()), "dod_e1": float(dod.mean()), "ci95": list(boot(dod, B, S)),
                   "verdict": "EXPLORATORY, NO VERDICT (11.5)", "registered_cell_input": E1_INPUT_NOTE[(x_, y)]}
            for arm in ("D", "B_wide"):
                ve1, vr = load(R, f"{x_}__{y}_e1", arm, "heart"), load(R, f"{x_}__{y}", arm, "heart")
                row[f"{arm}_e1"] = [float(ve1.mean()), float(ve1.std(ddof=1))]
                row[f"{arm}_registered"] = [float(vr.mean()), float(vr.std(ddof=1))]
            out["E1"][f"E1-({x_.upper()}->{y.upper()})"] = row
    return out


L1_MARGIN_POINTS = 1.0   # PREREGISTRATION_RECON.md 12.5, fixed before the rows were trained


def addendum_12(R: Path, B: int, S: int) -> dict:
    """L1, L2, L3' and the in-pool references of section 12. Same rules, same loaders, same bootstrap."""
    out: dict = {"note": "section 12 addendum (post-unblinding, hashed before training); "
                         "L1 and L2 are tested, L3' and the in-pool references carry no verdict",
                 "L1_margin_points": L1_MARGIN_POINTS}
    # ---- L1: equivalence of B_wide on the held-out reconstructor vs the mixed-ps row ----
    out["L1"] = {}
    for y in RECON:
        row = {}
        for arm in ("B_wide", "D"):
            x = load(R, f"loro_{y}__{y}", arm, "heart") - load(R, f"mixedps__{y}", arm, "heart")
            lo, hi = boot(x, B, S)
            q = {"mean": float(x.mean()), "sd": float(x.std(ddof=1)), "ci95": [lo, hi], "n": int(x.size),
                 "mean_points": float(100 * x.mean()), "ci95_points": [100 * lo, 100 * hi],
                 "within_margin": bool(100 * lo >= -L1_MARGIN_POINTS and 100 * hi <= L1_MARGIN_POINTS)}
            if arm == "B_wide":
                q["verdict"] = ("CONFIRMED (whole CI within +/-%.1f points)" % L1_MARGIN_POINTS if q["within_margin"]
                                else "FALSIFIED (CI not within +/-%.1f points)" % L1_MARGIN_POINTS)
            else:
                q["verdict"] = "REPORTED, NOT TESTED (12.5)"
            row[arm] = q
        out["L1"][f"L1-(LORO-{y.upper()}->{y.upper()})"] = row
    # ---- L2: the R1 rule on the held-out cells (plus the CI / W columns of RESULTS section 10(a)) ----
    out["L2"] = {}
    for y in RECON:
        q = r1_rule(R, f"loro_{y}__{y}")
        d, b = load(R, f"loro_{y}__{y}", "D", "heart"), load(R, f"loro_{y}__{y}", "B_wide", "heart")
        q["diff_ci95"] = list(boot(d - b, B, S))
        q["W"] = float(wilcoxon(d, b, correction=True, method="approx").statistic)
        q["D_gt_B_wide_seeds"] = int((d > b).sum())
        out["L2"][f"L2-(LORO-{y.upper()}->{y.upper()})"] = q
    out["L2_lung"] = {f"loro_{y}__{y}": r1_rule(R, f"loro_{y}__{y}", channel="lung") for y in RECON}
    # ---- L3': reported only ----
    out["L3p_vs_specialised"] = {}
    out["L3p_vs_no_retraining"] = {}
    for y in RECON:
        for arm in ("B_wide", "D"):
            v = load(R, f"loro_{y}__{y}", arm, "heart") - load(R, f"{y}__{y}", arm, "heart")
            out["L3p_vs_specialised"][f"{arm}: loro-{y}->{y} - {y}->{y}"] = {
                "mean": float(v.mean()), "ci95": list(boot(v, B, S))}
            for x_ in RECON:
                if x_ == y:
                    continue
                w = load(R, f"loro_{y}__{y}", arm, "heart") - load(R, f"{x_}__{y}", arm, "heart")
                out["L3p_vs_no_retraining"][f"{arm}: loro-{y}->{y} - {x_}->{y}"] = {
                    "mean": float(w.mean()), "ci95": list(boot(w, B, S)),
                    "registered_cell_input": E1_INPUT_NOTE[(x_, y)]}
    # ---- absolute DSC: held-out cells and the in-pool references ----
    out["absolute_heart"] = {}
    for ho in RECON:
        for ev in RECON:
            cell = f"loro_{ho}__{ev}"
            out["absolute_heart"][cell] = {
                "role": "held-out (L1/L2)" if ho == ev else "in-pool reference (reported only)",
                **{arm: [float(v.mean()), float(v.std(ddof=1))]
                   for arm in ("D", "B_wide") for v in [load(R, cell, arm, "heart")]}}
    # ---- per-seed range (min / max over seeds 0-29), reported only (REV-P3-3, 2026-10-17) ----
    out["seed_range_heart"] = {
        f"loro_{ho}__{ev}": {arm: [float(v.min()), float(v.max())]
                             for arm in ("D", "B_wide") for v in [load(R, f"loro_{ho}__{ev}", arm, "heart")]}
        for ho in RECON for ev in RECON}
    return out


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--results", type=Path, default=Path("results_recon"))
    ap.add_argument("--pilot", type=Path, default=Path("results_recon/pilot_checks.json"))
    ap.add_argument("--out", type=Path, default=Path("results_recon/recon_results.json"))
    ap.add_argument("--n-boot", type=int, default=100000)
    ap.add_argument("--seed", type=int, default=20260904)
    a = ap.parse_args()
    R, B, S = a.results, a.n_boot, a.seed
    res: dict = {"seeds": SEEDS, "n_boot": B, "boot_seed": S}

    # ---- R1 (registered order: GN, then BP) + GREIT diagonal reference -------
    res["R1"] = {f"R1-{x.upper()}": r1_rule(R, f"{x}__{x}") for x in ("gn", "bp")}
    g58 = all_seeds(R, "greit__greit")
    res["greit_diagonal_reference"] = {
        "seeds_0_29": r1_rule(R, "greit__greit"),
        f"seeds_all_{len(g58)}": r1_rule(R, "greit__greit", seeds=g58)}

    # ---- R3, six cells ------------------------------------------------------
    res["R3"] = {}
    for x in RECON:
        dxx = delta(R, f"{x}__{x}")
        for y in RECON:
            if y == x:
                continue
            dxy = delta(R, f"{x}__{y}")
            dod = dxy - dxx
            lo, hi = boot(dod, B, S)
            obs = float(dod.mean())
            if obs > 0 and lo > 0:
                v = "CONFIRMED"
            elif obs <= 0:
                v = "FALSIFIED (difference negative)" if obs < 0 else "FALSIFIED (difference zero)"
            else:
                v = "FALSIFIED (CI contains zero)"
            res["R3"][f"R3-({x.upper()}->{y.upper()})"] = {
                "delta_XY": float(dxy.mean()), "delta_XX": float(dxx.mean()),
                "dod": obs, "ci95": [lo, hi], "verdict": v}

    # ---- M1, three cells ----------------------------------------------------
    res["M1"] = {f"M1-(MIXED->{y.upper()})": r1_rule(R, f"mixed__{y}") for y in RECON}

    # ---- secondaries (reported, not tested) ---------------------------------
    pilot = json.loads(a.pilot.read_text())
    res["sec_a_perturbation_40_to_20"] = {
        x: {k: pilot[f"perturbation_40_to_20_{x}"][k]["median"]
            for k in ("peak_fraction_pct", "rms_fraction_pct")} for x in RECON}

    res["sec_b_lung"] = {f"{t}__{y}": r1_rule(R, f"{t}__{y}", channel="lung")
                         for t in TRAIN for y in RECON}

    sec_c = {}
    for t in TRAIN:
        for y in RECON:
            if t == y:
                continue
            reg, own = delta(R, f"{t}__{y}"), delta(R, f"{t}__{y}_ownaffine")
            row = {"delta_registered_affine": float(reg.mean()),
                   "delta_own_affine": float(own.mean())}
            for arm in ("D", "B_wide"):
                row[f"{arm}_registered_affine"] = float(load(R, f"{t}__{y}", arm, "heart").mean())
                row[f"{arm}_own_affine"] = float(load(R, f"{t}__{y}_ownaffine", arm, "heart").mean())
            if t != "mixed":
                dod = own - delta(R, f"{t}__{t}")
                row["dod_own_affine"] = float(dod.mean())
                row["dod_own_affine_ci95"] = list(boot(dod, B, S))
            sec_c[f"{t}__{y}"] = row
    res["sec_c_own_affine"] = sec_c

    res["sec_d_absolute_heart"] = {
        f"{t}__{y}": {arm: [float(v.mean()), float(v.std(ddof=1))]
                      for arm in ("D", "B_wide")
                      for v in [load(R, f"{t}__{y}", arm, "heart")]}
        for t in TRAIN for y in RECON}

    # ---- M2, M3 (reported, not tested) --------------------------------------
    res["M2"] = {}
    for y in RECON:
        for arm in ("B_wide", "D"):
            x = load(R, f"mixed__{y}", arm, "heart") - load(R, f"{y}__{y}", arm, "heart")
            res["M2"][f"{arm}: mixed->{y} - {y}->{y}"] = {"mean": float(x.mean()), "ci95": list(boot(x, B, S))}
    res["M3"] = {}
    for x_ in RECON:
        for y in RECON:
            if x_ == y:
                continue
            for arm in ("B_wide", "D"):
                v = load(R, f"mixed__{y}", arm, "heart") - load(R, f"{x_}__{y}", arm, "heart")
                res["M3"][f"{arm}: mixed->{y} - {x_}->{y}"] = {"mean": float(v.mean()), "ci95": list(boot(v, B, S))}

    # ---- section 11 addendum, after everything registered ------------------
    show = ["R1", "R3", "M1"]
    if (R / "mixedps__greit" / "per_seed.csv").exists():
        res["addendum_11"] = addendum_11(R, B, S)
        show.append("addendum_11")
    if all((R / f"loro_{ho}__{ev}" / "per_seed.csv").exists() for ho in RECON for ev in RECON):
        res["addendum_12"] = addendum_12(R, B, S)
        show.append("addendum_12")

    a.out.write_text(json.dumps(res, indent=1))
    print(json.dumps({k: res[k] for k in show}, indent=1))
    print(f"\nwrote {a.out}")


if __name__ == "__main__":
    main()
