# Research: Browser Automation Golden-Path E2E PoC

Last checked: 2026-09-16

## Goal

Prove the smallest real vertical slice before introducing abstractions or production hardening.

Success means one user can open a managed browser session, log in, hand the same session to
Playwright, reach billing/checkout, complete any interactive checkpoint with human takeover, perform
one supervised payment/subscription action, and verify the actual business outcome.

This is a functional PoC, not a production design.

## First provider

Start with **Browserbase** because the existing reference set already covers managed browser sessions,
Live View and session contexts, and because the PoC needs same-session human/automation handoff more
than it needs an agent framework.

References:

- [Browserbase Live View and Session Contexts](../references/browserbase-live-view-contexts.md)
- [Playwright Documentation](../references/playwright-docs.md)

Do not create a provider abstraction yet. If Browserbase blocks the golden path for a concrete reason,
record the failure and replay the same scenario on Browserless next.

## First controller

Use direct **Playwright**.

Do not use Stagehand, Browser Use, computer-use, WebMCP or a generic agent in the first run unless a
specific page interaction cannot be made reliable with ordinary Playwright.

Reason: the first experiment should test browser-session mechanics and merchant behavior, not model
behavior.

## Minimal components

```text
client
  Telegram button or tiny web page

backend
  create session
  expose temporary user-facing Live View link
  keep session id + PoC state
  attach Playwright to the same session
  close session

Browserbase
  Chromium session
  Live View
  Playwright/CDP connection

target merchant
  real login
  billing / checkout
  real or tightly controlled low-value action
```

No queue, Redis, workflow engine, provider adapter, persistent profile database or multi-tenant
orchestration is required for the first successful run.

## State machine

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

### CREATED

Backend creates one browser session and stores:

```text
poc_run_id
provider_session_id
state
created_at
current_url (diagnostic only)
last_error
```

### HUMAN_LOGIN

User receives the Live View URL and logs in manually.

The PoC must support ordinary login and one interactive authentication checkpoint if the merchant
requests it. The backend does not need to understand the user's credentials.

Transition criterion:

- user signals `I am logged in`, or
- automation observes a known authenticated page marker.

For the first implementation, explicit user confirmation is acceptable and simpler.

### AUTOMATION_ACTIVE

Playwright attaches to the already running Browserbase session.

Verify immediately that it is the same authenticated browser by checking one harmless authenticated
state marker before navigating elsewhere.

Then automate only the known merchant path to billing/checkout.

### CHECKOUT_READY

Automation stops before the consequential final action and verifies the visible checkout state:

```text
expected merchant/account
expected plan/product
expected amount/currency when exposed
payment form or stored-method state
```

The PoC does not need a universal checkout parser. Hard-code one merchant-specific verifier.

### HUMAN_CONFIRM_OR_CHALLENGE

For the first real run, keep the final irreversible submit human-supervised.

Possible patterns:

- human clicks the final button in Live View;
- automation clicks only after an explicit `confirm` command from the user;
- if 3DS/CAPTCHA/MFA appears, human takes control in the same browser session and completes it.

The important property is session continuity, not who physically performs the final click.

### VERIFYING_OUTCOME

Do not declare success from the click itself.

Check at least one merchant business-state signal after submit, for example:

```text
subscription status == active
plan name changed
receipt/order id appeared
billing page shows successful payment
```

Prefer two independent signals when easy, but one strong merchant-specific signal is enough for the
first PoC.

### AMBIGUOUS

Enter `AMBIGUOUS` when the submit may have happened but the outcome is unknown, for example:

- timeout after submit;
- browser crash immediately after submit;
- network loss during redirect;
- 3DS returns to an unexpected state.

In this state, **do not submit again automatically**. Re-open or refresh the merchant/account state
and determine whether the action already completed.

This rule is required for functional correctness even in a prototype.

### CLOSED

Close the provider session after success, known failure or manual stop.

For the first PoC, ephemeral sessions are enough.

## Minimal endpoints / commands

The exact framework is unimportant. A tiny API can be enough:

```text
POST /poc/start
  -> create browser session
  -> return run_id + live_view_url

POST /poc/{run_id}/resume
  -> attach Playwright
  -> verify authenticated state
  -> navigate to checkout
  -> stop at CHECKOUT_READY

POST /poc/{run_id}/confirm
  -> perform or allow final action
  -> verify outcome

POST /poc/{run_id}/close
  -> close session

GET /poc/{run_id}
  -> current state + diagnostic message
```

A Telegram bot may simply wrap these endpoints later. Do not make Telegram part of the first proof if
it slows browser work.

## Merchant adapter: deliberately ugly first version

For one target merchant, a single module is enough:

```text
merchant/
  target.ts
```

with functions roughly equivalent to:

```text
isLoggedIn(page)
openBilling(page)
prepareCheckout(page)
verifyCheckout(page)
submit(page)
verifyOutcome(page)
```

Selectors, URLs and plan expectations may be hard-coded for the experiment.

The purpose is to discover the real interface before designing a generic `MerchantAdapter`.

## What to record during every run

Capture a small experiment log, not a production audit system:

```text
run id
timestamps per state
provider session id
merchant
final result
failure stage
challenge type if any
number of human handoffs
manual notes
```

Optional during debugging:

```text
Playwright trace
provider session replay
screenshots at state transitions
```

Do not deliberately place passwords, TOTP seeds, PAN or CVV into those artifacts.

## Experiment sequence

### Run A — no money

Prove:

```text
create session
-> Live View works
-> user logs in
-> Playwright attaches to same authenticated session
-> reaches billing
-> returns control to human
-> closes cleanly
```

No purchase.

### Run B — checkout preparation

Prove:

```text
all of Run A
-> automation reaches exact checkout state
-> verifies plan/amount/account
-> stops before final submit
```

No purchase if the merchant allows reaching this point safely.

### Run C — one supervised real action

Use a cheap, controlled transaction/subscription that the user explicitly approves.

Prove:

```text
all of Run B
-> final submit
-> challenge/handoff if needed
-> business outcome verification
-> clean close
```

### Run D — controlled failure

Intentionally interrupt once before or around a non-destructive stage to prove the state machine does
not silently continue from stale assumptions.

Do not manufacture an ambiguous real charge merely to test ambiguity. That scenario can be simulated
until a naturally occurring timeout/failure provides evidence.

## PoC acceptance criteria

The first milestone is accepted when all of the following are demonstrated on the same target flow:

- user can open Live View from the intended client device;
- user can authenticate;
- Playwright resumes in the same authenticated browser session;
- deterministic automation reaches checkout;
- control can be returned to the human without losing the session;
- one supervised final action succeeds;
- the backend verifies the business outcome;
- browser session closes intentionally;
- a failed pre-submit run produces a clear failure state instead of random retry behavior.

No success-rate target is required yet. One complete run proves feasibility; repeated runs belong to
Step 2.

## Questions Step 1 should answer empirically

Record answers instead of designing around guesses:

1. Is Live View usable on iPhone/mobile Safari?
2. Does switching between human and Playwright introduce focus/input races?
3. Does the merchant react differently to the managed browser environment?
4. Does login remain valid when automation attaches/resumes?
5. Are payment fields normal DOM, cross-origin iframe or hosted checkout?
6. Does 3DS open inline, iframe, popup, redirect or external app?
7. What exact page/account state proves success?
8. What provider artifacts are useful for debugging the flow?
9. Which part of the golden path is actually brittle?

The answers drive Step 2 and later architecture.

## Explicitly postponed

Do not spend Step 1 time on:

- provider-neutral interfaces;
- persistent user profiles;
- distributed workers;
- retries/backoff framework;
- automatic provider failover;
- CAPTCHA vendor comparison;
- stealth/fingerprint tuning;
- semantic/vision agents;
- generic WebMCP support;
- secret vault architecture;
- encryption/retention/audit framework;
- full payment compliance design;
- prompt-injection defense framework;
- benchmark dashboards.

If one of these becomes necessary to make the first vertical slice work, add only the smallest piece
needed and record why it became a real requirement.

## Next decision after the first successful run

Do not immediately package the PoC as a skill.

Review the run evidence and classify every observed problem as one of:

```text
merchant-specific
browser/provider-specific
human-handoff-specific
authentication-specific
checkout/payment-specific
controller/Playwright-specific
```

Step 2 should address the dominant real failures, not the largest theoretical risk list.
