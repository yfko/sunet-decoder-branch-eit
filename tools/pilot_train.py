"""SNR pilot, training half. PREREGISTRATION_HEART.md s7.

Trains ARM B ONLY, one seed per SNR level, and reports heart-DSC median and
5th percentile. Computes no contrast between arms; no arm other than B is
trained here. Its purpose is to characterise task difficulty so the primary
SNR can be fixed before the study is registered.
"""
import sys, json; sys.path.insert(0, 'tools')
from pathlib import Path
import numpy as np, torch
import train_arms as T
from evaluate import per_image_metrics

LEVELS = [int(x) for x in (sys.argv[1:] or [60, 50, 40, 30, 20])]
dev = "mps" if torch.backends.mps.is_available() else "cpu"
out = Path('runs_pilot'); out.mkdir(exist_ok=True)
res = {}

for snr in LEVELS:
    p = Path(f'data/pilot_snr{snr:02d}/dataset.mat')
    if not p.exists():
        print(f"SNR {snr}: no dataset, skipped"); continue
    mixed, lung, heart, idx, mask = T.load_dataset(p)
    mu, sd, (mixed, lung, heart) = T.normalise(mixed[idx['train']], mask,
                                               mixed, lung, heart)
    meta = T.run_one("B", 0, (mixed, lung, heart, idx, mask), dev, out)
    # rename so each level keeps its own record
    for ext in ('.pt', '.json'):
        (out / f"B_seed0{ext}").rename(out / f"B_snr{snr:02d}{ext}")

    model = __import__('arms').build_arm("B").to(dev)
    model.load_state_dict(torch.load(out / f"B_snr{snr:02d}.pt", map_location=dev))
    model.eval()
    te = idx['test']
    x = torch.from_numpy(mixed[te]).unsqueeze(1)
    with torch.no_grad():
        pred = torch.cat([model(x[i:i+32].to(dev)).cpu()
                          for i in range(0, len(x), 32)]).numpy()
    d = np.array([per_image_metrics(pred[i, 1], heart[te][i], sd, mask)['dsc']
                  for i in range(len(te))])
    res[snr] = dict(n=len(d), median=float(np.median(d)),
                    p05=float(np.percentile(d, 5)), min=float(d.min()),
                    frac_gt99=float(np.mean(d > 0.99)),
                    epochs=meta['epochs_run'], minutes=meta['minutes'])
    r = res[snr]
    print(f"\n>>> SNR {snr} dB  heart DSC: median {r['median']:.4f}  "
          f"p05 {r['p05']:.4f}  min {r['min']:.4f}  >0.99 {100*r['frac_gt99']:.0f}%"
          f"  ({r['epochs']} ep, {r['minutes']:.1f} min)\n")

Path('runs_pilot/pilot_snr_result.json').write_text(json.dumps(res, indent=2))
print("\n=== 選取規則: 取『median <= 0.98 且 p05 <= 0.90』的最高 SNR ===")
ok = [s for s in sorted(res, reverse=True)
      if res[s]['median'] <= 0.98 and res[s]['p05'] <= 0.90]
print(f"合格: {ok}   ->  " + (f"選 {ok[0]} dB" if ok else "無合格值，需延伸到 15/10 dB"))
