# Source of truth map

Last reviewed: 2026-06-07

This file defines which sources are allowed to act as ground truth for sysadmin, networking, and infrastructure skills.

## Authority tiers

### Tier 0 — standards and upstream manuals

Use these when the question is about protocol behavior, Linux kernel behavior, POSIX-ish command behavior, or implementation-level semantics.

| Area | Source | URL | Use for |
|---|---|---|---|
| Internet standards | RFC Editor | https://www.rfc-editor.org/ | Published RFCs, protocol behavior, terminology |
| IETF drafts and WGs | IETF Datatracker | https://datatracker.ietf.org/ | Active drafts, status of proposed standards |
| Linux kernel | Linux Kernel Documentation | https://docs.kernel.org/ | Kernel features, networking stack, cgroups, filesystems, admin guide |
| Linux user-space manual pages | Linux man-pages project | https://man7.org/linux/man-pages/ | Syscalls, libc, procfs, capabilities, common Linux manual pages |
| systemd | systemd project docs | https://systemd.io/ | systemd concepts, boot, units, journald, networkd, resolved |
| OpenSSH | OpenSSH manual pages | https://www.openssh.com/manual.html | ssh, sshd, ssh_config, sshd_config, key handling |

### Tier 1 — official project/vendor documentation

Use these for production guidance, supported configuration, version-specific behavior, and operational procedures.

| Area | Source | URL | Use for |
|---|---|---|---|
| Debian administration | Debian Administrator's Handbook | https://www.debian.org/doc/manuals/debian-handbook/ | Debian system administration, packages, services, network infrastructure |
| Ubuntu Server | Ubuntu Server docs | https://ubuntu.com/server/docs/ | Ubuntu-specific server configuration and supported workflows |
| RHEL | Red Hat Enterprise Linux docs | https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/ | RHEL networking, security, system roles, SELinux, supported admin flows |
| NGINX | NGINX docs | https://nginx.org/en/docs/ | NGINX directives, modules, request processing, TLS, proxying |
| PostgreSQL | PostgreSQL docs | https://www.postgresql.org/docs/current/ | Database administration, backups, replication, configuration |
| Kubernetes | Kubernetes docs | https://kubernetes.io/docs/ | Kubernetes architecture, kubectl, workloads, services, ops guidance |
| Docker | Docker docs | https://docs.docker.com/ | Docker engine, compose, networking, storage, security |
| Prometheus | Prometheus docs | https://prometheus.io/docs/ | Metrics model, scraping, PromQL, alerting concepts |
| Grafana | Grafana docs | https://grafana.com/docs/ | Dashboards, alerting, data sources, operational visualization |

### Tier 2 — useful secondary references

Use only as cross-checks, examples, or practical context. Do not treat as the final authority unless the topic is explicitly community-maintained and no upstream documentation exists.

| Area | Source | URL | Use for |
|---|---|---|---|
| Linux practice | ArchWiki | https://wiki.archlinux.org/ | Excellent practical notes, but verify against upstream/distro docs |
| Tutorials | DigitalOcean Community | https://www.digitalocean.com/community/tutorials | Good onboarding examples; verify commands before production use |
| Security benchmarks | CIS Benchmarks | https://www.cisecurity.org/cis-benchmarks | Hardening baseline; map to distro/version before applying |
| Vulnerabilities | NVD | https://nvd.nist.gov/ | CVE metadata; verify exploitability against vendor advisories |

## Bullshit-check rules

Reject or downgrade a source when it has any of these signs:

- No version or date for version-sensitive behavior.
- Claims that contradict upstream manuals without explaining why.
- Commands copied without validation or rollback.
- Uses `curl | bash`, disabling firewalls, or blanket `chmod 777` as normal practice.
- Treats one distro's behavior as universal Linux behavior.
- Optimizes for SEO rather than correctness.
- Does not distinguish diagnosis, mitigation, and permanent fix.
- Hides risk behind vague wording such as "just run this".

## How to resolve conflicts

1. Prefer standard/RFC over blog explanations for protocol behavior.
2. Prefer upstream project docs over distro docs for upstream semantics.
3. Prefer distro docs over upstream docs for packaging paths, defaults, service names, SELinux/AppArmor profiles, and supported workflows.
4. Prefer installed local manuals/configs over web docs when debugging a concrete machine.
5. If still unclear, state the conflict and ask for the exact distro, version, package version, and config path.

## Required metadata for every new skill

Every skill added to this repo should include:

- Scope.
- Out-of-scope.
- Primary sources.
- Assumptions.
- Safety notes.
- Diagnostic commands.
- Validation commands.
- Rollback guidance.
- Known distro/version differences.
