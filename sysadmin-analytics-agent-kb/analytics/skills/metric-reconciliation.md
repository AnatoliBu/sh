# Skill: Metric Reconciliation

## Purpose

Verify that the same business metric is defined and computed consistently across warehouse queries, BI dashboards, product analytics tools, and reports.

## When to use

Use when:

- dashboards disagree;
- a new metric is introduced;
- a stakeholder challenges a number;
- a product/analytics agent prepares an executive summary;
- a migration changes tables, events, or semantic models.

## Required context

- Official metric definition.
- Metric owner.
- Grain and entity: user, account, session, order, event, etc.
- Timezone and calendar logic.
- Filters and exclusions.
- Warehouse SQL / semantic layer expression.
- BI dashboard query or model.
- Product analytics chart definition.

## Authority chain

1. Internal metric catalog / semantic layer.
2. Internal event taxonomy / tracking plan.
3. Certified dbt/LookML/Cube/WrenAI models.
4. Vendor docs for tool-specific semantics.
5. Community examples only as illustration.

## Allowed read-only actions

- Read metric definitions.
- Read SQL and BI semantic model definitions.
- Query warehouse in read-only mode.
- Export sampled aggregates.
- Compare counts by day/week/month.

## Forbidden actions

- Mutating warehouse data.
- Changing dashboards without owner approval.
- Publishing reconciled numbers without assumptions log.
- Inferring business definitions from column names alone.

## Workflow

1. Locate official definition.
2. Identify all implementations.
3. Normalize time range, timezone, grain, and filters.
4. Run comparable queries.
5. Diff results by period and segment.
6. Identify divergence source.
7. Recommend canonical implementation.
8. Create follow-up tasks for owners.

## Common divergence causes

- Timezone mismatch.
- Inclusive vs exclusive date boundary.
- Different identity stitching.
- Missing bot/test/internal-user filters.
- Event name renamed without backfill.
- One source uses created_at, another uses occurred_at.
- Late-arriving events.
- Refund/cancellation handling differs.

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
