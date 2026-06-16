---
artifact_type: rule
status: foundation
domain: java-qa
---

# Rule: Automation Decision Quality Gates

## Purpose

Prevent low-value, brittle, or misleading automation from entering the long-term Java QA suite or agent toolchain.

Apply this rule to new tests, migrated tests, framework refactors, CI suite changes, CLI commands, MCP tools, and AI-generated automation.

## Reference links

Authority references:

- [Practical Test Pyramid](../../references/practical-test-pyramid.md)
- [Selenium WebDriver Documentation](../../references/selenium-webdriver-docs.md)
- [JUnit User Guide](../../references/junit-user-guide.md)
- [QA Skills Agent Catalog](../../references/qa-skills-agent-catalog.md)
- [Agentic QA Boilerplate](../../references/agentic-qa-boilerplate.md)

## Required gates

### 1. Behavior gate

Automation must name the protected behavior. Reject or defer when expected behavior is unknown, the only oracle is an existing flaky or unclear test, the test only checks implementation details, or the test only proves that code executed.

### 2. Layer gate

The selected layer must be justified. Prefer a lower-cost layer when it gives equivalent confidence.

### 3. Oracle gate

Every assertion must trace to product requirement, API contract, OpenAPI schema, consumer/provider contract, bug regression rule, domain invariant, or explicit stakeholder decision.

Mark tribal or inferred expected behavior as an assumption.

### 4. Determinism gate

Automation must define data setup, isolation, cleanup, and dependency control.

Block or redesign when it depends on shared mutable state, run order, uncontrolled third-party dependency, arbitrary sleeps, dirty persistent data, or undocumented manual preconditions.

### 5. Diagnostics gate

Failure output must help classify the cause. Capture relevant inputs, expected vs actual result, failure category, and environment context.

### 6. CI placement gate

Every test or tool must have an intended execution lane: PR fast lane, smoke, nightly regression, release gate, manual/exploratory, or quarantine with owner and expiry.

### 7. Agent-safety gate

Agent-facing tooling must expose stable structured output, typed failure categories, secret redaction, mutation/cleanup policy, and a clear reuse path through shared core logic.

## Decision result labels

- `approved`
- `approved-with-risk`
- `spike-first`
- `manual-for-now`
- `reject`

## Anti-patterns to block

- New automation without a named protected behavior.
- Status-only API checks that do not validate the business or contract result.
- UI/E2E tests for logic that belongs in unit/component/API/contract layers.
- Shared mutable test data with no isolation plan.
- Prompt-only agent behavior where stable tools are required.
- Quarantine with no owner, expiry, or removal criterion.
