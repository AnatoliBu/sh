---
artifact_type: reference
authority_tier: Tier A
status: foundation
source_type: official-docs
topics:
  - java
  - testing
  - testcontainers
  - integration-testing
domains:
  - java-qa
owner: Testcontainers Project
last_checked: 2026-06-07
source_url: https://java.testcontainers.org/
---

# Reference: Testcontainers for Java Documentation

## Authority tier

Tier A

## Status

foundation

## Owner / maintainer

Testcontainers Project

## URL

https://java.testcontainers.org/

## Last checked

2026-06-07

## Scope

Java integration testing with disposable containers, modules, Docker requirements, lifecycle, networking, and framework integrations.

## Why trusted

Official Testcontainers for Java documentation.

## Caveats

Requires a working container runtime. CI behavior depends on runner permissions, Docker availability, and image pull access.

## Agent-facing artifacts that may consume this reference

- [Java QA Agent](../java-qa/agent.md)
- [Test Suite Architecture](../java-qa/skills/test-suite-architecture.md)
- [API and Contract Testing](../java-qa/skills/api-and-contract-testing.md)

## Extracted rules

- Use containerized dependencies when in-memory fakes hide important integration behavior.
- Keep integration tests isolated and reproducible.

## Do not use this source for

Unit test lifecycle or Selenium browser automation.

## Related references

- [JUnit User Guide](./junit-user-guide.md)
- [WireMock Java Documentation](./wiremock-java-docs.md)
