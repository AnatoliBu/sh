---
artifact_type: reference
authority_tier: Tier B
status: useful-after-audit
source_type: peer-reviewed-paper
topics:
  - testing
  - rest-api
  - search-based-testing
  - evolutionary-testing
  - test-generation
domains:
  - java-qa
owner: ACM Transactions on Software Engineering and Methodology
last_checked: 2026-10-07
source_url: https://doi.org/10.1145/3293455
---

# Reference: RESTful API Automated Test Case Generation with EvoMaster

## Authority tier

Tier B

## Status

useful-after-audit

## Owner / maintainer

Andrea Arcuri; published in ACM Transactions on Software Engineering and Methodology in 2019.

## URL

https://doi.org/10.1145/3293455

Project:

https://github.com/WebFuzzing/EvoMaster

## Last checked

2026-10-07

## Scope

Fully automated search-based generation of system-level REST API tests using evolutionary algorithms. EvoMaster's research line treats REST tests as sequences of HTTP requests/responses and optimizes generated tests using objectives such as coverage and fault finding.

Current EvoMaster REST tooling consumes OpenAPI/Swagger schemas to identify endpoints and request structure, but the 2019 paper's central contribution is white-box evolutionary search rather than specification-only black-box generation.

## Why trusted

Peer-reviewed ACM TOSEM article with a mature open-source research tool and a long follow-up publication record.

## Caveats

Do not group EvoMaster with pure OpenAPI-derived black-box methods. White-box mode assumes code/instrumentation access and uses implementation feedback unavailable to external consumers. Black-box use has weaker guidance.

## Agent-facing artifacts that may consume this reference

- [Java QA Agent](../java-qa/agent.md)
- [API and Contract Testing](../java-qa/skills/api-and-contract-testing.md)
- [QA Automation Decision Flow](../java-qa/skills/qa-automation-decision-flow.md)
- [Test Suite Architecture](../java-qa/skills/test-suite-architecture.md)

## Extracted rules

- Search-based generation is useful when the sequence/input space is too large for naive enumeration.
- Optimize generated tests against explicit objectives rather than random exploration alone.
- Keep the API schema as structural guidance while distinguishing schema evidence from code-derived feedback.
- Compare black-box and white-box modes explicitly when evaluating cost and effectiveness.

## Do not use this source for

Claims that OpenAPI alone is sufficient for evolutionary search quality or for product-level business oracles.

## Related references

- [RESTler](./restler-icse-2019.md)
- [Testing RESTful APIs: A Survey](./testing-restful-apis-survey-2023.md)
