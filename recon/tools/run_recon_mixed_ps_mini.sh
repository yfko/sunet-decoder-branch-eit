#!/usr/bin/env bash
# PREREGISTRATION_RECON.md section 11 (addendum, 2026-10-03): the mixed-ps row.
# Run on the MINI, from ~/work/sunet_mini, BY HAND, only when no other training is running
# (PI decision 2026-10-03: no automatic start):
#
#   nohup caffeinate -i bash tools/run_recon_mixed_ps_mini.sh ~/work/sunet_sweep > recon_mixed_ps_train.log 2>&1 &
#
# Input (built on the Air by tools/build_mixed_dataset_ps.py, gate tools/recon_mixed_ps_gate.py):
#   <sweep>/v2_full_snr20_mixed_ps/dataset.mat
# Registered: D and B_wide, seeds 0-29, every training constant unchanged, two processes.
# bash 3.2 (macOS): no associative arrays.
set -euo pipefail
SWEEP="${1:?usage: run_recon_mixed_ps_mini.sh <sweep-root>}"
cd "$(dirname "$0")/.."
DS="$SWEEP/v2_full_snr20_mixed_ps/dataset.mat"
DS_SHA=ba879fd13b3d920baff6f7ae5fd9953625e434b4465676f5d15bdcc0014c2ebf   # section 11.4
[ -f "$DS" ] || { echo "missing $DS"; exit 1; }
[ "$(shasum -a 256 "$DS" | cut -d' ' -f1)" = "$DS_SHA" ] || { echo "dataset hash differs from section 11.4"; exit 1; }
H=$(shasum -a 256 PREREGISTRATION_RECON.md | cut -d' ' -f1)
grep -q "^$H .*addendum section 11" PREREGISTRATION_RECON.sha256 || { echo "PREREGISTRATION_RECON.md hash $H is not the addendum state"; exit 1; }
echo "prereg hash $H = addendum state; dataset hash matches section 11.4"; date
if pgrep -f "mds_train.py|train_arms.py" >/dev/null; then echo "another training is running on this machine -- not starting (section 11.6 step 3)"; exit 1; fi

train () {  # <seeds...>
  python3 tools/train_arms.py --data "$DS" --arms D B_wide --seeds "$@" \
      --out runs_recon_mixed_ps --prereg PREREGISTRATION_RECON.md
}
train $(seq 0 14)  > recon_mixed_ps_A.log 2>&1 &
train $(seq 15 29) > recon_mixed_ps_B.log 2>&1 &
wait
echo "training done"; date
echo "runs_recon_mixed_ps: $(ls runs_recon_mixed_ps/*_seed*.pt | wc -l) checkpoints (expect 60)"
bash tools/eval_recon_mixed_ps.sh "$SWEEP"
