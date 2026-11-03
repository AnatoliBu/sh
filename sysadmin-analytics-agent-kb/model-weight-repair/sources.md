---
artifact_type: index
status: foundation
domain: model-weight-repair
---

# Model Weight Repair Sources

Primary, with a trust boundary:

1. [MIT CSAIL blog / Experiment 8](../references/weight-space-programming-2026.md) — original unreviewed claim and setup.
2. [Released experiment logs, code, diff and hashes](../references/weight-space-programming-exp8-logs.md) — reproducibility authority for the published patch.
3. [Qwen official model card](../references/qwen35-08b-official.md) — runtime and thinking-loop caveats.
4. [Independent community replication](../references/weight-space-programming-independent.md) — crucial thinking-off baseline comparator.
5. [Official Ollama context docs](../references/ollama-context-official.md) — allocated context and GPU offloading.
6. [ROME/MEMIT/EMMET paper](../references/model-editing-rome-memit.md) — related model-editing family, not the same mechanism.

7. [Statistical error bars for LLM evaluations](../references/llm-evaluation-error-bars-2024.md) — paired differences, power and uncertainty.
8. [SciPy paired permutation tests](../references/scipy-paired-permutation.md) — correct matched-pair null hypothesis.
9. [Hugging Face eval reproducibility guide](../references/huggingface-eval-reproducibility.md) — template, backend and sampling pitfalls.
10. [MLflow tracking](../references/mlflow-experiment-tracking.md) — run lineage, artifacts and registry.
11. [PyTorch reproducibility](../references/pytorch-reproducibility.md) — RNG and hardware limits.
12. [NVIDIA quantization accuracy](../references/nvidia-quantization-accuracy.md) — rounding/clipping consequences.

## Operational methodologies

- [Paired A/B experiments](./patterns/paired-llm-ab.md) — factorial controls, clustered intervals, MDE and holdout.
- [Artifact ML pipeline](./patterns/model-artifact-pipeline.md) — checkpoints, provenance, BF16/GGUF and gates.
- [Run/result contract](./patterns/experiment-contract.md) — minimal manifest, JSONL schema and decision record.

## Evidence hierarchy

Pinned weight bytes and reproduced tests > released log/manifests > investigator write-up >
independent community commentary > speculation. Preserve the distinction between
a verified checkpoint diff, replicated benchmark numbers and any unverified claims
about local 8 GB hardware.

## Reproducibility pointers

- Base: https://huggingface.co/Qwen/Qwen3.5-0.8B/tree/2fc06364715b967f1860aea9cf38778875588b17
- Submitted edit: https://github.com/RikiyaT/lm_understand-logs/tree/main/exp8_math/runs/p50c/edit
- Application script: https://github.com/RikiyaT/lm_understand-logs/blob/main/exp8_math/code/apply_edit.py
- Edited release: https://huggingface.co/RikiyaT/Qwen3.5-0.8B-weight-space-programming
- Independent model/benchmark: https://huggingface.co/JonathanColetti/Qwen3.5-0.8B-Astra-WeightEdit

Do not silently substitute similarly named models or revisions.
