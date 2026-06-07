# Agent KB CI Report

Generated at: `2026-06-07T10:30:40Z`
Git SHA: `e3bfe42534a98232a4f473f843e7686feccd39fc`
Quartz engine: `AnatoliBu/quartz`
Quartz branch: `agent-kb-v5`

## Summary

- **PASS** — Validate domain package structure
- **PASS** — Validate wiki links
- **FAIL** — Validate frontmatter
- **PASS** — Validate agent artifact references
- **PASS** — Build curated link graph
- **FAIL** — Build Quartz site
- **PASS** — Markdown lint

## Details

### PASS: Validate domain package structure

Command:

```bash
python sysadmin-analytics-agent-kb/tools/validate_structure.py
```

Output:

```text
Structure validation passed

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

### FAIL: Validate frontmatter

Command:

```bash
python sysadmin-analytics-agent-kb/tools/validate_frontmatter.py
```

Output:

```text
Frontmatter validation failed:
- analytics/sources.md: missing YAML frontmatter
- sysadmin/sources.md: missing YAML frontmatter

```

### PASS: Validate agent artifact references

Command:

```bash
python sysadmin-analytics-agent-kb/tools/validate_agent_artifact_references.py
```

Output:

```text
Agent artifact reference validation passed

```

### PASS: Build curated link graph

Command:

```bash
python sysadmin-analytics-agent-kb/tools/build_link_graph.py
```

Output:

```text
Generated curated graph: 27 nodes and 71 edges

```

### FAIL: Build Quartz site

Command:

```bash
bash sysadmin-analytics-agent-kb/tools/build_quartz_site.sh
```

Output:

```text
QUARTZ_REPO_TOKEN is required to clone private repo AnatoliBu/quartz.git

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
Linting: 50 file(s)
Summary: 0 error(s)

```
