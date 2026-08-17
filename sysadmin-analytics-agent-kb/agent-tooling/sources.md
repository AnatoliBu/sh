---
artifact_type: index
status: foundation
domain: agent-tooling
---

# Agent Tooling Sources

This domain separates **what a surface must satisfy** (standards) from **whether it actually
works** (measurement). Standards can be cited; usability has to be run.

## Foundation authority

1. [Model Context Protocol Specification](../references/model-context-protocol-spec.md)
   - tools vs resources vs prompts, consent requirements, and the clause that a tool's own
     annotations are untrusted.
2. [Command Line Interface Guidelines (clig.dev)](../references/cli-guidelines-clig.md)
   - stdout/stderr split, machine output modes, exit codes, dry-run, confirmation of
     dangerous actions, TTY-gated interactivity.
3. [Claude Code Plugin and Marketplace Format](../references/claude-code-plugin-format.md)
   - how a skill or tool surface is actually delivered to a machine and updated there.

## What the standards do not cover

Everything in `patterns/` exists because the sources above stop short of it:

```text
agent envelope shape          stable top-level keys across commands, data per command
domain-rich exit codes        retry-vs-bail semantics beyond success/failure
optimistic concurrency        hash + --if-match + conflict exit for shared resources
output-size guard             large payload to a file, path in the summary line
schema-before-data            --tree so the agent navigates before dumping
patch-mode for text fields    unique-substring edits instead of multi-KB rewrites
tool-surface sizing           curation, retrieval, workflow tools, code mode
delivery verification         proving the description reaches the model
blind two-arm measurement     weak model, frozen tasks, precomputed ground truth
```

## Trust rule

A standard defines the container. Whether an agent can use what is inside it is decided by a
measured run, and a measured run may only claim what it measured: this model, this effort
level, these tasks, this many rounds.
