# Source Review: NetClaw / OpenClaw

## Claimed purpose

Network automation / autonomous network engineering agent with broad integrations and skill coverage.

## Authority level

Moodboard only / quarantine.

## Red flags

- Excessive scope: many skills and integrations across network, observability, ITSM, cloud, security, collaboration tools.
- Broad blast radius if connected to real infrastructure.
- Dependency on an agent runtime model not designed as a narrow, audited production control plane.
- Marketing/README scope is much larger than what should be trusted without deep code audit.
- Risk of autonomous infrastructure mutation.

## What can be reused

- List of possible domains for future skills.
- Integration taxonomy: SoT, ITSM, observability, config validation, lab simulation, telemetry.
- Idea of reconciling intended state and observed state.

## What must not be reused

- Runtime as production foundation.
- Trust model.
- Direct tool execution model.
- Any broad autonomous network mutation pattern.
- Code or install scripts without audit.

## Verdict

Do not build on NetClaw/OpenClaw. Use only as a brainstorming artifact when designing a safer, narrower system.
