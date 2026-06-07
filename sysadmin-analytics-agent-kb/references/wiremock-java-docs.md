---
artifact_type: reference
authority_tier: Tier A
status: foundation
source_type: official-docs
topics:
  - java
  - testing
  - wiremock
  - api-mocking
  - service-virtualization
domains:
  - java-qa
owner: WireMock Project
last_checked: 2026-06-07
source_url: https://wiremock.org/docs/
---

# Reference: WireMock Java Documentation

## Authority tier

Tier A

## Status

foundation

## Owner / maintainer

WireMock Project

## URL

https://wiremock.org/docs/

## Last checked

2026-06-07

## Scope

HTTP API stubbing, request matching, response templating, verification, record/playback, faults, latency, Java usage, and JUnit integration.

## Why trusted

Official WireMock Java documentation.

## Caveats

Mocks and stubs must represent meaningful API contracts. They can become misleading if they drift away from real provider behavior.

## Agent-facing artifacts that may consume this reference

- [Java QA Agent](../java-qa/agent.md)
- [API and Contract Testing](../java-qa/skills/api-and-contract-testing.md)

## Extracted rules

- Use WireMock to isolate external HTTP dependencies and model expected edge cases.
- Keep mappings versioned and reviewed when they represent provider contracts.

## Do not use this source for

JUnit lifecycle rules or browser automation.

## Related references

- [REST Assured Documentation](./rest-assured-docs.md)
- [Testcontainers for Java Documentation](./testcontainers-java-docs.md)
