#!/bin/sh

set -eu

repo_root=$(CDPATH= cd -- "$(dirname -- "$0")/.." && pwd)
cd "$repo_root"

rm -rf dist
install -d dist/fonts

# The landing page remains hand-authored at the repository root. Keep this
# allowlist explicit so design notes and local artifacts cannot be deployed.
install -m 0644 index.html styles.css favicon.svg dist/
install -m 0644 fonts/jetbrains-mono-latin.woff2 dist/fonts/
install -m 0644 public/404.html public/_headers public/_redirects public/robots.txt dist/

PYTHONDONTWRITEBYTECODE=1 python3 -m mkdocs build --strict --clean --config-file mkdocs.yml

# Protect the landing page's current bytes and the curated artifact boundary.
cmp -s index.html dist/index.html
cmp -s styles.css dist/styles.css
cmp -s favicon.svg dist/favicon.svg
cmp -s fonts/jetbrains-mono-latin.woff2 dist/fonts/jetbrains-mono-latin.woff2

for forbidden in README.md DESIGN.md SITE-PLAN.md DOCS-PLAN.md CLAUDE.md screenshots .wrangler; do
  if [ -e "dist/$forbidden" ]; then
    echo "Unexpected deployment artifact: dist/$forbidden" >&2
    exit 1
  fi
done

test -f dist/index.html
test -f dist/docs/index.html
test -f dist/404.html
test -f dist/docs/404.html
test -f dist/docs/sitemap.xml
