# Agent KB CI Report

Generated at: `2026-06-07T10:39:16Z`
Git SHA: `5e478171e8663000dd543ad6edbb7aaae291b93b`
Quartz engine: `AnatoliBu/quartz`
Quartz branch: `agent-kb-v5`

## Summary

- **PASS** — Validate domain package structure
- **PASS** — Validate wiki links
- **PASS** — Validate frontmatter
- **PASS** — Validate agent artifact references
- **PASS** — Build curated link graph
- **FAIL** — Build Quartz site
- **FAIL** — Markdown lint

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

### PASS: Validate frontmatter

Command:

```bash
python sysadmin-analytics-agent-kb/tools/validate_frontmatter.py
```

Output:

```text
Frontmatter validation passed

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
Cloning into '/home/runner/work/sh/sh/quartz-work'...
remote: Repository not found.
fatal: repository 'https://github.com/AnatoliBu/quartz.git/' not found

```

### FAIL: Markdown lint

Command:

```bash
npx --yes markdownlint-cli2@0.18.1 'sysadmin-analytics-agent-kb/**/*.md'
```

Output:

```text
markdownlint-cli2 v0.18.1 (markdownlint v0.38.0)
Finding: sysadmin-analytics-agent-kb/**/*.md
Linting: 40 file(s)
Summary: 2 error(s)
sysadmin-analytics-agent-kb/analytics/sources.md:8 MD025/single-title/single-h1 Multiple top-level headings in the same document [Context: "Analytics / Product Analytics ..."]
sysadmin-analytics-agent-kb/sysadmin/sources.md:8 MD025/single-title/single-h1 Multiple top-level headings in the same document [Context: "Sysadmin / SRE / Network Sourc..."]

```
