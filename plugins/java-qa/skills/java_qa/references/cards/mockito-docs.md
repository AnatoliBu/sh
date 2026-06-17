---
artifact_type: reference
authority_tier: Tier A
status: foundation
source_type: official-docs
topics: [java, testing, mockito, test-doubles]
domains: [java-qa]
owner: Mockito Project
last_checked: 2026-06-07
source_url: https://site.mockito.org/
---

# Reference: Mockito (test doubles)

**Tier A · official-docs · https://site.mockito.org/** — моки/спаи/верификация. Authority по API, НЕ разрешение мокать всё.

## Use for
- Изоляция unit'а от коллабораторов, которые медленные/нестабильные/вне границы.
- Проверка взаимодействия, когда само взаимодействие и есть поведение (отправлено событие, вызван порт).

## Key decisions & gotchas
- **Strict stubs (по умолчанию в `MockitoExtension`):** неиспользованный стаб → `UnnecessaryStubbingException`. Это хорошо — ловит мёртвые стабы. `LENIENT` — только осознанно (codebase местами злоупотребляет — см. наш `@MockitoSettings(strictness=LENIENT)`).
- **Мокать роли, не данные:** мок для сервиса/порта, не для DTO/value-объекта (их строить настоящими).
- **`@Mock`/`@InjectMocks` + `MockitoExtension`** — не `mock()` руками в каждом тесте.
- **ArgumentCaptor** — проверить, ЧТО передали в коллаборатор (а не только что вызвали).
- **`verify(..., times(n))`/`never()`** — важно для идемпотентности (ровно 1 вызов списания).
- **static/final/constructor mocking** — `mockito-inline` (в 5.x встроено в core); `mockStatic`/`mockConstruction` в try-with-resources, иначе утечёт между тестами. Признак запаха дизайна — нужно редко.
- **BDD-стиль** `given(...).willReturn(...)` (BDDMockito) читается лучше.
- **Не `verify` каждый внутренний вызов** — тест станет зеркалом реализации, хрупким.

## Minimal pattern
```java
@ExtendWith(MockitoExtension.class)
class HoldServiceTest {
  @Mock BalancePort balance; @InjectMocks HoldService svc;
  @Test void debits_once() {
    svc.hold(req);
    verify(balance, times(1)).debit(eq(clientId), eq(100)); // exactly once
  }
}
```

## Version-sensitive
- Mockito 5.x: inline-mock-maker по умолчанию (static/final без отдельного артефакта); подняты требования JDK; ByteBuddy/Objenesis версии чувствительны (см. dependencyManagement в parent).
- `MockitoExtension` (JUnit5) — `mockito-junit-jupiter`.

## Anti-patterns
- Мок там, где можно настоящий объект (особенно value/DTO).
- LENIENT по умолчанию вместо точечного.
- `verify` всех внутренних вызовов; много моков на простое поведение.
- Мок типа, который ты не владеешь, без contract-теста (мок ≠ реальное поведение провайдера).

## Do not use for
Сериализация/контракт/реальная БД (→ web slice / Pact / Testcontainers). Не «разрешение» мокать каждую зависимость.
