---
artifact_type: reference
authority_tier: Tier B
status: foundation
source_type: research-preprint
topics:
  - model-evaluation
  - reproducibility
domains:
  - model-weight-repair
owner: Evan Miller
last_checked: 2026-11-03
source_url: https://arxiv.org/abs/2411.00640
---

# Reference: Adding Error Bars to Evals (Evan Miller, 2024)

## Authority tier

Tier B — an explicit statistical framework for evaluation; a preprint, not a normative standard

## Status

foundation

## Owner / maintainer

Evan Miller.

## URL

https://arxiv.org/abs/2411.00640

## Last checked

2026-11-03

## Scope

Experimental planning, error bars, paired model comparisons, uncertainty and sample-size reasoning.

## Why trusted

Primary methodological manuscript presenting formulas and assumptions.

## Caveats

Inference depends on what the test sample represents and how independent test items really are. A CI is not a guarantee of operational performance.

## Extracted rules

- Treat evaluation as an experiment with a predeclared estimand and sampling unit.
- Pair both models on the same question IDs and estimate the distribution of per-question paired differences.
- With multiple generations per question, keep all samples in the same question cluster when resampling; do not let repeated completions multiply effective N.
- Report uncertainty for the **difference** (e.g. candidate minus baseline, in percentage points), not just two independent accuracy intervals.
- Use a pilot to estimate variance/discordance and plan sample size for the desired minimum detectable effect (MDE).
- Report the population represented by the dataset and failure strata; conclusions are limited to it.

## Do not use this source for

Claiming significance proves a causal weight mechanism or treating multiple responses to one question as independent test questions.
