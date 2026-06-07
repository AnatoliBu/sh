---
artifact_type: reference
authority_tier: Tier A
status: foundation
source_type: official-docs
topics:
  - java
  - testing
  - spring
  - spring-test
domains:
  - java-qa
owner: Spring Team
last_checked: 2026-06-07
source_url: https://docs.spring.io/spring-framework/reference/testing.html
---

# Reference: Spring Framework Testing Documentation

## Authority tier

Tier A

## Status

foundation

## Owner / maintainer

Spring Team

## URL

https://docs.spring.io/spring-framework/reference/testing.html

## Last checked

2026-06-07

## Scope

Spring test support, application context testing, web testing support, transaction handling, annotations, and integration with JUnit.

## Why trusted

Official Spring Framework reference documentation.

## Caveats

Spring Boot adds its own test slices and auto-configuration. Check Spring Boot documentation when the project uses Boot-specific testing support.

## Agent-facing artifacts that may consume this reference

- [Java QA Agent](../java-qa/agent.md)
- [Test Suite Architecture](../java-qa/skills/test-suite-architecture.md)
- [API and Contract Testing](../java-qa/skills/api-and-contract-testing.md)

## Extracted rules

- Choose the smallest Spring test scope that gives the needed confidence.
- Avoid full application context tests when a smaller slice or unit test is enough.

## Do not use this source for

General Selenium or contract testing concepts.

## Related references

- [JUnit User Guide](./junit-user-guide.md)
- [Testcontainers for Java Documentation](./testcontainers-java-docs.md)
