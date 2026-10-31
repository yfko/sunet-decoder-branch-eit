# -*- coding: utf-8 -*-
"""Revision patch 1.1 for the RECON tier-3 manuscript, round 1b (2026-10-31 evening, Fable 5.1, academic-paper revision, patch mode).
Three replace_block ops on 13_DRAFT_v2.md (159791522c60), each inside the will_address targets of
revision-authority-round1b/roadmap.json. No number changes; the Abstract is shortened, two citation sentences are made exact
against the cited papers' PubMed abstracts (quotes carried in the anchors)."""
import json, re, sys
from pathlib import Path
PROJ = Path("/Users/yfko/Library/Mobile Documents/com~apple~CloudDocs/Documents/New idea/SunetBeta_the importance-of-divided-branch-structure")
S = Path.home() / ".claude/plugins/cache/academic-research-skills/academic-research-skills/3.23.0/scripts"
sys.path.insert(0, str(S.parent))
from scripts.revision_roadmap import bytes_hash, author_decision_digest  # noqa
ROOT = PROJ / "RECON_paper/manuscript/revision-authority-round1b"
BASE = PROJ / "RECON_paper/manuscript/13_DRAFT_v2.md"; MAN = PROJ / "RECON_paper/manuscript/13_DRAFT_v2.md.block-manifest.json"
manifest = json.loads(MAN.read_text(encoding="utf-8")); H = {b["block_id"]: b["old_hash"] for b in manifest["blocks"]}
txt = BASE.read_text(encoding="utf-8"); parts = re.split(r"(<!--block:(B\d{4})-->\n)", txt); BLK = {}; i = 1
while i < len(parts): BLK[parts[i + 1]] = parts[i + 2].rstrip("\n"); i += 3
def sub(bid, old, new):
    t = NEW.get(bid, BLK[bid]); assert t.count(old) == 1, (bid, old[:60], t.count(old)); NEW[bid] = t.replace(old, new)
def words(s): return len(re.sub(r"<!--[^>]*-->", "", s).split())
NEW = {}; R = {}

# ---------------- Abstract (REV-M1b-1): 333 -> <=300 words, every number and standing label kept
NEW["B0006"] = ("**Abstract** — Post-reconstruction networks for lung electrical impedance tomography (EIT) inherit their training reconstructor; whether a decoder branch for the weak cardiac component still helps under another conventional reconstructor was left open by the proposing study. "
 "We preregistered a parameter-matched comparison of a two-decoder network with a widened single-decoder control on simulated 16-electrode lung EIT at 20 dB under GREIT, one-step Gauss–Newton and back-projection, scored by heart-channel Dice against each reconstructor's own heart image. "
 "Under matched training the branch stayed below the registered floor on Gauss–Newton and back-projection (+0.32 and +0.63 Dice points against floors of 0.45 and 0.66; registered); the re-scored GREIT reference showed the same pattern. "
 "The registered transfer hypothesis (reconstructor change, no retraining) was falsified in all six cells, and in the two in-range cells the branch's advantage showed no evidence of growing; exploratory re-scoring put the cost of not retraining at 19 to 34 points. "
 "The registered pooled row, under one global normalisation, collapsed on the two reconstructors two orders of magnitude weaker in amplitude. In a post-unblinding, pre-hashed addendum with per-source affines, pooled training was, descriptively, never worse than retraining on the deployed reconstructor by over 0.3 points (−0.08 to +0.36; two of six intervals favoured pooling, confounded with threefold optimisation steps). "
 "In a second addendum, leaving one reconstructor out of the pool cost it 62, 16 and 36 points against a pre-fixed ±1.0-point margin (an upper bound: the reference moves with the reconstructor), falsified in all three cells; the branch's difference there reversed sign. "
 "On exploratory, descriptive and tested evidence respectively, the reconstructor behaves as a domain: the remedy is in the training data, not this branch, and pooling's benefit stops at the pool boundary for the three reconstructors tested. Every tested verdict followed a rule fixed before its data were read.")
R["B0006"] = ["REV-M1b-1"]
nums = lambda s: re.findall(r"[−+]?\d+(?:\.\d+)?", re.sub(r"<!--[^>]*-->", "", s))
assert sorted(nums(BLK["B0006"])) == sorted(nums(NEW["B0006"])), (sorted(nums(BLK["B0006"])), sorted(nums(NEW["B0006"])))
for lab in ("registered", "exploratory", "addendum", "descriptively", "tested", "confounded"):
    assert lab in NEW["B0006"], lab
print("abstract words:", words(BLK["B0006"]), "->", words(NEW["B0006"]))
assert words(NEW["B0006"]) <= 300

# ---------------- 1.1 Zhao per-index result (REV-M1b-3)
sub("B0011", "gave five ventilation indices with no statistically significant difference between algorithms, as that study reports it (Zhao et al., 2014) <!--ref:Zhao2014PhysiolMeas--><!--anchor:quote:influence%20of%20image%20reconstruction%20algorithms%20on%20linear%20thorax%20EIT%20image%20analysis%20of%20ventilation-->",
    "gave five ventilation indices none of which differed significantly between algorithms (p > 0.2, Kruskal–Wallis) (Zhao et al., 2014) <!--ref:Zhao2014PhysiolMeas--><!--anchor:quote:No%20significant%20differences%20were%20found%20in%20all%20examined%20indices%20among%20the%20four%20reconstruction%20algorithms-->")
R["B0011"] = ["REV-M1b-3"]

# ---------------- 2.3 Pulletz threshold band (REV-M1b-2)
sub("B0030", "the region above one quarter of the image's peak, a threshold of the kind clinical region-of-interest methods apply to EIT images (Pulletz et al., 2006) <!--ref:Pulletz2006ROI--><!--anchor:quote:define%20regions%20of%20interest%20for%20evaluation%20of%20regional%20lung%20ventilation-->, computed",
    "the region above one quarter of the image's peak; the registered 25% lies inside the 20–35% band that clinical region-of-interest methods recommend for functional EIT images, where the band is defined on per-pixel statistics rather than on a reconstructed amplitude (Pulletz et al., 2006) <!--ref:Pulletz2006ROI--><!--anchor:quote:20-35%25%20of%20the%20maximum%20standard%20deviation%20or%20regression%20coefficient-->. The endpoint is computed")
R["B0030"] = ["REV-M1b-2"]

ops = [{"op": "replace_block", "block_id": b, "old_hash": H[b], "new_text": NEW[b], "roadmap_item_ids": R[b], "claim_strength_changes": [], "collateral_authorization_ids": []} for b in sorted(NEW)]
roadmap_raw = (ROOT / "roadmap.json").read_bytes(); adj_raw = (ROOT / "author-adjudication.json").read_bytes(); cs_raw = (ROOT / "claim-surface-manifest.json").read_bytes()
adj = json.loads(adj_raw)
patch = {"patch_format_version": "1.1", "authorization_context": "review_roadmap", "revision_round": 2, "base_draft_hash": manifest["base_draft_hash"],
         "roadmap_sha256": bytes_hash(roadmap_raw), "author_adjudication_sha256": bytes_hash(adj_raw), "author_decision_digest": author_decision_digest(adj),
         "claim_surface_manifest_sha256": bytes_hash(cs_raw), "emitted_by": "draft_writer_agent (academic-paper revision round 1b, patch mode, Fable 5.1, 2026-10-31)", "ops": ops}
(ROOT / "revision_patch_round1b.json").write_text(json.dumps(patch, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
print("ops:", len(ops))
