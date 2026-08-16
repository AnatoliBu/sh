#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)"
KB="$ROOT/sysadmin-analytics-agent-kb"
WORK="$ROOT/quartz-work"
OUT="$KB/public"
QUARTZ_BRANCH="${QUARTZ_BRANCH:-agent-kb-v5}"
AUTH_TOKEN="${QUARTZ_REPO_TOKEN:-${GITHUB_TOKEN:-}}"

rm -rf "$WORK"

if [ -n "$AUTH_TOKEN" ]; then
  git clone --depth 1 --branch "$QUARTZ_BRANCH" "https://x-access-token:${AUTH_TOKEN}@github.com/AnatoliBu/quartz.git" "$WORK"
else
  git clone --depth 1 --branch "$QUARTZ_BRANCH" "https://github.com/AnatoliBu/quartz.git" "$WORK"
fi

rm -rf "$WORK/content"
mkdir -p "$WORK/content"

# A publishable domain is any first-level KB directory that contains agent.md.
# This deliberately avoids a hard-coded domain list: adding foo/agent.md is enough
# for the domain to appear in Quartz on the next successful main build.
mapfile -t DOMAIN_DIRS < <(
  find "$KB" -mindepth 2 -maxdepth 2 -type f -name agent.md -printf '%h\n' \
    | sort -u
)

if [ "${#DOMAIN_DIRS[@]}" -eq 0 ]; then
  echo "No publishable domains found (expected */agent.md)" >&2
  exit 1
fi

cat > "$WORK/content/index.md" <<'EOF'
---
title: Agent KB
artifact_type: index
status: foundation
domain: shared
---

# Agent KB

Curated source-of-truth references and agent harnesses.

## Domains

EOF

for domain_path in "${DOMAIN_DIRS[@]}"; do
  domain="$(basename "$domain_path")"
  title="$(awk '/^# / {sub(/^# /, ""); print; exit}' "$domain_path/agent.md")"
  if [ -z "$title" ]; then
    title="$domain"
  fi
  printf -- '- [%s](%s/agent.md)\n' "$title" "$domain" >> "$WORK/content/index.md"
done

cat >> "$WORK/content/index.md" <<'EOF'

## Knowledge base

- [References](references/README.md)
- [Global Rules](shared/rules/global-rules.md)
- [Roadmap](roadmap.md)

## Graph artifacts

- [Link Graph JSON](generated/link-graph.json)
- [Link Graph DOT](generated/link-graph.dot)
EOF

# Shared cross-domain content is explicit; domains themselves are discovered.
for item in references shared roadmap.md; do
  if [ -e "$KB/$item" ]; then
    cp -R "$KB/$item" "$WORK/content/"
  fi
done

for domain_path in "${DOMAIN_DIRS[@]}"; do
  cp -R "$domain_path" "$WORK/content/"
done

rm -rf "$WORK/content/research" "$WORK/content/site"
rm -rf "$WORK/content/references/tooling" "$WORK/content/references/sysadmin" "$WORK/content/references/analytics"
rm -f "$WORK/content/README.md"

if find "$WORK/content" \( -path '*/research/*' -o -path '*/site/*' -o -path '*/references/sysadmin/*' -o -path '*/references/analytics/*' -o -path '*/references/tooling/*' -o -name 'quartz-deploy.md' -o -name 'github-pages.md' -o -name 'quartz.md' \) | grep -q .; then
  echo "Non-curated docs leaked into Quartz content" >&2
  exit 1
fi

# Guard against a silent publish regression: every discovered domain must be present.
for domain_path in "${DOMAIN_DIRS[@]}"; do
  domain="$(basename "$domain_path")"
  if [ ! -f "$WORK/content/$domain/agent.md" ]; then
    echo "Publishable domain missing from Quartz content: $domain" >&2
    exit 1
  fi
done

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
