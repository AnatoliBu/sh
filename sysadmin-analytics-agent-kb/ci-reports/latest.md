# Agent KB CI Report

Generated at: `2026-06-06T16:40:07Z`
Git SHA: `6172be0953531c796f084838aab22e9a86a4127d`
Quartz branch: `agent-kb-v5`

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
Generated curated graph: 27 nodes and 58 edges

```

### FAIL: Build Quartz site

Command:

```bash
bash sysadmin-analytics-agent-kb/tools/build_quartz_site.sh
```

Output:

```text
QUARTZ_REPO_TOKEN is missing. Add it as a repository secret with read access to AnatoliBu/quartz.

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
Linting: 37 file(s)
Summary: 0 error(s)

```
