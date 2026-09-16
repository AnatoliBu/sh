# Browserbase Live View and Session Contexts

Official source: https://docs.browserbase.com/platform/browser/observability/session-live-view

Use this authority for Browserbase managed sessions, interactive Live View/human takeover, session
observability, and contexts that intentionally preserve browser identity/authentication state.

## Agent rules

- Human takeover is a normal state transition, not an exceptional workaround.
- Keep automation and human interaction in the same browser session.
- Persist a context only when continuity is intentional; prefer ephemeral state for one-off flows.
- Do not expose infrastructure API keys in user-facing viewer links.
