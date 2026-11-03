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
owner: SciPy maintainers
last_checked: 2026-11-03
source_url: https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.permutation_test.html
---

# Reference: SciPy paired permutation test

## Authority tier

Tier A — official documented implementation and explicit permutation null hypotheses

## Status

foundation

## Owner / maintainer

SciPy maintainers.

## URL

https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.permutation_test.html

## Last checked

2026-11-03

## Scope

Paired randomization/permutation inference for candidate-vs-baseline differences.

## Why trusted

SciPy API documentation specifies `permutation_type='samples'` for swapping within pairs.

## Caveats

Version and computational cost vary; the null hypothesis and choice of statistic must match the experimental design. Question clustering must be handled outside a naive per-generation test.

## Extracted rules

- For paired metrics, swap condition labels **within matched question pairs**; in SciPy this is `permutation_type='samples'`.
- Use the question as the exchangeability unit. For repeated seeds, aggregate per question before the simple paired permutation test, or use a cluster-aware approach.
- Use a prespecified statistic such as mean per-question candidate-minus-baseline correctness. State whether a p-value is exploratory or confirmatory.
- A paired bootstrap interval and a paired permutation p-value answer related but different questions; neither substitutes for guardrail checks.

## Do not use this source for

Treating a non-significant p-value as proof of equal quality or using independent-sample permutations for paired observations.
