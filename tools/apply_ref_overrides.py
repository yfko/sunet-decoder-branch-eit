"""Apply documented metadata corrections to the citation registry and re-render the
strings with cite.py's own renderers (MANUSCRIPT_RULES R12d: no hand-typed strings).

refs/overrides.json lists, per key, the corrected fields, the source consulted and the
date. Crossref is occasionally wrong (author order of IEEE CVPR records) or stale
(early-access TPAMI records without volume/pages); the override is the recorded
human verification, applied by program.

    python3 tools/apply_ref_overrides.py
"""
import json, datetime, sys
from pathlib import Path
sys.path.insert(0, "tools")
from cite import render_harvard, render_vancouver

reg = json.loads(Path("refs/prior_works.json").read_text())
ov = json.loads(Path("refs/overrides.json").read_text())
by_key = {e["key"]: e for e in reg}
log = []
for key, o in ov.items():
    e = by_key[key]
    for field, val in o["fields"].items():
        log.append(f"{key}.{field}: {e.get(field)!r} -> {val!r}  [{o['source']}, {o['verified']}]")
        e[field] = val
    e["overrides"] = {"fields": list(o["fields"]), "source": o["source"], "verified": o["verified"]}
reg.sort(key=lambda e: (e["authors"][0] if e["authors"] else "", e["year"]))
Path("refs/prior_works.json").write_text(json.dumps(reg, ensure_ascii=False, indent=2))

# re-render strings; keep the original verification statement and append the override log
strings = Path("refs/prior_works_strings.md").read_text()
head, rest = strings.split("## Harvard", 1)
statement = "\n---\n" + rest.split("\n---\n", 1)[1]
s = [head.rstrip() + "\n", "## Harvard（字母序）— Physiological Measurement 要求的格式\n"]
s += [f"- {render_harvard(e)}" for e in reg]
s.append("\n## Vancouver（編號制）— 若投稿期刊改變\n")
s += [render_vancouver(e, i) for i, e in enumerate(reg, 1)]
stamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
s.append(statement.rstrip() + f"\n\n### 人工核對後的覆寫（`refs/overrides.json`，由 `tools/apply_ref_overrides.py` 於 {stamp} 套用）\n\n" + "\n".join(f"- {l}" for l in log) + "\n")
Path("refs/prior_works_strings.md").write_text("\n".join(s))
print("\n".join(log)); print("re-rendered refs/prior_works_strings.md")
