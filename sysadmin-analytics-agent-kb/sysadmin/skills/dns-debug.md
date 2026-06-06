# Skill: DNS Debug

## Purpose

Diagnose DNS resolution issues safely and systematically.

## When to use

Use when:

- service name does not resolve;
- wrong IP is returned;
- DNS propagation is suspected;
- internal/external DNS differs;
- TLS/cert issue may be caused by DNS misrouting;
- Kubernetes Service discovery behaves unexpectedly.

## Required context

- Domain or service name.
- Expected record type: A, AAAA, CNAME, MX, TXT, SRV, NS, SOA.
- Expected environment: internal, public, staging, prod.
- Source of truth for DNS: Terraform, Route53/Cloudflare, NetBox/IPAM, Kubernetes, etc.
- Resolver path: local resolver, corporate DNS, cluster DNS, public resolver.

## Authority chain

1. Internal DNS/IaC source of truth.
2. Authoritative DNS provider records.
3. Kubernetes DNS docs if cluster-local.
4. Public resolver checks only as observation.

## Allowed read-only actions

- `dig`
- `nslookup`
- `host`
- `resolvectl query`
- read Terraform DNS records
- read cloud DNS zone records
- read Kubernetes Service/EndpointSlice/CoreDNS config in read-only mode

## Forbidden actions

- Modifying DNS records.
- Flushing caches on production nodes without approval.
- Restarting CoreDNS without approval.
- Changing TTLs without approval.

## Workflow

1. Identify expected record and authoritative source.
2. Query authoritative nameserver directly.
3. Query internal resolver.
4. Query public resolver if relevant.
5. Compare answers, TTLs, and CNAME chains.
6. Check recent DNS/IaC changes.
7. For Kubernetes: check Service, Endpoints/EndpointSlices, namespace, CoreDNS health.
8. Produce diagnosis and next safe action.

## Output format

```markdown
# DNS Debug Report

## Query target

## Expected answer

## Observed answers

## Resolver comparison

## TTL / propagation notes

## Suspected cause

## Safe next steps

## Approval needed
```
