---
artifact_type: reference
authority_tier: Tier A
status: foundation
source_type: industry-body
topics:
  - video
  - color-grading
  - asc-cdl
  - interchange
domains:
  - video-color
owner: American Society of Cinematographers
last_checked: 2026-08-17
source_url: https://theasc.com/articles/continuity-of-mission
---

# Reference: ASC Color Decision List

## Authority tier

Tier A

## Status

foundation

## Owner / maintainer

American Society of Cinematographers.

## URL

https://theasc.com/articles/continuity-of-mission

## Last checked

2026-08-17

## Scope

Portable primary color-correction intent and the role of ASC CDL as a cross-platform
RGB grading interchange mechanism.

## Why trusted

ASC developed the Color Decision List through its technology work and documents its role
as a widely adopted cross-platform grading language.

## Caveats

ASC CDL is intentionally limited to primary corrections. It is not a replacement for
full color management, camera characterization, spatial masks, keys, or arbitrary curves.

## Agent-facing artifacts that may consume this reference

- [Color Correction and Shot Matching](../video-color/skills/color-correction-shot-matching.md)
- [End-to-End Color Pipeline](../video-color/workflows/end-to-end-color-pipeline.md)

## Extracted rules

- Use CDL-like slope/offset/power/saturation when a portable primary correction is enough.
- Store a creative primary grade separately from the source and output color transforms.
- Do not force secondary or spatial corrections into a CDL representation.

## Do not use this source for

Camera profiling, segmentation, stabilization, or arbitrary LUT authoring.

## Related references

- [ACES 2 Color Management](./aces-2-color-management.md)
- [OpenColorIO Documentation](./opencolorio-docs.md)
