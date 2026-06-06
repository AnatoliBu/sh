# Bullshit Check Mode

Use this mode when evaluating an external repo, skill pack, agent framework, MCP server, or documentation source.

## Goal

Prevent weak repositories, demos, hype, and unaudited agent frameworks from entering the trusted base.

## Checks

### 1. Provenance

- Who maintains it?
- Is it official, vendor-owned, community-owned, or anonymous?
- Is there a real maintainer track record?
- Is the project tied to a known organization?

### 2. Maintenance

- Recent commits?
- Releases?
- Open issues?
- Closed issues?
- PR activity?
- Security policy?
- CI status?

### 3. Scope realism

Red flags:

- claims to automate everything;
- huge integration lists without tests;
- one-liner install for dangerous workflows;
- “autonomous” infra changes;
- no clear threat model;
- no rollback model.

### 4. Code and docs alignment

- Does the README match actual code?
- Are examples executable?
- Are permissions documented?
- Are error cases handled?
- Are tests present?

### 5. Blast radius

- What systems can it reach?
- Can it mutate prod?
- Can it access secrets?
- Can it run host commands?
- Can untrusted messages trigger actions?

### 6. Guardrails

- Read-only mode?
- Approval gates?
- Dry-run?
- Audit log?
- Rollback?
- Scoped credentials?
- Denylist/allowlist?

### 7. Supply chain risk

- Dependencies pinned?
- GitHub actions pinned by SHA?
- Install scripts audited?
- MCP tools authenticated?
- Skills downloaded from trusted source?

## Verdict levels

- **Foundation:** official/authoritative; can anchor skills.
- **Useful after audit:** can inspire structure but must be reviewed.
- **Cheat sheet only:** command/reference hints.
- **Moodboard only:** feature taxonomy; do not run.
- **Reject:** unsafe, misleading, or low-quality.

## Required output

```markdown
# Bullshit Check Report

## Source

## Claimed purpose

## Authority level

## Evidence

## Red flags

## What can be reused

## What must not be reused

## Verdict
```
