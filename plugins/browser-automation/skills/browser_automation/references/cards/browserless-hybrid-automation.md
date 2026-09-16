# Browserless Hybrid Automation

Official source: https://docs.browserless.io/baas/monitor-sessions/hybrid-automation

Use this authority for Browserless remote Chromium, CDP/Playwright integration, LiveURL handoff,
CAPTCHA workflow branches, and multi-stage human/automation sessions.

## Agent rules

- Pause, hand the same session to the human, then resume automation after a verified post-condition.
- Never put the Browserless API token into an end-user LiveURL.
- Treat CAPTCHA as a branch: permitted provider handling -> human takeover -> stop.
- Session timeout remains a lifecycle boundary even while a viewer is open.
