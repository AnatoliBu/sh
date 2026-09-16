---
artifact_type: reference
authority_tier: Tier A
status: foundation
source_type: payment-standard
topics:
  - browser-automation
  - payments
  - 3ds
  - authentication
domains:
  - browser-automation
owner: EMVCo
last_checked: 2026-09-16
source_url: https://www.emvco.com/whitepapers/emv-3-d-secure-whitepaper/3-d-secure-documentation/3-d-secure-specification/
---

# Reference: EMV 3-D Secure 2.3.1

## Authority tier

Tier A

## Status

foundation

## Owner / maintainer

EMVCo

## URL

https://www.emvco.com/whitepapers/emv-3-d-secure-whitepaper/3-d-secure-documentation/3-d-secure-specification/

## Last checked

2026-09-16

## Scope

Authoritative EMV 3-D Secure 2.3.1 specification family, including Protocol and Core Functions and
SDK specifications.

## Why trusted

EMVCo is the specification owner for EMV 3-D Secure.

## Caveats

3DS behavior exposed in a merchant checkout also depends on acquirer, gateway, issuer, region,
risk decisions and supported protocol versions. A browser automation layer does not control those
actors.

## Extracted rules

- Treat a 3DS challenge as an authentication boundary, not an ordinary DOM step.
- Keep human/cardholder participation available when the issuer requires it.
- After any ambiguous submit/challenge outcome, reconcile transaction state before retrying.
- Do not infer payment success merely from UI navigation.

## Do not use this source for

PCI DSS scope decisions or merchant-specific checkout selectors.

## Related references

- [PCI DSS](./pci-dss.md)
