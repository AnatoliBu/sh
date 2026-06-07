---
artifact_type: reference
authority_tier: Tier A
status: foundation
source_type: official-docs
topics:
  - java
  - testing
  - mockito
  - test-doubles
domains:
  - java-qa
owner: Mockito Project
last_checked: 2026-06-07
source_url: https://site.mockito.org/
---

# Reference: Mockito Documentation

## Authority tier

Tier A

## Status

foundation

## Owner / maintainer

Mockito Project

## URL

https://site.mockito.org/

## Last checked

2026-06-07

## Scope

Mockito setup, mocks, stubs, spies, verification, argument matching, captors, and Javadoc-based API behavior.

## Why trusted

Official Mockito project site and documentation entry point.

## Caveats

Mocking style affects test design. Use this as API authority, not as permission to mock every dependency.

## Agent-facing artifacts that may consume this reference

- [Java QA Agent](../java-qa/agent.md)
- [JUnit Java Test Design](../java-qa/skills/junit-java-test-design.md)
- [Test Code Quality](../java-qa/rules/test-code-quality.md)

## Extracted rules

- Prefer behavior-focused assertions over implementation-only interaction checks.
- Use mocks to isolate costly or unstable collaborators, not to reproduce the full object graph.

## Do not use this source for

HTTP contract testing or browser automation.

## Related references

- [JUnit User Guide](./junit-user-guide.md)
- [AssertJ Documentation](./assertj-docs.md)
