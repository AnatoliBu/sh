---
artifact_type: reference
authority_tier: Tier A
status: foundation
source_type: official-docs
topics:
  - java
  - testing
  - selenium
  - webdriver
  - ui-automation
domains:
  - java-qa
owner: Selenium Project
last_checked: 2026-06-07
source_url: https://www.selenium.dev/documentation/webdriver/
---

# Reference: Selenium WebDriver Documentation

## Authority tier

Tier A

## Status

foundation

## Owner / maintainer

Selenium Project

## URL

https://www.selenium.dev/documentation/webdriver/

## Last checked

2026-06-07

## Scope

Official WebDriver behavior, browser automation APIs, waits, locators, actions, browser support, Grid, and Selenium testing practices.

## Why trusted

Official Selenium documentation.

## Caveats

Browser and driver behavior can differ by browser version, driver version, Grid setup, and CI environment.

## Agent-facing artifacts that may consume this reference

- [Java QA Agent](../java-qa/agent.md)
- [Selenium UI Automation](../java-qa/skills/ui-automation-selenium.md)
- [Flaky Test Control](../java-qa/rules/flaky-test-control.md)

## Extracted rules

- Prefer explicit waits and stable locators over sleeps and brittle selectors.
- Treat UI tests as higher-cost tests that need strict scope and isolation.

## Do not use this source for

JUnit lifecycle behavior or API contract testing.

## Related references

- [Practical Test Pyramid](./practical-test-pyramid.md)
