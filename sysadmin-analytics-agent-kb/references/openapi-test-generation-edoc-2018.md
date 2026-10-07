---
artifact_type: reference
authority_tier: Tier B
status: useful-after-audit
source_type: peer-reviewed-paper
topics:
  - testing
  - rest-api
  - openapi
  - specification-based-testing
  - test-generation
domains:
  - java-qa
owner: IEEE EDOC
last_checked: 2026-10-07
source_url: https://doi.org/10.1109/EDOC.2018.00031
---

# Reference: Automatic Generation of Test Cases for REST APIs — EDOC 2018

## Authority tier

Tier B

## Status

useful-after-audit

## Owner / maintainer

Hamza Ed-douibi, Javier Luis Cánovas Izquierdo, and Jordi Cabot; published at IEEE EDOC 2018.

## URL

https://doi.org/10.1109/EDOC.2018.00031

## Last checked

2026-10-07

## Scope

Specification-based automatic REST API test generation from OpenAPI definitions. The approach extracts an OpenAPI model and generates tests intended to check whether the implementation conforms to the requirements represented by the specification.

The evaluation used 91 OpenAPI definitions. The paper reports average coverage of 76.5% of elements in the definitions and reports failures for 40% of the tested APIs.

## Why trusted

Peer-reviewed IEEE conference paper and an early direct treatment of OpenAPI as an executable model for automatic test generation rather than documentation only.

## Caveats

The study predates current OpenAPI 3.1 tooling. Specification conformance is not equivalent to business correctness: a schema-valid response can still contain a wrong price, tax, discount, inventory decision, or state transition.

## Agent-facing artifacts that may consume this reference

- [Java QA Agent](../java-qa/agent.md)
- [API and Contract Testing](../java-qa/skills/api-and-contract-testing.md)
- [QA Automation Decision Flow](../java-qa/skills/qa-automation-decision-flow.md)
- [Test Suite Architecture](../java-qa/skills/test-suite-architecture.md)

## Extracted rules

- Parse the API specification into a model before generating requests.
- Derive test inputs and expected structural behavior from specification elements rather than hard-coded examples only.
- Track specification-element coverage separately from code coverage.
- Keep business-semantic oracles outside pure OAS conformance checks.

## Do not use this source for

Stateful business-flow inference across multiple services, consumer-driven contracts, or domain-level e-commerce invariants.

## Related references

- [QuickREST](./quickrest-icst-2020.md)
- [RESTTESTGEN](./resttestgen-icst-2020.md)
- [RESTler](./restler-icse-2019.md)
