"""RECON tier-3 draft checks (adapted from tools/check_draft.py for the core paper):
per-section word counts (D4/D5; section targets 950/1900/1700/1900/250 kept as information; ceiling 8,000 since the PI's 2026-10-31 decision (was 6,750 band / 7,000 ceiling),
abstract <= 300 for PLoS One), writing-quality counts (R8), forbidden terms (TERMINOLOGY,
boundary clause, stress test §九), citation slugs vs refs/refs_in_recon.json, orphan references,
anchor kinds, and the R10b pipeline-leak scan on the manuscript part.

    python3 tools/check_recon_draft.py RECON_paper/manuscript/06_DRAFT_v1.md
"""
import json, re, sys
from collections import Counter

p = sys.argv[1]
s = open(p).read()
manu, _, internal = s.partition("# PIPELINE INTERNAL")
body = re.sub(r"<!--.*?-->", "", manu, flags=re.S)

# --- sections (main text = sections 1-5; stop at Acknowledgments)
main = body.split("\n## Acknowledgments")[0]
secs = re.split(r"^## (?=\d\. )", main, flags=re.M)
targets = {"1": 950, "2": 1900, "3": 1700, "4": 1900, "5": 250}
tot = 0
print("== word counts (D4/D5) ==")
for sec in secs[1:]:
    num = sec.split(".")[0]
    if num not in targets:
        continue
    text = sec.split("\n", 1)[1]
    n = len(re.findall(r"\S+", text))
    tot += n
    t = targets[num]
    print(f"  section {num}: {n:5d} / {t}  ({100*(n-t)/t:+.0f}%)  {'OK' if abs(n-t)<=0.15*t else 'OUT OF BAND'}")
print(f"  total    : {tot:5d}  (PCR 2026-10-31: ceiling 8,000, no band; pre-round-1b band was 6,750 ±10%)  ceiling 8000 {'OK' if tot<=8000 else 'EXCEEDED'}")
abst = re.search(r"\*\*Abstract\*\* — (.*?)\n\n", body, re.S).group(1)
print(f"  abstract : {len(abst.split())} words (PLoS One ≤300) {'OK' if len(abst.split())<=300 else 'OVER'}")
title = re.search(r"^# (.*)$", body, re.M).group(1)
short = re.search(r"\*\*Short title:\*\* (.*)", body).group(1)
print(f"  title    : {len(title)} chars (≤250); short title {len(short)} chars (≤100)")

# --- R8 writing quality on manuscript prose (exclude references, captions, tables)
prose = main
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
print(f"  semicolons in prose: {prose.count(';')}  (≤14 is the generic R8 threshold; this paper's number-dense Results are expected to exceed it, judge per sentence)")
ascii_minus = len(re.findall(r"(?<![\w])-(?=\d)", prose))
print(f"  ASCII minus before a digit in prose: {ascii_minus}  (should be 0; use −)")

# --- forbidden / watch terms (TERMINOLOGY, boundary clause §八/§九, stress test §九, §11.7/§12.7)
print("\n== forbidden / watch terms ==")
watch = {
    r"\bnoisy\b": "R9: use 'under threat'",
    r"divided[- ]branch": "R9: use 'decoder branch'",
    r"\bfirst to\b|\bthe first\b|\bnovel\b|no previous stud|first time|\bfor the first\b": "R12: no priority/absence claims",
    r"reconstructor-agnostic": "allowed only as the falsified term with the §12.7 clause",
    r"\brobust\b|robustness": "outline forbidden word",
    r"\breplicat": "stress test §九: 'consistent across conditions', not replicated",
    r"no effect|null effect": "write 'below the registered floor'",
    r"does not transfer|cannot transfer": "write 'no evidence of transfer'",
    r"\bequivalent\b": "M2′ is never 'equivalent'",
    r"40 dB": "outside scope (§2/§11.7/§12.7)",
    r"domain generalisation|domain generalization": "only when citing that literature",
    r"\bharmful\b": "no negative-direction reading of L2/R3",
    r"not on the architecture side|not architectural": "forbidden inference",
}
for w, why in watch.items():
    hits = [m.group(0) for m in re.finditer(w, prose, flags=re.I)]
    if hits: print(f"  {w}: {len(hits)}  ({why})")

# --- citations
corpus = {e["key"] for e in json.load(open("refs/refs_in_recon.json"))}
slugs = re.findall(r"<!--ref:([A-Za-z0-9_]+)-->", manu)
anchors = re.findall(r"<!--anchor:([a-z]+):", manu)
print("\n== citations ==")
print(f"  instances: {len(slugs)}; distinct: {len(set(slugs))}; anchors: {dict(Counter(anchors))}")
bad = [x for x in slugs if x not in corpus]; print(f"  slugs outside corpus: {bad}")
orphans = sorted(corpus - set(slugs)); print(f"  corpus entries never cited (orphans, {len(orphans)}): {orphans}")
refkeys = re.findall(r"<!--key:([A-Za-z0-9_]+)-->", manu)
print(f"  reference-list entries: {len(refkeys)}; cited-but-unlisted: {sorted(set(slugs)-set(refkeys))}; listed-but-uncited: {sorted(set(refkeys)-set(slugs))}")
gaps = re.findall(r"\[MATERIAL GAP[^\]]*\]", manu); print(f"  MATERIAL GAP markers ({len(gaps)}): {gaps}")

# --- R10b leak scan (manuscript part only)
leak = [w for w in ["Dimension Scores","Failure Condition","Writer Decision","writer_decision","Evaluator","pre-commitment","PRE-COMMITMENT","scoring_plan","acceptance_criteria"] if w in manu]
print("\n== R10b leak scan on manuscript part ==", leak or "clean")
