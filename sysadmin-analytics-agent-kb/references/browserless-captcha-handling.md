---
artifact_type: reference
authority_tier: Tier A
status: useful-after-audit
source_type: official-docs
topics:
  - browser-automation
  - browserless
  - captcha
  - human-handoff
domains:
  - browser-automation
owner: Browserless
last_checked: 2026-09-16
source_url: https://docs.browserless.io/baas/advanced-configurations/hybrid-automation-configurations
---

# Reference: Browserless CAPTCHA Handling

## Authority tier

Tier A

## Status

useful-after-audit

## Owner / maintainer

Browserless

## URL

https://docs.browserless.io/baas/advanced-configurations/hybrid-automation-configurations

## Last checked

2026-09-16

## Scope

Browserless CAPTCHA detection/solver hooks and the documented hybrid fallback from automated solve
to a one-time live browser URL for human intervention.

## Why trusted

Official Browserless documentation for its own CAPTCHA and LiveURL capabilities.

## Caveats

Solver support and success rates vary by challenge, site and protection configuration. Use only in
authorized workflows. This reference is a capability description, not an anti-bot evasion recipe.

## Extracted rules

- Model CAPTCHA as a typed workflow state: detected -> supported solve -> human handoff -> stop.
- Preserve the same browser session when handing a challenge to a human.
- Never loop solver retries without a hard attempt/time/cost budget.
- Log challenge class and outcome without capturing secrets entered during human control.
- If a site's policy or protection clearly rejects the automation, stop rather than escalating an
  evasion arms race.

## Do not use this source for

Fingerprint spoofing instructions or bypassing access controls without authorization.

## Related references

- [Browserless Hybrid Automation](./browserless-hybrid-automation.md)
- [Browserless BAP](./browserless-bap.md)
