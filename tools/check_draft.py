"""Draft checks: per-section word counts (D4/D5), writing-quality counts (R8),
forbidden terms (TERMINOLOGY / boundary clauses), citation slugs vs corpus,
orphan references, and R10b pipeline-leak scan on the manuscript part.

    python3 tools/check_draft.py manuscript/06_DRAFT_v1.md
"""
import json, re, sys
from collections import Counter

p = sys.argv[1]
s = open(p).read()
manu, _, internal = s.partition("# PIPELINE INTERNAL")
body_md = manu
# strip html comments for counting
body = re.sub(r"<!--.*?-->", "", body_md, flags=re.S)

# --- sections
secs = re.split(r"^## (?=\d\. )", body, flags=re.M)
targets = {"1": 900, "2": 1800, "3": 1400, "4": 1400, "5": 200}
tot = 0
print("== word counts (D4/D5) ==")
for sec in secs[1:]:
    num = sec.split(".")[0]
    if num not in targets: continue
    text = sec.split("\n", 1)[1]
    # stop at Acknowledgements for section 5
    text = text.split("\n## Acknowledgements")[0]
    n = len(re.findall(r"\S+", text))
    tot += n
    t = targets[num]
    print(f"  section {num}: {n:5d} / {t}  ({100*(n-t)/t:+.0f}%)  {'OK' if abs(n-t)<=0.15*t else 'OUT OF BAND'}")
print(f"  total    : {tot:5d} / 5700  ({100*(tot-5700)/5700:+.0f}%)  {'OK' if abs(tot-5700)<=570 else 'OUT OF BAND'}")
abst = re.search(r"\*\*Abstract\*\* — (.*?)\n\n", body, re.S).group(1)
print(f"  abstract : {len(abst.split())} words (TMI ≤250)")

# --- R8 writing quality on manuscript prose (exclude references, captions, keywords)
prose = body.split("## References")[0]
flag = ["delve","tapestry","landscape","pivotal","crucial","foster","showcase","testament","navigate","leverage","realm","embark","underscore","multifaceted","nuanced","comprehensive","robust","intricate","cornerstone","paradigm","synergy","holistic","streamline","cutting-edge","groundbreaking"]
print("\n== R8 flagged terms ==")
for w in flag:
    c = len(re.findall(rf"\b{w}\w*", prose, flags=re.I))
    if c: print(f"  {w}: {c}")
openers = ["It is worth noting","It is important to note","It should be noted","In order to","In today's","When it comes to","It goes without saying","In the realm of","This section will","We now turn"]
for o in openers:
    c = prose.count(o)
    if c: print(f"  opener '{o}': {c}")
print(f"  em dashes (—) in prose: {prose.count('—')}  (≤3; abstract/keywords header dashes counted too)")
print(f"  semicolons in prose: {prose.count(';')}  (≤14)")

# --- forbidden terms
print("\n== forbidden / watch terms ==")
for w in ["noisy","divided branch","divided-branch","\\bfirst to\\b","no previous stud","the first ","novel","9\\.24","Scientific Reports","IEEE Sensors","first time"]:
    c = len(re.findall(w, prose, flags=re.I))
    if c: print(f"  {w}: {c}")

# --- citations
corpus = {e["key"] for e in json.load(open("refs/refs_in.json"))}
slugs = re.findall(r"<!--ref:([A-Za-z0-9_]+)-->", body_md)
anchors = re.findall(r"<!--anchor:([a-z]+):", body_md)
print("\n== citations ==")
print(f"  instances: {len(slugs)}; distinct: {len(set(slugs))}; anchors none: {anchors.count('none')}/{len(anchors)}")
bad = [x for x in slugs if x not in corpus]; print(f"  slugs outside corpus: {bad}")
orphans = sorted(corpus - set(slugs)); print(f"  corpus entries never cited (orphans): {orphans}")
print("  per-slug:", dict(Counter(slugs)))

# --- R10b leak scan (manuscript part only)
leak = [w for w in ["Dimension Scores","Failure Condition","Writer Decision","writer_decision","Evaluator","pre-commitment","PRE-COMMITMENT","scoring_plan","acceptance_criteria"] if w in manu]
print("\n== R10b leak scan on manuscript part ==", leak or "clean")
