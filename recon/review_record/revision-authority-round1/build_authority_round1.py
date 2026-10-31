# -*- coding: utf-8 -*-
"""Revision-authority artefacts (#670) for the RECON tier-3 manuscript, round 1 (2026-10-31, Fable 5.1):
the five-seat manuscript panel (12_REVIEWER_PANEL_round1.md = phase_review_round1_20261031/synthesis.md,
mechanical major_revision; REV-M1-1 … REV-M1-43). Base: 06_DRAFT_v1.md after anchorize (751dacb8560c, 148 blocks).
Author event: author_event_20261031.txt (the PI's session mandate; default triage = every must_fix and
should_fix will_address, every consider declined for this round and listed for the PI).

The 43 roadmap items are parsed from the synthesis's two roadmap tables so that no description, anchor,
severity or confidence is retyped; only the schema mappings below are this script's own."""
import json, re, subprocess, sys
from pathlib import Path
PROJ = Path("/Users/yfko/Library/Mobile Documents/com~apple~CloudDocs/Documents/New idea/SunetBeta_the importance-of-divided-branch-structure")
S = Path.home() / ".claude/plugins/cache/academic-research-skills/academic-research-skills/3.23.0/scripts"
sys.path.insert(0, str(S.parent))
from scripts.revision_roadmap import bytes_hash, _source_key  # noqa
ROOT = PROJ / "RECON_paper/manuscript/revision-authority-round1"
BASE = PROJ / "RECON_paper/manuscript/06_DRAFT_v1.md"; MANIFEST = PROJ / "RECON_paper/manuscript/06_DRAFT_v1.md.block-manifest.json"
EVENT = ROOT / "author_event_20261031.txt"; LETTER = PROJ / "RECON_paper/manuscript/12_REVIEWER_PANEL_round1.md"
base_raw = BASE.read_bytes(); manifest_raw = MANIFEST.read_bytes(); letter = LETTER.read_text(encoding="utf-8")
assert bytes_hash(base_raw).startswith("751dacb8560c"), bytes_hash(base_raw)
def raw(v): return (json.dumps(v, ensure_ascii=False, sort_keys=True, separators=(",", ":")) + "\n").encode("utf-8")

COMP = {"EIC": "Journal-Fit seat of the 2026-10-31 manuscript panel (PLoS One academic-editor identity)",
        "R1": "Methodology seat of the 2026-10-31 manuscript panel (preregistered deep-learning simulation statistics)",
        "R2": "Domain seat (EIDORS thoracic EIT reconstruction) of the 2026-10-31 manuscript panel",
        "R3": "Perspective seat (medical-image domain generalisation / multi-source training) of the 2026-10-31 manuscript panel",
        "DA": "Devil's Advocate seat of the 2026-10-31 manuscript panel"}
CODE = {  # bounded-consequence label in the synthesis → closed schema enum
    "standing_mismatch": "claim_scope_unsupported", "equivalence_overclaim": "claim_scope_unsupported", "data_text_mismatch": "claim_scope_unsupported",
    "verification_gap": "reader_traceability_reduced", "deviation_record_incomplete": "reporting_requirement_unmet", "descriptive_overclaim": "claim_scope_unsupported",
    "methods_not_self_contained": "method_reproducibility_unresolved", "preregistration_statement_inexact": "reporting_requirement_unmet",
    "no_effect_wording": "claim_scope_unsupported", "placeholder_unresolved": "editorial_conformance_unmet", "required_statement_missing": "editorial_conformance_unmet",
    "promised_elements_missing": "reporting_requirement_unmet", "strength_mismatch": "claim_scope_unsupported", "confound_unstated": "interpretive_ambiguity_remains",
    "reproducibility_statement_missing": "method_reproducibility_unresolved", "assumption_unstated": "interpretive_ambiguity_remains",
    "definition_unstated": "reader_traceability_reduced", "transcription_unverified": "reader_traceability_reduced", "standing_unqualified": "claim_scope_unsupported",
    "rounding_inconsistent": "reader_traceability_reduced", "framing_unsupported_locally": "evidence_gap_remains", "adjacent_field_inaccuracy": "interpretive_ambiguity_remains",
    "attribution_incomplete": "reader_traceability_reduced", "attribution_unverified": "reader_traceability_reduced", "internal_inconsistency": "interpretive_ambiguity_remains",
    "qualification_missing": "claim_scope_unsupported", "opacity_for_outside_reader": "interpretive_ambiguity_remains", "term_undefined": "interpretive_ambiguity_remains",
    "term_defined_by_citation_only": "interpretive_ambiguity_remains", "term_ambiguity": "interpretive_ambiguity_remains", "implication_unstated": "interpretive_ambiguity_remains",
    "forward_reference_unexplained": "reader_traceability_reduced", "asymmetric_application_unexplained": "reporting_requirement_unmet",
    "da_position_recorded": "interpretive_ambiguity_remains", "argument_overreach": "claim_scope_unsupported", "timing_implicit": "reporting_requirement_unmet",
    "straw_man_wording": "claim_scope_unsupported", "mechanism_stated_as_fact": "claim_scope_unsupported", "presupposition_unsupported": "claim_scope_unsupported"}
# the synthesis's own "Acceptance criteria" (R1–R10) are reused verbatim for must_fix; should/consider use the bounded consequence
ACC = {}
for m in re.finditer(r"\*\*R(\d+): .*?\*\*\n(?:- .*\n)*?- \*\*Acceptance criteria\*\*: (.*)", letter):
    ACC[int(m.group(1))] = m.group(2).strip()
EXTRA_TARGETS = {  # structural needs beyond the synthesis's block lists: inserts for the new supporting tables / statements
    "REV-M1-8": [("B0097", "insert_after"), ("B0116", "replace_block"), ("B0117", "replace_block")],
    "REV-M1-19": [("B0116", "replace_block")],
    "REV-M1-7": [("B0089", "replace_block")],
    "REV-M1-9": [("B0117", "replace_block")],
    "REV-M1-10": [("B0094", "replace_block"), ("B0106", "replace_block"), ("B0113", "replace_block"), ("B0110", "replace_block"), ("B0108", "replace_block"), ("B0107", "replace_block"), ("B0111", "replace_block"), ("B0114", "replace_block"), ("B0115", "replace_block")],
    "REV-M1-1": [("B0107", "replace_block"), ("B0105", "replace_block")],
    "REV-M1-2": [("B0108", "replace_block")],
    "REV-M1-13": [("B0057", "replace_block")],
    "REV-M1-22": [("B0066", "replace_block"), ("B0070", "replace_block"), ("B0051", "replace_block")],
    "REV-M1-29": [("B0112", "replace_block"), ("B0058", "replace_block")],
    "REV-M1-11": [("B0020", "replace_block")],
    "REV-M1-12": [("B0020", "replace_block"), ("B0055", "replace_block"), ("B0056", "replace_block")],
    "REV-M1-5": [("B0085", "replace_block")],
    "REV-M1-20": [("B0028", "replace_block"), ("B0116", "replace_block"), ("B0036", "replace_block")],
    "REV-M1-14": [("B0028", "replace_block")],
    "REV-M1-31": [("B0028", "replace_block")],
    "REV-M1-32": [("B0024", "replace_block")],
    "REV-M1-16": [("B0109", "replace_block"), ("B0057", "replace_block")],
    "REV-M1-17": [("B0114", "replace_block")],
    "REV-M1-33": [("B0059", "replace_block"), ("B0114", "replace_block"), ("B0105", "replace_block")],
    "REV-M1-36": [("B0053", "replace_block"), ("B0036", "replace_block")],
    "REV-M1-43": [("B0020", "replace_block")],
    "REV-M1-11": [("B0077", "replace_block"), ("B0020", "replace_block")],
    "REV-M1-18": [("B0006", "replace_block"), ("B0066", "replace_block")],
    "REV-M1-23": [("B0023", "replace_block"), ("B0116", "replace_block")],
    "REV-M1-26": [("B0030", "replace_block")],
    "REV-M1-27": [("B0011", "replace_block")],
    "REV-M1-24": [("B0072", "replace_block")],
    "REV-M1-28": [("B0067", "replace_block")],
    "REV-M1-34": [("B0083", "replace_block")],
    "REV-M1-42": [("B0059", "replace_block")],
    "REV-M1-38": [("B0078", "replace_block")],
    "REV-M1-4": [("B0062", "replace_block"), ("B0006", "replace_block"), ("B0067", "replace_block"), ("B0063", "replace_block"), ("B0020", "replace_block")],
    "REV-M1-6": [("B0089", "replace_block"), ("B0042", "replace_block")],
    "REV-M1-15": [("B0031", "replace_block")],
    "REV-M1-21": [("B0006", "replace_block")],
    "REV-M1-3": [("B0085", "replace_block"), ("B0066", "replace_block")],
}

COLLATERAL = [  # (block, declined item whose proposed target it is, accepted item whose edit touches it)
    ("B0059", "REV-M1-33", "REV-M1-42"), ("B0114", "REV-M1-33", "REV-M1-10"), ("B0105", "REV-M1-33", "REV-M1-1"), ("B0106", "REV-M1-33", "REV-M1-1"), ("B0046", "REV-M1-33", "REV-M1-8"),
    ("B0024", "REV-M1-25", "REV-M1-19"), ("B0049", "REV-M1-30", "REV-M1-8"), ("B0078", "REV-M1-35", "REV-M1-38"), ("B0031", "REV-M1-37", "REV-M1-15"), ("B0036", "REV-M1-40", "REV-M1-9")]

def parse_rows(section):
    rows = []
    for line in section.splitlines():
        if not line.startswith("| ") or line.startswith("| Transport ref") or line.startswith("|---"):
            continue
        cells = [c.strip() for c in line.strip().strip("|").split(" | ")]
        if len(cells) != 11:
            raise SystemExit(f"row with {len(cells)} cells: {line[:80]}")
        rows.append(dict(zip(["tref", "id", "desc", "sc", "sev", "anchor", "conf", "source", "obl", "cost", "cons"], cells)))
    return rows

must = letter.split("### Required Revisions (Must Fix)")[1].split("### Required Item Details")[0]
sugg = letter.split("### Suggested Revisions (Should Fix / Consider)")[1].split("### Source-Traceability Checklist")[0]
rows = parse_rows(must) + parse_rows(sugg)
assert len(rows) == 43, len(rows)

def anchor_of(a):
    kind, _, rest = a.partition(": ")
    kind = kind.strip().lower()
    if kind == "text":
        m = re.search(r'^(.*?)\s*"(.*)"\s*$', rest.strip(), flags=re.S)
        loc = (m.group(1).strip() or "manuscript") if m else rest.strip()
        quote = m.group(2) if m else rest.strip()
        quote = " ".join(quote.split()[:25])
        return {"anchor_type": "text", "locator": loc.rstrip(" ,;:") or "manuscript", "quote": quote}
    if kind == "table":
        return {"anchor_type": "table", "locator": rest.strip()}
    if kind == "absence":
        loc, _, chk = rest.partition(" — ")
        if not chk:
            loc, _, chk = rest.partition("; checked ")
            chk = "checked " + chk
        return {"anchor_type": "absence", "locator": loc.strip(), "absence_scope": loc.strip(), "check_performed": chk.strip()}
    raise SystemExit(f"unknown anchor kind {kind!r}")

def seat_and_ordinal(src):
    m = re.match(r"(EIC|R1|R2|R3|DA)\s*\((?:W|MAJOR |minor |question )?(\d+)", src)
    if not m:
        m2 = re.match(r"(EIC|R1|R2|R3|DA)", src)
        return m2.group(1), 1
    return m.group(1), int(m.group(2))

def cost_of(c):
    kind, _, loc = c.partition(": ")
    kind = kind.strip()
    if kind not in ("sentence", "section", "re_analysis", "new_data"):
        kind = "section"
    loc = re.sub(r"\(pre-submission gate; cannot be closed in a revision draft before minting\)", "", loc)
    return {"kind": kind, "locator": loc.strip()[:300] or "manuscript"}

items = []
for r in rows:
    rid = r["id"]; n = int(rid.split("-")[-1])
    seat, ordinal = seat_and_ordinal(r["source"])
    sev = r["sev"].lower(); assert sev in ("critical", "major", "minor"), sev
    conf = int(re.match(r"\s*(\d)", r["conf"]).group(1))
    consensus = "SPLIT" if "SPLIT" in r["source"] else "SINGLE-VERIFIER"
    label = re.sub(r"\s*\(.*?\)\s*$", "", r["cons"].split("→")[0]).strip()
    code = CODE[label]
    blocks = set(re.findall(r"B\d{4}", r["cost"]))
    for a, z in re.findall(r"(B\d{4})[–-](B\d{4})", r["cost"]):
        blocks.update(f"B{n:04d}" for n in range(int(a[1:]), int(z[1:]) + 1))
    blocks = sorted(blocks)
    tgt = {}
    for b in blocks:
        tgt.setdefault(b, set()).add("replace_block")
    for b, op in EXTRA_TARGETS.get(rid, []):
        tgt.setdefault(b, set()).add(op)
    CANON = ["replace_block", "insert_after", "delete_block"]
    proposed = [{"block_id": b, "allowed_operations": [o for o in CANON if o in ops]} for b, ops in sorted(tgt.items())]
    tref = r["tref"]
    verify = ACC.get(int(tref[1:])) if tref.startswith("R") and r["obl"] == "must_fix" else f"{r['cons']} (verified against the acceptance text of the roadmap row {rid}; checker: block ids above re-read against the revised draft)."
    items.append(dict(id=rid, source_refs=[{"seat": seat, "channel": "finding", "ordinal": ordinal, "subclaim_ordinal": 0}], reviewer=seat,
        description=f"{r['sc']}: {r['desc']}", sub_claim_ids=[r["sc"].split(",")[0].strip()], obligation_class=r["obl"], severity=sev,
        evidence_anchor=anchor_of(r["anchor"]), confidence=conf, corroborating_sources=[], cost_scope=cost_of(r["cost"]),
        consequence_if_unaddressed={"code": code, "target": {"kind": "manuscript", "locator": ", ".join(blocks) or "manuscript"}},
        target_section=", ".join(blocks) or "manuscript", suggested_action=r["desc"][:1500], consensus_level=consensus,
        verification_criteria=verify, proposed_targets=proposed, competence_basis=COMP[seat]))
items.sort(key=lambda i: int(i["id"].split("-")[-1]))
seen = {}
for it in items:
    key = (it["source_refs"][0]["seat"], it["source_refs"][0]["ordinal"])
    it["source_refs"][0]["subclaim_ordinal"] = seen.get(key, 0); seen[key] = seen.get(key, 0) + 1
items.sort(key=lambda it: (_source_key(it["source_refs"][0]), it["id"]))
counts = {k: sum(1 for i in items if i["obligation_class"] == k) for k in ("must_fix", "should_fix", "consider")}
assert counts == {"must_fix": 10, "should_fix": 25, "consider": 8}, counts
roadmap = {"schema_version": "revision-roadmap/1.0", "revision_round": 1, "base_draft_sha256": bytes_hash(base_raw), "block_manifest_sha256": bytes_hash(manifest_raw),
    "items": items, "total_items": 43, "obligation_counts": counts, "editorial_decision": "Major Revision",
    "consensus_summary": "Five-seat manuscript panel round 1 (12_REVIEWER_PANEL_round1.md sha256 " + bytes_hash(LETTER.read_bytes()) + "): mechanical major_revision (F2 on repairable D3/D6 blocks, F3, F5; no fatal; DA 0 CRITICAL / 7 MAJOR). No seat questioned the data, design or statistics (R1 recomputed all twelve Wilcoxon p values and every printed quantity). Two corroborated findings, three severity/direction SPLITs arbitrated, no unresolved dissent.",
    "dissenting_opinions": ["REV-M1-37 (DA MAJOR 6): the upper-bound qualification of the held-out loss is unlicensed; R2, R3 and EIC list the qualification as a strength; the panel requires the assumption to be stated (REV-M1-15), not relabelling.",
                            "REV-M1-39 (DA MAJOR 7): the title attaches 'preregistered' to a design that exists only in the second addendum; EIC and R2 checked the title without objection; the panel requires a response, not a title change."]}
roadmap_raw = raw(roadmap); (ROOT / "roadmap.json").write_bytes(roadmap_raw)
cs = {"schema_version": "claim-surface-manifest/1.0", "revision_round": 1, "roadmap_sha256": bytes_hash(roadmap_raw), "base_draft_sha256": bytes_hash(base_raw), "claim_intent_sources": [], "surfaces": []}
(ROOT / "claim-surface-manifest.json").write_bytes(raw(cs))
event = "AUTHOR-EVENT-PI-recon-tier3-round1-2026-10-31"
adj = []
for it in items:
    if it["obligation_class"] == "consider":
        adj.append({"item_id": it["id"], "author_event_id": event, "author_triage": "wont_address", "authorized_targets": [], "claim_strength_authorizations": [],
                    "author_reason": "consider-class item left for the PI's decision at triage; not changed in round 1 (default policy recorded in author_event_20261031.txt); a response is given in the response letter"})
    else:
        adj.append({"item_id": it["id"], "author_event_id": event, "author_triage": "will_address", "authorized_targets": it["proposed_targets"], "claim_strength_authorizations": []})
choices = {"schema_version": "author-adjudication-input/1.0",
    "author_events": [{"event_id": event, "source": "explicit_session_user_message", "actor_role": "author", "input_sha256": bytes_hash(EVENT.read_bytes())}],
    "display_order": {"mode": "source_traceability", "item_ids": [i["id"] for i in items], "author_event_id": event},
    "author_adjudications": adj,
    "collateral_authorizations": [{"authorization_id": f"COLLATERAL-AUTH-round1-{blk}-{dec}", "author_event_id": event, "authorizing_item_id": acc, "constrained_item_id": dec, "block_id": blk, "operation": "replace_block",
        "reason": f"{dec} is a consider-class item left for the PI and is not implemented; the {acc} edit of {blk} does not carry out {dec}'s request (the term, attribution, clause or pointer it asks for is left as in the base draft)."} for blk, dec, acc in COLLATERAL]}
(ROOT / "author-choices.json").write_bytes(raw(choices))
if (ROOT / "author-adjudication.json").exists(): (ROOT / "author-adjudication.json").unlink()  # the builder refuses to overwrite
cli = [sys.executable, str(S / "revision_roadmap.py")]; common = ["--base", str(BASE), "--block-manifest", str(MANIFEST)]
for args in (["validate-roadmap", str(ROOT / "roadmap.json")] + common,
             ["build-adjudication", str(ROOT / "roadmap.json")] + common + ["--claim-surface", str(ROOT / "claim-surface-manifest.json"), "--author-choices", str(ROOT / "author-choices.json"), "--artifact-root", str(ROOT), "--output", str(ROOT / "author-adjudication.json")],
             ["validate-adjudication", str(ROOT / "roadmap.json"), str(ROOT / "author-adjudication.json")] + common + ["--claim-surface", str(ROOT / "claim-surface-manifest.json"), "--artifact-root", str(ROOT)]):
    r = subprocess.run(cli + args, capture_output=True, text=True); print(args[0], "rc=", r.returncode, (r.stdout + r.stderr).strip()[-600:])
