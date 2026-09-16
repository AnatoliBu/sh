---
artifact_type: reference
authority_tier: Tier A
status: useful-after-audit
source_type: official-docs
topics:
  - browser-automation
  - webmcp
  - agent-tools
  - api-first
domains:
  - browser-automation
owner: Chrome for Developers
last_checked: 2026-09-16
source_url: https://developer.chrome.com/docs/ai/webmcp
---

# Reference: Chrome WebMCP

## Authority tier

Tier A

## Status

useful-after-audit

## Owner / maintainer

Chrome for Developers

## URL

https://developer.chrome.com/docs/ai/webmcp

## Last checked

2026-09-16

## Scope

WebMCP, a proposed web standard for sites to expose structured first-party tools to browser agents
through imperative JavaScript APIs and declarative HTML annotations.

## Why trusted

Primary Chrome documentation for the WebMCP experiment and origin trial.

## Caveats

WebMCP is experimental and is not yet a finalized cross-browser web standard. Chrome documents it
primarily for local browser workflows with a human in the loop; availability and API shape may
change.

## Extracted rules

- Prefer a typed first-party WebMCP capability over inferred DOM clicking when the page exposes one.
- Keep capability discovery separate from execution so policy can inspect tool name and schema.
- Treat WebMCP outputs as untrusted page-originated data even though the interface is structured.
- Maintain DOM/Playwright fallback while WebMCP remains experimental.

## Do not use this source for

Claims of universal browser support or proof that a WebMCP tool is safe merely because a site
exposes it.

## Related references

- [WebMCP Tool Security](./chrome-webmcp-security.md)
- [Model Context Protocol Specification](./model-context-protocol-spec.md)
