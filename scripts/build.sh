#!/bin/sh

set -eu

repo_root=$(CDPATH= cd -- "$(dirname -- "$0")/.." && pwd)
cd "$repo_root"

# Keep every public Markdown page deliberately placed in the progressive nav.
find docs -type f -name '*.md' -print | sort | while IFS= read -r doc; do
  nav_path=${doc#docs/}
  nav_count=$(awk -v path="$nav_path" '
    {
      marker = ": " path
      if (length($0) >= length(marker) && substr($0, length($0) - length(marker) + 1) == marker) {
        count++
      }
    }
    END { print count + 0 }
  ' mkdocs.yml)

  if [ "$nav_count" -ne 1 ]; then
    echo "Expected $nav_path exactly once in mkdocs.yml nav; found $nav_count" >&2
    exit 1
  fi
done

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
test -f dist/docs/search.html
test -f dist/docs/search/search_index.json

# These files control the two route families and the response headers at the
# deployment edge. Keep the checks beside the artifact allowlist they protect.
grep -Fqx '/docs /docs/ 301' dist/_redirects
grep -Fq 'X-Content-Type-Options: nosniff' dist/_headers
grep -Fq 'X-Frame-Options: DENY' dist/_headers
grep -Fqx 'Sitemap: https://kodade.com/docs/sitemap.xml' dist/robots.txt

if find dist -type f \( -name '*.md' -o -name '*.dc.html' \) -print -quit | grep -q .; then
  echo 'Unexpected source or design file in deployment artifact' >&2
  exit 1
fi

PYTHONDONTWRITEBYTECODE=1 python3 scripts/validate_site.py dist
PYTHONDONTWRITEBYTECODE=1 python3 -m unittest -v scripts/test_validate_site.py
