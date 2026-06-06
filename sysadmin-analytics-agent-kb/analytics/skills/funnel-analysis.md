# Skill: Funnel Analysis

## Purpose

Analyze conversion through a product funnel while respecting the official event taxonomy, identity model, and metric definitions.

## When to use

Use when:

- conversion drops;
- onboarding, checkout, signup, activation, or retention flows are investigated;
- a stakeholder asks where users fall out;
- an experiment changes product flow;
- product analytics charts need validation against warehouse data.

## Required context

- Funnel goal.
- Ordered funnel steps.
- Official event names and properties.
- Identity rules: anonymous id, user id, account id, session id.
- Conversion window.
- Timezone.
- Segmentation dimensions.
- Exclusion rules: test users, bots, employees, refunds, spam.

## Authority chain

1. Internal tracking plan / event taxonomy.
2. Internal metric catalog.
3. Certified warehouse or semantic model.
4. Product analytics vendor docs for funnel semantics.
5. External blog/framework examples only as inspiration.

## Allowed read-only actions

- Read tracking plan.
- Read event schemas.
- Run read-only aggregate queries.
- Compare vendor funnel with warehouse reconstruction.
- Produce charts/tables.

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
5. Segment by channel, platform, country, cohort, version, experiment group.
6. Compare current period to previous period.
7. Identify the biggest absolute and relative drop-off changes.
8. List hypotheses and follow-up checks.
9. Produce recommendation with confidence level.

## Validation steps

- Verify every funnel step exists in event taxonomy.
- Check event volume for instrumentation breaks.
- Compare warehouse counts with product analytics tool counts.
- Check identity stitching changes.
- Check deploy/release calendar around metric shift.

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
