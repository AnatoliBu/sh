---
artifact_type: skill
authority_tier: Tier A
status: foundation
domain: analytics
owner: Agent KB
last_checked: 2026-06-06
---

# Skill: SQL Review

## Purpose

Review SQL for correctness, reproducibility, cost, and alignment with metric definitions.

## Reference links

Authority references:

- [Internal Metric Catalog](../../references/internal-metric-catalog.md)
- [Internal Event Taxonomy](../../references/internal-event-taxonomy.md)

## When to use

Use when a query is created or changed, a dashboard number is challenged, cost is suspected, or a metric discrepancy is being investigated.

## Required context

- Business question.
- Official metric definition.
- Target warehouse dialect.
- Table schemas and certified datasets.
- Expected grain.
- Date range and timezone.
- Access constraints.

## Authority chain

1. Internal semantic layer / certified model.
2. [Metric catalog](../../references/internal-metric-catalog.md).
3. [Event taxonomy](../../references/internal-event-taxonomy.md).
4. Warehouse official docs.
5. Internal SQL style guide.

## Review checklist

### Correctness

- Query answers the stated question.
- Grain is explicit and preserved.
- Joins do not create fanout.
- Filters match metric definition.
- Timezone and date boundaries are explicit.
- Null handling is intentional.
- Deduplication logic is explicit.

### Performance

- Partition filters present.
- Avoids unnecessary wide reads.
- Joins use appropriate keys.
- Aggregations happen at the right level.
- Query cost is estimated when possible.

### Reproducibility

- Query uses stable sources.
- Parameters are documented.
- Assumptions are listed.
- Results can be rerun.

## Output format

```markdown
# SQL Review

## Verdict
approve / request changes / reject

## Correctness findings

## Performance findings

## Governance findings

## Suggested rewrite

## Assumptions
```
