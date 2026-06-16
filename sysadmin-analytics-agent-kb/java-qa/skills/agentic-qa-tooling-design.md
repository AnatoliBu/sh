---
artifact_type: skill
status: foundation
domain: java-qa
---

# Skill: Agentic QA Tooling Design

## Purpose

Design QA automation capabilities so AI agents can safely use them through stable tools instead of relying on prompt-only knowledge.

Use this skill when exposing Java QA automation to CLI, MCP, CI diagnostics, local debugging commands, or AI coding agents.

## Reference links

Authority references:

- [QA Skills Agent Catalog](../../references/qa-skills-agent-catalog.md)
- [Agentic QA Boilerplate](../../references/agentic-qa-boilerplate.md)
- [REST Assured Documentation](../../references/rest-assured-docs.md)
- [Pact Documentation](../../references/pact-docs.md)
- [WireMock Java Documentation](../../references/wiremock-java-docs.md)
- [Testcontainers for Java Documentation](../../references/testcontainers-java-docs.md)
- [Practical Test Pyramid](../../references/practical-test-pyramid.md)

## Core idea

Agents should call stable domain tools. They should not manually assemble internal API requests, parse human logs, or depend on tribal endpoint knowledge.

Prefer:

```text
generated client / contract / fixture
→ shared domain action
→ JUnit, CI, CLI, MCP, or agent workflow
```

Avoid:

```text
agent prompt
→ raw endpoint URL
→ hand-written JSON
→ ad-hoc log parsing
```

## Required inputs

- Target consumer: human CLI, AI coding agent, MCP client, CI job, IDE plugin, or test framework.
- Domain action to expose.
- Inputs and outputs required by the action.
- Secret handling and redaction needs.
- Expected failure categories.
- Whether the action mutates data.
- Whether the action can be safely retried.
- Required evidence: request ID, correlation ID, response body, contract diff, logs, screenshots, trace link.

## Tooling design checklist

### 1. Start from a domain action

Good tool names describe a QA/product action:

```bash
lp-test order precheck --env test6 --actor main-customer --fixture default-cart --json
lp-test contract validate --operation orderPrecheck --status 200 --body response.json
lp-test db find-order --env test6 --order-id 123 --json
```

Bad tool names leak transport details or framework internals:

```bash
curl-post-order-json
run-karate-feature-123
parse-app-log-grep
```

### 2. Return structured output

Every agent-facing command should support machine-readable output.

Minimum JSON shape:

```json
{
  "status": "passed|failed|error",
  "category": "contract|assertion|environment|auth|data|timeout|tooling",
  "summary": "short human-readable result",
  "inputs": {},
  "evidence": {},
  "redactionsApplied": true
}
```

### 3. Use typed exit codes or typed error categories

Agents need to know whether to fix test code, product code, data, environment, credentials, or contracts.

Recommended categories:

| Category | Meaning |
|---|---|
| `assertion` | Behavior violated |
| `contract` | Schema/provider-consumer mismatch |
| `auth` | Credential/session/permission problem |
| `data` | Missing, dirty, or conflicting test data |
| `environment` | Dependency or environment unavailable |
| `timeout` | Polling or response deadline exceeded |
| `tooling` | CLI/MCP/test harness problem |
| `unknown` | Needs human classification |

### 4. Make mutation explicit

For every mutating tool, define:

- idempotency;
- retry policy;
- cleanup strategy;
- generated test data prefix or run ID;
- dry-run behavior, if available;
- environment restrictions.

### 5. Keep secrets out of outputs

Agent-facing tooling must redact:

- tokens;
- cookies;
- passwords;
- authorization headers;
- personally identifiable data;
- private infrastructure details.

### 6. Keep MCP thin

MCP tools should wrap the same core behavior as CLI/JUnit where possible. Do not build a second implementation of business logic for MCP.

## Output format

```markdown
## Tooling recommendation

Build / do not build / spike first.

## Target consumer

Human CLI / AI agent / MCP / CI / IDE.

## Domain action

The reusable action being exposed.

## Interface

Inputs, outputs, exit categories, evidence, redaction.

## Safety model

Mutation, retry, cleanup, environment restrictions.

## Reuse path

Which shared core code is reused by JUnit, CLI, MCP, or CI.

## Go/no-go proof

One command/tool invocation with stable JSON and typed failure handling.

## What not to do

Specific shortcuts that would make the tool unsafe or unmaintainable.
```

## Anti-patterns

- Agent tools that call raw private endpoints directly.
- CLI output that is only prose or logs.
- MCP implementation that duplicates business logic from tests.
- Retrying non-idempotent mutations without guardrails.
- Leaking secrets into traces, JSON, logs, or screenshots.
- Treating tool success as product correctness when assertions are weak.
