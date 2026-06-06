# Skill: Kubernetes Manifest Review

## Purpose

Review Kubernetes manifests for correctness, security, operability, and policy compliance before they are applied.

## Reference links

Authority references:

- [Kubernetes Pod Security Standards](../../references/sysadmin/kubernetes-pod-security-standards.md)

## When to use

Use for any proposed change to:

- Deployment / StatefulSet / DaemonSet / Job / CronJob;
- Service / Ingress / Gateway;
- ConfigMap / Secret reference;
- Role / ClusterRole / RoleBinding / ClusterRoleBinding;
- NetworkPolicy;
- Helm chart values or rendered manifests.

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
3. [Kubernetes Pod Security Standards](../../references/sysadmin/kubernetes-pod-security-standards.md).
4. OPA/Gatekeeper/Kyverno policies if used.
5. Audited community checklists.

## Allowed read-only actions

- Parse YAML.
- Run `kubectl diff` / `kubectl apply --dry-run=server` where safe.
- Run schema validation: `kubeconform`, `kubeval`.
- Run security/config scanners: `polaris`, `kube-score`, `trivy config`, `checkov`.
- Query cluster state read-only: API versions, namespace labels, quotas, existing resources.

## Forbidden actions

- `kubectl apply`
- `kubectl delete`
- `kubectl patch`
- `kubectl scale`
- `kubectl rollout restart`
- `kubectl drain` / `cordon` / `uncordon`
- creating wildcard RBAC without security approval
- deploying privileged pods without explicit exception

## Review checklist

### API and schema

- API versions valid for target cluster.
- No deprecated APIs.
- Namespaces exist.
- Required labels/annotations present.

### Runtime safety

- Requests and limits set.
- Readiness/liveness/startup probes make sense.
- Graceful termination configured where relevant.
- Rolling update strategy does not exceed capacity.

### Security

- No privileged container unless approved.
- No hostPID/hostIPC/hostNetwork unless approved.
- No hostPath unless approved.
- SecurityContext present.
- `runAsNonRoot` where possible.
- Image tag pinned; avoid `latest`.
- Pull from trusted registry.

### RBAC

- No wildcard `verbs`, `resources`, or `apiGroups` unless approved.
- Scope namespace-local unless cluster-scope is necessary.
- ServiceAccount explicitly named.

### Network

- Service ports match container ports.
- Ingress/Gateway has TLS policy.
- NetworkPolicy present for restricted namespaces.

## Validation steps

1. Render manifests if Helm/Kustomize is used.
2. Validate schema.
3. Run policy scanners.
4. Run server-side dry-run.
5. Produce diff.
6. Classify risk.
7. Request human approval before apply.

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
