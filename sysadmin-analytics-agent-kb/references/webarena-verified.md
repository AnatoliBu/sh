---
artifact_type: reference
authority_tier: Tier B
status: useful-after-audit
source_type: research-repo
topics:
  - browser-automation
  - evaluation
  - deterministic-eval
  - browser-agents
domains:
  - browser-automation
owner: ServiceNow Research
last_checked: 2026-09-16
source_url: https://github.com/ServiceNow/webarena-verified
---

# Reference: WebArena-Verified

## Authority tier

Tier B

## Status

useful-after-audit

## Owner / maintainer

ServiceNow Research

## URL

https://github.com/ServiceNow/webarena-verified

## Last checked

2026-09-16

## Scope

Curated WebArena task dataset with reviewed tasks and deterministic evaluators, including offline
network-trace replay and a cost-conscious hard subset.

## Why trusted

Maintained benchmark project focused specifically on correcting evaluator/task quality and improving
reproducibility.

## Caveats

A benchmark can compare agents under its task distribution but cannot prove correctness or safety on
unseen production sites.

## Extracted rules

- Prefer deterministic evaluators and precomputed ground truth over LLM-as-judge when the task admits
  objective verification.
- Freeze task/data versions before provider or model comparisons.
- Preserve traces so failed runs can be evaluated and debugged offline.
- Build a project-specific merchant scenario suite beside generic web-agent benchmarks.

## Do not use this source for

Replacing real end-to-end acceptance tests against supported merchants.

## Related references

- [BrowserGym](./browsergym.md)
