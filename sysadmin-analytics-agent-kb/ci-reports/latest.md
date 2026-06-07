# Agent KB CI Report

Generated at: `2026-06-07T11:17:11Z`
Git SHA: `126048be2ee114d53131a6fa4212d4ebf122be9d`
Quartz engine: `AnatoliBu/quartz`
Quartz branch: `agent-kb-v5`

## Summary

- **PASS** — Validate domain package structure
- **PASS** — Validate wiki links
- **PASS** — Validate frontmatter
- **PASS** — Validate agent artifact references
- **PASS** — Build curated link graph
- **PASS** — Build Quartz site
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
Generated curated graph: 48 nodes and 189 edges

```

### PASS: Build Quartz site

Command:

```bash
bash sysadmin-analytics-agent-kb/tools/build_quartz_site.sh
```

Output:

```text
Cloning into '/home/runner/work/sh/sh/quartz-work'...

added 492 packages, and audited 493 packages in 10s

182 packages are looking for funding
  run `npm fund` for details

4 vulnerabilities (3 moderate, 1 high)

To address all issues, run:
  npm audit fix

Run `npm audit` for details.

 Quartz v4.5.2  

Cleaned output directory `public` in 1ms
Found 47 input files from `content` in 56ms
Parsing input files using 1 threads

Warning: content/analytics/agent.md isn't yet tracked by git, dates will be inaccurate

Warning: content/analytics/skills/funnel-analysis.md isn't yet tracked by git, dates will be inaccurate

Warning: content/analytics/skills/metric-reconciliation.md isn't yet tracked by git, dates will be inaccurate

Warning: content/analytics/skills/sql-review.md isn't yet tracked by git, dates will be inaccurate

Warning: content/analytics/sources.md isn't yet tracked by git, dates will be inaccurate

Warning: content/index.md isn't yet tracked by git, dates will be inaccurate

Warning: content/java-qa/agent.md isn't yet tracked by git, dates will be inaccurate

Warning: content/java-qa/rules/flaky-test-control.md isn't yet tracked by git, dates will be inaccurate

Warning: content/java-qa/rules/test-code-quality.md isn't yet tracked by git, dates will be inaccurate

Warning: content/java-qa/skills/api-and-contract-testing.md isn't yet tracked by git, dates will be inaccurate

Warning: content/java-qa/skills/junit-java-test-design.md isn't yet tracked by git, dates will be inaccurate

Warning: content/java-qa/skills/test-suite-architecture.md isn't yet tracked by git, dates will be inaccurate

Warning: content/java-qa/skills/ui-automation-selenium.md isn't yet tracked by git, dates will be inaccurate

Warning: content/java-qa/sources.md isn't yet tracked by git, dates will be inaccurate

Warning: content/java-qa/workflows/automation-review.md isn't yet tracked by git, dates will be inaccurate

Warning: content/references/README.md isn't yet tracked by git, dates will be inaccurate

Warning: content/references/TEMPLATE.md isn't yet tracked by git, dates will be inaccurate

Warning: content/references/assertj-docs.md isn't yet tracked by git, dates will be inaccurate

Warning: content/references/google-sre-incident-management.md isn't yet tracked by git, dates will be inaccurate

Warning: content/references/gradle-java-testing.md isn't yet tracked by git, dates will be inaccurate

Warning: content/references/internal-certificate-management.md isn't yet tracked by git, dates will be inaccurate

Warning: content/references/internal-dns-source-of-truth.md isn't yet tracked by git, dates will be inaccurate

Warning: content/references/internal-event-taxonomy.md isn't yet tracked by git, dates will be inaccurate

Warning: content/references/internal-metric-catalog.md isn't yet tracked by git, dates will be inaccurate

Warning: content/references/istqb-testing-foundation.md isn't yet tracked by git, dates will be inaccurate

Warning: content/references/junit-user-guide.md isn't yet tracked by git, dates will be inaccurate

Warning: content/references/kubernetes-pod-security-standards.md isn't yet tracked by git, dates will be inaccurate

Warning: content/references/mockito-docs.md isn't yet tracked by git, dates will be inaccurate

Warning: content/references/netbox.md isn't yet tracked by git, dates will be inaccurate

Warning: content/references/pact-docs.md isn't yet tracked by git, dates will be inaccurate

Warning: content/references/practical-test-pyramid.md isn't yet tracked by git, dates will be inaccurate

Warning: content/references/rest-assured-docs.md isn't yet tracked by git, dates will be inaccurate

Warning: content/references/selenium-webdriver-docs.md isn't yet tracked by git, dates will be inaccurate

Warning: content/references/spring-framework-testing.md isn't yet tracked by git, dates will be inaccurate

Warning: content/references/terraform-mcp.md isn't yet tracked by git, dates will be inaccurate

Warning: content/references/testcontainers-java-docs.md isn't yet tracked by git, dates will be inaccurate

Warning: content/references/wiremock-java-docs.md isn't yet tracked by git, dates will be inaccurate

Warning: content/roadmap.md isn't yet tracked by git, dates will be inaccurate

Warning: content/shared/rules/bullshit-check.md isn't yet tracked by git, dates will be inaccurate

Warning: content/shared/rules/global-rules.md isn't yet tracked by git, dates will be inaccurate

Warning: content/sysadmin/agent.md isn't yet tracked by git, dates will be inaccurate

Warning: content/sysadmin/skills/dns-debug.md isn't yet tracked by git, dates will be inaccurate

Warning: content/sysadmin/skills/incident-triage.md isn't yet tracked by git, dates will be inaccurate

Warning: content/sysadmin/skills/k8s-manifest-review.md isn't yet tracked by git, dates will be inaccurate

Warning: content/sysadmin/skills/terraform-plan-review.md isn't yet tracked by git, dates will be inaccurate

Warning: content/sysadmin/skills/tls-cert-debug.md isn't yet tracked by git, dates will be inaccurate

Warning: content/sysadmin/sources.md isn't yet tracked by git, dates will be inaccurate
Parsed 47 Markdown files in 792ms
Filtered out 0 files in 108μs
Emitting files
Emitted 73 files to `public` in 290ms
Done processing 47 files in 1s

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
Linting: 61 file(s)
Summary: 0 error(s)

```
