---
artifact_type: reference
authority_tier: Tier A
status: foundation
source_type: official-docs
topics: [java, testing, spring, spring-test]
domains: [java-qa]
owner: Spring Team
last_checked: 2026-06-07
source_url: https://docs.spring.io/spring-framework/reference/testing.html
---

# Reference: Spring Framework Testing (core)

**Tier A · official-docs · https://docs.spring.io/spring-framework/reference/testing.html** — базовый TestContext framework (под Spring Boot test-слоями).

> Для Boot-специфики (slices, `@SpringBootTest`, `@ServiceConnection`, context cache) → карточка [spring-boot-testing.md](spring-boot-testing.md). Эта — про core-механику.

## Use for
- Понимание, что лежит под Boot-аннотациями: TestContext, кэш контекста, транзакции, web-test support.
- Не-Boot Spring проекты.

## Key decisions & gotchas
- **TestContext framework** — ядро: `@ContextConfiguration`/`@SpringJUnitConfig`, кэш контекста по сигнатуре конфигурации (тот же кэш, что эксплуатирует Boot).
- **Транзакции:** `@Transactional` на тесте → **rollback по умолчанию** после каждого теста (откат данных). `@Commit` если нужен коммит. Удобно для изоляции, но не покрывает то, что вне транзакции (триггеры, отдельные коннекты).
- **`@DirtiesContext`** — выкинуть контекст из кэша (дорого).
- **Web:** `MockMvc` (server-side, без сети), `WebTestClient` (реактивный/унифицированный), `MockRestServiceServer` (мок исходящих RestTemplate-вызовов).
- **`@TestPropertySource`/`@ActiveProfiles`** меняют сигнатуру контекста → влияют на кэш.
- **`ApplicationContextInitializer`/`@DynamicPropertySource`** — прокидывание динамических свойств (порты Testcontainers и т.п.).

## Minimal pattern (core, без Boot)
```java
@SpringJUnitConfig(AppConfig.class)
@Transactional // rollback after each test
class RepoTest {
  @Autowired DataSource ds;
  @Test void writesAndRollsBack() { /* ... */ }
}
```

## Version-sensitive
- Spring Framework 6.x (Jakarta namespace `jakarta.*`, не `javax.*`) — Boot 3.x.
- `@MockitoBean`/`@MockitoSpyBean` — SF 6.2+ (замена Boot `@MockBean`).
- JUnit5 интеграция — `SpringExtension` (в `@SpringJUnitConfig`).

## Anti-patterns
- Полный контекст там, где хватит slice (→ см. spring-boot-testing.md).
- Расчёт на `@Transactional`-rollback там, где поведение вне транзакции.
- Множить варианты `@TestPropertySource`/`@MockBean` → cache-busting.

## Do not use for
Boot-slices/auto-config специфику (→ spring-boot-testing.md). Реальная инфра (→ Testcontainers).
