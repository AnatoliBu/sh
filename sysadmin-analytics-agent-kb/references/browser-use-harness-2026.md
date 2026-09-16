---
artifact_type: reference
authority_tier: Tier A
status: useful-after-audit
source_type: official-changelog
topics:
  - browser-automation
  - browser-use
  - browser-harness
  - cost-controls
  - observability
domains:
  - browser-automation
owner: Browser Use
last_checked: 2026-09-16
source_url: https://browser-use.com/changelog
---

# Reference: Browser Use Browser Harness 2026

## Authority tier

Tier A

## Status

useful-after-audit

## Owner / maintainer

Browser Use

## URL

https://browser-use.com/changelog

## Last checked

2026-09-16

## Scope

Current Browser Harness API behavior announced in 2026: typed run/session states, cursor pagination,
session queues and interrupts, run event logs, configurable per-run spend caps and CAPTCHA handling
changes.

## Why trusted

Official product changelog for Browser Use Cloud.

## Caveats

Changelog entries are time-sensitive product documentation. Re-check the current OpenAPI/SDK before
coding against an announced endpoint or field.

## Extracted rules

- Give every autonomous run explicit runtime/step/token/money budgets where the provider supports
  them.
- Persist typed terminal states and make cancellation terminal-state semantics testable.
- Prefer event logs over opaque final answers when debugging an agent run.
- Keep follow-up/interrupt semantics explicit so user input cannot race silently with an active run.

## Do not use this source for

Comparative performance claims against other browser providers.

## Related references

- [Browser Use Authentication Profiles](./browser-use-authentication.md)
