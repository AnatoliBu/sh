# Agent KB CI Report

Generated at: `2026-09-16T12:41:50Z`
Git SHA: `ee74246630bdb451c0074cce569b9807cd3cd6dc`
Quartz engine: `AnatoliBu/quartz`
Quartz branch: `agent-kb-v5`

## Summary

- **PASS** — Validate domain package structure
- **PASS** — Validate wiki links
- **PASS** — Validate frontmatter
- **PASS** — Validate agent artifact references
- **PASS** — Build curated link graph
- **PASS** — Validate plugin packages are in sync with domains
- **PASS** — Validate plugin packages are installable
- **PASS** — Validate plugin release reaches installed copies
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
Generated curated graph: 134 nodes and 505 edges

```

### PASS: Validate plugin packages are in sync with domains

Command:

```bash
python sysadmin-analytics-agent-kb/tools/build_plugin_from_domain.py --check
```

Output:

```text
Plugin sync passed (6 package(s))

```

### PASS: Validate plugin packages are installable

Command:

```bash
python sysadmin-analytics-agent-kb/tools/validate_plugin_packages.py
```

Output:

```text
Plugin validation passed (6 package(s))

```

### PASS: Validate plugin release reaches installed copies

Command:

```bash
python sysadmin-analytics-agent-kb/tools/validate_plugin_release.py --base 'HEAD^'
```

Output:

```text
Release validation passed (пакеты не менялись относительно HEAD^)

```

### PASS: Build Quartz site

Command:

```bash
bash sysadmin-analytics-agent-kb/tools/build_quartz_site.sh
```

Output:

```text
urate

Warning: content/analytics/skills/metric-reconciliation.md isn't yet tracked by git, dates will be inaccurate

Warning: content/analytics/skills/sql-review.md isn't yet tracked by git, dates will be inaccurate

Warning: content/analytics/sources.md isn't yet tracked by git, dates will be inaccurate

Warning: content/browser-automation/agent.md isn't yet tracked by git, dates will be inaccurate

Warning: content/browser-automation/rules/browser-automation-safety.md isn't yet tracked by git, dates will be inaccurate

Warning: content/browser-automation/skills/browser-automation-architecture.md isn't yet tracked by git, dates will be inaccurate

Warning: content/browser-automation/skills/browser-flow-reliability.md isn't yet tracked by git, dates will be inaccurate

Warning: content/browser-automation/skills/human-handoff-auth.md isn't yet tracked by git, dates will be inaccurate

Warning: content/browser-automation/sources.md isn't yet tracked by git, dates will be inaccurate

Warning: content/browser-automation/workflows/build-browser-automation.md isn't yet tracked by git, dates will be inaccurate

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

Warning: content/references/mermaid-docs.md isn't yet tracked by git, dates will be inaccurate

Warning: content/references/mockito-docs.md isn't yet tracked by git, dates will be inaccurate

Warning: content/references/model-context-protocol-spec.md isn't yet tracked by git, dates will be inaccurate

Warning: content/references/netbox.md isn't yet tracked by git, dates will be inaccurate

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

Warning: content/references/rest-assured-docs.md isn't yet tracked by git, dates will be inaccurate

Warning: content/references/selenium-webdriver-docs.md isn't yet tracked by git, dates will be inaccurate

Warning: content/references/spring-framework-testing.md isn't yet tracked by git, dates will be inaccurate

Warning: content/references/stagehand-agent-modes.md isn't yet tracked by git, dates will be inaccurate

Warning: content/references/stagehand-v4-2026.md isn't yet tracked by git, dates will be inaccurate

Warning: content/references/steel-agent-skills.md isn't yet tracked by git, dates will be inaccurate

Warning: content/references/steel-browser-docs.md isn't yet tracked by git, dates will be inaccurate

Warning: content/references/terraform-mcp.md isn't yet tracked by git, dates will be inaccurate

Warning: content/references/testcontainers-java-docs.md isn't yet tracked by git, dates will be inaccurate

Warning: content/references/veac-video-editing-as-code.md isn't yet tracked by git, dates will be inaccurate

Warning: content/references/vex-video-editing-agent.md isn't yet tracked by git, dates will be inaccurate

Warning: content/references/video-use-agent-skill.md isn't yet tracked by git, dates will be inaccurate

Warning: content/references/w3c-webauthn-level-3.md isn't yet tracked by git, dates will be inaccurate

Warning: content/references/w3c-webdriver-bidi.md isn't yet tracked by git, dates will be inaccurate

Warning: content/references/webarena-verified.md isn't yet tracked by git, dates will be inaccurate

Warning: content/references/wiremock-java-docs.md isn't yet tracked by git, dates will be inaccurate

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
Parsed 133 Markdown files in 1s
Filtered out 0 files in 128μs
Emitting files
Emitted 172 files to `public` in 295ms
Done processing 133 files in 2s

```

### PASS: Markdown lint

Command:

```bash
npx --yes markdownlint-cli2@0.18.1 'sysadmin-analytics-agent-kb/**/*.md' 'plugins/**/*.md'
```

Output:

```text
markdownlint-cli2 v0.18.1 (markdownlint v0.38.0)
Finding: sysadmin-analytics-agent-kb/**/*.md plugins/**/*.md
Linting: 249 file(s)
Summary: 0 error(s)

```
