---
artifact_type: reference
authority_tier: Tier A
status: foundation
source_type: official-docs
topics:
  - video
  - color-management
  - ocio
  - cli
  - aces
domains:
  - video-color
owner: Academy Software Foundation / OpenColorIO
last_checked: 2026-08-17
source_url: https://opencolorio.readthedocs.io/en/stable/guides/using_ocio/tool_overview.html
---

# Reference: OpenColorIO Documentation

## Authority tier

Tier A

## Status

foundation

## Owner / maintainer

Academy Software Foundation / OpenColorIO.

## URL

https://opencolorio.readthedocs.io/en/stable/guides/using_ocio/tool_overview.html

## Last checked

2026-08-17

## Scope

OpenColorIO configuration, color-space transforms, validation, LUT inspection/baking,
and command-line conversion.

## Why trusted

Official documentation for the production color-management library and its CLI tools.

## Caveats

`ociocheck` verifies configuration consistency, not whether a transform is scientifically
correct for a camera. The agent must still establish the source color state.

## Agent-facing artifacts that may consume this reference

- [Video Color Agent](../video-color/agent.md)
- [Color Pipeline Safety](../video-color/rules/color-pipeline-safety.md)
- [Color Correction and Shot Matching](../video-color/skills/color-correction-shot-matching.md)
- [End-to-End Color Pipeline](../video-color/workflows/end-to-end-color-pipeline.md)

## Extracted rules

- Validate OCIO configs before batch work.
- Treat the OCIO config identity/version as part of the render recipe.
- Use explicit input and output color spaces instead of relying on implicit defaults.
- Use `ociochecklut` for LUT parse/evaluation checks and `ociobakelut` only when a
  downstream application requires a baked LUT.
- Prefer the ASWF ACES config rather than inventing a private set of transforms.

## Do not use this source for

Determining an unknown source camera encoding by visual inspection alone.

## Related references

- [ACES 2 Color Management](./aces-2-color-management.md)
- [FFmpeg Video Filters](./ffmpeg-video-filters.md)
