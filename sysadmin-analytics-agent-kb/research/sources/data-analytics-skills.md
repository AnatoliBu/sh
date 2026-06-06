# Source Review: data-analytics-skills

## Claimed purpose

A collection of portable data analytics skills for LLM agents: EDA, data quality, SQL validation, metric reconciliation, cohorts, funnels, A/B tests, dashboards, and narrative generation.

## Authority level

Useful after audit.

## Strengths

- Domain decomposition is sensible.
- Covers common analytics workflows.
- Encourages reusable procedural skills instead of one giant prompt.
- Good inspiration for skill taxonomy.

## Weaknesses / caveats

- Community repository, not an official statistical or vendor reference.
- Skill text may not match your internal metric definitions.
- Cannot be trusted for statistical correctness without review.
- Needs adaptation to your semantic layer and event taxonomy.

## What can be reused

- Skill categories.
- Workflow structure.
- Output formats.
- Idea of assumptions log, metric reconciliation, query validation.

## What must not be reused blindly

- Metric formulas.
- SQL examples.
- Experiment analysis claims.
- Any business assumptions.

## Verdict

Use as a scaffold source. Rewrite every skill against internal definitions and authoritative docs before using it in an agent.
