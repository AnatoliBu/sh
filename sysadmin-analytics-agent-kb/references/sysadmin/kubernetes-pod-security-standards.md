---
artifact_type: reference
authority_tier: Tier A
status: foundation
domain: sysadmin
owner: Kubernetes project
last_checked: 2026-06-06
source_url: https://kubernetes.io/docs/concepts/security/pod-security-standards/
---

# Reference: Kubernetes Pod Security Standards

## Authority tier

Tier A

## Status

foundation

## Owner / maintainer

Kubernetes project

## URL

https://kubernetes.io/docs/concepts/security/pod-security-standards/

## Last checked

2026-06-06

## Scope

Authoritative reference for Kubernetes Pod Security Standards: Privileged, Baseline, and Restricted profiles.

## Why trusted

This is upstream Kubernetes documentation maintained by the Kubernetes project. It defines the security profiles used by Pod Security Admission and gives concrete restrictions for pod specs.

## Caveats

Pod Security Standards are broad built-in profiles, not a complete security program. Organizations may need stricter policies through Kyverno, Gatekeeper/OPA, custom admission controls, runtime security, and supply-chain scanning.

## Skills that may consume this reference

- [Kubernetes Manifest Review](../../sysadmin/skills/k8s-manifest-review.md)
- future: k8s-rbac-review
- future: k8s-networkpolicy-review
- future: k8s-service-ingress-debug

## Agents that may consume this reference

- [Sysadmin / SRE / Network Assistant](../../agents/sysadmin-agent.md)

## Extracted rules

- Default application workloads should not use the Privileged profile.
- Baseline prevents known privilege escalations while remaining broadly adoptable.
- Restricted follows current pod hardening best practices.
- Privileged containers, host namespaces, hostPath volumes, and broad capabilities require explicit exception review.

## Do not use this source for

- General Kubernetes troubleshooting.
- Full cluster hardening.
- Cloud-provider-specific managed Kubernetes controls.
- Container image vulnerability policy.

## Related references

- future: Kubernetes RBAC docs
- future: Kubernetes NetworkPolicy docs
- future: OWASP Kubernetes Top 10
- future: CIS Kubernetes Benchmark

## Notes

Use this reference from manifest/security review skills rather than linking directly to the upstream page.
