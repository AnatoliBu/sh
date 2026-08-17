---
artifact_type: workflow
status: foundation
domain: agent-tooling
---

# Workflow: Tool Improvement Loop

## Reference links

Authority references:

- [Command Line Interface Guidelines (clig.dev)](../../references/cli-guidelines-clig.md)
- [Model Context Protocol Specification](../../references/model-context-protocol-spec.md)
- [Claude Code Plugin and Marketplace Format](../../references/claude-code-plugin-format.md)

## Goal

Take a tool that agents use badly — ignored, misused, or expensive — and end with a measured
verdict instead of a plausible refactor.

## Flow

```text
1. SYMPTOM
   name what the agent actually did wrong: wrong tool chosen, tool called then abandoned,
   raw dump into context, retry loop, fallback to curl/ssh

2. LOCATE THE LAYER
   discovery   -> the model never learned the tool exists or when to use it
   contract    -> it called the tool and could not use the answer
   capability  -> the answer it needed does not exist yet

3. FOR A DISCOVERY PROBLEM
   prove the text reaches the model (record real requests, grep a planted marker)
   fix where the model actually reads: the skill description first

4. FOR A CONTRACT PROBLEM
   retrofit per the CLI contract: envelope, exit codes, dry-run, fields, tree,
   full identifiers, actionable hints — minimal diff, pretty output preserved

5. FOR A CAPABILITY PROBLEM
   grow the tool, do not compensate in the agent: the missing slice becomes code,
   with tests, in the tool's own repo

6. FREEZE THE YARDSTICK
   5-8 blind tasks phrased as tickets, never naming a tool; precomputed ground truth

7. TWO ARMS, ONE DIFFERENCE
   same model (deliberately low effort), same data, isolated agent home,
   tool present vs absent — nothing else may differ

8. RUN >=2 ROUNDS
   treat a single flip as noise

9. READ TRANSCRIPTS, NOT ONLY METRICS
   calls/errors/tokens/duration point at the interesting run; the finding is what the
   agent reached for and what it did after the tool answered

10. VERDICT
    keep / fix / revert, stated with the numbers and the sample size

11. RECORD
    what was measured, what it may claim, and what stayed unmeasured
```

## What each layer costs

```text
discovery fix   cheapest, highest leverage — a description line can move a metric more
                than a rewrite of the tool
contract fix    bounded work with a clear checklist and verifiable one-liners
capability fix  real engineering; justified when the answer genuinely is not obtainable
```

Diagnosing a discovery problem as a contract problem is the common expensive mistake: the
tool gets rewritten, the agent still does not reach for it.

## Go/no-go before claiming an improvement

- the surface was verified to reach the model;
- two arms differ in exactly one thing, including background state;
- tasks were frozen before the change, not written to fit it;
- ground truth was precomputed, so correctness is not an opinion;
- at least two rounds, with flips treated as noise;
- transcripts were read, not just the metric table;
- the claim is scoped to what was measured — one model, one effort level, these tasks.

## Anti-patterns

- Shipping a surface change because it is obviously better.
- Editing tool descriptions without checking the model receives them.
- Measuring on a strong model, which papers over bad tool UX.
- Comparing arms that also differ in memory files, plugins, or a leftover nudge.
- Letting the agent's working directory sit next to previous results.
- Reporting a win from one round, or from a task that flipped between attempts.
- Claiming a general improvement from a single task family.
