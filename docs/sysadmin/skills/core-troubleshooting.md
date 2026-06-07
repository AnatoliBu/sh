---
title: Core Troubleshooting Skill
---

# Core Troubleshooting Skill

## Scope

First-pass Linux server troubleshooting and operational advice.

Covers:

- service state;
- process and port checks;
- logs;
- disk and memory pressure;
- basic network reachability;
- safe restart/reload decisions.

## Non-goals

This skill does not replace service-specific skills for databases, Kubernetes, cloud IAM, or security incident response.

## Primary references

- [[../../references/sysadmin|Sysadmin references]]
- local `man` pages;
- installed service documentation;
- distro documentation for package paths and defaults.

## First-pass questions

- What changed recently?
- Is the problem local, network, dependency, or application-level?
- Is SSH stable?
- Is there disk, memory, CPU, or file descriptor pressure?
- Is the service down, unhealthy, misconfigured, or unreachable from outside?

## Read-only diagnostics

```shell
hostnamectl
uptime
systemctl --failed
systemctl status <service>
journalctl -u <service> --since "1 hour ago" --no-pager
ss -tulpn
df -h
free -h
ip addr
ip route
```

## Interpretation hints

- `active (running)` means the daemon process exists; it does not prove the application works.
- `failed` means systemd saw a failed unit state; inspect logs before restarting.
- A port listening on `127.0.0.1` is not reachable externally.
- A port listening on `0.0.0.0` or `::` can still be blocked by firewall, cloud security group, or upstream routing.
- Disk full can break logs, databases, package managers, and service restarts.

## Safe action pattern

1. Save current evidence.
2. Validate configuration if the service supports it.
3. Prefer reload over restart when supported and sufficient.
4. Restart only when the failure mode requires it.
5. Validate status, logs, listener, and external behavior.

Example:

```shell
nginx -t
systemctl reload nginx
systemctl status nginx --no-pager
journalctl -u nginx --since "5 minutes ago" --no-pager
```

## Rollback pattern

Before editing configs:

```shell
cp /path/to/config /path/to/config.bak.$(date +%Y%m%d-%H%M%S)
```

After failure:

```shell
cp /path/to/config.bak.YYYYMMDD-HHMMSS /path/to/config
systemctl reload <service>
```

## Response template

1. Most likely cause.
2. Minimal read-only checks.
3. What each result means.
4. Safest fix path.
5. Validation.
6. Rollback.
