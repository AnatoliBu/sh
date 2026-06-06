---
artifact_type: skill
authority_tier: Tier A
status: foundation
domain: sysadmin
owner: Agent KB
last_checked: 2026-06-06
---

# Skill: TLS Certificate Debug

## Purpose

Diagnose TLS certificate, chain, hostname, expiration, and routing problems without mutating infrastructure.

## Reference links

Authority references:

- [Internal Certificate Management](../../references/internal-certificate-management.md)
- [Internal DNS Source of Truth](../../references/internal-dns-source-of-truth.md)

## When to use

Use when a client reports certificate errors, TLS handshake failures, expiration warnings, or a wrong certificate is served.

## Required context

- Hostname and port.
- Expected certificate owner.
- Expected TLS termination point.
- DNS source-of-truth entry.
- Client error text.
- Environment and route.

## Authority chain

1. [Internal Certificate Management](../../references/internal-certificate-management.md).
2. [Internal DNS Source of Truth](../../references/internal-dns-source-of-truth.md).
3. Observed server certificate and chain.
4. Load balancer / ingress / gateway configuration.
5. Client-side observation.

## Workflow

1. Identify expected certificate and termination point.
2. Inspect observed certificate chain.
3. Compare SAN/CN, issuer, validity, and chain.
4. Check DNS target and route.
5. Check whether multiple edges serve different certs.
6. Identify owner and required approval.

## Output format

```markdown
# TLS Certificate Debug Report

## Question

## Expected certificate/source

## Observed certificate

## Difference

## Likely cause

## Recommended next step

## Assumptions
```
