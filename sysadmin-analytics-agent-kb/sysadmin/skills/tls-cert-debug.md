# Skill: TLS Certificate Debug

## Purpose

Diagnose TLS certificate, chain, hostname, expiration, and routing problems without mutating infrastructure.

## Reference links

Authority references:

- [Internal Certificate Management](../../references/sysadmin/internal-certificate-management.md)
- [Internal DNS Source of Truth](../../references/sysadmin/internal-dns-source-of-truth.md)

## When to use

Use when a client reports certificate errors, TLS handshake failures, expiration warnings, or a wrong certificate is served.

## Required context

- Hostname and port.
- Expected certificate owner and issuer.
- Environment and network path.
- TLS termination point.
- Certificate source of truth.

## Authority chain

1. [Internal certificate management](../../references/sysadmin/internal-certificate-management.md).
2. Certificate manager or cloud provider docs.
3. Ingress, load balancer, or proxy docs.
4. External checks as observation.

## Allowed read-only actions

- inspect presented certificate
- check hostname resolution
- read ingress or load balancer configuration
- read certificate manager status

## Forbidden actions

- Changing certificate configuration without approval.
- Restarting ingress or proxy without approval.
- Changing DNS or TLS termination settings without approval.

## Workflow

1. Resolve hostname and identify target.
2. Inspect presented certificate with SNI.
3. Verify SANs, expiry, issuer, and chain.
4. Compare presented certificate to expected source of truth.
5. Check routing if the wrong certificate is served.
6. Propose safe remediation.

## Output format

```markdown
# TLS Certificate Debug Report

## Host

## Presented certificate

## Expected certificate

## Chain / issuer / SANs

## Expiration

## Routing / SNI findings

## Suspected cause

## Safe next steps

## Approval needed
```
