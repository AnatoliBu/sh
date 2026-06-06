---
artifact_type: reference
authority_tier: Tier A
status: foundation
domain: analytics
owner: Internal product analytics / data platform / instrumentation owners
last_checked: TODO
source_url: TODO
---

# Reference: Internal Event Taxonomy

## Authority tier

Tier A

## Status

foundation / internal-placeholder

## Owner / maintainer

Internal product analytics / data platform / instrumentation owners.

## URL

TODO: link to internal tracking plan, event taxonomy, Segment/Amplitude/Mixpanel/PostHog tracking spec, or data contract registry.

## Last checked

TODO

## Scope

Highest authority for event names, event properties, identity stitching, session rules, product surfaces, and instrumentation caveats.

## Why trusted

Product analytics depends on precise event semantics. Generic event names are not enough; the agent must use the approved tracking plan.

## Caveats

This is a placeholder until connected to the real event taxonomy.

## Skills that may consume this reference

- [Funnel Analysis](../../analytics/skills/funnel-analysis.md)
- [Metric Reconciliation](../../analytics/skills/metric-reconciliation.md)
- [SQL Review](../../analytics/skills/sql-review.md)
- future: cohort-analysis
- future: retention-analysis
- future: instrumentation-review

## Agents that may consume this reference

- [Data / Product Analytics Assistant](../../agents/analytics-agent.md)

## Extracted rules

- Do not infer event meaning from event name alone.
- Every funnel step must map to an official event/property definition.
- Identity model must be explicit.
- Instrumentation breaks must be checked before interpreting product behavior.

## Do not use this source for

- Business KPI ownership unless it also includes metric catalog entries.
- Statistical methodology.
- Warehouse performance guidance.

## Related references

- [Internal Metric Catalog](./internal-metric-catalog.md)

## Notes

Every product analytics skill should link here when it uses product events.
