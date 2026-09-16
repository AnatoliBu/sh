---
artifact_type: skill
status: foundation
domain: browser-automation
---

# Skill: Browser Automation Architecture

## Purpose

Choose the smallest browser architecture that remains reliable under real authentication, UI
variation, human handoff, and provider failure.

## Reference links

Authority references:

- [Playwright Documentation](../../references/playwright-docs.md)
- [Browserbase Live View and Session Contexts](../../references/browserbase-live-view-contexts.md)
- [Browserless Hybrid Automation](../../references/browserless-hybrid-automation.md)
- [Steel Browser Documentation](../../references/steel-browser-docs.md)
- [Browser Use](../../references/browser-use-repo.md)
- [Stagehand](../../references/browserbase-stagehand.md)

## Decision hierarchy

### 1. Start deterministic

If the workflow is known, encode it as a state machine over Playwright:

```text
state -> allowed actions -> expected post-condition -> timeout/failure state
```

Do not start with a free-form agent because the page contains HTML.

### 2. Add semantic automation only at unstable edges

Use Stagehand/browser-use/another agentic layer when the next action depends on page meaning or an
interface changes too often for selectors to be economical.

Keep the boundary narrow:

```text
deterministic -> semantic observe/act -> assert deterministic state -> deterministic
```

For irreversible actions, the final submit/cancel/upgrade/delete step stays explicit.

### 3. Add managed browser infrastructure when the product needs it

A cloud browser is justified by one or more of:

- user-facing live takeover;
- remote execution independent of the user's machine;
- persistent profiles/session contexts;
- fleet concurrency;
- centralized observability/replays;
- provider-managed browser/proxy/CAPTCHA facilities;
- reproducible runtime images.

Keep an internal provider interface such as:

```text
createSession()
connectCDP()
getLiveView()
saveOrDiscardProfile()
closeSession()
```

Merchant flows must not call vendor APIs directly.

### 4. Treat identity as part of workflow state

For authenticated consumer accounts, stable account/browser/network continuity is usually more
important than maximizing fingerprint variation.

Choose explicitly:

```text
EPHEMERAL  one-off sensitive flow, destroy state at end
PERSISTENT account repeatedly used and user consented to retained session state
```

Do not silently convert an ephemeral login into long-lived stored cookies.

## Provider selection

Evaluate Browserbase, Browserless, Steel, or another provider against a fixed scenario suite rather
than feature-page checkboxes:

- user login + MFA handoff;
- return from handoff into Playwright;
- iframe/payment UI;
- popup/new-tab behavior;
- download/upload if needed;
- failure evidence;
- session timeout behavior;
- target regions and latency;
- concurrency and cost at expected workload.

## Output

Return an architecture decision record containing:

```text
workflow classes
deterministic vs agentic boundaries
browser provider abstraction
session/profile policy
human-handoff mechanism
observability policy
sensitive-data boundaries
provider benchmark plan
known failure modes
```

## Anti-patterns

- one universal autonomous browser agent for every merchant;
- provider SDK calls spread through business logic;
- changing proxy/fingerprint on every run of the same authenticated account;
- selecting a provider only from marketing benchmark claims;
- persisting every browser context by default.
