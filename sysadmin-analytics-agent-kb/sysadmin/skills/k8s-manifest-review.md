---
artifact_type: skill
authority_tier: Tier A
status: foundation
domain: sysadmin
owner: Agent KB
last_checked: 2026-06-06
---

# Skill: Kubernetes Manifest Review

## Purpose

Review Kubernetes manifests for correctness, security, operability, and policy compliance before changes are applied.

## Reference links

Authority references:

- [Kubernetes Pod Security Standards](../../references/kubernetes-pod-security-standards.md)

## When to use

Use for proposed changes to workloads, services, ingress/gateway objects, configuration references, RBAC, NetworkPolicy, Helm values, or rendered manifests.

## Required context

- Manifest YAML/JSON.
- Target cluster version.
- Target namespace.
- Pod Security admission level.
- ResourceQuota and LimitRange.
- Organization security policy.
- Intended service owner and environment.

## Authority chain

1. Internal platform standards.
2. Kubernetes official docs.
3. [Kubernetes Pod Security Standards](../../references/kubernetes-pod-security-standards.md).
4. OPA/Gatekeeper/Kyverno policies if used.
5. Audited community checklists.

## Review checklist

### API and schema

- API versions valid for target cluster.
- No deprecated APIs.
- Namespaces exist.
- Required labels/annotations present.

### Runtime safety

- Requests and limits set.
- Health probes make sense.
- Graceful termination configured where relevant.
- Update strategy does not exceed capacity.

### Security

- No privileged container unless approved.
- No host namespaces unless approved.
- No hostPath unless approved.
- SecurityContext present.
- Image tag pinned.
- Pull from trusted registry.

### RBAC

- No wildcard privileges unless approved.
- Scope namespace-local unless cluster-scope is necessary.
- ServiceAccount explicitly named.

## Validation steps

1. Render manifests if Helm/Kustomize is used.
2. Validate schema.
3. Run policy scanners.
4. Produce diff.
5. Classify risk.
6. Request human approval before mutation.

## Output format

```markdown
# Kubernetes Manifest Review

## Verdict
approve / request changes / reject

## Risk level
low / medium / high

## Findings

## Required changes

## Optional improvements

## Validation output

## Approval notes
```
