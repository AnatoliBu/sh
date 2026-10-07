---
artifact_type: reference
status: foundation
domain: java-qa
---

# Java QA Sources

This file ranks source-of-truth references for Java QA automation agents.

## Tier A — foundation sources

- [JUnit User Guide](../references/junit-user-guide.md)
- [Selenium WebDriver Documentation](../references/selenium-webdriver-docs.md)
- [Testcontainers for Java Documentation](../references/testcontainers-java-docs.md)
- [REST Assured Documentation](../references/rest-assured-docs.md)
- [Mockito Documentation](../references/mockito-docs.md)
- [AssertJ Documentation](../references/assertj-docs.md)
- [WireMock Java Documentation](../references/wiremock-java-docs.md)
- [Spring Framework Testing Documentation](../references/spring-framework-testing.md)
- [Gradle Java Testing](../references/gradle-java-testing.md)
- [Pact Documentation](../references/pact-docs.md)
- [ISTQB Testing Foundation Materials](../references/istqb-testing-foundation.md)

## Tier B — peer-reviewed REST API test-generation research

- [Testing RESTful APIs: A Survey](../references/testing-restful-apis-survey-2023.md) — ACM TOSEM survey of 92 scientific articles; use as the taxonomy/index for the field.
- [Automatic Generation of Test Cases for REST APIs: A Specification-Based Approach](../references/openapi-test-generation-edoc-2018.md) — specification-based generation directly from OpenAPI.
- [QuickREST](../references/quickrest-icst-2020.md) — property-based test generation from OpenAPI documents.
- [RESTTESTGEN](../references/resttestgen-icst-2020.md) — nominal and error black-box test generation from Swagger/OpenAPI plus automated oracles.
- [RESTler](../references/restler-icse-2019.md) — stateful sequence generation by inferring producer-consumer dependencies from API specifications.
- [RESTest](../references/restest-icsoc-2020.md) — constraint-based generation for inter-parameter dependencies missing from plain OAS.
- [EvoMaster](../references/evomaster-tosem-2019.md) — adjacent search-based/white-box automated REST test generation; useful for sequence/search strategy, not a pure OAS-only method.

## Tier B — strategy and agent-workflow sources

- [Practical Test Pyramid](../references/practical-test-pyramid.md)
- [QA Skills Agent Catalog](../references/qa-skills-agent-catalog.md)
- [Agentic QA Boilerplate](../references/agentic-qa-boilerplate.md)

## Admission rule

A Java QA source may become foundation only if it is one of:

1. official framework or tool documentation;
2. standards or recognized testing syllabus material;
3. mature professional material with clear caveats;
4. internal source of truth for product behavior, test data, environments, or CI.

## Source usage rule

Tool docs define tool behavior. Product requirements and internal API contracts define expected system behavior.

Open-source agent repositories may define useful skill taxonomy, workflow shape, and prompt packaging patterns, but they do not override official framework documentation or internal product contracts.
