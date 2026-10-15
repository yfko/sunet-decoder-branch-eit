#!/usr/bin/env python3
"""Readiness gate for the Scientific Reports submission (MANUSCRIPT_RULES R16: readiness is decided by a mechanism, not declared).
Prints one line per gate item with the evidence and PASS / FAIL / PENDING (human action), and writes the report to
manuscript/45_READY_GATE_scirep_<date>.md. A PENDING item is never counted as PASS.

    python3 tools/ready_gate_scirep.py
"""
import hashlib, json, re, subprocess, sys, zipfile, datetime
from pathlib import Path
ROOT = Path(".").resolve(); M = ROOT / "manuscript"; PKG = ROOT / "submission_SciRep_20261008"
sha = lambda p: hashlib.sha256(Path(p).read_bytes()).hexdigest()
mtime = lambda p: datetime.datetime.fromtimestamp(Path(p).stat().st_mtime).strftime("%Y-%m-%d %H:%M")
rows = []
def item(name, ok, evidence):
    rows.append((name, ok, evidence)); print(f"[{ok}] {name}: {evidence}")
def docx_text(p):
    with zipfile.ZipFile(p) as z: x = z.read("word/document.xml").decode("utf-8")
    x = re.sub(r"</w:p>", "\n", x); return re.sub(r"<[^>]+>", "", x)
def pdf_pages(p):
    import pypdf; return len(pypdf.PdfReader(p).pages)

DRAFT, DELIV = M / "49_DRAFT_v6.md", M / "51_SUBMISSION_scirep_v6.md"
V5 = M / "41_DRAFT_v5.md"
dl = DELIV.read_text(); dr = DRAFT.read_text()

# 1 independent checks on file, with dates
rr3 = M / "38_REVIEWER_PANEL_rereview_round2_scirep.md"; ck3 = M / "phase_rereview_round2_scirep/checker_output.txt"
item("round-3 re-review (object v4) on file", "PASS" if rr3.exists() and "re-review synthesis ok" in ck3.read_text() else "FAIL",
     f"{rr3.name} ({mtime(rr3)}); legacy checker: {ck3.read_text().strip().splitlines()[-1][:90]}")
# round-4 re-review must have judged the CURRENT v5 bytes: manifest revised_manuscript sha256 == sha256(41_DRAFT_v5.md), checker exit 0, decision Accept/Minor
rr = M / "47_REVIEWER_PANEL_rereview_round4_scirep.md"; ck = M / "phase_rereview_round4_scirep/checker_output.txt"; mf = M / "phase_rereview_round4_scirep/input_manifest.json"
try:
    man = json.loads(mf.read_text()); judged = man["artifacts"]["revised_manuscript"]["sha256"]; cktxt = ck.read_text()
    last = cktxt.strip().splitlines()[-1]; dec = re.search(r"decision_state '([^']+)'", last); dec = dec.group(1) if dec else "?"
    ok = rr.exists() and judged == sha(DRAFT) and "re-review synthesis ok" in last and dec in ("Accept", "Minor Revision")
    ev = f"{rr.name} ({mtime(rr) if rr.exists() else 'absent'}); judged v5 {judged[:12]} == current {sha(DRAFT)[:12]}: {judged == sha(DRAFT)}; checker: {last[:110]}"
    if not ok and judged == sha(V5) and "re-review synthesis ok" in last:  # the full re-review judged v5; a scoped addendum must have judged the current bytes
        ad = M / "phase_rereview_round4_scirep/addendum_v6.json"; a = json.loads(ad.read_text()); verdicts = [i["verdict"] for i in a["items"]]
        ok = a["judged_revised_sha256"] == sha(DRAFT) and a["judged_original_sha256"] == sha(V5) and a["decision_state"] in ("Accept", "Minor Revision") and all(v == "FULLY_ADDRESSED" for v in verdicts)
        ev = f"{rr.name} judged v5 {judged[:12]} (checker: {last[:60]}); scoped addendum {ad.name}: judged v6 {a['judged_revised_sha256'][:12]} == current {sha(DRAFT)[:12]}: {a['judged_revised_sha256'] == sha(DRAFT)}; items {verdicts}; decision {a['decision_state']}; regressions {[n['new_issue_id'] for n in a.get('new_issues', []) if n.get('attribution') == 'regression']}"
except Exception as e:
    ok, ev = False, f"round-4 re-review artifacts missing or unreadable: {e}"
item("re-review of the current draft on file (round-4 re-review of v5 + scoped addendum for v6)", "PASS" if ok else "FAIL", ev)
try:  # visibility: regression-attributed new issues left open by the round-4 re-review (decision-relevant under B5; PI decides whether to patch)
    tr = json.loads((M / "phase_rereview_round4_scirep/traceability.json").read_text()); di = tr["decision_inputs"]
    adp = M / "phase_rereview_round4_scirep/addendum_v6.json"; adn = (lambda a: f"; round-5 addendum on {a['judged_revised_sha256'][:12]}: {a['decision_state']}, {[i['item_id'] + '=' + i['verdict'] for i in a['items']]}, new issues {len(a.get('new_issues', []))}")(json.loads(adp.read_text())) if adp.exists() else "; no round-5 addendum"
    item("round-4 re-review: regression-attributed new issues and their round-5 disposition", "INFO", f"v5 decision {tr['decision_state']}; regressions {di['regressions']}; previously_missed {di['non_regression_new_issue_ids']}; adjustments {len(tr['adjustments'])}{adn}")
except Exception as e:
    item("round-4 re-review: open regression-attributed new issues (PI triage)", "INFO", f"unreadable: {e}")
# disclosure mode (academic-paper disclosure, Sci Rep) on file, bound to the deliverable bytes it checked
dz = M / "48_DISCLOSURE_scirep.md"
if dz.exists():
    dt = dz.read_text(); fv = [l for l in dt.splitlines() if l.startswith("FINAL VERDICT") and sha(DELIV)[:12] in l]
    okd = bool(fv) and "COMPLIANT" in fv[-1] and "CHANGE REQUIRED" not in fv[-1]
    item("disclosure check on file (FINAL VERDICT line bound to the current deliverable bytes, COMPLIANT)", "PASS" if okd else "FAIL",
         f"{dz.name} ({mtime(dz)}); deliverable {sha(DELIV)[:12]}; " + (fv[-1][:140] if fv else "no FINAL VERDICT line for these bytes"))
else:
    item("disclosure check on file (FINAL VERDICT line bound to the current deliverable bytes, COMPLIANT)", "FAIL", "48_DISCLOSURE_scirep.md absent")
ca5 = M / "42_CITATION_AUDIT_v5.md"; item("citation-check on v5 on file", "PASS" if ca5.exists() and "PASS" in ca5.read_text().split("## 0. Verdict", 1)[1].strip().splitlines()[0] else "FAIL", f"{ca5.name} ({mtime(ca5)})")
ca = M / "50_CITATION_AUDIT_v6.md"; cat = ca.read_text() if ca.exists() else "## 0. Verdict\nABSENT"
vline = cat.split("## 0. Verdict", 1)[1].strip().splitlines()[0]
item("citation-check on v6 (current draft + deliverable) on file", "PASS" if "PASS" in vline else "FAIL", f"{ca.name} ({mtime(ca) if ca.exists() else 'absent'}); verdict: {vline[:100]}")
r44 = M / "44_RESPONSE_TO_REREVIEW_round4.md"; item("round-4 response on file", "PASS" if r44.exists() else "FAIL", f"{r44.name} ({mtime(r44)})")
r52 = M / "52_RESPONSE_TO_REREVIEW_round5.md"; item("round-5 response on file", "PASS" if r52.exists() else "FAIL", f"{r52.name} ({mtime(r52) if r52.exists() else 'absent'})")

# 2 hash chain v4 -> v5 -> deliverable -> package
rep = json.loads((M / "41_DRAFT_v5.md.apply-report.json").read_text())
ok = rep["base_draft_hash"] == sha(M / "34_DRAFT_v4.md")[:12] and rep["output_draft_hash"] == sha(V5)[:12] and rep["authorization_witness"]["status"] == "pass"
item("apply chain v4->v5", "PASS" if ok else "FAIL", f"base {rep['base_draft_hash']} out {rep['output_draft_hash']} witness {rep['authorization_witness']['status']} preserved {rep['counters']['blocks_preserved_byte_identical']}/{rep['counters']['blocks_total']}")
rep6 = json.loads((M / "49_DRAFT_v6.md.apply-report.json").read_text())
ok = rep6["base_draft_hash"] == sha(V5)[:12] and rep6["output_draft_hash"] == sha(DRAFT)[:12] and rep6["authorization_witness"]["status"] == "pass"
item("apply chain v5->v6", "PASS" if ok else "FAIL", f"base {rep6['base_draft_hash']} out {rep6['output_draft_hash']} witness {rep6['authorization_witness']['status']} preserved {rep6['counters']['blocks_preserved_byte_identical']}/{rep6['counters']['blocks_total']}")
same = sha(DELIV) == sha(PKG / "01_Manuscript/Manuscript_SciRep.md") and sha(M / "51_SUBMISSION_scirep_v6.docx") == sha(PKG / "01_Manuscript/Manuscript_SciRep.docx")
item("package manuscript == 51_ deliverable (md, docx)", "PASS" if same else "FAIL", f"md {sha(DELIV)[:12]} docx {sha(M/'51_SUBMISSION_scirep_v6.docx')[:12]}; deliverable newer than v5 draft: {mtime(DELIV) >= mtime(DRAFT)}")
# deliverable derived from v5: every v5 body sentence that changed in round 4 must appear in the deliverable
probes = ["Fable 5.1, Opus 5 and Opus 5.5, accessed August to October 2026", "which use 20,000", "between \u2212" + "0.12 and \u2212" + "0.01 points", "a benefit that did not survive training at the heavier level", "so the prediction is not tested there", "adds between 0.01 and 0.12 points", "0.05/7 = 0.0071", "grows by 0.03 points, to +0.223", "compares two estimates and does not depend on the floor", "fifty-four", "not deposited in a public archive", "on measured data is not tested here"]
miss = [p for p in probes if p not in dl]
item("round-4 and round-5 text present in deliverable", "PASS" if not miss else "FAIL", f"{len(probes)-len(miss)}/{len(probes)} probes found" + (f"; missing {miss}" if miss else ""))

# 3 titles word-for-word across every submission file
title = re.search(r"^# (.+)$", dl, re.M).group(1).strip()
t_docx = docx_text(M / "51_SUBMISSION_scirep_v6.docx").strip().splitlines()[0].strip()
supp = (PKG / "05_Supplementary/Supplementary_S1-S9.md").read_text(); t_supp = supp.splitlines()[2].replace(". Chen, Wang and Ko.", "").strip()
t_supp_docx = [l for l in docx_text(PKG / "05_Supplementary/Supplementary_S1-S9.docx").splitlines() if "decoder branch" in l][0].replace(". Chen, Wang and Ko.", "").strip()
cl = (PKG / "02_Cover_letter/Cover_letter_SciRep.md").read_text(); t_cl = re.search(r'manuscript "([^"]+)"', cl).group(1)
t_abs31 = None
titles = {"51_ md": title, "51_ docx": t_docx, "supplementary md": t_supp, "supplementary docx": t_supp_docx, "cover letter": t_cl}
item("title identical in every file", "PASS" if len(set(titles.values())) == 1 else "FAIL", "; ".join(f"{k}={'same' if v==title else repr(v[:50])}" for k, v in titles.items()) + f"; {len(title.split())} words")

# 4 abstract == 31_ English paragraph; keywords 6; abstract unstructured, no citation
a31 = (M / "31_ABSTRACT_SCIREP_bilingual.md").read_text().split("## English\n\n", 1)[1].split("\n\n**Keywords**", 1)[0].strip()
a43 = dl.split("**Abstract**", 1)[1].strip().split("\n\n", 1)[0].strip()
item("abstract == 31_ English paragraph", "PASS" if a43 == a31 else "FAIL", f"{len(a31.split())} words; '[' in abstract: {'[' in a43}; identical: {a43 == a31}")
kw = re.search(r"\*\*Keywords\*\*: (.+)", dl).group(1); nk = len([k for k in kw.split(";") if k.strip()])
item("keywords <= 6", "PASS" if nk <= 6 else "FAIL", f"{nk}: {kw}")

# 5 placeholders, CJK, stale strings
dtxt = docx_text(M / "51_SUBMISSION_scirep_v6.docx")
ph = re.findall(r"\[[^\]\n]*(?:to supply|to assign|to be|___|roles|URL AND TAG)[^\]\n]*\]", dl + dtxt)
item("no author-field placeholders (md + docx)", "PASS" if not ph else "FAIL", f"{len(ph)} found {ph[:3]}")
cjk = len(re.findall(r"[一-鿿]", dl + dtxt)); item("no CJK characters (md + docx)", "PASS" if cjk == 0 else "FAIL", f"{cjk}")
stale = [s for s in ("fifty-three", "accessed September 2026)", "removes 0.12 points", "belongs mostly", "shrinks by only", "v1.0-submission") if s in dl or s in dtxt]
if "\xa0" in dl: stale.append("NBSP in md")
item("no stale strings (md + docx; NBSP checked in md only, pandoc adds NBSP after 'et al.' by design)", "PASS" if not stale else "FAIL", f"{stale}")
item("cover letter has no placeholders", "PASS" if "【" not in cl and "[" not in cl.split("Dear")[1] else "FAIL", f"{cl.count('【')} 【 marks")

# 6 repository tag named in the manuscript exists on GitHub, is an ancestor of origin/main (main may move on after
#   submission; the tag itself must not), and the local working tree is clean
REPO = Path.home() / "work/sunet-decoder-branch-eit"
tag = re.search(r"\(tag ([^)]+)\)", dl).group(1)
ls = subprocess.run(["git", "-C", str(REPO), "ls-remote", "--tags", "--heads", "origin"], capture_output=True, text=True).stdout
mref = {l.split("\t")[1]: l.split("\t")[0] for l in ls.strip().splitlines()}
tag_commit = mref.get(f"refs/tags/{tag}^{{}}"); main_commit = mref.get("refs/heads/main")
subprocess.run(["git", "-C", str(REPO), "fetch", "--quiet", "origin"], capture_output=True, text=True)
is_anc = bool(tag_commit and main_commit) and subprocess.run(["git", "-C", str(REPO), "merge-base", "--is-ancestor", tag_commit, main_commit]).returncode == 0
st = subprocess.run(["git", "-C", str(REPO), "status", "--short"], capture_output=True, text=True).stdout
item("repository tag on GitHub == manuscript (exists, ancestor of main, local tree clean)", "PASS" if is_anc and not st.strip() else "FAIL", f"manuscript says {tag}; GitHub {tag} -> {str(tag_commit)[:8]}, main -> {str(main_commit)[:8]}; tag is ancestor of main: {is_anc}; local tree clean: {not st.strip()}")
# repo copies of the citation registry and key tools equal the project copies
R = Path.home() / "work/sunet-decoder-branch-eit"
diffs = [f for f in ("tools/cite.py", "tools/make_table_s9.py", "tools/format_convert_scirep.py", "refs/prior_works_strings.md", "refs/overrides.json", "results/tables/table_s9_sweep_all_arms.md", "review_record/41_DRAFT_v5.md.apply-report.json") if sha(R / f) != sha(ROOT / (f if not f.startswith("review_record/") else "manuscript/" + f.split("/", 1)[1]))]
SIGN = json.loads((M / "46_PI_SIGNOFF_scirep_20261007.json").read_text()) if (M / "46_PI_SIGNOFF_scirep_20261007.json").exists() else {}
wv = next((w for w in SIGN.get("waivers", []) if w["item"] == "repo copies == project copies"), None)
# a waiver holds only while its condition re-verifies: same files, deliverable md unchanged
if diffs and wv and sorted(diffs) == sorted(wv["files"]) and sha(DELIV).startswith(wv["deliverable_md_sha256_prefix"]):
    item("repo copies == project copies (registry, S9, tools, v5 apply report)", "WAIVED", f"differ: {diffs}; {wv['decision']} ({wv['by']}, {wv['when']}); condition re-verified: md {sha(DELIV)[:12]}")
else:
    item("repo copies == project copies (registry, S9, tools, v5 apply report)", "PASS" if not diffs else "FAIL", f"differ: {diffs}" if diffs else "7 files identical")

# 7 Sci Rep structure of the deliverable
order = ["## Data Availability", "## References", "## Acknowledgements", "## Author contributions", "## Additional Information", "## Figure legends", "## Tables"]
pos = [dl.find(h) for h in order]
item("back-matter order (Data Availability < References < Acknowledgements < Author contributions < Additional Information < Figure legends < Tables)", "PASS" if all(p >= 0 for p in pos) and pos == sorted(pos) else "FAIL", f"positions {pos}")
item("Methods carries Code availability and AI-use subsections", "PASS" if "### 2.8 Code availability" in dl and "### 2.9 Use of artificial intelligence tools" in dl and "accessed August to October 2026" in dl else "FAIL", "2.8, 2.9, period string")
legs = {m.group(1): len(m.group(2).split()) for m in re.finditer(r"^\*\*(Fig\. \d)\.\*\*(.*)$", dl, re.M)}
item("figure legends <= 350 words; display items <= 8", "PASS" if all(v <= 350 for v in legs.values()) and len(legs) + len(re.findall(r"^\*\*Table \d\.\*\*", dl, re.M)) <= 8 else "FAIL", f"legends {legs}; tables {len(re.findall(r'^[*][*]Table [0-9]', dl, re.M))}")
refs = re.findall(r"^(\d+)\. ", dl.split("## References")[1].split("## Acknowledgements")[0], re.M); nums = sorted(set(int(n) for n in re.findall(r"\[(\d+)", dl.split("## References")[0])))
item("references numbered 1..N contiguous and all cited", "PASS" if [int(x) for x in refs] == list(range(1, len(refs) + 1)) and nums == list(range(1, len(refs) + 1)) else "FAIL", f"{len(refs)} entries; cited numbers 1..{max(nums)}")
item("no footnotes / no 'reviewer' address in body", "PASS" if "[^" not in dl and "to a reviewer" not in dl else "FAIL", "")

# 8 package completeness
need = ["01_Manuscript/Manuscript_SciRep.docx", "01_Manuscript/Manuscript_SciRep.pdf", "02_Cover_letter/Cover_letter_SciRep.docx", "03_Figures/Fig1_fig1_separability.pdf", "03_Figures/Fig2_fig1_arms_and_task.pdf", "03_Figures/Fig3_fig_snr_sweep.pdf", "03_Figures/Fig4_fig_predictions.pdf", "05_Supplementary/Supplementary_S1-S9.pdf", "08_Related_material/Related_material_2025_manuscript_withdrawn_results.docx", "MANIFEST.md"]
missing = [f for f in need if not (PKG / f).exists()]
item("package files present", "PASS" if not missing else "FAIL", f"{len(need)-len(missing)}/{len(need)}" + (f"; missing {missing}" if missing else ""))
secs = re.findall(r"^## (S\d)", supp, re.M); item("supplementary sections S1..S9", "PASS" if secs == [f"S{i}" for i in range(1, 10)] else "FAIL", f"{secs}")
item("manuscript PDF pages", "INFO", f"{pdf_pages(PKG / '01_Manuscript/Manuscript_SciRep.pdf')} pages (manuscript), {pdf_pages(PKG / '05_Supplementary/Supplementary_S1-S9.pdf')} pages (supplementary)")

# 9 numbers: re-derive from per-seed files and compare the headline numbers in the deliverable
before = sha(ROOT / "results/manuscript_numbers.json")
subprocess.run([sys.executable, "tools/verify_manuscript_numbers.py"], capture_output=True, text=True)
after = sha(ROOT / "results/manuscript_numbers.json")
mn = json.loads((ROOT / "results/manuscript_numbers.json").read_text())
def g(*ks):
    v = mn
    for k in ks: v = v[k]
    return v
def f3(x): return f"{x:.3f}"
expect = [("40dB_D_minus_Bwide_heart", "mean_pts", "0.223"), ("40dB_D_minus_Bwide_heart", "control_seed_sd_pts", "0.670"),
          ("H5_20train_20eval_heart", "mean_pts", "0.229"), ("H5_20train_20eval_heart", "control_seed_sd_pts", "0.384"),
          ("sweep_20dB_heart", "mean_pts", "2.097"), ("H3_D20_minus_D60", "mean_pts", "1.937")]
bad = [(k, f, f3(mn[k][f]), want) for k, f, want in expect if f3(mn[k][f]) != want]
shrink = f"{mn['H5_gap_20in20_minus_20in40']['shrink_factor']:.1f}"
if shrink != "9.2": bad.append(("H5_gap_20in20_minus_20in40", "shrink_factor", shrink, "9.2"))
headline_in_deliv = all(s in dl for s in ("0.223 Dice points", "0.229", "1.937 points", "2.097 points", "9.2-fold", "0.670", "0.384"))
item("headline numbers: deliverable strings == re-derived per-seed numbers (3 dp)", "PASS" if headline_in_deliv and not bad else "FAIL", f"deliverable strings present: {headline_in_deliv}; mismatches: {bad or 'none'} (0.223/0.670, 0.229/0.384, 2.097, 1.937, 9.2-fold)")

# 10 human items (never auto-passed)
# a human view counts only for the exact docx in the package (hash-bound in 46_PI_SIGNOFF)
pkg_docx = sha(PKG / "01_Manuscript/Manuscript_SciRep.docx")
views = SIGN.get("rendered_docx_viewed") or []
v = next((x for x in views if x["docx_sha256"] == pkg_docx), None)
has_ln = "lnNumType" in zipfile.ZipFile(PKG / "01_Manuscript/Manuscript_SciRep.docx").read("word/document.xml").decode("utf-8")
if v and has_ln:
    item("rendered docx opened by a human (Table 2 one page, figures, page and line numbers)", "PASS", f"{v['by']}, {v['when']}: {v['what']}; docx {pkg_docx[:12]}; line numbers present")
else:
    seen = "; ".join(f"{x['by']} {x['when']} viewed {x['docx_sha256'][:12]}" for x in views) or "none recorded"
    item("rendered docx opened by a human (Table 2 one page, figures, page and line numbers)", "PENDING", f"package docx {pkg_docx[:12]} (line numbers: {has_ln}) not yet viewed; earlier views: {seen}")
for key, name, hint in (("submission_fields_typed", "submission-system fields typed == manuscript (title, abstract, keywords, authors, ORCIDs, grants, competing interests)", "done at upload from 09_SYSTEM_FIELDS.md"),
                        ("reviewer_emails_spot_checked", "cover letter reviewer e-mails spot-checked by PI", "sources listed in 40_ internal notes")):
    s_ = SIGN.get(key)
    item(name, "PASS" if s_ else "PENDING", f"{s_['by']}, {s_['when']}: {s_.get('what', '')}" if s_ else hint)

n_fail = sum(1 for r in rows if r[1] == "FAIL"); n_pend = sum(1 for r in rows if r[1] == "PENDING"); n_wv = sum(1 for r in rows if r[1] == "WAIVED")
verdict = "NOT READY (failures)" if n_fail else ("READY EXCEPT PENDING HUMAN ITEMS" if n_pend else ("READY WITH PI WAIVER" if n_wv else "READY"))
print(f"\nGATE: {verdict} — {sum(1 for r in rows if r[1]=='PASS')} PASS, {n_fail} FAIL, {n_wv} WAIVED, {n_pend} PENDING, {sum(1 for r in rows if r[1]=='INFO')} INFO")
out = M / f"45_READY_GATE_scirep_{datetime.date.today():%Y%m%d}.md"
out.write_text(f"# Readiness gate — Scientific Reports submission — {datetime.datetime.now():%Y-%m-%d %H:%M}\n\nGenerated by `tools/ready_gate_scirep.py` (R16: readiness decided by mechanism; PENDING items are human actions and never count as PASS; WAIVED = a PI decision recorded in 46_PI_SIGNOFF whose condition is re-verified on every run).\n\n**{verdict}**\n\n| Item | Result | Evidence |\n|---|---|---|\n" + "\n".join(f"| {n} | {o} | {e.replace('|', '/')} |" for n, o, e in rows) + "\n")
print("written", out)
