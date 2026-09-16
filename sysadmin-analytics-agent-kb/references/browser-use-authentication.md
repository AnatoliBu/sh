---
artifact_type: reference
authority_tier: Tier A
status: useful-after-audit
source_type: official-docs
topics:
  - browser-automation
  - browser-use
  - authentication
  - persistent-profiles
domains:
  - browser-automation
owner: Browser Use
last_checked: 2026-09-16
source_url: https://docs.browser-use.com/cloud/guides/authentication
---

# Reference: Browser Use Authentication Profiles

## Authority tier

Tier A

## Status

useful-after-audit

## Owner / maintainer

Browser Use

## URL

https://docs.browser-use.com/cloud/guides/authentication

## Last checked

2026-09-16

## Scope

Browser Use persistent cloud profiles for cookies/local storage and per-user authenticated browser
sessions.

## Why trusted

Official Browser Use Cloud documentation.

## Caveats

A persistent profile is credential-bearing state. Provider convenience does not remove the need for
per-user isolation, deletion, access control, encryption and explicit retention policy.

## Extracted rules

- Use one persistent profile per end user when authenticated continuity is required.
- Persist the provider profile ID, not raw cookies, unless the design explicitly requires export.
- Always close/stop sessions through all success and error paths when profile persistence depends on
  orderly shutdown.
- Re-authentication must be an explicit workflow state when cookies expire or risk controls trigger.

## Do not use this source for

A general recommendation to save passwords or MFA secrets in model prompts.

## Related references

- [Browser Use 2FA and Human Handoff](./browser-use-human-2fa.md)
- [OWASP Session Management](./owasp-session-management.md)
