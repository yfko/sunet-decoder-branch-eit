# -*- coding: utf-8 -*-
"""Revision-authority artefacts for round 1d (2026-10-31 evening): the five B5 operands of the re-review
(18_REVIEWER_PANEL_rereview_round1.md): NEW-1, NEW-2, NEW-3 (minor regressions) and the must_fix residuals of REV-M1-2 and
REV-M1-19. Base 17_DRAFT_v4.md (6379490727ef, 160 blocks). Seats = the re-review verifier that found/verified each item."""
import json, subprocess, sys
from pathlib import Path
PROJ = Path("/Users/yfko/Library/Mobile Documents/com~apple~CloudDocs/Documents/New idea/SunetBeta_the importance-of-divided-branch-structure")
S = Path.home() / ".claude/plugins/cache/academic-research-skills/academic-research-skills/3.23.0/scripts"
sys.path.insert(0, str(S.parent))
from scripts.revision_roadmap import bytes_hash, _source_key  # noqa
ROOT = PROJ / "RECON_paper/manuscript/revision-authority-round1d"
BASE = PROJ / "RECON_paper/manuscript/17_DRAFT_v4.md"; MANIFEST = PROJ / "RECON_paper/manuscript/17_DRAFT_v4.md.block-manifest.json"
EVENT = ROOT / "author_event_20261031d.txt"
base_raw = BASE.read_bytes(); manifest_raw = MANIFEST.read_bytes()
assert bytes_hash(base_raw).startswith("6379490727ef"), bytes_hash(base_raw)
def raw(v): return (json.dumps(v, ensure_ascii=False, sort_keys=True, separators=(",", ":")) + "\n").encode("utf-8")
COMP = {"EIC": "Journal-Fit seat of the 2026-10-31 re-review (Phase 2A/2B verifier persona from the frozen round-1 card)", "R2": "Domain seat (EIDORS thoracic EIT reconstruction) of the 2026-10-31 re-review (Phase 2A verifier persona from the frozen round-1 card)"}
def item(n, seat, ordinal, sc, desc, blocks, anchor_block, quote, obl, sev, code, verify, action, kind="sentence"):
    return dict(id=f"REV-M1d-{n}", source_refs=[{"seat": seat, "channel": "finding", "ordinal": ordinal, "subclaim_ordinal": 0}], reviewer=seat,
        description=f"{sc}: {desc}", sub_claim_ids=[sc], obligation_class=obl, severity=sev,
        evidence_anchor={"anchor_type": "text", "locator": anchor_block, "quote": quote}, confidence=5, corroborating_sources=[],
        cost_scope={"kind": kind, "locator": ", ".join(blocks)}, consequence_if_unaddressed={"code": code, "target": {"kind": "manuscript", "locator": ", ".join(blocks)}},
        target_section=", ".join(blocks), suggested_action=action, consensus_level="SINGLE-VERIFIER", verification_criteria=verify,
        proposed_targets=[{"block_id": b, "allowed_operations": ["replace_block"]} for b in sorted(blocks)], competence_basis=COMP[seat])
items = [
 item(1, "EIC", 1, "SC-NEW1", "Re-review NEW-1 (regression, minor): the amplitude-ratio sentence added to B0023 in round 1 uses 'GN' and 'BP' one paragraph before B0024 defines them.", ["B0023"], "B0023", "(training-split SD ratio; GREIT, GN, BP)", "must_fix", "minor", "reader_traceability_reduced",
      "B0023 names the reconstructors in full or after their definition; no abbreviation is used before it is defined.", "Write the names out in B0023."),
 item(2, "R2", 1, "SC-NEW2", "Re-review NEW-2 (regression, minor; = 16b_CITATION_RECHECK_v4.md N1): B0074 says this study's 16–62 and 19–34 point losses 'start where that range ends' while the analogue range in the same sentence is 4–31 points, so both begin inside it; and the sentence compares magnitudes while saying magnitudes cannot be compared.", ["B0074"], "B0074", "start where that range ends", "must_fix", "minor", "claim_scope_unsupported",
      "B0074 no longer ranks this study's losses against the analogue range; it calls them losses of the same kind and keeps the two differences that forbid a comparison of magnitudes.", "Replace the comparison clause without adding length."),
 item(3, "R2", 2, "SC-NEW3", "Re-review NEW-3 (regression, minor): B0028 and Table 4 (B0116) say the reused companion GREIT networks were 'trained on 2026-09-24 and 25'; the only training record (RESULTS_STUDY2.md §十之二) is a 116-run campaign 2026-09-24 16:26 to 2026-09-26 00:44 with no per-seed completion times; the before-hashing ordering (17:41 on 09-26) holds either way.", ["B0028", "B0116"], "B0028", "trained on 2026-09-24 and 25 and scored on 2026-09-26, before the registered state was hashed", "must_fix", "minor", "reporting_requirement_unmet",
      "B0028 and the Table 4 registered-state cell give the campaign window as the record gives it (2026-09-24 16:26 to 2026-09-26 00:44) and the hashing time (17:41 on 2026-09-26); S2 Table's training row carries the same window.", "Replace the two dates by the recorded window in B0028 and regenerate Table 4 (and the S2 training row) from tools/recon_draft_tables.py."),
 item(4, "EIC", 2, "SC-R2res", "Residual of REV-M1-2 (must_fix PARTIALLY, consider residual): the last sentence of B0066 restates the M2′ quantities ('differed by −0.08 to +0.36 points with two of six intervals favouring pooling') without a standing word, unlike every other number-carrying clause of B0066 and B0085.", ["B0066"], "B0066", "the two ways of doing so differed by −0.08 to +0.36 points with two of six intervals favouring pooling", "must_fix", "minor", "claim_scope_unsupported",
      "The last sentence of B0066 carries '(first addendum; descriptive)' beside the M2′ quantities.", "Add the standing parenthesis."),
 item(5, "R2", 3, "SC-R19res", "Residual of REV-M1-19 (must_fix PARTIALLY, consider residual): S2 Table (B0158) gives the contact impedance only as 'EIDORS default' and does not state the GREIT training-target distribution or the desired-image width; in addition, its 'training targets of radius parameter 0.02' is inexact (under distr 0 the training targets have radius 0.05 of the mean half-width; 0.02 is the noise-figure calibration target) and the normalised-difference setting of all three reconstructors is unstated.", ["B0158"], "B0158", "1,000 simulated training targets of radius parameter 0.02, noise figure 0.5 (nominal)", "must_fix", "minor", "method_reproducibility_unresolved",
      "S2 Table states the contact impedance value and its source, the GREIT training-target distribution (spiral, radii, plane), the desired-image function and radius, the noise-figure calibration target, and the normalised-difference setting, every value traceable to a named script line (author_event_20261031d.txt).", "Regenerate S2 Table from tools/recon_draft_tables.py after editing its Forward model, GREIT and Training rows.", kind="section"),
]
items.sort(key=lambda it: (_source_key(it["source_refs"][0]), it["id"]))
counts = {k: sum(1 for i in items if i["obligation_class"] == k) for k in ("must_fix", "should_fix", "consider")}
roadmap = {"schema_version": "revision-roadmap/1.0", "revision_round": 4, "base_draft_sha256": bytes_hash(base_raw), "block_manifest_sha256": bytes_hash(manifest_raw),
    "items": items, "total_items": len(items), "obligation_counts": counts, "editorial_decision": "Minor Revision",
    "consensus_summary": "Round 1d (2026-10-31 evening): the five B5 operands of the legacy three-gate re-review (18_REVIEWER_PANEL_rereview_round1.md, checker exit 0, Minor Revision after the PI adjudicated DIS-1/DIS-2 replacement_approved): regressions NEW-1, NEW-2, NEW-3 and the consider-level residuals of must_fix items REV-M1-2 and REV-M1-19. Wording, one standing label, one recorded time window and S2 Table method facts read from the EIDORS v3.8 source and the project scripts; no number of this study, verdict, hash, fixed sentence or scope rule changes.",
    "dissenting_opinions": []}
roadmap_raw = raw(roadmap); (ROOT / "roadmap.json").write_bytes(roadmap_raw)
cs = {"schema_version": "claim-surface-manifest/1.0", "revision_round": 4, "roadmap_sha256": bytes_hash(roadmap_raw), "base_draft_sha256": bytes_hash(base_raw), "claim_intent_sources": [], "surfaces": []}
(ROOT / "claim-surface-manifest.json").write_bytes(raw(cs))
event = "AUTHOR-EVENT-PI-recon-tier3-round1d-2026-10-31"
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
