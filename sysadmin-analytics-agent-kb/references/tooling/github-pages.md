# Reference: GitHub Pages

## Authority tier

Tier A for GitHub Pages behavior

## Status

foundation-context

## Owner / maintainer

GitHub

## URL

https://docs.github.com/en/pages/getting-started-with-github-pages/what-is-github-pages

## Last checked

2026-06-06

## Scope

Static site hosting from a GitHub repository, GitHub Actions based publishing, project site URL shape, repository visibility constraints, and Pages access control limitations.

## Why trusted

This is official GitHub documentation for GitHub Pages.

## Caveats

GitHub Pages availability depends on account plan and repository visibility. GitHub documentation states that Pages is available for public repositories with GitHub Free and for public/private repositories with GitHub Pro, Team, Enterprise Cloud, and Enterprise Server.

Private Pages access control is an Enterprise Cloud feature for organization project sites. Do not publish sensitive internal docs publicly by accident.

## Skills that may consume this reference

None directly. This is tooling infrastructure.

## Agents that may consume this reference

- [Sysadmin / SRE / Network Assistant](../../agents/sysadmin-agent.md)
- [Data / Product Analytics Assistant](../../agents/analytics-agent.md)

## Extracted rules

- Before enabling public GitHub Pages, confirm that the knowledge base contains no secrets, real topology, production service names, credentials, or sensitive internal runbooks.
- If the repository or organization cannot publish private Pages, prefer local Quartz preview or restricted hosting.
- Use GitHub Actions for deployment so validation can run before publication.

## Do not use this source for

- Quartz configuration details.
- Access control outside GitHub Pages.
- Enterprise policy decisions.

## Related references

- [Quartz](./quartz.md)

## Notes

This card exists so deployment plans can link to a local reference rather than directly to GitHub docs.
