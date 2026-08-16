# Source Review: Frame Composition and Perceptual QC

Last checked: 2026-08-17

## Sources reviewed

- NIMA: https://research.google/pubs/nima-neural-image-assessment/
- MUSIQ: https://research.google/pubs/musiq-multi-scale-image-quality-transformer/
- EditIQ: https://arxiv.org/abs/2502.02172
- Blackmagic Design professional editing/VFX training: https://www.blackmagicdesign.com/products/davinciresolve/training

## Claimed purpose

Research ways for an agent to reason about visual framing and shot quality without pretending that aesthetic composition can be reduced to one deterministic rule.

## Authority level

Research-only / soft evidence.

No source reviewed here should become a hard visual-composition authority.

NIMA and MUSIQ are primary image-quality research. EditIQ is an automatic cinematic-editing research lead. Blackmagic training is a professional workflow reference. None establishes a universal scoring function for good cinematography.

## Strong findings

### Aesthetic scores are distributions and proxies

NIMA predicts distributions of human image-quality/aesthetic ratings rather than treating aesthetics as a binary label. This is useful conceptually: disagreement is information.

For an agent, a visual-quality model should therefore be treated as a noisy preference signal with uncertainty, not as a pass/fail oracle.

### Preserve native composition when evaluating it

MUSIQ was motivated partly by the problem that resizing/cropping images to a fixed network input may alter aspect ratio, composition, or perceived quality. Its multi-scale approach processes varying image sizes and aspect ratios.

This reinforces a practical QC rule: do not evaluate composition on a preprocessing crop that destroys the framing being judged.

### Editing quality can combine semantic and visual evidence

EditIQ is interesting as a research pattern rather than an authority. It combines dialogue understanding with visual saliency and formulates shot selection with cinematic constraints and continuity. This supports a multi-signal candidate-ranking approach instead of a single threshold.

## Proposed composition evidence

A future visual-composition reviewer may inspect:

- primary subject and face bounds;
- gaze direction and look room;
- subject motion direction and lead room;
- subject clipping / accidental edge tangencies;
- saliency concentration and competing focal points;
- horizon angle and strong structural lines;
- negative-space distribution;
- shot size and subject scale;
- text/title safe regions;
- continuity relative to adjacent shots;
- camera motion and stabilization effects;
- aesthetic/technical quality model outputs.

These are diagnostic features, not universal rules.

## Proposed output contract

```json
{
  "frame": 842,
  "observations": [
    {
      "type": "subject-edge-risk",
      "severity": 0.62,
      "region": [0.84, 0.12, 0.99, 0.88]
    },
    {
      "type": "look-room",
      "direction": "right",
      "available_fraction": 0.31
    }
  ],
  "soft_scores": {
    "aesthetic_model": 0.71,
    "technical_quality": 0.86,
    "continuity": 0.77
  },
  "confidence": 0.58,
  "recommendation": "compare-with-alternate-crop"
}
```

The contract intentionally reports observations before recommendations.

## Candidate comparison loop

```text
source framing
  -> no-op candidate
  -> bounded crop/reframe candidates
  -> evaluate subject preservation + continuity + quality
  -> render representative frames and short motion proxy
  -> vision/human review
  -> keep original unless improvement is supported
```

The no-op candidate is mandatory. The system must be allowed to conclude that the original framing is preferable.

## What can be reused

- Predict distributions or uncertainty rather than one aesthetic truth score.
- Native-aspect-ratio / full-frame evaluation where possible.
- Multi-signal ranking: semantics, saliency, continuity, technical quality, and user intent.
- Candidate generation with a no-op baseline.
- Temporal review for video framing.

## What must not be reused blindly

- Optimizing a shot solely for NIMA/MUSIQ score.
- `rule of thirds` as a mandatory constraint.
- Golden ratio as a mandatory constraint.
- Centering every detected face.
- Saliency maximum equals intended subject.
- Single-frame aesthetic score equals good sequence composition.
- Cropping away narrative/contextual information to improve an image-quality model score.

## Candidate skills

- `visual-composition-review`
- `reframe-and-crop-candidates`
- `shot-size-continuity-review`
- `title-safe-layout-review`
- `perceptual-qc`

## Open questions

- Find stronger primary research on video-specific composition and temporal aesthetics.
- Evaluate models that can distinguish intentional asymmetry from accidental framing errors.
- Define user-intent controls for documentary, performance, music video, tutorial, and cinematic narrative styles.
- Determine which geometric heuristics are robust enough to report as observations without turning them into style rules.
- Build an eval set with human-ranked alternate crops and edits.

## Verdict

Keep visual composition as a separate perceptual-review lane. It should advise the editorial/motion agent through observations, alternatives, and uncertainty. Do not turn it into a hard validator until the task has an explicit style contract that makes a particular geometric rule objectively testable.
