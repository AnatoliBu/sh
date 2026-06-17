---
artifact_type: reference
authority_tier: Tier A
status: foundation
source_type: official-docs
topics: [java, testing, testcontainers, integration-testing]
domains: [java-qa]
owner: Testcontainers Project
last_checked: 2026-06-07
source_url: https://java.testcontainers.org/
---

# Reference: Testcontainers for Java

**Tier A · official-docs · https://java.testcontainers.org/** — реальные зависимости (БД/брокеры/сервисы) в Docker на время теста.

## Use for
- Integration-тесты против **реальных** MySQL/Postgres/Cassandra/Redis/Kafka вместо моков/embedded.
- Проверка миграций, SQL-диалекта, сериализации, транзакций, реальных сайд-эффектов (списание баллов и т.п.).
- Контейнеризация внешнего сервиса под provider/contract-проверку.

## Key decisions & gotchas
- **Lifecycle:** `@Container` static = один контейнер на класс (быстро, общий стейт); instance = на каждый тест (изоляция, медленно). Выбирать осознанно.
- **Reuse** (`.withReuse(true)` + `testcontainers.reuse.enable=true`) резко ускоряет локально; в CI обычно off.
- **Wait strategies — критично:** не `Thread.sleep`, а `Wait.forListeningPort()`/`forLogMessage()`/`forHttp()`. Иначе флаки на старте.
- **Singleton-контейнер** (static в базовом классе, без Spring) — частый паттерн для шеринга тяжёлой БД между классами.
- **Networking:** `Network.newNetwork()` + `withNetworkAliases` для контейнер↔контейнер; `getMappedPort()` для хоста (порт случайный, не хардкодить).
- **Spring Boot 3.1+:** `@ServiceConnection` автоматически прокидывает datasource/kafka в контекст — не нужен ручной `@DynamicPropertySource`.
- **Ryuk** (reaper) чистит контейнеры; в части CI/rootless-docker его отключают (`TESTCONTAINERS_RYUK_DISABLED`) — тогда чистить самим.
- Требует Docker в CI-агенте (docker-in-docker / socket).

## Minimal pattern (Spring Boot 3.1+)
```java
@SpringBootTest
@Testcontainers
class OrderRepositoryIT {
  @Container @ServiceConnection
  static MySQLContainer<?> db = new MySQLContainer<>("mysql:8.4");
  @Test void persists() { /* real DB, assert state */ }
}
```

## Version-sensitive
- `@ServiceConnection` — Spring Boot ≥3.1. На SB <3.1 — `@DynamicPropertySource`.
- Образы пинить по тегу (`mysql:8.4`, не `latest`) для воспроизводимости.
- JUnit5: `@Testcontainers` extension; JUnit4 — `@Rule`.

## Anti-patterns
- `latest`-теги образов; `Thread.sleep` вместо wait strategy.
- Контейнер на каждый тест без надобности (медленный CI).
- Контейнеризировать ВСЁ «на всякий случай» — только то, чьё реальное поведение проверяется.

## Do not use for
Чистая логика (→ unit). Контрактная совместимость провайдер/консьюмер (→ Pact/contract-тест). UI (→ Selenium/Playwright).
