---
title: Evidence Discipline Rules
---

# Evidence Discipline Rules

## Default behavior

Do not treat a chart, SQL result, dashboard, or model output as sufficient evidence until the metric definition and data grain are clear.

## Required distinctions

Always separate:

- observation;
- interpretation;
- hypothesis;
- decision recommendation;
- confidence level;
- limitation.

## Metric hygiene

A metric definition should include:

- name;
- purpose;
- numerator;
- denominator;
- entity;
- grain;
- time window;
- filters;
- owner;
- known caveats.

## Query hygiene

Before trusting a query result, check:

- joins do not multiply rows unexpectedly;
- filters match the business question;
- time zones are explicit;
- null handling is intentional;
- sampling is understood;
- test/internal data is handled.

## Claims to avoid

Avoid claims like:

- "conversion improved" without baseline, window, and denominator;
- "users churned" without churn definition;
- "experiment won" without confidence, guardrails, and sample details;
- "dashboard is wrong" without checking source, freshness, and transformation logic.
