---
artifact_type: skill
status: foundation
domain: java-qa
---

# Skill: QA Automation Decision Flow

## Purpose

Guide an automation QA decision before implementation, refactoring, migration, or framework/tooling adoption.

Use this skill when the user asks whether to automate something, which test layer to use, whether to migrate a suite, how to structure a Java QA platform, or how to expose automation capabilities to AI agents.

The goal is not to maximize the number of tests. The goal is to choose the smallest maintainable testing and tooling move that gives useful confidence.

## Reference links

Authority references:

- [Practical Test Pyramid](../../references/practical-test-pyramid.md)
- [JUnit User Guide](../../references/junit-user-guide.md)
- [REST Assured Documentation](../../references/rest-assured-docs.md)
- [Pact Documentation](../../references/pact-docs.md)
- [WireMock Java Documentation](../../references/wiremock-java-docs.md)
- [Testcontainers for Java Documentation](../../references/testcontainers-java-docs.md)
- [Selenium WebDriver Documentation](../../references/selenium-webdriver-docs.md)
- [Playwright Best Practices](../../references/playwright-best-practices.md)
- [QA Skills Agent Catalog](../../references/qa-skills-agent-catalog.md)
- [Agentic QA Boilerplate](../../references/agentic-qa-boilerplate.md)

## Required inputs

Collect or infer:

- Decision type: new test, refactor, framework choice, migration, CLI/MCP/tooling, CI policy, test data, service virtualization, or release gate.
- Behavior source: product requirement, API contract, OpenAPI spec, bug report, incident, logs, analytics, or tribal knowledge.
- Risk: customer impact, defect likelihood, affected surface, release urgency, business criticality.
- Existing coverage: unit, component, integration, contract, API, UI, exploratory, monitoring.
- Current pain: flakiness, slow CI, duplicate assertions, brittle data, unclear oracle, framework lock-in, hard-to-debug failure.
- Constraints: language, build tool, CI task, environment access, data access, security boundaries, team skill.

## Decision sequence

### 1. Name the decision

State the decision in one sentence.

Bad:

```text
Improve tests.
```

Good:

```text
Decide whether order precheck validation should be covered by JUnit API tests, contract tests, Karate legacy scenarios, or CLI-backed agent tools.
```

### 2. Identify protected behavior

Define what must remain true from the user, API consumer, or system perspective.

Do not start from framework mechanics. Start from behavior and failure impact.

### 3. Locate the source of truth

Classify the oracle:

| Source | Strength | Notes |
|---|---:|---|
| Product requirement / accepted ticket | High | Best for expected behavior |
| OpenAPI / schema / contract | High for interface | Does not prove business correctness alone |
| Incident / escaped defect | High for regression risk | Convert to explicit behavior rule |
| Logs / analytics | Useful signal | Needs interpretation |
| Existing test only | Weak | May encode old mistakes |
| Tribal memory | Weak | Ask for confirmation or mark as assumption |

### 4. Choose the cheapest sufficient test layer

Prefer the lowest layer that gives the required confidence.

```text
pure logic → unit test
serialization / validation / mapping → component or API test
provider/consumer compatibility → contract test
real wiring / DB / queues / auth → integration test
critical user journey → UI/E2E or API journey test
production safety → smoke, synthetic monitoring, canary checks
```

High-level tests are allowed, but must protect high-level behavior, not duplicate cheap checks.

### 5. Check architecture fit

Ask:

- Does this move behavior into shared reusable test logic or scatter it across tests?
- Will API/schema changes fail close to generated clients, contracts, or compile/runtime validation?
- Can the same capability be reused from JUnit, CI, CLI, MCP, or agent workflows if needed?
- Does this reduce or increase framework lock-in?

For Java API automation, prefer:

```text
spec / contract / generated client
→ shared domain action or fixture
→ JUnit/API/contract/load/CLI/MCP consumer
```

Avoid:

```text
raw JSON copied across tests
one-off auth setup
framework-specific business logic
agent prompt that knows endpoint internals
```

### 6. Check data, state, and determinism

Decide how the test creates, isolates, and cleans data.

Reject or redesign if the plan depends on:

- hidden global mutable state;
- run-order dependency;
- shared user balance/state without cleanup;
- `Thread.sleep` instead of condition polling;
- production-like data that cannot be reset;
- external systems without virtualization or clear contract boundaries.

### 7. Check assertion strength and diagnostics

A good automated test answers:

- What behavior failed?
- What input caused it?
- What expected result was violated?
- Which dependency or environment assumption may be involved?
- What evidence is attached: response body, correlation ID, logs, screenshots, trace, contract diff?

Avoid assertions that only prove a request returned `200 OK` unless status code is the behavior under test.

### 8. Check CI economics

Classify the test or tool:

| Placement | Use |
|---|---|
| PR fast lane | Deterministic, fast, high-signal checks |
| Smoke | Minimal release/blocker confidence |
| Nightly | Slower cross-system regression |
| Release gate | Business-critical flow and known risk areas |
| Quarantine | Temporary location for known flaky tests with owner and removal rule |
| Manual/exploratory | High uncertainty, low automation ROI, unstable requirements |

### 9. Compare alternatives

Provide at least two viable options when the decision is architectural.

For each option, compare:

- confidence gained;
- implementation cost;
- maintenance cost;
- CI runtime/stability;
- coupling / lock-in;
- migration reversibility;
- agent-readiness, if relevant.

### 10. Recommend and define the proof

Return one of:

```text
DO
DO SMALL SPIKE FIRST
DO LATER
DO NOT DO
KEEP MANUAL / EXPLORATORY FOR NOW
```

Every recommendation needs a go/no-go proof.

Examples:

- One migrated API operation compiles from generated DTOs, validates contract, and runs in PR CI.
- One CLI command returns stable JSON, typed exit codes, and redacted secrets.
- One flaky test class is isolated and proves reduced failure rate over N CI runs.
- One service dependency is replaced by WireMock/Pact/Testcontainers without losing meaningful coverage.

## Output format

```markdown
## Decision

DO / DO SMALL SPIKE FIRST / DO LATER / DO NOT DO / KEEP MANUAL FOR NOW

## Protected behavior

What user/API/system behavior is protected.

## Source of truth

Requirement, contract, OpenAPI, bug/incident, logs, or assumption.

## Recommended test/tooling layer

Chosen layer and why lower/higher layers are not enough.

## Alternatives considered

| Option | Confidence | Cost | Maintenance | CI impact | Coupling | Verdict |
|---|---:|---:|---:|---:|---:|---|

## Risks

Real risks and how to reduce them.

## Implementation shape

Smallest safe steps.

## Go/no-go proof

Measurable exit criteria.

## What not to do

Specific anti-patterns to avoid.
```

## Anti-patterns

- Automating unclear behavior.
- Choosing UI/E2E because it is easiest to imagine, not because it is the right layer.
- Raw request JSON copied across tests.
- Business logic hidden in framework glue.
- Test code that is harder to read than the product behavior.
- Shared mutable state that blocks future parallel execution.
- No explicit test owner, suite placement, or cleanup policy.
- Adding agent prompts instead of stable CLI/MCP tools when tools are needed.
- Migrating old framework files 1:1 instead of migrating behavior capabilities.
