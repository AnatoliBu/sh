---
title: Sysadmin Backlog
---

# Sysadmin Backlog

## Priority 1

| Item | Output |
|---|---|
| systemd and journald troubleshooting | Skill with commands, interpretation, validation, rollback. |
| SSH hardening and access recovery | Skill with second-session validation and lockout prevention. |
| NGINX reverse proxy basics | Skill for listeners, upstreams, TLS, logs, reload validation. |
| Disk space triage | Skill for `df`, `du`, logs, Docker, journal cleanup. |
| Firewall baseline | Skill for UFW/nftables and SSH-safe changes. |

## Priority 2

| Item | Output |
|---|---|
| PostgreSQL backup and restore | Skill with dump, restore, verification. |
| Docker Compose operations | Skill for logs, restart, volumes, networks, updates. |
| TLS certificates | Skill for renewal checks and failure triage. |
| Observability baseline | Prometheus/Grafana starter rules and dashboards. |

## Definition of done

A sysadmin artifact is ready when it has:

- primary references;
- scope and non-goals;
- read-only diagnostics;
- safe fix path;
- validation commands;
- rollback notes;
- known distro/version differences;
- at least one realistic failure scenario.
