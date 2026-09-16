---
artifact_type: reference
authority_tier: Tier A
status: foundation
source_type: official-repo
topics:
  - browser-automation
  - stagehand
  - agentic-browser
  - playwright
domains:
  - browser-automation
owner: Browserbase
last_checked: 2026-09-16
source_url: https://github.com/browserbase/stagehand
---

# Reference: Stagehand

## Authority tier

Tier A

## Status

foundation

## Owner / maintainer

Browserbase

## URL

https://github.com/browserbase/stagehand

## Last checked

2026-09-16

## Scope

LLM-assisted browser automation built for workflows that mix natural-language actions/extraction
with programmatic browser control.

## Why trusted

Official Browserbase repository for Stagehand.

## Caveats

Semantic/LLM actions trade some determinism for resilience to UI variation. They should not replace
explicit state checks or policy gates around destructive and financial actions.

## Extracted rules

- Use semantic actions where selectors are expensive or unstable, not as a blanket replacement for
  deterministic code.
- Assert the page/business state before and after any consequential action.
- Prefer constrained observe/extract steps when the agent only needs to understand the page.
- Keep payment submit/cancel/change-plan actions explicit and idempotency-aware.

## Do not use this source for

Remote browser infrastructure guarantees or card-data compliance.

## Related references

- [Playwright Documentation](./playwright-docs.md)
- [Browserbase Live View and Session Contexts](./browserbase-live-view-contexts.md)
