# Skill: Incident Triage

## Purpose

Classify an incident, separate symptoms from suspected causes, assess impact, and produce a safe initial mitigation plan.

## When to use

Use when:

- a monitoring alert fires;
- a user reports outage, latency, data loss, or security concern;
- an on-call engineer needs quick structured triage;
- a system degradation appears but root cause is not confirmed.

## Required context

- Alert text and timestamp.
- Affected service/component.
- SLO/SLA and severity matrix.
- Service catalog owner and escalation path.
- Recent deploy/change history.
- Monitoring dashboards and logs in read-only mode.
- Existing runbook, if any.

## Authority chain

1. Internal incident management policy and severity matrix.
2. Service-specific runbooks.
3. Google SRE incident management principles.
4. Monitoring/logging official docs.
5. Community examples only as phrasing inspiration.

## Allowed read-only actions

- Read dashboards, alerts, traces, logs, status pages.
- Read deploy history and recent changes.
- Read service catalog / on-call schedule.
- Read incident history.

## Forbidden actions

- Restart, delete, scale, drain, reboot, failover, patch, or deploy anything.
- Announce unconfirmed root cause as fact.
- Close/resolve incident without human confirmation.
- Change alert rules during active incident unless explicitly approved.

## Workflow

1. Identify user-visible symptom.
2. Estimate blast radius: users, regions, services, duration, data impact.
3. Classify severity.
4. Identify owner and escalation path.
5. Collect evidence from monitoring/logs.
6. List hypotheses, clearly marked as hypotheses.
7. Propose mitigations with risk level.
8. Draft stakeholder update.
9. Recommend next check-in time.
10. Create post-incident notes skeleton.

## Validation steps

- Every claim must be backed by dashboard/log/ticket evidence or marked unknown.
- Mitigation must include expected effect and rollback option.
- If severity is high, suggest Incident Commander / Comms Lead / Ops Lead split.

## Output format

```markdown
# Incident Triage Report

## Summary

## User impact

## Severity

## Evidence

## Hypotheses

## Recommended mitigation

## Risks

## Escalation

## Stakeholder update draft

## Unknowns / assumptions

## Follow-up actions
```
