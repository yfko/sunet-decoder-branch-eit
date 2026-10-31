# -*- coding: utf-8 -*-
import json, pathlib
P = pathlib.Path("/Users/yfko/Library/Mobile Documents/com~apple~CloudDocs/Documents/New idea/SunetBeta_the importance-of-divided-branch-structure")
rm = json.load(open(P/"RECON_paper/manuscript/revision-authority-round1/roadmap.json"))
adj = {a["item_id"]: a for a in json.load(open(P/"RECON_paper/manuscript/revision-authority-round1/author-adjudication.json"))["author_adjudications"]}
patch = json.load(open(P/"RECON_paper/manuscript/revision-authority-round1/revision_patch_round1.json"))
touched = {}
for op in patch["ops"]:
    for i in op["roadmap_item_ids"]: touched.setdefault(i, []).append(op["block_id"])
RESP = {
 "REV-M1-1": "Reference kept as reference: Table 1 verdict column now a dash with the legend 'reference cell re-scored from the companion study's networks, no hypothesis tested'; Abstract, heading 3.1, 3.1 text, contribution list and Conclusion say the two registered cells were falsified and the re-scored GREIT reference showed the same pattern.",
 "REV-M1-2": "Every number-carrying clause of the Conclusion and 4.1 now names its standing; the Abstract's pooled-training sentence is labelled descriptive; the closing sentence reads 'Every tested verdict followed a rule …; the descriptive quantities carry no verdict'.",
 "REV-M1-3": "'could not be separated at 0.4 points' removed from 4.1 and the Conclusion; replaced by the M2′ range −0.08 to +0.36 points, two of six intervals favouring pooling, confounded with threefold steps.",
 "REV-M1-4": "'adds nothing measurable' / 'no measurable effect' replaced by 'no measurable benefit', 'below the registered floor', 'sign reversed' (heading 3.6, Abstract, 4.1, contribution list); the GN held-out deficit is described, not tested (3.6).",
 "REV-M1-5": "Conclusion opening rewritten in the registered vocabulary, one standing per clause; matched-training cells no longer bundled under 'a change of reconstructor'.",
 "REV-M1-6": "Related-manuscript statement says the accompanying copy is the reference until the preprint DOI exists; Zenodo DOI and repository tag remain placeholders by nature (minted at submission) and are listed in the hand-off.",
 "REV-M1-7": "Data availability and Ethics statement added as separate sections after the related-manuscript statement; Funding and Competing interests: PLoS One instructs that these go in the submission system, not the manuscript file (refs/01 R2 record), so a pointer section says where they are declared. Partially addressed by venue rule.",
 "REV-M1-8": "New S3 Table quotes, verbatim and asserted at render time against the hashed file, the rule and both interpretation sentences of R1, R3, M1, M1′, L1 and L2; every fixed reading in 3.1–3.6 is now a quotation marked (S3 Table); 2.6 points to it.",
 "REV-M1-9": "Both post-read decisions added to 2.5, to Table 4 (new row) and to S2 Table with timing, rationale and consequence; the registered M1 interpretation is quoted in 3.3 and S2 Table with the reason it is not applied.",
 "REV-M1-10": "SD(Δ) column added to Tables 1 and 3; MDE80 for the six E1 cells added to Table 2; lung-channel Dice of every cell placed in S1 Table (caption); 2.6 now states 'normal approximation with continuity correction to two significant figures'.",
 "REV-M1-11": "4.5 and the contribution list state twelve informative verdict cells and eight (four R3, two M1, two L2) falsified in cells the design did not succeed in posing or could hardly have confirmed.",
 "REV-M1-12": "'never worse' everywhere bounded: 'never worse than retraining by more than 0.3 points in any cell' (interval lower bound −0.32), with the −0.08 to +0.36 range and the descriptive/first-addendum label (Abstract, contribution list, heading 3.4, 3.4, Conclusion).",
 "REV-M1-13": "Two-campaign confound stated in 2.2 and in 3.4's qualifications; GREIT campaign dates and PyTorch version given; retraining not done (not required).",
 "REV-M1-14": "2.2 and S2 Table state that the MPS backend does not guarantee bit-identical re-execution, so a seed defines a replicate; a one-seed re-run was not performed in this round (open for the PI).",
 "REV-M1-15": "2.3 now states the assumption under which the held-out loss is an upper bound and that it was not tested.",
 "REV-M1-16": "Table 2 caption defines M3′ as Dice(mixed-ps → Y) − Dice(X → Y) in points against the registered-path cell; the registered-path absolute Dice of the six no-retraining cells is now a Table 2 column; 3.4 says 'registered-path'.",
 "REV-M1-17": "Verified in the per-seed-derived result file: 0.09489 (GREIT) and 0.09490 (BP); coincidence at four decimals; stated in the Table 3 footnote.",
 "REV-M1-18": "Abstract and 4.1 first sentence state that the three signs rest on exploratory, descriptive and tested evidence respectively.",
 "REV-M1-19": "2.1 states the stimulation pattern, 208 voltages, the linear SNR definition (amplitude ratio 10, inhomogeneous frame only) and points to S2 Table, whose body now lists mesh, electrodes, contact impedance, geometry ranges, heterogeneity, GREIT training targets, GN parametrisation, BP interpolation.",
 "REV-M1-20": "The companion GREIT networks were trained 2026-09-24/25 and scored 2026-09-26, before the registered state (2026-09-26 17:41) was hashed; the registered text (§5) declares the reuse. 2.2, 2.5 and Table 4's 'Written after reading' cell now say so exactly; no deviation, because the reuse is in the registered text.",
 "REV-M1-21": "Abstract now attributes the collapse to the registered pooled row and the per-source re-run to the addendum.",
 "REV-M1-22": "'19 to 33' → '19 to 34' in the Abstract, 3.2, 4.1 and 4.2 (D on GN → BP under E1: 0.9672 − 0.629 = 33.8); '14 to 58' kept (13.9 and 57.5 round half-up to 14 and 58).",
 "REV-M1-23": "Heart/lung amplitude ratio of the single-organ reconstructions (training-split SD ratio: GREIT 0.143, GN 0.085, BP 0.099) computed from results_recon/scale_check.json and stated in 2.1 and S2 Table.",
 "REV-M1-24": "4.3 rephrased: MRI intensities are unitless and differ far less than two orders of magnitude.",
 "REV-M1-25": "Consider item, not implemented: Barber and Brown is not in the verified corpus; adding it requires the R12d pipeline (Crossref) and PI approval of a new entry.",
 "REV-M1-26": "Wording hedged to 'a threshold of the kind clinical ROI methods apply'; the 25% value is the registered endpoint; the exact Pulletz threshold is to be verified by the PI against the paper (open).",
 "REV-M1-27": "Wording now attributes the no-significant-difference statement to the study ('as that study reports it'); the per-index check against Zhao 2014 is to be done by the PI (open).",
 "REV-M1-28": "4.1 reconciled: 'the benefit demonstrated here is one of inclusion; whether source diversity adds anything was not resolved (Section 4.4)'.",
 "REV-M1-29": "Heading 3.5 carries 'upper bounds on the input-side loss'; Table 3 caption carries the clause for every held-out loss.",
 "REV-M1-30": "Consider item, not implemented (PI to decide whether a neutral clause about kinds of shift is added beside the fixed R3 sentence); 3.2 already says the noise sweep named in the fixed sentence is the companion study's.",
 "REV-M1-31": "'affine' defined at first use in 2.2 as a fixed location–scale standardisation; S2 Table repeats it.",
 "REV-M1-32": "2.1 defines the noise figure and why matching it makes two regularised reconstructors comparable.",
 "REV-M1-33": "Consider item, not implemented: 'reference' is kept for both the target image and the in-pool reference cells pending the PI's choice of term (interacts with REV-M1-1, resolved as 'reference, no verdict').",
 "REV-M1-34": "4.7 states that the per-source affine needs the reconstructor identity at deployment (Karani 2018) and that in the targeted EIT systems it is a configured setting whose exposure to downstream software must be confirmed.",
 "REV-M1-35": "Consider item, not implemented: the Acknowledgments already describe the simulated review panels; a forward pointer in 4.5 is left to the PI.",
 "REV-M1-36": "3.3 explains the asymmetry: the R3 reading describes what was observed per cell and is applied to all six with the input-state note; the M1 reading asserts an extension to pooled training the two cells could not test; recorded as a post-read decision in 2.5.",
 "REV-M1-37": "Consider item (DA position): the upper-bound qualification is kept, as R2, R3 and EIC regard it as correct; the assumption it rests on is now stated (REV-M1-15). Response for the letter: the bound is the honest direction given the task definition; a reconstructor-independent reference does not exist for this endpoint, which is why the attribution is reported as unmeasured.",
 "REV-M1-38": "4.5 rewritten: the addenda were written to test outcomes unfavourable to the recipe and found them; the results met the pre-stated expectations (3/3 verdicts) and exceeded the expected loss in two L1 cells; 'turned from generalises into in-pool only' removed.",
 "REV-M1-39": "Consider item (DA position on the title): response for the letter — the leave-one-reconstructor-out rows were preregistered in the sense the paper defines (rules, margin and expectations hashed before the runs) and the Abstract and 1.4 label them as a post-unblinding addendum; EIC and R2 checked the title without objection. Title change is the PI's call.",
 "REV-M1-40": "Consider item, not implemented: 2.5 already dates the matching-rule change as pre-hashing ('predated'); an explicit sentence is left to the PI.",
 "REV-M1-41": "Consider item, not implemented: the sentence names 'reconstructor-agnostic' as the term the first addendum's own §11.7 bars without the clause, so it is the authors' own prior wording, not a straw man; PI to decide whether to say so or drop the clause.",
 "REV-M1-42": "3.5 puts the coverage explanation of the loss order in the conditional and says the mechanism was not tested.",
 "REV-M1-43": "Contribution one reworded: the branch stays below the floor on GN and BP and the re-scored GREIT reference shows the same pattern; 'extends' dropped.",
}
L = ["# 14 — Response to the five-seat panel, round 1 (2026-10-31; Fable 5.1; `academic-paper` revision, patch mode)", "",
     "Decision letter: `12_REVIEWER_PANEL_round1.md` (mechanical major_revision; 43 roadmap items). Authority chain: `revision-authority-round1/` (roadmap, author-choices, author-adjudication, claim-surface manifest; three validators rc = 0). Patch: `revision_patch_round1.json` (48 ops: 47 replace_block + 1 insert_after; six heading ops acknowledged as structural). Base `06_DRAFT_v1.md` 751dacb8560c → output `13_DRAFT_v2.md` 159791522c60; apply report `13_DRAFT_v2.md.apply-report.json` (101 of 148 blocks byte-identical, touched ratio 0.32, authorization witness pass).", "",
     "**Triage applied (default under the PI's session mandate; PI may overturn):** every must_fix (10) and should_fix (25) item `will_address`; every consider item (8) not implemented this round, with the response below.", "",
     "**Open for the PI after this round:** (1) main-text length 7,904 words against the PCR ceiling of 7,000 (Intro 1,125, Methods 2,555, Results 2,079, Discussion 1,901, Conclusion 244; Abstract 331 against PLoS One's 300) — the panel's required additions (network specification, deviation record, verbatim rules, standing labels, forward-model pointers) cost about 900 words; decide between raising the ceiling, cutting (candidates: 1.2–1.3 literature sentences, 2.1 reconstructor sentences moved wholly to S2 Table, 4.4 literature comparison) or a mix; the Abstract must come back to 300 in any case; (2) the eight consider items; (3) REV-M1-26/-27 source checks (Pulletz threshold; Zhao per-index result) and REV-M1-14's optional one-seed re-run; (4) the three uncited corpus entries (Rusak2020, Zhang2020TMI, Zhang2022PhysiolMeas).", "",
     "| Item | Obligation | Severity | Triage | Blocks changed (v1 ids) | Response |", "|---|---|---|---|---|---|"]
for it in rm["items"]:
    i = it["id"]; a = adj[i]
    L.append(f"| {i} | {it['obligation_class']} | {it['severity']} | {a['author_triage']} | {', '.join(sorted(set(touched.get(i, [])))) or '—'} | {RESP[i]} |")
L += ["", "## Questions for the authors (from the decision letter) — draft answers", "",
      "1. GREIT matched cell: reference, not a verdict cell; it is the companion study's row, declared for reuse in the registered text (§5), re-scored here (Table 1 legend; 2.5).",
      "2. '0.4 points' was a rounding of the largest M2′ point estimate (+0.360) with its interval (+0.504); removed; the licensed descriptive form (never worse by more than 0.3 points; −0.08 to +0.36) is used.",
      "3. The GREIT training row is reproducible from the deposited per-seed files and the companion study's code (same repository); the checkpoints are the companion's and are available from the corresponding author.",
      "4. Power: paired t approximation, dz 0.60 (the floor as a standardised effect in the diagonal cells), α 0.05, n = 30 → 0.89; dz 0.80 → 0.99; dz 0.40 → 0.56 (preregistration §5 table; S2 Table).",
      "5. All Wilcoxon p values: normal approximation with continuity correction (scipy `wilcoxon(correction=True, method='approx')`); none exact (2.6).",
      "6. Yes: the registered-path absolute Dice of the six no-retraining cells is now a Table 2 column and in S1 Table.",
      "7. No seed was excluded or re-run in any row (30 of 30 in every cell).",
      "8. The GREIT networks (seeds 0–29) were trained 2026-09-24/25 and scored 2026-09-26 00:45, before the registered state was hashed (2026-09-26 17:41); their GREIT → GREIT heart Dice was known and is named in the registered text (§1, §5).",
      "9. One-step GN is parametrised on GREIT's 64 × 64 pixel grid through a coarse-to-fine mapping from the coarse cylinder (no rasterisation of a FEM solution); S2 Table.",
      "10. Noise on the inhomogeneous frame only; the homogeneous reference is noise-free; 20 dB is an amplitude (norm) ratio of 10 (2.1, S2 Table).",
      "11. Holzschuh 2024 (0.76 vs 0.74, p = 0.18) and Yan 2020 (0.89 → 0.60): the figures come from the project's literature notes (abstract-level); the PI will confirm against the full texts (listed as open).",
      "12. 131/154 (3.2) and 1/132, 1/156 (3.3) are both seed-0 within-frame SD ratios under two different affines (training-set affine for the single-source cells; single pooled affine for the mixed row); a clause can be added if the PI wishes (consider).",
      "13. In the targeted clinical EIT systems the reconstructor is a configured setting and therefore known at deployment; whether it is exposed to downstream software must be confirmed per system (4.7).",
      "14. The 1.7-fold target-scale weighting is reported as a design fact and is left as part of the per-source normalisation question for future work; it is outside this paper's claims."]
(P/"RECON_paper/manuscript/14_RESPONSE_TO_PANEL_round1.md").write_text("\n".join(L) + "\n", encoding="utf-8")
print("written", len(rm["items"]))
