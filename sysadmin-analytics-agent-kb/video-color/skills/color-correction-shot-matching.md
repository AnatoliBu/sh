---
artifact_type: skill
status: foundation
domain: video-color
---

# Skill: Color Correction and Shot Matching

## Purpose

Correct exposure, white balance, levels, contrast, curves, and saturation while preserving
shot continuity and a reproducible color-managed pipeline.

## Reference links

Authority references:

- [ACES 2 Color Management](../../references/aces-2-color-management.md)
- [OpenColorIO Documentation](../../references/opencolorio-docs.md)
- [FFmpeg Video Filters](../../references/ffmpeg-video-filters.md)
- [ASC Color Decision List](../../references/asc-color-decision-list.md)
- [Vex Video Editing Agent](../../references/vex-video-editing-agent.md)

## Required inputs

Collect or infer:

- source files and delivery target;
- camera/encoding metadata and trust level;
- intended working/output space;
- shot boundaries or permission to detect them;
- reference shot, reference still, or matching objective;
- creative direction, if any;
- whether skin/product colors are protected;
- whether global correction is sufficient.

## Decision sequence

### 1. Probe and classify source state

Persist `ffprobe` output and classify each source:

```text
KNOWN_MANAGED
KNOWN_DISPLAY_REFERRED
LIKELY_BUT_UNVERIFIED
UNKNOWN
```

For `UNKNOWN`, do not proceed with an irreversible or aggressive transform.

### 2. Normalize

For known log/wide-gamut media, transform into the selected working space with OCIO/ACES
or another explicit documented transform.

Do not hide input normalization inside a creative LUT.

### 3. Detect shots and sample representative frames

For edited media, build shot ranges first.

Sample several interior frames per shot. Avoid using only the first frame because fades,
motion blur, titles, or transitions can poison the estimate.

Collect at least:

```text
luma percentiles
channel means/percentiles
black/white clipping fractions
saturation distribution
neutral-region evidence
skin-region evidence when relevant
```

A few percentiles per channel beat one mean: two shots routinely agree in the highlights
and diverge in the midtones, which is exactly where a mixed illuminant shows up.

### 3b. Treat a long take as several shots

A shot is not a constant when the camera runs auto exposure and auto white balance. On
measured phone footage a single nine-minute take drifted by ~0.04 in the R/G ratio and
~11% in mean luma from start to end — larger than most of the corrections being fitted.

Segment long takes (≈30 s is a workable default), fit a profile per segment, and let the
correction follow the drift instead of averaging it away. If the source can be reshot,
locking exposure and WB in camera is cheaper than any of this.

### 4. Pick a reference strategy

Choose one:

```text
manual hero/reference shot
median well-exposed shot in the scene
camera-specific reference
external approved still
no cross-shot reference; correct shots independently
```

Never match every shot to the preceding shot recursively. Drift accumulates.

### 5. Generate bounded technical candidates

For each shot, include:

- no-op;
- conservative correction;
- nominal correction;
- optional stronger correction only when evidence is strong.

A correction candidate may modify:

```text
exposure / luma offset
WB gains or temperature/tint equivalent
black/white points
contrast
master/R/G/B curves
saturation
ASC CDL-compatible primaries
```

### 6. Score with multiple signals

Score candidates against:

- exposure target/reference;
- channel neutrality where a neutral region is credible;
- clipping increase;
- protected skin/product regions;
- saturation bounds;
- distance from neighboring shots;
- distance from no-op.

Do not optimize one scalar image statistic at the expense of perceptual continuity.

### 7. Smooth decisions across a scene

Use a continuity penalty or bounded temporal smoothing so adjacent shots from the same
camera/setup do not receive arbitrary grade jumps.

Keep real lighting changes when they are intentional.

### 8. Render a proxy and inspect

Render low-cost stills or a proxy sequence with identical color transforms.

Look at the frames before reading any number back. Scores rank the candidates that were
generated; they cannot report that the whole family was wrong. Lay the stills side by side
across cuts and along the timeline first, then use the metrics to explain what the eye
already flagged.

Review:

- waveform;
- RGB parade/vectorscope when useful;
- skin and neutral objects;
- highlights and channel clipping;
- shot boundaries;
- selected reference comparison.

### 9. Apply creative look after technical matching

Creative look is a separate stage. Use ASC CDL, CLF/LUT, curves, or explicit parameters as
appropriate, and preserve it separately in the manifest.

## Grade IR

Recommended shape:

```json
{
  "input": {
    "source_space": "known-or-null",
    "input_transform": "id-or-null",
    "confidence": 0.98
  },
  "working_space": "ACEScct",
  "shots": [
    {
      "start": 12.4,
      "end": 18.9,
      "reference": "shot-03",
      "correction": {
        "exposure_ev": 0.25,
        "wb": {"r": 0.99, "g": 1.0, "b": 1.03},
        "cdl": {"slope": [1, 1, 1], "offset": [0, 0, 0], "power": [1, 1, 1], "sat": 1.0}
      }
    }
  ],
  "look": "look-id-or-null",
  "output_transform": "display-view-id"
}
```

The exact schema may evolve; the invariant is separation of input, technical correction,
look, and output.

## Output

Return:

```text
source classification
working-space decision
shot table
selected reference strategy
per-shot corrections
warnings/confidence
proxy/QC evidence
deterministic grade-plan path
```

## Anti-patterns

- One auto-WB value for an entire multi-scene edit.
- Gray-world correction applied unconditionally to scenes dominated by one color.
- Matching every shot recursively to the immediately previous shot.
- Baking source normalization and creative look into an undocumented LUT.
- Large saturation/contrast changes before checking clipping and skin.
- Re-running perception on every final render instead of persisting decisions.
- One tone profile for a multi-minute auto-exposure take.
- Per-pixel comparison between two takes, where moved props read as a lighting change.
- Reporting a metric delta as the finding without ever looking at the two frames.
