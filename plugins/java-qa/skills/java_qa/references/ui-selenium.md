---
artifact_type: skill
status: foundation
domain: java-qa
---

# Skill: Selenium UI Automation

## Purpose

Design and review Selenium WebDriver tests for Java projects while keeping browser tests focused, stable, and useful.

## Reference links

Authority references (⚠ карточки вне установленного ядра cards/ помечены — файла нет, см. ../skill.md):

- [Selenium WebDriver Documentation](cards/selenium-webdriver-docs.md)
- [Practical Test Pyramid](cards/practical-test-pyramid.md)
- [JUnit User Guide](cards/junit-user-guide.md)

## Inputs

- User journey or UI behavior under test.
- Browser and driver setup.
- Locator strategy.
- Test data and environment state.
- CI runner details.
- Failure screenshots, logs, or video when available.

## Output

- Scope of the UI test.
- Locator and wait strategy.
- Page object or screen model notes.
- Data setup and cleanup notes.
- Flakiness risks.
- CI execution recommendation.

## Checklist

1. Confirm the behavior needs browser-level confidence.
2. Prefer stable semantic locators.
3. Use explicit waits for observable conditions.
4. Keep one critical user story per high-level UI test when practical.
5. Move pure business logic checks below the UI layer.
6. Capture useful diagnostics on failure.
7. Keep browser, driver, and Selenium versions visible in CI output.

## Review smells

- Fixed sleeps instead of condition-based waits.
- CSS or XPath selectors tied to cosmetic layout details.
- One test verifies too many unrelated behaviors.
- Browser test repeats assertions already covered by lower-level tests.
- Test depends on execution order or leftover state.
