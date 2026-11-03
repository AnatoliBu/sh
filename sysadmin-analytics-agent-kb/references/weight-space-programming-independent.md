---
artifact_type: reference
authority_tier: Tier C
status: useful-after-audit
source_type: community-replication
topics:
  - model-editing
  - weight-space-programming
domains:
  - model-weight-repair
owner: Jonathan Coletti (community model/reproduction)
last_checked: 2026-11-03
source_url: https://huggingface.co/JonathanColetti/Qwen3.5-0.8B-Astra-WeightEdit
---

# Reference: Independent Astra edit replication and MATH-500 comparison

## Authority tier

Tier C — independent community run, not official author evaluation

## Status

useful-after-audit

## Owner / maintainer

Jonathan Coletti (community model/reproduction).

## URL

https://huggingface.co/JonathanColetti/Qwen3.5-0.8B-Astra-WeightEdit

## Last checked

2026-11-03

## Scope

Replication of the original patch and a comparison against a non-thinking baseline.

## Why trusted

Provides MATH-500 500 x 4 run protocol, hashes/scripts and both thinking configurations.

## Caveats

Community experiment as of 2026-11-03; other datasets not yet independently replicated in this report. Different settings and run-to-run variation matter.

## Skills that may consume this reference

- model-weight-repair

## Extracted rules

- MATH-500 thinking-on: unedited 7.4%, edited 50.2%, matching the direction of the authors' result.
- MATH-500 thinking-off: unedited 45.8%, edited 43.6%. Under this tested protocol, the patch is not beneficial in non-thinking mode.
- Edited thinking-on vs **unedited thinking-off**: +4.3 percentage points (reported 95% CI [1.9, 6.8]); don't present the roughly six-fold gain as a fair best-vs-best comparison without this caveat.
- This community checkpoint is a convenient comparison, but the official diff plus pinned base checkpoint is the audit path.
- Evaluate any converted GGUF/quantized derivative separately; BF16 numbers cannot be transferred unchanged.

## Do not use this source for

Claiming the patched model beats every unedited configuration or that a patch always helps.
