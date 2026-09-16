---
artifact_type: reference
authority_tier: Tier A
status: foundation
source_type: security-guidance
topics:
  - browser-automation
  - agent-security
  - prompt-injection
  - least-privilege
domains:
  - browser-automation
owner: OWASP Cheat Sheet Series
last_checked: 2026-09-16
source_url: https://cheatsheetseries.owasp.org/cheatsheets/AI_Agent_Security_Cheat_Sheet.html
---

# Reference: OWASP AI Agent Security Cheat Sheet

## Authority tier

Tier A

## Status

foundation

## Owner / maintainer

OWASP Cheat Sheet Series

## URL

https://cheatsheetseries.owasp.org/cheatsheets/AI_Agent_Security_Cheat_Sheet.html

## Last checked

2026-09-16

## Scope

Agent-specific security risks including direct/indirect prompt injection, tool abuse, privilege
escalation, data exfiltration, memory poisoning, excessive autonomy and high-impact actions.

## Why trusted

OWASP security guidance maintained as part of the Cheat Sheet Series.

## Caveats

It is general security guidance rather than a browser-automation implementation specification.
Controls must be mapped to the project's concrete runtime and threat model.

## Extracted rules

- External web content is untrusted data, never policy.
- Give the browser agent the minimum tools, scopes and credentials required for the current task.
- Separate read-only capabilities from state-changing capabilities.
- Independently authorize financial, destructive, administrative and externally visible actions.
- Bound recursion, retries, tokens, runtime and monetary cost.
- Isolate memory and session state per user and expire it deliberately.

## Do not use this source for

Claims that prompt sanitization alone solves indirect prompt injection.

## Related references

- [WebMCP Tool Security](./chrome-webmcp-security.md)
- [OWASP Session Management](./owasp-session-management.md)
