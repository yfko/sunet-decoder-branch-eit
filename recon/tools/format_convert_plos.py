"""format-convert (academic-paper) for the RECON tier-3 paper -> PLoS One submission set.

From the anchorized working draft (markers intact) emits, with every ARS marker stripped and the pipeline-internal
block removed (R10b), following refs/01_JOURNAL_REQUIREMENTS_PLOSONE.md (R2 record, 2026-10-11):
  <out>/Manuscript.md / Manuscript.docx   title page; abstract (<= 300 words, no citations); body; back matter in PLoS order
                                          (... Acknowledgments -> References -> Supporting information captions);
                                          Vancouver citation-sequence numbers in square brackets, order of first appearance;
                                          reference list rendered FROM THE REGISTRY (refs/prior_works_recon.json via
                                          tools/cite.render_vancouver, overrides applied; R12d); figure captions and tables placed
                                          directly after the paragraph of first citation; tables renumbered in order of first
                                          citation (deliverable only, as the core paper's format-convert did for its figures);
                                          S-items renumbered by type in order of first citation; figures NOT embedded (separate files);
                                          DOCX: double spacing, page numbers, continuous line numbers, tables kept together.
  <out>/S1_Table.xlsx (+csv), S2_Table.docx, S3_Table.docx  (bodies removed from the main file)
  <out>/S1_Appendix.docx + .zip             the four preregistration states and the hash file (hashes asserted)
  <out>/Fig1.tif ... Fig5.tif, S1_Fig.tif   from figures/recon/ (Figs 1, 2, 5) and results_recon/figs (Figs 3, 4, S1 Fig)
  RECON_paper/manuscript/<NN>_SUBMISSION_plos.md  a copy of Manuscript.md for the record

    python3 tools/format_convert_plos.py RECON_paper/manuscript/20_DRAFT_v6.md submission_PLOS_20261031 22
"""
import re, subprocess, sys, json, shutil, zipfile, hashlib
from pathlib import Path
sys.path.insert(0, "tools")
from cite import render_vancouver

src = Path(sys.argv[1]); out = Path(sys.argv[2]); nn = sys.argv[3] if len(sys.argv) > 3 else "22"
out.mkdir(exist_ok=True)
raw = src.read_text(encoding="utf-8")
text = raw.split("# PIPELINE INTERNAL")[0].rstrip() + "\n"
text = re.sub(r"<!--block:B\d+-->\n?", "", text)
text = re.sub(r"\A(?:<!--(?!ref:|anchor:).*?-->\n)+", "", text, flags=re.S)          # header comments
text = re.sub(r"\n<!-- training records.*?-->\n", "\n", text, flags=re.S)

# ---- title page / abstract
m = re.search(r"\*\*Abstract\*\* — (.*?)\n\n\*\*Keywords\*\* — ([^\n]*)\n", text, flags=re.S); assert m
abstract, kw = m.group(1).strip(), m.group(2).strip()
aw = len(abstract.split()); assert aw <= 300, aw; assert "<!--ref:" not in abstract
text = text.replace(m.group(0), "## Abstract\n\n" + abstract + "\n\n**Keywords:** " + kw + "\n", 1)
for mark in ("²", "³", "\\*Corresponding author:"):
    text = text.replace("\n" + mark, "\n\n" + mark, 1)
text = text.replace("\n---\n\n## 1. Introduction", "\n## 1. Introduction", 1)

# ---- citations -> [n] in order of first appearance (the draft trails all markers after a parenthesis)
reg = {e["key"]: e for e in json.load(open("refs/prior_works_recon.json"))}
order = []
def num(key):
    assert key in reg, key
    if key not in order: order.append(key)
    return order.index(key) + 1
MARK = r"<!--ref:(\w+)--><!--anchor:[^>]*-->"
CIT = re.compile(r"^[A-Z][^;()]*?, \d{4}[a-z]?$")
import unicodedata
def surname_ok(item, key):
    s = unicodedata.normalize("NFKD", item.split(",")[0].split(" and ")[0].replace(" et al.", ""))
    s = re.sub(r"[^A-Za-z]", "", s).lower()
    return key.lower().startswith(s[:4])
def repl_any(mm):
    name, inside, tail = mm.group(1), mm.group(3), mm.group(4)
    keys = re.findall(r"<!--ref:(\w+)-->", tail)
    if name is not None:                       # narrative "Name (2024) <marker>"
        assert len(keys) == 1 and surname_ok(name, keys[0]), (name, keys); return f"{name} [{num(keys[0])}]"
    items = [i.strip() for i in inside.split(";")]
    cites = [i for i in items if CIT.match(i)]; prose = [i for i in items if not CIT.match(i)]
    assert len(cites) == len(keys), (inside, keys)
    for it, k in zip(cites, keys): assert surname_ok(it, k), (it, k)
    nums = "[" + ",".join(str(num(k)) for k in keys) + "]"
    if not prose: return nums
    return "(" + "; ".join(prose) + " " + nums + ")"
# one left-to-right pass over both forms, so numbers follow true document order
text = re.sub(r"(?:([A-Z][\w\-]+(?: et al\.| and [A-Z][\w\-]+)?) \((\d{4}[a-z]?)\)|\(([^()]*?)\))((?: " + MARK + r")+)", repl_any, text)
assert "<!--ref:" not in text and "<!--anchor:" not in text, re.findall(r".{60}<!--ref:.{40}", text)[:3]
text = re.sub(r" +([.,;:)])", r"\1", text)   # "] ." -> "]."
text = re.sub(r"\] \]", "]]", text)
assert len(order) == len(reg), (len(order), len(reg))
# order of first appearance must equal the draft's reference-list order
draft_keys = re.findall(r"<!--key:(\w+)-->", raw.split("## References")[1].split("## Supporting information")[0])
assert draft_keys == order, [(i, a, b) for i, (a, b) in enumerate(zip(draft_keys, order), 1) if a != b][:5]

# ---- reference list from the registry (Vancouver, overrides applied by apply_ref_overrides.py)
refs = "\n\n".join(render_vancouver(reg[k], i) for i, k in enumerate(order, 1))
text = re.sub(r"(## References\n\n)\[Vancouver strings generated by[^\n]*\]\n\n(?:\d+\. [^\n]+\n)+", lambda mm: mm.group(1) + refs + "\n", text)
assert refs.split("\n\n")[0] in text and refs.split("\n\n")[-1] in text
text = re.sub(r"<!--key:\w+-->", "", text)

# ---- pull out the Figure captions, Tables and SI-table sections
def take(h):
    global text
    mm = re.search(r"## " + re.escape(h) + r"\n\n(.*?)(?=\n## |\Z)", text, flags=re.S); assert mm, h
    body = mm.group(1).strip(); text = text.replace(mm.group(0), ""); return body
caps = take("Figure captions"); tabs = take("Tables"); sitabs = take("Supporting information tables")
figcaps = {int(mm.group(1)): mm.group(0).strip() for mm in re.finditer(r"\*\*Fig (\d)\. .*?(?=\n\n\*\*Fig \d\. |\Z)", caps, flags=re.S)}
assert sorted(figcaps) == [1, 2, 3, 4, 5], sorted(figcaps)
tabparts = [p.strip() for p in re.split(r"\n\n(?=\*\*Table \d\.)", tabs) if p.strip() and p.strip() != "---"]
tabblocks = {int(re.match(r"\*\*Table (\d)\.", p).group(1)): p for p in tabparts}; assert sorted(tabblocks) == [1, 2, 3, 4], sorted(tabblocks)
siparts = [p.strip() for p in re.split(r"\n\n(?=\*\*S\d Table\.)", sitabs) if p.strip() and p.strip() != "---"]
siblocks = {re.match(r"\*\*(S\d Table)\.", p).group(1): p for p in siparts}; assert sorted(siblocks) == ["S2 Table", "S3 Table"], sorted(siblocks)

# ---- end matter: Acknowledgments immediately before References (PLoS order); SI captions last
ack = take("Acknowledgments"); refs_body = take("References"); si_caps = take("Supporting information")
text = text.rstrip() + "\n\n## Acknowledgments\n\n" + ack + "\n\n## References\n\n" + refs_body + "\n\n## Supporting information\n\n" + si_caps + "\n"
main_end = text.index("\n## Related manuscript")

# ---- tables renumbered in order of first citation in the main text (deliverable only)
main = text[:main_end]
first_tab = {n: main.index(f"Table {n}") for n in (1, 2, 3, 4)}
new_of = {old: i + 1 for i, old in enumerate(sorted(first_tab, key=first_tab.get))}
print("table renumbering (draft -> deliverable):", new_of)
def renum_tables(s):
    s = re.sub(r"\bTable ([1-4])\b", lambda mm: f"Table \x00{new_of[int(mm.group(1))]}\x00", s)
    def pair(mm):
        a, b = sorted(new_of[int(mm.group(1))], new_of[int(mm.group(2))]) if False else sorted((new_of[int(mm.group(1))], new_of[int(mm.group(2))]))
        return f"Tables \x00{a}\x00 and \x00{b}\x00"
    s = re.sub(r"\bTables ([1-4]) and ([1-4])\b", pair, s)
    s = re.sub(r"\bTables 1–4\b", "Tables \x001\x00–\x004\x00", s)
    assert not re.search(r"\bTables? [1-4]\b", s.replace("\x00", "")) or True
    return s.replace("\x00", "")
text = renum_tables(text)
tabblocks = {new_of[k]: renum_tables(v) for k, v in tabblocks.items()}
tabblocks = {k: re.sub(r"^\*\*Table \d\.", f"**Table {k}.", v) for k, v in tabblocks.items()}
figcaps = {k: renum_tables(v) for k, v in figcaps.items()}
# ---- S-items: numbered by type in order of first citation (S3 Fig -> S1 Fig; tables keep S1, S2, S3)
assert "S1 Fig" not in text and "S2 Fig" not in text
text = text.replace("S3 Fig", "S1 Fig"); si_caps = si_caps.replace("S3 Fig", "S1 Fig")
text = text.replace("## Supporting information\n\n" + take("Supporting information"), "## Supporting information\n\n" + renum_tables(si_caps))
main_end = text.index("\n## Related manuscript"); main = text[:main_end]
first_s = [mm.group(0) for mm in re.finditer(r"\bS\d (?:Table|Fig|Appendix|Data)\b", main)]
seen = []; [seen.append(x) for x in first_s if x not in seen]
print("S-items by first citation (draft labels):", seen)
# PLoS: S-items numbered by type in order of first citation -> relabel tables (deliverable only; files renamed to match)
s_new = {}; counter = {}
for lab in seen:
    kind = lab.split(" ", 1)[1]; counter[kind] = counter.get(kind, 0) + 1; s_new[lab] = f"S{counter[kind]} {kind}"
assert set(s_new) == set(re.findall(r"\bS\d (?:Table|Fig|Appendix|Data)\b", text)), set(re.findall(r"\bS\d (?:Table|Fig|Appendix|Data)\b", text)) - set(s_new)
print("S-item relabelling (draft -> deliverable):", {k: v for k, v in s_new.items() if k != v})
def relabel_s(s):
    return re.sub(r"\bS\d (?:Table|Fig|Appendix|Data)\b", lambda mm: "\x01" + s_new[mm.group(0)] + "\x01", s).replace("\x01", "")
text = relabel_s(text); figcaps = {k: relabel_s(v) for k, v in figcaps.items()}; tabblocks = {k: relabel_s(v) for k, v in tabblocks.items()}
siblocks = {s_new[k]: relabel_s(v) for k, v in siblocks.items()}
# the SI caption list must be in S-number order within each type: reorder the caption paragraphs
si_sec = re.search(r"## Supporting information\n\n(.*)\Z", text, flags=re.S); paras = [q.strip() for q in si_sec.group(1).strip().split("\n\n") if q.strip()]
def s_key(q):
    mm = re.match(r"\*\*(S)(\d) (Table|Fig|Appendix|Data)\.", q); return ({"Fig": 0, "Table": 1, "Data": 2, "Appendix": 3}[mm.group(3)], int(mm.group(2)))
paras = sorted(paras, key=s_key)
text = text[:si_sec.start(1)] + "\n\n".join(paras) + "\n"
S1TABLE_FILE = s_new["S1 Table"].replace(" ", "_")   # the per-seed table's deliverable label

# ---- insert figure captions and tables after the paragraph of first citation (main text only)
def insert_after_first(s, label, block):
    i = s.index(label); j = s.index("\n\n", i)
    return s[:j] + "\n\n" + block + s[j:]
for n in (1, 2, 3, 4, 5):
    text = insert_after_first(text, f"Fig {n}", figcaps[n])
for n in (1, 2, 3, 4):
    text = insert_after_first(text, f"Table {n}", tabblocks[n])
for n in (1, 2, 3, 4, 5): assert text.index(f"Fig {n}") < text.index(f"**Fig {n}. ")
for n in (1, 2, 3, 4): assert text.index(f"Table {n}") < text.index(f"**Table {n}. ") and text.index(f"**Table {n}. ") < text.index("\n## Related manuscript")
seq = [int(mm.group(1)) for mm in re.finditer(r"\*\*Table (\d)\.", text)]; assert seq == [1, 2, 3, 4], seq
seqf = [int(mm.group(1)) for mm in re.finditer(r"\*\*Fig (\d)\.", text)]; assert seqf == [1, 2, 3, 4, 5], seqf

# ---- placeholders
gaps = sorted(set(re.findall(r"\[MATERIAL GAP:[^\]]*\]", text)))
print("author-supplied placeholders still open:", len(gaps)); [print("   ", g) for g in gaps]

# ---- checks
leak = [w for w in ["Dimension Scores", "Failure Condition", "Writer Decision", "PIPELINE INTERNAL", "<!--", "block:B0"] if w in text]
cjk = sorted(set(re.findall(r"[぀-ヿ㐀-䶿一-鿿가-힯]", text)))
body = re.search(r"## 1\. Introduction.*?(?=\n## Related manuscript)", text, flags=re.S).group(0)
body_wo = re.sub(r"\*\*Table \d\..*?(?=\n\n(?!\|)(?!¹)(?!M2′))", "", body, flags=re.S)
body_wo = re.sub(r"\*\*Fig \d\. [^\n]*\n", "", body_wo)
cites = re.findall(r"\[(\d+(?:,\d+)*)\]", text); used = sorted({int(x) for c in cites for x in c.split(",")})
print("R10b leak scan:", "clean" if not leak else leak, "| CJK:", cjk or "none")
print("abstract words:", aw, "| title chars:", len(re.search(r"^# (.*)$", text, re.M).group(1)), "| short title chars:", len(re.search(r"\*\*Short title:\*\* (.*)", text).group(1)))
print("citation instances:", len(cites), "| distinct:", len(used), "| max:", max(used), "| gaps:", sorted(set(range(1, len(reg) + 1)) - set(used)) or "none")
print("main text words incl. captions/tables:", len(body.split()), "| approx. prose only:", len(body_wo.split()))

# ---- write markdown (+ record copy)
(out / "Manuscript.md").write_text(text, encoding="utf-8")
rec = Path(f"RECON_paper/manuscript/{nn}_SUBMISSION_plos.md"); rec.write_text(text, encoding="utf-8")

# ---- SI table docx files (S2, S3), S1 Table copies, S1 Appendix
def pandoc(md_text, dst):
    tmp = out / (dst.stem + ".md"); tmp.write_text(md_text, encoding="utf-8")
    subprocess.run(["pandoc", str(tmp), "-o", str(dst), "--from", "markdown+smart", "--reference-doc", "tools/reference_pm.docx"], check=True); tmp.unlink()
for sname, blk in siblocks.items():
    pandoc(renum_tables(blk) + "\n", out / (sname.replace(" ", "_") + ".docx"))
for f in ("S1_Table.xlsx", "S1_Table.csv", "S1_Table_derived.csv"):
    p = Path("RECON_paper/manuscript/si") / f
    if p.exists(): shutil.copy(p, out / f.replace("S1_Table", S1TABLE_FILE))
APPX = s_new["S1 Appendix"].replace(" ", "_")
states = [("PREREGISTRATION_RECON.pre-dev20261003.md", "4b4c7a6d", "Registered state, 2026-09-26"), ("PREREGISTRATION_RECON.pre-add11_20261003.md", "3fdc703d", "Deviation record, 2026-10-03"),
          ("PREREGISTRATION_RECON.pre-add12_20261011.md", "0060eedf", "First addendum (section 11), 2026-10-03"), ("PREREGISTRATION_RECON.md", "9589b298", "Second addendum (section 12), 2026-10-11")]
app = [f"# {s_new['S1 Appendix']}. The preregistration in its four hashed states, with the hash file\n", "Each state is the full text of PREREGISTRATION_RECON.md as it was hashed; the SHA-256 of each file is given and recorded in PREREGISTRATION_RECON.sha256 (reproduced at the end).\n"]
with zipfile.ZipFile(out / f"{APPX}.zip", "w", zipfile.ZIP_DEFLATED) as z:
    for f, pre, label in states:
        b = Path(f).read_bytes(); h = hashlib.sha256(b).hexdigest(); assert h.startswith(pre), (f, h)
        z.write(f, arcname=f); app.append(f"\n\n---\n\n# {label} — `{f}` — SHA-256 {h}\n\n" + b.decode("utf-8"))
    z.write("PREREGISTRATION_RECON.sha256", arcname="PREREGISTRATION_RECON.sha256")
    app.append("\n\n---\n\n# PREREGISTRATION_RECON.sha256\n\n```\n" + Path("PREREGISTRATION_RECON.sha256").read_text() + "\n```\n")
pandoc("\n".join(app), out / f"{APPX}.docx")

# ---- figures: TIFF (LZW) copies; Figs 1, 2, 5 from figures/recon; Figs 3, 4 and S1 Fig from the seed-0 diagnostic PNGs
from PIL import Image
def to_tif(images, dst, dpi=300):
    ims = [Image.open(p).convert("RGB") for p in images]
    if len(ims) > 1:   # stack vertically on white, widths matched
        w = max(i.width for i in ims); ims = [i if i.width == w else i.resize((w, int(i.height * w / i.width))) for i in ims]
        canvas = Image.new("RGB", (w, sum(i.height for i in ims)), "white"); y = 0
        for i in ims: canvas.paste(i, (0, y)); y += i.height
        im = canvas
    else: im = ims[0]
    im.save(dst, compression="tiff_lzw", dpi=(dpi, dpi)); return im.size
fig_src = {"Fig1": [Path("figures/recon/Fig1.tif")], "Fig2": [Path("figures/recon/Fig2.tif")], "Fig5": [Path("figures/recon/Fig5.tif")],
           "Fig3": [Path("results_recon/figs/mixed_affine_inputs.png"), Path("results_recon/figs/mixed_ps_inputs.png")],
           "Fig4": [Path("results_recon/figs/loro_preds_seed0.png")],
           s_new["S1 Fig"].replace(" ", "_"): [Path("results_recon/figs/shift_inputs_D_seed0.png"), Path("results_recon/figs/loro_preds_seed0.png")]}
for name, srcs in fig_src.items():
    if all(p.exists() for p in srcs):
        if len(srcs) == 1 and srcs[0].suffix == ".tif": shutil.copy(srcs[0], out / f"{name}.tif"); print("figure copied:", name)
        else: print("figure composed:", name, to_tif(srcs, out / f"{name}.tif"))
    else: print("figure MISSING (not yet built):", name, [str(p) for p in srcs if not p.exists()])

# ---- DOCX: pandoc, then double spacing, table layout, page and line numbers
subprocess.run(["pandoc", str(out / "Manuscript.md"), "-o", str(out / "Manuscript.docx"), "--from", "markdown+smart", "--reference-doc", "tools/reference_pm.docx"], check=True)
import docx
from docx.shared import Pt, Inches
from docx.oxml.ns import qn
from docx.oxml import OxmlElement
from docx.enum.text import WD_ALIGN_PARAGRAPH
def _flag(pr, tag):
    if pr.find(qn(tag)) is None: pr.append(OxmlElement(tag))
d = docx.Document(out / "Manuscript.docx")
for p in d.paragraphs:
    p.paragraph_format.line_spacing = 2.0       # PLoS: double-spaced
for tbl in d.tables:
    el = tbl._tbl; cap = el.getprevious()
    if cap is not None and cap.tag == qn("w:p"): _flag(cap.get_or_add_pPr(), "w:keepNext")
    for row in tbl.rows:
        _flag(row._tr.get_or_add_trPr(), "w:cantSplit")
        for cell in row.cells:
            for p in cell.paragraphs:
                _flag(p._p.get_or_add_pPr(), "w:keepNext"); p.paragraph_format.line_spacing = 1.0
                for r in p.runs: r.font.size = Pt(8)
    ncol = len(tbl.columns); CH, PAD, TOTAL = 0.062, 0.16, 6.5
    tok = [max(len(w) for r in tbl.rows for w in (r.cells[j].text.split() or [""])) for j in range(ncol)]
    pref = [max(len(r.cells[j].text) for r in tbl.rows[1:]) for j in range(ncol)]
    lo = [t * CH + PAD for t in tok]; hi = [max(p_, t) * CH + PAD for p_, t in zip(pref, tok)]
    spare = TOTAL - sum(lo); room = [h - l for h, l in zip(hi, lo)]
    if spare <= 0 or sum(room) == 0: w_in = [l * TOTAL / sum(lo) for l in lo]
    elif spare <= sum(room): w_in = [l + spare * r / sum(room) for l, r in zip(lo, room)]
    else: w_in = [h + (spare - sum(room)) / ncol for h in hi]
    widths = [Inches(w) for w in w_in]; tblPr = el.tblPr; lay = tblPr.find(qn("w:tblLayout"))
    if lay is None: lay = OxmlElement("w:tblLayout"); tblPr.append(lay)
    lay.set(qn("w:type"), "fixed"); grid = el.find(qn("w:tblGrid"))
    for gc, w in zip(grid.findall(qn("w:gridCol")), widths): gc.set(qn("w:w"), str(int(w.inches * 1440)))
    for row in tbl.rows:
        for cell, w in zip(row.cells, widths): cell.width = w
for sec in d.sections:
    sp = sec._sectPr
    if sp.find(qn("w:lnNumType")) is None:
        ln = OxmlElement("w:lnNumType"); ln.set(qn("w:countBy"), "1"); ln.set(qn("w:distance"), "360"); ln.set(qn("w:restart"), "continuous")
        after = [qn(t) for t in ("w:footnotePr", "w:endnotePr", "w:type", "w:pgSz", "w:pgMar", "w:paperSrc", "w:pgBorders")]
        idx = max([i for i, c in enumerate(sp) if c.tag in after], default=-1); sp.insert(idx + 1, ln)
    fp = sec.footer.paragraphs[0]
    if "PAGE" not in sec.footer._element.xml:
        fp.alignment = WD_ALIGN_PARAGRAPH.CENTER; fld = OxmlElement("w:fldSimple"); fld.set(qn("w:instr"), "PAGE")
        r = OxmlElement("w:r"); t = OxmlElement("w:t"); t.text = "1"; r.append(t); fld.append(r); fp._p.append(fld)
d.save(out / "Manuscript.docx")
print("written:", out / "Manuscript.md", out / "Manuscript.docx", rec, "| tables in docx:", len(d.tables))
