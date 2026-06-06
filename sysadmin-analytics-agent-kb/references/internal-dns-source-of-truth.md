---
artifact_type: reference
authority_tier: Tier A
status: foundation
source_type: internal-source-of-truth
topics:
  - dns
  - network-source-of-truth
  - service-discovery
domains:
  - sysadmin
  - sre
  - network
  - devops
owner: Internal platform, network, or infrastructure team
last_checked: TODO
source_url: TODO
---

# Reference: Internal DNS Source of Truth

## Authority tier

Tier A

## Status

foundation / internal-placeholder

## Owner / maintainer

Internal platform, network, or infrastructure team.

## URL

TODO: link to the real DNS source of truth.

## Last checked

TODO

## Scope

Expected DNS zones, records, ownership, environments, TTL expectations, and change process.

## Why trusted

DNS debugging must compare observed resolver answers against intended records.

## Caveats

This is a placeholder until the real internal source is linked.

## Agent-facing artifacts that may consume this reference

- [Sysadmin Agent](../sysadmin/agent.md)
- [DNS Debug](../sysadmin/skills/dns-debug.md)

## Extracted rules

- Identify the authoritative DNS source before diagnosing mismatch.
- Resolver results are observations, not authority.
- DNS changes require explicit approval and audit trail.

## Do not use this source for

- Certificate ownership.
- Full network path analysis.

## Related references

- [NetBox](./netbox.md)
