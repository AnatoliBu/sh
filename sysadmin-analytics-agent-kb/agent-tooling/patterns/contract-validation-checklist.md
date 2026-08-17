---
artifact_type: index
status: foundation
domain: agent-tooling
---

# Validation Checklist

## Source integrity

- [ ] Source format and version are recorded.
- [ ] Imported operation or command identifiers are traceable.
- [ ] Missing source fields are marked as inferred rather than silently invented.
- [ ] Deprecated operations are identified.

## Capability model

- [ ] Capability ID is stable and unique.
- [ ] Provider, resource, and action are populated.
- [ ] Intents describe actual user requests.
- [ ] Input schema has bounded types and required fields.
- [ ] Output schema represents the normalized result.
- [ ] Error behavior is represented.

## Behavior and safety

- [ ] Read-only classification is verified.
- [ ] Destructive classification is verified.
- [ ] Idempotency is verified.
- [ ] Retry policy matches idempotency and failure modes.
- [ ] External communication is marked.
- [ ] Confirmation policy is explicit.
- [ ] Financial, permission, and identity effects are marked.

## CLI

- [ ] Command hierarchy is resource-oriented.
- [ ] Positional arguments are minimal and obvious.
- [ ] Flag names are unique and consistent.
- [ ] Structured output exists.
- [ ] stdout and stderr are separated.
- [ ] Exit codes are stable.
- [ ] Non-interactive operation is possible where appropriate.
- [ ] Large payloads can use stdin or files.
- [ ] Destructive actions show their target.

## MCP

- [ ] Tool, Resource, and Prompt distinctions are preserved.
- [ ] MCP names are stable and understandable.
- [ ] Input and output schemas are usable by a model.
- [ ] Behavioral annotations are populated.
- [ ] Large catalogs use curation, retrieval, workflows, or code mode.
- [ ] Sensitive tools are not advertised without appropriate authorization.

## Behavioral conformance

- [ ] Valid examples execute successfully.
- [ ] Invalid examples fail predictably.
- [ ] Actual output validates against the declared schema.
- [ ] CLI and MCP normalize equivalent results.
- [ ] Pagination and cursors terminate correctly.
- [ ] Retries do not duplicate unsafe operations.
- [ ] Read-only tests produce no state diff.
- [ ] Destructive tests run only in isolated fixtures.
