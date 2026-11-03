---
artifact_type: workflow
status: foundation
domain: model-weight-repair
---

# Workflow: Weight Edit to Local Inference — ML Artifact Pipeline

## Reference links

- [MLflow tracking and lineage](../../references/mlflow-experiment-tracking.md)
- [PyTorch reproducibility boundaries](../../references/pytorch-reproducibility.md)
- [NVIDIA numerical precision risks](../../references/nvidia-quantization-accuracy.md)
- [HF benchmark reproducibility](../../references/huggingface-eval-reproducibility.md)
- [Published Qwen patch and hashes](../../references/weight-space-programming-exp8-logs.md)
- [Ollama context/offload](../../references/ollama-context-official.md)

## Pipeline DAG

```text
source weight snapshot + exact revision/checksums
   -> dataset license, dedup, train/dev/holdout isolation
   -> base BF16 smoke and config A/B baseline
   -> trace extraction and frozen patch hypothesis
   -> sparse edit replay on a COPY (shape + base/edited hash gate)
   -> patched BF16 smoke / causal ablation / held-out evaluation
   -> quantizer compatibility check and conversion (new artifact ID)
   -> original-vs-edited GGUF A/B in same inference runtime
   -> Ollama local smoke: context, tokenizer, GPU offload, latency, loops
   -> model release manifest + promotion / rollback to baseline
```

The upstream `apply_edit.py` reproduces a specific BF16 tensor diff. It
does **not** operate on arbitrary quantized GGUF bytes. Repair in the source
weight space and then convert; every conversion creates a new model artifact.

## Stage contracts and stop gates

| Stage | Required evidence | Stop condition |
|---|---|---|
| Source | Repo, commit/revision, `safetensors` hashes, architecture, tokenizer/template | Revision/hash/shape mismatch |
| Data | Licensed source, immutable dataset snapshot, question IDs, dedup, dev vs holdout | Contamination/leakage or invalid labels |
| Baseline | Original think-on and best unedited config, sampling+context frozen | Bad harness/A/A drift |
| Intervention | Hypothesis, selected layers/columns, patch checksums, rollback | Edit outside allowed region or missing provenance |
| BF16 eval | Paired results, ablations, random edit control, guardrails | No robust practical gain |
| Conversion | Tool commit, quantization method, GGUF metadata and artifact hash | Unsupported architecture / tokenizer mismatch |
| Local eval | Original/edited GGUF with same settings; `ollama ps`; speed, memory, correctness | Regression, CPU spill outside budget, token/template mismatch |
| Promotion | Artifact lineage, model card, evaluation summary and original restoration path | Missing evidence or failed gate |

## What to record in a run

Minimum provenance fields:

- `experiment_id`, `parent_run_id`, wall clock / source commit;
- `base_model_repo`, `base_revision`, `base_sha256`;
- `edit_kind`, target tensor names, expected shapes, affected coordinates,
  `patch_sha256`, `edited_tensor_sha256`, counts addressed vs bit-different;
- `dataset_id`, `dataset_sha256`, split, dedup rules, grader version,
  `prompt_template_sha256`, exact stop criteria and mode;
- `backend` (Transformers/vLLM/llama.cpp/Ollama), full version, model loader,
  GPU name, VRAM, CUDA driver, quantizer revision, GGUF checksum;
- `temperature`, `top_p`, `top_k`, `seed`, `num_ctx`, `max_new_tokens`,
  `repeat_penalty`/`presence_penalty`, sampling and batch size;
- per-response raw output when licensing/privacy permits, parsed score,
  truncation, generated token count, elapsed time, CPU/GPU offload,
  error code and sampler failures.

Use lightweight JSONL + a manifest + content hashes for a local project.
MLflow Tracking and Model Registry are useful **optional** implementations
for run comparison, versioning, artifact lineage and promotion.

## Qwen / 8 GB laptop-specific pitfalls

- 262K model architecture capacity does not imply 262K fits on an 8 GB RTX
  3070 Laptop without offload. Check actual `CONTEXT`, `PROCESSOR` and
  `nvidia-smi`; use measured progressive context steps.
- Context changes KV/cache footprint, throughput, truncation rates and
  wall-time budget. Never change it only for the edited arm.
- Thinking on vs off, stop tokens and chat template are *behavioral* changes,
  not weight changes. Log them explicitly.
- Numeric drift exists even with the same seed across GPU backends. A
  byte-identical hash check verifies artifact identity, not identical outputs.
- Quantizer choice/calibration and GPU offload can erase small improvements.
  BF16 and GGUF each need own confirmation and rollback snapshots.
- Run A/B performance measurements after warmup, one model at a time, alternating
  order to mitigate laptop temperature/power drift.

## Rollback

Retain a pointer to the last known-good base model and Modelfile/config, not
just the edited weights. A rollback should restore the **checkpoint, tokenizer,
runner settings and quantized artifact** in one documented action. Do not
silently overwrite the running model tag.

## Deliverable

A DAG/manifest, dataset lineage, A/B report, source+patch+quantized hashes,
conversion logs, smoke results on actual hardware, promotion decision and
reversal instructions. A pipeline that merely finishes has not met its quality gate.
