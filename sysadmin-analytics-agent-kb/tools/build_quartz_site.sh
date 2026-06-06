#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)"
KB="$ROOT/sysadmin-analytics-agent-kb"
WORK="$ROOT/quartz-work"
OUT="$KB/public"
QUARTZ_BRANCH="${QUARTZ_BRANCH:-agent-kb-v5}"

rm -rf "$WORK"

if [ -z "${QUARTZ_REPO_TOKEN:-}" ]; then
  echo "QUARTZ_REPO_TOKEN is required to clone private repo AnatoliBu/quartz.git" >&2
  echo "Create a fine-grained GitHub token with read access to AnatoliBu/quartz and add it as a repository secret." >&2
  exit 1
fi

git clone --depth 1 --branch "$QUARTZ_BRANCH" "https://x-access-token:${QUARTZ_REPO_TOKEN}@github.com/AnatoliBu/quartz.git" "$WORK"

rm -rf "$WORK/content"
mkdir -p "$WORK/content"

cat > "$WORK/content/index.md" <<'EOF'
---
title: Agent KB
artifact_type: index
status: foundation
domain: tooling
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

# Curated content only. Do not copy staging/publishing folders.
for item in references agents rules skills sysadmin analytics roadmap.md; do
  if [ -e "$KB/$item" ]; then
    cp -R "$KB/$item" "$WORK/content/"
  fi
done

# Hard denylist: fail closed if non-curated docs leak into published content.
rm -rf "$WORK/content/references/tooling"
rm -rf "$WORK/content/site"
rm -rf "$WORK/content/research"
rm -f "$WORK/content/README.md"

if find "$WORK/content" \( \
  -path "$WORK/content/research" -o \
  -path "$WORK/content/research/*" -o \
  -path "$WORK/content/site" -o \
  -path "$WORK/content/site/*" -o \
  -path "$WORK/content/references/tooling" -o \
  -path "$WORK/content/references/tooling/*" -o \
  -name 'quartz-deploy.md' -o \
  -name 'github-pages.md' -o \
  -name 'quartz.md' \
\) | grep -q .; then
  echo "Non-curated docs leaked into Quartz content:" >&2
  find "$WORK/content" \( \
    -path "$WORK/content/research" -o \
    -path "$WORK/content/research/*" -o \
    -path "$WORK/content/site" -o \
    -path "$WORK/content/site/*" -o \
    -path "$WORK/content/references/tooling" -o \
    -path "$WORK/content/references/tooling/*" -o \
    -name 'quartz-deploy.md' -o \
    -name 'github-pages.md' -o \
    -name 'quartz.md' \
  ) >&2
  exit 1
fi

mkdir -p "$WORK/content/generated"
if [ -d "$KB/generated" ]; then
  cp -R "$KB/generated/." "$WORK/content/generated/"
fi

python - <<'PY'
from pathlib import Path

root = Path('quartz-work')
agent_ignore = '["private", "templates", ".obsidian", "archive", "research", "site", "references/tooling", "README.md"]'

ts_config = root / 'quartz.config.ts'
yaml_config = root / 'quartz.config.default.yaml'

if ts_config.exists():
    text = ts_config.read_text(encoding='utf-8')
    text = text.replace('pageTitle: "apps-api-tests"', 'pageTitle: "Agent KB"')
    text = text.replace('pageTitle: "Quartz 4"', 'pageTitle: "Agent KB"')
    text = text.replace('pageTitleSuffix: " | QA Notes"', 'pageTitleSuffix: " | Source of Truth"')
    text = text.replace('pageTitleSuffix: ""', 'pageTitleSuffix: " | Source of Truth"')
    text = text.replace('locale: "ru-RU"', 'locale: "en-US"')
    text = text.replace('baseUrl: "localhost:8080"', 'baseUrl: "anatolibu.github.io/sh"')
    text = text.replace('baseUrl: "quartz.jzhao.xyz"', 'baseUrl: "anatolibu.github.io/sh"')
    text = text.replace('ignorePatterns: ["private", "templates", ".obsidian", "archive", "research", "site", "references/tooling"]', f'ignorePatterns: {agent_ignore}')
    text = text.replace('ignorePatterns: ["private", "templates", ".obsidian", "archive"]', f'ignorePatterns: {agent_ignore}')
    text = text.replace('ignorePatterns: ["private", "templates", ".obsidian"]', f'ignorePatterns: {agent_ignore}')
    ts_config.write_text(text, encoding='utf-8')
elif yaml_config.exists():
    text = yaml_config.read_text(encoding='utf-8')
    text = text.replace('pageTitle: Quartz 5', 'pageTitle: Agent KB')
    text = text.replace('pageTitleSuffix: ""', 'pageTitleSuffix: " | Source of Truth"')
    text = text.replace('baseUrl: quartz.jzhao.xyz', 'baseUrl: anatolibu.github.io/sh')
    text = text.replace('locale: en-US', 'locale: en-US')
    text = text.replace('analytics:\n    provider: plausible', 'analytics: null')
    text = text.replace('ignorePatterns:\n    - private\n    - templates\n    - .obsidian', 'ignorePatterns:\n    - private\n    - templates\n    - .obsidian\n    - archive\n    - research\n    - site\n    - references/tooling\n    - README.md')
    (root / 'quartz.config.yaml').write_text(text, encoding='utf-8')
else:
    raise SystemExit('No supported Quartz config found: expected quartz.config.ts or quartz.config.default.yaml')
PY

cd "$WORK"
npm ci
if npm run | grep -q "install-plugins"; then
  npm run install-plugins
fi
npx quartz build

rm -rf "$OUT"
mkdir -p "$OUT"
cp -R "$WORK/public/." "$OUT/"
touch "$OUT/.nojekyll"
