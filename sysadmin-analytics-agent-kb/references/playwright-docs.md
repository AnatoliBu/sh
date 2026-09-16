---
artifact_type: reference
authority_tier: Tier A
status: foundation
source_type: official-docs
topics:
  - browser-automation
  - playwright
  - locators
  - authentication
domains:
  - browser-automation
owner: Microsoft Playwright
last_checked: 2026-09-16
source_url: https://playwright.dev/docs/intro
---

# Reference: Playwright Documentation

## Authority tier

Tier A

## Status

foundation

## Owner / maintainer

Microsoft Playwright

## URL

https://playwright.dev/docs/intro

## Last checked

2026-09-16

## Scope

Deterministic browser automation, browser contexts, locator strategy, auto-waiting, authentication
state, downloads, tracing, and Chromium/Firefox/WebKit control.

## Why trusted

Official documentation for Playwright.

## Caveats

A workflow that is stable under a test account can still fail under different locale, account
state, feature flags, anti-abuse controls, or third-party payment UI.

## Extracted rules

- Prefer role/label/text/test-id locators and Playwright auto-waiting over sleeps and brittle CSS.
- Model authentication state explicitly; persisted storage state is a credential and must be
  protected like one.
- Assert a post-condition after every state-changing step instead of assuming a click succeeded.
- Keep deterministic steps deterministic; add an LLM only where the DOM or task is genuinely open
  ended.

## Do not use this source for

Provider-specific cloud-browser behavior, CAPTCHA policy, or payment-card compliance.

## Related references

- [OWASP Session Management Cheat Sheet](./owasp-session-management.md)
- [PCI DSS](./pci-dss.md)
