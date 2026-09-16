---
artifact_type: reference
authority_tier: Tier A
status: useful-after-audit
source_type: official-docs
topics:
  - browser-automation
  - chrome-devtools
  - mcp
  - debugging
domains:
  - browser-automation
owner: Chrome DevTools
last_checked: 2026-09-16
source_url: https://developer.chrome.com/docs/devtools/agents/get-started
---

# Reference: Chrome DevTools for Agents

## Authority tier

Tier A

## Status

useful-after-audit

## Owner / maintainer

Chrome DevTools

## URL

https://developer.chrome.com/docs/devtools/agents/get-started

## Last checked

2026-09-16

## Scope

Official Chrome DevTools agent tooling: Chrome DevTools MCP server, CLI and agentic skills for
controlling and inspecting a live Chrome browser.

## Why trusted

Primary Chrome DevTools documentation.

## Caveats

Attaching an agent to an existing authenticated browser exposes the session's content, cookies and
reachable account state to that agent. This is a powerful debugging/runtime capability, not a safe
credential boundary by itself.

## Extracted rules

- Use DevTools/MCP for observability and diagnosis where it gives information unavailable through
  ordinary DOM actions.
- Treat attach-to-existing-browser as privileged access and isolate it from unrelated user sessions.
- Prefer temporary isolated profiles when persistent authentication is unnecessary.
- Scope agent capabilities and redact sensitive data from collected traces/artifacts.

## Do not use this source for

Granting a general-purpose coding agent unrestricted access to a user's daily browser profile.

## Related references

- [Playwright Agent Runtime 2026](./playwright-agent-runtime-2026.md)
- [OWASP AI Agent Security](./owasp-ai-agent-security.md)
