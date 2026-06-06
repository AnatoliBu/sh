---
artifact_type: skill
authority_tier: Tier A
status: foundation
domain: network
owner: Agent KB
last_checked: 2026-06-06
---

# Skill: DNS Debug

## Purpose

Diagnose DNS resolution issues safely and systematically.

## Reference links

Authority references:

- [Internal DNS Source of Truth](../../references/internal-dns-source-of-truth.md)
- [NetBox](../../references/netbox.md)

## When to use

Use for DNS resolution mismatch, unexpected record values, propagation checks, or service discovery questions.

## Required context

- Name being resolved.
- Expected record and owner.
- Client location and resolver.
- Environment.
- Relevant zone/source-of-truth entry.

## Authority chain

1. [Internal DNS Source of Truth](../../references/internal-dns-source-of-truth.md).
2. [NetBox](../../references/netbox.md) or approved inventory.
3. Authoritative DNS response.
4. Recursive resolver observation.
5. Client-side cache observation.

## Workflow

1. Identify expected record from source of truth.
2. Query authoritative nameservers.
3. Query recursive resolvers.
4. Compare TTL, value, and record type.
5. Check split-horizon or environment-specific zones.
6. Check recent changes and propagation window.
7. Classify mismatch and owner.

## Output format

```markdown
# DNS Debug Report

## Question

## Expected source-of-truth record

## Observed resolver results

## Difference

## Likely cause

## Recommended next step

## Assumptions
```
