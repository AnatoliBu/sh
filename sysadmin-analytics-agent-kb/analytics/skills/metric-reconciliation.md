---
artifact_type: skill
authority_tier: Tier A
status: foundation
domain: analytics
owner: Agent KB
last_checked: 2026-06-06
---

# Skill: Metric Reconciliation

## Purpose

Verify that the same business metric is defined and computed consistently across warehouse queries, BI dashboards, product analytics tools, and reports.

## Reference links

Authority references:

- [Internal Metric Catalog](../../references/analytics/internal-metric-catalog.md)
- [Internal Event Taxonomy](../../references/analytics/internal-event-taxonomy.md)

## When to use

Use when dashboards disagree, a new metric is introduced, a stakeholder challenges a number, or a migration changes tables, events, or semantic models.

## Required context

- Official metric definition.
- Metric owner.
- Grain and entity.
- Timezone and calendar logic.
- Filters and exclusions.
- SQL or semantic layer expression.
- BI dashboard query or model.
- Product analytics chart definition.

## Authority chain

1. [Internal metric catalog / semantic layer](../../references/analytics/internal-metric-catalog.md).
2. [Internal event taxonomy / tracking plan](../../references/analytics/internal-event-taxonomy.md).
3. Certified dbt / LookML / Cube / WrenAI models.
4. Vendor docs for tool-specific semantics.
5. Community examples only as illustration.

## Workflow

1. Locate official definition.
2. Identify all implementations.
3. Normalize time range, timezone, grain, and filters.
4. Run comparable read-only queries.
5. Diff results by period and segment.
6. Identify divergence source.
7. Recommend canonical implementation.
8. Create follow-up tasks for owners.

## Common divergence causes

- Timezone mismatch.
- Inclusive vs exclusive date boundary.
- Different identity stitching.
- Missing exclusion filters.
- Event name renamed without backfill.
- One source uses created_at, another uses occurred_at.
- Late-arriving events.
- Refund or cancellation handling differs.

## Output format

```markdown
# Metric Reconciliation Report

## Metric

## Official definition

## Implementations reviewed

## Comparison table

## Differences found

## Root cause

## Recommended canonical logic

## Required owner decisions

## Assumptions / unknowns
```
