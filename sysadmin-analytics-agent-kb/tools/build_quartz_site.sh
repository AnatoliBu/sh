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
domain: shared
---

# Agent KB

Curated knowledge base for reliable sysadmin/SRE/network and analytics/product-analytics agents.

## Start here

- [References](references/README.md)
- [Sysadmin Agent](sysadmin/agent.md)
- [Analytics Agent](analytics/agent.md)
- [Global Rules](shared/rules/global-rules.md)
- [Roadmap](roadmap.md)

## Graph artifacts

- [Link Graph JSON](generated/link-graph.json)
- [Link Graph DOT](generated/link-graph.dot)
EOF

for item in references shared sysadmin analytics roadmap.md; do
  if [ -e "$KB/$item" ]; then
    cp -R "$KB/$item" "$WORK/content/"
  fi
done

rm -rf "$WORK/content/research" "$WORK/content/site" "$WORK/content/agents" "$WORK/content/rules" "$WORK/content/skills"
rm -rf "$WORK/content/references/tooling" "$WORK/content/references/sysadmin" "$WORK/content/references/analytics"
rm -f "$WORK/content/README.md"

if find "$WORK/content" \( -path '*/research/*' -o -path '*/site/*' -o -path '*/agents/*' -o -path '*/rules/*' -o -path '*/skills/*' -o -path '*/references/sysadmin/*' -o -path '*/references/analytics/*' -o -path '*/references/tooling/*' -o -name 'quartz-deploy.md' -o -name 'github-pages.md' -o -name 'quartz.md' \) | grep -q .; then
  echo "Non-curated docs leaked into Quartz content" >&2
  exit 1
fi

mkdir -p "$WORK/content/generated"
if [ -d "$KB/generated" ]; then
  cp -R "$KB/generated/." "$WORK/content/generated/"
fi

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
