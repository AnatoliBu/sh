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

- [REST Assured Documentation](cards/rest-assured-docs.md)
- [WireMock Java Documentation](cards/wiremock-java-docs.md)
- [Pact Documentation](cards/pact-docs.md)
- [Testcontainers for Java Documentation](cards/testcontainers-java-docs.md)
- [Spring Framework Testing Documentation](cards/spring-framework-testing.md)
- [Spring Boot Testing](cards/spring-boot-testing.md) — slices, `@WebMvcTest` для provider contract-теста

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

## Schema evolution & compatibility (tolerant reader vs fail-fast)

Самая частая ошибка-автопилот: «навесь `@JsonIgnoreProperties(ignoreUnknown=true)` / выключи
`FAIL_ON_UNKNOWN_PROPERTIES`, чтобы не падало». Это маскировка, если применять бездумно.
И обратная крайность — «всегда fail-fast на любом расхождении» — ломает независимый деплой.
Правда в том, **где проходит граница**, и в разделении по ролям.

**Принцип (Postel / Tolerant Reader, Fowler):** будь либерален к тому, что принимаешь,
строг к тому, что от тебя зависит. Применяется ВЫБОРОЧНО, не «везде».

**Термины (две перспективы одного изменения):** добавление поля в ответ — это
**backward-compatible API change** для существующих консьюмеров, и реализуется через
**forward-compatible / tolerant reader** на стороне старого consumer-DTO. Не путать: «backward»
описывает совместимость API для старых клиентов; «forward» — способность старого читателя
переварить новый payload.

| Изменение | Правильно | Почему |
|---|---|---|
| Добавлено поле, которое **этот десериализатор не использует** | **tolerant** | Падать = запретить провайдеру аддитивно расти без синхронного передеплоя консьюмеров |
| **Удалено/переименовано** используемое поле | **fail-fast (тест)** | Breaking change; ⚠ в рантайме `ignoreUnknown` его НЕ ловит (см. ниже) |
| Сменился **тип** существующего поля; **unknown enum** в используемом поле | **fail-fast** | `ignoreUnknown` это и не маскирует — упадёт на десериализации/маппинге |
| Отсутствует **required**-поле | **fail-fast — но его надо реализовать** (см. ниже) | Само не возникнет |

**Сторона, не симметрия:** `ignoreUnknown` нужен тому, кто **десериализует** — но только к полям,
которые **этот десериализатор по контракту не использует**: провайдер к лишнему в **request**,
консьюмер к новым полям в **response**. Не «навесить симметрично везде».

**Jackson-механика — точно, без иллюзий:**
- `@JsonIgnoreProperties(ignoreUnknown=true)` **НЕ рекурсивен**: аннотация на верхнем DTO не
  покрывает вложенные типы (поля-объекты, элементы списков). Нужна политика на каждом nested-DTO,
  либо mix-in, либо **scoped `ObjectMapper`/`ObjectReader` на границе конкретного external-client/
  контракта** (`FAIL_ON_UNKNOWN_PROPERTIES=false`). ⚠ НЕ менять глобальный app-mapper без явной
  compatibility-политики — глобальное отключение скроет лишние поля во ВСЕХ DTO, включая те, где
  fail-fast нужен.
- `ignoreUnknown` **маскирует rename/delete** используемого поля через **тихий дефолт**: пропавшее
  поле станет `null` (объект) или **`0`/`false`** (primitive) — без ошибки. Поэтому semantically
  required поля **не должны быть primitive** (`int`/`boolean`), иначе потеря неотличима от нуля.
- `ignoreUnknown` **НЕ маскирует**: смену типа существующего поля и unknown enum в используемом
  поле — там Jackson упадёт сам.

**fail-fast надо реализовать — он не появляется сам.** Для «required отсутствует»:
- `@JsonProperty(required=true)` + `FAIL_ON_MISSING_CREATOR_PROPERTIES` / `FAIL_ON_NULL_CREATOR_PROPERTIES`
  работают **только для creator-свойств** (конструктор / `@JsonCreator` / record-компоненты), НЕ для
  mutable field/setter DTO — Jackson не валидирует `required` на сеттерах. Значит обязательные поля
  должны идти через конструктор/record (в LP так и есть — `ClientInfoResponse` через `@JsonCreator`).
- Для mutable/field DTO — Bean Validation (`@NotNull` + валидатор) / schema-validation / contract-тест.
- Отказ от primitive для обязательных полей (иначе пропажа = тихий `0`, см. выше).
- `@JsonProperty(required=true)` **сам по себе не универсальная runtime-защита.**

Лучшее место — **provider contract-тест / schema-diff в CI**, а не падение в рантайме прода
(рантайм — последняя линия).

**Rollout-порядок** (иначе tolerant не спасёт): сначала раскатить consumer с tolerant-reader на
ВСЕ релевантные консьюмеры, и только ПОТОМ провайдер начинает отдавать новые поля. Добавить
`ignoreUnknown` в новую версию модели не помогает консьюмеру, уже задеплоенному на старой версии.

**Unknown enum — не всегда fail-fast:** если enum управляет бизнес-веткой — fail-fast. Если это
extension point и консьюмер безопасно показывает `UNKNOWN`/логирует/игнорирует — tolerant легитимна
(`READ_UNKNOWN_ENUM_VALUES_AS_NULL` / default-value). Решать по семантике.

**Главное:** `ignoreUnknown` — это **политика эволюции схемы, НЕ защита и НЕ замена
контракт-теста**. Защиту от рассинхрона даёт тест (provider verify / schema-diff / version-gate),
аннотация лишь решает forward-compat для неиспользуемых аддитивных полей. Не путать инструменты.

## Review smells

- API test checks only status code.
- Stub response no longer matches real provider behavior.
- Contract exists but provider verification is missing.
- Tests require shared mutable environment state.
- Authentication setup hides what the scenario is actually testing.
- `ignoreUnknown=true` / disabled `FAIL_ON_UNKNOWN_PROPERTIES` подан как «фикс падений» вместо
  осознанной политики эволюции — маскирует breaking changes, если не подкреплён контракт-тестом.
- fail-fast на КАЖДОМ новом поле ответа (даже неиспользуемом) — хрупкость, блокирует независимый
  деплой провайдера.
- Решение про эволюцию схемы принято симметрично request=response, без учёта кто десериализует.
