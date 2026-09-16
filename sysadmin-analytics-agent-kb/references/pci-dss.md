---
artifact_type: reference
authority_tier: Tier A
status: foundation
source_type: standard
topics:
  - payments
  - security
  - pci-dss
  - cardholder-data
domains:
  - browser-automation
owner: PCI Security Standards Council
last_checked: 2026-09-16
source_url: https://www.pcisecuritystandards.org/standards/pci-dss/
---

# Reference: PCI DSS

## Authority tier

Tier A

## Status

foundation

## Owner / maintainer

PCI Security Standards Council

## URL

https://www.pcisecuritystandards.org/standards/pci-dss/

## Last checked

2026-09-16

## Scope

Baseline technical and operational requirements for entities that store, process, transmit, or can
impact the security of payment account data.

## Why trusted

Official PCI Security Standards Council material.

## Caveats

PCI scope depends on the actual payment architecture, contractual roles, and data paths. A skill can
identify likely scope-expanding design choices but cannot determine compliance by itself.

## Extracted rules

- Minimize the systems that can see or influence cardholder data.
- Do not place PAN/CVV or other payment secrets in logs, traces, screenshots, recordings, prompts,
  analytics, or general-purpose databases.
- Prefer hosted/tokenized payment surfaces and secret vault boundaries over application-level card
  handling.
- Treat any browser/session recording that can capture payment secrets as sensitive infrastructure.

## Do not use this source for

Site-automation permission, issuer rules, or provider-specific browser behavior.

## Related references

- [OWASP Session Management Cheat Sheet](./owasp-session-management.md)
- [Playwright Documentation](./playwright-docs.md)
