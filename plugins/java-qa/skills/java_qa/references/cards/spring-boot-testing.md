---
artifact_type: reference
authority_tier: Tier A
status: foundation
source_type: official-docs
topics: [java, testing, spring-boot, slice-tests, integration-testing]
domains: [java-qa]
owner: Spring Team (VMware/Broadcom)
last_checked: 2026-06-17
source_url: https://docs.spring.io/spring-boot/reference/testing/index.html
---

# Reference: Spring Boot Testing

**Tier A · official-docs · https://docs.spring.io/spring-boot/reference/testing/** — тест-поддержка Spring Boot: slices, context cache, auto-config.

## Use for
- Тест Spring-сервиса на нужном уровне: web-слой, persistence-слой, или полный контекст.
- Provider contract-тест контроллера (web slice + реальный Jackson).
- Integration-тест полного приложения (часто + Testcontainers).

## Выбор уровня (cheapest sufficient)
| Аннотация | Поднимает | Когда |
|---|---|---|
| `@WebMvcTest(X.class)` | только MVC-слой + указанный контроллер | проверить статусы/JSON/валидацию/маппинг — **provider contract-тест** |
| `@DataJpaTest` / `@JdbcTest` | persistence + embedded/TC БД | репозитории, SQL, маппинг сущностей |
| `@JsonTest` | Jackson-конфиг | сериализация одного DTO (round-trip) |
| `@SpringBootTest` | **весь контекст** | полный wiring, реальная интеграция |
| `@RestClientTest` | REST-клиент + MockRestServiceServer | тест исходящего клиента |

## Key decisions & gotchas
- **Context cache:** Spring кэширует ApplicationContext между тестами по **сигнатуре конфигурации**. Каждая уникальная комбинация (`@MockBean`, `@TestPropertySource`, profiles, slices) = новый контекст = дорого. Минимизируй вариативность конфигов → быстрее suite.
- **`@MockBean`/`@SpyBean` ломают кэш** — каждый набор моков создаёт новый контекст. Использовать экономно; в SB 3.4+ есть `@MockitoBean`/`@MockitoSpyBean` (новые, замена `@MockBean`).
- **`@DirtiesContext` — дорого:** выкидывает контекст из кэша. Применять только когда тест реально портит контекст, не «на всякий случай».
- **`@WebMvcTest` НЕ грузит** `@Service`/`@Repository` — коллабораторы мокать (`@MockitoBean`). Security-фильтры подключаются — учитывать (или `@AutoConfigureMockMvc(addFilters=false)`).
- **MockMvc vs WebTestClient vs REST Assured MockMvc:** MockMvc — классика для MVC; WebTestClient — для WebFlux и как унифицированный; REST Assured умеет работать поверх MockMvc.
- **`@SpringBootTest(webEnvironment=RANDOM_PORT)`** + `TestRestTemplate`/`WebTestClient` — реальный HTTP-стек (полнее, чем MOCK).
- **Testcontainers:** `@ServiceConnection` (SB 3.1+) вместо ручного проброса; `@DynamicPropertySource` для остального.

## Minimal pattern (provider contract via web slice)
```java
@WebMvcTest(ClientController.class)
class ClientControllerContractTest {
  @Autowired MockMvc mvc;
  @MockitoBean ClientService service; // collaborator
  @Test void notEnoughMoney_maps_to_402_with_string_status() throws Exception {
    when(service.hold(any())).thenReturn(HoldResult.notEnoughMoney());
    mvc.perform(post("/api/v1/holds").contentType(APPLICATION_JSON).content("{...}"))
       .andExpect(status().is(402))
       .andExpect(jsonPath("$.status").value("NOT_ENOUGH_MONEY")); // string, not ordinal
  }
}
```

## Version-sensitive
- `@MockitoBean`/`@MockitoSpyBean` — Spring Framework 6.2 / Spring Boot 3.4+ (предпочесть над `@MockBean`, которая deprecated).
- `@ServiceConnection` — SB 3.1+.
- JUnit5 (Jupiter) — дефолт начиная с SB 2.2; `spring-boot-starter-test` тащит JUnit5 + AssertJ + Mockito + JSONassert + Hamcrest.

## Anti-patterns
- `@SpringBootTest` там, где хватило бы slice (медленно, грузит весь контекст).
- `@DirtiesContext` без реальной порчи контекста.
- Десятки разных `@MockBean`-комбинаций → cache-busting, suite ползёт.
- Проверять только `200 OK` в web-тесте вместо тела/статуса/контракта.

## Do not use for
Чистая логика без Spring (→ plain JUnit). Кросс-сервисная совместимость (→ Pact/contract). Реальная БД-поведение (→ + Testcontainers).
