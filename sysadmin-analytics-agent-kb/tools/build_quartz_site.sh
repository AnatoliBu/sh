#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)"
KB="$ROOT/sysadmin-analytics-agent-kb"
WORK="$ROOT/quartz-work"
OUT="$KB/public"

rm -rf "$WORK"

if [ -z "${QUARTZ_REPO_TOKEN:-}" ]; then
  echo "QUARTZ_REPO_TOKEN is required to clone private repo AnatoliBu/quartz.git" >&2
  echo "Create a fine-grained GitHub token with read access to AnatoliBu/quartz and add it as a repository secret." >&2
  exit 1
fi

git clone --depth 1 --branch v4 "https://x-access-token:${QUARTZ_REPO_TOKEN}@github.com/AnatoliBu/quartz.git" "$WORK"

rm -rf "$WORK/content"
mkdir -p "$WORK/content"

cat > "$WORK/content/index.md" <<'EOF'
---
title: Agent KB
---

# Agent KB

Curated knowledge base for reliable sysadmin/SRE/network and analytics/product-analytics agents.

## Start here

- [References](references/README.md)
- [Sysadmin Agent](agents/sysadmin-agent.md)
- [Analytics Agent](agents/analytics-agent.md)
- [Global Rules](rules/global-rules.md)
- [Roadmap](roadmap.md)

## Graph artifacts

- [Link Graph JSON](generated/link-graph.json)
- [Link Graph DOT](generated/link-graph.dot)

Research notes, site deployment notes, and tooling docs are intentionally excluded from the published knowledge graph.
EOF

for item in references agents rules skills sysadmin analytics roadmap.md README.md; do
  if [ -e "$KB/$item" ]; then
    cp -R "$KB/$item" "$WORK/content/"
  fi
done

rm -rf "$WORK/content/references/tooling"
rm -rf "$WORK/content/site"
rm -rf "$WORK/content/research"

mkdir -p "$WORK/content/generated"
if [ -d "$KB/generated" ]; then
  cp -R "$KB/generated/." "$WORK/content/generated/"
fi

python - <<'PY'
from pathlib import Path

config = Path('quartz-work/quartz.config.ts')
text = config.read_text(encoding='utf-8')
text = text.replace('pageTitle: "apps-api-tests"', 'pageTitle: "Agent KB"')
text = text.replace('pageTitleSuffix: " | QA Notes"', 'pageTitleSuffix: " | Source of Truth"')
text = text.replace('locale: "ru-RU"', 'locale: "en-US"')
text = text.replace('baseUrl: "localhost:8080"', 'baseUrl: "anatolibu.github.io/sh"')
text = text.replace('ignorePatterns: ["private", "templates", ".obsidian", "archive"]', 'ignorePatterns: ["private", "templates", ".obsidian", "archive", "research", "site", "references/tooling"]')
config.write_text(text, encoding='utf-8')
PY

cd "$WORK"
npm ci
npx quartz build

rm -rf "$OUT"
mkdir -p "$OUT"
cp -R "$WORK/public/." "$OUT/"
touch "$OUT/.nojekyll"
