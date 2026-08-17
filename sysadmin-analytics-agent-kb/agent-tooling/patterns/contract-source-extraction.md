---
artifact_type: index
status: foundation
domain: agent-tooling
---

# Source Selection and Extraction

Which source to trust, and how to extract a contract from each kind.

## Source-of-truth ladder

Prefer in this order:

1. Maintained machine-readable contract
2. Typed implementation capable of deterministic schema generation
3. Native introspection protocol
4. Structured documentation and completions
5. Black-box behavioral extraction
6. Manual modeling

State explicitly when the available source is incomplete or inferred.

## Compact decision table

| Situation | Preferred approach |
|---|---|
| Small, clean REST API | OpenAPI → Capability IR → CLI + MCP |
| Large REST API | OpenAPI → IR → curation/retrieval/code mode |
| Internal typed service | Typed functions → JSON Schema/IR → interfaces |
| GraphQL service | Introspection/schema → IR → task-oriented tools |
| gRPC or Smithy service | Native IDL → IR → adapters |
| Existing structured CLI | CLI schema/completions → IR → MCP |
| Legacy CLI | docs/help → grammar → sandbox probing → IR |
| Existing MCP server | MCP discovery → IR → catalog/proxy/CLI |
| Event-driven system | AsyncAPI/native event contract → IR; do not force REST semantics |

## OpenAPI-First Rules

OpenAPI is sufficient as the initial source when:

- the system is predominantly HTTP/REST
- schemas are complete
- operation identifiers are stable
- security schemes are defined
- operation descriptions reflect user intent
- the API surface is small or will be curated

Use OpenAPI specification extensions for missing generation semantics. The recommended extension shape is shown in the `x-capability` / `x-cli` / `x-mcp` vocabulary.

Important extensions include:

```text
x-capability  normalized identity, intents, risk, behavior
x-cli         command path, positional arguments, flags, output modes
x-mcp         exposure type, public name, grouping, enablement
```

Do not put runtime secrets or environment-specific credentials into the specification.

## Existing CLI Extraction

Use native machine-readable schema when available. Otherwise apply this extraction ladder:

```text
--help / subcommand help / man pages / docs / shell completions
                              ↓
                     command grammar
                              ↓
                  sandboxed test matrix
                              ↓
       stdout / stderr / exit code / file and state diffs
                              ↓
                       Capability IR
```

Capture:

- command tree
- positional arguments
- flags and aliases
- types, defaults, enums, and repeatability
- environment variables
- stdin and TTY requirements
- output formats
- exit codes
- side effects
- created, modified, and deleted files
- network calls when observable and permitted
- interactive prompts

Never probe destructive commands against production state. Use disposable fixtures, temporary directories, mocks, or isolated accounts.

## Existing MCP Import

Read all three surfaces:

```text
tools/list
resources/list
prompts/list
```

Preserve their distinctions in Capability IR. Do not flatten Resources and Prompts into Tools unless the target interface cannot represent them and the loss is explicitly accepted.

Record:

- server identity and version
- item names and descriptions
- input and output schemas
- annotations
- resource URIs and templates
- prompt arguments
- authentication and transport
- pagination or cursor behavior
