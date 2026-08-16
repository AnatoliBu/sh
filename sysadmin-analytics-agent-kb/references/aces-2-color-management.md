---
artifact_type: reference
authority_tier: Tier A
status: foundation
source_type: official-docs
topics:
  - video
  - color-management
  - aces
  - scene-referred
domains:
  - video-color
owner: Academy of Motion Picture Arts and Sciences / ACES
last_checked: 2026-08-17
source_url: https://docs.acescentral.com/background/about-aces-2/
---

# Reference: ACES 2 Color Management

## Authority tier

Tier A

## Status

foundation

## Owner / maintainer

Academy of Motion Picture Arts and Sciences / ACES.

## URL

https://docs.acescentral.com/background/about-aces-2/

## Last checked

2026-08-17

## Scope

ACES 2 system concepts, scene-referred color management, Input Transforms, working-space
normalization, and Output Transforms.

## Why trusted

This is the official ACES documentation maintained by the organization defining the system.

## Caveats

ACES does not infer unknown camera encoding or repair bad metadata automatically. A correct
Input Transform still depends on knowing the camera/recording state or generating a valid
camera transform.

## Agent-facing artifacts that may consume this reference

- [Video Color Agent](../video-color/agent.md)
- [Color Correction and Shot Matching](../video-color/skills/color-correction-shot-matching.md)
- [End-to-End Color Pipeline](../video-color/workflows/end-to-end-color-pipeline.md)

## Extracted rules

- Separate input normalization, creative grading, and output rendering.
- Prefer a known camera Input Transform over ad-hoc RGB correction for log or wide-gamut media.
- Keep scene-referred processing distinct from display-referred output rendering.
- Record the selected input and output transforms in the reproducible grade manifest.

## Do not use this source for

FFmpeg syntax, object segmentation, stabilization, or camera-profile capture procedure details.

## Related references

- [ACES IDT Capture Guide](./aces-idt-capture-guide.md)
- [OpenColorIO Documentation](./opencolorio-docs.md)
