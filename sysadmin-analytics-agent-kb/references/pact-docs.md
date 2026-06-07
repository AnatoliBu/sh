---
artifact_type: reference
authority_tier: Tier A
status: foundation
source_type: official-docs
topics:
  - testing
  - contract-testing
  - pact
  - microservices
domains:
  - java-qa
owner: Pact Foundation
last_checked: 2026-06-07
source_url: https://docs.pact.io/
---

# Reference: Pact Documentation

## Authority tier

Tier A

## Status

foundation

## Owner / maintainer

Pact Foundation

## URL

https://docs.pact.io/

## Last checked

2026-06-07

## Scope

Consumer-driven contract testing concepts, consumer/provider terminology, Pact workflow, Pact Broker concepts, and contract test strategy.

## Why trusted

Official Pact documentation.

## Caveats

Contract testing complements integration and end-to-end tests. It does not prove all provider behavior or all client behavior.

## Agent-facing artifacts that may consume this reference

- [Java QA Agent](../java-qa/agent.md)
- [API and Contract Testing](../java-qa/skills/api-and-contract-testing.md)
- [Test Suite Architecture](../java-qa/skills/test-suite-architecture.md)

## Extracted rules

- Use consumer-driven contracts when integration behavior between services must be protected without deploying the whole system.
- Treat contracts as executable examples of used behavior, not as a full API schema.

## Do not use this source for

REST Assured syntax or Selenium browser automation.

## Related references

- [REST Assured Documentation](./rest-assured-docs.md)
- [WireMock Java Documentation](./wiremock-java-docs.md)
