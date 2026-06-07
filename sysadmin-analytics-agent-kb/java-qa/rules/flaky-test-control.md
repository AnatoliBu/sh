---
artifact_type: rule
status: foundation
domain: java-qa
---

# Rule: Flaky Test Control

## Purpose

Make flaky Java tests observable, diagnosable, and fixable instead of normalizing unstable CI.

## Reference links

Authority references:

- [Selenium WebDriver Documentation](../../references/selenium-webdriver-docs.md)
- [Gradle Java Testing](../../references/gradle-java-testing.md)
- [Testcontainers for Java Documentation](../../references/testcontainers-java-docs.md)
- [Practical Test Pyramid](../../references/practical-test-pyramid.md)

## Rules

1. Classify the flake before adding retries.
2. Record failure mode, environment, seed, time, browser, driver, and dependency versions where relevant.
3. Replace fixed waits with condition-based waits.
4. Remove shared mutable data from parallel tests.
5. Separate slow environment failures from product failures.
6. Quarantine only with an owner and follow-up date.
7. Prefer deterministic setup and explicit cleanup.

## Common flake sources

- Time and timezone assumptions.
- Random data without seed capture.
- Async behavior with weak waiting strategy.
- Database or message queue state leakage.
- External HTTP dependencies.
- Browser and driver mismatch.
- Order-dependent tests.

## Review questions

- Does the failure reproduce locally or only in CI?
- Is the test verifying stable user-visible behavior?
- Is the environment shared with other tests?
- Is the test too high-level for the assertion it checks?
- Does the failure artifact explain enough to debug the next occurrence?
