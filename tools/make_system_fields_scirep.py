"""Extract submission-system fields from the packaged manuscript md -> 09_SYSTEM_FIELDS.md.
Run after tools/pack_submission_scirep.py (pack wipes the package folder)."""
import re, pathlib
import sys
PKG = pathlib.Path(sys.argv[1] if len(sys.argv) > 1 else "submission_SciRep_20261008")
t = (PKG / "01_Manuscript/Manuscript_SciRep.md").read_text(encoding="utf-8")
L = t.split("\n")
title = next(l for l in L if l.startswith("# ")).lstrip("# ").strip()
abs_ = re.search(r"\*\*Abstract\*\*\n\n(.+?)\n\n\*\*Keywords\*\*", t, re.S).group(1).strip()
kw = re.search(r"\*\*Keywords\*\*: (.+)", t).group(1).strip().split("; ")
ack = re.search(r"## Acknowledgements\n\n(.+?)\n", t).group(1)
grants = re.findall(r"NSTC \d{3}-\d{4}-E-\d{3}-\d{3}", ack)
ci = re.search(r"\*\*Competing interests\.\*\* (.+?)\n", t).group(1)
aff = [l for l in L[:30] if l.startswith(("¹", "²", "³"))]
assert len(aff) == 3 and len(grants) == 3 and len(kw) == 6
out = f"""# 投稿系統逐欄（由 01_Manuscript/Manuscript_SciRep.md 機械抽出，tools/make_system_fields_scirep.py；不要手改，改稿請重跑）

## Title（{len(title.split())} words）
{title}

## Abstract（{len(abs_.split())} words）
{abs_}

## Keywords（{len(kw)}；系統若逐個填就一格一個）
""" + "\n".join(f"{i+1}. {k}" for i, k in enumerate(kw)) + f"""

## Authors（順序同稿件；共同作者 ORCID 見 manuscript/AUTHOR_FIELDS.json，2026-09-26 pub.orcid.org 核過）
1. Chang-Wen Chen — ORCID 0000-0001-7954-4278
   {aff[0]}
2. Tang-Chuan Wang — ORCID 0000-0002-5236-7117
   {aff[1]}
3. Yen-Fen Ko（corresponding）— ORCID 0000-0003-2986-9984 — kklven@gmail.com
   {aff[2]}

## Funding（{len(grants)} 筆；funder = National Science and Technology Council, Taiwan）
""" + "\n".join(f"- {g}" for g in grants) + f"""

稿件 Acknowledgements 原句：
{ack}

## Competing interests（稿件 Additional Information 原句）
{ci}

## Related material
上傳 08_Related_material/Related_material_2025_manuscript_withdrawn_results.docx；系統若分「給編輯」與「給審查人」，選給編輯。cover letter「Related earlier submissions」段已指明。
"""
(PKG / "09_SYSTEM_FIELDS.md").write_text(out, encoding="utf-8")
print("written", PKG / "09_SYSTEM_FIELDS.md")
