---
artifact_type: reference
authority_tier: Tier A
status: foundation
source_type: official-runtime-documentation
topics:
  - model-editing
  - weight-space-programming
domains:
  - model-weight-repair
owner: Ollama documentation maintainers
last_checked: 2026-11-03
source_url: https://docs.ollama.com/context-length
---

# Reference: Ollama context and GPU offloading

## Authority tier

Tier A — official inference runtime documentation

## Status

foundation

## Owner / maintainer

Ollama documentation maintainers.

## URL

https://docs.ollama.com/context-length

## Last checked

2026-11-03

## Scope

Default context behavior by available VRAM, context override and verification of GPU/CPU split.

## Why trusted

Maintained by the software provider.

## Caveats

A model card's maximum context is not the default or a guarantee it will fit; performance and memory depend on loaded model, cache, runtime version and other GPU processes.

## Skills that may consume this reference

- model-weight-repair

## Extracted rules

- Ollama defaults (as documented on 2026-11-03): under 24 GiB VRAM -> 4K context; 24–48 GiB -> 32K; 48 GiB or more -> 256K.
- For long contexts, set the context explicitly; increasing it increases memory use.
- Inspect `ollama ps` and record `CONTEXT` and `PROCESSOR` for every benchmark run.
- On limited VRAM, test 16K -> 32K -> 64K -> 128K incrementally instead of assuming the entire 256K configured window fits without CPU offloading.
- Keep runtime settings identical between baseline and candidate; do not treat memory or speed changes as improved model reasoning.

## Do not use this source for

Certifying 128K/256K context fits in an 8 GB GPU without a local measurement.
