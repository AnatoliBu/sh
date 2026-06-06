# Skill: DNS Debug

## Purpose

Diagnose DNS resolution issues safely and systematically.

## Reference links

Authority references:

- [Internal DNS Source of Truth](../../references/sysadmin/internal-dns-source-of-truth.md)
- [NetBox](../../references/sysadmin/netbox.md)

## When to use

Use for DNS resolution mismatch, unexpected record values, propagation checks, or service discovery questions.

## Required context

- Name being resolved.
- Expected record type.
- Expected environment.
- DNS source of truth.
- Resolver path.

## Authority chain

1. [Internal DNS source of truth](../../references/sysadmin/internal-dns-source-of-truth.md).
2. Authoritative provider records.
3. Cluster-local DNS docs if relevant.
4. Resolver checks as observation.

## Allowed read-only actions

- `dig`
- `nslookup`
- `host`
- read DNS records from approved sources
- read cluster DNS state in read-only mode

## Forbidden actions

- Changing DNS records.
- Restarting DNS services without approval.
- Changing TTLs without approval.

## Workflow

1. Identify expected record and source of truth.
2. Query authoritative source.
3. Query relevant resolvers.
4. Compare answers and TTLs.
5. Check recent changes.
6. Produce diagnosis and safe next action.

## Output format

```markdown
# DNS Debug Report

## Query target

## Expected answer

## Observed answers

## Resolver comparison

## Suspected cause

## Safe next steps

## Approval needed
```
