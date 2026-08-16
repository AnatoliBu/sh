#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)"
KB="$ROOT/sysadmin-analytics-agent-kb"
WORK="$ROOT/quartz-work"
OUT="$KB/public"
QUARTZ_BRANCH="${QUARTZ_BRANCH:-agent-kb-v5}"
AUTH_TOKEN="${QUARTZ_REPO_TOKEN:-${GITHUB_TOKEN:-}}"
DOMAIN_MANIFEST="$WORK/.agent-kb-domains"

rm -rf "$WORK"

if [ -n "$AUTH_TOKEN" ]; then
  git clone --depth 1 --branch "$QUARTZ_BRANCH" "https://x-access-token:${AUTH_TOKEN}@github.com/AnatoliBu/quartz.git" "$WORK"
else
  git clone --depth 1 --branch "$QUARTZ_BRANCH" "https://github.com/AnatoliBu/quartz.git" "$WORK"
fi

rm -rf "$WORK/content"
mkdir -p "$WORK/content"

# Domain discovery, landing-page metadata, and counts have one source of truth.
# A publishable domain is any first-level KB directory containing agent.md.
python "$KB/tools/generate_quartz_index.py" \
  --kb "$KB" \
  --output "$WORK/content/index.md" \
  --manifest "$DOMAIN_MANIFEST"

mapfile -t DOMAINS < "$DOMAIN_MANIFEST"
if [ "${#DOMAINS[@]}" -eq 0 ]; then
  echo "No publishable domains found (expected */agent.md)" >&2
  exit 1
fi

# Shared cross-domain content is explicit; domains themselves are discovered.
for item in references shared roadmap.md; do
  if [ -e "$KB/$item" ]; then
    cp -R "$KB/$item" "$WORK/content/"
  fi
done

for domain in "${DOMAINS[@]}"; do
  cp -R "$KB/$domain" "$WORK/content/"
done

rm -rf "$WORK/content/research" "$WORK/content/site"
rm -rf "$WORK/content/references/tooling" "$WORK/content/references/sysadmin" "$WORK/content/references/analytics"
rm -f "$WORK/content/README.md"

if find "$WORK/content" \( -path '*/research/*' -o -path '*/site/*' -o -path '*/references/sysadmin/*' -o -path '*/references/analytics/*' -o -path '*/references/tooling/*' -o -name 'quartz-deploy.md' -o -name 'github-pages.md' -o -name 'quartz.md' \) | grep -q .; then
  echo "Non-curated docs leaked into Quartz content" >&2
  exit 1
fi

# Guard against a silent publish regression: every discovered domain must be present.
for domain in "${DOMAINS[@]}"; do
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
