# Research: Browser Automation Expansion

Last checked: 2026-09-16

## Scope

Expand the `browser-automation` domain only after a real vertical slice proves that the intended
consumer workflow can work end to end.

This note is research-stage only. It is deliberately not a skill, rule or workflow yet.

The target product shape is narrower than a general web agent:

```text
user-authorized task
  -> remote browser session
  -> human login / MFA when needed
  -> automation resumes in the same session
  -> billing / checkout navigation
  -> explicit payment action
  -> business outcome verification
  -> session close
```

The immediate goal is functional proof, not production hardening. Security and compliance remain in
the backlog and should be applied after the mechanics, provider behavior and failure modes are known.

A few minimum correctness constraints still apply during prototyping: do not put real passwords,
TOTP seeds, PAN or CVV into ordinary logs/prompts; do not blindly retry an ambiguous payment submit;
and keep the final irreversible action supervised until the flow is understood.

The concrete Step 1 execution plan lives in
[Browser Automation Golden-Path E2E PoC](./browser-automation-e2e-poc.md).

## Revised step plan

### Step 1 — golden-path E2E PoC

Prove one real flow with one provider and one target service.

Use the smallest useful stack:

```text
bot or tiny web UI
  -> backend
  -> one managed browser provider
  -> Live View / human takeover
  -> user login / MFA
  -> Playwright in the same session
  -> billing / checkout
  -> supervised final action
  -> verified subscription/payment outcome
  -> session close
```

Do not add provider abstractions, persistent profiles, WebMCP, computer-use, multi-agent orchestration
or a generic merchant framework unless the golden path actually needs them.

### Step 2 — make the E2E mechanically reliable

Fix only failures observed in the real flow:

- CAPTCHA/challenge handling;
- iframe / popup / SPA navigation;
- human takeover and resume;
- reconnect after mobile/background/network loss;
- re-authentication and MFA;
- recurring/card-on-file behavior;
- explicit detection of success, failure and ambiguous state.

This step is still product mechanics, not broad security hardening.

### Step 3 — architecture synthesis from observed pain

Only after Steps 1–2, extract the contracts that proved necessary:

- `BrowserProvider` or equivalent provider boundary;
- merchant-specific adapter contract;
- browser/session state machine;
- ephemeral versus persistent profile policy;
- deterministic Playwright versus semantic/vision fallback;
- human-control ownership and resume semantics.

Prefer a small number of cross-cutting contracts over one skill per technology.

### Step 4 — provider/runtime comparison

Replay the same frozen working scenarios across Browserbase, Browserless, Steel, Browser Use and a
self-hosted Playwright baseline where practical.

Measure at least:

```text
verified success rate
latency
browser minutes
proxy traffic
model/token cost where applicable
challenge frequency + class
human interventions
reconnect/session-loss failures
ambiguous transaction states
provider-specific errors
```

Public browser-agent benchmarks are useful for harness methodology but do not substitute for these
production-shaped scenarios.

### Step 5 — security, privacy and compliance hardening

Once the E2E design is real and stable, harden the actual architecture rather than a hypothetical one:

- secret storage and redaction;
- session-token TTL / revoke / access control;
- recording, screenshot and trace policy;
- prompt-injection enforcement boundaries;
- least privilege / navigation and action allowlists;
- persistent-profile isolation and deletion;
- encryption / retention / audit;
- PCI scope and payment-data handling;
- abuse, policy and compliance constraints.

Security references remain valuable now as a checklist of future constraints, but they should not
block the first functional proof unless they expose an immediate risk of irreversible loss or real
credential/payment leakage.

### Step 6 — domain artifacts and plugin packaging

Only after the previous steps stabilize, promote the conclusions into narrow skills, rules and
workflows, update `sources.md`, regenerate/sync the plugin package, and run normal CI.

## Step 1 technical target

The first PoC should answer only these questions:

1. Can a backend create a browser session that a real user can open comfortably from a phone or PC?
2. Can the user log in and complete MFA in that same session?
3. Can Playwright resume control without creating a new browser/session identity?
4. Can the automation reach billing/checkout reliably enough to perform one known flow?
5. Can control be returned to the human if CAPTCHA, MFA, 3DS or another interactive checkpoint appears?
6. Can the system determine the actual business outcome instead of merely observing a button click?
7. Can the session close cleanly after success or controlled failure?

### Minimal PoC states

```text
CREATED
  -> HUMAN_LOGIN
  -> AUTOMATION_ACTIVE
  -> CHECKOUT_READY
  -> HUMAN_CONFIRM_OR_CHALLENGE
  -> VERIFYING_OUTCOME
  -> SUCCEEDED | FAILED | AMBIGUOUS
  -> CLOSED
```

`AMBIGUOUS` is functional correctness, not security hardening: after a submit timeout or crash, the
system must inspect merchant/account/payment state before another attempt.

### Explicit non-goals for Step 1

- generic support for arbitrary websites;
- multi-provider abstraction;
- permanent browser profiles;
- automatic fingerprint/proxy strategy;
- agentic computer-use as the default controller;
- WebMCP integration;
- unattended autonomous payment submission;
- full secret vault / PCI / production compliance design;
- production-grade prompt-injection policy;
- large benchmark suite.

## Evidence map retained for later steps

The accepted references are already broad enough to support the later work. They remain grouped by
capability so they can be promoted when a real failure or design decision requires them.

### Deterministic runtime

- [Playwright Documentation](../references/playwright-docs.md)
- [Playwright Best Practices](../references/playwright-best-practices.md)
- [Playwright Agent Runtime 2026](../references/playwright-agent-runtime-2026.md)
- [WebDriver BiDi](../references/w3c-webdriver-bidi.md)

### Managed browsers and human handoff

- [Browserbase Live View and Session Contexts](../references/browserbase-live-view-contexts.md)
- [Browserless Hybrid Automation](../references/browserless-hybrid-automation.md)
- [Browserless BAP](../references/browserless-bap.md)
- [Steel Browser Documentation](../references/steel-browser-docs.md)
- [Browser Use Browser Harness 2026](../references/browser-use-harness-2026.md)

### Agentic control and page-native tools

- [Stagehand](../references/browserbase-stagehand.md)
- [Stagehand v4 2026](../references/stagehand-v4-2026.md)
- [Browser Use](../references/browser-use-repo.md)
- [Gemini Computer Use](../references/gemini-computer-use.md)
- [Chrome WebMCP](../references/chrome-webmcp.md)
- [Browserbase Code Mode 2026](../references/browserbase-code-mode-2026.md)

### Authentication and persistent identity

- [Browser Use Authentication Profiles](../references/browser-use-authentication.md)
- [Browser Use 2FA and Human Handoff](../references/browser-use-human-2fa.md)
- [WebAuthn Level 3](../references/w3c-webauthn-level-3.md)
- [OWASP Session Management](../references/owasp-session-management.md)

### CAPTCHA / anti-bot diagnostics

- [Browserbase CAPTCHA and Identity Trend 2026](../references/browserbase-antibot-identity-2026.md)
- [Browserbase Agent Identity 2026](../references/browserbase-agent-identity-2026.md)
- [Browserless CAPTCHA Handling](../references/browserless-captcha-handling.md)

Keep these as diagnostic/continuity references. Do not turn them into an identity-rotation or access-
evasion playbook.

### Payment and later hardening

- [EMV 3-D Secure 2.3.1](../references/emvco-3ds-2-3-1.md)
- [PCI DSS](../references/pci-dss.md)
- [OWASP AI Agent Security](../references/owasp-ai-agent-security.md)
- [WebMCP Tool Security](../references/chrome-webmcp-security.md)

### Evaluation methodology

- [BrowserGym](../references/browsergym.md)
- [WebArena-Verified](../references/webarena-verified.md)

## Working architecture hypothesis

Do not freeze this until the first real flow works.

A likely action ladder remains:

```text
official API / typed first-party capability
  -> deterministic DOM
  -> semantic DOM / extraction
  -> vision + DOM
  -> computer use
  -> human
```

But Step 1 intentionally starts in the middle with the smallest proven combination:

```text
managed browser + Live View + deterministic Playwright + human checkpoints
```

The architecture should grow outward only in response to observed needs.

## Current P0

There is exactly one P0 objective:

> Make one real user-authorized browser payment/subscription flow work end to end and verify the
> business result.

Everything else is either a blocker discovered while doing that or a later-stage concern.

## Step 1 verdict

The source collection phase is complete enough for now.

The next useful work is not another reference card or a larger architecture diagram. It is the
smallest executable vertical slice that demonstrates human takeover, same-session automation and
outcome verification on a real target flow.
