# Skill: SQL Review

## Purpose

Review SQL for correctness, performance, reproducibility, and alignment with metric definitions.

## Reference links

Authority references:

- [Internal Metric Catalog](../../references/analytics/internal-metric-catalog.md)
- [Internal Event Taxonomy](../../references/analytics/internal-event-taxonomy.md)

## When to use

Use when an agent generates SQL, a metric query changes, a dashboard query changes, cost/performance is suspected, or a metric discrepancy is being investigated.

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
2. [Metric catalog](../../references/analytics/internal-metric-catalog.md).
3. [Event taxonomy](../../references/analytics/internal-event-taxonomy.md).
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

## Forbidden actions

- Running write queries in production.
- Querying sensitive fields unless explicitly required and approved.
- Publishing results without assumptions.

## Output format

```markdown
# SQL Review

## Verdict
approve / request changes / reject

## Correctness findings

## Performance findings

## Data governance findings

## Suggested rewrite

## Assumptions
```
