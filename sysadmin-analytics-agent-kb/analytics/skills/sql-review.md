# Skill: SQL Review

## Purpose

Review SQL for correctness, performance, reproducibility, and alignment with metric definitions.

## When to use

Use when:

- an agent generates SQL;
- an analyst edits a metric query;
- a dashboard query is changed;
- a warehouse cost/performance issue is suspected;
- a metric discrepancy is being investigated.

## Required context

- Business question.
- Official metric definition.
- Target warehouse dialect.
- Table schemas and certified datasets.
- Expected grain.
- Date range and timezone.
- Row-level access constraints.

## Authority chain

1. Internal semantic layer / certified model.
2. Metric catalog.
3. Warehouse official docs.
4. Internal SQL style guide.
5. Community examples only as syntax inspiration.

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
- Avoids unnecessary `SELECT *`.
- Joins use appropriate keys.
- Aggregations happen at the right level.
- Query cost is estimated when possible.

### Reproducibility

- Query uses stable sources.
- Parameters are documented.
- Assumptions are listed.
- Results can be rerun.

## Forbidden actions

- Running write queries: INSERT, UPDATE, DELETE, MERGE, TRUNCATE, DROP, CREATE in production.
- Querying raw PII unless explicitly required and approved.
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
