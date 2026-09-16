---
artifact_type: reference
authority_tier: Tier A
status: useful-after-audit
source_type: official-docs
topics:
  - browser-automation
  - computer-use
  - vision
  - prompt-injection
domains:
  - browser-automation
owner: Google Gemini API
last_checked: 2026-09-16
source_url: https://ai.google.dev/gemini-api/docs/computer-use
---

# Reference: Gemini Computer Use

## Authority tier

Tier A

## Status

useful-after-audit

## Owner / maintainer

Google Gemini API

## URL

https://ai.google.dev/gemini-api/docs/computer-use

## Last checked

2026-09-16

## Scope

Official Gemini Computer Use loop for browser/mobile/desktop control from screenshots, including
action intents, configurable safety policy and opt-in screenshot prompt-injection detection.

## Why trusted

Primary Google API documentation for Gemini Computer Use.

## Caveats

Google labels Computer Use as Preview and warns against unsupervised critical decisions, sensitive
data and hard-to-reverse actions. Prompt-injection detection is an additional signal, not a complete
security boundary.

## Extracted rules

- Keep screenshot/action execution in a sandbox with explicit navigation/action policy.
- Enable available prompt-injection detection, but still enforce privileges and high-impact gates
  outside the model.
- Require human or independent deterministic validation for financial and irreversible actions.
- Record model-proposed action, executed action and resulting state separately.

## Do not use this source for

Assuming model safety policy makes payment automation safe without application-level controls.

## Related references

- [OWASP AI Agent Security](./owasp-ai-agent-security.md)
- [Stagehand Agent Modes](./stagehand-agent-modes.md)
