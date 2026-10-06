#!/usr/bin/env python3
"""Table S9: the evaluation-only sweep for all five arms (heart channel), from the registered per-seed files.

Written 2026-10-07 to make the table emitted on 2026-10-06 (round-2 panel, DA-M2) reproducible by program
(RESEARCH_PRIMER: every reported number is program-generated). Reads results_v2_snr{60,...,20}_heart_fix/per_seed.csv,
pairs arms within seed, and reports mean Dice per arm, paired contrasts in Dice points with 95% percentile bootstrap
intervals over seeds (20,000 resamples, numpy default_rng(0)) and the number of seeds on which the first arm led.

    python3 tools/make_table_s9.py            # writes results/sweep_all_arms_heart.json and results/tables/table_s9_sweep_all_arms.md
    python3 tools/make_table_s9.py --check    # recompute and compare with the files on disk (means and lead counts must match exactly)
"""
import csv, json, sys
from pathlib import Path
import numpy as np

ROOT = Path(__file__).resolve().parents[1]
LEVELS = (60, 50, 40, 35, 30, 25, 20)
ARMS = ("B", "B_wide", "C", "C_wide", "D")
CONTRASTS = (("D", "B_wide"), ("B_wide", "B"), ("C_wide", "C"), ("D", "B"), ("C", "B"), ("C_wide", "B_wide"), ("D", "C_wide"))
N_BOOT, SEED = 20000, 0


def load(level):
    rows = [r for r in csv.DictReader(open(ROOT / f"results_v2_snr{level}_heart_fix/per_seed.csv")) if r["channel"] == "heart"]
    by = {}
    for r in rows:
        by.setdefault(r["arm"], {})[int(r["seed"])] = float(r["dsc"])
    seeds = sorted(set.intersection(*(set(by[a]) for a in ARMS)))
    return {a: np.array([by[a][s] for s in seeds]) for a in ARMS}, seeds


def contrast(a, b, rng):
    d = (a - b) * 100.0  # Dice points
    boots = rng.choice(d, size=(N_BOOT, d.size), replace=True).mean(axis=1)
    lo, hi = np.percentile(boots, [2.5, 97.5])
    return [round(float(d.mean()), 3), round(float(lo), 3), round(float(hi), 3), int((d > 0).sum())]


def compute():
    out = {}
    for lvl in LEVELS:
        arms, seeds = load(lvl)
        rng = np.random.default_rng(SEED)
        entry = {"n": len(seeds), "means": {a: round(float(arms[a].mean()), 4) for a in ARMS}}
        for x, y in CONTRASTS:
            entry[f"{x}-{y}"] = contrast(arms[x], arms[y], rng)
        out[str(lvl)] = entry
    return out


def fmt(c):
    m, lo, hi, k = c
    return f"{m:+.3f} [{lo:+.3f}, {hi:+.3f}] ({k}/58)"


def render(res):
    head = ("**Table S9.** Evaluation-only sweep for all five arms trained at 40 dB, heart-channel Dice (mean over 58 seeds) and paired "
            "contrasts in Dice points with 95% percentile bootstrap intervals over seeds (20,000 resamples) and the number of seeds on which "
            "the first arm led. Computed from the registered per-seed files (`results_v2_snr*_heart_fix/per_seed.csv`) by "
            "`tools/make_table_s9.py` in response to the round-2 panel (DA-M2); descriptive, no decision rule.\n\n")
    cols = ["SNR (dB)", "B", "B_wide", "C", "C_wide", "D", "B_wide − B (width only)", "C_wide − C (width, late split)",
            "D − B (branch, +39% params)", "C_wide − B_wide (late split)", "D − B_wide (registered)"]
    lines = ["| " + " | ".join(cols) + " |", "|" + "---|" * len(cols)]
    for lvl in LEVELS:
        e = res[str(lvl)]
        lines.append("| " + " | ".join([str(lvl)] + [f"{e['means'][a]:.4f}" for a in ARMS] +
                     [fmt(e["B_wide-B"]), fmt(e["C_wide-C"]), fmt(e["D-B"]), fmt(e["C_wide-B_wide"]), fmt(e["D-B_wide"])]) + " |")
    return head + "\n".join(lines) + "\n"


if __name__ == "__main__":
    res = compute()
    jp, mp = ROOT / "results/sweep_all_arms_heart.json", ROOT / "results/tables/table_s9_sweep_all_arms.md"
    if "--check" in sys.argv:
        old = json.loads(jp.read_text())
        bad = 0
        for lvl in LEVELS:
            o, n = old[str(lvl)], res[str(lvl)]
            if o["means"] != n["means"] or o["n"] != n["n"]:
                print(lvl, "MEANS DIFFER", o["means"], n["means"]); bad += 1
            for k in n:
                if k in ("n", "means"): continue
                if o.get(k) is None: print(lvl, k, "missing on disk"); continue
                if o[k][0] != n[k][0] or o[k][3] != n[k][3]:
                    print(lvl, k, "MEAN/COUNT DIFFER", o[k], n[k]); bad += 1
                elif o[k][1:3] != n[k][1:3]:
                    print(lvl, k, "CI differs (bootstrap RNG)", o[k][1:3], n[k][1:3])
        print("check done; hard mismatches:", bad)
    else:
        jp.write_text(json.dumps(res, indent=1) + "\n")
        mp.write_text(render(res))
        print("wrote", jp, mp)
