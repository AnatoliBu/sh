# Stagehand

Official source: https://github.com/browserbase/stagehand

Use this authority for LLM-assisted semantic browser actions/extraction mixed with programmatic
browser control.

## Agent rules

- Use semantic actions only where selectors are expensive or unstable.
- Prefer observe/extract when understanding the page is enough.
- Assert deterministic state before and after consequential actions.
- Keep final submit/cancel/upgrade/delete/payment actions explicit and reconciliation-aware.
