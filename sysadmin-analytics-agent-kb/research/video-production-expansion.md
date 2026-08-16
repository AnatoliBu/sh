# Research: Video Production Expansion

Last checked: 2026-08-17

## Scope

Extend the existing `video-color` work into adjacent production concerns without turning the agent into a GUI macro recorder:

- editorial / montage;
- compositing / VFX composition;
- animation / motion graphics;
- visual frame composition and perceptual QC.

This document is research-stage only. It is not source of truth and must not be published as an agent domain until the sources below are promoted into curated reference cards.

## Current verdict

The strongest architecture is not one giant video JSON and not one giant FFmpeg filter graph.

Use three related intermediate representations with explicit handoff points:

```text
assets + brief
  -> probe / transcript / shot detection
  -> Timeline IR
  -> Compositing Graph IR
  -> Motion IR
  -> color / finishing hooks
  -> render plan
  -> proxy
  -> technical + perceptual QC
  -> bounded revision
  -> final render
```

### Timeline IR

Owns editorial time and ordering:

- clips and source ranges;
- tracks / layers;
- gaps;
- transitions;
- markers;
- retiming;
- audio/video linkage;
- references to downstream comp or motion assets.

OpenTimelineIO is the best current foundation rather than inventing an incompatible timeline model.

### Compositing Graph IR

Owns spatial image assembly:

- node identity and connections;
- image inputs and outputs;
- transforms;
- alpha / premultiplication state;
- masks and mattes;
- merge operators;
- keying;
- tracking data;
- color-space expectations at node boundaries;
- temporal parameter animation.

OpenFX provides useful host/effect vocabulary. Natron and Blender are candidate execution targets; FFmpeg remains useful for simple deterministic graphs.

### Motion IR

Owns property evolution over time:

- scene hierarchy;
- property path;
- keyframes;
- interpolation;
- easing;
- delay / duration / iteration;
- parenting;
- sequence / parallel composition;
- media and typography references.

The W3C Web Animations timing model and CSS Easing specification are useful renderer-independent semantic references. Blender F-Curves, Remotion, Motion Canvas, Lottie, and OpenUSD are candidate targets or interchange layers depending on the task.

## Authority map

### Foundation / standards candidates

- OpenTimelineIO: editorial timeline interchange and manipulation.
- OpenFX: image-effect host/plugin contract and compositing vocabulary.
- W3C Web Animations: timing model and keyframe/effect semantics.
- W3C CSS Easing: linear, cubic Bézier, and step easing semantics.
- OpenUSD: large-scale 3D scene composition and animated value interchange.
- Blackmagic Design official training: professional editing and Fusion/VFX workflow reference.

### Implementation candidates

- PySceneDetect: shot-boundary analysis and OTIO/EDL output.
- Auto-Editor: audio/motion/subtitle-driven automatic edit labeling and action mapping.
- GStreamer Editing Services: programmable timeline playback/rendering.
- MLT / `melt`: CLI multitrack editing runtime.
- Natron / NatronRenderer: headless node compositing and Python control.
- Blender: 3D, animation, compositor, sequencer, Python, headless rendering.
- Remotion: code-first motion/video rendering with first-party Agent Skills.
- Motion Canvas: code-first explanatory/vector animation with generator-based timing.
- Lottie: JSON vector-animation interchange, with the caveat that its formal spec is still incomplete.

### Perceptual research leads

- NIMA and MUSIQ: image aesthetic/technical quality predictors. Useful only as soft ranking signals.
- EditIQ and other automatic-editing research: candidate generation and continuity constraints, not editorial truth.

## Editorial findings

OpenTimelineIO should be the durable editorial representation. It already models clips, tracks, transitions, markers, metadata, nested compositions, and external media references, and has adapter support for common editorial formats.

Automatic editing should be treated as a proposal generator. PySceneDetect can find structural cuts. Auto-Editor demonstrates a useful label/action model where moments are classified from audio, motion, subtitles, or combinations and mapped to cut/keep/speed/zoom-like actions. Neither is a substitute for narrative judgement.

Recommended agent loop:

```text
analyze footage
  -> annotate shots / transcript / audio activity / motion
  -> generate editorial candidates
  -> materialize candidates as Timeline IR
  -> render low-cost proxies
  -> inspect cut boundaries, continuity, pacing, dialogue, audio
  -> choose / revise
  -> persist winning timeline
```

Do not recursively edit from the previous rendered output. The timeline must remain the source of truth.

## Compositing findings

Treat technical compositing separately from visual composition.

Technical compositing can be formalized well as a directed graph. OpenFX standardizes useful contexts such as generator, filter, transition, paint, general effect, and retimer, as well as clips, parameters, pixel components, bit depths, and premultiplication state.

Natron is particularly interesting for an agent because its engine is designed to run headlessly through `NatronRenderer`, shares the same engine as the GUI, exposes Python, and hosts OpenFX plugins. Blender becomes the stronger target when 3D geometry, cameras, particles, lighting, or USD enter the task.

## Animation findings

Animation is more deterministic than editorial taste and therefore a good candidate for a strict IR.

A useful semantic model is:

```text
time
  -> iteration progress
  -> easing / interpolation
  -> property value
  -> scene hierarchy
  -> rendered frame
```

W3C Web Animations explicitly separates timing from animation effects and is stateless with respect to previous frames, which is valuable for seeking, deterministic preview, and distributed rendering.

Remotion deserves a close audit because it now ships first-party Agent Skills. Its `remotion-markup` guidance explicitly drives animation from frame/time, uses interpolation and Bézier/spring timing, models `from`, duration and trimming, and preserves code as the editable source. Those are good harness patterns even if Remotion is not the universal backend.

Motion Canvas is narrower but attractive for explanatory graphics and music/voice-synchronized vector animation. Blender remains the general 2.5D/3D animation target. OpenUSD should enter only when scene assembly or 3D interchange justifies its complexity.

## Visual frame composition findings

Do not encode aesthetic heuristics as hard rules.

A frame-composition evaluator may use evidence such as:

- face / subject bounds;
- gaze direction and available look room;
- subject clipping at frame edges;
- saliency distribution;
- horizon / dominant-line geometry;
- text-safe regions;
- motion direction;
- shot-size continuity;
- aesthetic-quality models.

These should produce diagnostics and candidate scores, not a binary pass/fail. Models such as NIMA or MUSIQ are imperfect proxies for aggregate human ratings and may be used only as one term in a ranking function. Final acceptance requires visual inspection or explicit user intent.

## Candidate skill set

### Editorial

- `footage-inventory-and-annotation`
- `rough-cut-generation`
- `dialogue-editing`
- `shot-selection-and-ordering`
- `pacing-and-continuity-qc`
- `timeline-conform-and-export`

### Compositing

- `compositing-graph-planning`
- `keying-matte-roto`
- `tracking-and-matchmove`
- `layer-integration-qc`
- `headless-comp-render`

### Animation / motion

- `motion-design-planning`
- `keyframe-and-easing-design`
- `typography-and-layout-animation`
- `audio-synchronized-motion`
- `2d-motion-render`
- `3d-animation-render`

### Cross-domain

- `video-production-orchestrator`
- `proxy-and-self-qc`
- `visual-composition-review`

## Candidate contract shapes

### Editorial decision

```json
{
  "shot": "shot-014",
  "source_range": [123.4, 131.8],
  "timeline_start": 48.2,
  "role": "dialogue-reaction",
  "confidence": 0.82,
  "reasons": ["speaker-reaction", "continuity"],
  "alternatives": ["shot-011", "shot-017"]
}
```

### Motion property

```json
{
  "target": "title.opacity",
  "keyframes": [
    {"t": 0.0, "value": 0.0},
    {"t": 0.45, "value": 1.0}
  ],
  "easing": {"type": "cubic-bezier", "value": [0.16, 1.0, 0.3, 1.0]}
}
```

### Compositing node

```json
{
  "id": "merge-foreground",
  "type": "merge",
  "inputs": {"A": "background", "B": "foreground", "mask": "person-matte"},
  "alpha": "premultiplied",
  "working_space": "scene-linear"
}
```

These are research sketches, not schemas yet.

## Rejected directions

- Raw FFmpeg command text as the project source of truth.
- One opaque model call that chooses cuts and immediately renders final media.
- A universal aesthetic score that automatically approves framing.
- Treating `rule of thirds`, golden ratio, or any single composition heuristic as a hard quality gate.
- Making Remotion, Blender, Natron, or any other execution engine the semantic project format.
- Mixing source interpretation, compositing, creative look, motion, and encode settings into one undifferentiated effect list.

## Next research questions

1. Extract editorial continuity and pacing heuristics from professional training sources and peer-reviewed editing research.
2. Evaluate OTIO limitations around effects, speed ramps, audio automation, and downstream comp references.
3. Decide whether the project needs an OTIO extension schema or a sibling manifest.
4. Compare Natron vs Blender compositor vs FFmpeg for deterministic headless VFX graphs.
5. Audit Remotion first-party skills beyond `remotion-markup`, especially render, multimedia, captions, and interactivity.
6. Define a minimal Motion IR that compiles cleanly to both Remotion and Blender.
7. Research robust temporal perceptual metrics for animation and edit quality, not just single-frame aesthetics.
8. Build eval cases before promoting this research into live skills.

## Source index

- https://opentimelineio.readthedocs.io/en/latest/
- https://www.blackmagicdesign.com/products/davinciresolve/training
- https://www.scenedetect.com/docs/latest/
- https://auto-editor.com/docs/
- https://gstreamer.freedesktop.org/documentation/gst-editing-services/
- https://www.mltframework.org/docs/melt/
- https://openfx.readthedocs.io/en/main/
- https://natron.readthedocs.io/en/rb-2.6/
- https://docs.blender.org/
- https://www.w3.org/TR/web-animations-1/
- https://www.w3.org/TR/css-easing-2/
- https://openusd.org/release/
- https://lottiefiles.github.io/lottie-spec/
- https://www.remotion.dev/
- https://github.com/remotion-dev/remotion/tree/main/packages/skills/skills
- https://motioncanvas.io/docs/
- https://research.google/pubs/nima-neural-image-assessment/
- https://research.google/pubs/musiq-multi-scale-image-quality-transformer/
- https://arxiv.org/abs/2502.02172
