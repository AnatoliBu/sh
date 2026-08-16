# Source Review: Animation and Motion

Last checked: 2026-08-17

## Sources reviewed

- W3C Web Animations: https://www.w3.org/TR/web-animations-1/
- W3C CSS Easing Functions Level 2: https://www.w3.org/TR/css-easing-2/
- Blender manual/API: https://docs.blender.org/
- OpenUSD: https://openusd.org/release/
- Lottie specification: https://lottiefiles.github.io/lottie-spec/
- Remotion: https://www.remotion.dev/
- Remotion first-party Agent Skills: https://github.com/remotion-dev/remotion/tree/main/packages/skills/skills
- Motion Canvas: https://motioncanvas.io/docs/

## Claimed purpose

Define a portable, deterministic motion model that can be authored by an agent, previewed cheaply, and compiled to code-first 2D or general 3D animation engines.

## Authority level

Mixed.

- W3C Web Animations and CSS Easing: foundation candidates for time/keyframe/easing semantics.
- OpenUSD: foundation candidate for complex 3D scene and animation interchange.
- Lottie: useful formal interchange candidate, but its specification is still work in progress.
- Blender: strong general animation execution target.
- Remotion: strong code-first video/motion implementation and agent-harness reference.
- Motion Canvas: strong specialist implementation for explanatory/vector motion.

## Strong findings

### Separate timing from property animation

The W3C Web Animations model explicitly separates a timing model from an animation model. Input time becomes iteration progress; the animation model then maps that progress to property values.

The timing model is described as stateless: an output at a given time does not depend on having rendered previous frames. This is a valuable design property for an agent because seeking, proxy rendering, parallel rendering, and deterministic verification become easier.

### Use explicit easing semantics

CSS Easing Level 2 provides precise semantics for linear piecewise easing, cubic Bézier easing, and step easing. These are more portable than renderer-specific names such as `smooth`, `ease2`, or opaque curve presets.

A Motion IR should therefore persist the actual easing representation, not only a backend-specific preset name.

### Blender

Blender F-Curves model animated properties as values over time, with keyframes and interpolation generating intermediate values. Blender is the strongest general executor in this set when the animation includes cameras, geometry, materials, lighting, 3D constraints, particles, or compositing.

Its Python API and headless render path make it suitable for deterministic agent execution, but Blender project files should not become the only semantic representation if we want portability.

### OpenUSD

OpenUSD provides non-destructive scene composition and time-sampled animated values for large 3D pipelines. Layer offsets support simple retiming; Value Clips support more flexible sequencing and retiming of animated data.

Use USD only for 3D scene assembly/interchange. A minimal 2D motion title should not require a USD stage.

### Lottie

Lottie is a JSON-based animated vector format with a machine-readable JSON Schema. It is attractive as an interchange/export target for vector motion, but the formal specification states that standardization is still incomplete. It should not define the universal Motion IR.

### Remotion

Remotion is especially relevant because it treats code as the video source and now maintains first-party Agent Skills. The official `remotion-markup` skill contains useful harness rules:

- animation driven from current frame/time rather than browser CSS transitions;
- explicit interpolation and Bézier/spring timing;
- explicit element start, duration, and trimming;
- editable structure preserved in code;
- media, effects, typography, and composition modeled as programmatic components.

These are good implementation patterns. They are not a replacement for renderer-neutral motion semantics.

### Motion Canvas

Motion Canvas uses TypeScript generator functions to describe animation flow and has flow primitives for sequential, parallel, delayed, and looped animation. It has real-time preview and can render image sequences or video through an FFmpeg exporter.

Its own documentation says it is specialized for informative vector animations and voice-over synchronization rather than traditional video editing. That makes it a focused target, not a universal video-production backend.

## Proposed Motion IR

### Core objects

- scene / composition;
- layer / node;
- parent-child hierarchy;
- property path;
- keyframe;
- interpolation mode;
- easing function;
- time range;
- iteration / repeat;
- sequence / parallel group;
- media reference;
- text/typography reference;
- optional expression or procedural generator with bounded semantics.

### Minimal keyframe contract

```json
{
  "target": "headline.position.x",
  "time_unit": "seconds",
  "keyframes": [
    {"t": 0.0, "value": -120},
    {"t": 0.6, "value": 0}
  ],
  "interpolation": "continuous",
  "easing": {
    "type": "cubic-bezier",
    "x1": 0.16,
    "y1": 1.0,
    "x2": 0.3,
    "y2": 1.0
  }
}
```

### Sequence semantics

```text
parallel(A, B)
sequence(A, B)
delay(0.25, A)
repeat(3, A)
trim(A, start, end)
retime(A, scale, offset)
```

The exact schema needs design work, but these operations should have deterministic timing independent of backend.

## Agent flow

```text
brief + assets + duration constraints
  -> identify hierarchy and narrative beats
  -> create motion plan
  -> author Motion IR
  -> compile to Remotion / Motion Canvas / Blender
  -> render selected stills + low-cost motion proxy
  -> inspect timing, hierarchy, legibility, collisions, rhythm, temporal aliasing
  -> bounded revision
  -> final render
```

## What can be reused

- W3C separation of timing and property-value computation.
- Explicit cubic Bézier / linear / step easing semantics.
- Frame/time-addressable rendering.
- Blender F-Curve model for property animation.
- Remotion's code-as-source, explicit timeline, and agent-skill patterns.
- Motion Canvas sequence/parallel generator vocabulary.
- Lottie as a possible vector interchange/export format.
- USD as a possible 3D interchange layer.

## What must not be reused blindly

- CSS or browser runtime animation mechanisms that are not deterministic in offline rendering.
- Backend-specific easing names with unclear mathematical meaning.
- Spring animation without persisted parameters and deterministic evaluation.
- Motion that is accepted from a few still frames only.
- Blender/Remotion project code as the sole cross-tool semantic source.
- Lottie as a promise that every motion feature will round-trip.

## Candidate skills

- `motion-design-planning`
- `keyframe-and-easing-design`
- `typography-and-layout-animation`
- `audio-synchronized-motion`
- `2d-motion-render`
- `3d-animation-render`
- `motion-temporal-qc`

## Verdict

Create a renderer-neutral Motion IR before choosing one favorite engine. Use W3C timing/easing as the semantic baseline, Remotion and Motion Canvas as code-first 2D implementation references, and Blender/OpenUSD when 3D scene complexity warrants them. Audit the remaining first-party Remotion Agent Skills before promoting any Remotion-specific skill into the live KB.
