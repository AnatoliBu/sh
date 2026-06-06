# Reference: Internal Metric Catalog

## Authority tier

Tier A

## Status

foundation / internal-placeholder

## Owner / maintainer

Internal analytics/product/data owners.

## URL

TODO: link to internal metric catalog, semantic layer, dbt docs, LookML project, BI glossary, or approved metric registry.

## Last checked

TODO

## Scope

Highest authority for business metric definitions: metric name, owner, grain, filters, timezone, aggregation, SQL/semantic expression, caveats, and dashboards.

## Why trusted

Internal metric definitions represent the business contract used by stakeholders. They override generic product analytics examples and vendor blog definitions.

## Caveats

This card is a placeholder until the actual internal source is linked. Do not mark analytics skills as fully production-ready until this reference points to a real maintained source.

## Skills that may consume this reference

- [Metric Reconciliation](../../analytics/skills/metric-reconciliation.md)
- [SQL Review](../../analytics/skills/sql-review.md)
- [Funnel Analysis](../../analytics/skills/funnel-analysis.md)
- future: cohort-analysis
- future: retention-analysis
- future: executive-summary

## Agents that may consume this reference

- [Data / Product Analytics Assistant](../../agents/analytics-agent.md)

## Extracted rules

- Definitions before queries.
- Internal definitions beat vendor examples.
- Every metric must state grain, timezone, filters, freshness, and owner.
- Reports must include assumptions and unknowns.

## Do not use this source for

- Tool-specific funnel/cohort semantics.
- Statistical methodology.
- Infrastructure telemetry.

## Related references

- [Internal Event Taxonomy](./internal-event-taxonomy.md)
- future: dbt semantic layer
- future: Mixpanel docs
- future: Amplitude docs

## Notes

This should become the central reference for analytics skills once real internal links are added.
