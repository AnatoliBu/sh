---
artifact_type: reference
authority_tier: Tier A
status: foundation
source_type: official-docs
topics:
  - video
  - ffmpeg
  - color-correction
  - masks
  - scopes
  - stabilization
domains:
  - video-color
owner: FFmpeg Project
last_checked: 2026-08-17
source_url: https://ffmpeg.org/ffmpeg-filters.html
---

# Reference: FFmpeg Video Filters

## Authority tier

Tier A

## Status

foundation

## Owner / maintainer

FFmpeg Project.

## URL

https://ffmpeg.org/ffmpeg-filters.html

## Last checked

2026-08-17

## Scope

Deterministic video filtering for levels, curves, color balance/correction, temperature,
LUTs, masked merging, signal analysis, scopes, and stabilization.

## Why trusted

Official FFmpeg filter documentation.

## Caveats

A syntactically valid filter graph does not prove the intended color science. Some filters
operate in specific pixel/color representations, and build-time options may affect
availability.

## Agent-facing artifacts that may consume this reference

- [Video Color Agent](../video-color/agent.md)
- [Color Pipeline Safety](../video-color/rules/color-pipeline-safety.md)
- [Color Correction and Shot Matching](../video-color/skills/color-correction-shot-matching.md)
- [Mask-Assisted Grading](../video-color/skills/mask-assisted-grading.md)
- [End-to-End Color Pipeline](../video-color/workflows/end-to-end-color-pipeline.md)

## Extracted rules

- Probe the input before choosing filters or output tags.
- Keep correction parameters bounded and reproducible.
- Use scopes and `signalstats` as evidence, not as the only acceptance oracle.
- Treat masks as explicit inputs to deterministic compositing such as `maskedmerge`.
- Use the two-pass `vidstabdetect` / `vidstabtransform` workflow when libvidstab is
  available and stabilization is requested.

## Do not use this source for

Inferring camera sensor colorimetry, designing an ACES IDT, or deciding a creative look.

## Related references

- [OpenColorIO Documentation](./opencolorio-docs.md)
- [ASC Color Decision List](./asc-color-decision-list.md)
