---
artifact_type: workflow
status: foundation
domain: browser-automation
---

# Workflow: Build and Harden a Browser Flow

## Reference links

Authority references:

- [Playwright Documentation](../../references/playwright-docs.md)
- [Browserbase Live View and Session Contexts](../../references/browserbase-live-view-contexts.md)
- [Steel Agent Skills](../../references/steel-agent-skills.md)
- [PCI DSS](../../references/pci-dss.md)

## Sequence

### 1. Define the business state machine

Write supported start states, terminal states, and irreversible transitions before selectors.

### 2. Record a human happy path

Capture URLs, page states, popups/frames, auth/MFA points, and success evidence. Do not record
secrets.

### 3. Implement deterministic Playwright

Use semantic locators, auto-waiting, scoped assertions, and explicit post-conditions.

### 4. Introduce handoff

Add a provider-independent `requestHumanControl()` boundary for login/MFA/consent/3DS.

### 5. Add semantic/agentic help only where measured

If a particular page remains selector-fragile, test Stagehand/browser-use there. Bound it to a small
action set and immediately return to deterministic assertions.

### 6. Add sensitive-data controls

Define secret source, redaction, recording policy, session TTL, and cleanup before wiring payment
credentials.

### 7. Add failure taxonomy and reconciliation

Map each exception/terminal page to a typed result. For ambiguous irreversible actions, inspect
merchant state before retrying.

### 8. Benchmark browser providers with the real scenario suite

Run the same flows on candidate cloud browsers. Compare success rate, handoff latency, debugging
evidence, session continuity, region support, concurrency, and cost.

### 9. Freeze regression scenarios

At minimum cover fresh/authenticated account, human takeover, iframe/popup, provider timeout,
changed UI copy, rejection, and ambiguous final-submit result.

### 10. Production gate

Ship only when:

```text
happy path repeats cleanly
failure states are typed
no blind irreversible retries
secrets absent from artifacts
human handoff works
cleanup is deterministic
provider outage has a defined response
merchant adapter has versioned tests
```
