---
artifact_type: index
status: foundation
domain: agent-tooling
---

# Building the harness

Everything here is generic; the working copy lives in
`<your-tool-repo>/scripts/` (`ab-rerun-graph-arm.sh`, `compare_ab_runs.py`).

## 1. Two agent homes, one difference

One `CODEX_HOME` per arm. They must differ in **exactly one line** — the MCP endpoint.

`~/.codex-lab/config.toml` (arm WITH your tool):

```toml
# Isolated CODEX_HOME for the <tool> usability lab.
# Deliberately WITHOUT AGENTS.md, MEMORY.md, skills/ — the subject agent must get no domain hint
# outside the MCP tool surface itself.
model = "gpt-5.6-luna"
model_reasoning_effort = "low"        # weak on purpose: a strong model hides bad tool UX
approval_policy = "never"             # exec-mode has no human to approve → else "user cancelled MCP tool call"
sandbox_mode = "danger-full-access"

[mcp_servers.logs]
url = "http://127.0.0.1:9901/mcp/"    # your tool + the same core tools
enabled = true

[projects.'c:\users\...\wd\a-r1']     # every working dir must be pre-trusted, lowercase path
trust_level = "trusted"
```

`~/.codex-lab-flat/config.toml` — identical, except `url = "…:9904/mcp/"` (stock upstream, your
category disabled: `OPENSEARCH_ENABLED_CATEGORIES=""`).

**Second server for the control arm.** Add a lab-only compose service rather than reconfiguring the
real one, e.g. `docker-compose.lab.yml` with an `osflat` service on another port.

**Verify the two surfaces before trusting a run** — count tools and description bytes each arm pays
for in context:

```python
resp = ost._mcp_rpc(port, 'tools/list', {})
tools = resp['result']['tools']
print(len(tools), sum(len(t.get('description') or '') for t in tools))
```

A tool surface is not free: the the project flat arm carried 11 tools ≈2.5k tokens before a single call.

## 2. Runner

```bash
run_one() {
  local task=$1 round=$2 wd winwd
  wd="$WD_ROOT/$task-r$round"
  rm -rf "$wd"; mkdir -p "$wd"          # EMPTY, and outside the results dir (see the leak trap)
  winwd=$(cygpath -m "$wd")             # Windows: codex wants a native path
  CODEX_HOME="$HOME_ARM" timeout 900 codex exec \
      --skip-git-repo-check -C "$winwd" --json \
      -o "$RUNS/$task-$arm-r$round.last.txt" \
      < "$LAB/prompts/$task.txt" \
      > "$RUNS/$task-$arm-r$round.jsonl" 2> "$RUNS/$task-$arm-r$round.err"
  echo "$task $arm-r$round rc=$? dur=$((end-start))s" >> "$IDX"
}
```

- `--json` is what makes the run measurable (event stream), `-o` keeps the final answer separate.
- Parallelism 2 keeps the stand's load comparable between rounds; more skews durations.
- `timeout 900` — a hung tool call must end the run, not the day. An `rc=124` IS a finding.

## 3. Parsing the event stream

Per line of `<task>-<arm>.jsonl`:

| event | meaning |
|---|---|
| `item.started` + `item.type == "mcp_tool_call"` | one tool call — record `tool` + `arguments` |
| `item.completed` + `mcp_tool_call` | match to the open call; `item.error` → tool-level failure |
| `item.started` + `command_execution` | shell fallback — **a high count means the agent bypassed your tool** |
| `item.completed` + `agent_message` | narration; the last one is usually the answer |
| `turn.completed` | `usage.input_tokens` / `output_tokens` |

Metrics worth printing: calls · errors · shells · in/out tokens · duration · the SET of tools used
(the set alone often tells the whole story — e.g. `YourTool` disappearing from the list).

## 4. Mechanical checks alongside the behavioural run

Behavioural runs are noisy; pair them with a deterministic script that asserts each past finding is
gone, one check per piece of evidence, PASS/FAIL + raw evidence
(`verify_findings.py` is the reference). Rules learned the hard way:

- a check must fail for the RIGHT reason — ours once failed on its own stale criterion (it grepped
  pre-`outputSchema` prose while the tool had moved to `structuredContent`);
- keep it in the repo, not in a temp dir;
- expected-FAIL checks (a fix not shipped yet) are fine if labelled as such.
