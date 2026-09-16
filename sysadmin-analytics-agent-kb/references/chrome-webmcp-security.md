---
artifact_type: reference
authority_tier: Tier A
status: foundation
source_type: official-docs
topics:
  - browser-automation
  - webmcp
  - prompt-injection
  - agent-security
domains:
  - browser-automation
owner: Chrome for Developers
last_checked: 2026-09-16
source_url: https://developer.chrome.com/docs/ai/webmcp/secure-tools
---

# Reference: WebMCP Tool Security

## Authority tier

Tier A

## Status

foundation

## Owner / maintainer

Chrome for Developers

## URL

https://developer.chrome.com/docs/ai/webmcp/secure-tools

## Last checked

2026-09-16

## Scope

Security considerations for browser agents consuming WebMCP tools, especially indirect prompt
injection and malicious or compromised tool behavior.

## Why trusted

Primary security guidance from the team documenting the WebMCP browser experiment.

## Caveats

The guidance is tied to an experimental API. General agent-security controls still need independent
application-level enforcement.

## Extracted rules

- Treat page text, tool descriptions, schemas and tool outputs as untrusted input.
- Never let instructions returned by a page silently expand the agent's permissions.
- Enforce navigation, tool, data-flow and high-impact-action policies below the model.
- Require independent validation for financial, credential, account and destructive actions.

## Do not use this source for

A complete threat model for all agent architectures.

## Related references

- [Chrome WebMCP](./chrome-webmcp.md)
- [OWASP AI Agent Security](./owasp-ai-agent-security.md)
