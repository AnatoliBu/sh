---
artifact_type: reference
authority_tier: Tier B
status: useful-after-audit
source_type: peer-reviewed-paper
topics:
  - testing
  - rest-api
  - openapi
  - black-box-testing
  - test-generation
  - test-oracles
domains:
  - java-qa
owner: IEEE ICST
last_checked: 2026-10-07
source_url: https://doi.org/10.1109/ICST46399.2020.00024
---

# Reference: RESTTESTGEN — ICST 2020

## Authority tier

Tier B

## Status

useful-after-audit

## Owner / maintainer

Emanuele Viglianisi, Michael Dallago, and Mariano Ceccato; published at IEEE ICST 2020. The approach was later expanded in Software Testing, Verification and Reliability.

## URL

https://doi.org/10.1109/ICST46399.2020.00024

Expanded journal version:

https://doi.org/10.1002/stvr.1808

## Last checked

2026-10-07

## Scope

Automated black-box test generation from Swagger/OpenAPI interface definitions. RESTTESTGEN generates input values and requests for API operations with two explicit goals: nominal execution scenarios and error scenarios. The approach includes automated test oracles.

The ICST evaluation reports fault finding on 87 real-world REST APIs; the expanded journal evaluation covers more than 100 real-world APIs.

## Why trusted

Peer-reviewed ICST paper, distinguished-paper award at ICST 2020, followed by an expanded peer-reviewed journal publication.

## Caveats

The generated checks mainly establish interface robustness and conformance. They do not infer product-specific business expectations automatically.

## Agent-facing artifacts that may consume this reference

- [Java QA Agent](../java-qa/agent.md)
- [API and Contract Testing](../java-qa/skills/api-and-contract-testing.md)
- [QA Automation Decision Flow](../java-qa/skills/qa-automation-decision-flow.md)
- [Test Suite Architecture](../java-qa/skills/test-suite-architecture.md)

## Extracted rules

- Generate nominal and error scenarios separately.
- Include explicit mutation/input-generation operators instead of treating invalid data as ad hoc examples.
- Keep automated oracles as first-class components of the framework.
- For microservices, black-box generation can be useful when source-level analysis across distributed components is unavailable or too expensive.

## Do not use this source for

Claiming that OpenAPI alone can validate price, tax, promotion, payment, inventory, or fulfillment semantics.

## Related references

- [QuickREST](./quickrest-icst-2020.md)
- [RESTest](./restest-icsoc-2020.md)
- [RESTler](./restler-icse-2019.md)
