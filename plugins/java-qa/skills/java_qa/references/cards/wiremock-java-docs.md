---
artifact_type: reference
authority_tier: Tier A
status: foundation
source_type: official-docs
topics: [java, testing, wiremock, api-mocking, service-virtualization]
domains: [java-qa]
owner: WireMock Project
last_checked: 2026-06-07
source_url: https://wiremock.org/docs/
---

# Reference: WireMock (service virtualization)

**Tier A · official-docs · https://wiremock.org/docs/** — HTTP-стаб внешних зависимостей: matching, templating, faults, latency, verify.

## Use for
- Заглушить **исходящие** HTTP-зависимости теста (внешний сервис, который нельзя/не нужно звать).
- Симуляция ошибок/таймаутов/латентности для проверки устойчивости (ретраи, fallbacks).
- Record/playback для снятия стабов с реального провайдера.

## Key decisions & gotchas
- **Stub drift — главный риск:** стаб должен отражать РЕАЛЬНЫЙ контракт провайдера. Разъехался — тест зелёный, прод падает. Связывать стабы с контрактом (Pact/schema) или периодически сверять.
- **Matching:** по method/path/headers/query/body (jsonPath, matchesJsonPath, equalToJson с `ignoreExtraElements`). Слишком строгий matcher → хрупко; слишком слабый → ложно-зелёный.
- **Faults/latency:** `Fault.CONNECTION_RESET_BY_PEER`, `withFixedDelay`/`withChunkedDribbleDelay` — тест ретраев/таймаутов (прямо для нашего RestRetryPolicy-кейса: 503/connect-fail).
- **Stateful scenarios:** `inScenario(...).whenScenarioStateIs(...)` — последовательности (например 503 → 200 на ретрае).
- **Response templating** (Handlebars) — динамический ответ от запроса; включать осознанно (`--global-response-templating`).
- **Verify:** `verify(postRequestedFor(...))` — проверить, что/сколько раз вызвали (важно для идемпотентности: ровно 1 вызов).
- **JUnit5:** `WireMockExtension` (предпочесть) вместо legacy `@Rule`.

## Minimal pattern (JUnit5 + retry/idempotency)
```java
@RegisterExtension
static WireMockExtension wm = WireMockExtension.newInstance()
   .options(wireMockConfig().dynamicPort()).build();

wm.stubFor(post("/charge").inScenario("retry")
   .whenScenarioStateIs(STARTED)
   .willReturn(serviceUnavailable()).willSetStateTo("second"));
wm.stubFor(post("/charge").inScenario("retry")
   .whenScenarioStateIs("second").willReturn(ok()));
// after client retry: verify exactly-once business effect
wm.verify(2, postRequestedFor(urlEqualTo("/charge")));
```

## Version-sensitive
- WireMock 3.x: артефакт `org.wiremock:wiremock` (по умолчанию **Jetty 11**); для **Jetty 12** — отдельный артефакт `org.wiremock:wiremock-jetty12`. JUnit5 `WireMockExtension`. Старые `com.github.tomakehurst` — 2.x.
- Templating-флаги и Jetty-версия — зоны несовместимости между 2.x/3.x (и между Jetty 11/12 внутри 3.x).

## Anti-patterns
- Стаб, который никто не сверяет с реальным провайдером (drift).
- `equalToJson` без `ignoreExtraElements` там, где провайдер аддитивно растёт.
- WireMock вместо contract-теста для проверки совместимости (он не верифицирует провайдера).

## Do not use for
Доказательство совместимости с реальным провайдером (→ Pact/contract). Реальная БД (→ Testcontainers).
