# -*- coding: utf-8 -*-
"""Revision-authority artefacts for round 1c (2026-10-31 evening): the six claim–source flags of 16_CITATION_AUDIT_v3.md
plus one '19 to 33' consistency slip. Base 15_DRAFT_v3.md (aed5252125fd, 160 blocks). Seat/channel: the roadmap schema's
seat enum has no citation-auditor seat; these are editorial-conformance findings carried on the EIC editorial channel,
ordinals 2–8 (1b used ordinal 1 in its own roadmap), each description naming the audit flag it comes from."""
import json, subprocess, sys
from pathlib import Path
PROJ = Path("/Users/yfko/Library/Mobile Documents/com~apple~CloudDocs/Documents/New idea/SunetBeta_the importance-of-divided-branch-structure")
S = Path.home() / ".claude/plugins/cache/academic-research-skills/academic-research-skills/3.23.0/scripts"
sys.path.insert(0, str(S.parent))
from scripts.revision_roadmap import bytes_hash, _source_key  # noqa
ROOT = PROJ / "RECON_paper/manuscript/revision-authority-round1c"
BASE = PROJ / "RECON_paper/manuscript/15_DRAFT_v3.md"; MANIFEST = PROJ / "RECON_paper/manuscript/15_DRAFT_v3.md.block-manifest.json"
EVENT = ROOT / "author_event_20261031c.txt"
base_raw = BASE.read_bytes(); manifest_raw = MANIFEST.read_bytes()
assert bytes_hash(base_raw).startswith("aed5252125fd"), bytes_hash(base_raw)
def raw(v): return (json.dumps(v, ensure_ascii=False, sort_keys=True, separators=(",", ":")) + "\n").encode("utf-8")
COMP = "Journal-Fit seat (EIC) carrying the strict citation-check's claim–source context findings (16_CITATION_AUDIT_v3.md §5, confirmed by the session model against the PubMed abstracts / PMC full text on 2026-10-31)"
def item(n, sc, desc, blocks, anchor_block, quote, obl, sev, code, verify, action, kind="sentence"):
    return dict(id=f"REV-M1c-{n}", source_refs=[{"seat": "EIC", "channel": "editorial", "ordinal": n + 1, "subclaim_ordinal": 0}], reviewer="EIC",
        description=f"{sc}: {desc}", sub_claim_ids=[sc], obligation_class=obl, severity=sev,
        evidence_anchor={"anchor_type": "text", "locator": anchor_block, "quote": quote}, confidence=5, corroborating_sources=[],
        cost_scope={"kind": kind, "locator": ", ".join(blocks)}, consequence_if_unaddressed={"code": code, "target": {"kind": "manuscript", "locator": ", ".join(blocks)}},
        target_section=", ".join(blocks), suggested_action=action, consensus_level="SINGLE-VERIFIER", verification_criteria=verify,
        proposed_targets=[{"block_id": b, "allowed_operations": ["replace_block"]} for b in sorted(blocks)], competence_basis=COMP)
items = [
 item(1, "SC-E1", "Audit flag E1. B0014 says the dual-branch reconstructor (Wang 2024) and the multi-branch network (Yu 2024a) 'all sit downstream of a reconstruction operator'; Yu 2024a's SA-HFL reconstructs conductivity from the measurement voltages and its aim is high-resolution reconstruction with robustness to measurement noise and modelling errors, not noise tolerance alone. Restrict 'downstream' to the branch tested here and the post-processing networks; describe Yu 2024a as the abstract does.",
      ["B0014"], "B0014", "All sit downstream of a reconstruction operator, as do the post-processing networks for EIT", "must_fix", "minor", "claim_scope_unsupported",
      "B0014 no longer places the Wang 2024 and Yu 2024a networks downstream of a reconstruction operator; Yu 2024a is described as reconstructing from voltages with branches fused for robustness to noise and modelling errors; the citation anchor quotes the abstract.", "Rewrite the two clauses; re-anchor Yu 2024a on its abstract."),
 item(2, "SC-E2", "Audit flag E2. B0013 attributes the quoted plan to the semi-Siamese study's 'conclusions' and says it names 'GREIT, Gauss–Newton and back-projection'; the sentence is in the Discussion and names the Sheffield back-projection algorithm, a FEM-based linearised Newton–Raphson algorithm and GREIT. Correct both; state that one-step Gauss–Newton is this study's linearised Newton–Raphson member; align B0024 'those the original study named'.",
      ["B0013", "B0024"], "B0013", "The semi-Siamese study's conclusions state that", "must_fix", "minor", "reader_traceability_reduced",
      "B0013 says 'discussion', names the three algorithms as the source does and states the Gauss–Newton correspondence; B0024 carries the same correspondence.", "Correct section and algorithm names in B0013; add the correspondence clause in B0024."),
 item(3, "SC-E3E4", "Audit flags E3 and E4 plus a consistency slip. B0074: 'Dice 0.89 to 0.60' is not a pair Yan 2020 reports (89.7→68.7, 90.6→59.5, 89.2→64.1); AlBadawy 2018's '0.59 to 0.68' are post-shift values, the losses being about 4 and 17 points from 0.72 and 0.76, so 'of that order' overstates the match with 16–62 points; and '19 to 33' contradicts the '19 to 34' of the Abstract, 3.2, 4.1 and 4.2.",
      ["B0074"], "B0074", "fell from Dice 0.89 to 0.60 when the MRI manufacturer changed", "must_fix", "minor", "claim_scope_unsupported",
      "B0074 reports Yan 2020 as a 21–31-point fall from 0.89–0.91 to 0.60–0.69, AlBadawy 2018 as losses of 4 and 17 points from 0.72 and 0.76 to 0.68 and 0.59, compares the 16–62 and 19–34 points to that range without 'of that order', and reads '19 to 34'; anchors quote the abstracts.", "Rewrite the comparison sentence with the abstracts' numbers."),
 item(4, "SC-E5", "Audit flag E5. B0011 says the clinical parameters derived from twelve reconstructions 'were close'; Grychtol 2014a restricts this to 'among the advanced algorithms' and says some algorithms are significantly worse.",
      ["B0011"], "B0011", "while the clinical parameters derived from them were close", "should_fix", "minor", "claim_scope_unsupported",
      "B0011 carries the restriction 'did not vary considerably among the advanced algorithms' and the anchor quotes that abstract sentence.", "Add the restriction; re-anchor."),
 item(5, "SC-E6", "Audit flag E6. The 1.1 heading (B0010) and the topic sentence of B0011 say the indices are 'insensitive' to the reconstructor, reading two non-significant comparisons as equivalence, which Section 4.2 (B0069) says non-significance cannot establish. Reword heading and sentence as 'have not been found to depend on' / 'did not depend detectably on … in the studies that compared reconstructors'.",
      ["B0010", "B0011"], "B0010", "Clinical indices are insensitive to the reconstructor; a pixel-level network is not", "should_fix", "minor", "internal_inconsistency" if False else "interpretive_ambiguity_remains",
      "Neither B0010 nor B0011 uses 'insensitive' for the indices; the wording states what the studies found (no detected dependence) rather than equivalence.", "Reword heading and topic sentence.", kind="section"),
]
items.sort(key=lambda it: (_source_key(it["source_refs"][0]), it["id"]))
counts = {k: sum(1 for i in items if i["obligation_class"] == k) for k in ("must_fix", "should_fix", "consider")}
roadmap = {"schema_version": "revision-roadmap/1.0", "revision_round": 3, "base_draft_sha256": bytes_hash(base_raw), "block_manifest_sha256": bytes_hash(manifest_raw),
    "items": items, "total_items": len(items), "obligation_counts": counts, "editorial_decision": "Major Revision",
    "consensus_summary": "Round 1c (author-side interim round, 2026-10-31 evening): the strict citation-check of v3 (16_CITATION_AUDIT_v3.md, PASS WITH FLAGS) found six claim–source context flags E1–E6, all confirmed by the session model against the sources; plus one '19 to 33'/'19 to 34' slip. Wording and anchors only; no number of this study, verdict, hash, fixed sentence or scope rule changes. The panel's round-1 decision Major Revision remains the decision in force until the re-review.",
    "dissenting_opinions": []}
roadmap_raw = raw(roadmap); (ROOT / "roadmap.json").write_bytes(roadmap_raw)
cs = {"schema_version": "claim-surface-manifest/1.0", "revision_round": 3, "roadmap_sha256": bytes_hash(roadmap_raw), "base_draft_sha256": bytes_hash(base_raw), "claim_intent_sources": [], "surfaces": []}
(ROOT / "claim-surface-manifest.json").write_bytes(raw(cs))
event = "AUTHOR-EVENT-PI-recon-tier3-round1c-2026-10-31"
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
    r = subprocess.run(cli + args, capture_output=True, text=True); print(args[0], "rc=", r.returncode, (r.stdout + r.stderr).strip()[-700:])
    if r.returncode: sys.exit(1)
