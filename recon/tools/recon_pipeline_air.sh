#!/usr/bin/env bash
# PREREGISTRATION_RECON.md §8 steps 2-4, chained on the Air. Every step logs to results_recon/.
#   bash tools/recon_pipeline_air.sh
# 2  gen_recon_full(20)                -> data/v2_full_snr20_{gn,bp}/, data/v2_test_snr40_{gn,bp}/, data/v2_voltages/
# 3  pilot_recon_checks.py (data only) -> results_recon/pilot_checks.json ; stops if a check fails
#    build_mixed_dataset.py            -> data/v2_full_snr20_mixed/dataset.mat
# 4  rsync datasets + code + prereg to the mini, then launch run_recon_mini.sh under nohup caffeinate
set -euo pipefail
cd "$(dirname "$0")/.."
mkdir -p results_recon
LOG=results_recon/pipeline_air.log
say () { echo "[$(date '+%m-%d %H:%M:%S')] $*" | tee -a "$LOG"; }
H=$(shasum -a 256 PREREGISTRATION_RECON.md | cut -d' ' -f1)
grep -q "$H" PREREGISTRATION_RECON.sha256 || { say "prereg hash mismatch"; exit 1; }
say "prereg $H ok"

say "step 2: gen_recon_full(20) start"
/Applications/MATLAB_R2026a.app/bin/matlab -batch "cd('$(pwd)'); addpath('tools'); gen_recon_full(20)" -logfile results_recon/gen_recon_full.log > /dev/null 2>&1
grep -q "wrote .*v2_voltages" results_recon/gen_recon_full.log || { say "gen_recon_full did not finish; see results_recon/gen_recon_full.log"; exit 1; }
grep -E "done in|self-check" results_recon/gen_recon_full.log | tee -a "$LOG"

say "step 3: pilot checks"
python3 tools/pilot_recon_checks.py > results_recon/pilot_checks.txt 2>&1 || { say "pilot checks crashed"; exit 1; }
python3 - <<'EOF' | tee -a "$LOG"
import json, sys
p = json.load(open("results_recon/pilot_checks.json")); bad = []
for r in ("greit", "gn", "bp"):
    h = p[f"qa_fraction_{r}"]["recon_heart"]["mean"]
    print(f"  heart QA fraction {r}: {h:.3f}")
    if not (0.02 < h < 0.40): bad.append(f"{r} heart QA fraction {h:.3f} outside (0.02, 0.40)")
for r in ("gn", "bp"):
    o = p[f"heart_peak_offset_vs_greit_{r}"]["max_abs"]
    print(f"  heart peak offset vs GREIT {r}: {o} px")
    if o > 3: bad.append(f"{r} heart peak offset {o} px > 3")
    print(f"  perturbation 40->20 dB {r}: median peak {p[f'perturbation_40_to_20_{r}']['peak_fraction_pct']['median']:.1f}%")
if bad: print("PILOT FAIL: " + "; ".join(bad)); sys.exit(1)
print("pilot checks pass")
EOF
say "step 3b: mixed dataset"
mkdir -p data/v2_full_snr20_mixed
python3 tools/build_mixed_dataset.py data/v2_full_snr20/dataset.mat data/v2_full_snr20_gn/dataset.mat data/v2_full_snr20_bp/dataset.mat data/v2_full_snr20_mixed/dataset.mat | tee -a "$LOG"

say "step 4: transfer to the mini"
M=yfko@192.168.68.66
for d in v2_full_snr20_gn v2_full_snr20_bp v2_full_snr20_mixed v2_test_snr40_gn v2_test_snr40_bp v2_voltages; do
  rsync -a "data/$d" "$M:~/work/sunet_sweep/"
done
rsync -a tools/evaluate.py tools/run_recon_mini.sh tools/eval_recon_matrix.sh "$M:~/work/sunet_mini/tools/"
rsync -a PREREGISTRATION_RECON.md PREREGISTRATION_RECON.sha256 "$M:~/work/sunet_mini/"
ssh "$M" 'cd ~/work/sunet_mini && shasum -a 256 ~/work/sunet_sweep/v2_full_snr20_{gn,bp,mixed}/dataset.mat' | tee -a "$LOG"
shasum -a 256 data/v2_full_snr20_{gn,bp,mixed}/dataset.mat | tee -a "$LOG"
ssh "$M" 'cd ~/work/sunet_mini && nohup caffeinate -i bash tools/run_recon_mini.sh ~/work/sunet_sweep > recon_train.log 2>&1 < /dev/null & echo launched pid $!' | tee -a "$LOG"
sleep 120
ssh "$M" 'cd ~/work/sunet_mini && head -3 recon_train.log; tail -2 recon_A.log recon_B.log; cat runs_recon_gn/run_meta.json 2>/dev/null | head -8' | tee -a "$LOG"
say "pipeline on the Air finished; training running on the mini"
