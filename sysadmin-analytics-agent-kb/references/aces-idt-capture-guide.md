---
artifact_type: reference
authority_tier: Tier A
status: foundation
source_type: official-docs
topics:
  - video
  - camera-profiling
  - aces
  - idt
  - colorchecker
domains:
  - video-color
owner: Academy of Motion Picture Arts and Sciences / ACES
last_checked: 2026-08-17
source_url: https://docs.acescentral.com/system-components/input-transforms/capture-guide/
---

# Reference: ACES IDT Capture Guide for Prosumer Cameras

## Authority tier

Tier A

## Status

foundation

## Owner / maintainer

Academy of Motion Picture Arts and Sciences / ACES.

## URL

https://docs.acescentral.com/system-components/input-transforms/capture-guide/

## Last checked

2026-08-17

## Scope

Controlled capture procedure for generating camera Input Transforms from grey-card and
24-patch ColorChecker material.

## Why trusted

This is the official ACES camera-capture procedure. It specifies the target, lighting,
camera setup, exposure bracketing, measurements, and metadata required for defensible
profiling.

## Caveats

The procedure is intentionally meticulous. It is not a shortcut for deriving a camera
profile from arbitrary production footage. A poorly captured target can create a worse
transform than using no custom transform.

## Agent-facing artifacts that may consume this reference

- [Camera Profiling](../video-color/skills/camera-profiling.md)
- [End-to-End Color Pipeline](../video-color/workflows/end-to-end-color-pipeline.md)

## Extracted rules

- Use a spectrally neutral grey card and a 24-patch ColorChecker under controlled,
  repeatable light.
- Disable automatic exposure, automatic white balance, in-camera LUTs, sharpening,
  and other processing that changes the measured signal.
- Record the intended camera encoding at base ISO and fixed aperture/ISO.
- Capture a bracketed response around nominal exposure, at least from -3 to +3 stops
  when practical.
- Log camera, lens, exposure, white-balance, lighting, and measurement metadata.
- Validate a generated transform on material that was not used to fit it.

## Do not use this source for

Creative look design, arbitrary shot matching, or automatic white balance on mixed-light
production footage.

## Related references

- [ACES 2 Color Management](./aces-2-color-management.md)
- [DCamProf Camera Profiling](./dcamprof-camera-profiling.md)
