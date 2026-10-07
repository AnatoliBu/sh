---
artifact_type: reference
authority_tier: Tier B
status: useful-after-audit
source_type: peer-reviewed-paper
topics:
  - testing
  - rest-api
  - openapi
  - stateful-testing
  - fuzzing
  - sequence-generation
domains:
  - java-qa
owner: IEEE ICSE / Microsoft Research
last_checked: 2026-10-07
source_url: https://doi.org/10.1109/ICSE.2019.00083
---

# Reference: RESTler — Stateful REST API Fuzzing, ICSE 2019

## Authority tier

Tier B

## Status

useful-after-audit

## Owner / maintainer

Vaggelis Atlidakis, Patrice Godefroid, and Marina Polishchuk; published at ICSE 2019. RESTler was developed at Microsoft Research.

## URL

https://doi.org/10.1109/ICSE.2019.00083

Project:

https://github.com/microsoft/restler-fuzzer

## Last checked

2026-10-07

## Scope

Stateful automatic REST API test generation from an OpenAPI/Swagger specification. RESTler infers producer-consumer dependencies between request types and uses values produced by earlier responses as inputs to later requests, enabling exploration of deeper service states through generated request sequences.

## Why trusted

Peer-reviewed ICSE paper from Microsoft Research with an open-source implementation and subsequent peer-reviewed work on security properties, differential regression testing, and data fuzzing.

## Caveats

Dependency inference is evidence-driven and can miss relationships that are not represented clearly in the specification. Authentication, prerequisite data, hidden business constraints, asynchronous workflows, and cross-service side effects can require extra configuration or external evidence.

## Agent-facing artifacts that may consume this reference

- [Java QA Agent](../java-qa/agent.md)
- [API and Contract Testing](../java-qa/skills/api-and-contract-testing.md)
- [QA Automation Decision Flow](../java-qa/skills/qa-automation-decision-flow.md)
- [Test Suite Architecture](../java-qa/skills/test-suite-architecture.md)

## Extracted rules

- Model API testing as sequence generation when operations depend on resources produced by previous operations.
- Infer producer-consumer relations before exploring request sequences.
- Reuse dynamically observed response values as later request inputs.
- Distinguish breadth and depth of state-space exploration.
- Do not interpret absence of an inferred dependency as proof that no dependency exists.

## Do not use this source for

Proving business-flow completeness from OpenAPI alone or deriving domain invariants such as refund <= captured amount.

## Related references

- [RESTTESTGEN](./resttestgen-icst-2020.md)
- [RESTest](./restest-icsoc-2020.md)
- [EvoMaster](./evomaster-tosem-2019.md)
