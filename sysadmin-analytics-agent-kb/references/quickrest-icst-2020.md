---
artifact_type: reference
authority_tier: Tier B
status: useful-after-audit
source_type: peer-reviewed-paper
topics:
  - testing
  - rest-api
  - openapi
  - property-based-testing
  - test-generation
domains:
  - java-qa
owner: IEEE ICST
last_checked: 2026-10-07
source_url: https://doi.org/10.1109/ICST46399.2020.00023
---

# Reference: QuickREST — ICST 2020

## Authority tier

Tier B

## Status

useful-after-audit

## Owner / maintainer

Stefan Karlsson, Adnan Causevic, and Daniel Sundmark; published at IEEE ICST 2020.

## URL

https://doi.org/10.1109/ICST46399.2020.00023

## Last checked

2026-10-07

## Scope

Property-based generation of REST API tests from OpenAPI documents. QuickREST uses the API description to derive automatic property-based tests that explore implementation behavior over many generated inputs.

## Why trusted

Peer-reviewed ICST research paper focused specifically on OpenAPI-described REST APIs and low-effort automated test generation.

## Caveats

OpenAPI-derived properties are strongest for structure, types, status codes, and other interface-level constraints. They do not by themselves establish domain truth such as correct order totals, tax calculation, stock reservation, payment capture, or refund amounts.

## Agent-facing artifacts that may consume this reference

- [Java QA Agent](../java-qa/agent.md)
- [API and Contract Testing](../java-qa/skills/api-and-contract-testing.md)
- [QA Automation Decision Flow](../java-qa/skills/qa-automation-decision-flow.md)
- [Test Suite Architecture](../java-qa/skills/test-suite-architecture.md)

## Extracted rules

- Derive generators from schema constraints instead of relying only on example-based cases.
- Express generic properties that should hold across many generated inputs.
- Treat generated values as exploration of an input space, not as a replacement for explicit domain scenarios.
- Add domain-specific invariants when structural OpenAPI properties are insufficient.

## Do not use this source for

Inferring e-commerce business rules from observed data or proving that schema-conformant values are semantically correct.

## Related references

- [Specification-based generation (EDOC 2018)](./openapi-test-generation-edoc-2018.md)
- [RESTTESTGEN](./resttestgen-icst-2020.md)
- [RESTest](./restest-icsoc-2020.md)
