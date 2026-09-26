#!/bin/bash
# Render figures/tex/arm_*.tex to figures/arm_*.pdf (+ PNG previews).
#
# Two things this handles that a bare pdflatex call does not:
#
#  1. The project lives under iCloud, so its path contains spaces
#     ("Mobile Documents", "New idea"). LaTeX's \subimport cannot follow a path
#     with spaces, so everything is copied to a scratch dir and the absolute
#     \subimport is rewritten to a relative one.
#  2. TinyTeX is installed per-user and its PATH entry needs admin rights to
#     register globally, so it is added here instead.
#
# Usage:  bash tools/build_figures.sh [arm_D ...]     (default: all)
set -euo pipefail

export PATH="$HOME/Library/TinyTeX/bin/universal-darwin:$PATH"
command -v pdflatex >/dev/null || { echo "pdflatex not found — is TinyTeX installed?"; exit 1; }

PROJ="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
BUILD="${TMPDIR:-/tmp}/pnnbuild"
rm -rf "$BUILD"; mkdir -p "$BUILD"
cp -R "$PROJ/tools/PlotNeuralNet/layers" "$BUILD/"

ARMS=("$@")
[ ${#ARMS[@]} -eq 0 ] && ARMS=(arm_A arm_B arm_B_wide arm_C arm_C_wide arm_D)

for a in "${ARMS[@]}"; do
  sed 's|\\subimport{.*}{init}|\\subimport{layers/}{init}|' \
      "$PROJ/figures/tex/$a.tex" > "$BUILD/$a.tex"
done

cd "$BUILD"
fail=0
for a in "${ARMS[@]}"; do
  printf "%-12s " "$a"
  if pdflatex -interaction=nonstopmode -halt-on-error "$a.tex" >"$a.log" 2>&1; then
    cp "$a.pdf" "$PROJ/figures/"
    echo "OK"
  else
    echo "FAIL — see $BUILD/$a.log"
    grep -E "^!" "$a.log" | head -3 || true
    fail=1
  fi
done

# PNG previews via Quick Look (no poppler on this machine)
mkdir -p "$PROJ/figures/png"
for a in "${ARMS[@]}"; do
  [ -f "$PROJ/figures/$a.pdf" ] && \
    qlmanage -t -s 1800 -o "$PROJ/figures/png" "$PROJ/figures/$a.pdf" >/dev/null 2>&1 || true
done

echo
echo "PDFs  -> $PROJ/figures/"
echo "PNGs  -> $PROJ/figures/png/"
exit $fail
