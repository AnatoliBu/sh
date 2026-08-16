---
artifact_type: skill
status: foundation
domain: video-color
---

# Skill: Mask-Assisted Grading

## Purpose

Use spatial masks only when a global correction cannot preserve the desired foreground,
background, skin, sky, product, or local lighting relationship.

## Reference links

Authority references:

- [FFmpeg Video Filters](../../references/ffmpeg-video-filters.md)
- [ACES 2 Color Management](../../references/aces-2-color-management.md)
- [OpenColorIO Documentation](../../references/opencolorio-docs.md)
- [browser-use/video-use Agent Skill](../../references/video-use-agent-skill.md)

## Decision sequence

### 1. Prove a mask is needed

Try the technically correct global correction first.

Use a mask when, for example:

- face is underexposed but background is already correct;
- sky requires a different highlight/saturation treatment;
- product color must remain fixed while environment shifts;
- mixed illumination needs local treatment;
- a creative secondary is explicitly requested.

### 2. Select mask source

Choose one:

```text
manual geometric mask
chroma/luma key
tracked roto
semantic/instance segmentation
hybrid segmentation + manual cleanup
```

Prefer the simplest mask that remains temporally stable.

### 3. Generate and persist the matte

Treat the mask as an inspectable artifact, not a hidden model output.

Persist:

- source range;
- model/tool and version;
- prompt/class/track identity;
- threshold;
- feather/blur;
- temporal smoothing;
- any manual corrections.

### 4. Check temporal stability

Inspect start/end and motion-heavy intervals.

Reject masks with:

- edge chatter;
- subject loss;
- identity switches;
- holes in protected regions;
- large frame-to-frame area jumps without matching motion.

### 5. Apply bounded secondary grade

Grade corrected and base branches in the same managed color space, then composite with the
mask.

With FFmpeg, `maskedmerge` is one deterministic option when the third video stream is the
per-pixel blend mask.

### 6. Inspect edges after the actual grade

A mask that looks acceptable as black/white matte may reveal halos only after exposure,
temperature, or saturation diverges between branches.

Review:

- hair and motion blur;
- high-contrast edges;
- semi-transparent material;
- skin boundaries;
- feathering through shot cuts.

## Output

Persist:

```text
mask asset
mask provenance
secondary correction
compositing recipe
edge/temporal QC frames
```

## Anti-patterns

- AI segmentation for every correction by default.
- Re-running segmentation at final render when an approved matte already exists.
- Hard mask edges for strong exposure/WB changes.
- Applying different input/output color transforms on the two mask branches.
- Accepting a mask from one still frame without temporal inspection.
