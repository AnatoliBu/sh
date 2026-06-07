# References

This directory stores authoritative source-of-truth references used by every rule, skill, agent, and research note in this knowledge base.

## Rule

Every document that relies on external or internal authority must link to one or more reference cards from this directory.

Do not link directly to random blog posts from skills. Skills should link to local reference cards. Reference cards may link to official documentation, standards, vendor docs, internal docs, or audited community sources.

## Layout

Keep reference cards almost flat:

```text
references/
├── README.md
├── TEMPLATE.md
├── google-sre-incident-management.md
├── internal-metric-catalog.md
├── internal-event-taxonomy.md
├── kubernetes-pod-security-standards.md
└── terraform-mcp.md
```

Do not add domain subfolders such as `references/sysadmin/` or `references/analytics/` unless the CI structure rules are explicitly changed.

## Why

This keeps authority centralized:

- one place to rank source trust;
- one place to update URLs;
- one place to capture caveats;
- one place to mark source status: foundation, useful after audit, cheat sheet, moodboard, rejected;
- one place to prevent low-quality repos from quietly becoming trusted.

## Link format

Prefer relative links:

```markdown
See [Google SRE Incident Management Guide](./google-sre-incident-management.md).
```

From a skill file, link back to references like this:

```markdown
Authority references:

- [Google SRE Incident Management Guide](../../references/google-sre-incident-management.md)
- [Kubernetes Pod Security Standards](../../references/kubernetes-pod-security-standards.md)
```

## Reference tiers

- **Tier A — Foundation:** official docs, standards, mature project docs, internal source of truth.
- **Tier B — Useful after audit:** community sources with useful structure but not authoritative.
- **Tier C — Cheat sheet only:** snippets and command lists.
- **Tier D — Moodboard / rejected:** do not use as implementation or runtime foundation.

## Required fields for every reference card

Use [`TEMPLATE.md`](./TEMPLATE.md).
