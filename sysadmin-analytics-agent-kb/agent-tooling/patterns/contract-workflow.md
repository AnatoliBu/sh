---
artifact_type: index
status: foundation
domain: agent-tooling
---

# Decision Workflow

Full nine-step procedure. `SKILL.md` carries only the step table; this file is the detail.

## 1. Inventory the sources

Classify every source:

- REST or HTTP API: OpenAPI
- Event or message API: AsyncAPI
- Graph API: GraphQL schema or introspection
- RPC API: Protobuf/gRPC or Smithy
- Typed internal functions: language types plus generated JSON Schema
- Existing CLI: native schema, help output, man pages, completions, docs, and black-box probing
- Existing MCP: `tools/list`, `resources/list`, and `prompts/list`

Do not force a source into OpenAPI when doing so would erase important semantics such as streaming, shell state, resource retrieval, prompts, or event subscriptions.

## 2. Select the source of truth

Ladder and per-source extraction procedures: [Source Extraction](../patterns/contract-source-extraction.md).

State explicitly when the available source is incomplete or inferred.

## 3. Import into Capability IR

Normalize names around resources and intent, not transport syntax.

Good:

```text
github.issues.create
github.pull_requests.merge
kubernetes.deployments.restart
```

Bad:

```text
post_repos_owner_repo_issues
patch_api_v1_namespaces_namespace_deployments_name
```

Keep the original transport identifier in `transport` and `provenance`. Naming conventions per target: [Capability IR Guide](../patterns/contract-capability-ir-guide.md).

## 4. Repair and enrich

Check for:

- missing or unstable operation identifiers
- weak summaries and descriptions
- unspecified request or response schemas
- inconsistent enums and nullability
- missing errors
- missing pagination metadata
- incomplete authentication requirements
- absent examples
- incorrect read-only, destructive, or idempotent classification
- ambiguous resource and action names

Do not silently invent important semantics. Mark inferred fields with confidence and evidence.

## 5. Classify MCP exposure

Use the following default mapping:

- **Tool**: executable action, query, mutation, calculation, or workflow
- **Resource**: addressable context that is primarily read, browsed, subscribed to, or referenced
- **Prompt**: reusable user-controlled interaction template

Do not convert every readable endpoint into a Tool by default. Prefer Resources for stable, addressable context when the target MCP runtime and client can use them effectively.

For tools, populate behavioral annotations when known: read-only, destructive, idempotent, open-world or external side effects.

## 6. Design the CLI surface

Organize commands by provider, domain, resource, and action:

```text
tool <provider> <resource> <action>
```

or, inside a provider-specific CLI:

```text
tool <resource> <action>
```

Use:

- positional arguments only for stable, obvious primary identifiers
- flags for optional or ambiguous inputs
- stdin for large text or structured payloads
- JSON output for automation
- human-readable output for interactive use
- stdout for result data
- stderr for diagnostics
- meaningful exit codes
- non-interactive mode
- `--dry-run` or equivalent for risky operations when feasible

Full rules, exit-code categories and configuration precedence: [CLI Design Rules](../patterns/contract-cli-design-rules.md).

## 7. Control tool-surface size

Strategies (curated tools, dynamic retrieval, workflow tools, code mode) and their trade-offs: [Scale Control](../patterns/contract-scale-control.md).

Do not hide destructive behavior inside a broad workflow without explicit metadata and confirmation policy.

## 8. Generate adapters

Prefer this implementation shape:

```text
Capability IR
    ↓
shared execution adapter or generated SDK
    ├── CLI renderer
    ├── MCP renderer
    ├── documentation renderer
    └── test renderer
```

Generated CLI and MCP layers should remain thin. Authentication, retries, pagination, request construction, response parsing, and error normalization should be shared.

## 9. Validate

Perform both static and dynamic checks.

### Static checks

- schemas parse and resolve
- required fields are present
- names are unique and stable
- input and output schemas are bounded and comprehensible
- auth scopes are attached
- risk metadata is populated
- CLI flags do not collide
- MCP names satisfy runtime constraints
- generated documentation matches schemas

### Behavioral checks

- valid examples succeed
- invalid inputs fail predictably
- output matches declared schema
- exit codes and error objects are stable
- pagination terminates correctly
- retries do not duplicate non-idempotent actions
- destructive actions require the declared confirmation policy
- read-only actions do not mutate state
- CLI and MCP produce equivalent normalized results

Use [Validation Checklist](../patterns/contract-validation-checklist.md).

## Output Expectations

For an architecture or design task, return:

1. source inventory
2. selected source-of-truth strategy
3. normalized taxonomy
4. Capability IR proposal or patch
5. CLI mapping
6. MCP mapping
7. scale-control strategy
8. generation pipeline
9. validation plan
10. unresolved assumptions and risks

For an implementation task, additionally produce:

- machine-readable Capability IR
- generated or patched OpenAPI extensions
- CLI command tree
- MCP definitions
- conformance fixtures or tests
- a reproducible generation command
