#!/usr/bin/env bash
# PREREGISTRATION_RECON.md section 11: score the mixed-ps row (M1', three cells) and the
# exploratory E1 re-scoring of the six R3 cells.
#   results_recon/mixedps__<eval>/      M1': input and output use the evaluation set's own affine (11.3)
#   results_recon/<train>__<eval>_e1/   E1: input by the evaluation set's affine, output by the training set's (11.5)
#   bash tools/eval_recon_mixed_ps.sh ~/work/sunet_sweep          # score
#   DRY=1 bash tools/eval_recon_mixed_ps.sh ~/work/sunet_sweep    # print the nine invocations only (gate, 11.4)
# bash 3.2 (macOS): lookups are case functions, not associative arrays.
set -euo pipefail
SWEEP="${1:?usage: eval_recon_mixed_ps.sh <sweep-root>}"
cd "$(dirname "$0")/.."
RUNS() { case $1 in greit) echo runs_20db;; gn) echo runs_recon_gn;; bp) echo runs_recon_bp;; esac; }
DATA() { case $1 in greit) echo v2_full_snr20;; gn) echo v2_full_snr20_gn;; bp) echo v2_full_snr20_bp;; esac; }
run () { if [ "${DRY:-0}" = 1 ]; then echo "python3 tools/evaluate.py $*"; else python3 tools/evaluate.py "$@" | tail -3; fi; }
mkdir -p results_recon
for ev in greit gn bp; do
  echo "=== M1': mixed-ps -> $ev ==="
  run --data "$SWEEP/$(DATA $ev)/dataset.mat" --runs runs_recon_mixed_ps \
      --out "results_recon/mixedps__${ev}" --primary D B_wide --channel heart
done
for tr in greit gn bp; do
  for ev in greit gn bp; do
    [ "$tr" = "$ev" ] && continue
    echo "=== E1 (exploratory): train $tr -> eval $ev ==="
    run --data "$SWEEP/$(DATA $ev)/dataset.mat" --runs "$(RUNS $tr)" \
        --affine-from-data "$SWEEP/$(DATA $tr)/dataset.mat" --input-own-affine \
        --out "results_recon/${tr}__${ev}_e1" --primary D B_wide --channel heart
  done
done
echo "mixed-ps row and E1 scored"; date
