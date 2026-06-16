---
artifact_type: reference
authority_tier: Tier B
status: useful-after-audit
source_type: open-source-agentic-qa-boilerplate
topics:
  - qa
  - agentic-qa
  - qa-lifecycle
  - regression
  - go-no-go
  - test-automation
domains:
  - java-qa
owner: upex-galaxy / agentic-qa-boilerplate
last_checked: 2026-06-16
source_url: https://github.com/upex-galaxy/agentic-qa-boilerplate
---

# Reference: Agentic QA Boilerplate

## Authority tier

Tier B

## Status

useful-after-audit

## Owner / maintainer

upex-galaxy / agentic-qa-boilerplate

## URL

https://github.com/upex-galaxy/agentic-qa-boilerplate

## Last checked

2026-06-16

## Scope

Agentic QA lifecycle pattern: project discovery, shift-left planning, sprint testing, test documentation, automation, regression, and release GO / CAUTION / NO-GO decision flow.

Use this source for:

- staged QA workflow design;
- command/skill decomposition ideas;
- lifecycle handoff between planning, testing, automation, and release readiness;
- agent context structure ideas.

## Why trusted

The repository is a concrete public implementation of a multi-skill QA agent workflow rather than a generic article. It is useful as an implementation reference for orchestrating QA work through explicit stages and decision gates.

## Caveats

The repository is centered on Playwright, TypeScript, KATA automation, and its own project conventions. Do not import its stack assumptions into Java API automation without review.

For this repository, use the lifecycle shape, not the exact toolchain.

## Agent-facing artifacts that may consume this reference

- [Java QA Agent](../java-qa/agent.md)
- [QA Automation Decision Flow](../java-qa/skills/qa-automation-decision-flow.md)
- [Agentic QA Tooling Design](../java-qa/skills/agentic-qa-tooling-design.md)
- [QA Automation Architecture Decision Workflow](../java-qa/workflows/qa-automation-architecture-decision.md)

## Extracted rules

- Separate QA decision stages: discover context, assess risk, design strategy, document tests, automate only the right layer, then run a release-readiness gate.
- Make GO / CAUTION / NO-GO decisions explicit rather than burying them in prose.
- Keep automation tied to product risk and regression value, not to framework enthusiasm.
- Treat agent workflows as auditable procedures with expected inputs and outputs.

## Do not use this source for

- Java framework API behavior.
- Product-specific expected results.
- Claiming Playwright/TypeScript is the target stack for Java API automation.
- Replacing official documentation for JUnit, Selenium, REST Assured, Pact, WireMock, or Testcontainers.

## Related references

- [QA Skills Agent Catalog](./qa-skills-agent-catalog.md)
- [Practical Test Pyramid](./practical-test-pyramid.md)
- [Selenium WebDriver Documentation](./selenium-webdriver-docs.md)
