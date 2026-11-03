---
artifact_type: workflow
status: foundation
domain: model-weight-repair
---

# Workflow: Diagnose, Patch, Validate, Roll Back

## Reference links

- [Experiment 8 execution and edit diff](../../references/weight-space-programming-exp8-logs.md)
- [Original publication](../../references/weight-space-programming-2026.md)
- [Official Ollama memory requirements](../../references/ollama-context-official.md)
- [Independent thinking-mode comparison](../../references/weight-space-programming-independent.md)

## Experiment quality and artifact provenance

For the full statistically paired trial protocol, use
[Paired A/B Evaluation](../patterns/paired-llm-ab.md). For source checkpoint,
patch, BF16 -> GGUF and Ollama provenance gates, use
[Artifact Pipeline](../patterns/model-artifact-pipeline.md).
Fill the [Experiment Record Contract](../patterns/experiment-contract.md)
before opening the blind holdout. These are required for claims about
robust improvements and deployability, not optional decoration.

## Phase 0 — target and instrumentation

Define task and failure signature before choosing a technique. Capture hardware
model/VRAM, runner versions, checkpoint, thinking mode, prompt template, output cap,
sampler, context and effective GPU/CPU offload.

For Ollama on Windows, read current runtime state:

```powershell
ollama --version
ollama ps
nvidia-smi
```

Do not infer that a 256K configured model has allocated 256K context or fits in VRAM.

## Phase 1 — baseline / counterfactual

Run a representative, frozen task matrix under (A) the current settings and
(B) the strongest cheap configuration fix (notably thinking off if the model loops).
For each result log correctness, looping, truncation, output tokens, latency, GPU
memory and CPU offload. Keep a separate training/practice set for exploration.
If B fixes the problem sufficiently, stop: a weight edit is not justified.

## Phase 2 — diagnose a weight-level candidate

Use a full-precision, pinned HF checkpoint. Collect matched successful/repetitive
traces, hidden states and layer outputs, compare intervention candidates, then test
an isolated edit. When the failure matches the published Qwen3.5-0.8B reasoning
loop, first reproduce the released diff rather than inventing coefficients.

Upstream audit path:

```text
Qwen/Qwen3.5-0.8B @ 2fc06364715b967f1860aea9cf38778875588b17
   + RikiyaT/lm_understand-logs/exp8_math/runs/p50c/edit/edit.npz
   + exp8_math/code/apply_edit.py
   -> SHA-256-verified edited BF16 tensors / checkpoint
```

Read the upstream `apply_edit.py --help` or source for current invocation; do not
invent a runnable CLI signature. Match exact base tensor hashes before writing.

## Phase 3 — causal controls

Test edit dose, each edited layer alone, both layers, and a norm-matched random
edit. Record paired practice effects. No difference on previously completed
answers may indicate restored termination rather than new reasoning ability.
Run independent held-out correctness and guardrails next.

## Phase 4 — local deployment

Only after BF16 A/B, convert a copy through a backend that supports this
architecture and verify GGUF metadata, tokenizer/template, context and
the actual thinking mode. Re-run baselines and guardrails in Ollama.
`ollama ps` must show measured GPU split; progressively increase context
rather than promising 128K/256K on an 8 GB GPU.

## Phase 5 — verdict

Deliver a table: baseline-current, baseline-best-config, edited-BF16,
edited-local-quantized (if built). Record sample sizes, CIs/seeds, correct answers,
cut-at-limit share, mean tokens, latency and regressions. Keep only robust wins.
On failure, restore the hashed baseline and report what the intervention did not fix.
