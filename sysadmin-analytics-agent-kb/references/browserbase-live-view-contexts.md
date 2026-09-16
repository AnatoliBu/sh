---
artifact_type: reference
authority_tier: Tier A
status: foundation
source_type: official-docs
topics:
  - browser-automation
  - browserbase
  - human-handoff
  - session-context
domains:
  - browser-automation
owner: Browserbase
last_checked: 2026-09-16
source_url: https://docs.browserbase.com/platform/browser/observability/session-live-view
---

# Reference: Browserbase Live View and Session Contexts

## Authority tier

Tier A

## Status

foundation

## Owner / maintainer

Browserbase

## URL

https://docs.browserbase.com/platform/browser/observability/session-live-view

## Last checked

2026-09-16

## Scope

Managed remote browser sessions, Live View for interactive human takeover, session observability,
and Browserbase contexts for reusing browser identity/authentication state.

## Why trusted

Official Browserbase platform documentation.

## Caveats

Capabilities, quotas, supported regions, anti-bot features, and plan boundaries change. Verify
current docs before encoding a provider-specific assumption into application logic.

## Extracted rules

- Treat human takeover as a first-class state transition, not an exceptional manual workaround.
- Keep the same browser session when handing control between automation and a human.
- Reuse a persistent context only when continuity is intentional; ephemeral sessions are safer for
  one-off sensitive operations.
- Keep provider viewer/session links short-lived and never expose provider API keys to end users.

## Do not use this source for

Generic Playwright locator design or PCI scope determination.

## Related references

- [Playwright Documentation](./playwright-docs.md)
- [OWASP Session Management Cheat Sheet](./owasp-session-management.md)
