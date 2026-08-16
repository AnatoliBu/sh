---
artifact_type: reference
authority_tier: Tier B
status: useful-after-audit
source_type: audited-community-repo
topics:
  - agents
  - video-editing
  - dsl
  - ffmpeg
domains:
  - video-color
owner: AgentsMesh / VEAC
last_checked: 2026-08-17
source_url: https://github.com/AgentsMesh/veac
---

# Reference: VEAC Video Editing as Code

## Authority tier

Tier B

## Status

useful-after-audit

## Owner / maintainer

AgentsMesh / VEAC.

## URL

https://github.com/AgentsMesh/veac

## Last checked

2026-08-17

## Scope

Declarative video-editing-as-code architecture: a constrained DSL/IR compiled to an
FFmpeg execution plan.

## Why trusted

The repository is a concrete implementation of an agent-friendly declarative editing
layer with check/plan/build/probe concepts.

## Caveats

The project is young and has limited adoption. It should be treated as an architectural
lead, not a dependency requirement and not an authority on grading methodology.

## Agent-facing artifacts that may consume this reference

- [Video Color Agent](../video-color/agent.md)
- [End-to-End Color Pipeline](../video-color/workflows/end-to-end-color-pipeline.md)

## Extracted rules

- Keep the agent-facing edit/grade representation declarative.
- Compile a stable intermediate representation into deterministic FFmpeg/OCIO commands.
- Separate planning and validation from execution.
- Make the IR inspectable before expensive rendering.

## Do not use this source for

Camera profiling or deciding the actual color transform mathematics.

## Related references

- [browser-use/video-use Agent Skill](./video-use-agent-skill.md)
- [FFmpeg Video Filters](./ffmpeg-video-filters.md)
