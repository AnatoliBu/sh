# Playwright Documentation

Official source: https://playwright.dev/docs/intro

Use this authority for deterministic browser control, contexts, locators, auto-waiting,
authentication state, downloads, and tracing.

## Agent rules

- Prefer role/label/text/test-id locators over generated CSS/XPath.
- Wait for observable state, not fixed sleeps.
- Treat persisted storage state as a credential.
- Assert a business post-condition after every state-changing action.
- Keep deterministic steps deterministic; use an LLM only where the task is genuinely open-ended.
