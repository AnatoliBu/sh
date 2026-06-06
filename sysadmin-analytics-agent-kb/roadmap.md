# Roadmap

## Phase 1 — Repository skeleton

Status: started.

- [x] Create top-level structure.
- [x] Add source hierarchy for sysadmin/SRE/network.
- [x] Add source hierarchy for analytics/product analytics.
- [x] Add global skill template.
- [x] Add global agent rules.
- [x] Add bullshit-check mode.
- [x] Add initial sysadmin skills.
- [x] Add initial analytics skills.

## Phase 2 — Source-of-truth cards

Create source cards for:

- Google SRE
- Kubernetes official docs
- Kubernetes Pod Security Standards
- OWASP Kubernetes Top 10
- CIS Kubernetes Benchmark
- NetBox
- Nautobot
- Batfish
- Terraform docs / Terraform MCP
- Prometheus
- Grafana
- Ansible
- PagerDuty
- BigQuery
- Snowflake
- Databricks
- dbt semantic layer
- Mixpanel
- Amplitude
- PostHog

## Phase 3 — Skills

### Sysadmin

- linux-readonly-triage
- systemd-service-triage
- disk-memory-cpu-triage
- network-path-debug
- dns-debug
- tls-cert-debug
- k8s-manifest-review
- k8s-rbac-review
- k8s-service-ingress-debug
- terraform-plan-review
- ansible-playbook-review
- netbox-drift-analysis
- incident-triage
- postmortem-generator

### Analytics

- sql-review
- metric-reconciliation
- funnel-analysis
- cohort-analysis
- retention-analysis
- ab-test-review
- dashboard-specification
- executive-summary
- assumptions-log

## Phase 4 — Agent packaging

- Sysadmin/SRE agent definition.
- Analytics/Product analytics agent definition.
- Shared guardrails.
- Approval protocol.
- Output schemas.
- Evaluation cases.

## Phase 5 — Evaluation

Build small benchmark cases:

- bad Kubernetes manifest;
- dangerous Terraform plan;
- noisy alert triage;
- DNS mismatch;
- TLS wrong certificate;
- metric discrepancy;
- funnel drop-off;
- SQL fanout bug;
- invalid A/B test conclusion.
