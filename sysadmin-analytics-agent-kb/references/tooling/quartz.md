# Reference: Quartz

## Authority tier

Tier A for Quartz-specific behavior

## Status

foundation-context

## Owner / maintainer

Quartz project / jackyzha0

## URL

https://quartz.jzhao.xyz/

## Last checked

2026-06-06

## Scope

Static-site publishing for Markdown knowledge bases, digital gardens, backlinks, local/global graph view, wiki links, search, and readable docs UI.

## Why trusted

Quartz is the upstream documentation for Quartz behavior and deployment. It describes Quartz as a static-site generator that transforms Markdown into a functional website and includes features such as graph view, wiki links, backlinks, search, popover previews, and Obsidian compatibility.

## Caveats

Quartz is a publishing UI, not the authority layer. Source-of-truth references must remain in `references/`, and CI must validate links independently of Quartz rendering.

Quartz 5 graph view is a community plugin, so pin plugin versions and keep dependency updates reviewed.

## Skills that may consume this reference

None directly. This is tooling infrastructure.

## Agents that may consume this reference

- [Sysadmin / SRE / Network Assistant](../../agents/sysadmin-agent.md)
- [Data / Product Analytics Assistant](../../agents/analytics-agent.md)

## Extracted rules

- Use Quartz for human-readable browsing and graph visualization.
- Do not use Quartz as a validator; keep validation in CI.
- Use backlinks and graph view to inspect relationships between references, skills, agents, and rules.
- Keep published content free of secrets and internal production details unless site access is private.

## Do not use this source for

- Source authority ranking.
- Security approval.
- Link validation by itself.
- Private access guarantees.

## Related references

- [GitHub Pages](./github-pages.md)

## Notes

Quartz is a strong fit for this repository because the knowledge base is link-heavy and benefits from backlinks and graph view.
