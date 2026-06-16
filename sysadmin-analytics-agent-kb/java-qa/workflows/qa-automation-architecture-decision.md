---
artifact_type: workflow
status: foundation
domain: java-qa
---

# Workflow: QA Automation Architecture Decision

## Purpose

Run a structured decision review before making a Java QA automation architecture change.

Use this workflow for framework choices, suite migration, test-layer selection, shared test-platform design, CI lane changes, service virtualization, contract testing, CLI/MCP exposure, and AI-agent automation tooling.

## Reference links

Authority references:

- [QA Skills Agent Catalog](../../references/qa-skills-agent-catalog.md)
- [Agentic QA Boilerplate](../../references/agentic-qa-boilerplate.md)
- [Practical Test Pyramid](../../references/practical-test-pyramid.md)
- [JUnit User Guide](../../references/junit-user-guide.md)
- [REST Assured Documentation](../../references/rest-assured-docs.md)
- [Pact Documentation](../../references/pact-docs.md)
- [WireMock Java Documentation](../../references/wiremock-java-docs.md)
- [Testcontainers for Java Documentation](../../references/testcontainers-java-docs.md)

## Input package

- Decision proposal.
- Product behavior or platform capability being protected.
- Source of truth for expected behavior.
- Current implementation and pain.
- Existing tests and CI lanes.
- Known flaky history or incident history.
- Tooling constraints and environment constraints.
- Agent/CLI/MCP consumer needs, if relevant.

## Review steps

1. State the decision in one sentence.
2. Identify protected behavior or platform capability.
3. Identify source of truth and classify assumptions.
4. Map current coverage and current pain.
5. Choose the cheapest sufficient test/tooling layer.
6. Check architecture fit and reuse path.
7. Check data, state, cleanup, and determinism.
8. Check assertion strength and diagnostics.
9. Check CI placement and runtime/stability impact.
10. Check agent-readiness when tooling is exposed to AI agents.
11. Compare alternatives.
12. Decide approve, spike first, defer, or reject and define proof.

## Output

```markdown
# QA Automation Architecture Decision

## Decision

approve / caution / reject / spike first / manual for now

## Proposal

## Protected behavior or capability

## Source of truth

## Recommended layer or architecture

## Alternatives considered

## Risks and mitigations

## Implementation slice

## Proof

## Follow-up artifacts
```

## Approval criteria

- The decision names the behavior or capability being protected.
- The selected layer is justified against cheaper alternatives.
- The source of truth is explicit.
- State and cleanup are deterministic enough for CI.
- Failure output will be diagnostic.
- CI placement is explicit.
- Agent-facing tools expose stable structured outputs and do not duplicate business logic.
