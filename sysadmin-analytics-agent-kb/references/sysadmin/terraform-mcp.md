# Reference: Terraform MCP Server

## Authority tier

Tier A for documentation context, not execution

## Status

foundation-context / beta-caveat

## Owner / maintainer

HashiCorp

## URL

https://developer.hashicorp.com/terraform/mcp-server

## Last checked

2026-06-06

## Scope

Authoritative context source for current Terraform provider documentation, Registry modules, policies, and Terraform/HCP Terraform metadata exposed through MCP.

## Why trusted

This is official HashiCorp documentation. It exists specifically to give AI tools current Terraform documentation and registry context rather than relying on stale model training data.

## Caveats

The Terraform MCP Server documentation marks the feature as beta. Treat it as a context/documentation source unless a separate security review approves any workspace operations. Do not use it as a trusted production execution plane by default.

## Skills that may consume this reference

- [Terraform Plan Review](../../sysadmin/skills/terraform-plan-review.md)
- future: terraform-module-review
- future: terraform-drift-analysis

## Agents that may consume this reference

- [Sysadmin / SRE / Network Assistant](../../agents/sysadmin-agent.md)

## Extracted rules

- Prefer current provider docs over model memory.
- Generated Terraform must pass fmt, validate, lint, security checks, plan review, and approval.
- Terraform apply/destroy/import/state operations require explicit approval.
- MCP context does not remove the need for policy-as-code and human review.

## Do not use this source for

- Production apply approval.
- General cloud architecture authority outside Terraform provider docs.
- Secret handling policy.

## Related references

- future: Terraform CLI docs
- future: Terraform Registry
- future: Open Policy Agent / Sentinel

## Notes

Skills should link here when they rely on Terraform MCP as a current-docs source.
