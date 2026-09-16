---
artifact_type: reference
authority_tier: Tier A
status: foundation
source_type: standard-guidance
topics:
  - security
  - session-management
  - authentication
  - cookies
domains:
  - browser-automation
owner: OWASP
last_checked: 2026-09-16
source_url: https://cheatsheetseries.owasp.org/cheatsheets/Session_Management_Cheat_Sheet.html
---

# Reference: OWASP Session Management Cheat Sheet

## Authority tier

Tier A

## Status

foundation

## Owner / maintainer

OWASP

## URL

https://cheatsheetseries.owasp.org/cheatsheets/Session_Management_Cheat_Sheet.html

## Last checked

2026-09-16

## Scope

Session identifiers, cookies, session lifecycle, transport protection, timeout, storage, fixation,
and handling of sensitive authenticated session state.

## Why trusted

OWASP Cheat Sheet Series is mature security guidance maintained by the application-security
community.

## Caveats

It is general application-security guidance, not provider-specific remote-browser documentation.

## Extracted rules

- Session identifiers must be unpredictable and must not contain sensitive business data.
- Authenticated browser state is a bearer credential: restrict access, lifetime, logging, and
  persistence.
- Prefer ephemeral/non-persistent session state when long-term reuse is not required.
- Destroy or revoke temporary sessions promptly after the workflow reaches a terminal state.

## Do not use this source for

Browser vendor feature selection or payment-network rules.

## Related references

- [PCI DSS](./pci-dss.md)
- [Playwright Documentation](./playwright-docs.md)
