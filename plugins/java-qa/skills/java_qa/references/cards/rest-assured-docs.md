---
artifact_type: reference
authority_tier: Tier A
status: foundation
source_type: official-docs
topics: [java, testing, api-testing, rest-assured]
domains: [java-qa]
owner: REST Assured Project
last_checked: 2026-06-07
source_url: https://rest-assured.io/
---

# Reference: REST Assured

**Tier A · official-docs · https://rest-assured.io/** — DSL для тестирования REST API и валидации ответов в Java.

## Use for
- API-тесты против развёрнутого сервиса (given/when/then), проверка статуса/тела/заголовков.
- Поверх MockMvc/WebTestClient (`RestAssuredMockMvc`) — provider contract-тест без сети.
- JSON-schema валидация ответа, извлечение значений (JsonPath) для цепочек.

## Key decisions & gotchas
- **Ассертить поведение, не `200 OK`:** конкретные поля, бизнес-значения, форма ошибки — иначе тест бесполезен.
- **JSON mapper:** REST Assured сам сериализует/десериализует через Jackson/Gson на classpath — конфиг маппера влияет на тесты (даты, unknown props).
- **`RestAssuredMockMvc`** (модуль `spring-mock-mvc`) гоняет контроллер без поднятия сервера — быстрый provider-тест.
- **Спецификации:** `RequestSpecification`/`ResponseSpecification` выносить общий setup (база URL, auth, content-type), не копировать по тестам.
- **Логирование:** `.log().ifValidationFails()` — диагностика без шума.
- **Schema validation:** `matchesJsonSchemaInClasspath(...)` (модуль json-schema-validator) — дёшево фиксирует форму.
- **Auth:** добавлять через спеку/фильтр, не в каждый тест руками.

## Minimal pattern
```java
given().spec(apiSpec).body(req)
.when().post("/api/v1/holds")
.then().statusCode(402)
       .body("status", equalTo("NOT_ENOUGH_MONEY"));
```

## Version-sensitive (зоны, где ломается при смене версии)
- Coordinates: `io.rest-assured:rest-assured` (groupId сменился со старого `com.jayway.restassured`).
- JSON mapper config (Jackson/Gson), фильтры, Kotlin/Groovy-совместимость, модуль `spring-mock-mvc` — версионно-чувствительны. Сверять major перед version-specific синтаксисом.

## Anti-patterns
- Только `statusCode(200)` без проверки тела.
- Копипаст base-URL/auth по каждому тесту вместо спеки.
- Сырой JSON-строкой везде вместо типизированных DTO/билдеров.

## Do not use for
Consumer/provider контракт (→ Pact). UI (→ Selenium/Playwright). Юнит чистой логики (→ JUnit).
