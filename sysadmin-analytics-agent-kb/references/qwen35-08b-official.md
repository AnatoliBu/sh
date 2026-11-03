---
artifact_type: reference
authority_tier: Tier A
status: foundation
source_type: official-model-documentation
topics:
  - model-editing
  - weight-space-programming
domains:
  - model-weight-repair
owner: Qwen Team
last_checked: 2026-11-03
source_url: https://huggingface.co/Qwen/Qwen3.5-0.8B
---

# Reference: Qwen3.5-0.8B official model card

## Authority tier

Tier A — publisher documentation for this checkpoint

## Status

foundation

## Owner / maintainer

Qwen Team.

## URL

https://huggingface.co/Qwen/Qwen3.5-0.8B

## Last checked

2026-11-03

## Scope

Architecture, supported context, thinking mode, known thinking-loop limitation and recommended runtime parameters.

## Why trusted

Primary maintainer of the model and weights.

## Caveats

262,144 is the model's native configured context, not a verified memory budget on an RTX 3070 Laptop; actual allocation and quality depend on runtime and inference settings.

## Skills that may consume this reference

- model-weight-repair

## Extracted rules

- Qwen3.5-0.8B has 24 language-model layers, 1024 hidden width and native context length 262,144.
- It is **non-thinking by default** in the model card; enable and verify thinking explicitly where supported. Qwen3.5 does not use the Qwen3 soft `/think` and `/nothink` switch.
- Official documentation warns that thinking mode on 0.8B can enter repetitive loops; monitor streaming and bound output length.
- For reproducible comparisons, record exact base revision, prompt/chat template, sampling, max-new-tokens and effective thinking behavior.
- Benchmarking on a text-only test does not validate image/vision behavior.

## Do not use this source for

Guaranteeing 256K context on 8 GB VRAM, comparing edited-vs-base math under unmatched thinking modes.
