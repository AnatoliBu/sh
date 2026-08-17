---
artifact_type: skill
status: foundation
domain: agent-tooling
---

# Agentic A/B lab

**Why:** an agent-facing tool is only as good as what a *weak* agent does with it. Author intuition
and your own (strong-model) session prove nothing — a measured run on a real tool turned six "obvious wins"
into four real bugs and one regression nobody predicted.

## Reference links

Authority references:

- [Model Context Protocol Specification](../../references/model-context-protocol-spec.md)
- [Claude Code Plugin and Marketplace Format](../../references/claude-code-plugin-format.md)

**Working reference implementation** (copy it, don't reinvent):
`<your-tool-repo>/scripts/` — `ab-rerun-graph-arm.sh` (runner),
`compare_ab_runs.py` (metrics + before/after table), `verify_findings.py` (mechanical checks).
Live results: TASK-002 / TASK-003 in that repo's `_docs/`.

## The shape

| Piece | Rule |
|---|---|
| **Subject** | `codex exec --json` (headless), **deliberately weak**: `model_reasoning_effort = "low"`. A strong model papers over bad tool UX. |
| **Arms** | Two MCP endpoints differing in **exactly one thing**: your tool present vs absent (stock upstream). Same model, same prompts, same data. |
| **Isolation** | Separate `CODEX_HOME` per arm, **no AGENTS.md / MEMORY.md / skills** — the tool surface must be the only source of domain hints. `approval_policy = "never"` + `sandbox_mode = "danger-full-access"`, else every MCP call comes back "user cancelled". |
| **Tasks** | 5–8 **blind** prompts written as a support ticket ("клиент жалуется…", "вот обрезанный лог"), never naming a tool. Freeze them — they are the yardstick across releases. |
| **Ground truth** | Precomputed by direct queries into `ground_truth.json`, so "did it answer right" is not an opinion. |
| **Repeats** | ≥2 rounds per task, and treat any single flip as noise: three tasks reversed between attempts. |

## Run it

```bash
bash scripts/ab-rerun-graph-arm.sh          # both rounds, 2 tasks in parallel, timeout 900s each
python scripts/compare_ab_runs.py           # per-run table + delta line per task
python scripts/compare_ab_runs.py D graph-w2r1   # dump ONE run: every tool call + final answer
```

## Reading the result — the part that matters

Metrics (`calls`, `errors`, `tokens`, `dur`) only *point at* the interesting runs. The finding is
always in the transcript: **which tool the agent reached for, and what it did after your tool
answered.** In one re-measure, "1 → 7 calls" was not noise — it was the agent receiving a
technically perfect refusal and abandoning the tool entirely (BUG-008).

⚠ **Trap that invalidates the whole QUESTION, not just a run — check it FIRST.** Before measuring any
edit to an agent-facing surface, prove the surface reaches the model: record what the client actually
sends (`record_model_requests.py` in the reference repo — a transparent proxy in front of the real
endpoint) and grep the first request for a marker planted in your text. On codex ≥0.14x with a
`code_mode_only` model, MCP tool descriptions and server `instructions` are **not in the model's
context at all** — the model gets `exec` plus "deferred tools are listed in `ALL_TOOLS`", and your
text first appears in the output of a JS filter the agent has to think of writing. Two rounds
(p = 0.50, then a third abandoned) were spent editing words the model never saw. What *does* arrive
unprompted is a skill's `description` line (`<skills_instructions>`, first request) — moving the same
claim there took the metric 17/30 → 30/30, p = 2.3e-05. Details: [Surface Delivery](../patterns/ab-surface-delivery.md).

⚠ **Traps that invalidate a run** (all three cost us a full round):

1. **Leaked answers.** Working dirs inside the results dir → the agent read last run's `.last.txt`
   via `cd ..` and answered with **0 tool calls**. Give every run an EMPTY dir far from artifacts.
2. **Stale server.** The arm must serve the CURRENT code — a native fallback launcher pointing at
   an old checkout serves month-old behaviour while `/health` says OK.
3. **Uncontrolled background state.** A red `verify` verdict, a stale nudge, or a leftover plugin
   (`github.list_repositories` showed up mid-run) changes the agent's behaviour. Note it as
   background, or clean it — and never compare across different background states.

## References

| File | When to read |
|---|---|
| [A/B Harness](../patterns/ab-harness.md) | Building the harness from scratch: config.toml per arm, runner script, JSONL event parsing, metric definitions |
| [Measuring](../patterns/ab-measuring.md) | Choosing tasks, writing ground truth, verdict rules, variance/n, what a "win" may and may not claim |

**Related:** [CLI Agent Contract](./cli-agent-contract.md) (the contract you are A/B-testing on a CLI) ·
[Contract-First Interfaces](./contract-first-interfaces.md) (tool-surface design) ·
a headless runner for the subject model (the subject runner).
