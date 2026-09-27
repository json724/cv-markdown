#!/usr/bin/env bash
# Render a CV markdown file to an ATS-friendly PDF: ./build.sh json_cv_2026.md
set -euo pipefail
src="${1:-json_cv_2026.md}"
out="${src%.md}.pdf"
tmp="$(mktemp -d)"
pandoc "$src" -f markdown-smart -t html -s --metadata pagetitle="$(basename "${src%.md}")" \
  --css "$PWD/build/cv.css" --embed-resources -o "$tmp/cv.html"
google-chrome --headless --disable-gpu --no-sandbox --no-pdf-header-footer \
  --print-to-pdf="$PWD/$out" "file://$tmp/cv.html" 2>/dev/null
rm -rf "$tmp"
echo "wrote $out"
