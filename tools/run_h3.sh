#!/usr/bin/env bash
# H3 evaluation sweep. Run on the MACHINE THAT HOLDS THE WEIGHTS (the mini).
#
#   bash tools/run_h3.sh ~/work/sunet_sweep
#
# PREREGISTRATION_HEART.md section 5 registers an evaluation-only sweep; models
# are trained once at 40 dB and evaluated across 60/50/40/30/20 dB, so nothing
# is retrained.
#
# H3's anchor is THIS SWEEP'S OWN 40 dB level, not the original results_v2 --
# in both branches of gen_snr_sweep.m's self-check that is the correct choice,
# because H3 compares levels to each other and every level in the sweep shares
# one forward mesh. The original results_v2 then serves as an independent
# cross-check of the 40 dB level rather than as an input to the test.
set -euo pipefail

SWEEP="${1:?usage: run_h3.sh <sweep-root>}"
LEVELS="60 50 40 30 20"

cd "$(dirname "$0")/.."
for s in $LEVELS; do
    d="$SWEEP/v2_snr$s/dataset.mat"
    [ -f "$d" ] || { echo "missing $d"; exit 1; }
done

for s in $LEVELS; do
    echo "=== evaluating $s dB ==="
    python3 tools/evaluate.py --data "$SWEEP/v2_snr$s/dataset.mat" \
        --runs runs --out "results_v2_snr$s" --primary D B_wide --channel heart \
        | tail -20
done

echo
echo "=== cross-check: sweep's own 40 dB against the original results_v2 ==="
python3 - <<'PY'
import csv, math
from pathlib import Path
def load(p):
    return {(r["arm"], r["seed"], r["channel"]): float(r["dsc"])
            for r in csv.DictReader(open(Path(p) / "per_seed.csv"))}
a, b = load("results_v2"), load("results_v2_snr40")
keys = sorted(set(a) & set(b))
d = [abs(a[k] - b[k]) for k in keys]
print(f"  {len(keys)} matched arm/seed/channel cells")
print(f"  max |DSC difference| = {max(d):.3e}   mean = {sum(d)/len(d):.3e}")
print("  -> identical; the replay reproduced the registered 40 dB run"
      if max(d) < 1e-9 else
      "  -> NOT identical. Report the sweep as its own internally consistent\n"
      "     series and state this cross-check value in the manuscript.")
PY

echo
echo "=== H3, registered rule ==="
python3 tools/h3_snr.py \
    --results results_v2_snr60 results_v2_snr50 results_v2_snr40 \
              results_v2_snr30 results_v2_snr20 \
    --snr 60 50 40 30 20
