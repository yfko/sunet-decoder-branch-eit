"""Render Tables 1-4 and the supplementary S2/S3 tables of the RECON tier-3 manuscript as
Markdown, reading only results_recon/recon_results.json, results_recon/recon_delta_ci.json,
results_recon/scale_check.json, PREREGISTRATION_RECON.md / .sha256 and tools/arch_spec.json
(MANUSCRIPT_RULES R10c: no number is typed by hand; every quoted rule is a substring of the
hashed preregistration file, asserted at render time).

Revision round 1 (2026-10-31, five-seat panel REV-M1-*): Table 1 GREIT row carries no verdict
(REV-M1-1), paired-difference SD columns (REV-M1-10), Table 2 R-path Dice and E1 MDE80 (REV-M1-10,
-16), Table 3 upper-bound clause and SD note (REV-M1-17, -29), Table 4 post-read row and exact
registered-state wording (REV-M1-9, -20), S2 Table body (REV-M1-19, -9, -10) and S3 Table of
verbatim rules (REV-M1-8).

    python3 tools/recon_draft_tables.py > RECON_paper/manuscript/phase4_draft/tables.md
"""
import json, re, sys, pathlib

ROOT = pathlib.Path(__file__).resolve().parents[1]
R = json.load(open(ROOT / "results_recon/recon_results.json"))
C = json.load(open(ROOT / "results_recon/recon_delta_ci.json"))
SC = json.load(open(ROOT / "results_recon/scale_check.json"))
AR = json.load(open(ROOT / "tools/arch_spec.json"))
PREREG = (ROOT / "PREREGISTRATION_RECON.md").read_text(encoding="utf-8")
A11, A12 = R["addendum_11"], R["addendum_12"]
P = lambda x: 100 * x  # Dice -> points


def neg(s):
    return s.replace("-", "−")  # typographic minus, never ASCII hyphen (core-paper NEW-1)


def pts(x, d=3):
    return neg(f"{P(x):+.{d}f}")


def ci(c, d=2):
    return neg(f"[{P(c[0]):+.{d}f}, {P(c[1]):+.{d}f}]")


def pfmt(p):
    return neg(f"{p:.1e}") if p < 0.001 else f"{p:.2g}" if p < 0.01 else f"{p:.2f}" if p >= 0.1 else f"{p:.3g}"


def lab(k):
    return k.replace("->", "→").replace(" - ", " − ").replace("greit", "GREIT").replace("gn", "GN").replace("bp", "BP")


def verdict(v):
    return "falsified" if v.startswith("FALSIFIED") else v.lower()


def q(s):
    """Verbatim quotation from the hashed preregistration; asserted present."""
    assert s in PREREG, s[:60]
    return s


out = []

# ---------------- Table 1
out.append("**Table 1. Matched-training cells and the pooled rows.** Heart-channel Dice, test split, seeds 0–29 (n = 30). Δ = D − B_wide in Dice points (0.01); 95% CI by percentile bootstrap over paired seeds (100,000 resamples); SD(Δ) = seed SD of the paired difference; floor = B_wide's seed-to-seed SD; W = Wilcoxon signed-rank statistic; p two-sided, normal approximation with continuity correction. Standing: R = registered (hash 4b4c7a6d…), A1 = first addendum (0060eedf…), ref = reference cell re-scored from the companion study's networks, no hypothesis tested, no verdict.")
out.append("")
out.append("| Cell (train → evaluate) | Standing | B_wide Dice (mean ± SD) | D Dice (mean ± SD) | Δ (points) | 95% CI | SD(Δ) | Floor | dz | W | p | D > B_wide | Verdict |")
out.append("|---|---|---|---|---|---|---|---|---|---|---|---|---|")
rows = [
    ("R1-GN (GN → GN)", "R", R["R1"]["R1-GN"], C["tested_cells"]["R1-GN"]),
    ("R1-BP (BP → BP)¹", "R", R["R1"]["R1-BP"], C["tested_cells"]["R1-BP"]),
    ("GREIT → GREIT", "ref", R["greit_diagonal_reference"]["seeds_0_29"], C["tested_cells"]["GREIT-diag-30"]),
    ("M1 (mixed → GREIT)", "R", R["M1"]["M1-(MIXED->GREIT)"], C["tested_cells"]["M1-(MIXED->GREIT)"]),
    ("M1 (mixed → GN)²", "R", R["M1"]["M1-(MIXED->GN)"], C["tested_cells"]["M1-(MIXED->GN)"]),
    ("M1 (mixed → BP)¹ ²", "R", R["M1"]["M1-(MIXED->BP)"], C["tested_cells"]["M1-(MIXED->BP)"]),
    ("M1′ (mixed-ps → GREIT)", "A1", A11["M1p"]["M1'-(MIXED-PS->GREIT)"], C["tested_cells"]["M1'-(MIXED-PS->GREIT)"]),
    ("M1′ (mixed-ps → GN)", "A1", A11["M1p"]["M1'-(MIXED-PS->GN)"], C["tested_cells"]["M1'-(MIXED-PS->GN)"]),
    ("M1′ (mixed-ps → BP)¹", "A1", A11["M1p"]["M1'-(MIXED-PS->BP)"], C["tested_cells"]["M1'-(MIXED-PS->BP)"]),
]
for name, st, r, c in rows:
    assert abs(r["diff"] - c["delta_mean"]) < 1e-12
    v = "— (reference; same pattern, below the floor)" if st == "ref" else verdict(r["verdict"])
    out.append(f"| {name} | {st} | {r['B_wide_mean']:.4f} ± {r['B_wide_sd']:.4f} | {r['D_mean']:.4f} ± {r['D_sd']:.4f} | {pts(r['diff'])} | {ci(c['delta_ci95'])} | {P(c['delta_sd']):.3f} | {P(r['B_wide_sd']):.3f} | {r['dz']:+.2f} | {c['wilcoxon_W']:.0f} | {pfmt(r['p_wilcoxon'])} | {c['seeds_D_gt_B']}/30 | {v} |")
out.append("")
out.append("¹ BP single-organ peaks are offset from GREIT's by up to 2 px on the 64 × 64 raster (one pixel of BP's native grid; preregistration §10). ² Under the single pooled affine the GN and BP inputs vary by 1/132 and 1/156 of a GREIT input (Section 3.3); the registered verdict stands, and the cell is not read as evidence about pooled training. The GREIT → GREIT row is the registered reference (the companion study's networks, seeds 0–29, re-scored here); R1 names GN and BP only, so this row carries no verdict.")
out.append("")
out.append("M2′ (A1; reported, not tested; descriptive): mixed-ps → Y minus Y → Y, paired by seed, points [95% CI]: "
           + "; ".join(f"{lab(k)} {pts(v['mean'])} {ci(v['ci95'])}" for k, v in A11["M2p"].items()) + ". "
           + "Registered M2 (R; mixed → Y minus Y → Y): "
           + "; ".join(f"{lab(k)} {pts(v['mean'], 1)} {ci(v['ci95'], 1)}" for k, v in R["M2"].items()) + ".")
out.append("")

# ---------------- Table 2
out.append("**Table 2. Reconstructor change without retraining: the six registered R3 cells, the exploratory E1 re-scoring and M3′.** Difference of differences (DoD) = Δ(X→Y) − Δ(X→X) in points, 95% percentile bootstrap CI over paired seeds; SD = seed SD of the DoD; MDE80 = DoD detectable with 80% power at n = 30 (paired-t approximation, dz 0.53), given for the registered and the E1 path; input state from the seed-0 diagnosis (within-frame SD of the network's input under the training set's affine; diagonal ≈ 0.82). Dice columns give the absolute heart Dice of B_wide / D under the registered path (training set's affine for input and output) and under E1 (evaluation set's affine for the input, training set's for the output). M3′ = Dice(mixed-ps → Y) − Dice(X → Y) in points, the latter being the registered-path cell. Standing: R = registered; E = exploratory, no verdict (A1); A1 = first addendum, reported, not tested.")
out.append("")
out.append("| Cell X → Y | Input state (R path) | B_wide / D Dice, R path | Δ(X→Y) R | DoD R (points) | 95% CI | SD | MDE80 R | Verdict (R) | B_wide / D Dice, E1 | Δ(X→Y) E1 | DoD E1 (points) | 95% CI | MDE80 E1 | M3′ B_wide / D (A1) |")
out.append("|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|")
pairs = [("GREIT", "GN"), ("GREIT", "BP"), ("GN", "GREIT"), ("GN", "BP"), ("BP", "GREIT"), ("BP", "GN")]
state = {"degenerate input": "degenerate (near-constant)", "over-range input": "over-range", "in-range input": "in range"}
for X, Y in pairs:
    r = R["R3"][f"R3-({X}->{Y})"]; c = C["R3_dod"][f"R3-({X}->{Y})"]; e = A11["E1"][f"E1-({X}->{Y})"]; ce = C["E1_dod"][f"E1-({X}->{Y})"]
    assert abs(r["dod"] - c["dod_mean"]) < 1e-12 and abs(e["dod_e1"] - ce["dod_mean"]) < 1e-12
    k3b = f"B_wide: mixed-ps->{Y.lower()} - {X.lower()}->{Y.lower()}"; k3d = k3b.replace("B_wide:", "D:")
    m3b, m3d = A11["M3p"][k3b], A11["M3p"][k3d]
    ab = R["sec_d_absolute_heart"][f"{X.lower()}__{Y.lower()}"]
    st = e["registered_cell_input"]
    st = next((v for k, v in state.items() if k in st), st)
    out.append(f"| {X} → {Y}{'¹' if 'BP' in (X, Y) else ''} | {st} | {ab['B_wide'][0]:.3f} / {ab['D'][0]:.3f} | {pts(r['delta_XY'], 2)} | {pts(r['dod'], 2)} | {ci(r['ci95'])} | {P(c['dod_sd']):.1f} | {c['mde_80pct_power_n30_points']:.1f} | {verdict(r['verdict'])} | {e['B_wide_e1'][0]:.3f} / {e['D_e1'][0]:.3f} | {pts(e['delta_XY_e1'], 2)} | {pts(e['dod_e1'], 2)} | {ci(e['ci95'])} | {ce['mde_80pct_power_n30_points']:.1f} | {pts(m3b['mean'], 1)} / {pts(m3d['mean'], 1)} |")
out.append("")
own = R["sec_c_own_affine"]
out.append("¹ BP raster offset, see Table 1. The registered secondary path (evaluation set's affine for input and output) is listed and not read, because it moves the output's background off zero (Section 3.2; a post-read decision, Section 2.5): DoD "
           + "; ".join(f"{k.replace('__', ' → ').upper()} {pts(v['dod_own_affine'], 2)} {ci(v['dod_own_affine_ci95'])}" for k, v in own.items() if "mixed" not in k) + ".")
out.append("")

# ---------------- Table 3
out.append("**Table 3. Leave-one-reconstructor-out rows (second addendum, hash 9589b298…).** Held-out cell loro-Y → Y: the network never saw Y. Every held-out loss in this table is an upper bound on the input-side generalisation loss, because the reference image moves with the reconstructor (Section 2.3). L1: B_wide on loro-Y → Y minus B_wide on mixed-ps → Y, paired by seed, 95% percentile bootstrap CI, margin ±1.0 point fixed before the runs (D beside, not tested). L2: Δ = D − B_wide on loro-Y → Y under the R1 rule; SD(Δ) = seed SD of the paired difference. L3′ (reported, not tested): loro-Y → Y minus Y → Y, and minus the two registered no-retraining cells X → Y (in-range cells only; the four cells crossing GREIT carry the degenerate/over-range note and are in S1 Table). In-pool comparison cells: the same rows evaluated on their two pool members (no hypothesis tested).")
out.append("")
out.append("| Held-out Y | B_wide Dice (mean ± SD) | D Dice (mean ± SD) | B_wide per-seed min–max | L1: B_wide loss vs mixed-ps (points) [95% CI] | L1 verdict | D loss (not tested) | L2: Δ (points) [95% CI] | SD(Δ) | Floor | dz | W | p | D > B_wide | L2 verdict | Lung Dice B_wide / D |")
out.append("|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|")
sds = {}
for Y in ["GREIT", "GN", "BP"]:
    y = Y.lower(); k1 = f"L1-(LORO-{Y}->{Y})"; k2 = f"L2-(LORO-{Y}->{Y})"; cell = f"loro_{y}__{y}"
    l1 = A12["L1"][k1]; l2 = A12["L2"][k2]; sr = A12["seed_range_heart"][cell]; lu = A12["L2_lung"][cell]
    sds[Y] = l2["B_wide_sd"]
    out.append(f"| {Y}{'¹' if Y == 'BP' else ''} | {l2['B_wide_mean']:.4f} ± {l2['B_wide_sd']:.4f} | {l2['D_mean']:.4f} ± {l2['D_sd']:.4f} | {sr['B_wide'][0]:.3f}–{sr['B_wide'][1]:.3f} | {l1['B_wide']['mean_points']:+.1f} {ci(l1['B_wide']['ci95'], 1)} | {verdict(l1['B_wide']['verdict'])} | {l1['D']['mean_points']:+.1f} {ci(l1['D']['ci95'], 1)} | {pts(l2['diff'], 1)} {ci(l2['diff_ci95'], 1)} | {P(l2['diff_sd']):.2f} | {P(l2['B_wide_sd']):.2f} | {l2['dz']:+.2f} | {l2['W']:.0f} | {pfmt(l2['p_wilcoxon'])} | {l2['D_gt_B_wide_seeds']}/30 | {verdict(l2['verdict'])} | {lu['B_wide_mean']:.3f} / {lu['D_mean']:.3f} |".replace("+-", "−").replace("| -", "| −"))
out.append("")
ref = A12["absolute_heart"]
inpool = [f"loro-{k.split('__')[0].split('_')[1].upper()} → {k.split('__')[1].upper()} {v['B_wide'][0]:.4f} / {v['D'][0]:.4f}" for k, v in ref.items() if "in-pool" in v["role"]]
out.append("¹ BP raster offset, see Table 1. The B_wide seed SD of the GREIT and BP held-out cells coincides at four decimals by chance "
           + f"({sds['GREIT']:.5f} and {sds['BP']:.5f} in the per-seed file). In-pool comparison cells (B_wide / D Dice): " + "; ".join(inpool) + ". "
           + "L3′ relative to specialised training (loro-Y → Y minus Y → Y), points [95% CI]: "
           + "; ".join(f"{lab(k)} {pts(v['mean'], 1)} {ci(v['ci95'], 1)}" for k, v in A12["L3p_vs_specialised"].items()) + ". "
           + "L3′ relative to the two in-range no-retraining cells: "
           + "; ".join(f"{lab(k)} {pts(v['mean'], 1)} {ci(v['ci95'], 1)}" for k, v in A12["L3p_vs_no_retraining"].items() if "in range" in v.get("registered_cell_input", "") or "in-range" in v.get("registered_cell_input", "")) + ".")
out.append("")

# ---------------- Table 4
sha = (ROOT / "PREREGISTRATION_RECON.sha256").read_text()
hashes = re.findall(r"^([0-9a-f]{64})\s+PREREGISTRATION_RECON\.md", sha, flags=re.M)
assert len(hashes) == 4, hashes
h = [x[:8] + "…" for x in hashes]
out.append("**Table 4. The four SHA-256 states of the preregistration file, what each governs and what had been read when each was written; and the two post-read reading decisions, which changed no hashed text and no verdict.** The hash of each state is written into the metadata of every training run it governs; the four full texts and the hash file are deposited with the minimal dataset (S1 Appendix). S3 Table quotes the rules and interpretation sentences verbatim.")
out.append("")
out.append("| State (date) | SHA-256 (prefix) | Governs | Written after reading | Fixed before the runs |")
out.append("|---|---|---|---|---|")
out.append(f"| Registered (2026-09-26) | {h[0]} | R1 (2 cells), R3 (6 cells), M1 (3 cells); rules, interpretations in both outcomes, n = 30, pilot | No cell of this study: no GN, BP or pooled arm existed and no contrast of this study had been computed. The companion study's GREIT networks (seeds 0–29, trained in the campaign of 2026-09-24 16:26 to 2026-09-26 00:44 and scored 2026-09-26, before hashing at 17:41) and their GREIT → GREIT result were known and are declared in the registered text as the reused reference row | All of the above |")
out.append(f"| Deviation record (2026-10-03) | {h[1]} | Two §10 entries (GN noise-figure band superseded by the realised-value matching rule; BP 2-px raster offset) | Pilot files only; no cell of the matrix | No hypothesis, endpoint, arm, setting, n or rule changed |")
out.append(f"| First addendum (2026-10-03) | {h[2]} | mixed-ps row: M1′ (3 cells, R1 rule), M2′, M3′ (reported), E1 (exploratory, no verdict) | All 12 registered cells and the 9 secondary-path cells | Row, scoring path, data gate, rule, expectation (3 falsifications, +0.27 to +0.63), readings of both outcomes |")
out.append(f"| Second addendum (2026-10-11) | {h[3]} | loro-GREIT, loro-GN, loro-BP: L1 (equivalence, ±1.0 point), L2 (R1 rule), L3′ and in-pool comparison cells (reported) | The first addendum's results (M1′, M2′, M3′, E1) and the first simulated review round | Rows, scoring path, data gate, margin and its reasons, rules, expectations (L1: 3 falsifications, 5–30 points; L2: 3 falsifications, −0.02 to +0.63), readings of both outcomes |")
out.append("| Post-read reading decisions (2026-10-03 and 2026-10-10; not hashed) | — | (a) the registered secondary scoring path (evaluation set's affine for input and output) is listed, not read, because it moves the output's background off zero; (b) the registered interpretation of a falsified M1 is quoted but not applied to the GN and BP cells, whose input was unreadable under the single pooled affine | The registered matrix (a); the registered matrix and the seed-0 input diagnosis (b) | Nothing: these are reading decisions on registered analyses, recorded in Section 2.5 and S2 Table; no verdict, rule or number changed |")
out.append("")

# ---------------- S2 Table (supporting information body)
hr = {k: SC[f"v2_full_snr20{'' if k == 'GREIT' else '_' + k.lower()}"] for k in ("GREIT", "GN", "BP")}
tr = C["training"]
out.append("## Supporting information tables")
out.append("")
out.append("**S2 Table. Forward model, reconstructor settings, pilot checks, deviations and post-read decisions, hashes, power and training records.** Every value is read from the generation scripts (`gen_dataset.m`, `gen_recon_full.m`, `p2_add_noise.m`), the preregistration file and the result files; none is typed from memory.")
out.append("")
out.append("| Item | Value |")
out.append("|---|---|")
out.append("| Forward model | EIDORS v3.8 with Netgen; cylinder of radius 2 and height 2 (model units), 16 electrodes of radius 0.1 in one ring at height 1 (`ng_mk_cyl_models([2,2,maxh],[16,1],[0.1])`), electrode contact impedance 0.01 (the `ng_mk_fwd_model` default; EIDORS assigns the value no unit); normalised difference data for all three reconstructors (`mdl_normalize`); tetrahedral forward mesh with maximum element size 0.10; adjacent drive and adjacent measurement with current-carrying electrodes excluded (`mk_stim_patterns(16,1,[0,1],[0,1],{'no_meas_current'},1)`), 208 measurements per frame |")
out.append("| Geometry | 3,600 geometries: background 1.0 S/m; two lung inclusions at 0.5 S/m with radius drawn from U(0.30, 0.60); one heart inclusion at 2.0 S/m with radius drawn independently from U(0.15, 0.30); inclusion centres jittered by ±0.05 around fixed positions; within-organ heterogeneity σ(x) = σ₀(1 + 0.25 f(x)), f the sum of 8 random sinusoids with correlation length 0.60; split 2,880 / 360 / 360 by geometry index, identical for all three reconstructors |")
out.append("| Noise | Additive white Gaussian noise on the 208 inhomogeneous-frame voltages only (homogeneous reference frame noise-free), scaled so that ‖vᵢ − vₕ‖ / ‖noise‖ = 10^(20/20) = 10 (an amplitude ratio; 20 dB), seed `noise_seed0 + i`, identical across reconstructors |")
out.append("| GREIT | `mk_GREIT_model` on a coarse cylinder (maximum element size 0.20): 64 × 64 image; 1,000 simulated training targets on the GREITv1 spiral (`distr` 0: radial position 0 to 0.9 of the mesh half-width in equal steps, angle 4321 × that fraction in radians, in the electrode plane, each of radius 0.05 of the mean half-width); desired image the EIDORS default sigmoid of radius 0.2 of the model radius (`GREIT_desired_img_sigmoid`, steepness 10/radius); noise figure 0.5 (nominal) calibrated on one central target of radius 0.02 of the model radius (`target_size`); realised noise figure on the common reference frame 0.602 |")
out.append("| One-step Gauss–Newton | `inv_solve_diff_GN_one_step` with `prior_laplace`, parametrised on GREIT's 64 × 64 reconstruction grid through `mk_coarse_fine_mapping` from the same coarse cylinder (no resampling onto the GREIT raster); hyperparameter 0.0016 set by bisection in log₁₀ so that the noise figure (0.607) matches GREIT's realised 0.602 on the common reference frame |")
out.append("| Back-projection | Sheffield MKI back-projection matrix (`mk_common_gridmdl('backproj')`), 32 × 32 raster, upsampled 2 × 2 by pixel replication (`kron(·, ones(2))`) and masked to GREIT's field of view; no free parameter; noise figure 0.831 on the common reference frame |")
out.append(f"| Heart-image amplitude relative to lung-image amplitude (training-split SD ratio of the single-organ reconstructions) | GREIT {hr['GREIT']['recon_heart']['sd']/hr['GREIT']['recon_lung']['sd']:.3f}; GN {hr['GN']['recon_heart']['sd']/hr['GN']['recon_lung']['sd']:.3f}; BP {hr['BP']['recon_heart']['sd']/hr['BP']['recon_lung']['sd']:.3f} |")
out.append(f"| Mixed-image amplitude (training-split SD) | GREIT {hr['GREIT']['recon_mixed']['sd']:.2f}; GN {hr['GN']['recon_mixed']['sd']:.4f}; BP {hr['BP']['recon_mixed']['sd']:.4f} (ratios {hr['GREIT']['recon_mixed']['sd']/hr['GN']['recon_mixed']['sd']:.0f} and {hr['GREIT']['recon_mixed']['sd']/hr['BP']['recon_mixed']['sd']:.0f}) |")
out.append("| Normalisation (\"affine\") | For each training row one location–scale standardisation estimated on that row's training split (subtract the mean, divide by the SD of all pixels of the mixed images), applied to inputs and targets; fixed, not learned; the pooled rows standardise each source with its own single-source affine before concatenation (per-source affine) |")
out.append("| Network | U-Net encoder 32-64-128-256 channels, 512-channel bottleneck, two 3 × 3 convolutions with batch normalisation and ReLU per level, 2 × 2 max-pooling; decoders with 2 × 2 transposed convolutions and skip concatenation; D: two decoders of the original width; B_wide: one decoder widened by 1.5312 (48, 96, 192, 392 channels fine to coarse) with two 1 × 1 output heads; " + f"parameters D {AR['D']['params']:,}, B_wide {AR['B_wide']['params']:,} |")
out.append("| Training | Adam 1 × 10⁻³ with cosine decay to 1 × 10⁻⁵, batch 16, ≤ 200 epochs, early stopping on validation loss (patience 20, best weights restored), L1 loss, unit loss weights, no augmentation, no output activation; seeds 0–29 per arm and row; Mac mini M4, Apple MPS backend, PyTorch 2.8.0 (seeds fix data order and initialisation; the backend does not guarantee bit-identical re-execution, so a seed defines a replicate, not an exactly reproducible run); the reused GREIT row comes from the companion study's 58-seed campaign of 2026-09-24 16:26 to 2026-09-26 00:44 (two parallel processes; per-run durations were logged, completion timestamps were not written to the run files) |")
out.append("| Power of the branch rule at n = 30 | Paired power at α 0.05 for dz 0.60 / 0.80 (the floor as a standardised effect in the diagonal cells) 0.89 / 0.99; for dz 0.40 (below the floor) 0.56; not intended to power a below-floor effect (preregistration §5) |")
out.append("| Pairing | Seed s against seed s in every contrast; for the held-out rows the two sides are separate trainings sharing initialisation and data order; with L1 effects 14 to 58 points outside the margin, paired or unpaired resampling changes no verdict |")
out.append("| Pilot checks (registered §6) | Heart quarter-amplitude coverage of the single-organ targets (mean) GREIT 0.068, GN 0.130, BP 0.105; noise figures GREIT 0.602, GN 0.607, BP 0.831; single-organ peak offset to GREIT: GN 1 px, BP 2 px (ten frames); GREIT replay of a 20 dB test frame reproduced to 2 × 10⁻¹⁴ |")
out.append("| Deviations (pre-read, 2026-10-03) | (1) §6(iii)'s acceptance band for GN's noise figure (0.5 ± 0.05) was superseded by §4's rule of matching GREIT's realised noise figure, a rule changed before hashing but not carried into §6; (2) BP's single-organ peak offset of 2 px exceeded §6(v)'s one-pixel tolerance; the automatic gate used 3 px and passed. Neither changed a hypothesis, endpoint, arm, setting, sample size or rule |")
out.append("| Post-read reading decisions (2026-10-03; 2026-10-10) | (3) the registered secondary scoring path (evaluation set's affine for input and output) is listed but not read: it moves the output's background off zero in image units and the quarter-amplitude mask fills the field; (4) the registered interpretation of a falsified M1, \"" + q("extending the matched-training null to a pooled training distribution") + "\", is not applied to the GN and BP cells, whose input under the single pooled affine was near-constant; the verdicts stand. Consequence of both: no verdict changed; one registered secondary quantity is unused; the registered M1 reading is replaced for those two cells by the design fact |")
out.append(f"| Preregistration states (SHA-256 prefixes) | registered {h[0]} (2026-09-26); deviation record {h[1]} (2026-10-03); first addendum {h[2]} (2026-10-03); second addendum {h[3]} (2026-10-11) |")
out.append("| Training records (epochs run, median [min–max]; minutes per run, median) | " + "; ".join(f"{row} {arm}: {v['epochs_run_median']:g} [{v['epochs_run_min']}–{v['epochs_run_max']}], {v['minutes_median']:.0f} min" for row, arms in tr.items() for arm, v in arms.items()) + " |")
out.append("")

# ---------------- S3 Table: verbatim rules and fixed interpretations
out.append("**S3 Table. The registered decision rule and both fixed interpretation sentences for every tested hypothesis, quoted verbatim from the hashed preregistration file (governing state in the first column).** Quotation marks in the Results sections refer to this table.")
out.append("")
out.append("| Hypothesis (state) | Decision rule (verbatim) | Fixed interpretation if confirmed (verbatim) | Fixed interpretation if falsified (verbatim) |")
out.append("|---|---|---|---|")
out.append("| R1-GN, R1-BP (registered 4b4c7a6d…) | \"" + q("mean DSC_heart(D) − DSC_heart(B_wide) exceeds B_wide's seed-to-seed SD under that condition **and** Wilcoxon signed-rank (two-sided, normal approximation with continuity correction) over paired seeds gives p < 0.05").replace("**", "") + "\"; falsified if \"" + q("either condition fails, or the sign is reversed") + "\" | \"" + q("the matched-training null of the core paper is GREIT-bounded; the branch pays off under matched training when the reconstructor passes enough of the measurement perturbation into the image") + "\" | \"" + q("the null extends across the three reconstructors the original study named") + "\" |")
out.append("| R3 (six cells; registered) | \"" + q("Δ(X→Y) − Δ(X→X) > 0 with a 95% percentile bootstrap CI over paired seeds (100,000 resamples) that excludes zero, where Δ is the paired D − B_wide heart-DSC difference") + "\"; falsified if \"" + q("the CI contains zero, or the difference is negative") + "\" | \"" + q("the branch's shift tolerance is not specific to noise amplitude; it transfers to a reconstructor change") + "\" | \"" + q("the tolerance seen in the noise sweep is specific to that kind of shift") + "\"; \"" + q("Cells are reported individually and never pooled; a mixed pattern is reported as mixed") + "\" |")
out.append("| M1 (three cells; registered) | \"" + q("the R1 rule applied to D − B_wide trained on the pooled split and evaluated on reconstructor Y. Confirmed if the difference exceeds B_wide's seed SD under that cell **and** p < 0.05; falsified otherwise").replace("**", "") + "\" | \"" + q("confirmed in a cell means the branch pays off when the training distribution spans reconstructors, i.e. the branch adds something on top of domain randomisation") + "\" | \"" + q("falsified means it does not, extending the matched-training null to a pooled training distribution") + "\" |")
out.append("| M1′ (three cells; first addendum 0060eedf…) | \"" + q("The R1 rule, unchanged: confirmed if mean DSC_heart(D) − DSC_heart(B_wide) exceeds B_wide's seed-to-seed SD in that cell **and** Wilcoxon signed-rank (two-sided, normal approximation with continuity correction) over the thirty paired seeds gives p < 0.05; falsified if either fails or the sign is reversed").replace("**", "") + "\" | \"" + q("the branch adds something on top of pooled training on that reconstructor. This would be a result from a post-unblinding addendum and is reported as such; it changes neither M1's record nor R1's, and the imaging paper may not lead with it") + "\" | \"" + q("under pooled, source-aware-normalised training the branch does not clear the floor on that reconstructor; the matched-training null extends to a training distribution that spans the three reconstructors") + "\" |")
out.append("| L1 (three cells; second addendum 9589b298…) | \"" + q("Quantity: DSC_heart(B_wide, loro-Y→Y) − DSC_heart(B_wide, mixed-ps→Y), paired by seed index (seed s against seed s, as M2 and M2′ were paired), 95% percentile bootstrap CI over the thirty pairs (100,000 resamples, seed 20260904). **Confirmed if the whole CI lies within [−1.0, +1.0] Dice points; falsified otherwise.**").replace("**", "") + "\" | \"" + q("pooled training with a per-source affine generalises, at the 1-point level and in this simulation, to that conventional reconstructor without ever seeing it") + "\" | \"" + q("the recipe stays in-pool only for that reconstructor, and the loss is reported as the cost of deploying on an unseen reconstructor") + "\" |")
out.append("| L2 (three cells; second addendum) | \"" + q("confirmed if mean DSC_heart(D) − DSC_heart(B_wide) on loro-Y→Y exceeds B_wide's seed-to-seed SD in that cell **and** Wilcoxon signed-rank (two-sided, normal approximation with continuity correction) over the thirty paired seeds gives p < 0.05; falsified if either fails or the sign is reversed").replace("**", "") + "\" | \"" + q("the branch adds something on an unseen reconstructor; a result from a second post-unblinding addendum, reported as such, changing neither R1, M1 nor M1′, and the imaging paper may not lead with it") + "\" | \"" + q("the matched-training null extends to a reconstructor the network never saw") + "\" |")
out.append("")
out.append("<!-- training records (RESULTS §10(c)): " + "; ".join(f"{row} {arm}: epochs median {v['epochs_run_median']}, minutes median {v['minutes_median']:.0f}" for row, arms in tr.items() for arm, v in arms.items()) + " -->")

sys.stdout.write("\n".join(out) + "\n")
