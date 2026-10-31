# -*- coding: utf-8 -*-
"""Revision patch 1.1, round 1c (2026-10-31 evening, Fable 5.1, academic-paper revision, patch mode): the six citation-context
flags of 16_CITATION_AUDIT_v3.md and the '19 to 33' slip. Base 15_DRAFT_v3.md (aed5252125fd). Literature numbers are copied from
the source abstracts (PubMed, 2026-10-31); no number of this study changes."""
import json, re, sys
from pathlib import Path
PROJ = Path("/Users/yfko/Library/Mobile Documents/com~apple~CloudDocs/Documents/New idea/SunetBeta_the importance-of-divided-branch-structure")
S = Path.home() / ".claude/plugins/cache/academic-research-skills/academic-research-skills/3.23.0/scripts"
sys.path.insert(0, str(S.parent))
from scripts.revision_roadmap import bytes_hash, author_decision_digest  # noqa
ROOT = PROJ / "RECON_paper/manuscript/revision-authority-round1c"
BASE = PROJ / "RECON_paper/manuscript/15_DRAFT_v3.md"; MAN = PROJ / "RECON_paper/manuscript/15_DRAFT_v3.md.block-manifest.json"
manifest = json.loads(MAN.read_text(encoding="utf-8")); H = {b["block_id"]: b["old_hash"] for b in manifest["blocks"]}
txt = BASE.read_text(encoding="utf-8"); parts = re.split(r"(<!--block:(B\d{4})-->\n)", txt); BLK = {}; i = 1
while i < len(parts): BLK[parts[i + 1]] = parts[i + 2].rstrip("\n"); i += 3
NEW = {}; R = {}
def sub(bid, old, new):
    t = NEW.get(bid, BLK[bid]); assert t.count(old) == 1, (bid, old[:70], t.count(old)); NEW[bid] = t.replace(old, new)
def add(bid, *ids): R[bid] = sorted(set(R.get(bid, [])) | set(ids))

# E6 — heading and topic sentence
NEW["B0010"] = "### 1.1 Clinical indices have not been found to depend on the reconstructor; a pixel-level network does"; add("B0010", "REV-M1c-5")
sub("B0011", "Those indices are insensitive to which linear reconstructor produced the image:", "Where reconstructors were compared, those indices did not depend detectably on which linear reconstructor produced the image:"); add("B0011", "REV-M1c-5")
# E5 — Grychtol restriction + anchor
sub("B0011", "while the clinical parameters derived from them were close (Grychtol et al., 2014a) <!--ref:Grychtol2014PLOSONE--><!--anchor:quote:Functional%20Validation%20and%20Comparison%20Framework%20for%20EIT%20Lung%20Imaging-->",
    "while the clinical parameters derived from them did not vary considerably among the advanced algorithms (Grychtol et al., 2014a) <!--ref:Grychtol2014PLOSONE--><!--anchor:quote:clinically%20relevant%20parameters%20do%20not%20vary%20considerably%20among%20the%20advanced%20algorithms-->"); add("B0011", "REV-M1c-4")
# E2 — section and algorithm names; B0024 correspondence
sub("B0013", "The semi-Siamese study's conclusions state that \"the separation effect of the EIT image obtained by the different reconstruction algorithms will be investigated\" (Ko and Cheng, 2021b) <!--ref:Ko2021PLOSONE--><!--anchor:quote:the%20separation%20effect%20of%20the%20EIT%20image%20obtained%20by%20the%20different%20reconstruction%20algorithms%20will%20be%20investigated-->, naming GREIT, Gauss–Newton and back-projection; this paper answers it.",
    "The semi-Siamese study's discussion states that \"the separation effect of the EIT image obtained by the different reconstruction algorithms will be investigated\" (Ko and Cheng, 2021b) <!--ref:Ko2021PLOSONE--><!--anchor:quote:the%20separation%20effect%20of%20the%20EIT%20image%20obtained%20by%20the%20different%20reconstruction%20algorithms%20will%20be%20investigated-->, naming the Sheffield back-projection algorithm, a finite-element linearised Newton–Raphson algorithm and GREIT; this paper answers it, with one-step Gauss–Newton as its linearised Newton–Raphson member."); add("B0013", "REV-M1c-2")
sub("B0024", "The three reconstructors are those the original study named, each at one fixed setting;", "The three reconstructors are those the original study named (Section 1.2; Gauss–Newton stands for its linearised Newton–Raphson), each at one fixed setting;"); add("B0024", "REV-M1c-2")
# E1 — Yu 2024a / downstream
sub("B0014", "with EIT relatives in a dual-branch reconstructor (Wang et al., 2024) <!--ref:Wang2024TIM--><!--anchor:quote:Dual-Branch%20U-Net%20Based%20on%20Deformable%20Convolution%20and%20Hyper-Convolution--> and a multi-branch network built for noise tolerance (Yu et al., 2024a) <!--ref:Yu2024CMPB--><!--anchor:quote:structure-aware%20hybrid-fusion%20learning-->. All sit downstream of a reconstruction operator, as do the post-processing networks for EIT",
    "with EIT relatives among reconstructors: a dual-branch reconstructor (Wang et al., 2024) <!--ref:Wang2024TIM--><!--anchor:quote:Dual-Branch%20U-Net%20Based%20on%20Deformable%20Convolution%20and%20Hyper-Convolution--> and a multi-branch network that reconstructs conductivity from the measured voltages, its branches fused to resist measurement noise and modelling errors (Yu et al., 2024a) <!--ref:Yu2024CMPB--><!--anchor:quote:enhance%20the%20robustness%20against%20the%20measurement%20noise%20and%20modeling%20errors-->. The branch tested here sits downstream of a reconstruction operator, as do the post-processing networks for EIT"); add("B0014", "REV-M1c-1")
# E3/E4 + 19 to 34
sub("B0074", "a left-ventricle segmentation network that fell from Dice 0.89 to 0.60 when the MRI manufacturer changed (Yan et al., 2020) <!--ref:Yan2020RadiolAI--><!--anchor:quote:MRI%20Manufacturer%20Shift%20and%20Adaptation--> and cross-institutional tumour segmentation at 0.59 to 0.68 (AlBadawy et al., 2018) <!--ref:AlBadawy2018MedPhys--><!--anchor:quote:cross-institutional%20training%20and%20testing-->; the 16 to 62 points lost here and the exploratory 19 to 33 points are of that order, but",
    "a left-ventricle segmentation network that fell by 21 to 31 Dice points, from 0.89–0.91 to 0.60–0.69, when the MRI manufacturer changed (Yan et al., 2020) <!--ref:Yan2020RadiolAI--><!--anchor:quote:Dice%20reduced%20from%2089.7%25--> and cross-institutional tumour segmentation that lost 4 and 17 points, from 0.72 and 0.76 to 0.68 and 0.59 (AlBadawy et al., 2018) <!--ref:AlBadawy2018MedPhys--><!--anchor:quote:dice%20coefficients%3A%200.68%20%C2%B1%200.19%20and%200.59%20%C2%B1%200.19-->; the 16 to 62 points lost here and the exploratory 19 to 34 points start where that range ends, but"); add("B0074", "REV-M1c-3")
ops = [{"op": "replace_block", "block_id": b, "old_hash": H[b], "new_text": NEW[b], "roadmap_item_ids": R[b], "claim_strength_changes": [], "collateral_authorization_ids": []} for b in sorted(NEW)]
roadmap_raw = (ROOT / "roadmap.json").read_bytes(); adj_raw = (ROOT / "author-adjudication.json").read_bytes(); cs_raw = (ROOT / "claim-surface-manifest.json").read_bytes()
patch = {"patch_format_version": "1.1", "authorization_context": "review_roadmap", "revision_round": 3, "base_draft_hash": manifest["base_draft_hash"],
         "roadmap_sha256": bytes_hash(roadmap_raw), "author_adjudication_sha256": bytes_hash(adj_raw), "author_decision_digest": author_decision_digest(json.loads(adj_raw)),
         "claim_surface_manifest_sha256": bytes_hash(cs_raw), "emitted_by": "draft_writer_agent (academic-paper revision round 1c, patch mode, Fable 5.1, 2026-10-31)", "ops": ops}
(ROOT / "revision_patch_round1c.json").write_text(json.dumps(patch, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
print("ops:", len(ops), sorted(NEW))
