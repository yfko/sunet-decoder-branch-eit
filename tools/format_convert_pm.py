"""format-convert (academic-paper, Phase 7) for the core paper -> Physiological Measurement submission set.

From the working draft (markers intact) emits, with every ARS marker stripped and the
pipeline-internal block removed (R10b):
  manuscript/24_SUBMISSION_pm.md    clean markdown; PM structured abstract from 22_ABSTRACT_PM_bilingual.md;
                                    IOP Harvard in-text citations "(Adler and Lionheart 2006)", "Wang et al (2024)";
                                    alphabetical Harvard reference list from refs/prior_works_strings.md (cite.py output);
                                    Conflicts of Interest merged into Acknowledgements (PM rule)
  manuscript/24_SUBMISSION_pm.docx  via pandoc (IOP accepts free-format single PDF; convert docx -> PDF at >= 12 pt)

    python3 tools/format_convert_pm.py manuscript/15_DRAFT_v2.md
"""
import re, subprocess, sys, json
from pathlib import Path

src = Path(sys.argv[1]); out_md = Path("manuscript/24_SUBMISSION_pm.md")
text = src.read_text().split("# PIPELINE INTERNAL")[0].rstrip() + "\n"
text = re.sub(r"^<!--.*?-->\n", "", text, flags=re.S)
text = re.sub(r"<!--block:B\d+-->\n?", "", text)

# ---- structured abstract from the abstract-mode file (English section only)
abs_src = Path("manuscript/22_ABSTRACT_PM_bilingual.md").read_text()
en = abs_src.split("## English")[1].split("## 繁體中文")[0].strip()
paras = [p.strip() for p in en.split("\n\n") if p.strip()]
abstract_paras = [p for p in paras if p.startswith("**Objective.**") or p.startswith("**Approach.**") or p.startswith("**Main results.**") or p.startswith("**Significance.**")]
keywords = next(p for p in paras if p.startswith("**Keywords**"))
assert len(abstract_paras) == 4
abstract_words = sum(len(re.sub(r"\*\*[^*]+\*\*\s*", "", p).split()) for p in abstract_paras)
assert abstract_words <= 250, abstract_words
new_abs = "**Abstract**\n\n" + "\n\n".join(abstract_paras) + "\n\n" + keywords.replace("**Keywords**:", "**Keywords** —")
text = re.sub(r"\*\*Abstract\*\* — .*?\n\n\*\*Keywords\*\* — [^\n]*\n", new_abs + "\n", text, count=1, flags=re.S)
assert "**Objective.**" in text

# ---- IOP Harvard in-text, rendered FROM THE REGISTRY (refs/prior_works.json), not from the draft's
# visible author-year text, so that a registry correction (refs/overrides.json) reaches the deliverable.
reg = {e["key"]: e for e in json.load(open("refs/prior_works.json"))}
suffix = {"Ko2021PhysiolMeas": "a", "Ko2021PLOSONE": "b"}   # same as the reference-list tagging below
def intext(slug):
    e = reg[slug]; fam = [a.rsplit(" ", 1)[0] for a in e["authors"]]
    who = fam[0] if len(fam) == 1 else f"{fam[0]} and {fam[1]}" if len(fam) == 2 else f"{fam[0]} et al"
    return who, f"{e['year']}{suffix.get(slug, '')}"
def paren(m):
    who, yr = intext(m.group(2)); return f"({who} {yr})"
def narr(m):
    who, yr = intext(m.group(3)); return f"{who} ({yr})"
text = re.sub(r"\(([A-Z][^()]*?), (?:\d{4}[a-z]?)\) <!--ref:(\w+)--><!--anchor:[^>]*-->", lambda m: paren(type("M", (), {"group": lambda self, i: (m.group(1), m.group(2))[i-1]})()), text)
text = re.sub(r"([A-Z][\w-]+(?: et al\.| and [A-Z][\w-]+)?) \((\d{4}[a-z]?)\) <!--ref:(\w+)--><!--anchor:[^>]*-->", narr, text)
assert "<!--ref:" not in text and "<!--anchor:" not in text
text = re.sub(r"<!--.*?-->", "", text, flags=re.S)

# ---- Harvard reference list, alphabetical, straight from the generated strings (R12d); add 2021a/2021b
strings = Path("refs/prior_works_strings.md").read_text()
harv_block = strings.split("## Harvard")[1].split("## Vancouver")[0]
entries = [l[2:] for l in harv_block.splitlines() if l.startswith("- ")]
assert len(entries) == 19, len(entries)
def tag(e, letter, must):
    assert must in e, (must, e); return e.replace(" 2021 ", f" 2021{letter} ", 1)
entries = [tag(e, "a", "U-Net-based approach") if "Ko YF and Cheng KS 2021 U-Net" in e else
           tag(e, "b", "Semi-Siamese U-Net for separation") if "Ko YF and Cheng KS 2021 Semi-Siamese" in e else e for e in entries]
refs = "\n\n".join(entries)
text = re.sub(r"(## References\n\n)\[Rendered by[^\n]*\]\n\n(?:\d+\. [^\n]+\n)+", lambda m: m.group(1) + refs + "\n", text)
assert entries[0] in text
# in-text 2021a/2021b must resolve
for k in ("2021a", "2021b"): assert k in text.split("## References")[0]

# ---- PM: competing interests inside Acknowledgements (no separate section)
m = re.search(r"## Conflicts of Interest\n\n(.*?)\n\n", text, flags=re.S)
coi = m.group(1); text = text.replace(m.group(0), "")
text = re.sub(r"(## Acknowledgements\n\n.*?)(\n\n## )", lambda mm: mm.group(1) + "\n\n" + coi + mm.group(2), text, count=1, flags=re.S)
assert text.count("## Conflicts of Interest") == 0 and coi in text
# ---- author-supplied fields (manuscript/AUTHOR_FIELDS.json): substituted in the deliverable only; the working draft keeps its placeholders
af = Path("manuscript/AUTHOR_FIELDS.json")
if af.exists():
    for k, v in json.load(open(af)).items():
        if not k.startswith("_") and k in text:
            text = text.replace(k, v)
remaining = sorted(set(re.findall(r"\[[^\]\n]*(?:to supply|to assign|to be|___|roles|email|URL)[^\]\n]*\]", text)))
print("placeholders still open:", remaining or "none")
# ---- title page: one paragraph per affiliation line (the draft separates them by single newlines only)
for mark in ("²", "³", "\\*Corresponding author:"):
    text = text.replace("\n" + mark, "\n\n" + mark, 1)
assert re.search(r"(?m)^¹ .*\n\n² .*\n\n³ .*\n\n\\\*Corresponding author:", text), "title-page affiliations not split"

# ---- complete document for review: embed Fig. 1-4 above their captions and Tables 1-3 in full
FIGS = {"Fig. 1.": "fig1_arms_and_task", "Fig. 2.": "fig1_separability", "Fig. 3.": "fig_snr_sweep", "Fig. 4.": "fig_predictions"}
def tex_caption(t):
    c = re.search(r"\\caption\{(.*)\}", Path(f"results/tables/{t}.tex").read_text()).group(1)
    for a, b in [("~", " "), ("\\_", "_"), ("$\\Delta$", "Δ"), ("$p$", "p"), ("$d_z$", "dz"), ("95\\%", "95%"),
                 ("$(\\mathrm{D}-\\mathrm{B\\_wide})/(1-\\mathrm{B\\_wide})$", "(D − B_wide)/(1 − B_wide)"), ("i.e.\\ ", "i.e. "),
                 ("DSC percentage points", "Dice points")]:
        c = c.replace(a, b)
    return c
def table_block(n, t):
    md = Path(f"results/tables/{t}.md").read_text().strip()
    rows = [l for l in md.splitlines() if l.startswith("|")]
    note = " ".join(l for l in md.splitlines() if l.strip() and not l.startswith("|"))
    if len(rows[0].split("|")) - 2 > 10:   # too wide for a portrait page: transpose (conditions become columns); content unchanged
        cells = [[c.strip() for c in r.strip("|").split("|")] for r in rows if not set(r.replace("|", "").strip()) <= set("-: ")]
        head, body = cells[0], cells[1:]
        tr = [[head[i]] + [b[i] for b in body] for i in range(len(head))]
        cond = ["Condition"] + [f"{b[0]} trained, {b[1]} evaluated" for b in body]
        tr = [cond] + [r for r in tr if r[0] not in ("Trained", "Evaluated")]
        rows = ["| " + " | ".join(tr[0]) + " |", "|" + "---|" * len(tr[0])] + ["| " + " | ".join(r) + " |" for r in tr[1:]]
    return f"**Table {n}.** {tex_caption(t)}\n\n" + "\n".join(rows) + f"\n\n*Note.* {note}\n"
sec = re.search(r"## Figure and table captions\n\n(.*?)(\*\*Supplementary material\.\*\*)", text, flags=re.S)
parts = re.split(r"\n\n(?=\*\*(?:Fig\. \d\.|Table 1\.))", sec.group(1).strip())
figs_md = []
for ptxt in parts:
    key = next((k for k in FIGS if ptxt.startswith(f"**{k}**")), None)
    if key:
        img = Path("figures") / f"{FIGS[key]}.png"
        figs_md.append(f"![]({img.resolve()}){{width=100%}}\n\n{ptxt}\n")
tables_md = "\n\n".join(table_block(n, t) for n, t in ((1, "table1_arms_40db"), (2, "table2_snr_sweep"), (3, "table3_retrained_20db")))
text = text[:sec.start()] + "## Figures\n\n" + "\n\n".join(figs_md) + "\n\n## Tables\n\n" + tables_md + "\n\n## Supplementary material\n\n" + sec.group(2) + text[sec.end():]
assert text.count("![](") == 4 and "**Table 3.**" in text
out_md.write_text(text)

# ---- checks: R10b leak, CJK characters (PM: Roman only outside the author list), abstract words, body words
leak = [w for w in ["Dimension Scores", "Failure Condition", "Writer Decision", "writer_decision", "Evaluator", "pre-commitment",
                    "PRE-COMMITMENT", "scoring_plan", "acceptance_criteria", "PIPELINE INTERNAL", "<!--"] if w in text]
cjk = sorted(set(re.findall(r"[぀-ヿ㐀-䶿一-鿿가-힯]", text)))
body = text.split("## References")[0]
sec = re.search(r"## 1\. Introduction.*?(?=\n## Acknowledgements)", body, flags=re.S).group(0)
print("R10b leak scan:", "clean" if not leak else leak)
print("CJK characters in deliverable:", cjk or "none")
print("abstract words:", abstract_words, "| main text words (sections 1-5):", len(sec.split()))
print("in-text citations:", len(re.findall(r"\((?:[A-Z][^()]*? )?\d{4}[a-z]?\)", body)))
subprocess.run(["pandoc", str(out_md), "-o", "manuscript/24_SUBMISSION_pm.docx", "--from", "markdown+smart", "--reference-doc", "tools/reference_pm.docx"], check=True)
print("written:", out_md, "manuscript/24_SUBMISSION_pm.docx")
