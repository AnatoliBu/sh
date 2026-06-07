---
artifact_type: reference
authority_tier: Tier A
status: foundation
source_type: official-docs
topics:
  - java
  - testing
  - gradle
  - build-tool
domains:
  - java-qa
owner: Gradle Project
last_checked: 2026-06-07
source_url: https://docs.gradle.org/current/userguide/java_testing.html
---

# Reference: Gradle Java Testing

## Authority tier

Tier A

## Status

foundation

## Owner / maintainer

Gradle Project

## URL

https://docs.gradle.org/current/userguide/java_testing.html

## Last checked

2026-06-07

## Scope

Gradle test task behavior, JVM test suites, test filtering, reporting, parallelism, logging, and test framework integration for Java and JVM projects.

## Why trusted

Official Gradle User Manual.

## Caveats

Build behavior depends on Gradle version, plugins, test task configuration, and CI runner resources.

## Agent-facing artifacts that may consume this reference

- [Java QA Agent](../java-qa/agent.md)
- [Test Suite Architecture](../java-qa/skills/test-suite-architecture.md)
- [Automation Review Workflow](../java-qa/workflows/automation-review.md)

## Extracted rules

- Inspect the actual build configuration before recommending test execution commands.
- Separate unit, integration, contract, and UI test tasks when feedback speed or stability requires it.

## Do not use this source for

JUnit API semantics or Selenium locator strategy.

## Related references

- [JUnit User Guide](./junit-user-guide.md)
