---
artifact_type: reference
authority_tier: Tier A
status: foundation
source_type: official-docs
topics: [testing, contract-testing, pact, microservices]
domains: [java-qa]
owner: Pact Foundation
last_checked: 2026-06-07
source_url: https://docs.pact.io/
---

# Reference: Pact (consumer-driven contracts)

**Tier A · official-docs · https://docs.pact.io/** — consumer-driven contract testing для REST/messages.

## Use for
- Несколько **независимых** консьюмеров провайдера с раздельными релизами.
- Проверка, что консьюмер реально парсит то, что провайдер реально отдаёт — без поднятия всей системы.
- Защита от контракт-дрейфа в PR (consumer публикует pact → provider verify).

## Key decisions & gotchas
- **Pact без Broker почти бессмыслен.** Broker (или PactFlow) = источник истины + `can-i-deploy` (безопасно ли катить эту пару версий). Без брокера проще JSON Schema / обычные тесты.
- **Consumer-driven, не provider-wishlist:** контракт = исполняемые примеры РЕАЛЬНО используемого поведения, не полная схема API.
- **Держать контракты loose:** матчеры (type matchers), а не точные значения, где значение не есть поведение. Иначе хрупко.
- **Provider states** («product 42 exists») настраивать через API сервиса / state handlers, НЕ прямой мутацией БД.
- **Не использовать pact как stub** для разработки — это убивает смысл.
- Pact проверяет ТОЛЬКО использованные поля/ветки → не заменяет integration- и schema-проверку.
- Bi-directional (BDCT): consumer публикует pact, provider публикует OpenAPI, брокер сверяет — когда provider verify запустить нельзя.

## Minimal pattern (JVM, JUnit5 consumer)
```java
@ExtendWith(PactConsumerTestExt.class)
@PactTestFor(providerName = "client-service")
class ConsumerPactTest {
  @Pact(consumer = "registration-service")
  V4Pact getClient(PactDslWithProvider b) {
    return b.given("client 42 exists")
      .uponReceiving("get client").path("/client/42").method("GET")
      .willRespondWith().status(200)
        .body(newJsonBody(o -> o.numberType("publicClientId", 42)).build())
      .toPact(V4Pact.class);
  }
  @Test @PactTestFor(pactMethod = "getClient")
  void verify(MockServer mock) { /* call real client against mock.getUrl() */ }
}
```
Provider side: `@Provider("client-service")` + `@PactBroker` + `@TestTemplate` verify; в CI — `can-i-deploy`.

## Version-sensitive
- Pact spec **v4** (≥4.0.0) — улучшенный message-based + plugins (gRPC/protobuf). Целиться в v4.
- pact-jvm требует совместимости JUnit5 платформы; провайдер-verify зависит от версии брокера.

## Anti-patterns
- Pact для одного консьюмера в том же репо-периметре (overkill — хватит shared client + provider contract-тест).
- Provider verification отсутствует (контракт есть, проверки нет — классический smell).
- Точные значения вместо матчеров; описывать в pact весь OpenAPI.

## Do not use for
REST Assured-синтаксис, Selenium, нагрузочное. Не доказывает бизнес-корректность сама по себе.
