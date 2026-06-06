# Skill: Terraform Plan Review

## Purpose

Review Terraform changes before apply, explain blast radius, and ensure validation/policy checks pass.

## When to use

Use when:

- Terraform code is generated or edited;
- a plan is created;
- drift is suspected;
- infrastructure changes need human-readable review.

## Required context

- Terraform module path.
- Target workspace/environment.
- Provider versions.
- Current plan output.
- State backend and workspace metadata, if readable.
- Internal platform standards.

## Authority chain

1. Internal IaC standards.
2. HashiCorp Terraform docs / provider docs / Terraform Registry.
3. Policy-as-code rules: Sentinel, OPA, Checkov, tfsec.
4. Prior accepted modules/patterns.

## Allowed read-only actions

- `terraform fmt -check`
- `terraform validate`
- `terraform plan`
- `terraform show -json plan.out`
- `tflint`
- `checkov`
- `tfsec`
- read provider docs via Terraform MCP or official Registry

## Forbidden actions

- `terraform apply`
- `terraform destroy`
- editing remote state
- changing backend config in production without explicit approval
- rotating or exposing secrets
- importing resources without a written plan

## Review checklist

- What resources are created/updated/deleted/replaced?
- Is any replacement destructive?
- Does the change affect public exposure, IAM, network paths, storage, DNS, or data retention?
- Are provider/module versions pinned?
- Are variables and outputs sane?
- Are secrets avoided in state and outputs?
- Do policy checks pass?
- Is rollback possible?

## Risk classification

- Low: additive non-production changes with no IAM/network/public exposure.
- Medium: production changes without deletion/replacement and with clean policy checks.
- High: deletions, replacements, IAM widening, public ingress, DB/storage changes, state/backend edits.

## Output format

```markdown
# Terraform Plan Review

## Verdict
approve / request changes / reject

## Blast radius

## Resource changes

## Security concerns

## Cost concerns

## Data loss risk

## Validation output

## Required approvals

## Rollback plan

## Assumptions
```
