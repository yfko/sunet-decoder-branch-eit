# -*- coding: utf-8 -*-
"""Revision patch 1.1, round 1f (2026-10-31): B0092 regenerated from the re-rendered registry; B0091 bracket updated."""
import json, re, sys
from pathlib import Path
PROJ = Path("/Users/yfko/Library/Mobile Documents/com~apple~CloudDocs/Documents/New idea/SunetBeta_the importance-of-divided-branch-structure")
S = Path.home() / ".claude/plugins/cache/academic-research-skills/academic-research-skills/3.23.0/scripts"
sys.path.insert(0, str(S.parent)); sys.path.insert(0, str(PROJ / "tools"))
from scripts.revision_roadmap import bytes_hash, author_decision_digest  # noqa
from cite import render_vancouver  # noqa
ROOT = PROJ / "RECON_paper/manuscript/revision-authority-round1f"
BASE = PROJ / "RECON_paper/manuscript/20_DRAFT_v6.md"; MAN = PROJ / "RECON_paper/manuscript/20_DRAFT_v6.md.block-manifest.json"
manifest = json.loads(MAN.read_text(encoding="utf-8")); H = {b["block_id"]: b["old_hash"] for b in manifest["blocks"]}; assert manifest["base_draft_hash"] == "ab11b87add5c"
txt = BASE.read_text(encoding="utf-8"); parts = re.split(r"(<!--block:(B\d{4})-->\n)", txt); BLK = {}; i = 1
while i < len(parts): BLK[parts[i + 1]] = parts[i + 2].rstrip("\n"); i += 3
reg = {e["key"]: e for e in json.load(open(PROJ / "refs/prior_works_recon.json"))}
keys = re.findall(r"<!--key:(\w+)-->", BLK["B0092"]); assert len(keys) == 72 == len(reg) and len(set(keys)) == 72
new92 = "\n".join(f"{render_vancouver(reg[k], i)} <!--key:{k}-->" for i, k in enumerate(keys, 1))
# the regenerated lines must equal the strings file's Vancouver section (same renderer, same registry)
strings = (PROJ / "refs/prior_works_recon_strings.md").read_text(); vanc = strings.split("## Vancouver")[1].split("\n## ")[0]
by_doi = {m.group(1).lower(): re.sub(r"^\d+\.\s+", "", l) for l in vanc.splitlines() if re.match(r"^\d+\.\s", l) for m in [re.search(r"doi: (\S+)$", l)] if m}
for k, line in zip(keys, new92.splitlines()):
    body = re.sub(r"^\d+\.\s+", "", line).replace(f" <!--key:{k}-->", ""); assert body == by_doi[reg[k]["doi"].lower()], k
old_lines = {re.search(r"<!--key:(\w+)-->", l).group(1): re.sub(r"^\d+\.\s+", "", l) for l in BLK["B0092"].splitlines()}
new_lines = {re.search(r"<!--key:(\w+)-->", l).group(1): re.sub(r"^\d+\.\s+", "", l) for l in new92.splitlines()}
changed = sorted(k for k in keys if old_lines[k] != new_lines[k])
ov = json.load(open(PROJ / "refs/overrides.json")); today = {k for k, o in ov.items() if o.get("verified") == "2026-10-31"}
# every changed line is either an override key of today or differs only by the two renderer changes
def norm(s): return s.replace("doi: ", "doi:").replace("?. ", "? ").replace("? ", "?. ")
only_renderer = [k for k in changed if k not in today and old_lines[k].replace("doi:", "doi: ") == new_lines[k]]
qmark = [k for k in changed if k not in today and k not in only_renderer]
for k in qmark: assert old_lines[k].replace("doi:", "doi: ").replace("?. ", "? ") == new_lines[k], (k, old_lines[k], new_lines[k])
print("changed lines:", len(changed), "| override keys today:", len([k for k in changed if k in today]), "| doi-space only:", len(only_renderer), "| doi-space + '?.':", len(qmark), qmark)
assert len(changed) == 72  # the doi form changes every line
NEW = {"B0092": new92}
b91 = BLK["B0091"]; assert "2026-10-17" in b91 and "<!--ref:" not in b91
NEW["B0091"] = b91.replace("`refs/prior_works_recon_strings.md`, 2026-10-17", "`refs/prior_works_recon_strings.md`, re-rendered 2026-10-31 with the verified metadata overrides of `refs/overrides.json`")
assert NEW["B0091"] != b91 and "2026-10-17" not in NEW["B0091"]
ops = [{"op": "replace_block", "block_id": b, "old_hash": H[b], "new_text": NEW[b], "roadmap_item_ids": [r], "claim_strength_changes": [], "collateral_authorization_ids": []} for b, r in (("B0091", "REV-M1f-2"), ("B0092", "REV-M1f-1"))]
roadmap_raw = (ROOT / "roadmap.json").read_bytes(); adj_raw = (ROOT / "author-adjudication.json").read_bytes(); cs_raw = (ROOT / "claim-surface-manifest.json").read_bytes()
patch = {"patch_format_version": "1.1", "authorization_context": "review_roadmap", "revision_round": 6, "base_draft_hash": manifest["base_draft_hash"],
         "roadmap_sha256": bytes_hash(roadmap_raw), "author_adjudication_sha256": bytes_hash(adj_raw), "author_decision_digest": author_decision_digest(json.loads(adj_raw)),
         "claim_surface_manifest_sha256": bytes_hash(cs_raw), "emitted_by": "draft_writer_agent (academic-paper format-convert / revision round 1f, patch mode, Fable 5.1, 2026-10-31)", "ops": ops}
(ROOT / "revision_patch_round1f.json").write_text(json.dumps(patch, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
print("ops:", len(ops)); print("B0091 new:", NEW["B0091"][:220])
