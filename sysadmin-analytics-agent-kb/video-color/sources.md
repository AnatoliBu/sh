---
artifact_type: index
status: foundation
domain: video-color
---

# Video Color Sources

This domain intentionally separates **authority** from **implementation leads**.

## Foundation authority

1. [ACES 2 Color Management](../references/aces-2-color-management.md)
   - scene-referred pipeline and transform separation.
2. [ACES IDT Capture Guide](../references/aces-idt-capture-guide.md)
   - controlled camera-characterization capture procedure.
3. [OpenColorIO Documentation](../references/opencolorio-docs.md)
   - executable color-management configuration and CLI tooling.
4. [FFmpeg Video Filters](../references/ffmpeg-video-filters.md)
   - deterministic rendering, analysis, masks, scopes, and stabilization.
5. [ASC Color Decision List](../references/asc-color-decision-list.md)
   - portable primary grading representation.

## Specialist implementation sources

- [DCamProf Camera Profiling](../references/dcamprof-camera-profiling.md)
  - useful DCP/ICC profiling path after capture methodology is established.

## Agent-skill implementation leads

- [browser-use/video-use](../references/video-use-agent-skill.md)
  - **adapt** project persistence, preview, and self-verification.
- [claude-mods FFmpeg Operations](../references/claude-mods-ffmpeg-ops.md)
  - **adapt** probe-first execution and quality-gate patterns.
- [Vex](../references/vex-video-editing-agent.md)
  - **mine ideas** for shot-aware candidate generation/evaluation; do not copy code
    without license review.
- [VEAC](../references/veac-video-editing-as-code.md)
  - **mine architecture** for declarative Grade IR -> deterministic backend compilation.

## Trust rule

A community agent skill may define a useful harness pattern but may not override a Tier A
color-management or camera-characterization reference.
