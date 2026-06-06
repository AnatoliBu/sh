# Agent KB CI Report

Generated at: `2026-06-06T17:10:15Z`
Git SHA: `27b8472b67d44550aff8e9a3fa6b01b3735e231f`
Quartz engine: `AnatoliBu/quartz`
Quartz branch: `agent-kb-v5`

## Summary

- **PASS** — Validate docs links and reference-card contract
- **PASS** — Validate wiki links
- **FAIL** — Validate frontmatter
- **PASS** — Validate agent artifact references
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

### FAIL: Validate frontmatter

Command:

```bash
python sysadmin-analytics-agent-kb/tools/validate_frontmatter.py
```

Output:

```text
Frontmatter validation failed:
- references/google-sre-incident-management.md: missing frontmatter keys: domain
- references/internal-certificate-management.md: missing frontmatter keys: domain
- references/internal-dns-source-of-truth.md: missing frontmatter keys: domain
- references/internal-event-taxonomy.md: missing frontmatter keys: domain
- references/internal-metric-catalog.md: missing frontmatter keys: domain
- references/kubernetes-pod-security-standards.md: missing frontmatter keys: domain
- references/netbox.md: missing frontmatter keys: domain
- references/terraform-mcp.md: missing frontmatter keys: domain

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
Generated curated graph: 40 nodes and 106 edges

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
