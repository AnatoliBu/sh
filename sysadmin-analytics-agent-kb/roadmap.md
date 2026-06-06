---
artifact_type: index
status: foundation
domain: tooling
owner: Agent KB
last_checked: 2026-06-06
---

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

## Phase 6 — Quartz publishing and UX

### Current deployment mode

- [x] Build public GitHub Pages from this repository without cross-repo tokens.
- [x] Use public Quartz engine as build dependency.
- [x] Copy only curated Agent KB content into Quartz `content/`.
- [x] Exclude `research/`, `site/`, `references/tooling/`, and root `README.md` from published Quartz content.
- [x] Write aggregated CI logs to `ci-reports/latest.md` so failures can be read from the repository.

### Later option: private Quartz engine repo

- [ ] Decide whether a private Quartz engine repo is still useful.
- [ ] If using a private engine repo, document that public GitHub Pages exposes compiled JS/CSS assets even when source repo stays private.
- [ ] Treat private repo as protection for source history, development workflow, and non-published tooling — not as strong secrecy for browser-executed UI logic.
- [ ] For genuinely private UX or operational logic, use a private/restricted hosting target instead of public GitHub Pages.
- [ ] If private engine repo is adopted, add `QUARTZ_REPO_TOKEN` or a deploy key and restore cross-repo checkout intentionally.

### UX backlog

- [ ] Evaluate stock Quartz graph/search/backlinks after public deploy.
- [ ] Port only missing Agent KB-specific UX:
  - graph folder semantics;
  - backlinks grouping by artifact type/domain;
  - frontmatter badges/filters;
  - lightweight reference previews if stock popovers are insufficient.
