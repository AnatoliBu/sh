# Agent KB CI Report

Generated at: `2026-06-16T08:14:18Z`
Git SHA: `daf5d62befdef56593ebe9548dcc96c69040df0d`
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
Generated curated graph: 57 nodes and 252 edges

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

6 vulnerabilities (2 moderate, 4 high)

To address issues that do not require attention, run:
  npm audit fix

To address all issues (including breaking changes), run:
  npm audit fix --force

Run `npm audit` for details.

 Quartz v4.5.2  

Cleaned output directory `public` in 1ms
Found 56 input files from `content` in 47ms
Parsing input files using 1 threads

Warning: content/analytics/agent.md isn't yet tracked by git, dates will be inaccurate

Warning: content/analytics/skills/funnel-analysis.md isn't yet tracked by git, dates will be inaccurate

Warning: content/analytics/skills/metric-reconciliation.md isn't yet tracked by git, dates will be inaccurate

Warning: content/analytics/skills/sql-review.md isn't yet tracked by git, dates will be inaccurate

Warning: content/analytics/sources.md isn't yet tracked by git, dates will be inaccurate

Warning: content/index.md isn't yet tracked by git, dates will be inaccurate

Warning: content/java-qa/agent.md isn't yet tracked by git, dates will be inaccurate

Warning: content/java-qa/rules/automation-decision-quality-gates.md isn't yet tracked by git, dates will be inaccurate

Warning: content/java-qa/rules/flaky-test-control.md isn't yet tracked by git, dates will be inaccurate

Warning: content/java-qa/rules/test-code-quality.md isn't yet tracked by git, dates will be inaccurate

Warning: content/java-qa/skills/agentic-qa-tooling-design.md isn't yet tracked by git, dates will be inaccurate

Warning: content/java-qa/skills/api-and-contract-testing.md isn't yet tracked by git, dates will be inaccurate

Warning: content/java-qa/skills/junit-java-test-design.md isn't yet tracked by git, dates will be inaccurate

Warning: content/java-qa/skills/qa-automation-decision-flow.md isn't yet tracked by git, dates will be inaccurate

Warning: content/java-qa/skills/test-suite-architecture.md isn't yet tracked by git, dates will be inaccurate

Warning: content/java-qa/skills/ui-automation-selenium.md isn't yet tracked by git, dates will be inaccurate

Warning: content/java-qa/sources.md isn't yet tracked by git, dates will be inaccurate

Warning: content/java-qa/workflows/automation-review.md isn't yet tracked by git, dates will be inaccurate

Warning: content/java-qa/workflows/qa-automation-architecture-decision.md isn't yet tracked by git, dates will be inaccurate

Warning: content/references/README.md isn't yet tracked by git, dates will be inaccurate

Warning: content/references/TEMPLATE.md isn't yet tracked by git, dates will be inaccurate

Warning: content/references/agentic-qa-boilerplate.md isn't yet tracked by git, dates will be inaccurate

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

Warning: content/references/mermaid-docs.md isn't yet tracked by git, dates will be inaccurate

Warning: content/references/mockito-docs.md isn't yet tracked by git, dates will be inaccurate

Warning: content/references/netbox.md isn't yet tracked by git, dates will be inaccurate

Warning: content/references/pact-docs.md isn't yet tracked by git, dates will be inaccurate

Warning: content/references/playwright-best-practices.md isn't yet tracked by git, dates will be inaccurate

Warning: content/references/practical-test-pyramid.md isn't yet tracked by git, dates will be inaccurate

Warning: content/references/qa-skills-agent-catalog.md isn't yet tracked by git, dates will be inaccurate

Warning: content/references/rest-assured-docs.md isn't yet tracked by git, dates will be inaccurate

Warning: content/references/selenium-webdriver-docs.md isn't yet tracked by git, dates will be inaccurate

Warning: content/references/spring-framework-testing.md isn't yet tracked by git, dates will be inaccurate

Warning: content/references/terraform-mcp.md isn't yet tracked by git, dates will be inaccurate

Warning: content/references/testcontainers-java-docs.md isn't yet tracked by git, dates will be inaccurate

Warning: content/references/wiremock-java-docs.md isn't yet tracked by git, dates will be inaccurate

Warning: content/roadmap.md isn't yet tracked by git, dates will be inaccurate

Warning: content/shared/rules/bullshit-check.md isn't yet tracked by git, dates will be inaccurate

Warning: content/shared/rules/diagram-usage.md isn't yet tracked by git, dates will be inaccurate

Warning: content/shared/rules/global-rules.md isn't yet tracked by git, dates will be inaccurate

Warning: content/sysadmin/agent.md isn't yet tracked by git, dates will be inaccurate

Warning: content/sysadmin/skills/dns-debug.md isn't yet tracked by git, dates will be inaccurate

Warning: content/sysadmin/skills/incident-triage.md isn't yet tracked by git, dates will be inaccurate

Warning: content/sysadmin/skills/k8s-manifest-review.md isn't yet tracked by git, dates will be inaccurate

Warning: content/sysadmin/skills/terraform-plan-review.md isn't yet tracked by git, dates will be inaccurate

Warning: content/sysadmin/skills/tls-cert-debug.md isn't yet tracked by git, dates will be inaccurate

Warning: content/sysadmin/sources.md isn't yet tracked by git, dates will be inaccurate
Parsed 56 Markdown files in 917ms
Filtered out 0 files in 148μs
Emitting files
Emitted 82 files to `public` in 265ms
Done processing 56 files in 1s

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
Linting: 70 file(s)
Summary: 0 error(s)

```
