---
artifact_type: reference
authority_tier: Tier A
status: useful-after-audit
source_type: official-docs
topics:
  - browser-automation
  - stagehand
  - dom
  - computer-use
  - vision
domains:
  - browser-automation
owner: Browserbase Stagehand
last_checked: 2026-09-16
source_url: https://docs.stagehand.dev/v3/basics/agent
---

# Reference: Stagehand Agent Modes

## Authority tier

Tier A

## Status

useful-after-audit

## Owner / maintainer

Browserbase Stagehand

## URL

https://docs.stagehand.dev/v3/basics/agent

## Last checked

2026-09-16

## Scope

Stagehand agent execution modes: DOM, hybrid DOM+coordinate actions, and screenshot-based Computer
Use Agent mode, plus mode-specific capability differences.

## Why trusted

Official Stagehand documentation.

## Caveats

Hybrid and CUA behavior depends strongly on model capability and current Stagehand version. Some
features are experimental.

## Extracted rules

- Choose the least agentic modality that reliably completes the step: deterministic DOM first,
  semantic DOM next, hybrid vision/DOM when necessary, full computer-use last.
- Keep model-dependent coordinate actions away from irreversible actions unless independently
  validated.
- Measure success and cost per mode on the project's actual merchants rather than assuming a mode is
  globally superior.

## Do not use this source for

Claims that visual computer-use is more reliable than deterministic browser APIs.

## Related references

- [Stagehand](./browserbase-stagehand.md)
- [Stagehand v4 2026](./stagehand-v4-2026.md)
- [Gemini Computer Use](./gemini-computer-use.md)
