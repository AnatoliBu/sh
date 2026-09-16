---
artifact_type: reference
authority_tier: Tier A
status: foundation
source_type: official-repo
topics:
  - browser-automation
  - browser-use
  - agentic-browser
  - llm
domains:
  - browser-automation
owner: Browser Use
last_checked: 2026-09-16
source_url: https://github.com/browser-use/browser-use
---

# Reference: Browser Use

## Authority tier

Tier A

## Status

foundation

## Owner / maintainer

Browser Use

## URL

https://github.com/browser-use/browser-use

## Last checked

2026-09-16

## Scope

Agentic browser control where an LLM perceives browser state, plans actions, and operates through a
browser session, including integration with remote CDP browsers.

## Why trusted

Official Browser Use repository.

## Caveats

Agentic operation is more flexible but less deterministic than a fixed Playwright state machine.
Do not put irreversible payment actions behind unconstrained free-form planning.

## Extracted rules

- Use agentic browsing for discovery, changing interfaces, and tasks whose next action cannot be
  encoded cheaply.
- Bound the agent with explicit goals, allowed actions, terminal states, budgets, and assertions.
- Once a path becomes repetitive, compile the successful behavior into a deterministic workflow.
- Keep irreversible actions behind an explicit confirmation/policy gate.

## Do not use this source for

Payment security, legal permission to automate a site, or generic session security.

## Related references

- [Playwright Documentation](./playwright-docs.md)
- [Steel Browser Documentation](./steel-browser-docs.md)
