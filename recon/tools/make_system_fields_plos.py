"""PLoS One submission-system fields for the RECON tier-3 paper, extracted mechanically from the packaged deliverable
(submission_PLOS_<date>/Manuscript.md) and the author registry -> <package>/00_SYSTEM_FIELDS.md and
RECON_paper/manuscript/27_SYSTEM_FIELDS_plos.md. Do not hand-edit: rerun after any change to the deliverable.

    python3 tools/make_system_fields_plos.py submission_PLOS_20261031
"""
import re, sys, json
from pathlib import Path
PKG = Path(sys.argv[1] if len(sys.argv) > 1 else "submission_PLOS_20261031"); t = (PKG / "Manuscript.md").read_text(encoding="utf-8"); L = t.split("\n")
title = next(l for l in L if l.startswith("# ")).lstrip("# ").strip()
short = re.search(r"\*\*Short title:\*\* (.*)", t).group(1).strip()
abstract = re.search(r"## Abstract\n\n(.+?)\n\n\*\*Keywords", t, re.S).group(1).strip()
kw = [k.strip() for k in re.search(r"\*\*Keywords:\*\* (.+)", t).group(1).split(";")]
aff = [l for l in L[:40] if l.startswith(("¹", "²", "³"))]; assert len(aff) == 3
def sec(h):
    m = re.search(r"## " + re.escape(h) + r"\n\n(.*?)(?=\n## |\Z)", t, re.S); return m.group(1).strip()
related, data, ethics, ack = sec("Related manuscript"), sec("Data availability"), sec("Ethics statement"), sec("Acknowledgments")
si = re.findall(r"^\*\*(S\d (?:Fig|Table|Appendix|Data))\.\*\* (.+)$", sec("Supporting information"), re.M)
figs = re.findall(r"^\*\*Fig (\d)\. (.+?)\*\*", t, re.M)
gaps = sorted(set(re.findall(r"\[MATERIAL GAP:[^\]]*\]", t)))
coi = ("The corresponding author (Y.-F. K.) is the original author of the semi-Siamese architecture whose decoder branch is evaluated in this study "
       "(Ko and Cheng, PLoS One 2021). The authors declare no other competing interests. This does not alter our adherence to PLOS ONE policies on sharing data and materials.")
out = f"""# PLoS One 投稿系統逐欄（由 {PKG}/Manuscript.md 機械抽出，tools/make_system_fields_plos.py；不要手改，改稿請重跑）

## Article type
Research Article

## Full title（{len(title)} chars ≤ 250）
{title}

## Short title（{len(short)} chars ≤ 100）
{short}

## Abstract（{len(abstract.split())} words ≤ 300；無引用）
{abstract}

## Keywords（{len(kw)}；系統若有欄位）
""" + "\n".join(f"{i+1}. {k}" for i, k in enumerate(kw)) + f"""

## Authors（順序同稿件；ORCID 依 New idea/AUTHORS_registry.md）
1. Yen-Fen Ko（corresponding）— ORCID 0000-0003-2986-9984 — kklven@gmail.com
   {aff[0]}
2. Chang-Wen Chen — ORCID 0000-0001-7954-4278
   {aff[1]}
3. Tang-Chuan Wang — ORCID 0000-0002-5236-7117
   {aff[2]}

## CRediT（**PENDING PI**：登記檔的慣例是核心論文的；本篇「依實際分工另定」。下面是沿用核心論文慣例的草案）
- Yen-Fen Ko: Conceptualization, Methodology, Software, Validation, Formal analysis, Investigation, Data curation, Writing – original draft, Writing – review & editing, Visualization, Supervision, Project administration, Funding acquisition
- Chang-Wen Chen: Conceptualization, Writing – review & editing
- Tang-Chuan Wang: Conceptualization, Writing – review & editing

## Financial Disclosure（稿件內不寫；PI 決定 7，2026-10-17：CMU114-MF-46 不列）
Funder: National Science and Technology Council, Taiwan. Grants: NSTC 114-2221-E-039-006; NSTC 113-2221-E-039-006; NSTC 112-2221-E-039-006 (recipient: Y.-F. K.).
The funders had no role in study design, data collection and analysis, decision to publish, or preparation of the manuscript.

## Competing Interests（稿件內不寫，round 1g 已刪指標節；系統填這段）
{coi}

## Data Availability Statement（系統欄；稿件 Data availability 節原句）
{data}

## Ethics statement（稿件原句）
{ethics}

## Related manuscripts（系統「related work」聲明；上傳核心論文副本為 related material）
{related}
Copy to upload: the companion manuscript as submitted to Scientific Reports on 2026-10-15 (Submission ID fe9fef03-af7f-47a6-97bb-d6fc471500cb; formal manuscript number pending) — file 08_Related_material/Companion_core_paper_SciRep_submission.docx.

## AI disclosure（PLoS：寫在正文；Acknowledgments 第一段原句，系統若另問就貼同一段）
{ack.split(chr(10))[0]}

## Figures（另檔上傳；圖說在稿件內）
""" + "\n".join(f"- Fig{n}.tif — {cap}" for n, cap in figs) + """

## Supporting information files
""" + "\n".join(f"- {lab}: {cap[:140]}{'…' if len(cap) > 140 else ''}" for lab, cap in si) + f"""

## Author-supplied placeholders still in the manuscript（{len(gaps)}；投稿當天填）
""" + "\n".join(f"- {g}" for g in gaps) + """

## Suggested Academic Editors（**PENDING PI**；PLoS 規定不可是近期合作者或同機構）
【PI 選；從 journals.plos.org/plosone/s/editorial-board 搜尋 electrical impedance tomography / medical image segmentation / reproducibility；不可：成大 Kuo-Sheng Cheng、2025 共同作者 Yen-Da Lin、Po-Lan Su；不可同機構 China Medical University】

## Opposed reviewers
None.
"""
(PKG / "00_SYSTEM_FIELDS.md").write_text(out, encoding="utf-8"); Path("RECON_paper/manuscript/27_SYSTEM_FIELDS_plos.md").write_text(out, encoding="utf-8")
print("written", PKG / "00_SYSTEM_FIELDS.md", "| title chars", len(title), "| abstract words", len(abstract.split()), "| figs", len(figs), "| SI", len(si), "| gaps", len(gaps))
