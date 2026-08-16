---
artifact_type: index
status: foundation
domain: video-color
---

# Video Color Tooling

## Recommended stack

| Layer | Tool | Role | Default |
|---|---|---|---|
| Probe | `ffprobe` | codec, pixel format, tags, duration, stream metadata | required |
| Render | `ffmpeg` | correction, LUTs, masks, scopes, stabilization, encode | required |
| Color management | OpenColorIO | explicit source/working/output transforms | required for managed workflows |
| Config | ACES OCIO config | standard ACES transforms and views | preferred |
| Shot detection | PySceneDetect / FFmpeg scene metrics | cut/shot ranges | recommended |
| Analysis | Python + OpenCV + NumPy | frame sampling, masks, statistics | recommended |
| Color math | Colour | colorimetry, chart/reference calculations | recommended |
| Camera profile | ACES IDT tooling | ACES-native camera Input Transform | task-specific |
| Camera profile | DCamProf | DCP/ICC profiling | optional |
| Segmentation | SAM 2 / YOLO segmentation | person/skin/sky/object mask proposals | optional |
| Scriptable video graph | VapourSynth | Python-authored frame pipeline | optional |
| Headless compositor | NatronRenderer | roto/key/tracking/compositing | optional |
| Stabilization | libvidstab through FFmpeg | two-pass motion stabilization | optional |

## Core CLI surface

### Probe

```bash
ffprobe -v error -show_streams -show_format -of json input.mov
```

Persist the output to `inventory.json`. Do not repeatedly rediscover the same source
metadata.

### Inspect available FFmpeg capabilities

```bash
ffmpeg -filters
ffmpeg -h filter=curves
ffmpeg -h filter=lut3d
ffmpeg -h filter=maskedmerge
```

Do this before assuming a packaged build contains optional filters.

### OCIO validation

```bash
ociocheck --iconfig config.ocio
ociochecklut -v look.cube
```

Use explicit config identity/version in the grade manifest.

### OCIO conversion and LUT baking

```bash
ocioconvert input.exr ACEScg output.exr sRGB
ociobakelut --inputspace <src> --outputspace <dst> --format <fmt> output.lut
```

Exact argument availability may vary by OCIO release; query `--help` in the installed
version.

### Shot-aware analysis

Use PySceneDetect or FFmpeg scene-change signals to propose shot boundaries, then sample
several frames inside each shot. Do not grade a long edited sequence from one global
histogram.

### Scopes and measurable QC

Useful FFmpeg primitives include:

```text
signalstats
histogram
waveform
vectorscope
ciescope
```

Numeric metrics are evidence. They are not a substitute for rendered image review.

### Spatial masks

Produce masks as ordinary grayscale frame sequences or lossless video, then combine a
corrected and uncorrected branch using `maskedmerge` or an equivalent compositor.

Keep mask generation separate from grade generation so each can be inspected and
replaced independently.

## Tool choice by job

```text
basic correction
  -> ffprobe + ffmpeg

log / wide gamut / multi-camera
  -> ffprobe + OCIO/ACES + ffmpeg

shot matching
  -> + shot detector + Python analysis

person/sky/object secondary
  -> + segmentation/tracking + masked render

camera profiling
  -> controlled capture + ACES IDT tooling
  -> optionally DCamProf for DCP/ICC

complex roto/key/compositing
  -> NatronRenderer or a dedicated compositor
```

## What not to build first

Do not start by wrapping every FFmpeg filter in an MCP server. Start with a small
declarative Grade IR and a compiler for the operations the agent can validate reliably.
