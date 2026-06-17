---
artifact_type: reference
authority_tier: Tier A
status: foundation
source_type: official-docs
topics: [java, testing, junit, unit-testing]
domains: [java-qa]
owner: JUnit Team
last_checked: 2026-06-07
source_url: https://junit.org/junit5/docs/current/user-guide/
---

# Reference: JUnit 5 (Jupiter)

**Tier A · official-docs · https://junit.org/junit5/docs/current/user-guide/** — платформа + Jupiter: lifecycle, параметризация, extensions, теги, параллелизм.

## Use for
- Unit/component-тесты Java; база для интеграционных (вместе с Spring/Testcontainers extensions).
- Параметризованные кейсы (таблица входов→ожиданий), сгруппированные сценарии.

## Key decisions & gotchas
- **Lifecycle:** `@BeforeEach`/`@AfterEach` (на тест), `@BeforeAll`/`@AfterAll` (static, на класс). `@TestInstance(PER_CLASS)` снимает static-требование, но шарит состояние — осторожно.
- **Параметризация:** `@ParameterizedTest` + `@CsvSource`/`@MethodSource`/`@EnumSource` — одна логика, много входов. Лучше, чем копипаст тестов.
- **`@Nested`** — группировка по контексту (given-состояние); читаемая структура.
- **Extensions** (`@ExtendWith`) — точка интеграции: Mockito (`MockitoExtension`), Spring (`SpringExtension`), Testcontainers, WireMock. Свои — через `Extension`-API (замена JUnit4 `@Rule`).
- **Теги** (`@Tag("integration")`) — разводят линии CI (fast PR vs nightly). Фильтр в Surefire/Failfast/Gradle.
- **Параллелизм** (`junit.jupiter.execution.parallel.enabled=true` + `@Execution(CONCURRENT)`): требует thread-safe тестов; `@ResourceLock` для общих ресурсов. Включать осознанно.
- **Assumptions** (`assumeTrue`) — пропуск, а не падение, при невыполненном предусловии (env-specific тесты).
- **Не путать с ассертами Hamcrest/AssertJ** — Jupiter assertions базовые; для читаемости предпочесть AssertJ.

## Minimal pattern
```java
@ParameterizedTest
@CsvSource({ "100, ELIGIBLE", "0, REJECTED" })
void discount(int balance, String expected) {
  assertThat(service.evaluate(balance)).isEqualTo(Result.valueOf(expected));
}
```

## Version-sensitive
- JUnit 5 (Jupiter) — отдельные артефакты platform/jupiter/vintage; BOM `junit-bom` фиксирует версии.
- Параллелизм и ряд extension-API эволюционируют по minor — сверять версию перед version-specific фичами.
- `vintage`-engine нужен только для запуска старых JUnit4 тестов.

## Anti-patterns
- Копипаст почти-одинаковых тестов вместо `@ParameterizedTest`.
- Static-состояние между тестами без изоляции (ломает параллелизм/порядок).
- Имя теста об одном, ассерт о другом.

## Do not use for
Сериализация/контракт/реальная БД (→ web slice / contract / Testcontainers). JUnit — каркас, не оракул сам по себе.
