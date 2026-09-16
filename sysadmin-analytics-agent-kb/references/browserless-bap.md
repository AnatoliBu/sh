---
artifact_type: reference
authority_tier: Tier A
status: useful-after-audit
source_type: official-docs
topics:
  - browser-automation
  - browserless
  - cloud-browser
  - typed-api
domains:
  - browser-automation
owner: Browserless
last_checked: 2026-09-16
source_url: https://docs.browserless.io/bap
---

# Reference: Browserless Browser Automation Protocol

## Authority tier

Tier A

## Status

useful-after-audit

## Owner / maintainer

Browserless

## URL

https://docs.browserless.io/bap

## Last checked

2026-09-16

## Scope

Browserless BAP, a typed automation layer above BrowserQL with Playwright/Puppeteer-shaped APIs,
managed browser sessions, proxy/stealth options, CAPTCHA handling and live debugging.

## Why trusted

Official Browserless product documentation.

## Caveats

Authoritative only for Browserless product behavior. Claims around stealth, anti-bot success and
provider quality require target-site evaluation and must not be generalized to the web.

## Extracted rules

- Hide provider-specific session creation and connection details behind a project adapter.
- Evaluate typed BAP against raw Playwright/CDP on the same scenario suite before standardizing.
- Keep success criteria in business state, not in provider-specific response shape.
- Treat provider CAPTCHA and proxy features as optional capabilities with observable fallbacks.

## Do not use this source for

Authorization to automate a site against its rules or guarantees that anti-bot systems will allow a
session.

## Related references

- [Browserless Hybrid Automation](./browserless-hybrid-automation.md)
- [Browserless CAPTCHA Handling](./browserless-captcha-handling.md)
