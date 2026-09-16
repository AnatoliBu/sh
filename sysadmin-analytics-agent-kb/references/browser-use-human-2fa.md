---
artifact_type: reference
authority_tier: Tier A
status: useful-after-audit
source_type: official-docs
topics:
  - browser-automation
  - browser-use
  - 2fa
  - human-handoff
domains:
  - browser-automation
owner: Browser Use
last_checked: 2026-09-16
source_url: https://docs.browser-use.com/cloud/guides/2fa
---

# Reference: Browser Use 2FA and Human Handoff

## Authority tier

Tier A

## Status

useful-after-audit

## Owner / maintainer

Browser Use

## URL

https://docs.browser-use.com/cloud/guides/2fa

## Last checked

2026-09-16

## Scope

Browser Use patterns for persistent profiles, human-in-the-loop 2FA, email verification and live
browser takeover.

## Why trusted

Official Browser Use documentation for its product capabilities.

## Caveats

The page also demonstrates putting a TOTP seed directly into an agent prompt. That pattern conflicts
with this KB's secret-boundary requirements and must not be adopted for end-user production flows.

## Extracted rules

- Prefer login-once persistent profiles when the relying party permits durable sessions.
- For end-user products, prefer human takeover in the same session for MFA and other high-trust
  authentication ceremonies.
- Do not place passwords, TOTP seeds, recovery codes or payment secrets in prompts or ordinary logs.
- Treat email-code automation as credential access requiring explicit scope and isolation.
- Re-authentication is a normal state, not an exceptional crash.

## Do not use this source for

Justifying autonomous possession of a user's authenticator secret.

## Related references

- [Browser Use Authentication Profiles](./browser-use-authentication.md)
- [WebAuthn Level 3](./w3c-webauthn-level-3.md)
