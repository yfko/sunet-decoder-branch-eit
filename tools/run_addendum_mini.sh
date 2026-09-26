#!/usr/bin/env bash
# PREREGISTRATION_HEART.md section 9 (addendum registered 2026-09-23). Run on the
# MINI, the machine that trained the original 290 runs (section 6: all runs of a
# contrast on one machine).
#
#   bash tools/run_addendum_mini.sh ~/work/sunet_sweep
#
# Inputs (transferred from the Air, generated 2026-09-23 by gen_snr_sweep([35 25])
# and gen_snr_full(20)):
#   <sweep>/v2_snr35/dataset.mat, <sweep>/v2_snr25/dataset.mat   (test split re-noised)
#   <sweep>/v2_full_snr20/dataset.mat                            (all splits at 20 dB)
#
# Steps, in the registered order:
#   1. 9.2  train D and B_wide at 20 dB, seeds 0-57, prereg = the addendum state of
#           PREREGISTRATION_HEART.md (hash a252444b... recorded in run_meta.json)
#   2. 9.2  score runs_20db on the 20 dB full-split test frames -> results_20db_fix
#   3. 9.3  score the ORIGINAL 40 dB-trained runs at 35 and 25 dB -> results_v2_snr{35,25}_heart_fix
#   4. 9.4  per_image.csv from every results dir above plus results_v2_fix and
#           results_v2_snr20_heart_fix is what tools/geom_bootstrap.py reads
set -euo pipefail
SWEEP="${1:?usage: run_addendum_mini.sh <sweep-root>}"
cd "$(dirname "$0")/.."

for f in v2_snr35 v2_snr25 v2_full_snr20; do
  [ -f "$SWEEP/$f/dataset.mat" ] || { echo "missing $SWEEP/$f/dataset.mat"; exit 1; }
done
H=$(shasum -a 256 PREREGISTRATION_HEART.md | cut -d' ' -f1)
grep -q "$H" PREREGISTRATION_HEART.sha256 || { echo "PREREGISTRATION_HEART.md hash $H not in .sha256 — file changed after registration"; exit 1; }
echo "prereg hash $H matches the recorded addendum state"

echo "=== 9.2 train D, B_wide at 20 dB (116 runs) ==="
python3 tools/train_arms.py --data "$SWEEP/v2_full_snr20/dataset.mat" \
    --arms D B_wide --seeds $(seq 0 57) --out runs_20db --prereg PREREGISTRATION_HEART.md

echo "=== 9.2 score runs_20db at 20|20 ==="
python3 tools/evaluate.py --data "$SWEEP/v2_full_snr20/dataset.mat" --runs runs_20db \
    --out results_20db_fix --primary D B_wide --channel heart | tail -20

echo "=== 9.3 score original runs at 35 and 25 dB (evaluation only) ==="
for s in 35 25; do
  python3 tools/evaluate.py --data "$SWEEP/v2_snr$s/dataset.mat" --runs runs \
      --out "results_v2_snr${s}_heart_fix" --primary D B_wide --channel heart | tail -8
done

echo "=== 9.4 per-image files present? ==="
for d in results_v2_fix results_v2_snr20_heart_fix results_20db_fix results_v2_snr35_heart_fix results_v2_snr25_heart_fix; do
  ls -la "$d/per_image.csv" || echo "  $d: no per_image.csv (evaluate.py must write it for 9.4)"
done
echo "done. Copy results_20db_fix/, results_v2_snr{35,25}_heart_fix/, runs_20db/run_meta.json and every per_image.csv back to iCloud."
