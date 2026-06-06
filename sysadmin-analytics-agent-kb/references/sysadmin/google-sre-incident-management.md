---
artifact_type: reference
authority_tier: Tier A
status: foundation
domain: sre
owner: Google SRE
last_checked: 2026-06-06
source_url: https://sre.google/resources/practices-and-processes/incident-management-guide/
---

# Reference: Google SRE Incident Management Guide

## Authority tier

Tier A

## Status

foundation

## Owner / maintainer

Google SRE / sre.google

## URL

https://sre.google/resources/practices-and-processes/incident-management-guide/

## Last checked

2026-06-06

## Scope

Authoritative guidance for incident preparation, alerting philosophy, incident roles, stakeholder communication, mitigation, learning, and blameless postmortems.

## Why trusted

Google SRE is one of the most influential sources for modern reliability engineering. The incident guide is published by Google SRE and aligns with the broader SRE books and Site Reliability Workbook.

## Caveats

Google-scale practices must be adapted to smaller organizations. The guide provides principles and process, not environment-specific runbooks.

## Skills that may consume this reference

- [Incident Triage](../../sysadmin/skills/incident-triage.md)
- future: postmortem-generator
- future: alert-quality-review
- future: severity-classification

## Agents that may consume this reference

- [Sysadmin / SRE / Network Assistant](../../agents/sysadmin-agent.md)

## Extracted rules

- Alerts should focus on user-visible symptoms, not only internal causes.
- Alerts must be timely and actionable.
- On-call teams need up-to-date playbooks and training.
- Major incidents benefit from explicit roles such as Incident Commander, Communications Lead, and Operations Lead.
- Incident communications are as important as technical mitigation.
- Postmortems should be blameless and focus on improving systems, procedures, and training.

## Do not use this source for

- Exact commands for your infrastructure.
- Your organization’s severity matrix.
- Legal/compliance incident obligations.
- Product-specific customer communication language.

## Related references

- future: Google SRE Book
- future: Site Reliability Workbook

## Notes

Skills should link here instead of linking directly to the external Google SRE URL.
