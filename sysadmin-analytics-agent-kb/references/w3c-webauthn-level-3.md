---
artifact_type: reference
authority_tier: Tier A
status: foundation
source_type: standard
topics:
  - browser-automation
  - authentication
  - webauthn
  - passkeys
domains:
  - browser-automation
owner: W3C Web Authentication Working Group
last_checked: 2026-09-16
source_url: https://www.w3.org/TR/webauthn-3/
---

# Reference: WebAuthn Level 3

## Authority tier

Tier A

## Status

foundation

## Owner / maintainer

W3C Web Authentication Working Group

## URL

https://www.w3.org/TR/webauthn-3/

## Last checked

2026-09-16

## Scope

WebAuthn Level 3 public-key credentials and passkey ceremonies, relying-party scoping, authenticator
behavior and user-consent requirements.

## Why trusted

W3C Recommendation published 2026-08-25.

## Caveats

Automation frameworks may provide virtual authenticators for testing, but that does not remove
relying-party policy, user-consent or production-authenticator requirements.

## Extracted rules

- Model passkeys as scoped credentials bound to a relying party, not generic reusable secrets.
- Do not silently replace a required real user-consent ceremony with a virtual authenticator in a
  production user workflow.
- Treat exported virtual credential private keys as high-value authentication secrets.
- Keep passkey lifecycle and browser-profile lifecycle explicit and revocable.

## Do not use this source for

Vendor-specific browser automation APIs or authorization to bypass a site's authentication policy.

## Related references

- [Playwright Agent Runtime 2026](./playwright-agent-runtime-2026.md)
- [OWASP Session Management](./owasp-session-management.md)
