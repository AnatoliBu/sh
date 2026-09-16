---
artifact_type: reference
authority_tier: Tier A
status: foundation
source_type: official-repo
topics:
  - agent-skills
  - browser-automation
  - steel
  - reliability
domains:
  - browser-automation
owner: Steel
last_checked: 2026-09-16
source_url: https://github.com/steel-dev/skills
---

# Reference: Steel Agent Skills

## Authority tier

Tier A

## Status

foundation

## Owner / maintainer

Steel

## URL

https://github.com/steel-dev/skills

## Last checked

2026-09-16

## Scope

First-party coding-agent skills for live browser work, integration development, session debugging,
reliability, and converting repeated browser tasks into reusable workflows.

## Why trusted

First-party Steel repository and documentation for its own agent skills.

## Caveats

These skills are vendor-specific. Use their structure and operational playbooks as references, but
keep project orchestration behind a provider adapter so the application is not locked to one cloud.

## Extracted rules

- Separate doing browser work from developing browser integrations and from debugging reliability.
- Use a dedicated reliability playbook for bot detection, identity, CAPTCHA, pacing, and retries.
- Turn a repeatedly successful exploratory run into a reusable deterministic workflow.
- Run provider preflight/doctor checks before blaming application code.

## Do not use this source for

Playwright semantics that are independent of Steel.

## Related references

- [Steel Browser Documentation](./steel-browser-docs.md)
- [Playwright Documentation](./playwright-docs.md)
