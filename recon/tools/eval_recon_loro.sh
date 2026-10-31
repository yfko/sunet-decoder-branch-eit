#!/usr/bin/env bash
# PREREGISTRATION_RECON.md section 12: score the three leave-one-out rows.
#   results_recon/loro_<ho>__<ho>/   L1/L2: the held-out reconstructor, input and output under ITS OWN training-split affine (12.3)
#   results_recon/loro_<ho>__<x>/    reported only: the two in-pool reconstructors (two-source in-pool reference)
#   bash tools/eval_recon_loro.sh ~/work/sunet_sweep          # score
#   DRY=1 bash tools/eval_recon_loro.sh ~/work/sunet_sweep    # print the nine invocations only (gate, 12.4)
set -euo pipefail
SWEEP="${1:?usage: eval_recon_loro.sh <sweep-root>}"
cd "$(dirname "$0")/.."
DATA() { case $1 in greit) echo v2_full_snr20;; gn) echo v2_full_snr20_gn;; bp) echo v2_full_snr20_bp;; esac; }
run () { if [ "${DRY:-0}" = 1 ]; then echo "python3 tools/evaluate.py $*"; else python3 tools/evaluate.py "$@" | tail -3; fi; }
mkdir -p results_recon
for ho in greit gn bp; do
  for ev in greit gn bp; do
    if [ "$ev" = "$ho" ]; then echo "=== L1/L2: loro_$ho -> $ev (held out) ==="; else echo "=== reported: loro_$ho -> $ev (in pool) ==="; fi
    run --data "$SWEEP/$(DATA $ev)/dataset.mat" --runs runs_recon_loro_$ho \
        --out "results_recon/loro_${ho}__${ev}" --primary D B_wide --channel heart
  done
done
echo "leave-one-out rows scored"; date
