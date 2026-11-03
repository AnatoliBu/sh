---
artifact_type: reference
authority_tier: Tier A
status: foundation
source_type: official-tool-documentation
topics:
  - model-evaluation
  - reproducibility
domains:
  - model-weight-repair
owner: MLflow maintainers
last_checked: 2026-11-03
source_url: https://mlflow.org/docs/latest/tracking/
---

# Reference: MLflow Tracking and model lineage

## Authority tier

Tier A — primary documentation for logging run parameters, code versions, metrics and artifacts

## Status

foundation

## Owner / maintainer

MLflow maintainers.

## URL

https://mlflow.org/docs/latest/tracking/

## Last checked

2026-11-03

## Scope

Experiment lineage, run tracking, artifact registry and model promotion.

## Why trusted

Official MLflow platform documentation.

## Caveats

MLflow is an optional implementation; structured local JSONL and immutable hashes can satisfy the same evidence contract for small projects. Tracking does not automatically validate data leakage.

## Extracted rules

- Give each run an ID; log code revision, checkpoint source/hash, edit diff/hash, dataset snapshot/hash, runner and environment.
- Log metrics **and raw per-item outputs**, subject to data permissions; include prompt and grader versions.
- Treat every artifact (base BF16, patched BF16, quantized GGUF, Ollama model definition) as a distinct lineage node.
- Promote a model only after frozen holdout, regression checks, hardware smoke and rollback readiness; never overwrite the baseline.

## Do not use this source for

Claiming every experiment needs a tracking server or that logging alone makes an experiment reproducible.
