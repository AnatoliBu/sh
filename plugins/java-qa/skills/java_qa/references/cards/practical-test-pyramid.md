---
artifact_type: reference
authority_tier: Tier B
status: useful-after-audit
source_type: professional-article
topics: [testing, test-strategy, test-pyramid, automation]
domains: [java-qa]
owner: Martin Fowler site / Ham Vocke
last_checked: 2026-06-07
source_url: https://martinfowler.com/articles/practical-test-pyramid.html
---

# Reference: Practical Test Pyramid

**Tier B · professional-article · Fowler/Vocke** — стратегия портфеля тестов. Адаптировать под риск/архитектуру, не догма.

## Use for
- Решение о пропорциях слоёв: много дешёвых низких, мало дорогих высоких.
- Аргумент против over-investing в E2E/UI там, где хватит нижнего слоя.

## Key ideas
- **Форма:** широкое основание (unit) → component/integration → contract → тонкая верхушка (E2E/UI).
- **Push down:** что можно проверить ниже — проверять ниже (быстрее, стабильнее, точнее диагностика).
- **Каждый слой защищает СВОЁ поведение, не дублирует нижний.** Высокий тест, повторяющий unit-проверку — мусор.
- **«Ice-cream cone»** (перевёрнуто, много ручного/E2E) — анти-форма.
- Имя слоя неважно — важно: что доказывает, что стоит, как часто ломается.

## Адаптация (важный нюанс для нашего контекста)
Классическая пирамида говорит «почти всё в unit». Но при **миграции/контрактных границах** центр тяжести смещается к **contract + component-integration** — потому что риск именно на стыке (сериализация, совместимость), а его unit не видит. Форма следует за риском, не за каноном.

## Anti-patterns
- Ice-cream cone: основной слой — ручное/E2E.
- Дублирование дешёвых проверок на дорогом слое.
- Выбор UI/E2E «потому что нагляднее», а не потому что это правильный слой для поведения.
- Метрика «процент покрытия» как цель вместо «какое поведение защищено».

## Do not use for
Конкретный API инструментов (→ карточки JUnit/Pact/Testcontainers). Это стратегия, не how-to.
