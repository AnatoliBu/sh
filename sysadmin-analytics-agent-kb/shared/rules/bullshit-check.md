---
artifact_type: rule
status: foundation
domain: shared
owner: Agent KB
last_checked: 2026-06-06
---

# Source Quality Check Mode

Use this mode when evaluating an external repo, skill pack, agent framework, MCP server, or documentation source.

## Reference links

Authority references:

- [References](../../references/README.md)

## Goal

Prevent weak repositories, demos, hype, and unaudited agent frameworks from entering the trusted base.

## Checks

1. Provenance: owner, maintainer, official status, track record.
2. Maintenance: commits, releases, issues, PRs, CI status.
3. Scope realism: whether claims match the actual code and tests.
4. Code and docs alignment: whether examples are executable and documented.
5. Blast radius: what systems the tool can reach or change.
6. Guardrails: read-only mode, approval gates, dry-run, audit trail, rollback.
7. Supply chain: pinned dependencies, reviewed install path, authenticated tool calls.

## Verdict levels

- Foundation.
- Useful after audit.
- Cheat sheet only.
- Moodboard only.
- Reject.

## Required output

```markdown
# Source Quality Check Report

## Source

## Claimed purpose

## Authority level

## Evidence

## Red flags

## What can be reused

## What must not be reused

## Verdict
```
