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
