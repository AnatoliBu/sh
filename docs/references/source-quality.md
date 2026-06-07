---
title: Source Quality
---

# Source Quality

Use this document to decide whether a source can be promoted into rules, skills, or agents.

## Authority tiers

### Tier 0 — standards and upstream manuals

Use for protocol behavior, implementation semantics, and canonical command behavior.

Examples:

- RFC Editor
- IETF Datatracker
- Linux Kernel Documentation
- Linux man-pages project
- upstream project manuals

### Tier 1 — official project, vendor, or distribution documentation

Use for supported configuration, version-specific behavior, and operational procedures.

Examples:

- Debian documentation
- Ubuntu Server documentation
- Red Hat Enterprise Linux documentation
- PostgreSQL documentation
- NGINX documentation
- Kubernetes documentation
- Docker documentation

### Tier 2 — secondary references

Use only as examples, context, or leads.

Examples:

- ArchWiki
- DigitalOcean tutorials
- CIS Benchmarks
- NVD
- high-quality engineering blogs

## Reject or downgrade when

- There is no version or date for version-sensitive behavior.
- Commands are copied without validation or rollback.
- The source uses `curl | bash`, blanket `chmod 777`, disabling firewall, or deleting state as normal practice.
- One distro's behavior is presented as universal Linux behavior.
- The source hides risk behind phrases like "just run this".
- The source does not distinguish diagnosis, mitigation, permanent fix, and rollback.

## Promotion rule

Before a reference becomes a domain artifact, capture:

- source URL;
- version or date;
- claim extracted from the source;
- scope of the claim;
- known exceptions;
- validation command or test, when possible.
