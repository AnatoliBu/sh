---
artifact_type: reference
authority_tier: Tier B
status: useful-after-audit
source_type: professional-article
topics:
  - testing
  - test-strategy
  - test-pyramid
  - automation
domains:
  - java-qa
owner: Martin Fowler site / Ham Vocke
last_checked: 2026-06-07
source_url: https://martinfowler.com/articles/practical-test-pyramid.html
---

# Reference: Practical Test Pyramid

## Authority tier

Tier B

## Status

useful-after-audit

## Owner / maintainer

Martin Fowler site / Ham Vocke

## URL

https://martinfowler.com/articles/practical-test-pyramid.html

## Last checked

2026-06-07

## Scope

Test portfolio strategy across unit, integration, contract, UI, end-to-end, acceptance, and exploratory testing.

## Why trusted

Widely cited professional article on test automation strategy.

## Caveats

Use as strategy guidance. Adapt it to product risk, architecture, delivery process, and team skills.

## Agent-facing artifacts that may consume this reference

- [Java QA Agent](../java-qa/agent.md)
- [Test Suite Architecture](../java-qa/skills/test-suite-architecture.md)
- [Selenium UI Automation](../java-qa/skills/ui-automation-selenium.md)

## Extracted rules

- Prefer fast focused tests near the code where practical.
- Keep high-level browser and end-to-end tests smaller and more selective.
- Avoid repeating the same assertion at every test layer.

## Do not use this source for

Exact framework APIs or project-specific CI commands.

## Related references

- [JUnit User Guide](./junit-user-guide.md)
- [Selenium WebDriver Documentation](./selenium-webdriver-docs.md)
- [Pact Documentation](./pact-docs.md)
