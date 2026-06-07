# sh

`sh` is a documentation and agent-harness repository for operational knowledge.

The content model is split into two different concerns:

1. `references/` — source-of-truth material and reference catalogs.
2. domain folders such as `sysadmin/` and `analytics/` — reusable agent artifacts: skills, rules, agents, harnesses, and backlog.

For Quartz, the documentation content lives under `docs/`.

## Documentation structure

```text
docs/
├── index.md
├── references/
│   ├── index.md
│   ├── source-quality.md
│   ├── sysadmin.md
│   └── analytics.md
├── sysadmin/
│   ├── index.md
│   ├── backlog.md
│   ├── agents/
│   │   └── operator.md
│   ├── harnesses/
│   │   └── default.md
│   ├── rules/
│   │   └── command-safety.md
│   └── skills/
│       └── core-troubleshooting.md
└── analytics/
    ├── index.md
    ├── backlog.md
    ├── agents/
    │   └── product-analyst.md
    ├── harnesses/
    │   └── default.md
    ├── rules/
    │   └── evidence-discipline.md
    └── skills/
        └── core-analysis.md
```

## Design rules

- Keep `references/` mostly flat. It is a catalog, not a nested knowledge base.
- Keep domain folders organized by agent-harness artifact type: `skills`, `rules`, `agents`, `harnesses`.
- Do not mix source catalogs with executable agent behavior.
- Do not store secrets, credentials, private infrastructure dumps, customer data, or production configs.
- Treat blogs, snippets, Reddit, and LLM output as leads, not source of truth.

## CI note

Quartz builds documentation from `docs/`. If CI pulls Quartz from the private `AnatoliBu/quartz` repository, this repository must also be private or the GitHub Actions access policy must allow the caller repository. GitHub's private Actions component access is not available to public caller repositories under the current setting.

## Status

Initial documentation structure was corrected on 2026-06-07 to match the agreed `references / sysadmin / analytics` model.
