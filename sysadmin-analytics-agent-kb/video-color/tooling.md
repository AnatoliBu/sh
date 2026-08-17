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

### Probe the color state, not only the container

Four stream fields decide interpretation. Read them explicitly instead of scanning a full
`-show_streams` dump by eye:

```bash
ffprobe -v error -select_streams v:0 \
  -show_entries stream=pix_fmt,color_range,color_space,color_transfer,color_primaries \
  -show_entries stream_side_data=rotation \
  -of default=noprint_wrappers=1 input.mov
```

```text
color_primaries  -> gamut
color_transfer   -> transfer function (may be a log or HDR curve)
color_space      -> Y'CbCr matrix
color_range      -> tv (limited) or pc (full)
```

An empty field means **unspecified**, not Rec.709. `rotation` side data means the coded
frame size is not the display size: a 3840x2160 phone stream can be a vertical 2160x3840
image. HDR mastering-display and content-light metadata is carried per frame:

```bash
ffprobe -v error -select_streams v:0 -read_intervals '%+#1' \
  -show_entries frame_side_data=side_data_type -of default=noprint_wrappers=1 input.mov
```

Do not add `-show_frames` to that call: it re-enables the full per-frame section and buries
the one field being queried.

Record all four fields plus rotation in `inventory.json` and map each source to the trust
classes used by the correction skill. Absent tags are an `UNKNOWN`/`LIKELY_BUT_UNVERIFIED`
input, not a license to assume the delivery space.

### Inspect available FFmpeg capabilities

```bash
ffmpeg -filters
ffmpeg -h filter=curves
ffmpeg -h filter=lut3d
ffmpeg -h filter=maskedmerge
```

Do this before assuming a packaged build contains optional filters.

### Convert color spaces explicitly

Container tags and pixel transforms are two different things:

```bash
# transforms pixels (Y'CbCr matrix, TRC, primaries, range)
ffmpeg -i in.mov -vf "colorspace=all=bt709:iall=bt470bg:itrc=smpte170m:irange=tv" out.mov

# only writes tags — pixels untouched
ffmpeg -i in.mov -colorspace bt709 -color_trc bt709 -color_primaries bt709 \
  -color_range tv -c copy tagged.mov
```

A correct render needs both: the filter to move the pixels and the output flags so the next
tool interprets them the same way. `zscale` (libzimg) is the alternative when a build lacks
`colorspace` support or a linear intermediate is wanted:

```bash
ffmpeg -filters | grep -E '^ .. (colorspace|zscale|tonemap)'
```

Neither filter is a substitute for a documented input transform on log footage.

### HDR sources

Phones are the common case: a modern iPhone or Android records HDR HEVC by default, which
probes as `color_primaries=bt2020`, `color_transfer=arib-std-b67` (HLG) or `smpte2084` (PQ),
often with Dolby Vision metadata. Handing that to an SDR filter chain produces washed-out,
desaturated output that no amount of curve tweaking repairs.

Decide the dynamic-range path before grading:

```text
HDR delivery      -> stay in the HDR transfer function, tag output accordingly
SDR delivery      -> explicit tone map, then grade in the SDR working space
unknown delivery  -> stop; ask, do not silently tone map
```

```bash
ffmpeg -i hlg.mov -vf \
  "zscale=t=linear:npl=100,tonemap=hable:desat=0,zscale=p=bt709:t=bt709:m=bt709:r=tv,\
format=yuv420p" -c:v libx264 -crf 18 sdr.mp4
```

Record the operator, its parameters, and the peak-luminance assumption in the grade plan.
A tone map is a creative decision disguised as a technical one.

### Work above delivery precision

An 8-bit filter graph with curves, exposure, and saturation changes produces banding in
gradients. Promote before grading and dither on the way down:

```text
grade in 10/12-bit or float  -> format=yuv420p10le / gbrpf32le
deliver 8-bit                -> zscale=...:dither=error_diffusion, then format=yuv420p
```

Chroma subsampling is also destructive: 4:2:0 is a delivery format, not a grading format.
Where the source allows it, keep intermediates at 4:2:2/4:4:4.

### OCIO validation

```bash
ociocheck --iconfig config.ocio
ociochecklut -v look.cube 0.18 0.18 0.18
```

`ociochecklut` needs a LUT **and** an input value (or `-t`) — passing the file alone only
parses it and proves nothing about the transform. Use explicit config identity/version in
the grade manifest.

OCIO is not always installed, and a missing binary is not a reason to fake a managed
pipeline: verify first, then either install it or downgrade the plan to a documented
FFmpeg-only path.

```bash
command -v ociocheck ocioconvert ociobakelut || echo 'OCIO CLI absent'
```

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
