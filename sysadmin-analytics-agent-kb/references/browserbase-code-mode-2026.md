---
artifact_type: reference
authority_tier: Tier B
status: useful-after-audit
source_type: vendor-perspective
topics:
  - browser-automation
  - code-mode
  - agent-tooling
  - typed-capabilities
domains:
  - browser-automation
owner: Browserbase
last_checked: 2026-09-16
source_url: https://www.browserbase.com/blog/code-mode-is-all-you-need
---

# Reference: Browserbase Code Mode 2026

## Authority tier

Tier B

## Status

useful-after-audit

## Owner / maintainer

Browserbase

## URL

https://www.browserbase.com/blog/code-mode-is-all-you-need

## Last checked

2026-09-16

## Scope

Browserbase's engineering thesis that capable agents often benefit from writing ordinary code
against a small set of typed capabilities rather than consuming very large bespoke tool catalogs.

## Why trusted

Useful primary engineering perspective from a browser-agent infrastructure vendor.

## Caveats

This is an architectural opinion, not a standard and not a controlled independent evaluation.
Applicability depends on model coding ability, sandbox quality, task shape and security boundaries.

## Extracted rules

- Consider code execution over a small typed capability surface when tool-catalog overhead becomes
  large.
- Enforce credentials, egress, write permissions, resource limits and audit below the generated code.
- Promote repeatedly successful exploratory code into deterministic tested adapters.
- Compare code-mode against workflow tools and direct Playwright on frozen tasks before standardizing.

## Do not use this source for

A blanket rule that every agent should receive arbitrary shell or browser-code execution.

## Related references

- [Agent Tooling sources](./model-context-protocol-spec.md)
- [Playwright Agent Runtime 2026](./playwright-agent-runtime-2026.md)
