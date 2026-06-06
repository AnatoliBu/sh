# Skill: TLS Certificate Debug

## Purpose

Diagnose TLS certificate, chain, hostname, expiration, and routing problems without mutating infrastructure.

## When to use

Use when:

- browser/client reports certificate error;
- TLS handshake fails;
- cert is expired or near expiry;
- wrong certificate is served;
- SNI / ingress / load balancer / proxy issue is suspected.

## Required context

- Hostname and port.
- Expected certificate owner/issuer.
- Environment and network path.
- TLS termination point: ingress, load balancer, CDN, reverse proxy, app server.
- Certificate source of truth: cert-manager, ACM, Vault, Cloudflare, manual secret, etc.

## Authority chain

1. Internal certificate ownership/runbook.
2. Certificate manager / cloud provider docs.
3. Ingress/load balancer/proxy official docs.
4. Public certificate transparency / external checks as observation.

## Allowed read-only actions

- `openssl s_client -connect host:443 -servername host`
- `curl -vI https://host`
- `dig` to check target resolution
- read ingress/load balancer configuration
- read Kubernetes Secret metadata only; do not print private key material
- read cert-manager Certificate/CertificateRequest/Order/Challenge resources

## Forbidden actions

- Printing private keys.
- Downloading secrets into chat.
- Replacing certificates.
- Restarting ingress/proxy.
- Changing DNS or TLS termination settings without approval.

## Workflow

1. Resolve hostname and identify target IP/load balancer/CDN.
2. Inspect presented certificate with SNI.
3. Verify SANs match hostname.
4. Verify expiry, issuer, chain completeness.
5. Compare presented certificate to expected source of truth.
6. Check ingress/proxy routing if wrong cert is served.
7. Check cert-manager/cloud certificate status if managed.
8. Propose safe remediation.

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
