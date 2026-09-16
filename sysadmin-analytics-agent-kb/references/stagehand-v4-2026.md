---
artifact_type: reference
authority_tier: Tier A
status: useful-after-audit
source_type: official-changelog
topics:
  - browser-automation
  - stagehand
  - browser-extension
  - agent-runtime
domains:
  - browser-automation
owner: Browserbase Stagehand
last_checked: 2026-09-16
source_url: https://www.browserbase.com/changelog/stagehand-v4
---

# Reference: Stagehand v4 2026

## Authority tier

Tier A

## Status

useful-after-audit

## Owner / maintainer

Browserbase Stagehand

## URL

https://www.browserbase.com/changelog/stagehand-v4

## Last checked

2026-09-16

## Scope

Stagehand v4 architecture announced 2026-08-10: more browser-resident execution through an
extension, context-management changes, self-healing actions and iframe improvements.

## Why trusted

Official Stagehand product changelog for the release architecture.

## Caveats

The same page reports vendor benchmarks claiming roughly 2x Playwright speed and about 80% token
savings. Those figures are Browserbase's own benchmark and must not be copied as independent
performance evidence.

## Extracted rules

- Browser-resident execution can reduce CDP round trips and race windows; benchmark this on real
  workflows before adopting it as architecture.
- Keep Stagehand behind an adapter so major runtime revisions do not leak through merchant logic.
- Treat self-healing as a recovery aid, not proof that the intended business action occurred.

## Do not use this source for

Neutral performance comparisons with Playwright or competing providers.

## Related references

- [Stagehand](./browserbase-stagehand.md)
- [Stagehand Agent Modes](./stagehand-agent-modes.md)
