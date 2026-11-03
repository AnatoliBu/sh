---
artifact_type: reference
authority_tier: Tier B
status: useful-after-audit
source_type: peer-reviewed-research
topics:
  - model-editing
  - weight-space-programming
domains:
  - model-weight-repair
owner: Akshat Gupta, Dev Sajnani, Gopala Anumanchipalli
last_checked: 2026-11-03
source_url: https://aclanthology.org/2024.findings-emnlp.903/
---

# Reference: A Unified Framework for Model Editing (EMNLP 2024)

## Authority tier

Tier B — peer-reviewed research on ROME, MEMIT and EMMET

## Status

useful-after-audit

## Owner / maintainer

Akshat Gupta, Dev Sajnani, Gopala Anumanchipalli.

## URL

https://aclanthology.org/2024.findings-emnlp.903/

## Last checked

2026-11-03

## Scope

Alternative model-editing methods for factual associations and their constraints.

## Why trusted

ACL Anthology peer-reviewed paper with an explicit formal model-editing objective.

## Caveats

Primarily factual-memory editing, not a demonstrated repair of Qwen3.5-0.8B repetition loops; no transfer of performance claims.

## Skills that may consume this reference

- model-weight-repair

## Extracted rules

- ROME and MEMIT edit model associations using preservation/memorization objectives; EMMET unifies them conceptually.
- Use these as **alternative mechanisms**, not as evidence that the published Astra edit employed them.
- Select a method by the diagnosed failure: local repeated output -> investigate activations and causal patch; factual association -> evaluate ROME/MEMIT-style approaches; systematic reasoning error -> prompting, tools or fine-tuning may be more appropriate.

## Do not use this source for

Attributing the Astra Qwen repair to ROME/MEMIT or using factual-edit metrics as a proxy for mathematical reasoning.
