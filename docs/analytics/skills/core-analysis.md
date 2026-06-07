---
title: Core Analysis Skill
---

# Core Analysis Skill

## Scope

First-pass product and data analytics work.

Covers:

- metric definition;
- event and entity modeling;
- SQL reasoning;
- funnel and retention framing;
- experiment readouts;
- evidence quality checks.

## Non-goals

This skill does not replace domain-specific finance, medical, legal, or regulated analytics review.

## Primary references

- [[../../references/analytics|Analytics references]]
- database documentation for SQL behavior;
- product analytics tool documentation for implementation details;
- experiment literature for statistical interpretation.

## Required questions

Before answering, identify:

- decision being supported;
- metric definition;
- entity and grain;
- event source;
- time window;
- filters and exclusions;
- known bias or missing data.

## Analysis shape

1. Define the business question.
2. Define the metric.
3. Define the data grain.
4. Identify required events or tables.
5. State assumptions.
6. Produce query or method.
7. Validate edge cases.
8. Explain limitations.

## Validation checks

- Does the numerator and denominator use the same grain?
- Are bots, tests, refunds, cancellations, or internal users excluded where needed?
- Does the time zone match the business reporting convention?
- Are late-arriving events possible?
- Is the metric stable enough to support the requested decision?
