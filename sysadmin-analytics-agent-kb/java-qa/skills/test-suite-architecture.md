---
artifact_type: skill
status: foundation
domain: java-qa
---

# Skill: Test Suite Architecture

## Purpose

Design or review a Java test suite so it gives useful confidence with reasonable feedback time and maintenance cost.

## Reference links

Authority references:

- [Practical Test Pyramid](../../references/practical-test-pyramid.md)
- [JUnit User Guide](../../references/junit-user-guide.md)
- [Gradle Java Testing](../../references/gradle-java-testing.md)
- [Testcontainers for Java Documentation](../../references/testcontainers-java-docs.md)
- [Spring Framework Testing Documentation](../../references/spring-framework-testing.md)
- [ISTQB Testing Foundation Materials](../../references/istqb-testing-foundation.md)

## Inputs

- Application type and architecture.
- Current test folders and CI tasks.
- Failure history and flaky tests.
- Product risks and release cadence.
- Dependencies: database, message broker, external APIs, browser, files, time, auth.

## Output

- Proposed test layers.
- What belongs in each layer.
- Execution command or CI task per layer.
- Data and environment strategy.
- Gaps, duplication, and flakiness risks.

## Checklist

1. Map current tests by layer.
2. Find duplicated assertions across layers.
3. Move cheap deterministic checks closer to code.
4. Keep integration tests for real wiring, persistence, serialization, transactions, and configuration.
5. Keep UI tests focused on user-critical flows.
6. Separate smoke, regression, and expensive suites in CI.
7. Document what each suite proves and does not prove.

## Anti-patterns

- Mostly UI tests for logic that can be checked below the browser.
- Integration tests that only repeat unit checks.
- Unit tests that mirror implementation instead of behavior.
- Shared mutable test data across parallel runs.
- No explicit owner for slow or flaky suites.
