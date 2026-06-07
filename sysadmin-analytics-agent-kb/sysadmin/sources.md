---
artifact_type: reference
status: foundation
domain: sysadmin
---

# Sysadmin / SRE / Network Sources

This file ranks source-of-truth references by authority for building reliable agent skills.

## Tier A — foundation sources

### Google SRE

Use Google SRE books and the Incident Management Guide as foundation references for:

- incident response;
- alerting philosophy;
- on-call preparation;
- blameless postmortems;
- SLO/error budget thinking.

Operational rule: agent output must separate symptoms, impact, mitigation, suspected root cause, and confirmed root cause.

### Kubernetes official documentation

Use upstream Kubernetes docs as the source of truth for:

- API versions;
- workloads;
- RBAC;
- NetworkPolicy;
- Pod Security Standards;
- probes;
- resource requests/limits.

Operational rule: agent must not rely on memory for Kubernetes API details. Validate manifests through schema/dry-run tools.

### NetBox / Nautobot docs

Use these as source-of-truth references for network inventory, IPAM, DCIM, intended topology, ownership, and automation inputs.

Operational rule: agent must not invent network topology. It reads intended state from SoT and compares with observed state.

### HashiCorp Terraform docs and Terraform MCP

Use HashiCorp docs for Terraform syntax, providers, modules, policies, and current registry metadata.

Operational rule: Terraform MCP is context, not trusted execution. Agent proposes config, runs validation/plan, then requires approval.

### Prometheus / Grafana docs

Use official docs for PromQL, alerting rules, recording rules, and dashboard semantics.

Operational rule: agent must not make up alert semantics. It must link alert expression to user impact or explicitly label it as preventive/internal.

## Tier B — useful after audit

- cc-devops-skills: good scaffold pattern for generate → validate → dry-run workflows, but audit before reuse.
- Kubernetes community skills: useful prompt structure, but not authority.
- Incident runbook templates: useful as form, not content.

## Tier C — cheat sheets only

- terminal-skills and command collections: use as command discovery only; not as expertise.

## Tier D — quarantine / inspiration only

- NetClaw / OpenClaw: too much scope, weak trust model, broad blast radius. Use only as a feature taxonomy or moodboard, not as runtime, implementation model, or foundation.

## Source admission checklist

A source may enter Tier A only if it is one of:

1. official vendor/project documentation;
2. standards/security benchmark;
3. mature, widely deployed open-source project documentation;
4. internal company source of truth.

Every source entry should include:

- owner;
- URL;
- last checked date;
- authority tier;
- what skills can consume it;
- known caveats.
