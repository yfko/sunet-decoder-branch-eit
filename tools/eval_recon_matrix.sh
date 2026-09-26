#!/usr/bin/env bash
# PREREGISTRATION_RECON.md: score the 4 (trained) x 3 (evaluated) matrix, twice:
#   results_recon/<train>__<eval>/            registered cells: affine from the TRAINING dataset
#   results_recon/<train>__<eval>_ownaffine/  secondary 3(c): affine from the EVALUATION dataset
# GREIT row = runs_20db (58 seeds trained under the addendum; the analysis keeps seeds 0-29).
#   bash tools/eval_recon_matrix.sh ~/work/sunet_sweep
set -euo pipefail
SWEEP="${1:?usage: eval_recon_matrix.sh <sweep-root>}"
cd "$(dirname "$0")/.."
declare -A RUNS=( [greit]=runs_20db [gn]=runs_recon_gn [bp]=runs_recon_bp [mixed]=runs_recon_mixed )
declare -A DATA=( [greit]=v2_full_snr20 [gn]=v2_full_snr20_gn [bp]=v2_full_snr20_bp [mixed]=v2_full_snr20_mixed )
mkdir -p results_recon
for tr in greit gn bp mixed; do
  for ev in greit gn bp; do
    echo "=== train $tr -> eval $ev ==="
    python3 tools/evaluate.py --data "$SWEEP/${DATA[$ev]}/dataset.mat" --runs "${RUNS[$tr]}" \
        --affine-from-data "$SWEEP/${DATA[$tr]}/dataset.mat" \
        --out "results_recon/${tr}__${ev}" --primary D B_wide --channel heart | tail -3
    if [ "$tr" != "$ev" ]; then
      python3 tools/evaluate.py --data "$SWEEP/${DATA[$ev]}/dataset.mat" --runs "${RUNS[$tr]}" \
          --out "results_recon/${tr}__${ev}_ownaffine" --primary D B_wide --channel heart | tail -3
    fi
  done
done
echo "matrix scored"; date
