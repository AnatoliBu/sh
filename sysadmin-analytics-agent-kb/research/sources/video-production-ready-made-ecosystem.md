# Source Review: Ready-Made Video Agent Ecosystem

Last checked: 2026-08-17

## Scope

Evaluate existing CLI harnesses, agent skills, MCP servers, and semi-finished video-production systems before building new executor layers for editorial, compositing, motion, and finishing.

## Sources reviewed

- CLI-Anything / CLI-Hub: https://github.com/HKUDS/CLI-Anything
- skills.sh video ecosystem: https://skills.sh/
- Everything Claude Code: https://github.com/affaan-m/everything-claude-code
- Remotion first-party skills: https://github.com/remotion-dev/skills
- browser-use/video-use: https://github.com/browser-use/video-use
- Vercel json-render Remotion package: https://github.com/vercel-labs/json-render
- cc-blender-skill: https://github.com/roble3/cc-blender-skill
- MCP directories such as mcp.so / Smithery for discovery only

## Executive verdict

Do not build a complete executor layer from scratch.

There are now several useful layers that can be adopted or wrapped:

1. CLI-Anything already provides stateful agent-oriented CLIs for Kdenlive, Shotcut, Blender, OBS, Audacity, and related creative tools.
2. Remotion maintains first-party agent skills for programmatic video, markup, rendering, captions, multimedia, maps, and interactivity.
3. video-use is a strong end-to-end editorial harness for transcript-first editing, EDL generation, FFmpeg rendering, animation slots, preview, and self-QC.
4. skills.sh contains useful specialist skills, but quality ranges from strong implementation playbooks to generic prompt packs; every non-authoritative skill still needs audit.
5. MCP servers can be useful adapters, but a thin MCP wrapper should not become the semantic source of truth when a stable CLI or project IR exists underneath.

## CLI-Anything

### Kdenlive

`cli-anything-kdenlive` uses a JSON project representation and generates Kdenlive/MLT XML for rendering with melt.

Useful agent-facing operations include:

- media-bin import/list/get;
- timeline tracks, add/remove/move/trim/split clips;
- filters and parameters;
- transitions;
- guides/markers;
- render/export;
- session undo/redo/history;
- machine-readable `--json` output.

This is already close to an executor contract for a Timeline IR compiler target.

### Shotcut

`cli-anything-shotcut` is currently the more interesting editorial harness because it additionally exposes:

- two-step media import and timeline placement;
- keyframed volume envelopes and ducking;
- filter and transition introspection;
- blend modes, opacity, and picture-in-picture operations;
- real preview bundles and live preview sessions;
- preview artifacts including MP4, sampled frames, hero frame, summary JSON, and append-only trajectory history.

This preview protocol is especially reusable for our candidate -> proxy -> inspect -> revise loop.

### Blender

`cli-anything-blender` provides a JSON scene representation compiled through generated `bpy` scripts. It already exposes objects, transforms, materials, modifiers, cameras, lights, keyframes, frame ranges, render settings, undo/redo, JSON output, and preview bundles/live sessions.

It is a strong candidate executor for a future Motion IR / 3D branch, but its JSON scene schema should not automatically become our renderer-neutral Motion IR.

### Caveat

CLI-Anything is implementation infrastructure, not craft authority. Its generated harnesses need capability tests against our required operations, round-trip behavior, timeline semantics, color/alpha provenance, and failure handling.

## Remotion first-party skills

The official Remotion skill collection is substantially more useful than a generic community prompt pack. It covers:

- creation/scaffolding;
- React markup and frame-driven animation;
- rendering;
- captions;
- multimedia operations;
- interactivity;
- maps;
- upgrade/docs guidance.

The markup skill explicitly prefers frame/time-driven interpolation over browser CSS animation, persists timing/trimming, and encourages editable programmatic structure. Reuse these implementation rules for the Remotion compiler target.

Do not let Remotion-specific component semantics define the universal Motion IR.

## video-use

This remains one of the strongest semi-finished editorial systems found.

Useful architecture:

```text
raw media
  -> word-level transcription
  -> packed transcript
  -> human/agent cut strategy
  -> EDL JSON
  -> per-segment processing
  -> concat / overlays / subtitles
  -> preview
  -> cut-boundary self-evaluation
  -> revision
```

Reusable ideas:

- transcript as a compact reasoning view;
- cuts snapped to word boundaries;
- persistent EDL;
- on-demand filmstrip + waveform inspection instead of scanning every frame;
- animation slots delegated to specialist engines;
- explicit hard production-correctness rules separated from artistic taste;
- self-evaluation on rendered output before presenting a preview.

Limitations:

- optimized strongly for speech-driven footage;
- FFmpeg/PIL implementation choices are not universal editorial semantics;
- several exact timing values are implementation/taste examples, not standards;
- should map into OTIO / our Timeline IR rather than replacing it.

## Everything Claude Code and marketplace skills

Everything Claude Code currently exposes relevant skills including:

- `video-editing`;
- `remotion-video-creation`;
- `manim-video`;
- `ui-demo`;
- motion foundations/patterns/advanced;
- Blender motion-state inspection;
- generic verification/eval skills that may be reusable for visual QC loops.

Its video-editing skill is useful as workflow inspiration but is less concrete than video-use or CLI-Anything. Treat it as scaffold/moodboard material, not technical authority.

## Other useful semi-finished candidates

### Vercel json-render + Remotion

A JSON timeline/spec rendered through Remotion is directly relevant to our IR/compiler direction. Audit whether its `TimelineSpec` is expressive enough to reuse or adapt before inventing another 2D timeline schema.

### cc-blender-skill

Interesting specialist skills include animation quality gates, rendering, export, and reference-to-3D workflows. The strongest reusable idea is evidence-based acceptance: contact sheets, structured state, and explicit failure analysis rather than accepting an animation merely because it rendered.

### Claude video editor plugin ecosystems

There are skill packs exposing cut, silence removal, render profiles, MLT/Kdenlive integration, subtitle burning, transcription cleanup, timeline inspection, and project/library management. These are good candidates for extracting narrow procedures, but they need code/license/security review before reuse.

## MCP marketplace verdict

MCP directories are useful for discovery, not for authority scoring.

Observed Remotion MCP wrappers expose render/scaffold/read-write operations, but they generally add less value than first-party Remotion skills plus the underlying CLI/API unless they provide a strong state/preview contract.

Prefer:

```text
stable IR -> deterministic CLI/compiler -> optional MCP adapter
```

instead of:

```text
LLM -> opaque MCP tool collection -> hidden project state
```

## Revised architecture recommendation

Do not write executors first.

```text
Timeline IR / OTIO
  -> adapter: CLI-Anything Shotcut or Kdenlive
  -> adapter: FFmpeg / custom renderer only where needed

Compositing Graph IR
  -> Natron / Blender / FFmpeg targets

Motion IR
  -> Remotion / Motion Canvas / CLI-Anything Blender

shared preview protocol
  -> low-cost render
  -> sampled frames / contact sheet
  -> waveform / scopes / structured facts
  -> self-QC
```

## Spike order

1. Install and capability-test `cli-anything-shotcut` against a representative edit.
2. Compare its project JSON with OTIO and identify loss/translation boundaries.
3. Test CLI-Anything preview/live-session protocol as the shared visual feedback contract.
4. Test Remotion first-party skills plus Vercel `json-render` before designing Motion IR from scratch.
5. Use `video-use` as the reference editorial orchestration loop and map its EDL to OTIO.
6. Test `cli-anything-blender` for keyframe/camera/preview execution.
7. Only implement missing adapters after the spike matrix shows real gaps.

## Candidate promotion decisions

Likely promote after hands-on validation:

- CLI-Anything Shotcut/Kdenlive as executor references;
- CLI-Anything preview protocol as a harness pattern;
- Remotion first-party skills as implementation references;
- video-use as editorial orchestration reference;
- Vercel json-render as an IR/compiler design candidate.

Keep in research until validated:

- generic marketplace video skills;
- third-party Remotion MCP servers;
- broad Blender prompt packs;
- any skill whose popularity is the main evidence of quality.
