# -*- coding: utf-8 -*-
"""Revision patch 1.1, round 1g (2026-10-31 night): B0087 replaced by the 26_ §6.1 paragraph (read verbatim from 26_); B0153/B0154 deleted."""
import json, re, sys
from pathlib import Path
PROJ = Path("/Users/yfko/Library/Mobile Documents/com~apple~CloudDocs/Documents/New idea/SunetBeta_the importance-of-divided-branch-structure")
S = Path.home() / ".claude/plugins/cache/academic-research-skills/academic-research-skills/3.23.0/scripts"
sys.path.insert(0, str(S.parent))
from scripts.revision_roadmap import bytes_hash, author_decision_digest  # noqa
ROOT = PROJ / "RECON_paper/manuscript/revision-authority-round1g"
BASE = PROJ / "RECON_paper/manuscript/23_DRAFT_v7.md"; MAN = PROJ / "RECON_paper/manuscript/23_DRAFT_v7.md.block-manifest.json"
manifest = json.loads(MAN.read_text(encoding="utf-8")); H = {b["block_id"]: b["old_hash"] for b in manifest["blocks"]}; assert manifest["base_draft_hash"] == "d02ec9b62ff1"
txt = BASE.read_text(encoding="utf-8"); parts = re.split(r"(<!--block:(B\d{4})-->\n)", txt); BLK = {}; i = 1
while i < len(parts): BLK[parts[i + 1]] = parts[i + 2].rstrip("\n"); i += 3
# the replacement paragraph, verbatim from 26_ §6.1 (the single blockquote line in that subsection)
d26 = (PROJ / "RECON_paper/manuscript/26_DISCLOSURE_plos.md").read_text(encoding="utf-8")
sec = d26.split("**6.1 Acknowledgments")[1].split("**6.2")[0]
quotes = [l[2:].strip() for l in sec.splitlines() if l.startswith("> ")]; assert len(quotes) == 1, quotes
new87 = quotes[0]
for must in ("Fable 5.1, Opus 5 and Opus 5.5", "August to October 2026", "simulation, data-generation, training, analysis, scoring and figure code", "searched for and screened literature", "drafted the preregistration, its two addenda and the written interpretation", "took or approved every design decision", "with a separate checking script", "No image was produced by a generative image model; every figure was plotted from the result files by the code described above."):
    assert must in new87, must
assert "<!--" not in new87 and "\n" not in new87 and new87 != BLK["B0087"]
assert BLK["B0153"] == "## Funding and competing interests" and BLK["B0154"].startswith("The journal collects funding")
ops = [{"op": "replace_block", "block_id": "B0087", "old_hash": H["B0087"], "new_text": new87, "roadmap_item_ids": ["REV-M1g-1"], "claim_strength_changes": [], "collateral_authorization_ids": []},
       {"op": "delete_block", "block_id": "B0153", "old_hash": H["B0153"], "roadmap_item_ids": ["REV-M1g-2"], "claim_strength_changes": [], "collateral_authorization_ids": []},
       {"op": "delete_block", "block_id": "B0154", "old_hash": H["B0154"], "roadmap_item_ids": ["REV-M1g-2"], "claim_strength_changes": [], "collateral_authorization_ids": []}]
roadmap_raw = (ROOT / "roadmap.json").read_bytes(); adj_raw = (ROOT / "author-adjudication.json").read_bytes(); cs_raw = (ROOT / "claim-surface-manifest.json").read_bytes()
patch = {"patch_format_version": "1.1", "authorization_context": "review_roadmap", "revision_round": 7, "base_draft_hash": manifest["base_draft_hash"],
         "roadmap_sha256": bytes_hash(roadmap_raw), "author_adjudication_sha256": bytes_hash(adj_raw), "author_decision_digest": author_decision_digest(json.loads(adj_raw)),
         "claim_surface_manifest_sha256": bytes_hash(cs_raw), "emitted_by": "draft_writer_agent (academic-paper revision round 1g, patch mode, Fable 5.1, 2026-10-31)", "ops": ops}
(ROOT / "revision_patch_round1g.json").write_text(json.dumps(patch, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
print("ops:", len(ops), "| B0087 words old/new:", len(BLK["B0087"].split()), len(new87.split()))
