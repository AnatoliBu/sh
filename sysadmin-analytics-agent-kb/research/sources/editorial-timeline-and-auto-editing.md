# Source Review: Editorial Timeline and Automatic Editing

Last checked: 2026-08-17

## Sources reviewed

- OpenTimelineIO documentation: https://opentimelineio.readthedocs.io/en/latest/
- Blackmagic Design DaVinci Resolve 20 training: https://www.blackmagicdesign.com/products/davinciresolve/training
- PySceneDetect 0.7 documentation: https://www.scenedetect.com/docs/latest/
- Auto-Editor documentation: https://auto-editor.com/docs/
- GStreamer Editing Services: https://gstreamer.freedesktop.org/documentation/gst-editing-services/
- MLT `melt`: https://www.mltframework.org/docs/melt/

## Claimed purpose

Represent, analyze, generate, exchange, preview, and render editorial decisions without depending on one NLE GUI.

## Authority level

Mixed.

- OpenTimelineIO: foundation candidate for timeline representation.
- Blackmagic official training: professional workflow reference, vendor-specific but respectable.
- PySceneDetect: implementation tool for structural shot detection.
- Auto-Editor: implementation lead for automatic edit labeling/actions.
- GES and MLT: execution/runtime candidates.

## Strong findings

### OpenTimelineIO

OTIO is the clearest current base for a durable Timeline IR. It models editorial cut information rather than rendered pixels and supports clips, time ranges, tracks, transitions, gaps, markers, metadata, nesting, and external media references.

Its adapter model matters because the agent should be able to move a cut between systems instead of making its own format a dead end. Current community adapters cover formats such as AAF, CMX 3600, FCP XML, Maya Sequencer, SVG, and XGES.

OTIO deliberately does not define arbitrary effect behavior. That is a useful boundary: editorial time should not silently become the compositing graph.

### Blackmagic professional training

The current Resolve 20 Editor's Guide is useful as a professional workflow source because it covers multiple editorial forms rather than only UI mechanics: interviews, dramatic scenes, documentary material, music videos, transcription-assisted editing, variable-speed work, audio mixing, and delivery.

This should inform future craft extraction, but vendor shortcuts and GUI instructions must be rewritten into renderer-neutral decisions.

### PySceneDetect

PySceneDetect is useful upstream analysis. Current 0.7 supports multiple detector families, including content, adaptive, histogram, hash, and threshold/fade approaches. It can emit scene data as EDL, FCP, and OTIO.

This makes it a good shot-boundary detector, not an editor.

### Auto-Editor

Auto-Editor contains a strong agent pattern: classify moments with audio, motion, subtitles, or combined expressions, assign labels, then map labels to actions such as cut, keep, speed, or zoom.

Its v3 format demonstrates nonlinear overlapping tracks and transitions, but it should not become our canonical timeline because OTIO is a stronger interchange foundation and Auto-Editor's own formats are implementation-specific. The v3 documentation currently calls the format partially stable.

### GES / MLT

GES provides a programmable timeline abstraction with layers, tracks, clips, trim/move edit operations, preview, render, and smart-render modes. `ges-launch-1.0` can create or load timelines and render them from the command line.

MLT's `melt` is a mature multitrack CLI-oriented editor/runtime. It is worth keeping as a possible compiler target, especially for operations that become awkward as raw FFmpeg graphs.

## What can be reused

- OTIO as the persisted editorial backbone.
- Separate analysis annotations from edit decisions.
- Scene detection as evidence, not authority.
- Auto-Editor's classify -> label -> action pattern.
- Candidate timelines rather than one irreversible automatic cut.
- Proxy render and review before accepting an edit.
- NLE adapters as export boundaries.
- GES/MLT as optional execution targets.

## What must not be reused blindly

- Audio silence equals editorial dead space.
- Motion level equals importance.
- Scene boundary equals desired cut point.
- Automatic edit thresholds as universal defaults.
- Vendor-specific keyboard/UI procedures.
- Auto-Editor timeline formats as the project-wide semantic standard.

## Candidate skill decomposition

- `footage-inventory-and-annotation`
- `rough-cut-generation`
- `dialogue-editing`
- `shot-selection-and-ordering`
- `pacing-and-continuity-qc`
- `timeline-conform-and-export`

## Proposed automatic-edit contract

An analysis system should emit evidence separately from the cut:

```json
{
  "range": [14.2, 18.7],
  "features": {
    "speech": 0.94,
    "motion": 0.31,
    "shot_boundary_before": true,
    "speaker": "A"
  },
  "proposals": [
    {"action": "keep", "confidence": 0.83},
    {"action": "trim-head", "seconds": 0.25, "confidence": 0.61}
  ]
}
```

The editorial planner can then choose among proposals and persist the result into OTIO-like Timeline IR.

## Verdict

Promote OTIO and Blackmagic training to curated references after a focused source-card pass. Keep PySceneDetect, Auto-Editor, GES, and MLT as implementation references. Build the future editing agent around persisted timeline decisions plus candidate/proxy/self-QC loops, not direct render commands.
