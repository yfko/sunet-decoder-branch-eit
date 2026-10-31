# -*- coding: utf-8 -*-
"""Revision patch 1.1 for the RECON tier-3 manuscript, round 1 (2026-10-31, Fable 5.1, academic-paper revision, patch mode).
Every op cites will_address roadmap items of revision-authority-round1/roadmap.json and stays inside their authorised
targets. Numbers in new text come from Tables 1-3 (generated from the result files) and the preregistration; the three
new table-derived figures (19 to 34 points; 0.3-point bound; heart/lung amplitude ratios) are checked by
tools/check_recon_draft_numbers.py after apply."""
import json, re, sys, subprocess
from pathlib import Path
PROJ = Path("/Users/yfko/Library/Mobile Documents/com~apple~CloudDocs/Documents/New idea/SunetBeta_the importance-of-divided-branch-structure")
S = Path.home() / ".claude/plugins/cache/academic-research-skills/academic-research-skills/3.23.0/scripts"
sys.path.insert(0, str(S.parent))
from scripts.revision_roadmap import bytes_hash, author_decision_digest  # noqa
ROOT = PROJ / "RECON_paper/manuscript/revision-authority-round1"
BASE = PROJ / "RECON_paper/manuscript/06_DRAFT_v1.md"; MAN = PROJ / "RECON_paper/manuscript/06_DRAFT_v1.md.block-manifest.json"
manifest = json.loads(MAN.read_text(encoding="utf-8")); H = {b["block_id"]: b["old_hash"] for b in manifest["blocks"]}
txt = BASE.read_text(encoding="utf-8"); parts = re.split(r"(<!--block:(B\d{4})-->\n)", txt); BLK = {}; i = 1
while i < len(parts): BLK[parts[i + 1]] = parts[i + 2].rstrip("\n"); i += 3

# regenerated tables (tools/recon_draft_tables.py, round-1 version)
tables = subprocess.run([sys.executable, str(PROJ / "tools/recon_draft_tables.py")], capture_output=True, text=True, check=True).stdout
T = [b.strip("\n") for b in re.split(r"\n\s*\n", tables.strip()) if b.strip()]
assert len(T) == 18, len(T)
TABLE_IDS = ["B0105", "B0106", "B0107", "B0108", "B0109", "B0110", "B0111", "B0112", "B0113", "B0114", "B0115", "B0116"]
for bid, t in zip(TABLE_IDS, T[:12]):
    assert BLK[bid].split("\n")[0][:12].strip("*| ")[:6] == t.split("\n")[0][:12].strip("*| ")[:6] or bid in ("B0108",), (bid, BLK[bid][:40], t[:40])

def sub(bid, old, new, count=1):
    t = NEW.get(bid, BLK[bid]); assert t.count(old) == count, (bid, old[:60], t.count(old)); NEW[bid] = t.replace(old, new)

NEW = {}
R = {  # roadmap items served by each op (filled below)
}

# ---------------- Abstract (REV-M1-1, -2, -4, -12, -18, -21, -22)
NEW["B0006"] = ("**Abstract** — Post-reconstruction networks for lung electrical impedance tomography (EIT) inherit the reconstructor they were trained on; whether a decoder branch for the weak cardiac component still helps under another conventional reconstructor was left open by the study that proposed it. "
 "We preregistered and hashed a parameter-matched comparison of a two-decoder network (D) against a widened single-decoder control (B_wide) on simulated 16-electrode lung EIT at 20 dB, reconstructed by GREIT, one-step Gauss–Newton and back-projection, scored by heart-channel Dice against each reconstructor's own heart image. "
 "Under matched training the branch stayed below the registered floor on Gauss–Newton and back-projection (+0.32 and +0.63 Dice points against floors of 0.45 and 0.66; registered), and the re-scored GREIT reference showed the same pattern. "
 "The registered transfer hypothesis for a reconstructor change without retraining was falsified in all six cells, with no evidence in the two in-range cells that the branch's advantage grew under the shift; exploratory re-scoring put the cost of not retraining at 19 to 34 points. "
 "The registered pooled row, trained under one global normalisation, collapsed on the two reconstructors whose amplitudes lie two orders of magnitude below the third's. In a post-unblinding, pre-hashed addendum with a per-source affine, pooled training was, descriptively, never worse than retraining on the deployed reconstructor by more than 0.3 points (−0.08 to +0.36; two of six intervals favoured pooling, confounded with threefold optimisation steps). "
 "In a second addendum, leaving one reconstructor out of the pool cost 62, 16 and 36 points on it against a pre-fixed margin of ±1.0 point (an upper bound, since the reference moves with the reconstructor), falsified in all three cells, and the branch's difference there reversed sign. "
 "The reconstructor behaves as a domain, on exploratory, descriptive and tested evidence respectively: the remedy for a reconstructor change lies in the training data, not in this branch, and the benefit of pooled training stops at the pool boundary for the three conventional reconstructors tested. Every tested verdict followed a rule fixed before its data were read.")
R["B0006"] = ["REV-M1-1", "REV-M1-2", "REV-M1-4", "REV-M1-12", "REV-M1-18", "REV-M1-21", "REV-M1-22"]

# ---------------- 1.1 Zhao wording (REV-M1-27)
sub("B0011", "gave five ventilation indices with no significant difference between them (Zhao et al., 2014)", "gave five ventilation indices with no statistically significant difference between algorithms, as that study reports it (Zhao et al., 2014)")
R["B0011"] = ["REV-M1-27"]

# ---------------- 1.4 contributions (REV-M1-1, -4, -11, -12, -43)
NEW["B0020"] = ("The paper contributes four things: registered, the branch stays below the registered floor under matched training on Gauss–Newton and back-projection, with the re-scored GREIT reference showing the same pattern and no evidence that the branch's advantage grows under a reconstructor change; from the first addendum, pooled training with a per-source affine was, descriptively, never worse than retraining on the deployed reconstructor by more than 0.3 points, and a global affine is a failure mode worth reporting; from the second, the pooled recipe does not generalise to a reconstructor outside the pool, tested and falsified at a pre-fixed margin, and the branch shows no measurable benefit there; and, methodologically, a preregistered study in which every one of twenty verdicts was a falsification, twelve of them in cells that posed their question, reported with its deviations and expectation hit rates.")
R["B0020"] = ["REV-M1-4", "REV-M1-11", "REV-M1-12", "REV-M1-43"]

# ---------------- 2.1 forward model / SNR / amplitude (REV-M1-19, -23)
sub("B0023", "on the registered 16-electrode cylinder with 3,600 geometries:", "on the registered 16-electrode cylinder (adjacent drive and adjacent measurement, 208 voltages per frame; mesh, electrode and geometry parameters in S2 Table) with 3,600 geometries:")
sub("B0023", "Gaussian measurement noise was added to the voltage frame before reconstruction at a signal-to-noise ratio (SNR) of 20 dB in the EIDORS convention, the ratio of the norm of the difference frame to the norm of the added noise.",
    "Gaussian measurement noise was added to the inhomogeneous voltage frame only, before reconstruction, at a signal-to-noise ratio (SNR) of 20 dB in the EIDORS convention: the norm of the difference frame divided by the norm of the added noise equals 10, an amplitude ratio. In the single-organ reconstructions the heart image's amplitude is 0.14, 0.085 and 0.099 of the lung image's (training-split SD ratio; GREIT, GN, BP), which is what makes the cardiac component weak for this simulation (S2 Table).")
R["B0023"] = ["REV-M1-19", "REV-M1-23"]

# ---------------- 2.1 reconstructors (REV-M1-19, -32)
NEW["B0024"] = ("The three reconstructors are those the original study named, each at one fixed setting; the settings are listed in S2 Table. GREIT, the Graz consensus reconstruction algorithm for EIT (Adler et al., 2009) <!--ref:Adler2009GREIT--><!--anchor:quote:GREIT%3A%20a%20unified%20approach%20to%202D%20linear%20EIT%20reconstruction%20of%20lung%20images-->, was built as registered on a 64 × 64 grid (nominal noise figure 0.5, realised 0.602 on a common reference frame). The noise figure (Adler and Guardo, 1996) <!--ref:Adler1996TMI--><!--anchor:quote:regularized%20imaging%20and%20contrast%20detection--> is the ratio of relative noise in the image to relative noise in the measurements, so matching it compares two regularised linear reconstructors at equal noise amplification on the same data. One-step Gauss–Newton (GN) with a Laplace prior was parametrised on GREIT's 64 × 64 grid, its hyperparameter set by bisection so that its noise figure matched GREIT's realised value (hp 0.0016, noise figure 0.607). Back-projection (BP) used the Sheffield back-projection matrix distributed with EIDORS (Adler and Lionheart, 2006) <!--ref:Adler2006EIDORS--><!--anchor:quote:an%20extensible%20software%20base%20for%20EIT-->, with no free parameter (noise figure 0.831); its 32 × 32 raster was upsampled two-fold by pixel replication and masked to GREIT's field of view. Because reconstruction settings strongly influence what a reconstructor produces (Thürk et al., 2019) <!--ref:Thurk2019PhysiolMeas--><!--anchor:quote:Influence%20of%20reconstruction%20settings-->, every result holds for these three operators at these settings.")
R["B0024"] = ["REV-M1-19", "REV-M1-32"]

# ---------------- 2.2 affine definition, determinism, GREIT-row provenance (REV-M1-31, -14, -20, -13)
sub("B0028", "and one dataset-wide normalisation affine estimated from that dataset's training split and applied to inputs and targets.",
    "and one dataset-wide normalisation affine, a fixed location–scale standardisation (subtract the training-split mean, divide by its SD) estimated on that dataset's training split and applied to inputs and targets, referred to below as that dataset's affine.")
sub("B0028", "Thirty seeds (0 to 29) per arm and training row were trained on one machine (Mac mini M4); seed-to-seed variability",
    "Thirty seeds (0 to 29) per arm and training row were trained on one machine (Mac mini M4, Apple MPS backend; a seed fixes data order and initialisation, but the backend does not guarantee bit-identical re-execution, so a seed defines a replicate rather than an exactly reproducible run); seed-to-seed variability")
sub("B0028", "The GREIT row reuses seeds 0 to 29 of the companion study's 20 dB training (same machine, same code).",
    "The GREIT row reuses seeds 0 to 29 of the companion study's 20 dB training (same machine and code; PyTorch 2.8.0), trained on 2026-09-24 and 25 and scored on 2026-09-26, before the registered state was hashed; the registered text declares this reuse and names that row as the reference against which the two R1 cells are read (Section 2.5), and a between-campaign difference is therefore confounded with every contrast that pairs a GREIT-trained network with one trained in this study (Section 3.4).")
R["B0028"] = ["REV-M1-31", "REV-M1-14", "REV-M1-20", "REV-M1-13"]

# ---------------- 2.3 Pulletz threshold wording (REV-M1-26); upper-bound assumption (REV-M1-15)
sub("B0030", "the region above one quarter of the image's peak, the threshold clinical region-of-interest methods apply to EIT images (Pulletz et al., 2006)",
    "the region above one quarter of the image's peak, a threshold of the kind clinical region-of-interest methods apply to EIT images (Pulletz et al., 2006)")
R["B0030"] = ["REV-M1-26"]
sub("B0031", "and is reported as an upper bound on the input-side generalisation loss, because the reference moves with the reconstructor. How much of a given loss is attributable to the reference style was not measured.",
    "and is reported as an upper bound on the input-side generalisation loss, because the reference moves with the reconstructor. The bound rests on an assumption this study did not test: that scoring a network's output against a reference style it was not trained towards can only lower Dice relative to the held-out reconstructor's own heart image. How much of a given loss is attributable to the reference style was not measured.")
R["B0031"] = ["REV-M1-15"]

# ---------------- 2.5 registered-state wording, deviation record (REV-M1-20, -9, -36)
NEW["B0036"] = ("Table 4 gives the four SHA-256 states of the preregistration file, what each governs, and what had been read when each was written; S3 Table quotes every decision rule and fixed interpretation sentence verbatim. The registered state (2026-09-26) fixed R1, R3 and M1 with their rules, interpretations in both outcomes, n = 30 and the pilot before any arm of this study was trained; the companion study's GREIT networks, whose reuse the registered text declares, already existed (Section 2.2). Two deviations were recorded on 2026-10-03 before any cell was read: the pilot's acceptance band for GN's noise figure predated the change of matching rule from GREIT's nominal to its realised value, and BP's single-organ peaks were offset from GREIT's by up to 2 pixels against a registered tolerance of one pixel (2 pixels is one pixel of BP's native grid). No hypothesis, endpoint, arm, setting, sample size or rule changed; BP was analysed as registered, with the offset noted beside every BP cell. Two further decisions were taken after cells had been read and are recorded in Table 4 and S2 Table with their timing and consequence: the registered secondary scoring path is listed but not read, because it moves the output's background off zero (Section 3.2), and the registered interpretation of a falsified M1 is quoted but not applied to the two cells whose input was unreadable (Section 3.3). Neither changes a verdict.")
R["B0036"] = ["REV-M1-20", "REV-M1-9", "REV-M1-36"]

# ---------------- 2.6 statistics (REV-M1-8, -10)
sub("B0039", "The floor is the registered smallest effect of interest; n = 30 gives at least 0.89 power for a floor-sized effect at diagonal-cell variability and deliberately does not power a below-floor effect.",
    "The floor is the registered smallest effect of interest; n = 30 gives 0.89 power for a floor-sized effect at diagonal-cell variability (dz 0.60, paired, α 0.05; S2 Table) and deliberately does not power a below-floor effect. The rules and both fixed interpretation sentences of every hypothesis are quoted verbatim in S3 Table and are applied as written.")
sub("B0039", "Pairing by seed follows the registered rule; with effects 14 to 58 points outside the margin, paired or unpaired resampling affects no verdict.",
    "Pairing by seed follows the registered rule (S2 Table).")
R["B0039"] = ["REV-M1-8"]
sub("B0040", "the Wilcoxon statistic W, and exact p values at or above 0.001 (intervals are rarely reported in segmentation studies; Christodoulou et al., 2024)",
    "the Wilcoxon statistic W, and p values from the normal approximation with continuity correction to two significant figures (intervals are rarely reported in segmentation studies; Christodoulou et al., 2024)")
sub("B0040", "For the R3 and E1 cells the achieved sensitivity (the difference of differences detectable with 80% power at n = 30 from that cell's observed seed SD) is reported, because the registered power table assumed diagonal-cell variability.",
    "For the R3 and E1 cells the achieved sensitivity (the difference of differences detectable with 80% power at n = 30 from that cell's observed seed SD) is reported in Table 2, because the registered power table assumed diagonal-cell variability; the paired-difference SD of every tested cell is in Tables 1 and 3 and the lung channel of every cell in S1 Table.")
R["B0040"] = ["REV-M1-10"]

# ---------------- 2.7 placeholders wording (REV-M1-6)
sub("B0042", "[MATERIAL GAP: Zenodo DOI, to be minted at submission]", "[MATERIAL GAP: Zenodo DOI, minted at submission; the deposit is prepared]")
R["B0042"] = ["REV-M1-6"]

# ---------------- 3.1 heading and text (REV-M1-1, -8)
NEW["B0045"] = "### 3.1 Under matched training, the branch stays below the registered floor on Gauss–Newton and back-projection, and the GREIT reference shows the same pattern"
R["B0045"] = ["REV-M1-1"]
NEW["B0046"] = ("Table 1 gives the matched cells. On GN the paired difference D minus B_wide was +0.323 points (95% CI +0.183 to +0.470; p 0.00015) against a floor of 0.449; on BP it was +0.631 (CI +0.399 to +0.885; p 3 × 10⁻⁵) against a floor of 0.664. Both p values pass and neither difference exceeds its floor, so R1-GN and R1-BP are falsified, and the registered reading applies as written: \"the null extends across the three reconstructors the original study named\" (S3 Table). The GREIT → GREIT cell is the registered reference, re-scored from the companion study's networks and tested by no hypothesis; it shows the same pattern (+0.271 against a floor of 0.343; Table 1). In the first addendum the mixed-ps row gave −0.015 (floor 0.173, p 0.64) on GREIT, +0.201 (floor 0.248, p 0.00086) on GN and +0.404 (floor 0.531, p 0.0048) on BP: M1′ falsified in all three, by sign reversal on GREIT and by the floor on GN and BP (expectation met on 3 of 3 verdicts and 1 of 3 magnitudes). Its fixed reading, verbatim: \"under pooled, source-aware-normalised training the branch does not clear the floor on that reconstructor; the matched-training null extends to a training distribution that spans the three reconstructors\" (S3 Table).")
R["B0046"] = ["REV-M1-8"]

# ---------------- 3.2 fixed reading quoted (REV-M1-8); 19 to 34 (REV-M1-22)
sub("B0049", "The fixed reading is that whatever shift tolerance the branch has is specific to the kind of shift.",
    "The fixed reading for a falsified cell is, verbatim, \"the tolerance seen in the noise sweep is specific to that kind of shift\" (S3 Table); the noise sweep it names is the companion study's, whose result this paper does not use.")
R["B0049"] = ["REV-M1-8"]
sub("B0051", "Under it both arms lost about 19 to 33 points relative to their diagonals in every cell (Table 2)", "Under it both arms lost 19 to 34 points relative to their diagonals in every cell (Table 2)")
sub("B0051", "a reconstructor change without retraining costs about 19 to 33 heart-Dice points even after scale correction", "a reconstructor change without retraining costs 19 to 34 heart-Dice points even after scale correction")
R["B0051"] = ["REV-M1-22"]

# ---------------- 3.3 M1 interpretation quoted and the asymmetry explained (REV-M1-8, -9, -36)
sub("B0053", "Whether the registered row posed its intended question is a design matter: on GN and BP the networks were shown an input they could not read, so those two cells are not evidence about pooled training, and the registered interpretation of a falsified M1 is not applied to them.",
    "Whether the registered row posed its intended question is a design matter: on GN and BP the networks were shown an input they could not read, so those two cells are not evidence about pooled training. The registered interpretation of a falsified M1, \"extending the matched-training null to a pooled training distribution\" (S3 Table), is therefore quoted but not applied to them, a decision taken after the cells were read and recorded in Section 2.5. The asymmetry with Section 3.2 is deliberate: the registered R3 reading describes what was observed in a cell and is applied to all six, with the input-state note beside it, whereas the registered M1 reading asserts an extension to pooled training that these two cells could not test.")
R["B0053"] = ["REV-M1-8", "REV-M1-9", "REV-M1-36"]

# ---------------- 3.4 heading, text, qualifications (REV-M1-12, -13, -16)
NEW["B0055"] = "### 3.4 Pooled training with a per-source affine was never worse than retraining on the deployed reconstructor by more than 0.3 points (reported, not tested)"
R["B0055"] = ["REV-M1-12"]
NEW["B0056"] = "M2′ (first addendum; reported, not tested; descriptive) is the paired difference between the mixed-ps row and the matched row on the same reconstructor (Table 1). The six point estimates run from −0.083 to +0.360 points and no interval extends below −0.32 points: pooled training was never worse than retraining by more than 0.3 points in any cell, and two of the six intervals, both for the control arm on GREIT and GN, lie above zero."
R["B0056"] = ["REV-M1-12"]
sub("B0057", "And the normalisation is source-aware. M3′, the share of the no-retraining loss that pooling removed, is in Table 2 (+34.7/+44.8 points for GN→BP and +15.1/+11.7 for BP→GN in the two in-range cells; the four cells crossing GREIT carry the degenerate or over-range note).",
    "And the normalisation is source-aware. For the GREIT cell of M2′ and for every contrast that pairs a GREIT-trained network with one trained in this study, the GREIT networks come from the companion study's campaign (Section 2.2), so a between-campaign difference is confounded with the contrast. M3′, the share of the registered-path no-retraining loss that pooling removed, is in Table 2 in points (+34.7/+44.8 for GN→BP and +15.1/+11.7 for BP→GN in the two in-range cells; the four cells crossing GREIT carry the degenerate or over-range note).")
R["B0057"] = ["REV-M1-13", "REV-M1-16"]

# ---------------- 3.5 heading, fixed reading, conditional mechanism (REV-M1-29, -8, -42, -33)
NEW["B0058"] = "### 3.5 Pooled training does not generalise to a reconstructor outside the pool: losses of 62, 16 and 36 points, upper bounds on the input-side loss"
R["B0058"] = ["REV-M1-29"]
sub("B0059", "The fixed reading applies to each reconstructor in turn: the recipe stays in-pool only for that reconstructor, and the loss is reported as the cost of deploying on an unseen reconstructor.",
    "The fixed reading applies to each reconstructor in turn, verbatim: \"the recipe stays in-pool only for that reconstructor, and the loss is reported as the cost of deploying on an unseen reconstructor\" (S3 Table).")
sub("B0059", "The six in-pool reference cells of the same rows scored 0.957 to 0.967, the level of the diagonals, so the two-source pools were not deficient: the networks failed only on the source they had not seen. The loss order, GN smallest and GREIT largest, is the two-source pool's coverage of the held-out reconstructor, not a ranking of reconstructors.",
    "The six in-pool reference cells of the same rows scored 0.957 to 0.967, the level of the diagonals, so the two-source pools were not deficient: the networks failed only on the source they had not seen. The loss order, GN smallest and GREIT largest, would follow if the loss reflects how well the two-source pool covers the held-out reconstructor; that mechanism was not tested, and the order is not a ranking of reconstructors.")
R["B0059"] = ["REV-M1-8", "REV-M1-42"]

# ---------------- 3.6 heading and text (REV-M1-4, -8)
NEW["B0062"] = "### 3.6 On an unseen reconstructor the branch shows no measurable benefit: its difference reverses sign"
R["B0062"] = ["REV-M1-4"]
sub("B0063", "falsified in all three by sign reversal, and the fixed reading is that the matched-training null extends to a reconstructor the network never saw.",
    "falsified in all three by sign reversal, and the fixed reading applies verbatim: \"the matched-training null extends to a reconstructor the network never saw\" (S3 Table).")
sub("B0063", "and in the GN cell (CI −5.3 to −2.4; p 0.00012; D above B_wide on 4 of 30 seeds).",
    "and in the GN cell, whose negative difference (−3.9 points, CI −5.3 to −2.4; p 0.00012; D above B_wide on 4 of 30 seeds) is described, not tested.")
R["B0063"] = ["REV-M1-4", "REV-M1-8"]

# ---------------- 4.1 (REV-M1-2, -3, -4, -18, -22, -28)
NEW["B0066"] = ("All three signs named in Section 1.1 appeared, on evidence of three standings. Without retraining, a change of reconstructor cost both arms 19 to 34 heart-Dice points even after scale correction (exploratory), and the registered transfer hypothesis was falsified in every cell (registered). With the deployed reconstructor's images in the training pool, pooled training with a per-source affine was never worse than retraining on that reconstructor by more than 0.3 points (first addendum; descriptive). With the deployed reconstructor outside the pool, the same recipe lost 16 to 62 points (an upper bound, Section 2.3), falsified against a margin fixed in advance (second addendum; tested). Fig 5 arranges the remedies tested. Only putting the target reconstructor's images into training recovered the loss; the two ways of doing so differed by −0.08 to +0.36 points with two of six intervals favouring pooling, a difference this design cannot separate from threefold optimisation steps.")
R["B0066"] = ["REV-M1-2", "REV-M1-3", "REV-M1-18", "REV-M1-22"]
sub("B0067", "Two sources pooled gave no evidence of helping on a third, so within this study the benefit of pooling is one of inclusion, not of diversity. And the one architectural remedy tested, the branch, had no measurable effect at any of the three layers.",
    "Two sources pooled gave no evidence of helping on a third, so the benefit demonstrated here is one of inclusion; whether source diversity adds anything was not resolved (Section 4.4). And the one architectural remedy tested, the branch, showed no measurable benefit at any of the three layers: below the registered floor in-pool, sign reversed out of pool.")
R["B0067"] = ["REV-M1-4", "REV-M1-28"]

# ---------------- 4.2 (REV-M1-22)
sub("B0070", "its 0.96 is an addendum value and its no-retraining cost of 19 to 33 points is exploratory", "its 0.96 is an addendum value and its no-retraining cost of 19 to 34 points is exploratory")
R["B0070"] = ["REV-M1-22"]

# ---------------- 4.3 MRI sentence (REV-M1-24)
sub("B0072", "Where sources are already on comparable scales, as in multi-centre magnetic resonance imaging (MRI), the choice among normalisation methods changes Dice by less than 0.02 (Albert et al., 2023)",
    "Where source differences are modest, as among multi-centre magnetic resonance imaging (MRI) scanners whose unitless intensities differ by far less than two orders of magnitude, the choice among normalisation methods changes Dice by less than 0.02 (Albert et al., 2023)")
R["B0072"] = ["REV-M1-24"]

# ---------------- 4.5 counts and defence (REV-M1-11, -38)
sub("B0077", "Of twenty verdict cells, twenty were falsified.", "Of twenty verdict cells, twenty were falsified; twelve posed the question they were designed for, and eight (four R3 cells with unreadable input, two M1 cells with unreadable input, and the two held-out L2 cells whose floors were 9.5 points) were falsified in cells the design did not succeed in posing or could hardly have confirmed (Sections 3.2, 3.3 and 3.6).")
R["B0077"] = ["REV-M1-11"]
sub("B0078", "Both addenda went against the authors' own recipe: the first left the branch below the floor, and the second turned the pooled recipe from \"generalises\" into \"in-pool only\". And the second addendum's rows were those a simulated review round, recorded in the repository before the addendum was written, had asked for.",
    "Both addenda were written to test outcomes unfavourable to the authors' own recipe, and found them: the first left the branch below the floor, and the second denied the pooled recipe any generalisation beyond the pool at the pre-fixed margin. The expectations written before those runs anticipated the falsifications, so the results met the authors' stated expectations rather than surprising them, and in two of the three L1 cells the loss exceeded the expected range. And the second addendum's rows were those a simulated review round, recorded in the repository before the addendum was written, had asked for.")
R["B0078"] = ["REV-M1-38"]

# ---------------- 4.7 deployment identity (REV-M1-34)
sub("B0083", "and \"the same reconstructor\" should be defined as algorithm, implementation and hyperparameters together.",
    "and \"the same reconstructor\" should be defined as algorithm, implementation and hyperparameters together. The per-source affine requires the reconstructor's identity at deployment, a domain label at test time (Karani et al., 2018) <!--ref:Karani2018MICCAI--><!--anchor:quote:Across%20Scanners%20and%20Protocols-->; in the EIT systems such a study targets the reconstructor is a configured setting and therefore known, but whether that setting is exposed to downstream software must be confirmed for each system.")
R["B0083"] = ["REV-M1-34"]

# ---------------- Conclusion (REV-M1-1, -2, -3, -4, -5, -12)
NEW["B0085"] = ("The question the original study left open has an answer for the three conventional reconstructors it named, in simulation at 20 dB. Under matched training the branch stayed below the registered floor on Gauss–Newton and back-projection (registered), and the re-scored GREIT reference showed the same pattern; without retraining, its advantage showed no evidence of growing under the shift (registered); in pooled training it stayed below the floor (first addendum); and on a reconstructor the network had never seen its difference reversed sign (second addendum). The cost of a reconstructor change was recovered by putting that reconstructor's images into training, by retraining or by pooling with a per-source affine; the two differed by −0.08 to +0.36 points, with two of six intervals favouring pooling (first addendum; reported, not tested), and nothing else that was tested recovered it. The benefit of pooling stops at the pool boundary: leaving one reconstructor out cost 62, 16 and 36 points on GREIT, Gauss–Newton and back-projection against a margin of ±1.0 point fixed before the runs (second addendum; tested), an upper bound on the input-side loss because the reference moves with the reconstructor, so the in-pool restriction of the recipe is a tested and falsified generalisation claim, not an assumption. Every tested verdict followed a rule written and hashed before the data it judged were read; the descriptive quantities carry no verdict. Learned harmonisation, wider randomisation and measured data lie outside this study and are where the next tests belong.")
R["B0085"] = ["REV-M1-1", "REV-M1-2", "REV-M1-3", "REV-M1-5", "REV-M1-12"]

# ---------------- Related manuscript (REV-M1-6)
sub("B0089", "[MATERIAL GAP: preprint DOI, to be inserted when the companion study is posted as a preprint; until then it is not cited.]",
    "[MATERIAL GAP: preprint DOI, to be inserted when the companion study is posted as a preprint; until then it is not cited and the accompanying copy is the reference.]")
R["B0089"] = ["REV-M1-6"]

# ---------------- Supporting information captions (REV-M1-10, -19, -9, -8)
NEW["B0094"] = "**S1 Table.** Per-seed heart- and lung-channel Dice for every cell of the design (three matched, six no-retraining, two pooled, three held-out rows with their in-pool comparison cells), the registered-path absolute Dice of the six no-retraining cells, the lung-channel Dice of every cell, and the registered secondary-path values, E1, M3′ and L3′ in full."
R["B0094"] = ["REV-M1-10"]
NEW["B0095"] = "**S2 Table.** Forward model, reconstructor settings, normalisation, network and training constants, power, pairing, pilot checks, the two pre-read deviations and the two post-read reading decisions, the four preregistration hashes and the training records (body after Table 4)."
R["B0095"] = ["REV-M1-19", "REV-M1-9"]
INS_B0097 = "**S3 Table.** The registered decision rule and both fixed interpretation sentences of every tested hypothesis (R1, R3, M1, M1′, L1, L2), quoted verbatim from the hashed preregistration file with the governing hash state (body after Table 4)."
INS_B0089 = ("## Data availability\n\nThe minimal dataset (per-seed Dice for every cell, the aggregated results file, gate and seed-0 diagnostic files) and the four preregistration states with their hash file are deposited on Zenodo [MATERIAL GAP: Zenodo DOI, minted at submission]; the data-generation, training, scoring and figure code is in the project repository under a tagged release [MATERIAL GAP: repository tag for this paper]. Model checkpoints are available from the corresponding author.\n\n"
             "## Ethics statement\n\nThe study used simulated data only; no human participants, animals or patient data were involved, and no ethics approval was required.\n\n"
             "## Funding and competing interests\n\nThe journal collects funding and competing-interest statements in its submission system rather than in the manuscript file; the corresponding author's authorship of the semi-Siamese architecture evaluated here (Section 4.6) is declared there.")

# ---------------- tables (REV-M1-1, -2, -9, -10, -16, -17, -20, -29, -33) and supplementary bodies (REV-M1-8, -19, -23)
for bid, t in zip(TABLE_IDS, T[:12]):
    NEW[bid] = t
R["B0105"] = ["REV-M1-1"]; R["B0106"] = ["REV-M1-1", "REV-M1-10"]; R["B0107"] = ["REV-M1-1", "REV-M1-10"]; R["B0108"] = ["REV-M1-2", "REV-M1-10"]
R["B0109"] = ["REV-M1-16"]; R["B0110"] = ["REV-M1-10", "REV-M1-16"]; R["B0111"] = ["REV-M1-10"]; R["B0112"] = ["REV-M1-29"]
R["B0113"] = ["REV-M1-10"]; R["B0114"] = ["REV-M1-10", "REV-M1-17"]; R["B0115"] = ["REV-M1-10"]; R["B0116"] = ["REV-M1-9", "REV-M1-20"]
INS_B0116 = "\n\n".join(T[12:17])
assert T[17] == BLK["B0117"]  # training-records comment unchanged

# one op per block: the inserted statements and supplementary bodies ride on the replaced block they follow
NEW["B0089"] = NEW["B0089"] + "\n\n" + INS_B0089; R["B0089"] = R["B0089"] + ["REV-M1-7"]
NEW["B0116"] = NEW["B0116"] + "\n\n" + INS_B0116; R["B0116"] = R["B0116"] + ["REV-M1-8", "REV-M1-19", "REV-M1-23"]
COLL = {"B0059": "REV-M1-33", "B0114": "REV-M1-33", "B0105": "REV-M1-33", "B0106": "REV-M1-33", "B0046": "REV-M1-33", "B0024": "REV-M1-25", "B0049": "REV-M1-30", "B0078": "REV-M1-35", "B0031": "REV-M1-37", "B0036": "REV-M1-40"}
ops = []
for bid, new in NEW.items():
    assert new != BLK[bid], bid
    ops.append({"op": "replace_block", "block_id": bid, "old_hash": H[bid], "new_text": new, "roadmap_item_ids": R[bid], "claim_strength_changes": [], "collateral_authorization_ids": ([f"COLLATERAL-AUTH-round1-{bid}-{COLL[bid]}"] if bid in COLL else [])})
ops.append({"op": "insert_after", "block_id": "B0097", "old_hash": H["B0097"], "new_text": INS_B0097, "roadmap_item_ids": ["REV-M1-8"], "claim_strength_changes": [], "collateral_authorization_ids": []})
ops.sort(key=lambda o: (o["block_id"], 0 if o["op"] == "replace_block" else 1))

rm_raw = (ROOT / "roadmap.json").read_bytes(); adj_raw = (ROOT / "author-adjudication.json").read_bytes(); cs_raw = (ROOT / "claim-surface-manifest.json").read_bytes()
patch = {"patch_format_version": "1.1", "authorization_context": "review_roadmap", "revision_round": 1, "base_draft_hash": manifest["base_draft_hash"],
         "roadmap_sha256": bytes_hash(rm_raw), "author_adjudication_sha256": bytes_hash(adj_raw), "author_decision_digest": author_decision_digest(json.loads(adj_raw)),
         "claim_surface_manifest_sha256": bytes_hash(cs_raw), "ops": ops,
         "emitted_by": "draft_writer_agent (academic-paper revision round 1, patch mode, Fable 5.1, 2026-10-31)"}
(ROOT / "revision_patch_round1.json").write_text(json.dumps(patch, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
print(len(ops), "ops;", sum(1 for o in ops if o["op"] == "insert_after"), "inserts")
