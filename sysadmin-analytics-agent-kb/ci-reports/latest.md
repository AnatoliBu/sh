# Agent KB CI Report

Generated at: `2026-06-06T16:48:52Z`
Git SHA: `6b1c456a049bbcf2c9bb8269edd555574aac1b2d`
Quartz engine: `https://github.com/jackyzha0/quartz.git`
Quartz branch: `v4`

## Summary

- **PASS** — Validate docs links and reference-card contract
- **PASS** — Validate wiki links
- **PASS** — Validate frontmatter
- **PASS** — Build curated link graph
- **FAIL** — Build Quartz site
- **PASS** — Markdown lint

## Details

### PASS: Validate docs links and reference-card contract

Command:

```bash
python sysadmin-analytics-agent-kb/tools/validate_docs.py
```

Output:

```text
Documentation validation passed

```

### PASS: Validate wiki links

Command:

```bash
python sysadmin-analytics-agent-kb/tools/validate_wiki_links.py
```

Output:

```text
Wiki link validation passed

```

### PASS: Validate frontmatter

Command:

```bash
python sysadmin-analytics-agent-kb/tools/validate_frontmatter.py
```

Output:

```text
Frontmatter validation passed

```

### PASS: Build curated link graph

Command:

```bash
python sysadmin-analytics-agent-kb/tools/build_link_graph.py
```

Output:

```text
Generated curated graph: 28 nodes and 58 edges

```

### FAIL: Build Quartz site

Command:

```bash
bash sysadmin-analytics-agent-kb/tools/build_quartz_site.sh
```

Output:

```text
Using Quartz engine: https://github.com/jackyzha0/quartz.git@v4
Cloning into '/home/runner/work/sh/sh/quartz-work'...
sysadmin-analytics-agent-kb/tools/build_quartz_site.sh: line 82: syntax error near unexpected token `)'

```

### PASS: Markdown lint

Command:

```bash
npx --yes markdownlint-cli2@0.18.1 'sysadmin-analytics-agent-kb/**/*.md'
```

Output:

```text
markdownlint-cli2 v0.18.1 (markdownlint v0.38.0)
Finding: sysadmin-analytics-agent-kb/**/*.md
Linting: 38 file(s)
Summary: 0 error(s)

```
