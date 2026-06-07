---
artifact_type: reference
authority_tier: Tier A
status: foundation
source_type: official-docs
topics:
  - java
  - testing
  - assertions
  - assertj
domains:
  - java-qa
owner: AssertJ Project
last_checked: 2026-06-07
source_url: https://assertj.github.io/doc/
---

# Reference: AssertJ Documentation

## Authority tier

Tier A

## Status

foundation

## Owner / maintainer

AssertJ Project

## URL

https://assertj.github.io/doc/

## Last checked

2026-06-07

## Scope

Fluent assertions for Java and JVM tests, supported types, exception assertions, extraction, filtering, soft assertions, and Javadoc examples.

## Why trusted

Official AssertJ documentation.

## Caveats

Assertion style should improve failure diagnostics and readability; it should not hide unclear test intent.

## Agent-facing artifacts that may consume this reference

- [Java QA Agent](../java-qa/agent.md)
- [JUnit Java Test Design](../java-qa/skills/junit-java-test-design.md)
- [Test Code Quality](../java-qa/rules/test-code-quality.md)

## Extracted rules

- Prefer assertions with useful failure messages and precise expected values.
- Use extraction and filtering only when they make the test clearer.

## Do not use this source for

Mocking behavior or test execution lifecycle.

## Related references

- [JUnit User Guide](./junit-user-guide.md)
- [Mockito Documentation](./mockito-docs.md)
