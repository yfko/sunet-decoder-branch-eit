"""Can a conventional method pull the heart out of a mixed EIT image?

The manuscript's premise is that in a reconstructed lung-EIT image the cardiac
component cannot be obtained directly — the lung dominates and the two are
blurred together. That is a claim about SEPARABILITY, not about energy, and it
is testable without training anything: apply the thresholding that clinical ROI
methods use to the MIXED image, and score what comes out against each organ's
own reconstruction.

If the premise holds, the lung comes out and the heart does not.

Reference for each organ: the quarter-amplitude set of that organ's own
reconstruction — the same target definition the study's DSC uses.
"""
import sys, glob; sys.path.insert(0, 'tools')
from pathlib import Path
import numpy as np
import h5py

QA = 0.25

def load(p):
    with h5py.File(p, "r") as f:
        g = lambda k: np.array(f[k]).transpose(0, 2, 1)
        return g("recon_mixed"), g("recon_lung"), g("recon_heart")

def qa(img, fov):
    a = np.abs(img) * fov
    m = a.max()
    return a > QA * m if m > 0 else np.zeros_like(a, bool)

def dsc(a, b):
    s = a.sum() + b.sum()
    return 1.0 if s == 0 else 2.0 * (a & b).sum() / s

def report(name, path):
    M, L, H = load(path)
    fov = np.isfinite(M).all(axis=0)
    for a in (M, L, H):
        np.nan_to_num(a, copy=False)
    n = len(M)
    print(f"\n=== {name}  ({n} 筆) ===")

    rows = []
    for i in range(n):
        mixed = M[i]
        # 臨床閾值法：對混合影像取 25% 最大振幅
        # 負值區 = 通氣（肺，sigma < background）；正值區 = 心（sigma > background）
        amp = np.abs(mixed) * fov
        thr = QA * amp.max()
        neg = (mixed < -thr) & fov          # 取負向成分
        pos = (mixed >  thr) & fov          # 取正向成分
        both = amp > thr                    # 不分正負

        tL, tH = qa(L[i], fov), qa(H[i], fov)
        rows.append([
            dsc(both, tL), dsc(neg, tL),    # 肺：不分正負 / 只取負向
            dsc(both, tH), dsc(pos, tH),    # 心：不分正負 / 只取正向
            tL.sum(), tH.sum(),
        ])
    r = np.array(rows, float)
    lab = ["肺 |img|>thr", "肺 只取負向", "心 |img|>thr", "心 只取正向"]
    for k in range(4):
        print(f"  {lab[k]:14s} DSC {r[:,k].mean():.4f} ± {r[:,k].std():.4f}"
              f"   中位數 {np.median(r[:,k]):.4f}")
    print(f"  參考區域大小: 肺 {r[:,4].mean():.0f} px, 心 {r[:,5].mean():.0f} px")

for name, path in (("圓柱體模（研究一/二）", "data/v2/dataset.mat"),
                   ("真實成人胸腔",           "data/probe_thorax/dataset.mat")):
    if Path(path).exists():
        report(name, path)
    else:
        print(f"\n({path} 不存在，略過)")
