---
artifact_type: workflow
status: foundation
domain: java-qa
---

# Workflow: Automation Review

## Purpose

Review a Java QA automation change before it becomes part of the long-term regression suite.

## Reference links

Authority references:

- [JUnit User Guide](../../references/junit-user-guide.md)
- [Gradle Java Testing](../../references/gradle-java-testing.md)
- [Practical Test Pyramid](../../references/practical-test-pyramid.md)
- [Selenium WebDriver Documentation](../../references/selenium-webdriver-docs.md)
- [REST Assured Documentation](../../references/rest-assured-docs.md)

## Input package

- Test diff or proposed test design.
- Product behavior source.
- Existing related tests.
- CI task where the test will run.
- Known flaky history.

## Review steps

1. Identify the protected behavior.
2. Identify the selected test layer.
3. Check whether a lower-cost layer can provide the same confidence.
4. Check data setup and cleanup.
5. Check assertion strength and failure diagnostics.
6. Check dependency and environment assumptions.
7. Estimate CI runtime and stability impact.
8. Record whether the test belongs in smoke, PR, nightly, or release suite.

## Output

```markdown
# Automation Review

## Behavior protected

## Current layer

## Suggested layer

## Assertion quality

## Test data and environment

## Flakiness risks

## CI placement

## Required changes
```

## Approval criteria

- The test has a clear behavior source.
- The selected layer is justified.
- The failure message should be useful.
- The setup is deterministic enough for CI.
- The test does not duplicate another test without reason.
