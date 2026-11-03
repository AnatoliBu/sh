---
artifact_type: reference
authority_tier: Tier A
status: foundation
source_type: official-technical-documentation
topics:
  - model-evaluation
  - reproducibility
domains:
  - model-weight-repair
owner: NVIDIA TensorRT maintainers
last_checked: 2026-11-03
source_url: https://docs.nvidia.com/deeplearning/tensorrt/10.x.x/inference-library/accuracy-considerations.html
---

# Reference: NVIDIA TensorRT accuracy considerations

## Authority tier

Tier A — primary documentation explaining rounding, clipping and precision effects

## Status

foundation

## Owner / maintainer

NVIDIA TensorRT maintainers.

## URL

https://docs.nvidia.com/deeplearning/tensorrt/10.x.x/inference-library/accuracy-considerations.html

## Last checked

2026-11-03

## Scope

Accuracy risks and validation of reduced-precision / quantized model deployment.

## Why trusted

Official inference framework documentation for numerical precision behavior.

## Caveats

NVIDIA TensorRT mechanisms are general numerical background; they do not verify specific llama.cpp GGUF quantizers or the Ollama runtime.

## Extracted rules

- Quantization can alter outputs through rounding and clipping. A BF16 edit hash does not imply equivalent Q4/Q8 behavior.
- If calibration is involved, split calibration examples from blind holdout and document their provenance.
- Evaluate original BF16 -> edited BF16 first; then original GGUF -> edited GGUF with the **same quantizer and runtime**.
- Capture tokenizer, tensor metadata, conversion command/version, kernel, GPU offload, actual context allocation and speed before promotion.

## Do not use this source for

Inferring that two numerical formats have equivalent accuracy without end-to-end evaluation.
