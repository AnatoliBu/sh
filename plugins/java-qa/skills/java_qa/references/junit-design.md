---
artifact_type: skill
status: foundation
domain: java-qa
---

# Skill: JUnit Java Test Design

## Purpose

Design and review Java unit and component tests built around JUnit, AssertJ, and Mockito.

## Reference links

Authority references (⚠ карточки вне установленного ядра cards/ помечены — файла нет, см. ../skill.md):

- [JUnit User Guide](cards/junit-user-guide.md)
- [AssertJ Documentation](cards/assertj-docs.md)
- [Mockito Documentation](cards/mockito-docs.md)
- [ISTQB Testing Foundation Materials](cards/istqb-testing-foundation.md)

## Inputs

- Class or method under test.
- Expected behavior source.
- Edge cases and failure modes.
- Collaborators and side effects.
- Existing test style and naming convention.

## Output

- Test cases grouped by behavior.
- Test data and oracle definition.
- Suggested JUnit features.
- Assertion style.
- Mocking boundary.
- Review notes for maintainability.

## Checklist

1. Identify public behavior, not private implementation.
2. State the expected result before writing assertions.
3. Cover happy path, boundaries, invalid input, and exceptional behavior.
4. Prefer readable domain test data over magic values.
5. Use mocks for collaborators that are slow, unstable, or outside the unit boundary.
6. Avoid verifying every internal call unless the interaction is the behavior.
7. Keep assertion failures diagnostic.

## Naming guidance

Prefer names that describe behavior and condition:

```text
returns_discount_when_customer_is_eligible
rejects_order_when_payment_is_missing
```

## Review smells

- Test name says one thing but assertions check another.
- Too many mocks for a simple behavior.
- Assertions only check non-null or size without business meaning.
- Fixture setup is larger than the behavior being tested.
