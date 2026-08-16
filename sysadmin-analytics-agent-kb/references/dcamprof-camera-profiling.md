---
artifact_type: reference
authority_tier: Tier B
status: useful-after-audit
source_type: specialist-project-docs
topics:
  - camera-profiling
  - dcamprof
  - dcp
  - icc
domains:
  - video-color
owner: DCamProf / Anders Torger
last_checked: 2026-08-17
source_url: https://torger.se/anders/dcamprof.html
---

# Reference: DCamProf Camera Profiling

## Authority tier

Tier B

## Status

useful-after-audit

## Owner / maintainer

DCamProf / Anders Torger.

## URL

https://torger.se/anders/dcamprof.html

## Last checked

2026-08-17

## Scope

Command-line camera characterization and DCP/ICC profile generation from target
measurements or spectral sensitivity data.

## Why trusted

DCamProf is a specialist profiling tool with detailed technical documentation and a
repeatable CLI workflow. It is useful when the output target is DCP/ICC rather than an
ACES-native Input Transform.

## Caveats

This is specialist project documentation rather than a current industry standard.
The capture methodology should be grounded in a stronger authority such as the ACES
capture guide, and the generated profile must be independently validated.

## Agent-facing artifacts that may consume this reference

- [Camera Profiling](../video-color/skills/camera-profiling.md)

## Extracted rules

- Separate target measurement/capture from profile fitting.
- Preserve the source target measurements and profile-generation command line.
- Validate the generated profile against held-out images and neutral/saturated patches.
- Do not use a fitted profile merely because the command completed successfully.

## Do not use this source for

Creative grading or as a replacement for ACES/OCIO workflow definitions.

## Related references

- [ACES IDT Capture Guide](./aces-idt-capture-guide.md)
