---
artifact_type: reference
authority_tier: Tier B
status: useful-after-audit
source_type: open-source-agent-skill-catalog
topics:
  - qa
  - test-automation
  - agent-skills
  - skill-taxonomy
  - ai-assisted-qa
domains:
  - java-qa
owner: petrkindlmann / qa-skills
last_checked: 2026-06-16
source_url: https://github.com/petrkindlmann/qa-skills
---

# Reference: QA Skills Agent Catalog

## Authority tier

Tier B

## Status

useful-after-audit

## Owner / maintainer

petrkindlmann / qa-skills

## URL

https://github.com/petrkindlmann/qa-skills

## Last checked

2026-06-16

## Scope

Reusable taxonomy and packaging ideas for QA and test-automation skills consumed by AI coding agents.

Use this source for:

- naming and grouping QA skills;
- deciding which QA concerns deserve separate skills;
- examples of agent-facing activation surfaces;
- separating lightweight skill instructions from heavier references.

## Why trusted

The repository is a public, structured catalog of QA and test-automation skills for AI agent runtimes. It explicitly covers strategy, risk-based testing, API testing, contract testing, service virtualization, test reliability, AI QA review, release readiness, and test-suite curation.

It is useful as a pattern source because it treats QA capabilities as reusable agent skills instead of one giant prompt.

## Caveats

This is not an authority for Java framework behavior, product correctness, API contracts, or internal test-platform architecture.

Many skills are oriented toward web/UI automation and modern frontend stacks. Adapt the taxonomy to Java, OpenAPI, JUnit, REST Assured, Pact, WireMock, Testcontainers, Gatling, CLI, and MCP before using it in this repository.

## Agent-facing artifacts that may consume this reference

- [Java QA Agent](../java-qa/agent.md)
- [QA Automation Decision Flow](../java-qa/skills/qa-automation-decision-flow.md)
- [Agentic QA Tooling Design](../java-qa/skills/agentic-qa-tooling-design.md)
- [QA Automation Architecture Decision Workflow](../java-qa/workflows/qa-automation-architecture-decision.md)

## Extracted rules

- Model QA agent behavior as small, composable skills instead of one monolithic QA prompt.
- Keep skill files lean and route heavy evidence to references.
- Include both strategy skills and execution skills: test strategy, risk-based testing, API testing, contract testing, service virtualization, test reliability, release readiness, and test-suite curation.
- Treat AI-generated tests as proposals that still need source-of-truth behavior, oracle quality, maintainability, and CI stability review.

## Do not use this source for

- Exact Java APIs.
- Claims about Selenium, JUnit, REST Assured, Pact, WireMock, or Testcontainers behavior.
- Internal LP product behavior.
- Deciding that a UI/E2E-heavy structure is automatically right for Java API automation.

## Related references

- [Practical Test Pyramid](./practical-test-pyramid.md)
- [JUnit User Guide](./junit-user-guide.md)
- [REST Assured Documentation](./rest-assured-docs.md)
- [Pact Documentation](./pact-docs.md)
- [WireMock Java Documentation](./wiremock-java-docs.md)
