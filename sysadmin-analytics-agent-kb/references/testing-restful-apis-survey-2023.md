---
artifact_type: reference
authority_tier: Tier B
status: useful-after-audit
source_type: peer-reviewed-survey
topics:
  - testing
  - rest-api
  - openapi
  - test-generation
  - fuzzing
domains:
  - java-qa
owner: ACM Transactions on Software Engineering and Methodology
last_checked: 2026-10-07
source_url: https://doi.org/10.1145/3617175
---

# Reference: Testing RESTful APIs: A Survey

## Authority tier

Tier B

## Status

useful-after-audit

## Owner / maintainer

Amid Golmohammadi, Man Zhang, and Andrea Arcuri; published in ACM Transactions on Software Engineering and Methodology.

## URL

https://doi.org/10.1145/3617175

## Last checked

2026-10-07

## Scope

Comprehensive survey of research on automated REST API testing. The paper analyzes 92 scientific articles and organizes the field around test generation, fuzzing, search-based techniques, black-box and white-box methods, and open research challenges.

## Why trusted

Peer-reviewed ACM TOSEM survey with an explicit literature-search and study-selection process. It is useful as the top-level map for finding primary research rather than relying on vendor taxonomies.

## Caveats

This is secondary evidence. Use the primary papers below when implementing a concrete generator, oracle, dependency model, or search strategy.

## Agent-facing artifacts that may consume this reference

- [Java QA Agent](../java-qa/agent.md)
- [API and Contract Testing](../java-qa/skills/api-and-contract-testing.md)
- [QA Automation Decision Flow](../java-qa/skills/qa-automation-decision-flow.md)
- [Test Suite Architecture](../java-qa/skills/test-suite-architecture.md)

## Extracted rules

- Treat REST API test generation as a family of techniques rather than a single method.
- Separate input generation, sequence/state exploration, dependency modeling, and test-oracle construction.
- Use the survey to identify primary work; use primary papers to justify specific implementation decisions.

## Do not use this source for

Normative OpenAPI semantics, product-specific business correctness, or claims that one tool is universally best.

## Related references

- [Specification-based generation (EDOC 2018)](./openapi-test-generation-edoc-2018.md)
- [QuickREST](./quickrest-icst-2020.md)
- [RESTTESTGEN](./resttestgen-icst-2020.md)
- [RESTler](./restler-icse-2019.md)
- [RESTest](./restest-icsoc-2020.md)
- [EvoMaster](./evomaster-tosem-2019.md)
