# -*- coding: utf-8 -*-
"""Round 1h (placeholders + data-availability rewording after the PI's 2026-10-31 decisions: no Zenodo, S1 Data + GitHub).
Reads revision-authority-round1h/answers.json:
  {"tag": "<git tag>", "preprint_doi": null | "10.xxxx/...", "fig_sentence": "keep" | "revise", "month": "October" | "November",
   "pi_words": "<the PI's exact words authorising this round>"}
--dry-run: print the new block texts and word counts only. Without it: write author_event, roadmap, adjudication, patch (apply is a separate command).
Base 30_DRAFT_v8.md (9085e617e453, 158 blocks). preprint_doi != null is NOT implemented here (needs an R12d registry entry first): the script stops."""
import json, re, sys, datetime
from pathlib import Path
PROJ = Path("/Users/yfko/Library/Mobile Documents/com~apple~CloudDocs/Documents/New idea/SunetBeta_the importance-of-divided-branch-structure")
S = Path.home() / ".claude/plugins/cache/academic-research-skills/academic-research-skills/3.23.0/scripts"
sys.path.insert(0, str(S.parent))
from scripts.revision_roadmap import bytes_hash, _source_key, author_decision_digest  # noqa
ROOT = PROJ / "RECON_paper/manuscript/revision-authority-round1h"
BASE = PROJ / "RECON_paper/manuscript/30_DRAFT_v8.md"; MAN = PROJ / "RECON_paper/manuscript/30_DRAFT_v8.md.block-manifest.json"
DRY = "--dry-run" in sys.argv
A = json.loads((ROOT / ("answers.sample.json" if DRY and not (ROOT / "answers.json").exists() else "answers.json")).read_text())
assert A["fig_sentence"] in ("keep", "revise") and A["month"] in ("October", "November") and re.fullmatch(r"[\w.\-]+", A["tag"]), A
if A.get("preprint_doi"): sys.exit("preprint path not implemented: register the preprint through tools/cite.py first, then extend this script")
manifest = json.loads(MAN.read_text(encoding="utf-8")); H = {b["block_id"]: b["old_hash"] for b in manifest["blocks"]}; assert manifest["base_draft_hash"] == "9085e617e453"
base_raw = BASE.read_bytes(); assert bytes_hash(base_raw).startswith("9085e617e453")
txt = base_raw.decode("utf-8"); parts = re.split(r"(<!--block:(B\d{4})-->\n)", txt); BLK = {}; i = 1
while i < len(parts): BLK[parts[i + 1]] = parts[i + 2].rstrip("\n"); i += 3
NEW = {}
REPO = "github.com/yfko/sunet-decoder-branch-eit"
# B0042 (Methods 2.7) and B0150 (Data availability): Zenodo -> S1 Data + repository tag
head = "The minimal dataset (per-seed Dice for every cell, the aggregated results file, gate and seed-0 diagnostic files) is supplied as S1 Data, and the four preregistration states with their hash file as S1 Appendix; the same data and the data-generation, training, scoring and figure code are in the project repository ({repo}) under the tagged release {tag}."
assert BLK["B0042"].startswith("The minimal dataset (per-seed Dice for every cell") and "Zenodo" in BLK["B0042"] and BLK["B0042"].endswith("Checkpoints are available from the corresponding author; artificial-intelligence use is disclosed in the Acknowledgments.")
NEW["B0042"] = head.format(repo=REPO, tag=A["tag"]) + " Checkpoints are available from the corresponding author; artificial-intelligence use is disclosed in the Acknowledgments."
assert BLK["B0150"].endswith("Model checkpoints are available from the corresponding author.") and "Zenodo" in BLK["B0150"]
NEW["B0150"] = head.format(repo=REPO, tag=A["tag"]) + " Model checkpoints are available from the corresponding author."
# B0013 / B0089: companion preprint placeholders removed (no preprint)
g13 = " [MATERIAL GAP: preprint DOI, see Related manuscript]"; assert BLK["B0013"].endswith("declared related submissions" + g13 + ".")
NEW["B0013"] = BLK["B0013"].replace(g13, "")
g89 = re.search(r" \[MATERIAL GAP: preprint DOI, to be inserted[^\]]*\]$", BLK["B0089"]); assert g89
NEW["B0089"] = BLK["B0089"][:g89.start()]
# B0087: month and (optionally) the figure sentence (NEW-1g-1)
b87 = BLK["B0087"]; assert "accessed August to October 2026" in b87
new87 = b87.replace("accessed August to October 2026", f"accessed August to {A['month']} 2026")
if A["fig_sentence"] == "revise":
    old_fig = "every figure was plotted from the result files by the code described above."; assert b87.endswith(old_fig)
    new87 = new87.replace(old_fig, "every figure was plotted by the code described above from the data, checkpoint and result files.")
if new87 != b87: NEW["B0087"] = new87
# S1 Data caption: inserted after S1 Appendix (B0097)
S1DATA = "**S1 Data.** The minimal data set: per-seed heart- and lung-channel metrics for every cell of the design, the aggregated results and bootstrap files, the pre-read gates, the seed-0 diagnostics and the run records, with a README listing the SHA-256 of every file (zip archive)."
assert BLK["B0097"].startswith("**S1 Appendix.**")
for b, t in NEW.items(): assert "\n" not in t and "<!--block" not in t and t != BLK[b], b
print("--- new texts"); [print(f"{b} ({len(BLK[b].split())} -> {len(t.split())} words):\n  {t}\n") for b, t in NEW.items()]; print(f"insert_after B0097:\n  {S1DATA}\n")
main_old = txt.split("\n## Acknowledgments")[0]; main_new = main_old
for b in ("B0013", "B0042"): main_new = main_new.replace(BLK[b], NEW[b])
wc = lambda s: len(re.sub(r"<!--.*?-->", "", s.split("## 1. Introduction")[1]).split())
print("main text words (sections 1-5, approx. same counter as check_recon_draft):", wc(main_old), "->", wc(main_new), "(ceiling 8,000)")
gaps_left = [g for b in BLK for g in re.findall(r"\[MATERIAL GAP:[^\]]*\]", NEW.get(b, BLK[b]))]; print("placeholders left after patch:", gaps_left)
if DRY: sys.exit(0)
# ---- authority chain (1g precedent)
event_txt = f"""Author event for revision round 1h of the RECON tier-3 manuscript (RECON_paper/manuscript/30_DRAFT_v8.md, 9085e617e453), {datetime.date.today()} (Fable 5.1).

Source of authority: the PI's session messages of 2026-10-31 night — 「Zenodo 不使用 commit to github」 and 「S1 Data 加 GitHub」 (the minimal data set is supplied as Supporting Information S1 Data and, with the code, in the GitHub repository under a tagged release; no Zenodo deposit) — and the PI's answers recorded in revision-authority-round1h/answers.json: {json.dumps(A, ensure_ascii=False)}.

Decisions applied: (1) B0042 and B0150: Data availability reworded from a Zenodo deposit to S1 Data + S1 Appendix + repository release {A['tag']}; (2) B0013 and B0089: the companion-study preprint placeholders removed (no preprint; the companion remains a declared related submission with a copy attached); (3) a caption for S1 Data inserted after the S1 Appendix caption (B0097); (4) B0087: period 'August to {A['month']} 2026'; figure sentence {'revised per NEW-1g-1 (addendum_v8)' if A['fig_sentence'] == 'revise' else 'kept (PI choice; NEW-1g-1 declined)'}.
Unchanged: every other block; every number, table, verdict, fixed sentence and reference.
"""
(ROOT / f"author_event_{datetime.date.today():%Y%m%d}h.txt").write_text(event_txt, encoding="utf-8"); EVENT = ROOT / f"author_event_{datetime.date.today():%Y%m%d}h.txt"
def raw(v): return (json.dumps(v, ensure_ascii=False, sort_keys=True, separators=(",", ":")) + "\n").encode("utf-8")
COMP = "Journal-Fit seat (EIC) carrying the PLoS One submission-requirement items (refs/01: Data Availability, related-manuscript rule, placeholders; 26_/32_ P5/P6/P8) and the scoped re-verification's NEW-1g-1 (addendum_v8); PI decisions 2026-10-31 night"
def item(n, ordinal, sc, desc, targets, anchor_block, quote, verify, action):
    return dict(id=f"REV-M1h-{n}", source_refs=[{"seat": "EIC", "channel": "editorial", "ordinal": ordinal, "subclaim_ordinal": 0}], reviewer="EIC",
        description=f"{sc}: {desc}", sub_claim_ids=[sc], obligation_class="must_fix", severity="minor",
        evidence_anchor={"anchor_type": "text", "locator": anchor_block, "quote": quote}, confidence=5, corroborating_sources=[],
        cost_scope={"kind": "section", "locator": ", ".join(b for b, _ in targets)}, consequence_if_unaddressed={"code": "reporting_requirement_unmet", "target": {"kind": "manuscript", "locator": ", ".join(b for b, _ in targets)}},
        target_section=", ".join(b for b, _ in targets), suggested_action=action, consensus_level="SINGLE-VERIFIER", verification_criteria=verify,
        proposed_targets=[{"block_id": b, "allowed_operations": ops} for b, ops in sorted(targets)], competence_basis=COMP)
items = [
 item(1, 8, "SC-H1", "Data availability (P6/P8): the two statements name a Zenodo deposit with placeholders; the PI decided the minimal data set is supplied as S1 Data (SI zip) and, with the code, in the repository under a tagged release.",
      [("B0042", ["replace_block"]), ("B0150", ["replace_block"])], "B0042", "deposited on Zenodo [MATERIAL GAP: Zenodo DOI",
      f"Both statements name S1 Data, S1 Appendix, the repository {REPO} and the tag {A['tag']}; no MATERIAL GAP remains in them; the checkpoint and AI-disclosure sentences unchanged.", "Reword both statements."),
 item(2, 9, "SC-H2", "Companion preprint placeholders (P5): no preprint is posted; remove the two placeholders; the related-submission declaration stays.",
      [("B0013", ["replace_block"]), ("B0089", ["replace_block"])], "B0089", "[MATERIAL GAP: preprint DOI, to be inserted",
      "B0013 ends 'declared related submissions.'; B0089 ends '(Section 2.2).'; no other change in either block.", "Remove the placeholders."),
 item(3, 10, "SC-H3", "S1 Data needs a Supporting Information caption (PLoS: every SI file captioned in the manuscript).",
      [("B0097", ["insert_after"])], "B0097", "**S1 Appendix.** The preregistration",
      "A caption block '**S1 Data.** …' follows B0097; S-items in the deliverable are renumbered by type by format-convert.", "Insert the caption."),
]
if "B0087" in NEW:
    items.append(item(4, 11, "SC-H4", f"AI-disclosure paragraph: period to '{A['month']}'; figure sentence {'revised per NEW-1g-1' if A['fig_sentence']=='revise' else 'unchanged'}.",
      [("B0087", ["replace_block"])], "B0087", "accessed August to October 2026", f"B0087 says 'August to {A['month']} 2026'" + ("; figure sentence names data, checkpoint and result files" if A["fig_sentence"] == "revise" else "") + "; nothing else changes.", "Replace the paragraph."))
items.sort(key=lambda it: (_source_key(it["source_refs"][0]), it["id"]))
counts = {k: sum(1 for i in items if i["obligation_class"] == k) for k in ("must_fix", "should_fix", "consider")}
roadmap = {"schema_version": "revision-roadmap/1.0", "revision_round": 8, "base_draft_sha256": bytes_hash(base_raw), "block_manifest_sha256": bytes_hash(MAN.read_bytes()),
    "items": items, "total_items": len(items), "obligation_counts": counts, "editorial_decision": "Minor Revision",
    "consensus_summary": "Round 1h: placeholders and data-availability rewording (S1 Data + repository release; no Zenodo), S1 Data caption, AI-disclosure period/figure sentence. No number, table, verdict, fixed sentence or reference changes.", "dissenting_opinions": []}
roadmap_raw = raw(roadmap); (ROOT / "roadmap.json").write_bytes(roadmap_raw)
cs = {"schema_version": "claim-surface-manifest/1.0", "revision_round": 8, "roadmap_sha256": bytes_hash(roadmap_raw), "base_draft_sha256": bytes_hash(base_raw), "claim_intent_sources": [], "surfaces": []}
(ROOT / "claim-surface-manifest.json").write_bytes(raw(cs))
event = f"AUTHOR-EVENT-PI-recon-tier3-round1h-{datetime.date.today()}"
choices = {"schema_version": "author-adjudication-input/1.0", "author_events": [{"event_id": event, "source": "explicit_session_user_message", "actor_role": "author", "input_sha256": bytes_hash(EVENT.read_bytes())}],
    "display_order": {"mode": "source_traceability", "item_ids": [i["id"] for i in items], "author_event_id": event},
    "author_adjudications": [{"item_id": it["id"], "author_event_id": event, "author_triage": "will_address", "authorized_targets": it["proposed_targets"], "claim_strength_authorizations": []} for it in items], "collateral_authorizations": []}
(ROOT / "author-choices.json").write_bytes(raw(choices))
if (ROOT / "author-adjudication.json").exists(): (ROOT / "author-adjudication.json").unlink()
import subprocess
cli = [sys.executable, str(S / "revision_roadmap.py")]; common = ["--base", str(BASE), "--block-manifest", str(MAN)]
for args in (["validate-roadmap", str(ROOT / "roadmap.json")] + common,
             ["build-adjudication", str(ROOT / "roadmap.json")] + common + ["--claim-surface", str(ROOT / "claim-surface-manifest.json"), "--author-choices", str(ROOT / "author-choices.json"), "--artifact-root", str(ROOT), "--output", str(ROOT / "author-adjudication.json")],
             ["validate-adjudication", str(ROOT / "roadmap.json"), str(ROOT / "author-adjudication.json")] + common + ["--claim-surface", str(ROOT / "claim-surface-manifest.json"), "--artifact-root", str(ROOT)]):
    r = subprocess.run(cli + args, capture_output=True, text=True); print(args[0], "rc=", r.returncode, (r.stdout + r.stderr).strip()[-200:])
    if r.returncode: sys.exit(1)
rid = {"B0042": "REV-M1h-1", "B0150": "REV-M1h-1", "B0013": "REV-M1h-2", "B0089": "REV-M1h-2", "B0087": "REV-M1h-4"}
ops = [{"op": "replace_block", "block_id": b, "old_hash": H[b], "new_text": NEW[b], "roadmap_item_ids": [rid[b]], "claim_strength_changes": [], "collateral_authorization_ids": []} for b in NEW]
ops.append({"op": "insert_after", "block_id": "B0097", "old_hash": H["B0097"], "new_text": S1DATA, "roadmap_item_ids": ["REV-M1h-3"], "claim_strength_changes": [], "collateral_authorization_ids": []})
adj_raw = (ROOT / "author-adjudication.json").read_bytes(); cs_raw = (ROOT / "claim-surface-manifest.json").read_bytes()
patch = {"patch_format_version": "1.1", "authorization_context": "review_roadmap", "revision_round": 8, "base_draft_hash": manifest["base_draft_hash"],
         "roadmap_sha256": bytes_hash(roadmap_raw), "author_adjudication_sha256": bytes_hash(adj_raw), "author_decision_digest": author_decision_digest(json.loads(adj_raw)),
         "claim_surface_manifest_sha256": bytes_hash(cs_raw), "emitted_by": f"draft_writer_agent (academic-paper revision round 1h, patch mode, Fable 5.1, {datetime.date.today()})", "ops": ops}
(ROOT / "revision_patch_round1h.json").write_text(json.dumps(patch, ensure_ascii=False, indent=1) + "\n", encoding="utf-8"); print("patch ops:", len(ops))
