---
artifact_type: reference
authority_tier: Tier B
status: useful-after-audit
source_type: research-repo
topics:
  - browser-automation
  - evaluation
  - benchmark
  - browser-agents
domains:
  - browser-automation
owner: ServiceNow Research
last_checked: 2026-09-16
source_url: https://github.com/ServiceNow/BrowserGym
---

# Reference: BrowserGym

## Authority tier

Tier B

## Status

useful-after-audit

## Owner / maintainer

ServiceNow Research

## URL

https://github.com/ServiceNow/BrowserGym

## Last checked

2026-09-16

## Scope

Extensible browser-agent research environment integrating multiple web-task benchmarks, including
WebArena, WebArena-Verified, VisualWebArena, WorkArena and others.

## Why trusted

Maintained open research framework from ServiceNow Research and useful as a reproducible benchmark
harness reference.

## Caveats

Benchmark tasks are proxies for production reliability. They do not reproduce merchant fraud/risk
systems, real user identity, payment authentication or the exact operational distribution of this
project.

## Extracted rules

- Keep provider/model evaluation reproducible and task-versioned.
- Separate benchmark framework from production acceptance tests.
- Reuse benchmark methodology, not benchmark score, as proof of merchant-flow reliability.

## Do not use this source for

Predicting success rates on production payment or authenticated SaaS workflows.

## Related references

- [WebArena-Verified](./webarena-verified.md)
