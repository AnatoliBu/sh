---
artifact_type: reference
authority_tier: Tier B
status: foundation
source_type: official-community-guide
topics:
  - model-evaluation
  - reproducibility
domains:
  - model-weight-repair
owner: Hugging Face evaluation-guidebook maintainers
last_checked: 2026-11-03
source_url: https://github.com/huggingface/evaluation-guidebook/blob/main/contents/troubleshooting/troubleshooting-reproducibility.md
---

# Reference: Hugging Face evaluation reproducibility troubleshooting

## Authority tier

Tier B — maintainer guidance on realistic LLM benchmark variance

## Status

foundation

## Owner / maintainer

Hugging Face evaluation-guidebook maintainers.

## URL

https://github.com/huggingface/evaluation-guidebook/blob/main/contents/troubleshooting/troubleshooting-reproducibility.md

## Last checked

2026-11-03

## Scope

Prompt ordering, few-shot contamination, decoding parameters, backends, precision, batching and reproducibility.

## Why trusted

Published by a leading evaluation tooling ecosystem, with firsthand benchmark pitfalls.

## Caveats

A guidebook, not a guarantee of identical outputs across GPU kernels or architectures.

## Extracted rules

- Freeze prompt, system text, chat template, sample/few-shot ordering, stop tokens, scoring parser, max output, sampling and seed.
- Backend, loading precision, GPU, batch size and numerical algorithms can change output; record all of them.
- Keep exact raw completions when allowed, including parser failures and `truncated_at_limit`.
- Avoid using the blind benchmark repeatedly to select patch scale or sampling temperature.

## Do not use this source for

Assuming a fixed random seed guarantees bit-identical output across vLLM, Transformers, llama.cpp and Ollama.
