# -*- coding: utf-8 -*-
"""Revision-authority artefacts (#670) for the RECON tier-3 manuscript, round 1b (2026-10-31 evening, Fable 5.1).
Base: 13_DRAFT_v2.md (159791522c60, 160 blocks). Author event: author_event_20261031b.txt (the PI's length decision
and the two source checks). Three items: Abstract back to <=300 words (EIC editorial channel, PLoS One conformance);
REV-M1-26 and REV-M1-27 follow-ups now that Pulletz 2006 and Zhao 2014 were checked against their PubMed records."""
import json, subprocess, sys
from pathlib import Path
PROJ = Path("/Users/yfko/Library/Mobile Documents/com~apple~CloudDocs/Documents/New idea/SunetBeta_the importance-of-divided-branch-structure")
S = Path.home() / ".claude/plugins/cache/academic-research-skills/academic-research-skills/3.23.0/scripts"
sys.path.insert(0, str(S.parent))
from scripts.revision_roadmap import bytes_hash, _source_key  # noqa
ROOT = PROJ / "RECON_paper/manuscript/revision-authority-round1b"
BASE = PROJ / "RECON_paper/manuscript/13_DRAFT_v2.md"; MANIFEST = PROJ / "RECON_paper/manuscript/13_DRAFT_v2.md.block-manifest.json"
EVENT = ROOT / "author_event_20261031b.txt"
base_raw = BASE.read_bytes(); manifest_raw = MANIFEST.read_bytes()
assert bytes_hash(base_raw).startswith("159791522c60"), bytes_hash(base_raw)
def raw(v): return (json.dumps(v, ensure_ascii=False, sort_keys=True, separators=(",", ":")) + "\n").encode("utf-8")
EIC = "Journal-Fit seat of the 2026-10-31 manuscript panel (PLoS One academic-editor identity); PLoS One submission guideline 'Abstract: not exceed 300 words' (refs/01_JOURNAL_REQUIREMENTS_PLOSONE.md)"
R2 = "Domain seat (EIDORS thoracic EIT reconstruction) of the 2026-10-31 manuscript panel; follow-up closed by the author's check of the cited paper's PubMed record on 2026-10-31"
items = [
 dict(id="REV-M1b-1", source_refs=[{"seat": "EIC", "channel": "editorial", "ordinal": 1, "subclaim_ordinal": 0}], reviewer="EIC",
      description="SC-E1: The Abstract of 13_DRAFT_v2.md runs to 331 words after the round-1 standing labels and confound clause were added; PLoS One requires at most 300 words. Cut it to 300 or fewer without removing any number, standing label (registered / addendum / exploratory / descriptive / tested) or the confound clause that round 1 added (REV-M1-1, -2, -4, -12, -18, -21, -22).",
      sub_claim_ids=["SC-E1"], obligation_class="must_fix", severity="major",
      evidence_anchor={"anchor_type": "text", "locator": "B0006", "quote": "Post-reconstruction networks for lung electrical impedance tomography (EIT) inherit the reconstructor they were trained on"},
      confidence=5, corroborating_sources=[], cost_scope={"kind": "sentence", "locator": "B0006 (Abstract), wording only"},
      consequence_if_unaddressed={"code": "editorial_conformance_unmet", "target": {"kind": "manuscript", "locator": "B0006"}},
      target_section="B0006", suggested_action="Shorten the Abstract to at most 300 words by tightening phrasing; keep every quantity and every standing label.",
      consensus_level="SINGLE-VERIFIER",
      verification_criteria="tools/check_recon_draft.py reports the Abstract at 300 words or fewer; every number and standing label present in the v2 Abstract is present in the revised one (checked by listing the numeric tokens of both versions).",
      proposed_targets=[{"block_id": "B0006", "allowed_operations": ["replace_block"]}], competence_basis=EIC),
 dict(id="REV-M1b-2", source_refs=[{"seat": "R2", "channel": "finding", "ordinal": 8, "subclaim_ordinal": 1}], reviewer="R2",
      description="SC-26: Follow-up of REV-M1-26. The PubMed record of Pulletz et al. (2006) states that the recommended ROI contour is '20-35% of the maximum standard deviation or regression coefficient', a band defined on pixel statistics, not a single 25% applied to a reconstructed amplitude. Replace the round-1 hedge in B0030 with that exact statement and say that the registered 25% lies inside the band.",
      sub_claim_ids=["SC-26"], obligation_class="should_fix", severity="minor",
      evidence_anchor={"anchor_type": "text", "locator": "B0030", "quote": "a threshold of the kind clinical region-of-interest methods apply to EIT images (Pulletz et al., 2006)"},
      confidence=5, corroborating_sources=[], cost_scope={"kind": "sentence", "locator": "B0030 (Section 2.3), one sentence and its anchor"},
      consequence_if_unaddressed={"code": "reader_traceability_reduced", "target": {"kind": "manuscript", "locator": "B0030"}},
      target_section="B0030", suggested_action="State the 20-35% band, its definition on pixel statistics, and that 25% lies inside it; anchor the citation on the abstract sentence that carries the band.",
      consensus_level="SINGLE-VERIFIER",
      verification_criteria="B0030 names the 20-35% band and its definition exactly as the Pulletz 2006 abstract gives it, states that the registered 25% lies inside it, and the citation anchor quotes that abstract sentence.",
      proposed_targets=[{"block_id": "B0030", "allowed_operations": ["replace_block"]}], competence_basis=R2),
 dict(id="REV-M1b-3", source_refs=[{"seat": "R2", "channel": "finding", "ordinal": 9, "subclaim_ordinal": 1}], reviewer="R2",
      description="SC-27: Follow-up of REV-M1-27. The PubMed record of Zhao et al. (2014) states 'No significant differences were found in all examined indices among the four reconstruction algorithms (p > 0.2, Kruskal-Wallis test)'; the per-index statement holds for all five indices. Replace the round-1 hedge ('as that study reports it') in B0011 with the exact statement and its test.",
      sub_claim_ids=["SC-27"], obligation_class="should_fix", severity="minor",
      evidence_anchor={"anchor_type": "text", "locator": "B0011", "quote": "gave five ventilation indices with no statistically significant difference between algorithms, as that study reports it (Zhao et al., 2014)"},
      confidence=5, corroborating_sources=[], cost_scope={"kind": "sentence", "locator": "B0011 (Section 1.1), one clause and its anchor"},
      consequence_if_unaddressed={"code": "reader_traceability_reduced", "target": {"kind": "manuscript", "locator": "B0011"}},
      target_section="B0011", suggested_action="State that no index differed significantly across the four algorithms (p > 0.2, Kruskal-Wallis) and anchor the citation on that abstract sentence.",
      consensus_level="SINGLE-VERIFIER",
      verification_criteria="B0011 states the per-index result with the test and p bound exactly as the Zhao 2014 abstract gives it, and the citation anchor quotes that sentence.",
      proposed_targets=[{"block_id": "B0011", "allowed_operations": ["replace_block"]}], competence_basis=R2),
]
items.sort(key=lambda it: (_source_key(it["source_refs"][0]), it["id"]))
counts = {k: sum(1 for i in items if i["obligation_class"] == k) for k in ("must_fix", "should_fix", "consider")}
roadmap = {"schema_version": "revision-roadmap/1.0", "revision_round": 2, "base_draft_sha256": bytes_hash(base_raw), "block_manifest_sha256": bytes_hash(manifest_raw),
    "items": items, "total_items": 3, "obligation_counts": counts, "editorial_decision": "Major Revision",
    "consensus_summary": "Round 1b (author-side interim round between the round-1 patch and the scoped re-review; the panel's round-1 decision Major Revision remains the decision in force). One editorial-conformance item (Abstract length, PLoS One <=300 words) raised by the round-1 patch itself, and two follow-ups that close REV-M1-26 and REV-M1-27 now that the PI-delegated source checks were done against the papers' PubMed records (author_event_20261031b.txt). No new reviewer finding; no data, verdict or rule touched.",
    "dissenting_opinions": []}
roadmap_raw = raw(roadmap); (ROOT / "roadmap.json").write_bytes(roadmap_raw)
cs = {"schema_version": "claim-surface-manifest/1.0", "revision_round": 2, "roadmap_sha256": bytes_hash(roadmap_raw), "base_draft_sha256": bytes_hash(base_raw), "claim_intent_sources": [], "surfaces": []}
(ROOT / "claim-surface-manifest.json").write_bytes(raw(cs))
event = "AUTHOR-EVENT-PI-recon-tier3-round1b-2026-10-31"
adj = [{"item_id": it["id"], "author_event_id": event, "author_triage": "will_address", "authorized_targets": it["proposed_targets"], "claim_strength_authorizations": []} for it in items]
choices = {"schema_version": "author-adjudication-input/1.0",
    "author_events": [{"event_id": event, "source": "explicit_session_user_message", "actor_role": "author", "input_sha256": bytes_hash(EVENT.read_bytes())}],
    "display_order": {"mode": "source_traceability", "item_ids": [i["id"] for i in items], "author_event_id": event},
    "author_adjudications": adj, "collateral_authorizations": []}
(ROOT / "author-choices.json").write_bytes(raw(choices))
if (ROOT / "author-adjudication.json").exists(): (ROOT / "author-adjudication.json").unlink()
cli = [sys.executable, str(S / "revision_roadmap.py")]; common = ["--base", str(BASE), "--block-manifest", str(MANIFEST)]
for args in (["validate-roadmap", str(ROOT / "roadmap.json")] + common,
             ["build-adjudication", str(ROOT / "roadmap.json")] + common + ["--claim-surface", str(ROOT / "claim-surface-manifest.json"), "--author-choices", str(ROOT / "author-choices.json"), "--artifact-root", str(ROOT), "--output", str(ROOT / "author-adjudication.json")],
             ["validate-adjudication", str(ROOT / "roadmap.json"), str(ROOT / "author-adjudication.json")] + common + ["--claim-surface", str(ROOT / "claim-surface-manifest.json"), "--artifact-root", str(ROOT)]):
    r = subprocess.run(cli + args, capture_output=True, text=True); print(args[0], "rc=", r.returncode, (r.stdout + r.stderr).strip()[-700:])
