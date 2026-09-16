---
artifact_type: reference
authority_tier: Tier A
status: useful-after-audit
source_type: standard-draft
topics:
  - browser-automation
  - webdriver
  - bidi
  - browser-protocol
domains:
  - browser-automation
owner: W3C Browser Testing and Tools Working Group
last_checked: 2026-09-16
source_url: https://www.w3.org/TR/webdriver-bidi/
---

# Reference: WebDriver BiDi

## Authority tier

Tier A

## Status

useful-after-audit

## Owner / maintainer

W3C Browser Testing and Tools Working Group

## URL

https://www.w3.org/TR/webdriver-bidi/

## Last checked

2026-09-16

## Scope

The bidirectional WebDriver protocol for remotely controlling user agents and receiving browser
events.

## Why trusted

Primary W3C specification maintained by the Browser Testing and Tools Working Group.

## Caveats

As of 2026-08-25 this is a W3C Working Draft, not a Recommendation. Implementations can lead or lag
the draft and interoperability must be tested against target browsers.

## Extracted rules

- Prefer standardized browser protocol capabilities when they satisfy the workflow rather than
  depending on Chromium-only behavior unnecessarily.
- Treat protocol support as a capability matrix, not a boolean.
- Record browser/version/protocol features in reproducibility metadata.

## Do not use this source for

Assuming every draft command is uniformly implemented by every browser.

## Related references

- [Playwright Documentation](./playwright-docs.md)
