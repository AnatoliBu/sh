---
artifact_type: workflow
status: foundation
domain: video-color
---

# Workflow: End-to-End Video Color Pipeline

## Reference links

Authority references:

- [ACES 2 Color Management](../../references/aces-2-color-management.md)
- [ACES IDT Capture Guide](../../references/aces-idt-capture-guide.md)
- [OpenColorIO Documentation](../../references/opencolorio-docs.md)
- [FFmpeg Video Filters](../../references/ffmpeg-video-filters.md)
- [ASC Color Decision List](../../references/asc-color-decision-list.md)
- [browser-use/video-use Agent Skill](../../references/video-use-agent-skill.md)
- [Vex Video Editing Agent](../../references/vex-video-editing-agent.md)
- [VEAC Video Editing as Code](../../references/veac-video-editing-as-code.md)

## Goal

Turn source footage plus a color intent into a deterministic grade recipe and a verified
render without relying on GUI automation.

## Flow

```text
1. INVENTORY
   ffprobe every source
   save tags, codec, bit depth, fps, rotation, duration

2. TRUST ASSESSMENT
   decide what source color metadata is known vs assumed

3. NORMALIZE
   known log/wide-gamut -> explicit OCIO/ACES input transform
   simple known Rec.709 -> preserve/display-referred path as appropriate

4. SEGMENT
   detect cuts / define shots
   group related shots into scenes/setups

5. ANALYZE
   sample representative frames
   luma/channel/saturation/clipping + neutral/skin evidence

6. CORRECT
   exposure -> WB -> levels -> contrast/curve -> saturation
   use bounded candidates, including no-op

7. MATCH
   compare shots to a stable scene reference
   penalize unnecessary inter-shot discontinuity

8. SECONDARIES
   only when global correction is insufficient
   create/persist masks and tracked decisions

9. LOOK
   apply creative CDL/LUT/CLF/explicit grade separately from correction

10. PREVIEW
    compile Grade IR -> FFmpeg/OCIO pipeline
    render stills or low-cost proxy

11. QC LOOP
    scopes + metrics + rendered visual review
    fix -> rerender
    cap autonomous retries; surface unresolved uncertainty

12. OUTPUT
    explicit output transform
    explicit encode/pixel format/color tags

13. VERIFY
    ffprobe final
    inspect boundaries, highlights, skin, masks, representative frames

14. PERSIST
    save approved grade-plan.json and QC evidence
```

## Grade IR boundary

The model should edit a constrained grade plan, not hand-author an opaque shell pipeline
on every iteration.

Recommended high-level operations:

```text
InputTransform
Exposure
WhiteBalance
Levels
Curve
CDL
Saturation
LUT/CLF
MaskSecondary
Stabilize
OutputTransform
Encode
```

Each operation should have typed parameters, bounds, source range, and provenance.

The compiler may target:

```text
FFmpeg filter graphs
OpenColorIO transforms
VapourSynth scripts
Natron render graphs
```

The selected backend is an implementation detail. The grade intent is not.

## Candidate loop

For ambiguous automatic correction:

```text
analyze shot
  -> candidate no-op
  -> conservative candidate
  -> nominal candidate
  -> optional stronger candidate
  -> render representative frames
  -> score technical damage + reference distance + continuity
  -> visual/perceptual check
  -> persist winner
```

The final render reuses the winner. It does not ask the model to choose again.

## White-balance policy

Priority:

```text
known camera/lighting metadata + valid transform
  > measured grey/neutral target
  > credible neutral-region estimate
  > bounded statistical estimate
  > no automatic WB
```

For mixed illuminants, prefer a local/masked solution or preserve the lighting intent
instead of forcing one global neutral.

## Profiling branch

If the task is camera characterization rather than shot correction:

```text
stop normal grade flow
  -> controlled ACES capture procedure
  -> generate IDT/profile
  -> validate
  -> version transform
  -> return to normal pipeline with known Input Transform
```

## Go/no-go checks

Before final render:

- input color state is explicit or uncertainty is documented;
- no unexplained transform is baked into a creative LUT;
- shot-match decisions are stable;
- clipping did not materially worsen without intent;
- masks pass temporal/edge review;
- output transform and tags match delivery;
- deterministic recipe can rebuild the render.

## Third-party skill adoption

Use community skills selectively:

| Source | Take | Do not delegate |
|---|---|---|
| `browser-use/video-use` | project memory, preview, self-QC | color science |
| `claude-mods` FFmpeg ops | probe-first, quality gates | source transform truth |
| `Vex` | shot candidates, continuity scoring concepts | standards decisions |
| `VEAC` | declarative IR/compiler shape | grade methodology |

This hybrid is stronger than installing one end-to-end video skill unchanged.
