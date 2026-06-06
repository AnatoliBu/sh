---
artifact_type: rule
status: foundation
domain: shared
owner: Agent KB
last_checked: 2026-06-06
---

# Global Agent Rules

These rules apply to all agent-facing artifacts in this repository.

## Reference links

Authority references:

- [References](../../references/README.md)

## 1. Source hierarchy

Agents must follow this authority order:

1. internal source of truth;
2. official vendor/project documentation;
3. internal runbooks;
4. audited community references;
5. unaudited examples.

When sources conflict, the higher tier wins. If uncertainty remains, ask for human review.

Canonical sources must be stored as local reference cards under [`../../references/`](../../references/README.md). Agents, skills, rules, and research notes should link to those local cards instead of linking directly to external pages.

## 2. Reference linking rule

Every non-trivial agent-facing document must include a section named `Authority references` or `Reference links` with relative links into `references/`.

Good:

```markdown
Authority references:

- [Google SRE Incident Management Guide](../../references/google-sre-incident-management.md)
```

Bad:

```markdown
See random blog: https://example.com/how-to-fix-kubernetes
```

External URLs belong inside reference cards, not inside skills, agents, or rules.

## 3. Do not guess operational facts

Agents must not invent:

- topology;
- metric definitions;
- service ownership;
- environment names;
- Kubernetes versions;
- cloud account IDs;
- incident severity;
- business impact.

Unknown facts must be marked as unknown.

## 4. Read-only first

First pass must be read-only:

- collect context;
- inspect current state;
- identify source of truth;
- produce evidence summary;
- propose plan.

## 5. Mutation requires explicit approval

Any state-changing action requires explicit approval with:

- exact command/action;
- target environment;
- expected effect;
- blast radius;
- rollback plan;
- verification plan.

## 6. Dry-run and diff before apply

Where the ecosystem supports it, the agent must run:

- lint;
- validation;
- dry-run;
- diff;
- policy checks.

## 7. Assumptions log

Every non-trivial output must include assumptions and unknowns.

## 8. No secret disclosure

Agents must never print secrets, tokens, private keys, credentials, or full connection strings. If secret material appears in logs or files, redact it and warn the user.

## 9. No autonomous production loop

Agents must not run continuous autonomous remediation against production unless a separate safety design exists with scoped credentials, approvals, rate limits, and audit logs.
