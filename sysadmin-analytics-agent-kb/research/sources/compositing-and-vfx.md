# Source Review: Compositing and VFX

Last checked: 2026-08-17

## Sources reviewed

- OpenFX 1.5.1 specification: https://openfx.readthedocs.io/en/main/
- Blackmagic Design Resolve 20 Visual Effects training: https://www.blackmagicdesign.com/products/davinciresolve/training
- Natron 2.6 documentation: https://natron.readthedocs.io/en/rb-2.6/
- Blender documentation: https://docs.blender.org/
- OpenUSD: https://openusd.org/release/

## Claimed purpose

Create a renderer-neutral model for technical image compositing that an agent can plan, validate, preview, and compile to one or more headless execution engines.

## Authority level

Mixed.

- OpenFX: foundation candidate for effect/host terminology and technical contracts.
- Blackmagic official VFX training: professional compositing methodology reference.
- Natron: strong open implementation reference for node graphs and headless compositing.
- Blender: strong implementation platform, especially when 3D enters the graph.
- OpenUSD: foundation candidate for large-scale 3D scene interchange/composition, not a default 2D comp format.

## Strong findings

### OpenFX

OpenFX formalizes image-effect plug-ins as hosts, effects, clips, parameters, images, actions, and capabilities. Standard contexts include generators, filters, transitions, paint/general effects, and retimers.

The API also makes details such as supported image components, pixel depths, input/output clips, and premultiplication state explicit. Those ideas should appear in a Compositing Graph IR even when the actual executor is not an OFX host.

OpenFX is not a graph serialization format. It should inform node contracts rather than become our project file.

### Natron

Natron is architecturally relevant to agents because the node-based compositor has a GUI-free engine, Python bindings, OpenFX hosting, proxy/cache behavior, tracking/roto support, and a separate `NatronRenderer` binary for headless execution.

Its 2.6 architecture documentation describes a 32-bit float linear multi-channel pipeline and OpenColorIO color management. This aligns well with the existing `video-color` domain and makes explicit color-space handoffs mandatory when a comp graph crosses into grading/finishing.

### Blackmagic Fusion methodology

The official Resolve 20 VFX material covers basic node compositing and advances into 3D camera tracking, USD, particles, and combining 3D elements with live action. It is a useful professional methodology source, but Resolve/Fusion UI steps should not become agent contracts.

### Blender

Blender is a broader target than Natron: compositor, camera/geometry/lighting, animation, Python API, and headless rendering. It becomes preferable when the task is more than 2D image assembly.

### OpenUSD

OpenUSD is designed for collaborative construction of animated 3D scenes and non-destructive scene composition. Composition arcs, layers, references, time samples, layer offsets, and Value Clips are relevant for complex 3D/animation pipelines.

USD would be excessive for simple titles, masks, or 2D merges. Use it only when 3D scene assembly or interchange creates enough value to justify the complexity.

## Proposed Compositing Graph IR responsibilities

The IR should make these boundaries explicit:

- node type and stable node id;
- named input and output ports;
- media/image format expectations;
- bit depth and channel/component expectations when material;
- color space / transfer state at graph boundaries;
- alpha state: straight, premultiplied, opaque, unknown;
- transform and resampling policy;
- masks/mattes and their provenance;
- keying operations;
- tracking data and reference frame;
- merge operator;
- animated parameters;
- render range and resolution;
- cache/proxy hints that do not alter semantics.

## Candidate operation vocabulary

```text
Read
Transform
Reformat
Premultiply
Unpremultiply
Key
RotoMask
Track
CornerPin
Blur
Grade
Merge
TimeOffset
Retime
Write
```

This is an initial portable vocabulary, not a final schema.

## Agent flow

```text
inspect plates/assets
  -> establish color/alpha/format state
  -> identify required spatial relationships
  -> plan graph
  -> validate graph contracts
  -> compile to target engine
  -> render representative frames + short temporal proxy
  -> inspect edges, mattes, tracking, integration, color, temporal stability
  -> bounded revision
  -> persist graph + provenance
```

## What can be reused

- OpenFX vocabulary for explicit host/effect/input/output/parameter contracts.
- Natron's headless-engine separation as an architectural pattern.
- Node graph as source of truth instead of flattened effect text.
- Explicit alpha/premultiplication and color-space state.
- Proxy and region-based rendering for fast agent feedback.
- Blender/USD only when 3D needs justify them.

## What must not be reused blindly

- A GUI node name as a universal semantic operation.
- Hidden implicit color transforms between nodes.
- Hidden premultiply/unpremultiply behavior.
- A mask generated once and assumed valid for an entire sequence.
- Still-frame approval for tracking or temporal edges.
- USD as the default representation for simple 2D comps.

## Candidate skills

- `compositing-graph-planning`
- `keying-matte-roto`
- `tracking-and-matchmove`
- `layer-integration-qc`
- `headless-comp-render`

## Verdict

Promote OpenFX and the Blackmagic VFX training material as methodology/contract references. Audit Natron as the likely open 2D headless compositor target and Blender as the general 3D-capable target. Keep color and alpha provenance mandatory across all comp operations.
