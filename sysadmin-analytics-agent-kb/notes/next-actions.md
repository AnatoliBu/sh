# Next Actions

## Immediate

1. Move this folder into a dedicated private repository when repo creation is available.
2. Convert `sources.md` into individual source cards.
3. Add citations/links to each source card.
4. Add evaluation cases for skills.
5. Add CI checks for markdown structure.

## Source card template

```markdown
# Source: <name>

## Authority tier

## Owner / maintainer

## URL

## Last checked

## Why trusted

## Caveats

## Skills that can consume it

## Extracted rules

## Rejected / not reusable parts
```

## Priority skills to add next

### Sysadmin

- linux-readonly-triage
- systemd-service-triage
- network-path-debug
- k8s-rbac-review
- k8s-service-ingress-debug
- ansible-playbook-review
- netbox-drift-analysis
- postmortem-generator

### Analytics

- cohort-analysis
- retention-analysis
- ab-test-review
- dashboard-specification
- executive-summary
- assumptions-log

## Evaluation cases

- broken Kubernetes manifest
- wildcard RBAC manifest
- Terraform plan with destructive replacement
- DNS split-horizon mismatch
- wrong TLS certificate via SNI
- metric discrepancy caused by timezone
- SQL fanout bug
- funnel drop caused by instrumentation change
- A/B test with underpowered sample
