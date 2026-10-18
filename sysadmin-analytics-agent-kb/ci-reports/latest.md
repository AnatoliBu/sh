# Agent KB CI Report

Generated at: `2026-10-18T12:04:42Z`
Git SHA: `b9d08f2a95bc9ac79391e78a47da167e743c7302`
Quartz engine: `AnatoliBu/quartz`
Quartz branch: `agent-kb-v5`

## Summary

- **PASS** — Validate domain package structure
- **PASS** — Validate wiki links
- **PASS** — Validate frontmatter
- **FAIL** — Validate agent artifact references
- **PASS** — Build curated link graph
- **PASS** — Validate plugin packages are in sync with domains
- **PASS** — Validate plugin packages are installable
- **PASS** — Validate plugin release reaches installed copies
- **PASS** — Build Quartz site
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

### FAIL: Validate agent artifact references

Command:

```bash
python sysadmin-analytics-agent-kb/tools/validate_agent_artifact_references.py
```

Output:

```text
Agent artifact reference validation failed:
- reverse-engineering/skills/cli-recon.md: missing reference section

```

### PASS: Build curated link graph

Command:

```bash
python sysadmin-analytics-agent-kb/tools/build_link_graph.py
```

Output:

```text
Generated curated graph: 146 nodes and 571 edges

```

### PASS: Validate plugin packages are in sync with domains

Command:

```bash
python sysadmin-analytics-agent-kb/tools/build_plugin_from_domain.py --check
```

Output:

```text
Plugin sync passed (7 package(s))

```

### PASS: Validate plugin packages are installable

Command:

```bash
python sysadmin-analytics-agent-kb/tools/validate_plugin_packages.py
```

Output:

```text
Plugin validation passed (7 package(s))

```

### PASS: Validate plugin release reaches installed copies

Command:

```bash
python sysadmin-analytics-agent-kb/tools/validate_plugin_release.py --base 'HEAD^'
```

Output:

```text
Release validation passed (изменены: leanrea, версии не пинятся)

```

### PASS: Build Quartz site

Command:

```bash
bash sysadmin-analytics-agent-kb/tools/build_quartz_site.sh
```

Output:

```text
ll be inaccurate

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

Warning: content/references/aces-2-color-management.md isn't yet tracked by git, dates will be inaccurate

Warning: content/references/aces-idt-capture-guide.md isn't yet tracked by git, dates will be inaccurate

Warning: content/references/agentic-qa-boilerplate.md isn't yet tracked by git, dates will be inaccurate

Warning: content/references/asc-color-decision-list.md isn't yet tracked by git, dates will be inaccurate

Warning: content/references/assertj-docs.md isn't yet tracked by git, dates will be inaccurate

Warning: content/references/browser-use-authentication.md isn't yet tracked by git, dates will be inaccurate

Warning: content/references/browser-use-harness-2026.md isn't yet tracked by git, dates will be inaccurate

Warning: content/references/browser-use-human-2fa.md isn't yet tracked by git, dates will be inaccurate

Warning: content/references/browser-use-repo.md isn't yet tracked by git, dates will be inaccurate

Warning: content/references/browserbase-agent-identity-2026.md isn't yet tracked by git, dates will be inaccurate

Warning: content/references/browserbase-antibot-identity-2026.md isn't yet tracked by git, dates will be inaccurate

Warning: content/references/browserbase-code-mode-2026.md isn't yet tracked by git, dates will be inaccurate

Warning: content/references/browserbase-live-view-contexts.md isn't yet tracked by git, dates will be inaccurate

Warning: content/references/browserbase-stagehand.md isn't yet tracked by git, dates will be inaccurate

Warning: content/references/browsergym.md isn't yet tracked by git, dates will be inaccurate

Warning: content/references/browserless-bap.md isn't yet tracked by git, dates will be inaccurate

Warning: content/references/browserless-captcha-handling.md isn't yet tracked by git, dates will be inaccurate

Warning: content/references/browserless-hybrid-automation.md isn't yet tracked by git, dates will be inaccurate

Warning: content/references/chrome-devtools-agents.md isn't yet tracked by git, dates will be inaccurate

Warning: content/references/chrome-webmcp-security.md isn't yet tracked by git, dates will be inaccurate

Warning: content/references/chrome-webmcp.md isn't yet tracked by git, dates will be inaccurate

Warning: content/references/claude-code-plugin-format.md isn't yet tracked by git, dates will be inaccurate

Warning: content/references/claude-mods-ffmpeg-ops.md isn't yet tracked by git, dates will be inaccurate

Warning: content/references/cli-guidelines-clig.md isn't yet tracked by git, dates will be inaccurate

Warning: content/references/dcamprof-camera-profiling.md isn't yet tracked by git, dates will be inaccurate

Warning: content/references/emvco-3ds-2-3-1.md isn't yet tracked by git, dates will be inaccurate

Warning: content/references/evomaster-tosem-2019.md isn't yet tracked by git, dates will be inaccurate

Warning: content/references/ffmpeg-video-filters.md isn't yet tracked by git, dates will be inaccurate

Warning: content/references/gemini-computer-use.md isn't yet tracked by git, dates will be inaccurate

Warning: content/references/google-sre-incident-management.md isn't yet tracked by git, dates will be inaccurate

Warning: content/references/gradle-java-testing.md isn't yet tracked by git, dates will be inaccurate

Warning: content/references/internal-certificate-management.md isn't yet tracked by git, dates will be inaccurate

Warning: content/references/internal-dns-source-of-truth.md isn't yet tracked by git, dates will be inaccurate

Warning: content/references/internal-event-taxonomy.md isn't yet tracked by git, dates will be inaccurate

Warning: content/references/internal-metric-catalog.md isn't yet tracked by git, dates will be inaccurate

Warning: content/references/istqb-testing-foundation.md isn't yet tracked by git, dates will be inaccurate

Warning: content/references/junit-user-guide.md isn't yet tracked by git, dates will be inaccurate

Warning: content/references/kubernetes-pod-security-standards.md isn't yet tracked by git, dates will be inaccurate

Warning: content/references/leanrea-repo.md isn't yet tracked by git, dates will be inaccurate

Warning: content/references/mermaid-docs.md isn't yet tracked by git, dates will be inaccurate

Warning: content/references/mockito-docs.md isn't yet tracked by git, dates will be inaccurate

Warning: content/references/model-context-protocol-spec.md isn't yet tracked by git, dates will be inaccurate

Warning: content/references/netbox.md isn't yet tracked by git, dates will be inaccurate

Warning: content/references/openapi-test-generation-edoc-2018.md isn't yet tracked by git, dates will be inaccurate

Warning: content/references/opencolorio-docs.md isn't yet tracked by git, dates will be inaccurate

Warning: content/references/owasp-ai-agent-security.md isn't yet tracked by git, dates will be inaccurate

Warning: content/references/owasp-session-management.md isn't yet tracked by git, dates will be inaccurate

Warning: content/references/pact-docs.md isn't yet tracked by git, dates will be inaccurate

Warning: content/references/pci-dss.md isn't yet tracked by git, dates will be inaccurate

Warning: content/references/playwright-agent-runtime-2026.md isn't yet tracked by git, dates will be inaccurate

Warning: content/references/playwright-best-practices.md isn't yet tracked by git, dates will be inaccurate

Warning: content/references/playwright-docs.md isn't yet tracked by git, dates will be inaccurate

Warning: content/references/practical-test-pyramid.md isn't yet tracked by git, dates will be inaccurate

Warning: content/references/qa-skills-agent-catalog.md isn't yet tracked by git, dates will be inaccurate

Warning: content/references/quickrest-icst-2020.md isn't yet tracked by git, dates will be inaccurate

Warning: content/references/rest-assured-docs.md isn't yet tracked by git, dates will be inaccurate

Warning: content/references/restest-icsoc-2020.md isn't yet tracked by git, dates will be inaccurate

Warning: content/references/restler-icse-2019.md isn't yet tracked by git, dates will be inaccurate

Warning: content/references/resttestgen-icst-2020.md isn't yet tracked by git, dates will be inaccurate

Warning: content/references/selenium-webdriver-docs.md isn't yet tracked by git, dates will be inaccurate

Warning: content/references/spring-framework-testing.md isn't yet tracked by git, dates will be inaccurate

Warning: content/references/stagehand-agent-modes.md isn't yet tracked by git, dates will be inaccurate

Warning: content/references/stagehand-v4-2026.md isn't yet tracked by git, dates will be inaccurate

Warning: content/references/steel-agent-skills.md isn't yet tracked by git, dates will be inaccurate

Warning: content/references/steel-browser-docs.md isn't yet tracked by git, dates will be inaccurate

Warning: content/references/terraform-mcp.md isn't yet tracked by git, dates will be inaccurate

Warning: content/references/testcontainers-java-docs.md isn't yet tracked by git, dates will be inaccurate

Warning: content/references/testing-restful-apis-survey-2023.md isn't yet tracked by git, dates will be inaccurate

Warning: content/references/veac-video-editing-as-code.md isn't yet tracked by git, dates will be inaccurate

Warning: content/references/vex-video-editing-agent.md isn't yet tracked by git, dates will be inaccurate

Warning: content/references/video-use-agent-skill.md isn't yet tracked by git, dates will be inaccurate

Warning: content/references/w3c-webauthn-level-3.md isn't yet tracked by git, dates will be inaccurate

Warning: content/references/w3c-webdriver-bidi.md isn't yet tracked by git, dates will be inaccurate

Warning: content/references/webarena-verified.md isn't yet tracked by git, dates will be inaccurate

Warning: content/references/wiremock-java-docs.md isn't yet tracked by git, dates will be inaccurate

Warning: content/reverse-engineering/agent.md isn't yet tracked by git, dates will be inaccurate

Warning: content/reverse-engineering/rules/authorized-analysis.md isn't yet tracked by git, dates will be inaccurate

Warning: content/reverse-engineering/skills/cli-recon.md isn't yet tracked by git, dates will be inaccurate

Warning: content/reverse-engineering/sources.md isn't yet tracked by git, dates will be inaccurate

Warning: content/roadmap.md isn't yet tracked by git, dates will be inaccurate

Warning: content/shared/rules/bullshit-check.md isn't yet tracked by git, dates will be inaccurate

Warning: content/shared/rules/diagram-usage.md isn't yet tracked by git, dates will be inaccurate

Warning: content/shared/rules/global-rules.md isn't yet tracked by git, dates will be inaccurate

Warning: content/shared/rules/skill-delivery.md isn't yet tracked by git, dates will be inaccurate

Warning: content/sysadmin/agent.md isn't yet tracked by git, dates will be inaccurate

Warning: content/sysadmin/skills/dns-debug.md isn't yet tracked by git, dates will be inaccurate

Warning: content/sysadmin/skills/incident-triage.md isn't yet tracked by git, dates will be inaccurate

Warning: content/sysadmin/skills/k8s-manifest-review.md isn't yet tracked by git, dates will be inaccurate

Warning: content/sysadmin/skills/terraform-plan-review.md isn't yet tracked by git, dates will be inaccurate

Warning: content/sysadmin/skills/tls-cert-debug.md isn't yet tracked by git, dates will be inaccurate

Warning: content/sysadmin/sources.md isn't yet tracked by git, dates will be inaccurate

Warning: content/video-color/agent.md isn't yet tracked by git, dates will be inaccurate

Warning: content/video-color/rules/color-pipeline-safety.md isn't yet tracked by git, dates will be inaccurate

Warning: content/video-color/skills/camera-profiling.md isn't yet tracked by git, dates will be inaccurate

Warning: content/video-color/skills/color-correction-shot-matching.md isn't yet tracked by git, dates will be inaccurate

Warning: content/video-color/skills/mask-assisted-grading.md isn't yet tracked by git, dates will be inaccurate

Warning: content/video-color/sources.md isn't yet tracked by git, dates will be inaccurate

Warning: content/video-color/tooling.md isn't yet tracked by git, dates will be inaccurate

Warning: content/video-color/workflows/end-to-end-color-pipeline.md isn't yet tracked by git, dates will be inaccurate
Parsed 145 Markdown files in 2s
Filtered out 0 files in 177μs
Emitting files
Emitted 187 files to `public` in 448ms
Done processing 145 files in 3s

```

### FAIL: Markdown lint

Command:

```bash
npx --yes markdownlint-cli2@0.18.1 'sysadmin-analytics-agent-kb/**/*.md' 'plugins/**/*.md'
```

Output:

```text
markdownlint-cli2 v0.18.1 (markdownlint v0.38.0)
Finding: sysadmin-analytics-agent-kb/**/*.md plugins/**/*.md
Linting: 267 file(s)
Summary: 32 error(s)
plugins/leanrea/skills/leanrea/references/cli-recon.md:7 MD022/blanks-around-headings Headings should be surrounded by blank lines [Expected: 1; Actual: 0; Below] [Context: "## Rules"]
plugins/leanrea/skills/leanrea/references/cli-recon.md:8 MD032/blanks-around-lists Lists should be surrounded by blank lines [Context: "- Work on a copy (`cp -c` on A..."]
plugins/leanrea/skills/leanrea/references/cli-recon.md:17 MD022/blanks-around-headings Headings should be surrounded by blank lines [Expected: 1; Actual: 0; Below] [Context: "## First move: one call each, paste and run"]
plugins/leanrea/skills/leanrea/references/cli-recon.md:19 MD031/blanks-around-fences Fenced code blocks should be surrounded by blank lines [Context: "```sh"]
plugins/leanrea/skills/leanrea/references/cli-recon.md:21 MD031/blanks-around-fences Fenced code blocks should be surrounded by blank lines [Context: "```"]
plugins/leanrea/skills/leanrea/references/cli-recon.md:25 MD031/blanks-around-fences Fenced code blocks should be surrounded by blank lines [Context: "```sh"]
plugins/leanrea/skills/leanrea/references/cli-recon.md:27 MD031/blanks-around-fences Fenced code blocks should be surrounded by blank lines [Context: "```"]
plugins/leanrea/skills/leanrea/references/cli-recon.md:32 MD022/blanks-around-headings Headings should be surrounded by blank lines [Expected: 1; Actual: 0; Below] [Context: "## Router"]
plugins/leanrea/skills/leanrea/references/cli-recon.md:33 MD058/blanks-around-tables Tables should be surrounded by blank lines [Context: "| Target (detect) | Fastest pa..."]
plugins/leanrea/skills/leanrea/references/cli-recon.md:35:527 MD038/no-space-in-code Spaces inside code span elements [Context: "...de the channels, so also run `"]
plugins/leanrea/skills/leanrea/references/cli-recon.md:35:590 MD038/no-space-in-code Spaces inside code span elements [Context: "`. Fuses: `"]
plugins/leanrea/skills/leanrea/references/cli-recon.md:35:246 MD056/table-column-count Table column count [Expected: 2; Actual: 17; Too many cells, extra data will be missing]
plugins/leanrea/skills/leanrea/references/cli-recon.md:41:183 MD038/no-space-in-code Spaces inside code span elements [Context: "...| rg -m1 -A200 'Go buildinf' `"]
plugins/leanrea/skills/leanrea/references/cli-recon.md:54 MD022/blanks-around-headings Headings should be surrounded by blank lines [Expected: 1; Actual: 0; Below] [Context: "## Speed patterns"]
plugins/leanrea/skills/leanrea/references/cli-recon.md:55 MD032/blanks-around-lists Lists should be surrounded by blank lines [Context: "- Strings and imports first. O..."]
plugins/leanrea/skills/leanrea/references/cli-recon.md:62 MD022/blanks-around-headings Headings should be surrounded by blank lines [Expected: 1; Actual: 0; Below] [Context: "## Install (only on request)"]
sysadmin-analytics-agent-kb/reverse-engineering/skills/cli-recon.md:11 MD022/blanks-around-headings Headings should be surrounded by blank lines [Expected: 1; Actual: 0; Below] [Context: "## Rules"]
sysadmin-analytics-agent-kb/reverse-engineering/skills/cli-recon.md:12 MD032/blanks-around-lists Lists should be surrounded by blank lines [Context: "- Work on a copy (`cp -c` on A..."]
sysadmin-analytics-agent-kb/reverse-engineering/skills/cli-recon.md:21 MD022/blanks-around-headings Headings should be surrounded by blank lines [Expected: 1; Actual: 0; Below] [Context: "## First move: one call each, paste and run"]
sysadmin-analytics-agent-kb/reverse-engineering/skills/cli-recon.md:23 MD031/blanks-around-fences Fenced code blocks should be surrounded by blank lines [Context: "```sh"]
sysadmin-analytics-agent-kb/reverse-engineering/skills/cli-recon.md:25 MD031/blanks-around-fences Fenced code blocks should be surrounded by blank lines [Context: "```"]
sysadmin-analytics-agent-kb/reverse-engineering/skills/cli-recon.md:29 MD031/blanks-around-fences Fenced code blocks should be surrounded by blank lines [Context: "```sh"]
sysadmin-analytics-agent-kb/reverse-engineering/skills/cli-recon.md:31 MD031/blanks-around-fences Fenced code blocks should be surrounded by blank lines [Context: "```"]
sysadmin-analytics-agent-kb/reverse-engineering/skills/cli-recon.md:36 MD022/blanks-around-headings Headings should be surrounded by blank lines [Expected: 1; Actual: 0; Below] [Context: "## Router"]
sysadmin-analytics-agent-kb/reverse-engineering/skills/cli-recon.md:37 MD058/blanks-around-tables Tables should be surrounded by blank lines [Context: "| Target (detect) | Fastest pa..."]
sysadmin-analytics-agent-kb/reverse-engineering/skills/cli-recon.md:39:527 MD038/no-space-in-code Spaces inside code span elements [Context: "...de the channels, so also run `"]
sysadmin-analytics-agent-kb/reverse-engineering/skills/cli-recon.md:39:590 MD038/no-space-in-code Spaces inside code span elements [Context: "`. Fuses: `"]
sysadmin-analytics-agent-kb/reverse-engineering/skills/cli-recon.md:39:246 MD056/table-column-count Table column count [Expected: 2; Actual: 17; Too many cells, extra data will be missing]
sysadmin-analytics-agent-kb/reverse-engineering/skills/cli-recon.md:45:183 MD038/no-space-in-code Spaces inside code span elements [Context: "...| rg -m1 -A200 'Go buildinf' `"]
sysadmin-analytics-agent-kb/reverse-engineering/skills/cli-recon.md:58 MD022/blanks-around-headings Headings should be surrounded by blank lines [Expected: 1; Actual: 0; Below] [Context: "## Speed patterns"]
sysadmin-analytics-agent-kb/reverse-engineering/skills/cli-recon.md:59 MD032/blanks-around-lists Lists should be surrounded by blank lines [Context: "- Strings and imports first. O..."]
sysadmin-analytics-agent-kb/reverse-engineering/skills/cli-recon.md:66 MD022/blanks-around-headings Headings should be surrounded by blank lines [Expected: 1; Actual: 0; Below] [Context: "## Install (only on request)"]

```
