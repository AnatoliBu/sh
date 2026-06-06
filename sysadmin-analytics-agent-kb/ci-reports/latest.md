# Agent KB CI Report

Generated at: `2026-06-06T17:12:31Z`
Git SHA: `431dbd39dd1cc261a813efe62fb5f6502b5ef0cc`
Quartz engine: `AnatoliBu/quartz`
Quartz branch: `agent-kb-v5`

## Summary

- **FAIL** — Validate domain package structure
- **PASS** — Validate wiki links
- **FAIL** — Validate frontmatter
- **PASS** — Validate agent artifact references
- **PASS** — Build curated link graph
- **FAIL** — Build Quartz site
- **PASS** — Markdown lint

## Details

### FAIL: Validate domain package structure

Command:

```bash
python sysadmin-analytics-agent-kb/tools/validate_structure.py
```

Output:

```text
Structure validation failed:
- agents/analytics-agent.md: legacy root artifact folder is not allowed
- agents/sysadmin-agent.md: legacy root artifact folder is not allowed
- references/analytics/internal-event-taxonomy.md: categorized references are not allowed; use flat references/*.md
- references/analytics/internal-metric-catalog.md: categorized references are not allowed; use flat references/*.md
- references/sysadmin/google-sre-incident-management.md: categorized references are not allowed; use flat references/*.md
- references/sysadmin/internal-certificate-management.md: categorized references are not allowed; use flat references/*.md
- references/sysadmin/internal-dns-source-of-truth.md: categorized references are not allowed; use flat references/*.md
- references/sysadmin/kubernetes-pod-security-standards.md: categorized references are not allowed; use flat references/*.md
- references/sysadmin/netbox.md: categorized references are not allowed; use flat references/*.md
- references/sysadmin/terraform-mcp.md: categorized references are not allowed; use flat references/*.md
- references/tooling/github-pages.md: categorized references are not allowed; use flat references/*.md
- references/tooling/quartz.md: categorized references are not allowed; use flat references/*.md
- rules/bullshit-check.md: legacy root artifact folder is not allowed
- rules/global-rules.md: legacy root artifact folder is not allowed
- skills/TEMPLATE.md: legacy root artifact folder is not allowed

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
- references/README.md: missing YAML frontmatter
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
