# Citation audit v3 — `29_DRAFT_v3.md` (academic-paper citation-check, 2026-10-06, Fable 5.1)

**Draft**: `manuscript/29_DRAFT_v3.md` (patch apply of 2026-10-06, round 2; apply report `29_DRAFT_v3.md.apply-report.json`, output hash `0a5114777ca6`, witness PASS, 110/125 blocks byte-identical). **Corpus**: `refs/refs_in.json` (53) → `refs/prior_works.json` + `refs/prior_works_strings.md` (`tools/cite.py`, Crossref REST + PubMed E-utilities, 2026-10-06 16:31; `refs/overrides.json` applied 16:35). **Policy**: existence strict, retraction strict (R12d). **Scanners**: `tools/check_draft.py`; the visible-form check below. Run after the round-2 revision, as R12 requires; the v2 audit is `17_CITATION_AUDIT_v2.md`.

## 1. Existence and retraction (strict)

| Item | Result |
|---|---|
| Reference entries | 53 (19 in v2 + 34 ★ entries accepted by the PI on 2026-10-06; the six no-DOI candidates were not cited, by PI decision) |
| Resolved by DOI (Crossref) | 53/53 (`refs/prior_works_strings.md` 核對聲明) |
| PubMed-indexed | 38/53; the 15 not indexed are conference, LNCS, SIAM and TIM entries (abbreviation from Crossref short-container-title) |
| Retracted | 0 |
| Corrected (`updated-by`) | 0 in the registry run; Ren 2020 TIM has a separate correction notice (10.1109/tim.2020.3012378) read on IEEE Xplore 2026-10-06: it corrects the typesetting of equation (9) only, so the original is cited unchanged |
| Hand-typed strings | 0 (the reference block was written by `phase6_revision/emit_patch_round2.py` reading the Vancouver section of `prior_works_strings.md`; 53 lines, asserted) |
| Overrides applied (human-checked, sourced in `refs/overrides.json`) | Kendall 2018 author order (CVF page); Vandenhende 2022 year/volume/issue/pages (PubMed); Kurin 2022 particle 'De Palma' (NeurIPS page); LNCS volumes for Isensee 2024, Myronenko 2019, Rusak 2020 (Springer chapter pages); Vandenhende 2020 particles 'Van Gool'/'De Brabandere' (order per Crossref and S2; **BMVC PDF not opened, order to be checked at format-convert**) |

**Verdict: strict existence passes; no blocker.**

## 2. In-text ↔ reference list

| Item | Result |
|---|---|
| In-text instances | 65 |
| Distinct sources | 53 |
| Slugs outside corpus | 0 |
| Orphan references | 0 (every one of the 53 entries is cited at least once) |
| Cited but unlisted | 0 |
| Visible author–year form vs registry | 65/65 match on first-author surname and year (script in session log); the two fixes carried from v2 §4 are now in the text: "Kendall et al., 2018" (was "Cipolla et al."), "Vandenhende et al., 2022" (was 2021) |
| Same-surname disambiguation | Zhang K 2018 / 2021 / 2022 (Physiol Meas) and Zhang T 2022 (review) are written with initials ("K. Zhang et al., 2022", "T. Zhang et al., 2022"); Ko and Cheng 2021a/2021b unchanged. Format-convert replaces all with numbers for PLoS One/Vancouver-style venues |
| Self-citation | 3/53 = 5.7% (v2: 15.8%; ARS flag at 15%). Stated in §4.3 and Conflicts of Interest ("Three of the fifty-three") |
| Source currency | 13/53 from 2022 or later (25%); 18/53 older than 10 years, all either method originals (Wilcoxon 1945, Adler 1996, Caruana 1997, Eyuboglu 1988, Zadehkoochak 1992, Leathard 1994), tools (EIDORS 2006, GREIT 2009, U-Net 2015) or the field's standard references for ROI, temporal separation and instrument SNR (Pulletz 2006, Deibele 2008, Frerichs 2009, Gagnon 2010, Grant 2011, Boyle 2011, Borges 2012, Nguyen 2012, Lakens 2013). None flagged for replacement |

Distribution: Ko2021PLOSONE 3, Wang2024TIM 3; Nguyen 2012, Borges 2012, Ko 2025, Hamilton 2018, Herzberg 2023, Yu 2024, Kamann 2021, Boone 2023 ×2; all others ×1.

## 3. Claim faithfulness of the 34 new citations

Every new citation sentence was written in this session against the abstract-level **Key finding** recorded for that entry in `literature/lit_review_20261006/phase2_bibliography/block1–4` (bibliography agents, Opus, 2026-10-06), and checked again here sentence by sentence. **No full text was read for any of the 34**, so no quote anchors are claimed (`anchor:none:` on all 34; 53/65 instances overall). The table lists what each sentence attributes and the basis.

| Block | Source | What the sentence attributes | Basis | Verdict |
|---|---|---|---|---|
| B0009 | Spinelli 2021 | EIT-measured V/Q mismatch an independent predictor of ARDS mortality, prospective cohort | abstract: 50 ARDS patients, unmatched units higher in non-survivors, independent predictor (OR 1.22, AUC 0.88) | ✔ |
| B0009 | Nguyen 2012 | perfusion EIT reviewed as a route to detecting pulmonary embolism | abstract: PE named the most likely main application | ✔ |
| B0009 | Leathard 1994 | tidal breathing ≈9% resistivity change; cardiac-cycle change 0.9–2.6%, region-dependent | abstract: 9% (SD 3%); −0.9% to −2.6% by region | ✔ (sign dropped in text; magnitude only) |
| B0009 / B0062 | Borges 2012 | bolus first-pass perfusion agreed with SPECT and was superior to the pulsatility estimate; separated component ≠ perfusion | abstract: agreement with SPECT; superior to impedance-pulsatility estimate (6 piglets) | ✔ |
| B0115 | Eyuboglu 1988 | ECG-gated averaging in applied potential tomography; low SNR required synchronised acquisition and averaging | abstract: synchronisation with cardiac activity required; time averaging because of low SNR; R-wave-locked gating methods compared | ✔ |
| B0115 | Zadehkoochak 1992 | frequency filtering; separable bands; ≈15 s of data vs ≥100 cardiac cycles for gating | abstract: gated averaging needs ≥100 cycles; components separable in frequency; ≈15 s acquisition | ✔ |
| B0115 | Nguyen 2012 | ECG gating, frequency filtering, PCA and breath holding as the standard routes | abstract: reviews ECG gating, frequency filtering, PCA | ✔ (breath holding is from Grant 2011, cited in the same sentence) |
| B0115 | Stowe 2019 | same animal data, bolus reference: filtering > ensemble averaging; similar during ventilation and apnoea | abstract: as stated (7 lambs) | ✔ |
| B0115 | Silva 2025 | adaptive harmonic methods; spectral and spatial overlap named as a limitation of existing methods | abstract: harmonic least-squares and harmonically constrained filtering; spectral/spatial overlap, interaction and non-stationarity as limitations | ✔ |
| B0115 | Zhang K 2022 Physiol Meas | Siamese network on breath-hold series → feature-matching constraint; unsupervised separation of a chest EIT image **series**; qualitative agreement with nuclear perfusion in 3 patients | abstract: as stated | ✔ (the series-vs-frame distinction is the manuscript's, stated as such) |
| B0126 | Zhang T 2022 (review) | three headings: single network, network + conventional algorithm, multi-network hybrids | abstract: three categories as stated | ✔ |
| B0126 | Zhang K 2021 TBME | supervised descent; accuracy and noise resistance vs Gauss–Newton on synthetic data; broadly consistent with CT on measured chest data | abstract (S2): as stated; CT comparison qualitative | ✔ |
| B0126 / B0053 | Hamilton 2018 | CNN post-processing of D-bar, trained on simulation, applied to experimental data without transfer training | abstract: as stated (ACT4, KIT4 data) | ✔ |
| B0126 / B0053 | Herzberg 2023 | graph U-Net trained on simple 2-D simulations post-processed reconstructions from devices of different geometry/instrumentation incl. 3-D | abstract: as stated | ✔ |
| B0126 | Capps 2021 | network trained on scattering-transform/organ-boundary pairs recovered heart and lung boundaries within the D-bar framework | abstract (PubMed): as stated | ✔ |
| B0126 / B0011 | Yu 2024 | segmentation branch + reconstruction branch fused, lung-shaped data, tolerance of measurement noise and modelling error a stated aim | abstract (PubMed): as stated | ✔ |
| B0011 | Misra 2016 | where to split has no general answer, starting point of cross-stitch | abstract: existing approaches enumerate architectures per task and do not generalise | ✔ |
| B0011 | Vandenhende 2020 | branching structures compared under a fixed parameter budget, built from task affinity, shallow shared/deep specific; "the one study we found" | abstract: as stated; search-bounded wording | ✔ (search-bounded) |
| B0011 | Kendall 2018 | learned per-task uncertainty weighting | title/method | ✔ (unchanged from v2 except author order) |
| B0011 | Liu 2019 | dynamic average following each task's rate of loss change (DWA) | abstract: DWA proposed; less sensitive to weighting | ✔ |
| B0011 | Kurin 2022 | plain sum of losses with single-task regularisation matches or beats specialised multi-task optimisers | abstract: as stated | ✔ |
| B0011 | Xin 2022 | MTO methods did not outperform a tuned weighted average across language and vision tasks | abstract: as stated | ✔ |
| B0011 | Isensee 2024 | claims of new architectures beating a U-Net often rested on inadequate baselines and did not survive rigorous validation | abstract: baseline/dataset/compute shortcomings; claims do not hold | ✔ |
| B0011 / B0056 | Kamann 2021 | tolerance of corruptions differs between architectures and depends strongly on corruption type | abstract: as stated | ✔ |
| B0011 / B0056 | Boone 2023 | MRI segmentation networks highly sensitive to simulated distribution shifts incl. SNR changes | abstract: as stated; augmentation improves | ✔ |
| B0027 | Ren 2020 | random simulated measurement noise and model error in training data, shape reconstruction | abstract: as stated | ✔ |
| B0027 | Murphy 2019 | training data assumed poor electrode contact without specifying electrodes; cardiac-output estimation | abstract: as stated | ✔ |
| B0027 | Jeschke 2025 | electrode-displacement samples added to the training set, wearable thoracic EIT | abstract: as stated | ✔ |
| B0052 | Castro 2020 | "acquisition shift" vocabulary for development/target mismatch | abstract: causal framing of dataset–environment mismatch incl. acquisition-related shift | ✔ (term attribution) |
| B0052 | Zhang K 2018 FFDNet | discriminative denoisers trained per noise level, no flexibility; FFDNet takes a noise-level map as input | abstract: as stated | ✔ |
| B0052 | Rusak 2020 | appropriately tuned Gaussian noise during training improved generalisation to unseen corruptions (classification) | abstract (arXiv): as stated | ✔ |
| B0053 | Adler 1996 | regularised linearised inverse; noise amplification as figure of merit; contrast detectability vs measurement noise and algorithm | abstract: as stated | ✔ |
| B0056 | Gagnon 2010 | resistive mesh phantom; SNR depends on frame rate, frequency, current, strategy; report figures with those parameters | abstract: as stated (also intermodulation distortion, omitted) | ✔ |
| B0058 | Graham 2019 HoVer-Net | shared encoder with task-specific up-sampling branches; nuclear segmentation and classification; widely used | abstract: as stated; "widely used" is the manuscript's characterisation | ✔ (one adjective ours) |
| B0062 | Boyle 2011 | electrode-area/contact-impedance errors give ringing, field-wide artefacts and structural distortion rather than additive noise | abstract: as stated (plus mean contact impedance rise harmless, omitted) | ✔ |
| B0062 | Myronenko 2019 | added reconstruction (VAE) branch as regulariser of the shared encoder, brain-tumour segmentation, limited data | abstract: as stated (BraTS 2018 winner) | ✔ |

No sentence attributes to a source a finding beyond its abstract. Two sentences carry a characterisation that is ours and is marked above (HoVer-Net "widely used"; the series-versus-frame contrast). The Introduction's absence claim is now bounded by four named databases, a date and a pointer to the stored strings (R12), and names the two nearest adjacent works.

## 4. Metadata and rendering items (do not hand-edit; fix at the registry or at format-convert)

1. **Vandenhende 2020 author order**: Crossref and S2 give Vandenhende, Georgoulis, Van Gool, De Brabandere; arXiv 1904.02920 gives De Brabandere before Van Gool. The BMVC 2020 PDF was not opened (site 404 on 2026-10-06). **Check the PDF at format-convert**; if the order differs, add an override with the source and re-run `cite.py`.
2. Carried from v1/v2: Pulletz 2006 given-name rendering ("Genderingen HRv"), Lakens 2013 missing article number 863, Ronneberger 2015 missing LNCS volume 9351, Wang 2024 and Ren 2020 double full stop in "IEEE Trans. Instrum. Meas..", Herzberg 2023 stray "⋆" in the Crossref title. All for format-convert.
3. Kendall 2018 and Vandenhende 2022 are now correct in both the list and the text (v2 §4 items 1–2 closed).

## 5. Anchor locators (v3.7.3)

53/65 instances carry `anchor:none:`; the 12 quote anchors are the three prior works, Wang 2024, Frerichs 2009, Grant 2011, Deibele 2008 and Graf 2017 (unchanged from v2). None of the 34 new entries was read in full, so none carries a quote anchor; `source_verification_agent`-style locators would need full-text reading, which the PI did not order. Format-convert strips anchor markers.

## 6. Watch-term scan (R12 / boundary clauses) and R8

`check_draft.py` on v3: no "first to", "no previous stud", "novel", "first time", "noisy", "divided branch", "robust"; "the first " ×4 (v2 ×3; the new one is "came first" in the history of ECG gating, not a priority claim). Em dashes 2 (abstract/keywords headers), semicolons 14 (threshold 14). Pipeline-leak scan on the manuscript part: clean.

## 7. Conclusion

Strict existence and retraction pass. Zero orphans both ways, zero out-of-corpus slugs, self-citation 5.7%. One registry item (§4.1, author order to confirm against the BMVC PDF) and five rendering items go to format-convert; none blocks the next step. Next citation-check: after the next major change.
