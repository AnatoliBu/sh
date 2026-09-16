---
artifact_type: skill
status: foundation
domain: browser-automation
---

# Skill: Browser Flow Reliability

## Purpose

Turn a browser script that "worked once" into a workflow with explicit states, bounded retries,
diagnostics, and safe recovery.

## Reference links

Authority references:

- [Playwright Documentation](../../references/playwright-docs.md)
- [Steel Agent Skills](../../references/steel-agent-skills.md)
- [Browserless Hybrid Automation](../../references/browserless-hybrid-automation.md)

## Reliability contract

Every consequential step needs:

```text
precondition
action
post-condition
timeout
retry policy
evidence on failure
idempotency classification
```

Example:

```text
state: BILLING_PAGE
pre: current plan and target account are visible
action: click "Add payment method"
post: payment form/hosted frame is visible
retry: re-read page once; never double-submit a payment
failure evidence: URL + sanitized DOM summary + screenshot + console/network errors
```

## Locator order

Prefer:

1. role + accessible name;
2. associated label;
3. stable text in a scoped container;
4. application test id when available;
5. stable semantic attribute;
6. CSS/XPath only when there is no stronger contract.

Do not use fixed sleeps for readiness. Wait for the actual state.

## Retries

Classify failures before retrying:

```text
TRANSIENT_NETWORK
PAGE_NOT_READY
SESSION_EXPIRED
HUMAN_REQUIRED
BUSINESS_REJECTED
UNKNOWN_UI
IRREVERSIBLE_UNKNOWN
```

Only the first two are normally safe for automatic replay. Session expiration goes to auth/handoff.
Business rejection is a terminal business result. Unknown irreversible state requires reconciliation
before any retry.

## Idempotency

For payments, subscription changes, orders, invitations, or deletes:

- persist an operation id before browser action;
- capture merchant-visible result identifiers;
- on timeout, inspect current state before repeating;
- separate "click did not return" from "operation did not happen";
- never use blind retry around final submit.

## Evidence

On failure keep the minimum evidence necessary to reproduce:

```text
workflow/session id
merchant adapter + version
logical state
sanitized URL
last successful assertion
screenshot with secret zones masked
console errors
selected network failures
provider session/trace reference
```

Do not capture passwords, MFA secrets, PAN/CVV, authorization headers, or unredacted storage state.

## Regression suite

For every supported merchant/account class, freeze scenarios for:

- fresh login;
- already logged in;
- MFA/3DS/human takeover;
- expected recurring/plan state;
- changed UI text;
- popup/iframe;
- provider timeout;
- merchant rejection;
- ambiguous result after submit.

A browser flow is production-ready only after repeated clean runs and deliberate failure injection.

## Anti-patterns

- `waitForTimeout(5000)` as synchronization;
- retrying every exception three times;
- selectors copied from generated class names;
- treating HTTP/browser success as business success;
- screenshotting the whole payment page into logs.
