---
artifact_type: reference
authority_tier: Tier B
status: useful-after-audit
source_type: peer-reviewed-paper
topics:
  - testing
  - rest-api
  - openapi
  - constraint-based-testing
  - test-generation
domains:
  - java-qa
owner: ICSOC / Springer
last_checked: 2026-10-07
source_url: https://doi.org/10.1007/978-3-030-65310-1_33
---

# Reference: RESTest — Black-Box Constraint-Based Testing of RESTful Web APIs

## Authority tier

Tier B

## Status

useful-after-audit

## Owner / maintainer

Alberto Martin-Lopez, Sergio Segura, and Antonio Ruiz-Cortés; published at ICSOC 2020.

## URL

https://doi.org/10.1007/978-3-030-65310-1_33

Project:

https://github.com/isa-group/RESTest

## Last checked

2026-10-07

## Scope

Constraint-based automatic generation of black-box REST API tests derived from API specifications. RESTest focuses on inter-parameter dependencies that plain API schemas often cannot express and uses constraint solving to generate valid combinations more efficiently.

The paper reports evaluation on six commercial APIs, with up to 99% more valid test cases than random techniques, 60% on average, and failures that random generation did not expose.

## Why trusted

Peer-reviewed ICSOC research backed by an open-source implementation and explicit empirical evaluation.

## Caveats

The approach requires dependencies to be represented in a machine-readable form beyond ordinary OpenAPI where the base specification cannot express them. Constraint satisfaction improves input validity but still does not provide a complete business oracle.

## Agent-facing artifacts that may consume this reference

- [Java QA Agent](../java-qa/agent.md)
- [API and Contract Testing](../java-qa/skills/api-and-contract-testing.md)
- [QA Automation Decision Flow](../java-qa/skills/qa-automation-decision-flow.md)
- [Test Suite Architecture](../java-qa/skills/test-suite-architecture.md)

## Extracted rules

- Identify inter-parameter constraints explicitly instead of assuming independent parameter generation.
- Prefer solver-backed generation when valid inputs require relationships such as conditional presence, mutual exclusion, or dependent ranges.
- Treat extensions to OAS as a way to make hidden input constraints executable.
- Separate input-validity generation from business-result verification.

## Do not use this source for

Inferring unrecorded business dependencies automatically or validating downstream order/payment/inventory semantics.

## Related references

- [QuickREST](./quickrest-icst-2020.md)
- [RESTTESTGEN](./resttestgen-icst-2020.md)
- [RESTler](./restler-icse-2019.md)
