# -*- coding: utf-8 -*-
"""Revision-authority artefacts for round 1e (2026-10-31 late evening): the PI's answers (「照建議全收」) to the items left
open after the re-review — six consider items of round 1 (REV-M1-25/-30/-33/-35/-40/-41; -37/-39 kept as letter responses),
the should_fix residuals REV-M1-6/-13, the registry orphans of 16_CITATION_AUDIT_v3.md §7 (Zhang2022PhysiolMeas cited,
two removed), the audit's minor wording items m1/m2/m3/m5/m6/m7/m8/m10/m12, and the three S2 Table qualifiers of the
scoped v5 addendum. Base 19_DRAFT_v5.md (bf252f799a3a, 160 blocks). Continued round-1 items reuse the seat and ordinal of
the round-1 roadmap with subclaim_ordinal 1 (round 1b precedent); audit items ride the EIC editorial channel (1c precedent)."""
import json, subprocess, sys
from pathlib import Path
PROJ = Path("/Users/yfko/Library/Mobile Documents/com~apple~CloudDocs/Documents/New idea/SunetBeta_the importance-of-divided-branch-structure")
S = Path.home() / ".claude/plugins/cache/academic-research-skills/academic-research-skills/3.23.0/scripts"
sys.path.insert(0, str(S.parent))
from scripts.revision_roadmap import bytes_hash, _source_key  # noqa
ROOT = PROJ / "RECON_paper/manuscript/revision-authority-round1e"
BASE = PROJ / "RECON_paper/manuscript/19_DRAFT_v5.md"; MANIFEST = PROJ / "RECON_paper/manuscript/19_DRAFT_v5.md.block-manifest.json"
EVENT = ROOT / "author_event_20261031e.txt"
base_raw = BASE.read_bytes(); manifest_raw = MANIFEST.read_bytes()
assert bytes_hash(base_raw).startswith("bf252f799a3a"), bytes_hash(base_raw)
def raw(v): return (json.dumps(v, ensure_ascii=False, sort_keys=True, separators=(",", ":")) + "\n").encode("utf-8")
COMP = {"EIC": "Journal-Fit seat of the 2026-10-31 manuscript panel (PLoS One academic-editor identity)",
        "R1": "Methodology seat of the 2026-10-31 manuscript panel (preregistered deep-learning simulation statistics)",
        "R2": "Domain seat (EIDORS thoracic EIT reconstruction) of the 2026-10-31 manuscript panel",
        "R3": "Perspective seat (medical-image domain generalisation / multi-source training) of the 2026-10-31 manuscript panel",
        "DA": "Devil's Advocate seat of the 2026-10-31 manuscript panel",
        "AUD": "Journal-Fit seat (EIC) carrying the strict citation-check's registry and wording findings (16_CITATION_AUDIT_v3.md §5, §7, §10; PI decision 2026-10-31 late evening)",
        "SV": "Domain seat (EIDORS thoracic EIT reconstruction) carrying the scoped v5 re-verification's untraceable-qualifier notes (18_ second Addendum)"}
def item(n, seat, channel, ordinal, sub, sc, desc, blocks, anchor_block, quote, obl, sev, code, verify, action, kind="sentence", comp=None):
    return dict(id=f"REV-M1e-{n}", source_refs=[{"seat": seat, "channel": channel, "ordinal": ordinal, "subclaim_ordinal": sub}], reviewer=seat,
        description=f"{sc}: {desc}", sub_claim_ids=[sc], obligation_class=obl, severity=sev,
        evidence_anchor={"anchor_type": "text", "locator": anchor_block, "quote": quote}, confidence=5, corroborating_sources=[],
        cost_scope={"kind": kind, "locator": ", ".join(blocks)}, consequence_if_unaddressed={"code": code, "target": {"kind": "manuscript", "locator": ", ".join(blocks)}},
        target_section=", ".join(blocks), suggested_action=action, consensus_level="SINGLE-VERIFIER", verification_criteria=verify,
        proposed_targets=[{"block_id": b, "allowed_operations": ["replace_block"]} for b in sorted(blocks)], competence_basis=COMP[comp or seat])
items = [
 item(1, "R2", "finding", 7, 1, "SC-25", "Continuation of REV-M1-25 (consider, PI accepted): add the original Sheffield attribution for back-projection beside the EIDORS citation in B0024 — Barber and Brown 1984 (doi:10.1088/0022-3735/17/9/002), registered through the R12d pipeline; the reference list (B0092) is regenerated in order of first citation.",
      ["B0024", "B0092"], "B0024", "Back-projection (BP) used the Sheffield back-projection matrix distributed with EIDORS", "should_fix", "minor", "reader_traceability_reduced",
      "B0024 cites Barber and Brown 1984 for the Sheffield back-projection matrix with a verified anchor; B0092 lists it with the Crossref-generated Vancouver string; numbering remains order of first citation.", "Add the citation and regenerate the reference list."),
 item(2, "R3", "finding", 4, 1, "SC-30", "Continuation of REV-M1-30 (consider, PI accepted): add, outside the fixed R3 interpretation sentence in B0049, a neutral clause stating that the shift tested here is a change of reconstructor and that other kinds of shift (e.g. measurement-noise level) were not tested; the fixed sentence is untouched.",
      ["B0049"], "B0049", "the noise sweep it names is the companion study's, whose result this paper does not use", "should_fix", "minor", "interpretive_ambiguity_remains",
      "B0049 carries the design-fact clause after the fixed sentence; the quoted fixed sentence is byte-identical to v5.", "Append one sentence."),
 item(3, "R3", "finding", 7, 1, "SC-33", "Continuation of REV-M1-33 (consider, PI chose option (a)): the leave-one-reconstructor-out in-pool cells are called 'in-pool comparison cells' in B0059, the Table 3 caption (B0112), the Table 3 footnote (B0114) and Table 4 (B0116), matching the S1 caption (B0094); 'reference' remains for the target image and the re-scored GREIT reference row.",
      ["B0059", "B0112", "B0114", "B0116"], "B0059", "The six in-pool reference cells of the same rows", "should_fix", "minor", "interpretive_ambiguity_remains",
      "No block of the manuscript calls the loro in-pool cells 'reference cells' or 'in-pool references'; B0059, B0112, B0114 and B0116 say 'in-pool comparison cells'; the GREIT reference row and the reference image keep 'reference'.", "Rename in the four blocks (tables via tools/recon_draft_tables.py).", kind="section"),
 item(4, "R3", "finding", 9, 1, "SC-35", "Continuation of REV-M1-35 (consider, PI accepted): B0078's 'a simulated review round' carries a pointer to the Acknowledgments where the panels are described.",
      ["B0078"], "B0078", "those a simulated review round, recorded in the repository before the addendum was written, had asked for", "should_fix", "minor", "reader_traceability_reduced",
      "B0078 carries '(Acknowledgments)' beside 'a simulated review round'.", "Insert the pointer."),
 item(5, "DA", "finding", 3, 2, "SC-40", "Continuation of REV-M1-40 (consider, PI accepted): B0036 states explicitly that the matching rule changed before hashing and that §6's acceptance band was not updated, so 'no setting or rule changed' and 'the change of matching rule' no longer sit together without timing.",
      ["B0036"], "B0036", "predated the change of matching rule from GREIT's nominal to its realised value", "should_fix", "minor", "interpretive_ambiguity_remains",
      "B0036 carries the timing parenthesis beside the matching-rule deviation.", "Insert the parenthesis."),
 item(6, "DA", "finding", 4, 1, "SC-41", "Continuation of REV-M1-41 (consider, PI accepted): B0069 attributes 'reconstructor-agnostic' to the authors' own first-addendum wording, so the falsified term is sourced rather than unattributed.",
      ["B0069"], "B0069", "Within this study's scope the term \"reconstructor-agnostic\" is falsified", "should_fix", "minor", "claim_scope_unsupported",
      "B0069 names the first addendum as the source of the term.", "Insert the attribution."),
 item(7, "EIC", "finding", 5, 1, "SC-6res", "Residual of REV-M1-6 (should_fix PARTIALLY, consider residual): the repository-tag placeholders in B0042 and B0150 carry no 'set at submission' marking and B0013's '[MATERIAL GAP: preprint DOI]' is a bare token explained only in B0089.",
      ["B0013", "B0042", "B0150"], "B0042", "[MATERIAL GAP: repository tag for this paper]", "should_fix", "minor", "reporting_requirement_unmet",
      "Every MATERIAL GAP marker states when it is filled or where it is explained: B0042/B0150 'repository tag, set at submission'; B0013 points at the Related manuscript statement.", "Reword the three markers."),
 item(8, "R1", "finding", 7, 1, "SC-13res", "Residual of REV-M1-13 (should_fix PARTIALLY, consider residual): the 3.4 confound sentence (B0057) does not name the two R3 cells scored on the companion-trained GREIT networks (GREIT → GN, GREIT → BP).",
      ["B0057"], "B0057", "the GREIT networks come from the companion study's campaign (Section 2.2), so a between-campaign difference is confounded with the contrast", "should_fix", "minor", "reporting_requirement_unmet",
      "B0057 names GREIT → GN and GREIT → BP as the R3 cells evaluated on the companion-trained networks.", "Add the clause."),
 item(9, "EIC", "editorial", 2, 0, "SC-G", "Citation audit §7/§10 item 9 (registry orphans; PI decision): Zhang2022PhysiolMeas is cited in B0013 (a Siamese network as feature-matching constraint for unsupervised separation of the cardiac-related signal from chest EIT image series, from the Crossref abstract) as 'Zhang et al., 2022a', so the lone 'Zhang et al., 2022b' is paired; Rusak2020ECCV and Zhang2020TMI are removed from refs/refs_in_recon.json; B0092 regenerated.",
      ["B0013", "B0092"], "B0013", "and heart-related image reconstruction from GREIT frames with optimised loss weights (Ko et al., 2025)", "should_fix", "minor", "reader_traceability_reduced",
      "B0013 cites Zhang2022PhysiolMeas with a verified anchor and a claim matching its abstract; tools/check_recon_draft.py reports 0 orphans and 72 reference-list entries equal to the distinct cited keys.", "Add the clause; regenerate the list.", comp="AUD"),
 item(10, "EIC", "editorial", 3, 0, "SC-m", "Citation audit §5 minor wording items m1 (B0030 Pulletz: one study's recommendation), m2 (B0072 Albert: intensity premise marked as the authors'), m3 (B0027 Isensee: adequately configured baseline at comparable compute), m5 (B0077: 'a kind of result exposed', not 'most'), m6 (B0016 Liu: 'used'), m7 (B0028 Caruana: sharing the encoder is the hard parameter sharing), m8 (B0028 Renard: variability can be large; 'of the order of the effects' is this study's), m10 (B0075 Du: CT radiomics), m12 (B0033 Jeschke: one design). PI accepted all.",
      ["B0016", "B0027", "B0028", "B0030", "B0033", "B0072", "B0075", "B0077"], "B0077", "the kind of result most exposed to under-reporting", "should_fix", "minor", "claim_scope_unsupported",
      "Each of the nine sentences reads as the audit's suggestion (16_ §5 table); citation anchors unchanged; no number changes.", "Apply the nine wording changes.", kind="section", comp="AUD"),
 item(11, "R2", "finding", 10, 0, "SC-S2q", "Scoped v5 re-verification, three untraceable S2 qualifiers (18_ second Addendum): (a) 'in model units' beside the contact impedance 0.01 is replaced by the statement that EIDORS assigns the default no unit; (b) the noise-figure calibration target's radius 0.02 is stated as a fraction of the model radius (mk_GREIT_model.m lines 378–382: xyzr(4) = mean(target_size)·0.5·R with R the node extent); (c) 'no per-seed completion times were logged' is replaced by 'per-run durations were logged; completion timestamps were not written to the run files' (tools/train_arms.py lines 173–184, 229–240).",
      ["B0158"], "B0158", "no per-seed completion times were logged", "should_fix", "minor", "method_reproducibility_unresolved",
      "S2 Table (B0158): the contact-impedance cell names the default and that EIDORS gives no unit; the GREIT cell says 'radius 0.02 of the model radius'; the Training cell says per-run durations were logged and completion timestamps were not written to the run files; every statement traceable to the named script lines.", "Edit the three rows in tools/recon_draft_tables.py and regenerate.", kind="section", comp="SV"),
]
items.sort(key=lambda it: (_source_key(it["source_refs"][0]), it["id"]))
counts = {k: sum(1 for i in items if i["obligation_class"] == k) for k in ("must_fix", "should_fix", "consider")}
roadmap = {"schema_version": "revision-roadmap/1.0", "revision_round": 5, "base_draft_sha256": bytes_hash(base_raw), "block_manifest_sha256": bytes_hash(manifest_raw),
    "items": items, "total_items": len(items), "obligation_counts": counts, "editorial_decision": "Minor Revision",
    "consensus_summary": "Round 1e (2026-10-31 late evening): the PI's answers (「照建議全收」) to the items left open after the re-review and round 1d — six round-1 consider items implemented (REV-M1-25/-30/-33/-35/-40/-41; -37/-39 answered in the letter only), the should_fix residuals REV-M1-6/-13, the registry orphans (Zhang2022PhysiolMeas cited; Rusak2020ECCV and Zhang2020TMI removed; Barber and Brown 1984 added for REV-M1-25), the audit's nine minor wording items, and the three S2 Table qualifiers of the scoped v5 addendum. Wording, one new citation and one restored citation, three placeholder markers, two S2 method facts read from EIDORS and project source; no number of this study, verdict, hash, fixed sentence or scope rule changes; main text kept ≤ 8,000 words by trims inside the replaced blocks.",
    "dissenting_opinions": []}
roadmap_raw = raw(roadmap); (ROOT / "roadmap.json").write_bytes(roadmap_raw)
cs = {"schema_version": "claim-surface-manifest/1.0", "revision_round": 5, "roadmap_sha256": bytes_hash(roadmap_raw), "base_draft_sha256": bytes_hash(base_raw), "claim_intent_sources": [], "surfaces": []}
(ROOT / "claim-surface-manifest.json").write_bytes(raw(cs))
event = "AUTHOR-EVENT-PI-recon-tier3-round1e-2026-10-31"
choices = {"schema_version": "author-adjudication-input/1.0",
    "author_events": [{"event_id": event, "source": "explicit_session_user_message", "actor_role": "author", "input_sha256": bytes_hash(EVENT.read_bytes())}],
    "display_order": {"mode": "source_traceability", "item_ids": [i["id"] for i in items], "author_event_id": event},
    "author_adjudications": [{"item_id": it["id"], "author_event_id": event, "author_triage": "will_address", "authorized_targets": it["proposed_targets"], "claim_strength_authorizations": []} for it in items],
    "collateral_authorizations": []}
(ROOT / "author-choices.json").write_bytes(raw(choices))
if (ROOT / "author-adjudication.json").exists(): (ROOT / "author-adjudication.json").unlink()
cli = [sys.executable, str(S / "revision_roadmap.py")]; common = ["--base", str(BASE), "--block-manifest", str(MANIFEST)]
for args in (["validate-roadmap", str(ROOT / "roadmap.json")] + common,
             ["build-adjudication", str(ROOT / "roadmap.json")] + common + ["--claim-surface", str(ROOT / "claim-surface-manifest.json"), "--author-choices", str(ROOT / "author-choices.json"), "--artifact-root", str(ROOT), "--output", str(ROOT / "author-adjudication.json")],
             ["validate-adjudication", str(ROOT / "roadmap.json"), str(ROOT / "author-adjudication.json")] + common + ["--claim-surface", str(ROOT / "claim-surface-manifest.json"), "--artifact-root", str(ROOT)]):
    r = subprocess.run(cli + args, capture_output=True, text=True); print(args[0], "rc=", r.returncode, (r.stdout + r.stderr).strip()[-600:])
    if r.returncode: sys.exit(1)
