---
artifact_type: rule
status: foundation
domain: browser-automation
---

# Rule: Browser Automation Safety

## Reference links

Authority references:

- [OWASP Session Management Cheat Sheet](../../references/owasp-session-management.md)
- [PCI DSS](../../references/pci-dss.md)
- [Browserless Hybrid Automation](../../references/browserless-hybrid-automation.md)

## Invariants

1. Automate only an authorized workflow and respect the target site's applicable rules.
2. A CAPTCHA or anti-bot challenge is not permission to escalate evasion. Use supported handling,
   human takeover, or stop.
3. Passwords, MFA seeds, PAN/CVV, auth headers, and raw browser storage state are secrets.
4. Irreversible actions need an explicit business/policy gate and a post-action reconciliation
   path.
5. Human takeover must stay in the same scoped session; never share infrastructure API keys.
6. Session/profile persistence is opt-in by workflow, not a default.
7. Observability must be useful without capturing secrets.

## Risk classes

```text
R0 read-only public browsing
R1 authenticated read-only
R2 reversible account mutation
R3 financial/irreversible mutation
```

R0 can usually run unattended. R1 requires protected auth state. R2 requires explicit target and
post-condition. R3 requires pre-submit verification, idempotency/reconciliation, and a policy gate;
human/cardholder authentication remains with the authorized user when required.

## Stop conditions

Stop instead of improvising when:

- account identity/merchant/amount cannot be verified;
- the session appears to belong to the wrong user;
- the payment result is ambiguous;
- the site demands credentials outside the expected origin;
- automation would require defeating a security control outside the authorized workflow;
- the provider session/viewer URL was exposed or reused unexpectedly.
