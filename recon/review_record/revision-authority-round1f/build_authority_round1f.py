# -*- coding: utf-8 -*-
"""Revision-authority artefacts for round 1f (2026-10-31 late evening): reference-list metadata (16_ §10 items 11-12, 21_ flag F1).
Base 20_DRAFT_v6.md (ab11b87add5c, 160 blocks). EIC editorial channel (1c precedent), ordinals 4-5."""
import json, subprocess, sys
from pathlib import Path
PROJ = Path("/Users/yfko/Library/Mobile Documents/com~apple~CloudDocs/Documents/New idea/SunetBeta_the importance-of-divided-branch-structure")
S = Path.home() / ".claude/plugins/cache/academic-research-skills/academic-research-skills/3.23.0/scripts"
sys.path.insert(0, str(S.parent))
from scripts.revision_roadmap import bytes_hash, _source_key  # noqa
ROOT = PROJ / "RECON_paper/manuscript/revision-authority-round1f"
BASE = PROJ / "RECON_paper/manuscript/20_DRAFT_v6.md"; MANIFEST = PROJ / "RECON_paper/manuscript/20_DRAFT_v6.md.block-manifest.json"
EVENT = ROOT / "author_event_20261031f.txt"
base_raw = BASE.read_bytes(); manifest_raw = MANIFEST.read_bytes()
assert bytes_hash(base_raw).startswith("ab11b87add5c"), bytes_hash(base_raw)
def raw(v): return (json.dumps(v, ensure_ascii=False, sort_keys=True, separators=(",", ":")) + "\n").encode("utf-8")
COMP = "Journal-Fit seat (EIC) carrying the citation audit's metadata/format items (16_CITATION_AUDIT_v3.md §1 F1-F11, §10 items 11-12) and the scoped re-check's flag F1 (21_CITATION_RECHECK_v6.md); PI instruction of 2026-10-31 (format-convert step)"
def item(n, ordinal, sc, desc, blocks, anchor_block, quote, verify, action):
    return dict(id=f"REV-M1f-{n}", source_refs=[{"seat": "EIC", "channel": "editorial", "ordinal": ordinal, "subclaim_ordinal": 0}], reviewer="EIC",
        description=f"{sc}: {desc}", sub_claim_ids=[sc], obligation_class="should_fix", severity="minor",
        evidence_anchor={"anchor_type": "text", "locator": anchor_block, "quote": quote}, confidence=5, corroborating_sources=[],
        cost_scope={"kind": "section", "locator": ", ".join(blocks)}, consequence_if_unaddressed={"code": "reporting_requirement_unmet", "target": {"kind": "manuscript", "locator": ", ".join(blocks)}},
        target_section=", ".join(blocks), suggested_action=action, consensus_level="SINGLE-VERIFIER", verification_criteria=verify,
        proposed_targets=[{"block_id": b, "allowed_operations": ["replace_block"]} for b in sorted(blocks)], competence_basis=COMP)
items = [
 item(1, 4, "SC-F1", "Reference-list metadata (16_ §1 F1/F2/F3/F5/F6/F7/F8): the Vancouver strings in B0092 carry Crossref short titles instead of NLM abbreviations for the non-PubMed containers, a doubled full stop (Wang 2024), '?.' after question-mark titles, no LNCS volume for Karani 2018, 'doi:' without the PLoS space, online instead of issue years for Chambers and Du, and unverified name forms (Genderingen HRv, Palma ND, Boulesteix A). Regenerate B0092 from the re-rendered registry (refs/prior_works_recon_strings.md, 2026-10-31, overrides applied) in the same first-citation order.",
      ["B0092"], "B0092", "Lecture Notes in Computer Science. 2018:476-484. doi:10.1007/978-3-030-00928-1_54", 
      "Every line of B0092 equals tools/cite.render_vancouver of the registry entry (overrides applied) for the key in that position; the key order is unchanged (72 keys, order of first citation); the changed lines are exactly the keys named in refs/overrides.json's 2026-10-31 entries plus the two global renderer changes (doi: with a space; no '.' after '?').", "Regenerate the list."),
 item(2, 5, "SC-F1b", "21_CITATION_RECHECK_v6.md flag F1: the bracket above the reference list (B0091) dates the generated strings '2026-10-17' and gives the registry size as 73; the strings were re-rendered on 2026-10-31 from 72 entries.",
      ["B0091"], "B0091", "refs/prior_works_recon_strings.md`, 2026-10-17", "B0091 names the 2026-10-31 render and the overrides file; no other text changes.", "Update the bracket."),
]
items.sort(key=lambda it: (_source_key(it["source_refs"][0]), it["id"]))
counts = {k: sum(1 for i in items if i["obligation_class"] == k) for k in ("must_fix", "should_fix", "consider")}
roadmap = {"schema_version": "revision-roadmap/1.0", "revision_round": 6, "base_draft_sha256": bytes_hash(base_raw), "block_manifest_sha256": bytes_hash(manifest_raw),
    "items": items, "total_items": len(items), "obligation_counts": counts, "editorial_decision": "Minor Revision",
    "consensus_summary": "Round 1f (2026-10-31 late evening): reference-list metadata only — NLM abbreviations, LNCS volume, issue years, author name forms, PLoS 'doi: ' form, no '?.'; the bracket above the list updated. No sentence, table, number, verdict or fixed reading changes.",
    "dissenting_opinions": []}
roadmap_raw = raw(roadmap); (ROOT / "roadmap.json").write_bytes(roadmap_raw)
cs = {"schema_version": "claim-surface-manifest/1.0", "revision_round": 6, "roadmap_sha256": bytes_hash(roadmap_raw), "base_draft_sha256": bytes_hash(base_raw), "claim_intent_sources": [], "surfaces": []}
(ROOT / "claim-surface-manifest.json").write_bytes(raw(cs))
event = "AUTHOR-EVENT-PI-recon-tier3-round1f-2026-10-31"
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
    r = subprocess.run(cli + args, capture_output=True, text=True); print(args[0], "rc=", r.returncode, (r.stdout + r.stderr).strip()[-300:])
    if r.returncode: sys.exit(1)
