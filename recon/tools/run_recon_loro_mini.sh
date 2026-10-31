#!/usr/bin/env bash
# PREREGISTRATION_RECON.md section 12 (addendum, 2026-10-11): the three leave-one-reconstructor-out rows.
# Run on the MINI, from ~/work/sunet_mini, BY HAND, only when no other training is running:
#
#   nohup caffeinate -i bash tools/run_recon_loro_mini.sh ~/work/sunet_sweep > recon_loro_train.log 2>&1 &
#
# Input (built on the Air by tools/build_loro_dataset_ps.py, gate tools/recon_loro_gate.py):
#   <sweep>/v2_full_snr20_loro_{greit,gn,bp}/dataset.mat   (pool of the other two, per-source affine)
# Registered: D and B_wide, seeds 0-29, every training constant unchanged, two processes per row, rows in sequence.
# bash 3.2 (macOS): no associative arrays.
set -euo pipefail
SWEEP="${1:?usage: run_recon_loro_mini.sh <sweep-root>}"
cd "$(dirname "$0")/.."
SHA () { case $1 in greit) echo 08e1b7021717e790be473407c213253570947f410998beca61ca966f10b6dae1;;   # section 12.4
                   gn)    echo 9ea5af3ea2e4bee3d54959dff80395856a7a64e8f6cfa70005b5316aa6486273;;
                   bp)    echo 3f29b53c7634270f7fefa76c555b4bdd882769b4f58de1c149588a1702e3f3e0;; esac; }
for ho in greit gn bp; do
  DS="$SWEEP/v2_full_snr20_loro_$ho/dataset.mat"
  [ -f "$DS" ] || { echo "missing $DS"; exit 1; }
  [ "$(shasum -a 256 "$DS" | cut -d' ' -f1)" = "$(SHA $ho)" ] || { echo "dataset hash of loro_$ho differs from section 12.4"; exit 1; }
done
H=$(shasum -a 256 PREREGISTRATION_RECON.md | cut -d' ' -f1)
grep -q "^$H .*addendum section 12" PREREGISTRATION_RECON.sha256 || { echo "PREREGISTRATION_RECON.md hash $H is not the section-12 addendum state"; exit 1; }
echo "prereg hash $H = section-12 addendum state; three dataset hashes match section 12.4"; date
if pgrep -f "mds_train.py|train_arms.py" >/dev/null; then echo "another training is running on this machine -- not starting"; exit 1; fi
for ho in greit gn bp; do
  DS="$SWEEP/v2_full_snr20_loro_$ho/dataset.mat"
  echo "=== row loro_$ho (pool = the other two; held out: $ho) ==="; date
  python3 tools/train_arms.py --data "$DS" --arms D B_wide --seeds $(seq 0 14)  --out runs_recon_loro_$ho --prereg PREREGISTRATION_RECON.md > recon_loro_${ho}_A.log 2>&1 &
  python3 tools/train_arms.py --data "$DS" --arms D B_wide --seeds $(seq 15 29) --out runs_recon_loro_$ho --prereg PREREGISTRATION_RECON.md > recon_loro_${ho}_B.log 2>&1 &
  wait
  echo "row loro_$ho done: $(ls runs_recon_loro_$ho/*_seed*.pt | wc -l) checkpoints (expect 60)"; date
done
echo "training done"; date
bash tools/eval_recon_loro.sh "$SWEEP"
