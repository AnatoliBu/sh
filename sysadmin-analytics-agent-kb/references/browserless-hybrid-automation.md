---
artifact_type: reference
authority_tier: Tier A
status: foundation
source_type: official-docs
topics:
  - browser-automation
  - browserless
  - human-handoff
  - captcha
domains:
  - browser-automation
owner: Browserless
last_checked: 2026-09-16
source_url: https://docs.browserless.io/baas/monitor-sessions/hybrid-automation
---

# Reference: Browserless Hybrid Automation

## Authority tier

Tier A

## Status

foundation

## Owner / maintainer

Browserless

## URL

https://docs.browserless.io/baas/monitor-sessions/hybrid-automation

## Last checked

2026-09-16

## Scope

Remote Chromium, Playwright/Puppeteer over CDP, secure LiveURL handoff, CAPTCHA detection and
solver integration, multi-stage human/automation workflows, and session debugging.

## Why trusted

Official Browserless documentation.

## Caveats

Automated CAPTCHA handling is a provider capability, not permission to defeat a site's access
controls. Use it only in workflows the operator and site permit; otherwise hand control to the
authorized user or stop.

## Extracted rules

- A hybrid workflow can pause automation, issue a short-lived interactive URL, wait for the human,
  and then resume in the same session.
- Do not place the Browserless API token in a user-facing LiveURL.
- Build CAPTCHA as a branch in the workflow: detect, use permitted provider handling if
  appropriate, then fall back to human takeover or stop.
- Session timeout is a hard lifecycle constraint; a viewer URL does not extend the browser session.

## Do not use this source for

Credential-storage design or payment-card compliance.

## Related references

- [Playwright Documentation](./playwright-docs.md)
- [OWASP Session Management Cheat Sheet](./owasp-session-management.md)
