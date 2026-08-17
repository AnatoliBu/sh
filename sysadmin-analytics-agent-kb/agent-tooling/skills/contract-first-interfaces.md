---
artifact_type: skill
status: foundation
domain: agent-tooling
---

# Contract-First CLI and MCP

Turn heterogeneous executable interfaces into a normalized capability catalog, then generate or improve CLI, MCP, SDK, documentation, and tests from that catalog.

## Reference links

Authority references:

- [Model Context Protocol Specification](../../references/model-context-protocol-spec.md)
- [Command Line Interface Guidelines (clig.dev)](../../references/cli-guidelines-clig.md)

```text
OpenAPI / AsyncAPI / GraphQL / Protobuf / Smithy / CLI / MCP
      ↓ importers
Capability IR  →  lint → repair → enrich → classify
      ↓
SDK / CLI / MCP / docs / tests / registry
```

Treat OpenAPI as an important input format, not as the universal model for every tool. Use JSON Schema as the common type vocabulary where possible. Preserve transport-specific details separately from user-facing intent and behavior.

## Core Principles

1. **Separate transport from capability semantics.** HTTP paths, shell flags, RPC methods and MCP tool names are execution details; user intent, resource, action, risk, idempotency and expected result belong in the normalized model.
2. **Prefer one source of behavioral truth.** Generate CLI and MCP over a shared SDK or execution adapter. Do not independently reimplement authentication, pagination, retries, serialization, and errors in each interface.
3. **Do not equate endpoint count with tool count.** Small APIs may support direct operation-to-tool generation; large APIs require curation, grouping, semantic retrieval, workflow tools, or code mode.
4. **Use static contracts plus behavioral verification.** A schema can prove structure, not actual runtime behavior. Validate generated adapters against a sandbox, mock, fixture, or safe test environment.
5. **Preserve provenance.** Record which source, version, operation, command, or MCP server produced every capability. Generated files must be reproducible and auditable.

## Workflow

| # | Step | Governing rule | Detail |
|---|---|---|---|
| 1 | Inventory the sources | Classify by native contract format; do not force a source into OpenAPI when that erases streaming, shell state, resources, prompts, or events | [Contract Workflow](../patterns/contract-workflow.md) |
| 2 | Select the source of truth | Six-level ladder; state explicitly when the source is incomplete or inferred | [Source Extraction](../patterns/contract-source-extraction.md) |
| 3 | Import into Capability IR | Normalize names around resource and intent, never transport syntax | [Contract Workflow](../patterns/contract-workflow.md), [Capability IR Guide](../patterns/contract-capability-ir-guide.md) |
| 4 | Repair and enrich | Ten-point defect list; do not silently invent semantics — mark inferred with confidence and evidence | [Contract Workflow](../patterns/contract-workflow.md) |
| 5 | Classify MCP exposure | Tool / Resource / Prompt; not every readable endpoint is a Tool | [Contract Workflow](../patterns/contract-workflow.md) |
| 6 | Design the CLI surface | `tool <resource> <action>`; JSON for automation, stdout for data, stderr for diagnostics | [CLI Design Rules](../patterns/contract-cli-design-rules.md) |
| 7 | Control tool-surface size | Curation, dynamic retrieval, workflow tools, or code mode | [Scale Control](../patterns/contract-scale-control.md) |
| 8 | Generate adapters | Thin CLI and MCP renderers over one shared execution adapter | [Contract Workflow](../patterns/contract-workflow.md) |
| 9 | Validate | Static plus behavioral; no conformance claim without execution tests | [Validation Checklist](../patterns/contract-validation-checklist.md) |

## Hard Rules

- Never infer read-only status from `GET` alone or idempotency from `PUT` alone. Verify documented and observed behavior.
- Do not silently invent important semantics. Mark inferred fields with confidence and evidence.
- Do not hide destructive behavior inside a broad workflow without explicit metadata and confirmation policy.
- Never probe destructive commands against production state. Use disposable fixtures, temporary directories, mocks, or isolated accounts.
- Do not put runtime secrets or environment-specific credentials into the specification.
- Keep the original transport identifier in `transport` and `provenance`; do not leak URLs, verbs, or executable filenames into public names.
- Assign every executable capability a risk class and exactly one confirmation policy.

## References

| File | When to read |
|---|---|
| [Contract Workflow](../patterns/contract-workflow.md) | Doing the work: full nine steps, plus what an architecture or implementation task must return |
| [Source Extraction](../patterns/contract-source-extraction.md) | Choosing what to trust: source-of-truth ladder, OpenAPI-first criteria, extraction from an existing CLI, import from an existing MCP server, compact decision table per situation |
| the machine-readable capability schema | Writing the artifact: canonical machine-readable capability shape |
| [Capability IR Guide](../patterns/contract-capability-ir-guide.md) | Field semantics: minimum fields, naming per target, behavior claims, risk and confirmation, provenance and confidence levels |
| [CLI Design Rules](../patterns/contract-cli-design-rules.md) | Designing commands: inputs, outputs, exit-code categories, safety, pagination, configuration precedence |
| [Scale Control](../patterns/contract-scale-control.md) | Catalog too large for static tools; also the full anti-pattern list |
| [Validation Checklist](../patterns/contract-validation-checklist.md) | Before claiming done: static and behavioral QA checklist |
| the `x-capability` / `x-cli` / `x-mcp` vocabulary | Enriching a spec in place: `x-capability`, `x-cli`, `x-mcp` vocabulary |
| [Research and Standards](../patterns/contract-research-and-standards.md) | Background: standards and research reading list |
| the worked end-to-end example | End-to-end worked example: enriched OpenAPI → capability → MCP tool → CLI contract |
| a package self-check script | Validating this package and its JSON files |
