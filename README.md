# sh

`sh` is a compact sysadmin / infrastructure handbook for agent-assisted work.

The goal is not to collect random tutorials. The goal is to keep a **source-of-truth map**, practical agent rules, and small reusable skills for Linux, networking, services, security, observability, and incident response.

## Current scope

This repository is for:

- Linux server administration
- networking and protocol basics
- SSH, systemd, logs, packages, firewalls
- web/service operations such as NGINX and PostgreSQL
- safe troubleshooting workflows
- agent rules for checking claims before acting

This repository is **not** for secrets, private infrastructure dumps, customer data, credentials, production configs, or one-off notes that cannot be generalized.

## Structure

```text
.
├── README.md
├── docs/
│   ├── agent-rules.md
│   ├── source-of-truth.md
│   └── backlog.md
├── skills/
│   └── sysadmin-core.md
└── sources/
    └── sysadmin.yml
```

## Operating principle

Use this order when building or reviewing material:

1. Protocol specs and upstream manuals.
2. Official vendor/project documentation.
3. Distribution documentation for distro-specific behavior.
4. High-quality community references only as secondary context.
5. Blogs, LLM output, Reddit, snippets, and Stack Overflow are leads, not source of truth.

If sources disagree, prefer the source closest to the implementation or standard, and record the disagreement instead of smoothing it over.

## Agent workflow

When an agent uses this repo:

1. Identify the domain: Linux, network, service, database, observability, security, or incident triage.
2. Open `docs/source-of-truth.md` and choose sources by authority tier.
3. Apply `docs/agent-rules.md` before suggesting commands.
4. Use the relevant skill file as the response/checklist shape.
5. For dangerous operations, produce a plan, validation command, backup/rollback path, and explicit assumptions.

## Status

Initial scaffold created on 2026-06-07. The repository previously contained only the MIT license. The next useful step is to fill the first real skill: `systemd + journald troubleshooting` or `SSH hardening and access recovery`.
