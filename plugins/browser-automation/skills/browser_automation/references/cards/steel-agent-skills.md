# Steel Agent Skills

Official source: https://github.com/steel-dev/skills

First-party coding-agent skills include `steel-browser`, `steel-developer`,
`steel-session-debugging`, `steel-reliability`, and `steel-skill-creator`.

## Agent rules

- Separate doing browser work, developing integrations, debugging sessions, and reliability work.
- Use a reliability playbook for identity, CAPTCHA, pacing, retries, and bot-detection failures.
- Run provider preflight/doctor checks before blaming application logic.
- Convert repeatedly successful exploratory browser work into reusable deterministic workflows.
