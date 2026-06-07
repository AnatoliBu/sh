---
title: Backlog
---

# Backlog

This backlog keeps the repository honest: add small, useful skills before broad theory dumps.

## Priority 1

| Item | Why it matters | Output |
|---|---|---|
| systemd and journald troubleshooting | Most Linux service incidents start here | Skill with commands, interpretation, and rollback |
| SSH hardening and access recovery | Easy to lock yourself out | Skill with safe rollout and second-session validation |
| NGINX reverse proxy basics | Common deployment layer | Skill for listeners, upstreams, TLS, logs, reload validation |
| Disk space triage | Frequent VPS failure mode | Skill for `df`, `du`, logs, Docker, journal cleanup |
| Firewall baseline | High-risk if done blindly | Skill for UFW/nftables rules and SSH-safe changes |

## Priority 2

| Item | Why it matters | Output |
|---|---|---|
| PostgreSQL backup and restore | Backups are useless until restore is tested | Skill with `pg_dump`, `pg_restore`, verification |
| Docker Compose operations | Common for small servers and bots | Skill for logs, restart, volumes, networks, updates |
| Prometheus and Grafana basics | Observability beats guessing | Source map and starter dashboard notes |
| TLS certificates | Common production breakage | Skill for certbot/acme.sh diagnosis and renewal checks |

## Priority 3

| Item | Why it matters | Output |
|---|---|---|
| Incident report template | Prevents repeated blind fixes | Template with timeline, impact, cause, fix, follow-up |
| VPS baseline checklist | Useful for new servers | Checklist for users, SSH, firewall, updates, monitoring |
| Network packet basics | Helps with non-obvious failures | Notes for TCP, DNS, HTTP, TLS, ICMP |

## Definition of done for a skill

A skill is ready when it has:

- primary sources;
- scope and non-goals;
- read-only diagnostics;
- safe fix path;
- validation commands;
- rollback notes;
- known distro/version differences;
- at least one realistic failure scenario.
