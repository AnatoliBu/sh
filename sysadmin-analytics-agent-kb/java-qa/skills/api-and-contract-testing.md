---
artifact_type: skill
status: foundation
domain: java-qa
---

# Skill: API and Contract Testing

## Purpose

Design and review Java API tests, service mocks, container-backed integration tests, and consumer-driven contract tests.

## Reference links

Authority references:

- [REST Assured Documentation](../../references/rest-assured-docs.md)
- [WireMock Java Documentation](../../references/wiremock-java-docs.md)
- [Pact Documentation](../../references/pact-docs.md)
- [Testcontainers for Java Documentation](../../references/testcontainers-java-docs.md)
- [Spring Framework Testing Documentation](../../references/spring-framework-testing.md)

## Inputs

- API contract or endpoint description.
- Consumer and provider ownership.
- Test environment and dependency map.
- Test data setup.
- Authentication and authorization model.
- Expected response status, body, headers, and side effects.

## Output

- Recommended test type: API integration, mock-backed, contract, smoke, or end-to-end.
- Request and response assertions.
- Data setup and cleanup plan.
- Contract or stub maintenance notes.
- CI execution scope.

## Checklist

1. Identify whether the test protects provider behavior, consumer expectations, or both.
2. Check status code, business payload, error shape, and important headers.
3. Use WireMock for external dependencies that should not be called during tests.
4. Use Pact when consumer-provider expectations need executable agreement.
5. Use Testcontainers when infrastructure behavior matters.
6. Avoid broad end-to-end tests when contract or integration tests give clearer failure signals.

## Review smells

- API test checks only status code.
- Stub response no longer matches real provider behavior.
- Contract exists but provider verification is missing.
- Tests require shared mutable environment state.
- Authentication setup hides what the scenario is actually testing.
