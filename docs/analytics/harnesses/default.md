---
title: Default Analytics Harness
---

# Default Analytics Harness

## Purpose

Default harness for combining analytics references, rules, skills, and agent behavior.

## Load order

1. [[../../references/source-quality|Source quality]]
2. [[../../references/analytics|Analytics references]]
3. [[../rules/evidence-discipline|Evidence discipline rules]]
4. [[../skills/core-analysis|Core analysis skill]]
5. [[../agents/product-analyst|Product analyst agent]]

## Checklist

- Identify the decision supported by the analysis.
- Define metric, entity, grain, and time window.
- Make filters and exclusions explicit.
- Check source freshness and transformation logic.
- Separate observation, interpretation, recommendation, and limitation.
- Extract reusable knowledge into `skills` or `rules`, not into `references`.

## Response sections

Use these sections when helpful:

- Business question
- Metric definition
- Data needed
- Method
- Validation checks
- Result interpretation
- Limitations
- Follow-up artifact candidate
