#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)"
KB="$ROOT/sysadmin-analytics-agent-kb"
WORK="$ROOT/quartz-work"
OUT="$KB/public"

rm -rf "$WORK"
git clone --depth 1 --branch v5 https://github.com/jackyzha0/quartz.git "$WORK"

rm -rf "$WORK/content"
mkdir -p "$WORK/content"

cat > "$WORK/content/index.md" <<'EOF'
# Agent KB

Knowledge base for reliable sysadmin/SRE/network and analytics/product-analytics agents.

## Start here

- [References](references/README.md)
- [Sysadmin Agent](agents/sysadmin-agent.md)
- [Analytics Agent](agents/analytics-agent.md)
- [Global Rules](rules/global-rules.md)
- [Quartz Deploy Plan](site/quartz-deploy.md)
- [Roadmap](roadmap.md)

## Graph artifacts

- [Link Graph JSON](generated/link-graph.json)
- [Link Graph DOT](generated/link-graph.dot)

The site is rendered by Quartz. CI remains responsible for validating links and source-of-truth references.
EOF

for item in references agents rules sysadmin analytics research site roadmap.md README.md; do
  if [ -e "$KB/$item" ]; then
    cp -R "$KB/$item" "$WORK/content/"
  fi
done

mkdir -p "$WORK/content/generated"
if [ -d "$KB/generated" ]; then
  cp -R "$KB/generated/." "$WORK/content/generated/"
fi

python - <<'PY'
from pathlib import Path

root = Path('quartz-work')
config = root / 'quartz.config.default.yaml'
text = config.read_text(encoding='utf-8')
text = text.replace('pageTitle: Quartz 5', 'pageTitle: Agent KB')
text = text.replace('pageTitleSuffix: ""', 'pageTitleSuffix: " - Source of Truth"')
text = text.replace('baseUrl: quartz.jzhao.xyz', 'baseUrl: anatolibu.github.io/sh')
text = text.replace('locale: en-US', 'locale: en-US')
(root / 'quartz.config.yaml').write_text(text, encoding='utf-8')
PY

cd "$WORK"
npm ci
npx quartz plugin install
npx quartz build

rm -rf "$OUT"
mkdir -p "$OUT"
cp -R "$WORK/public/." "$OUT/"
touch "$OUT/.nojekyll"
