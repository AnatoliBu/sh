---
artifact_type: reference
authority_tier: Tier A
status: foundation
source_type: internal-source-of-truth
topics:
  - tls
  - certificates
  - pki
  - service-identity
domains:
  - sysadmin
  - sre
  - security
  - devops
owner: Internal platform, security, or infrastructure team
last_checked: TODO
source_url: TODO
---

# Reference: Internal Certificate Management

## Authority tier

Tier A

## Status

foundation / internal-placeholder

## Owner / maintainer

Internal platform, security, or infrastructure team.

## URL

TODO: link to the real certificate management runbook or system.

## Last checked

TODO

## Scope

Expected certificate ownership, issuer, renewal process, TLS termination points, and operational runbooks.

## Why trusted

TLS debugging must compare observed certificates against the expected certificate source and ownership model.

## Caveats

This is a placeholder until the real internal source is linked.

## Agent-facing artifacts that may consume this reference

- [Sysadmin Agent](../sysadmin/agent.md)
- [TLS Certificate Debug](../sysadmin/skills/tls-cert-debug.md)

## Extracted rules

- Identify the TLS termination point before proposing remediation.
- Certificate replacement or renewal requires approval and audit trail.

## Do not use this source for

- DNS authority.
- Application-layer authentication policy.

## Related references

- [Internal DNS Source of Truth](./internal-dns-source-of-truth.md)
