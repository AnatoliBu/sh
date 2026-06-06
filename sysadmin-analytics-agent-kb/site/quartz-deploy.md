# Quartz Deploy Plan

## Reference links

Authority references:

- [Quartz](../references/tooling/quartz.md)
- [GitHub Pages](../references/tooling/github-pages.md)

## Decision

Use Quartz as the human-readable documentation frontend for the agent knowledge base.

Quartz is a good fit because this repo is a linked knowledge graph:

- references point to skills;
- skills point to references;
- agents compose skills;
- rules constrain agents;
- research notes evaluate sources.

Quartz gives backlinks and graph navigation, while CI remains responsible for validation.

## Important safety note

Do not publish sensitive material to a public Pages site.

Before enabling deployment, check whether the target GitHub account/repository supports private Pages. If not, use one of these safer options:

1. local Quartz preview only;
2. Cloudflare Pages or another static host with access control;
3. private GitHub Pages if available;
4. separate sanitized public docs site.

## Architecture

Recommended structure:

```text
sysadmin-analytics-agent-kb/
  references/
  agents/
  rules/
  sysadmin/
  analytics/
  research/
  site/
  tools/
```

Quartz build should treat `sysadmin-analytics-agent-kb/` as content, excluding generated/cache/build folders.

## Deployment pipeline

1. Run docs validation:
   - local links;
   - reference-card requirement;
   - line anchors;
   - wiki links;
   - markdown lint.
2. Generate link graph artifacts.
3. Build Quartz site.
4. Deploy static output only after validation passes.

## Quartz setup approach

Preferred approach:

- keep source docs in `sysadmin-analytics-agent-kb/`;
- add Quartz config under `quartz/` or a separate branch/subtree;
- copy or symlink docs into Quartz `content/` during CI;
- build Quartz;
- deploy built `public/` output.

Avoid making Quartz the source of truth. Markdown source remains the source.

## Graph strategy

Use two graph layers:

1. **Quartz graph** for human exploration.
2. **CI generated graph** for deterministic validation and review artifacts.

The CI graph should be generated from the same Markdown links that validators check.

## Alternative tools considered

### MkDocs Material

Excellent documentation UI, navigation, search, and plugins. Better for polished manuals, worse for backlink-heavy graph exploration.

### Docusaurus

Good for product documentation and versioning. Heavier than needed and not graph-first.

### Obsidian

Excellent local graph and editing experience. Not a deployment target by itself.

### Graphviz

Great for deterministic CI-generated graphs. Not a docs UI. Use it alongside Quartz.

### Graphite

Graphite is mostly associated with stacked PR/code review workflows, not this kind of documentation graph. It is not the primary fit here.

## Verdict

Use Quartz for the docs website and Graphviz/DOT-style generated graph artifacts for CI and reviews.
