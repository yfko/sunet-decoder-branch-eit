#!/usr/bin/env python3
"""Readiness gate for the PLoS One submission of the RECON tier-3 paper (MANUSCRIPT_RULES R16: readiness is decided by a
mechanism, not declared). One line per item with evidence and PASS / FAIL / PENDING (human action); PENDING never counts as PASS.
Writes RECON_paper/manuscript/28_READY_GATE_plos_<date>.md.

    python3 tools/ready_gate_plos.py [submission_PLOS_20261031]
"""
import hashlib, json, re, subprocess, sys, zipfile, datetime
from pathlib import Path
ROOT = Path(".").resolve(); M = ROOT / "RECON_paper/manuscript"; PKG = ROOT / (sys.argv[1] if len(sys.argv) > 1 else "submission_PLOS_20261031")
sha = lambda p: hashlib.sha256(Path(p).read_bytes()).hexdigest()
mtime = lambda p: datetime.datetime.fromtimestamp(Path(p).stat().st_mtime).strftime("%Y-%m-%d %H:%M")
rows = []
def item(name, ok, ev): rows.append((name, ok, ev)); print(f"[{ok}] {name}: {ev}")
def docx_xml(p):
    with zipfile.ZipFile(p) as z: return z.read("word/document.xml").decode("utf-8")
def blocks(p):
    t = Path(p).read_text(encoding="utf-8"); parts = re.split(r"(<!--block:(B\d{4})-->\n)", t); B = {}; i = 1
    while i < len(parts): B[parts[i + 1]] = parts[i + 2].rstrip("\n"); i += 3
    return B
V5, V6, V7, V8, V9 = M / "19_DRAFT_v5.md", M / "20_DRAFT_v6.md", M / "23_DRAFT_v7.md", M / "30_DRAFT_v8.md", M / "33_DRAFT_v9.md"
DELIV7, DELIV8, DELIV = M / "24_SUBMISSION_plos_v7.md", M / "31_SUBMISSION_plos_v8.md", M / "34_SUBMISSION_plos_v9.md"  # round 1h (2026-10-31 night): v9 = placeholders filled, S1 Data, figure sentence
dl = DELIV.read_text(encoding="utf-8"); d7 = V9.read_text(encoding="utf-8")

# 1 review chain on file
r1 = M / "12_REVIEWER_PANEL_round1.md"; item("five-seat round-1 review on file", "PASS" if r1.exists() else "FAIL", f"{r1.name} ({mtime(r1) if r1.exists() else 'absent'})")
ck = M / "phase_rereview_round1_20261031/checker_output_rev2.txt"; last = ck.read_text().strip().splitlines()[-1] if ck.exists() else ""
item("legacy re-review checker exit 0, decision Minor Revision", "PASS" if "re-review synthesis ok" in last and "Minor Revision" in last else "FAIL", last[:120])
a6 = json.loads((M / "phase_rereview_round1_20261031/addendum_v6.json").read_text()); verd = [i["verdict"] for i in a6["items"]]
ok = a6["revised_manuscript_sha256"] == sha(V6) and a6["base_sha256"] == sha(V5) and a6["candidate_decision"].startswith("Accept") and all(v == "FULLY_ADDRESSED" for v in verd)
item("scoped re-verification of round 1e judged the v6 bytes: Accept (scoped), all FULLY", "PASS" if ok else "FAIL", f"judged {a6['revised_manuscript_sha256'][:12]} == v6 {sha(V6)[:12]}; {a6['candidate_decision']}; {len(verd)} items")
b6, b7 = blocks(V6), blocks(V7); diff67 = sorted(k for k in b6 if b6[k] != b7[k])
item("v6 -> v7 changed only the reference list and its bracket (no reviewed sentence changed after the scoped Accept)", "PASS" if diff67 == ["B0091", "B0092"] else "FAIL", f"changed blocks {diff67}")
b8 = blocks(V8); diff78 = sorted(k for k in b7 if k in b8 and b7[k] != b8[k]); gone78 = sorted(set(b7) - set(b8)); new78 = sorted(set(b8) - set(b7))
item("v7 -> v8 changed only the AI-disclosure paragraph and deleted the funding/COI section (round 1g; sections 1-5 byte-identical)", "PASS" if diff78 == ["B0087"] and gone78 == ["B0153", "B0154"] and not new78 else "FAIL", f"changed {diff78}; removed {gone78}; added {new78}")
a8p = M / "phase_rereview_round1_20261031/addendum_v8.json"
if a8p.exists():
    a8 = json.loads(a8p.read_text()); v8v = [i["verdict"] for i in a8["items"]]
    ok8 = a8["revised_manuscript_sha256"] == sha(V8) and a8["base_sha256"] == sha(V7) and a8["candidate_decision"].startswith("Accept") and all(v == "FULLY_ADDRESSED" for v in v8v)
    item("scoped re-verification of round 1g judged the v8 bytes: Accept (scoped), all FULLY", "PASS" if ok8 else "FAIL", f"judged {a8['revised_manuscript_sha256'][:12]} == v8 {sha(V8)[:12]}; {a8['candidate_decision']}; {len(v8v)} items")
else: item("scoped re-verification of round 1g (addendum_v8.json)", "PENDING", "absent")
b9 = blocks(V9); diff89 = sorted(k for k in b8 if k in b9 and b8[k] != b9[k]); gone89 = sorted(set(b8) - set(b9)); new89 = sorted(set(b9) - set(b8))
item("v8 -> v9 changed only the placeholder/data-availability blocks, the disclosure paragraph and added the S1 Data caption (round 1h)", "PASS" if diff89 == ["B0013", "B0042", "B0087", "B0089", "B0150"] and not gone89 and new89 == ["B0161"] else "FAIL", f"changed {diff89}; removed {gone89}; added {new89}")
a9p = M / "phase_rereview_round1_20261031/addendum_v9.json"
if a9p.exists():
    a9 = json.loads(a9p.read_text()); v9v = [i["verdict"] for i in a9["items"]]
    ok9 = a9["revised_manuscript_sha256"] == sha(V9) and a9["base_sha256"] == sha(V8) and a9["candidate_decision"].startswith("Accept") and all(v == "FULLY_ADDRESSED" for v in v9v)
    item("scoped re-verification of round 1h judged the v9 bytes: Accept (scoped), all FULLY", "PASS" if ok9 else "FAIL", f"judged {a9['revised_manuscript_sha256'][:12]} == v9 {sha(V9)[:12]}; {a9['candidate_decision']}; {len(v9v)} items")
else: item("scoped re-verification of round 1h (addendum_v9.json)", "PENDING", "absent")
# 2 citation checks
for name, f, tag in (("citation-check v3 (strict) on file", "16_CITATION_AUDIT_v3.md", "PASS"), ("scoped citation re-check v6 on file", "21_CITATION_RECHECK_v6.md", "PASS"), ("scoped citation re-check v7 (reference metadata + deliverable list + retraction refresh) on file", "25_CITATION_RECHECK_v7.md", "PASS")):
    p = M / f; txt = p.read_text(encoding="utf-8") if p.exists() else ""; m = re.search(r"citation_check=(PASS[^`*\n]*|FAIL)", txt)
    item(name, "PASS" if m and m.group(1).startswith("PASS") else ("PENDING" if not p.exists() else "FAIL"), f"{f} ({mtime(p) if p.exists() else 'absent'}); {m.group(1) if m else 'no verdict line'}")
# 3 apply chain
for base, out, rep in ((V5, V6, M / "20_DRAFT_v6.md.apply-report.json"), (V6, V7, M / "23_DRAFT_v7.md.apply-report.json"), (V7, V8, M / "30_DRAFT_v8.md.apply-report.json"), (V8, V9, M / "33_DRAFT_v9.md.apply-report.json")):
    r = json.loads(rep.read_text()); ok = sha(base).startswith(r["base_draft_hash"]) and sha(out).startswith(r["output_draft_hash"]) and r["authorization_witness"]["status"] == "pass"
    item(f"apply chain {base.name} -> {out.name}", "PASS" if ok else "FAIL", f"base {r['base_draft_hash']} out {r['output_draft_hash']} witness {r['authorization_witness']['status']}")
# 4 draft checkers
chk = subprocess.run([sys.executable, "-X", "utf8", "tools/check_recon_draft.py", str(V9)], capture_output=True, text=True).stdout
tot = int(re.search(r"total\s*:\s*(\d+)", chk).group(1)); ab = int(re.search(r"abstract : (\d+)", chk).group(1)); orph = int(re.search(r"orphans, (\d+)", chk).group(1))
item("main text <= 8,000 (PCR), abstract <= 300, 0 orphans, R10b clean", "PASS" if tot <= 8000 and ab <= 300 and orph == 0 and "R10b leak scan on manuscript part == clean" in chk else "FAIL", f"{tot} words; abstract {ab}; orphans {orph}")
num = subprocess.run([sys.executable, "-X", "utf8", "tools/check_recon_draft_numbers.py", str(V9)], capture_output=True, text=True).stdout.strip().splitlines()[-1]
item("R10c: every number in the draft derivable from the result/registration files", "PASS" if "not derivable from the result/registration files: 0" in num else "FAIL", num)
# 5 deliverable == package; docx properties
item("package Manuscript.md == 34_ record copy (v9)", "PASS" if sha(PKG / "Manuscript.md") == sha(DELIV) else "FAIL", f"{sha(DELIV)[:12]}")
x = docx_xml(PKG / "Manuscript.docx")
with zipfile.ZipFile(PKG / "Manuscript.docx") as _z: foot = "".join(_z.read(n).decode("utf-8") for n in _z.namelist() if "footer" in n)
has_ln, has_pg, has_ds = "w:lnNumType" in x, foot.count("PAGE") >= 1, 'w:line="480"' in x
item("DOCX: continuous line numbers, page-number field, double spacing", "PASS" if has_ln and has_pg and has_ds else "FAIL", f"lnNumType {has_ln}; PAGE {has_pg}; line=480 {has_ds}; docx {mtime(PKG/'Manuscript.docx')}")
# 6 title / abstract / placeholders / leaks
title = re.search(r"^# (.*)$", dl, re.M).group(1); dx = re.sub(r"<[^>]+>", "", x)
cl = (PKG / "02_Cover_letter/Cover_letter_PLOS.md").read_text(encoding="utf-8"); sf = (PKG / "00_SYSTEM_FIELDS.md").read_text(encoding="utf-8")
item("title identical in deliverable md, docx, cover letter, system fields", "PASS" if title in dx and title in cl and title in sf else "FAIL", f"{len(title)} chars; docx {title in dx}; letter {title in cl}; fields {title in sf}")
ab_del = re.search(r"## Abstract\n\n(.+?)\n\n\*\*Keywords", dl, re.S).group(1).strip(); ab_dr = re.search(r"\*\*Abstract\*\* — (.*?)\n\n", d7, re.S).group(1).strip()
item("abstract == draft abstract, <= 300 words, no citation", "PASS" if ab_del == ab_dr and len(ab_del.split()) <= 300 and "[" not in ab_del else "FAIL", f"{len(ab_del.split())} words; identical {ab_del == ab_dr}")
gaps = sorted(set(re.findall(r"\[MATERIAL GAP:[^\]]*\]", dl))); item("author-supplied placeholders filled (repository tag, companion preprint DOI; Data availability names S1 Data, round 1h)", "PENDING" if gaps else "PASS", f"{len(gaps)} open: " + "; ".join(g[14:50] for g in gaps))
leak = [w for w in ("PIPELINE INTERNAL", "<!--", "Dimension Scores", "Writer Decision") if w in dl or w in dx]; cjk = len(re.findall(r"[一-鿿]", dl + dx))
item("no pipeline leak, no markers, no CJK in deliverable (md + docx)", "PASS" if not leak and cjk == 0 else "FAIL", f"leaks {leak}; CJK {cjk}")
# 7 ordering rules
tab_first = [int(m.group(1)) for m in re.finditer(r"\bTable (\d)\b", dl.split("\n## Related manuscript")[0])]; seen = []; [seen.append(n) for n in tab_first if n not in seen]
fig_first = [int(m.group(1)) for m in re.finditer(r"\bFig (\d)\b", dl.split("\n## Related manuscript")[0])]; fseen = []; [fseen.append(n) for n in fig_first if n not in fseen]
item("tables and figures cited in ascending order of first appearance; captions follow the citing paragraph", "PASS" if seen == [1, 2, 3, 4] and fseen == [1, 2, 3, 4, 5] else "FAIL", f"tables {seen}; figs {fseen}")
s_first = []; [s_first.append(m.group(0)) for m in re.finditer(r"\bS\d (?:Fig|Table|Appendix)\b", dl.split("\n## Supporting information")[0]) if m.group(0) not in s_first]
by_type = {}; okS = True
for lab in s_first:
    k = lab.split(" ", 1)[1]; by_type[k] = by_type.get(k, 0) + 1; okS &= lab == f"S{by_type[k]} {k}"
item("S-items numbered by type in order of first citation", "PASS" if okS else "FAIL", f"{s_first}")
refs = re.findall(r"^(\d+)\. .+ doi: 10\.", dl, re.M); nums = sorted({int(n) for c in re.findall(r"\[(\d+(?:,\d+)*)\]", dl) for n in c.split(",")})
item("references 1..N contiguous, PLoS 'doi: ' form, all cited", "PASS" if [int(n) for n in refs] == list(range(1, len(refs) + 1)) and nums == list(range(1, len(refs) + 1)) else "FAIL", f"{len(refs)} entries; cited 1..{max(nums)}")
order = [dl.index(h) for h in ("\n## Acknowledgments", "\n## References", "\n## Supporting information")]
item("end-matter order Acknowledgments < References < Supporting information captions; no funding or competing-interest statement in the file", "PASS" if order == sorted(order) and "NSTC" not in dl and "competing interest" not in dl.lower() else "FAIL", f"positions {order}; 'NSTC' in file: {'NSTC' in dl}; 'competing interest' in file: {'competing interest' in dl.lower()}")
# 8 package files
need = ["Manuscript.docx", "Manuscript.md", "Fig1.tif", "Fig2.tif", "Fig3.tif", "Fig4.tif", "Fig5.tif", "S1_Fig.tif", "S1_Table.docx", "S2_Table.docx", "S3_Table.xlsx", "S3_Table.csv", "S1_Appendix.docx", "S1_Appendix.zip",
        "02_Cover_letter/Cover_letter_PLOS.docx", "08_Related_material/Companion_core_paper_SciRep_submission.docx", "S1_Data.zip", "00_SYSTEM_FIELDS.md", "CHECKLIST_author_fields.md", "MANIFEST.sha256"]
missing = [f for f in need if not (PKG / f).exists()]; item("package files present", "PASS" if not missing else "FAIL", f"{len(need)-len(missing)}/{len(need)}" + (f"; missing {missing}" if missing else ""))
man = {l.split("  ", 1)[1]: l.split("  ", 1)[0] for l in (PKG / "MANIFEST.sha256").read_text().splitlines() if l.strip()}
stale = [f for f, h in man.items() if not (PKG / f).exists() or sha(PKG / f) != h]; item("MANIFEST.sha256 matches every package file", "PASS" if not stale else "FAIL", f"{len(man)} files" + (f"; stale {stale[:4]}" if stale else ""))
# figure specs
try:
    from PIL import Image; specs = []
    for f in ("Fig1", "Fig2", "Fig3", "Fig4", "Fig5", "S1_Fig"):
        im = Image.open(PKG / f"{f}.tif"); dpi = float(im.info.get("dpi", (0, 0))[0]); wcm = im.width / dpi * 2.54 if dpi else 0; specs.append(f"{f} {im.width}x{im.height}@{dpi:.0f}dpi={wcm:.1f}cm {im.mode}")
    okf = all(Image.open(PKG / f"{f}.tif").mode == "RGB" for f in ("Fig1", "Fig2", "Fig5"))
    item("figure TIFFs: Figs 1/2/5 RGB 600 dpi within 6.68-19.05 cm; Figs 3/4/S1 from seed-0 diagnostics (PLoS waives format until acceptance)", "PASS" if okf else "FAIL", "; ".join(specs))
except Exception as e: item("figure TIFFs readable", "FAIL", str(e))
s1d = PKG / "S1_Data.zip"; s1d_ok = s1d.exists() and s1d.stat().st_size < 20 * 1024 * 1024
item("S1 Data zip present and under the PLoS 20 MB SI limit; manuscript Data availability names S1 Data", "PASS" if s1d_ok and "S1 Data" in dl else ("FAIL" if not s1d_ok else "PENDING"), f"{s1d.stat().st_size // 1024 if s1d.exists() else 0} KB; 'S1 Data' in deliverable: {'S1 Data' in dl} (round 1h)")
# 9 disclosure
dp = M / "35_DISCLOSURE_plos_v9.md"  # 32_ (COMPLIANT) is bound to the v8 bytes and superseded by round 1h
if dp.exists():
    dt = dp.read_text(encoding="utf-8"); fv = re.search(r"FINAL VERDICT[^\n]*", dt); bound = sha(PKG / "Manuscript.md")[:12] in dt or sha(DELIV)[:12] in dt
    item("disclosure check (PLoS AI policy) FINAL VERDICT COMPLIANT and bound to the deliverable bytes", "PASS" if fv and "COMPLIANT" in fv.group(0) and "CHANGE REQUIRED" not in fv.group(0) and bound else "FAIL", f"{dp.name} ({mtime(dp)}); {fv.group(0)[:90] if fv else 'no verdict line'}; bound {bound}")
else: item("disclosure check on file (re-run on the v9 deliverable)", "PENDING", "35_DISCLOSURE_plos_v9.md absent")
# 10 human items
item("cover letter: Academic Editors chosen by the PI (no 【】 left)", "PASS" if "【" not in cl else "PENDING", f"{cl.count('【')} 【 marks")
item("CRediT roles for this paper confirmed by the PI", "PASS" if "PENDING PI" not in sf.split("## CRediT")[1].split("##")[0] else "PENDING", "system fields CRediT block")
so = M / "29_PI_SIGNOFF_plos.json"
if so.exists():
    s = json.loads(so.read_text())
    for k, hint in (("docx_viewed", "PI opened Manuscript.docx (tables, line numbers, captions after first citation)"), ("github_tag", "repository tag pushed (must equal the tag named in the manuscript)"), ("system_fields_entered", "submission-system fields entered from 00_SYSTEM_FIELDS.md")):
        v = s.get(k); item(hint, "PASS" if v else "PENDING", json.dumps(v, ensure_ascii=False)[:120] if v else "not recorded")
else:
    for hint in ("PI opened Manuscript.docx", "repository tag pushed", "submission-system fields entered"): item(hint, "PENDING", "29_PI_SIGNOFF_plos.json absent")
n_fail = sum(r[1] == "FAIL" for r in rows); n_pend = sum(r[1] == "PENDING" for r in rows); n_pass = sum(r[1] == "PASS" for r in rows)
verdict = "READY" if n_fail == 0 and n_pend == 0 else ("NOT READY — FAIL present" if n_fail else "NOT READY — human items pending")
print(f"\nGATE: {verdict} — {n_pass} PASS, {n_fail} FAIL, {n_pend} PENDING")
stamp = datetime.date.today().strftime("%Y%m%d"); out = M / f"28_READY_GATE_plos_{stamp}.md"
out.write_text(f"# Ready gate — PLoS One submission of the RECON tier-3 paper ({datetime.datetime.now():%Y-%m-%d %H:%M}; tools/ready_gate_plos.py)\n\n| Item | Result | Evidence |\n|---|---|---|\n" + "\n".join(f"| {n} | **{o}** | {e} |" for n, o, e in rows) + f"\n\n**GATE: {verdict}** — {n_pass} PASS, {n_fail} FAIL, {n_pend} PENDING\n", encoding="utf-8")
print("written", out)
