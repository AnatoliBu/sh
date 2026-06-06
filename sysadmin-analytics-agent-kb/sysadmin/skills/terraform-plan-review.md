---
artifact_type: skill
authority_tier: Tier A
status: foundation
domain: sysadmin
owner: Agent KB
last_checked: 2026-06-06
---

# Skill: Terraform Plan Review

## Purpose

Review Terraform changes, explain blast radius, and ensure validation/policy checks pass.

## Reference links

Authority references:

- [Terraform MCP Server](../../references/terraform-mcp.md)

## When to use

Use when Terraform code is generated or edited, a plan is created, drift is suspected, or infrastructure changes need human-readable review.

## Required context

- Terraform plan output.
- Target workspace/environment.
- Module path.
- Provider versions.
- Relevant policies.
- Expected owner and service.

## Authority chain

1. Internal IaC standards.
2. Terraform state and plan output.
3. [Terraform MCP Server](../../references/terraform-mcp.md) for current docs context.
4. Provider official docs.
5. Policy-as-code rules.

## Review checklist

- Identify creates, updates, replacements, and destroys.
- Flag high-risk resources.
- Check provider and module versions.
- Check security-sensitive changes.
- Confirm tags/labels/ownership.
- Confirm rollback or recovery path.
- Confirm required approval.

## Output format

```markdown
# Terraform Plan Review

## Verdict
approve / request changes / reject

## Summary

## Blast radius

## High-risk changes

## Policy findings

## Required approvals

## Rollback / recovery

## Assumptions
```
