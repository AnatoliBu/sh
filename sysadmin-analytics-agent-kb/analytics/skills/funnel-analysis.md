---
artifact_type: skill
authority_tier: Tier A
status: foundation
domain: analytics
owner: Agent KB
last_checked: 2026-06-06
---

# Skill: Funnel Analysis

## Purpose

Analyze conversion through a product funnel while respecting the official event taxonomy, identity model, and metric definitions.

## Reference links

Authority references:

- [Internal Event Taxonomy](../../references/analytics/internal-event-taxonomy.md)
- [Internal Metric Catalog](../../references/analytics/internal-metric-catalog.md)

## When to use

Use when conversion drops, onboarding or activation flows are investigated, a stakeholder asks where users fall out, or product analytics charts need validation against warehouse data.

## Required context

- Funnel goal.
- Ordered funnel steps.
- Official event names and properties.
- Identity rules.
- Conversion window.
- Timezone.
- Segmentation dimensions.
- Exclusion rules.

## Authority chain

1. [Internal tracking plan / event taxonomy](../../references/analytics/internal-event-taxonomy.md).
2. [Internal metric catalog](../../references/analytics/internal-metric-catalog.md).
3. Certified warehouse or semantic model.
4. Product analytics vendor docs for funnel semantics.
5. External blog/framework examples only as inspiration.

## Allowed read-only actions

- Read tracking plan.
- Read event schemas.
- Run read-only aggregate queries.
- Compare vendor funnel with warehouse reconstruction.
- Produce charts and tables.

## Forbidden actions

- Changing tracking definitions without owner approval.
- Calling correlation a cause.
- Combining incompatible identity grains.
- Hiding exclusions or assumptions.

## Workflow

1. Confirm funnel question and business decision it supports.
2. Map each step to exact event/property definition.
3. Confirm conversion window and user grain.
4. Compute baseline funnel.
5. Segment by relevant dimensions.
6. Compare current period to previous period.
7. Identify the biggest absolute and relative drop-off changes.
8. List hypotheses and follow-up checks.
9. Produce recommendation with confidence level.

## Validation steps

- Verify every funnel step exists in event taxonomy.
- Check event volume for instrumentation breaks.
- Compare warehouse counts with product analytics tool counts.
- Check identity stitching changes.
- Check release calendar around metric shift.

## Output format

```markdown
# Funnel Analysis

## Question

## Funnel definition

## Data sources

## Baseline conversion

## Segment findings

## Largest drop-offs

## Hypotheses

## Validation checks

## Recommendations

## Assumptions / unknowns
```
