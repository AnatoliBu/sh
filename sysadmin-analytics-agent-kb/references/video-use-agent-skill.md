---
artifact_type: reference
authority_tier: Tier B
status: useful-after-audit
source_type: audited-community-repo
topics:
  - agents
  - video-editing
  - ffmpeg
  - skills
domains:
  - video-color
owner: browser-use / video-use
last_checked: 2026-08-17
source_url: https://github.com/browser-use/video-use
---

# Reference: browser-use/video-use Agent Skill

## Authority tier

Tier B

## Status

useful-after-audit

## Owner / maintainer

browser-use.

## URL

https://github.com/browser-use/video-use

## Last checked

2026-08-17

## Scope

Agent workflow patterns for conversational video editing: project memory, EDL persistence,
preview rendering, self-verification, and per-segment FFmpeg grading.

## Why trusted

The repository provides a concrete, inspectable `SKILL.md` and helper-based workflow
designed specifically for coding agents editing video.

## Caveats

It is an implementation pattern, not an authority on color science. Its color-grading
section is intentionally lightweight and should not override ACES/OCIO/ASC guidance.

## Agent-facing artifacts that may consume this reference

- [Video Color Agent](../video-color/agent.md)
- [End-to-End Color Pipeline](../video-color/workflows/end-to-end-color-pipeline.md)

## Extracted rules

- Keep source media untouched and persist project decisions separately.
- Render a cheap preview before the final render.
- Self-verify rendered output rather than trusting command success.
- Persist deterministic edit/grade decisions so iteration does not redo perception.
- Apply grading per shot/segment when continuity requires it.

## Do not use this source for

Camera characterization, display transforms, or scientific white-balance methodology.

## Related references

- [FFmpeg Video Filters](./ffmpeg-video-filters.md)
- [Vex Video Editing Agent](./vex-video-editing-agent.md)
- [VEAC Video Editing as Code](./veac-video-editing-as-code.md)
