---
artifact_type: reference
authority_tier: Tier A
status: foundation
source_type: official-library-documentation
topics:
  - model-evaluation
  - reproducibility
domains:
  - model-weight-repair
owner: PyTorch maintainers
last_checked: 2026-11-03
source_url: https://pytorch.org/docs/stable/notes/randomness.html
---

# Reference: PyTorch reproducibility note

## Authority tier

Tier A — official statement of repeatability limitations and controls

## Status

foundation

## Owner / maintainer

PyTorch maintainers.

## URL

https://pytorch.org/docs/stable/notes/randomness.html

## Last checked

2026-11-03

## Scope

Seeds, deterministic kernel modes, CUDA behavior and environment pinning.

## Why trusted

Primary framework documentation maintained by PyTorch.

## Caveats

Determinism has performance costs and is not guaranteed between releases, hardware, CPU/GPU or inference frameworks.

## Extracted rules

- Pin CUDA, driver, PyTorch release, kernels, torch dtype and hardware when claiming bit reproducibility.
- Record Python/NumPy/torch seed controls; distinguish reproducibility **within one runtime** from cross-runtime agreement.
- Deterministic algorithms may slow down runs; measure speed under the deployment configuration separately.
- Keep an untouched hashed base for every candidate to rule out background environment drift.

## Do not use this source for

Promising bit-for-bit results on different runtimes from the same seed.
