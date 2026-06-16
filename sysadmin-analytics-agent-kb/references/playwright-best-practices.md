---
artifact_type: reference
authority_tier: Tier A
status: foundation
source_type: official-docs
topics:
  - testing
  - ui-automation
  - isolation
  - locators
  - test-design
  - best-practices
domains:
  - java-qa
owner: Microsoft Playwright Project
last_checked: 2026-06-16
source_url: https://playwright.dev/docs/best-practices
---

# Reference: Playwright Best Practices

## Authority tier

Tier A

## Status

foundation

## Owner / maintainer

Microsoft Playwright Project

## URL

https://playwright.dev/docs/best-practices

## Last checked

2026-06-16

## Scope

Official Playwright guidance on resilient automated tests, test philosophy, user-visible behavior, test isolation, locators, assertions, and CI-oriented diagnostics.

Even when the target project uses Java/Selenium/API testing rather than Playwright, this source is useful for general automation design principles.

## Why trusted

Official documentation from the Playwright project.

## Caveats

Use this source for automation design principles and Playwright-specific behavior only. Do not use it as authority for Selenium, JUnit, REST Assured, Pact, WireMock, Testcontainers, or internal Java test-platform behavior.

## Agent-facing artifacts that may consume this reference

- [Java QA Agent](../java-qa/agent.md)
- [QA Automation Decision Flow](../java-qa/skills/qa-automation-decision-flow.md)
- [Automation Decision Quality Gates](../java-qa/rules/automation-decision-quality-gates.md)

## Extracted rules

- Prefer testing behavior visible to the user or API consumer over implementation details.
- Keep tests isolated so they can run independently and fail independently.
- Accept small local duplication when it keeps a test clearer and easier to maintain.
- Prefer stable, intention-revealing selectors and assertions over brittle implementation coupling.
- Capture useful CI diagnostics for failures instead of relying on local reproduction only.

## Do not use this source for

- Selenium WebDriver API behavior.
- Java/JUnit lifecycle details.
- API contract rules.
- Internal product behavior.

## Related references

- [Selenium WebDriver Documentation](./selenium-webdriver-docs.md)
- [Practical Test Pyramid](./practical-test-pyramid.md)
- [JUnit User Guide](./junit-user-guide.md)
