---
name: browser_automation
description: >
  Экспертная методология production browser automation: Playwright state machines, cloud browser,
  Browserbase/Browserless/Steel, Stagehand, browser-use, human takeover, login/MFA/2FA, CAPTCHA,
  persistent profiles, payment checkout и 3DS, retries, idempotency, traces и secret redaction.
  Use when: «автоматизируй сайт/checkout», «сделай cloud browser», «нужен Playwright flow»,
  «передай браузер пользователю для логина/2FA/3DS», «падает из-за captcha/anti-bot»,
  «выбери Browserbase vs Browserless vs Steel», «стабилизируй browser agent», browser automation,
  human handoff, authenticated browser, payment flow, session reliability.
---

# Browser Automation

Строй браузерную автоматизацию как наблюдаемый state machine: детерминированный код по умолчанию,
agentic/semantic слой только на реально нестабильных участках, human handoff как штатное состояние.

## Что читать когда

| Файл | Когда |
|---|---|
| [references/architecture.md](references/architecture.md) | Выбрать Playwright vs agentic layer, local vs cloud browser, persistent vs ephemeral session, provider abstraction. |
| [references/reliability.md](references/reliability.md) | Стабилизировать локаторы, retries, post-conditions, idempotency, traces и regression suite. |
| [references/human-handoff-auth.md](references/human-handoff-auth.md) | Login/MFA/2FA/CAPTCHA/3DS, live takeover, session persistence, payment-secret boundary. |
| [references/rules.md](references/rules.md) | Гейты безопасности и stop conditions, особенно для authenticated/payment workflows. |
| [references/workflow.md](references/workflow.md) | Сквозной порядок: human path -> deterministic flow -> handoff -> hardening -> provider benchmark. |
| `references/cards/` | Authority: Playwright, Browserbase, Browserless, Steel, Stagehand, browser-use, OWASP, PCI DSS. |

## Базовая развилка

```text
известный повторяемый UI           -> Playwright state machine
селекторы дороги/интерфейс плавает -> узкий Stagehand/browser-use участок
нужен удалённый browser/handoff    -> provider adapter + Browserbase/Browserless/Steel
login/MFA/3DS                      -> human takeover в ТОМ ЖЕ session
CAPTCHA                            -> permitted provider handling -> human -> stop
финальное списание/изменение плана -> explicit gate + verify target/amount + reconcile
```

## Порядок работы

1. Сначала описать бизнес-состояния и необратимые переходы.
2. Один раз пройти happy path человеком и зафиксировать страницы/frames/popups без секретов.
3. Реализовать максимум детерминированно на Playwright.
4. После каждого действия проверять бизнес post-condition.
5. Добавить typed failures и разные политики retry.
6. Login/MFA/consent/3DS вынести в provider-independent human handoff.
7. Только затем пробовать agentic/semantic слой на тех шагах, где он реально снижает fragility.
8. Ввести redaction, TTL и cleanup до подключения настоящих credentials/payment data.
9. Прогнать одинаковую scenario suite на кандидатах cloud browser.
10. Повторяющийся успешный exploratory flow превратить в deterministic merchant adapter.

## Жёсткие инварианты

- Не хранить password/TOTP seed/PAN/CVV в чатах, логах, traces, screenshots или обычной БД.
- Не делать blind retry после неоднозначного payment submit.
- Не размазывать SDK cloud-browser provider по business logic.
- Не использовать fingerprint/proxy rotation как замену корректной account/session continuity.
- CAPTCHA/anti-bot не превращать в гонку обходов: только разрешённый workflow, human handoff или stop.
