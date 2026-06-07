# sh

`sh` is a documentation and agent-harness repository for operational knowledge.

The active knowledge base lives in `sysadmin-analytics-agent-kb/`.

## Active structure

```text
sysadmin-analytics-agent-kb/
├── references/
│   ├── README.md
│   ├── TEMPLATE.md
│   ├── google-sre-incident-management.md
│   ├── internal-event-taxonomy.md
│   ├── internal-metric-catalog.md
│   ├── kubernetes-pod-security-standards.md
│   └── ...
├── sysadmin/
│   ├── agent.md
│   ├── sources.md
│   └── skills/
├── analytics/
│   ├── agent.md
│   ├── sources.md
│   └── skills/
├── shared/
│   └── rules/
├── tools/
├── ci-reports/
└── roadmap.md
```

## Design rules

- Keep `references/` mostly flat. It is a catalog of source-of-truth cards, not a deeply nested knowledge base.
- Keep domain folders organized by agent-harness concern: agent definitions, sources, skills, rules, workflows, evals.
- Do not mix source catalogs with executable agent behavior.
- Do not store secrets, credentials, private infrastructure dumps, customer data, or production configs.
- Treat blogs, snippets, Reddit, and LLM output as leads, not source of truth.

## CI

The CI entry point is `.github/workflows/test.yml`.

It runs `sysadmin-analytics-agent-kb/tools/run_agent_kb_ci.py`, which validates:

- domain package structure;
- wiki links;
- frontmatter;
- agent artifact references;
- curated link graph;
- Quartz site build;
- markdown lint.

Quartz is cloned from `AnatoliBu/quartz`. If `QUARTZ_REPO_TOKEN` or `GITHUB_TOKEN` is available, CI uses token-based clone. If the Quartz repository is public and no token is available, the build script falls back to a plain public clone URL.

## Status

On 2026-06-07 the repository was corrected back to the agreed model: first-level `references`, `sysadmin`, and `analytics` inside `sysadmin-analytics-agent-kb/`, with references kept mostly flat and agent domains holding skills/rules/agents/harness-style artifacts.
