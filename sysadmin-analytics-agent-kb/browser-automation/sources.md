---
artifact_type: index
status: foundation
domain: browser-automation
---

# Browser Automation Sources

The domain separates four authority layers:

1. browser semantics and deterministic automation;
2. remote-browser/human-handoff infrastructure;
3. agentic browser control;
4. security constraints for authenticated and payment-bearing sessions.

## Foundation authority

- [Playwright Documentation](../references/playwright-docs.md) — deterministic browser control,
  locators, waits, contexts, auth state.
- [Browserbase Live View and Session Contexts](../references/browserbase-live-view-contexts.md) —
  managed sessions and human takeover.
- [Browserless Hybrid Automation](../references/browserless-hybrid-automation.md) — LiveURL,
  Playwright/CDP, hybrid human/automation flow.
- [Steel Browser Documentation](../references/steel-browser-docs.md) and
  [Steel Agent Skills](../references/steel-agent-skills.md) — browser infra, debugging and
  reliability playbooks for coding agents.
- [Browser Use](../references/browser-use-repo.md) and
  [Stagehand](../references/browserbase-stagehand.md) — agentic/semantic browser control.
- [OWASP Session Management Cheat Sheet](../references/owasp-session-management.md) — bearer-session
  security.
- [PCI DSS](../references/pci-dss.md) — card-data scope and handling constraints.

## Trust rule

Vendor documentation is authoritative for the vendor API, not proof that a workflow is reliable on
a target site. Reliability must be demonstrated with recorded scenario tests, failure injection,
and repeated runs against the accounts/locales actually supported.
