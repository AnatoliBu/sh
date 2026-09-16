---
artifact_type: reference
authority_tier: Tier A
status: foundation
source_type: official-docs
topics:
  - browser-automation
  - steel
  - cloud-browser
  - observability
domains:
  - browser-automation
owner: Steel
last_checked: 2026-09-16
source_url: https://docs.steel.dev/
---

# Reference: Steel Browser Documentation

## Authority tier

Tier A

## Status

foundation

## Owner / maintainer

Steel

## URL

https://docs.steel.dev/

## Last checked

2026-09-16

## Scope

Managed and open-source browser infrastructure for agents: sessions, CDP connections, interactive
viewers, profiles, CAPTCHA integration, proxies, observability, and SDK/CLI integrations.

## Why trusted

Official Steel documentation.

## Caveats

Stealth/proxy features can reduce operational friction but must not be treated as authorization to
evade a site's security policy. Reliability for authenticated user accounts usually benefits from
stable identity and session continuity rather than arbitrary fingerprint rotation.

## Extracted rules

- Keep browser infrastructure separate from the business workflow so providers can be swapped.
- Prefer named session/profile lifecycles and evidence-backed debugging over blind retries.
- Use interactive viewing for authentication, MFA, or ambiguous states that need the user.
- Capture enough session evidence to debug failures, but redact or disable recording around
  credentials and payment secrets.

## Do not use this source for

Generic web application security requirements.

## Related references

- [Steel Agent Skills](./steel-agent-skills.md)
- [OWASP Session Management Cheat Sheet](./owasp-session-management.md)
