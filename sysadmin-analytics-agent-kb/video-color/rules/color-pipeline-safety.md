---
artifact_type: rule
status: foundation
domain: video-color
---

# Rule: Color Pipeline Safety

## Reference links

Authority references:

- [ACES 2 Color Management](../../references/aces-2-color-management.md)
- [OpenColorIO Documentation](../../references/opencolorio-docs.md)
- [FFmpeg Video Filters](../../references/ffmpeg-video-filters.md)
- [ASC Color Decision List](../../references/asc-color-decision-list.md)
- [claude-mods FFmpeg Operations](../../references/claude-mods-ffmpeg-ops.md)

## Rules

### Never guess a source transform silently

If primaries, transfer function, matrix/range, log encoding, or camera profile is unknown,
mark it unknown. Do not silently treat unknown footage as Rec.709 because it looks normal
in one viewer.

### Normalize before creative grading

For log or wide-gamut inputs, establish the input transform and working space before
applying a creative look.

### Separate technical and creative operations

Persist these independently:

```text
source interpretation
input transform
technical correction
shot match
secondary/mask corrections
creative look
output transform
encoding
```

### Never accept solely on histogram targets

A technically centered histogram can still contain bad skin, wrong WB, clipped channels,
or discontinuity. Use metrics to find problems, then inspect rendered frames/scopes.

### Bound automatic corrections

Automatic exposure, WB, saturation, and contrast changes require:

- hard parameter limits;
- clipping/gamut checks;
- confidence or evidence;
- a no-op candidate;
- comparison against neighboring shots.

### Protect source media

Never overwrite source video or calibration captures.

### Preserve provenance

The final grade manifest must include enough information to re-render without asking the
model to make the same aesthetic decisions again.

### Treat masks as data

Store mask source, model/tool version, temporal tracking/smoothing settings, and feather
parameters. Review edges and temporal stability.

### Validate output metadata

After render, use `ffprobe` to check codec, dimensions, frame rate, bit depth/pixel format,
and color tags expected by the delivery target.

## Stop conditions

Stop automatic execution and surface uncertainty when:

- camera encoding is materially ambiguous;
- mixed illuminants make a global WB correction unsafe;
- clipping would increase materially;
- a mask flickers or loses the subject;
- shot-match confidence is low and no stable reference shot exists;
- profiling capture violates the controlled-capture requirements.
