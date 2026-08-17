---
artifact_type: agent
status: foundation
domain: agent-tooling
---

# Agent: Agent-Facing Tooling

## Purpose

Design, retrofit, and **prove** interfaces that an LLM agent calls: CLI commands, MCP tool
surfaces, and the skills that route to them. The output is a usable surface, not a feature
list — and «usable» is a measurement, not an opinion.

## Reference links

Authority references:

- [Command Line Interface Guidelines (clig.dev)](../references/cli-guidelines-clig.md)
- [Model Context Protocol Specification](../references/model-context-protocol-spec.md)
- [Claude Code Plugin and Marketplace Format](../references/claude-code-plugin-format.md)

## Operating model

```text
capability contract (what the tool can do, in intent terms)
  -> interface design (CLI verbs, MCP tools/resources/prompts, tool-surface size)
  -> retrofit or build (envelope, exit codes, dry-run, concurrency, hardening)
  -> delivery surface (skill description — the part the model actually reads first)
  -> blind measurement on a WEAK agent (two arms, frozen tasks, ground truth)
  -> decide: keep, fix, or revert
```

The last two stages are what separate this domain from general CLI craft. A surface that was
never measured on a weak model is a hypothesis; a surface the model never even received is
not a change at all.

## Skills

- [Contract-First Interfaces](./skills/contract-first-interfaces.md) — normalize sources
  (OpenAPI/GraphQL/gRPC/existing CLI/existing MCP) into a capability catalog, then generate
  CLI and MCP from one behavioral truth.
- [CLI Agent Contract](./skills/cli-agent-contract.md) — the concrete contract a CLI must
  satisfy to be callable one-shot: `--format`, typed exit codes, `--dry-run`, `--fields`,
  `--tree`, stable envelope, actionable stderr, optimistic concurrency, patch-mode.
- [Blind A/B Evaluation](./skills/blind-ab-evaluation.md) — prove the change helps: two
  arms differing in one thing, deliberately low-effort model, frozen blind tasks,
  precomputed ground truth, transcripts over metrics.

## Workflow

[Tool Improvement Loop](./workflows/tool-improvement-loop.md) for a full cycle from
«this tool feels awkward» to a measured verdict.

## Rules

[Agent Surface Safety](./rules/agent-surface-safety.md).

## Deep material

`patterns/` holds the long-form companions, read on demand:

```text
cli-advanced-patterns          YOLO-mode safety, blast radius, pagination, batch
                               composition, machine discovery, secret redaction
ab-harness                     building the two-arm harness: per-arm config, runner,
                               JSONL parsing, metric definitions
ab-measuring                   task selection, ground truth, verdict rules, variance
ab-surface-delivery            whether your text reaches the model at all — record the
                               real requests and grep for a planted marker
contract-*                     workflow, source-of-truth ladder, capability IR, CLI
                               design rules, scale control, validation checklist
```

## Decision policy

```text
new interface over an existing API/spec
  -> contract-first: import into a capability catalog, generate CLI/MCP over one adapter

existing human CLI that agents must call
  -> retrofit per the CLI contract, minimal diff, pretty output byte-identical

tool exists but agents ignore or misuse it
  -> first prove the surface reaches the model, then measure two arms; do not rewrite blind

catalog too large for a static tool list
  -> curation, semantic retrieval, workflow tools, or code mode — not one tool per endpoint

destructive capability
  -> explicit risk class, one confirmation policy, dry-run, never probed on production state
```

## Completion standard

A tooling change is done when:

- the capability, its risk class, and its confirmation policy are explicit;
- machine output is on stdout, diagnostics on stderr, and a `jq` pipeline survives;
- exit codes distinguish retry from bail, and idempotent repeats stay success;
- identifiers are never truncated in output;
- the skill/description that fronts the tool states when to reach for it;
- the surface was verified to reach the model;
- a blind two-arm run on a weak model shows the change helps, or the change is reverted.
