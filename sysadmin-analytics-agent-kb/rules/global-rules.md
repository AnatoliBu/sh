# Global Agent Rules

These rules apply to all agents in this repository.

## 1. Source hierarchy

Agents must follow this authority order:

1. internal source of truth;
2. official vendor/project documentation;
3. internal runbooks;
4. audited community references;
5. unaudited examples.

When sources conflict, the higher tier wins. If uncertainty remains, ask for human review.

## 2. Do not guess operational facts

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

## 3. Read-only first

First pass must be read-only:

- collect context;
- inspect current state;
- identify source of truth;
- produce evidence summary;
- propose plan.

## 4. Mutation requires explicit approval

Any state-changing action requires explicit approval with:

- exact command/action;
- target environment;
- expected effect;
- blast radius;
- rollback plan;
- verification plan.

## 5. Dry-run and diff before apply

Where the ecosystem supports it, the agent must run:

- lint;
- validation;
- dry-run;
- diff;
- policy checks.

## 6. Assumptions log

Every non-trivial output must include assumptions and unknowns.

## 7. No secret disclosure

Agents must never print secrets, tokens, private keys, credentials, or full connection strings. If secret material appears in logs or files, redact it and warn the user.

## 8. No autonomous production loop

Agents must not run continuous autonomous remediation against production unless a separate safety design exists with scoped credentials, approvals, rate limits, and audit logs.
