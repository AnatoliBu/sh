# Analytics / Product Analytics Sources

This file ranks source-of-truth references for analytics agents.

## Tier A — foundation sources

### Internal metric catalog / semantic layer

This is the highest authority. It should include:

- metric name;
- business definition;
- SQL / semantic model definition;
- owner;
- grain;
- timezone;
- filters;
- freshness expectations;
- known caveats;
- dashboard references;
- validation tests.

Operational rule: if internal definitions disagree with vendor/blog examples, internal definitions win.

### Internal event taxonomy

This defines product analytics events, properties, identity stitching, session logic, and instrumentation contracts.

Operational rule: agent must not infer event meaning from names alone. It must read event definitions and known caveats.

### Data warehouse / semantic layer docs

Use BigQuery, Snowflake, Databricks, dbt, LookML, Cube, WrenAI, or other semantic layer documentation depending on the actual stack.

Operational rule: the agent should prefer semantic models and certified datasets over raw table spelunking.

### Product analytics vendor documentation

Use Amplitude, Mixpanel, PostHog, GA4 docs for platform-specific concepts:

- funnels;
- cohorts;
- retention;
- user identity;
- experiments;
- dashboards;
- event tracking.

Operational rule: vendor docs explain tool semantics, but not the business definition of your metric.

### Statistical references

Use established statistics and experimentation references for:

- hypothesis testing;
- confidence intervals;
- power analysis;
- multiple testing;
- causal inference;
- experiment guardrails.

Operational rule: agent must explicitly state assumptions and avoid causal claims from observational data unless causal design supports them.

## Tier B — useful after audit

- data-analytics-skills: useful workflow taxonomy for EDA, metric reconciliation, SQL review, cohort/funnel analysis, documentation, narrative generation.
- AI Analyst style repos: useful architecture ideas, not trusted analytical truth.
- product analytics skills from community repos: useful patterns, must be rewritten against internal metrics and event taxonomy.

## Tier C — snippets only

- SQL gists;
- dashboard examples;
- blog recipes;
- growth-hacking frameworks.

Use as examples only. Never treat as authoritative.

## Tier D — reject as foundation

- autonomous analytics agents without explicit evaluation;
- repos that generate SQL without semantic layer or query validation;
- projects that skip metric ownership and assumption logs.

## Source admission checklist

Every analytics source entry should include:

- owner;
- authority tier;
- URL or internal location;
- scope;
- what metrics/skills can use it;
- caveats;
- last checked date;
- whether it is normative or illustrative.
