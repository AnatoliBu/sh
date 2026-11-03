---
name: model_weight_repair
description: >
  Use when: «исправь веса Qwen», «Astra patch», «model weight repair»,
  «Qwen3.5-0.8B зацикливается», «почему локальная LLM тупит на математике»,
  «скопируй/проверь weight-space programming», «проверить GGUF после патча»,
  «Ollama RTX 3070 model editing». Evidence-led diagnosis and reversible
  neural-network weight edits, published GPT-6 Astra Qwen repair, controlled
  paired A/B evaluation, statistical confidence, ML artifact lineage, quantization gates, causal ablations and rollback.
---

# Model Weight Repair

Use this skill to determine **whether a change to weights is warranted**, then
audit or run a small, reversible experiment. It is a methodology, not a claim
that a generic LLM can reliably fix all networks.

## Read as needed

| File | Task |
|---|---|
| [references/weight-repair.md](references/weight-repair.md) | Failure triage, comparator, metrics and candidate design |
| [references/workflow.md](references/workflow.md) | End-to-end baseline -> diagnosis -> patch -> quantized local validation |
| [references/paired-llm-ab.md](references/paired-llm-ab.md) | Matched-arm A/B, thinking-mode counterfactual, cluster bootstrap, power and guards |
| [references/model-artifact-pipeline.md](references/model-artifact-pipeline.md) | ML lineage, BF16 -> GGUF/quantization gates, hardware/runtime verification |
| [references/experiment-contract.md](references/experiment-contract.md) | Trial manifest and per-response JSONL fields |
| [references/safety.md](references/safety.md) | SHA/shape gates, held-out split, causal controls, privacy, rollback |
| [references/cards/weight-space-programming-exp8-logs.md](references/cards/weight-space-programming-exp8-logs.md) | Pinned Qwen revision, published edit files, exact hashes and counts |
| [references/cards/weight-space-programming-2026.md](references/cards/weight-space-programming-2026.md) | Study protocol and interpretation limits |
| [references/cards/qwen35-08b-official.md](references/cards/qwen35-08b-official.md) | Official Qwen architecture, thinking mode and loop warning |
| [references/cards/weight-space-programming-independent.md](references/cards/weight-space-programming-independent.md) | Independent thinking-on/off comparator |
| [references/cards/ollama-context-official.md](references/cards/ollama-context-official.md) | Effective context and GPU/CPU offload |
| [references/cards/model-editing-rome-memit.md](references/cards/model-editing-rome-memit.md) | Other editing families; not the Astra algorithm |

## Routing

```text
slow/CPU spill -> runtime/context/quantization, NOT weight editing
repetition -> compare thinking off / sampling / output budget first
wrong answers despite completion -> tool/prompt/fine-tune alternative
reproducible defect + causal evidence -> pinned, reversible sparse edit
```

## Critical checks

1. Fix exact checkpoint, chat template, thinking mode, sampler, token budget,
   evaluation data and runtime versions before comparing outputs.
2. Include the **best unedited configuration**, not only a broken thinking-on
   baseline. Blind holdout must be untouched during patch design.
3. For the Astra Qwen edit, use the original released diff and pinned base
   revision, not handwritten approximations or a different Qwen size.
4. Keep the untouched BF16 model, check tensor hashes, apply a diff to a copy,
   test layer ablations and a norm-matched random control.
5. For 8 GB RTX 3070 + Ollama, measure actual `CONTEXT` and `PROCESSOR`
   with `ollama ps`; 256K advertised context is **not** a fit guarantee.
6. Re-test after GGUF/quantization and report correctness, loops, truncated
   outputs, memory, tokens/s, regression and uncertainty. Reject weak wins.

Before opening the blind holdout, specify task sampling, primary effect,
MDE, comparison arms, clustered uncertainty procedure and guardrail limits.
Track run metadata and immutable hashes for BF16 and quantized variants.

The published edit primarily addresses a reasoning **loop**, not general
mathematical capability. Make that distinction explicit in every report.

## Output

A reproducibility card: failure, evidence, baselines, intervention and tensor
diff, test matrix, guardrails, confidence limits, decision and rollback path.
