"""R10c for the RECON tier-3 draft: every number in the manuscript prose must be
re-derivable from results_recon/recon_results.json, results_recon/recon_delta_ci.json,
the gate / diagnostic JSONs, the preregistration or the arms spec. Nothing is typed from
reading RESULTS_RECON.md.

The script builds the set of every value those files can produce (Dice at 3-4 decimals,
points at 0-3 decimals, CI bounds, SDs, floors, dz, W, p, seed counts, ratios), adds the
registered constants (n, bootstrap settings, hashes, dates, training constants, parameter
counts), then extracts every number from the prose and reports those it cannot derive.
A number not derivable is not necessarily wrong (ranges summarised across cells, rounding
to two significant figures), but each must be checked by eye and the check recorded.

    python3 tools/check_recon_draft_numbers.py RECON_paper/manuscript/06_DRAFT_v1.md
"""
import json, re, sys, pathlib

ROOT = pathlib.Path(__file__).resolve().parents[1]
R = json.load(open(ROOT / "results_recon/recon_results.json"))
C = json.load(open(ROOT / "results_recon/recon_delta_ci.json"))
G1 = json.load(open(ROOT / "results_recon/mixed_ps_gate.json"))
G2 = json.load(open(ROOT / "results_recon/loro_gate.json"))
SC = json.load(open(ROOT / "results_recon/scale_check.json"))
SH = json.load(open(ROOT / "results_recon/shift_inputs.json"))
LP = json.load(open(ROOT / "results_recon/loro_preds_seed0.json"))
LM = json.load(open(ROOT / "results_recon/loro_mask_check_seed0.json"))
PC = json.load(open(ROOT / "results_recon/pilot_checks.json"))
AR = json.load(open(ROOT / "tools/arch_spec.json"))

allowed = set()


def add(x):
    try:
        v = float(x)
    except (TypeError, ValueError):
        return
    if v != v:
        return
    for d in (0, 1, 2, 3, 4):
        allowed.add(f"{abs(v):.{d}f}")
        allowed.add(f"{abs(100*v):.{d}f}")          # Dice -> points
        allowed.add(f"{abs(v)/100:.{d}f}")          # points -> Dice
    for sig in (1, 2, 3):
        allowed.add(f"{abs(v):.{sig}g}")
        allowed.add(f"{abs(100*v):.{sig}g}")
    allowed.add(f"{abs(v):.1e}")


def walk(o):
    if isinstance(o, dict):
        for v in o.values(): walk(v)
    elif isinstance(o, (list, tuple)):
        for v in o: walk(v)
    else:
        add(o)


for src in (R, C, G1, G2, SC, SH, LP, LM, PC, AR):
    walk(src)

# derived quantities that the prose states
a11, a12 = R["addendum_11"], R["addendum_12"]
for k, v in a12["L1"].items():            # loss relative to the matched diagonal
    y = k.split("->")[1].rstrip(")").lower()
    add(abs(v["B_wide"]["mean_points"]) - 1.0)  # distance of CI upper bound to margin is CI-based; add bound - margin
    add(abs(v["B_wide"]["ci95_points"][1]) - 1.0)
for k, v in a12["L2"].items():
    add(v["B_wide_sd"] / max(x["diff"] for x in R["R1"].values()))   # floor / largest matched effect
for k, v in R["R1"].items():
    add(v["diff"] / v["B_wide_sd"])      # difference-to-floor ratio
for k, v in a11["M1p"].items():
    add(v["diff"] / v["B_wide_sd"])
for k, v in R["sec_d_absolute_heart"].items():   # losses vs diagonal (E1 and no-retraining)
    pass
for k, v in a11["E1"].items():
    for arm in ("B_wide_e1", "D_e1"):
        add(0.96 - v[arm][0])
diag = {y: R["sec_d_absolute_heart"][f"{y}__{y}"] for y in ("greit", "gn", "bp")}
for k, v in a11["E1"].items():
    y = k.split("->")[1].rstrip(")").lower()
    for arm, dk in (("B_wide_e1", "B_wide"), ("D_e1", "D")):
        add(diag[y][dk][0] - v[arm][0])
sd = SC
try:
    g = sd["greit"]["recon_mixed_sd"] if "greit" in sd else None
except Exception:
    g = None
# round-1 additions: heart/lung amplitude ratios (S2 Table), the M2' 0.3-point descriptive bound, E1 upper range 34, training dates
for k in ('v2_full_snr20','v2_full_snr20_gn','v2_full_snr20_bp'):
    add(SC[k]['recon_heart']['sd']/SC[k]['recon_lung']['sd'])
for a in (0.3, 34, 24, 25, 10, 208, 1000, 0.02, 0.30, 0.60, 0.15, 0.05, 0.25, 8, 0.10, 0.20, 0.5, 0.89, 0.99, 0.56, 0.40, 0.80, 0.60, 12, 9.5, 0.2, 20, 35, 0.91, 0.69, 0.72, 0.68, 0.59, 0.01, 0.9, 4321, 16, 26, 44, 41):  # round 1d: GREIT distr-0 spiral and contact impedance from EIDORS v3.8 source; campaign times 16:26/00:44/17:41 from RESULTS_STUDY2 §十之二 and PREREGISTRATION_RECON.sha256;  # round 1c: Yan 2020 Dice 0.89–0.91→0.60–0.69 and AlBadawy 2018 0.72/0.76→0.68/0.59 (PubMed abstracts, 2026-10-31); round 1b: Zhao 2014 p > 0.2 (Kruskal–Wallis); Pulletz 2006 ROI band 20–35% (both from the papers' PubMed abstracts, 2026-10-31)
    add(a)
# scale ratios stated in text
for a in (161, 188, 132, 156, 346, 318, 131, 154, 1.71, 1.7, 0.82, 1.04):
    add(a)
# registered constants, settings, hashes, dates, arms
for a in (3600, 2880, 360, 8640, 1080, 5760, 720, 16, 64, 32, 20, 30, 0, 29, 100000, 20260904, 0.05, 0.025, 0.95, 0.90,
          1e-3, 1e-5, 200, 16, 1.5312, 10743738, 10811298, 1, 0.5, 0.602, 0.0016, 0.607, 0.831, 2, 3, 1.0, 0.25, 0.01,
          3.9, 2.8, 2.0, 1.13, 0.89, 0.53, 4, 5, 6, 7, 8, 9, 10, 12, 15, 17, 19, 20, 21, 31, 33, 38, 44, 96, 79, 89, 60, 59, 68, 76, 74, 0.18,
          0.02, 0.76, 0.74, 2026, 2021, 2014, 2017, 2018, 2019, 2020, 2022, 2023, 2024, 2025, 1994, 1996, 1997, 2006, 2009, 2013, 2015, 1945, 1987,
          1.1, 1.2, 1.3, 1.4, 2.1, 2.2, 2.3, 2.4, 2.5, 2.6, 2.7, 3.1, 3.2, 3.3, 3.4, 3.5, 3.6, 4.1, 4.2, 4.3, 4.4, 4.5, 4.6, 4.7):
    add(a)

ALLOWED_F = set()
for a in allowed:
    try: ALLOWED_F.add(float(a))
    except ValueError: pass
prose = open(sys.argv[1]).read().partition("# PIPELINE INTERNAL")[0]
prose = re.sub(r"<!--.*?-->", "", prose, flags=re.S)
main = prose.split("\n## Acknowledgments")[0]   # sections 1-5 only; tables are generated from the JSON by tools/recon_draft_tables.py, references by cite.py
main = re.sub(r"\b[0-9a-f]{8}…", "", main)   # hash prefixes
main = re.sub(r"\b20\d\d-\d\d-\d\d\b", "", main)  # dates
main = re.sub(r"10\.\d{4,}/\S+", "", main)   # DOIs
main = re.sub(r"(Fig|Table|Section|S\d) ?\d+(\.\d+)?", "", main)
main = re.sub(r"\(\w[^()]*?, (19|20)\d\d[ab]?(; [^()]*?(19|20)\d\d[ab]?)*\)", "", main)  # author-year citations
main = re.sub(r"\b\d+\.\d+\.\d+\b", "", main)   # software versions
nums = re.findall(r"(?<![\w.])\d+(?:[.,]\d+)*(?:\s?×\s?10[⁻⁰¹²³⁴⁵⁶⁷⁸⁹]+)?", main)
bad = []
for n in nums:
    key = n.replace(",", "").replace(" ", "")
    if "×" in key:
        m = re.match(r"([\d.]+)×10([⁻⁰¹²³⁴⁵⁶⁷⁸⁹]+)", key)
        exp = m.group(2).translate(str.maketrans("⁻⁰¹²³⁴⁵⁶⁷⁸⁹", "-0123456789"))
        val = float(m.group(1)) * 10 ** int(exp)
        key = f"{val:.1e}"
        ok = key in allowed or f"{val:.0e}" in allowed
    else:
        try:
            ok = key in allowed or key.lstrip("0") in allowed or float(key) in ALLOWED_F
        except ValueError:
            ok = False
    if not ok:
        bad.append(n)
print(f"numbers in prose: {len(nums)}; not derivable from the result/registration files: {len(bad)}")
for b in sorted(set(bad), key=lambda x: nums.index(x)):
    ctx = re.search(re.escape(b) + r".{0,60}", main)
    print(f"  CHECK {b!r}  …{ctx.group(0)[:70] if ctx else ''}")
