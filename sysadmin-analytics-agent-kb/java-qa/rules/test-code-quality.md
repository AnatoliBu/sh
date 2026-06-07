---
artifact_type: rule
status: foundation
domain: java-qa
---

# Rule: Test Code Quality

## Purpose

Keep Java test code readable, diagnostic, and resilient to safe production refactoring.

## Reference links

Authority references:

- [JUnit User Guide](../../references/junit-user-guide.md)
- [AssertJ Documentation](../../references/assertj-docs.md)
- [Mockito Documentation](../../references/mockito-docs.md)
- [ISTQB Testing Foundation Materials](../../references/istqb-testing-foundation.md)

## Rules

1. A test must identify behavior, condition, and expected result.
2. Assertions must prove business meaning, not only object existence.
3. Test data should be readable and local unless shared fixtures are intentional.
4. Mocks should support isolation, not hide unclear design.
5. Test names should help locate the failed behavior quickly.
6. Setup should not be larger than the behavior under test without a clear reason.
7. The expected result must be traceable to requirements, contract, bug, or domain rule.

## Review questions

- What behavior does this test protect?
- What would break in production if this test failed?
- Is the assertion precise enough to diagnose the failure?
- Is the test too close to implementation details?
- Can this be a smaller or faster test?

## Bad signs

- `assertNotNull` as the main assertion.
- Large copied fixtures with unclear important fields.
- Many mocks and no visible behavior.
- Test name says one scenario, assertions check another.
- Hidden ordering or environment dependency.
