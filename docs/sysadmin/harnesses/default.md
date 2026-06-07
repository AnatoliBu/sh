---
title: Default Sysadmin Harness
---

# Default Sysadmin Harness

## Purpose

Default harness for combining sysadmin references, rules, skills, and agent behavior.

## Load order

1. [[../../references/source-quality|Source quality]]
2. [[../../references/sysadmin|Sysadmin references]]
3. [[../rules/command-safety|Command safety rules]]
4. [[../skills/core-troubleshooting|Core troubleshooting skill]]
5. [[../agents/operator|Sysadmin operator agent]]

## Checklist

- Classify the request as diagnosis, configuration, deployment, recovery, hardening, or review.
- Gather only the missing system facts that affect the answer.
- Prefer read-only checks before changes.
- For changes, include validation and rollback.
- After resolution, extract reusable knowledge into `skills` or `rules`, not into `references`.

## Response sections

Use these sections when helpful:

- Situation
- Evidence needed
- Read-only checks
- Interpretation
- Safe action
- Validation
- Rollback
- Follow-up artifact candidate
