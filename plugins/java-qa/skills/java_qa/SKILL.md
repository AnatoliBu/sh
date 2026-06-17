---
name: java_qa
description: Java QA automation methodology — test design, test-suite architecture, API & consumer-driven contract testing (Pact/Spring Cloud Contract), Testcontainers integration tests, WireMock/REST Assured, JUnit/Mockito/AssertJ unit design, Selenium UI automation, flaky-test control, test-pyramid & CI-lane decisions, and agentic QA tooling. Use when designing/reviewing Java tests, choosing a test layer, planning a suite migration (e.g. monolith→microservice), deciding contract vs integration vs E2E, или when asked "where/how to test", "contract test", "should we automate this".
---

# Java QA Automation

Методология выбора **минимального поддерживаемого** тестового хода, дающего полезную уверенность — не максимизация числа тестов. Цель активации: дизайн/ревью Java-тестов, выбор слоя, архитектура набора, контрактное/интеграционное тестирование, миграция (монолит→сервис), флаки, CI-стратегия.

## Когда что читать (progressive disclosure)

| Файл | Когда |
|---|---|
| [references/decision-flow.md](references/decision-flow.md) | **Главное.** Перед любым решением «автоматизировать ли / какой слой / мигрировать ли». 10-шаговая последовательность + output-формат с вердиктом DO/SPIKE/LATER/DO NOT. |
| [references/contract-testing.md](references/contract-testing.md) | API-тесты, моки сервисов, контейнерные интеграционные, consumer-driven contract (Pact/SCC). Контрактная миграция из монолита. **+ Schema evolution: tolerant reader vs fail-fast, где граница, `ignoreUnknown` ≠ защита.** |
| [references/test-architecture.md](references/test-architecture.md) | Дизайн/ревью структуры набора: какие слои, что в каждом, data/env-стратегия, дубли, флаки. |
| [references/junit-design.md](references/junit-design.md) | Дизайн unit/component-тестов на JUnit + AssertJ + Mockito; именование, границы моков, review-smells. |
| [references/ui-selenium.md](references/ui-selenium.md) | Selenium WebDriver: локаторы, waits, page object, диагностика, когда вообще нужен браузерный слой. |
| [references/agentic-tooling.md](references/agentic-tooling.md) | Экспозиция QA-возможностей как CLI/MCP/agent-инструментов (стабильный вывод, типизированные сбои, redaction). |
| [references/rules.md](references/rules.md) | Quality gates: test code quality, flaky control, 7 ворот решения об автоматизации. Чек перед мерджем. |
| [references/workflows.md](references/workflows.md) | Готовые ревью-процессы: Automation Review (перед мерджем) и Architecture Decision (перед арх. изменением). |

## Authority-карточки по инструментам

`references/cards/` — authority-страницы по ядру (use-for / gotchas / minimal pattern / version-sensitive / anti-patterns):
`pact-docs` · `testcontainers-java-docs` · `rest-assured-docs` · `wiremock-java-docs` · `junit-user-guide` · `mockito-docs` · `practical-test-pyramid` · `spring-framework-testing` · `spring-boot-testing`.

> Часть доков ссылается на неядровые карточки (selenium, assertj, gradle, istqb, playwright, qa-skills-catalog, agentic-qa-boilerplate) — они **не установлены** (выбрано «ядро»). Источник: репо `AnatoliBu/sh` → `sysadmin-analytics-agent-kb/references/` — дотянуть оттуда при необходимости.

## Связки

- Глубокая многошаговая задача (ревью набора, арх. решение, план миграции) → субагент **`java-qa-automation`** (Agent tool).
- Выбор слоя при выборе цепочки расследования: codegraph (структура) → этот skill (стратегия) → реализация.
- Смежные инструменты LP: `newman_testing`, `playwright`, `wiremock_alefbet`, `jenkins_cli`.

## Быстрый старт

1. Сформулируй решение одним предложением (см. decision-flow §1).
2. Назови защищаемое поведение и источник истины (требование/контракт/OpenAPI/инцидент).
3. Выбери самый дешёвый достаточный слой (logic→unit, serialization/mapping→component/API, provider/consumer→contract, real wiring/DB→integration, critical journey→E2E).
4. Прогони через 7 ворот (rules.md) и выдай вердикт по output-формату.
