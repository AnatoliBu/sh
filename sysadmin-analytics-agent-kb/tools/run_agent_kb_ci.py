#!/usr/bin/env python3
from __future__ import annotations

import datetime as dt
import os
import shlex
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
KB = ROOT / "sysadmin-analytics-agent-kb"
REPORT_DIR = KB / "ci-reports"
REPORT_PATH = REPORT_DIR / "latest.md"

CHECKS = [
    {"name": "Validate domain package structure", "cmd": ["python", "sysadmin-analytics-agent-kb/tools/validate_structure.py"]},
    {"name": "Validate wiki links", "cmd": ["python", "sysadmin-analytics-agent-kb/tools/validate_wiki_links.py"]},
    {"name": "Validate frontmatter", "cmd": ["python", "sysadmin-analytics-agent-kb/tools/validate_frontmatter.py"]},
    {"name": "Validate agent artifact references", "cmd": ["python", "sysadmin-analytics-agent-kb/tools/validate_agent_artifact_references.py"]},
    {"name": "Build curated link graph", "cmd": ["python", "sysadmin-analytics-agent-kb/tools/build_link_graph.py"]},
    {"name": "Build Quartz site", "cmd": ["bash", "sysadmin-analytics-agent-kb/tools/build_quartz_site.sh"]},
    {"name": "Markdown lint", "cmd": ["npx", "--yes", "markdownlint-cli2@0.18.1", "sysadmin-analytics-agent-kb/**/*.md"]},
]


def run_check(cmd: list[str], env: dict[str, str]) -> tuple[int, str]:
    proc = subprocess.run(cmd, cwd=ROOT, env=env, text=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    return proc.returncode, proc.stdout


def redact(text: str) -> str:
    for key in ("QUARTZ_REPO_TOKEN", "GITHUB_TOKEN"):
        token = os.environ.get(key, "")
        if token:
            text = text.replace(token, f"***REDACTED_{key}***")
    return text


def main() -> int:
    REPORT_DIR.mkdir(parents=True, exist_ok=True)
    env = os.environ.copy()
    env.setdefault("QUARTZ_BRANCH", "agent-kb-v5")

    started = dt.datetime.utcnow().replace(microsecond=0).isoformat() + "Z"
    sections: list[str] = [
        "# Agent KB CI Report",
        "",
        f"Generated at: `{started}`",
        f"Git SHA: `{env.get('GITHUB_SHA', 'local')}`",
        "Quartz engine: `AnatoliBu/quartz`",
        f"Quartz branch: `{env.get('QUARTZ_BRANCH')}`",
        "",
        "## Summary",
        "",
    ]

    failures = 0
    results: list[tuple[str, int, str, list[str]]] = []
    for check in CHECKS:
        name = check["name"]
        cmd = check["cmd"]
        code, output = run_check(cmd, env)
        output = redact(output)
        if code != 0:
            failures += 1
        results.append((name, code, output, cmd))

    for name, code, _output, _cmd in results:
        status = "PASS" if code == 0 else "FAIL"
        sections.append(f"- **{status}** — {name}")

    sections.extend(["", "## Details", ""])
    for name, code, output, cmd in results:
        status = "PASS" if code == 0 else "FAIL"
        sections.extend([
            f"### {status}: {name}",
            "",
            "Command:",
            "",
            "```bash",
            " ".join(shlex.quote(part) for part in cmd),
            "```",
            "",
            "Output:",
            "",
            "```text",
            output[-12000:] if output else "<no output>",
            "```",
            "",
        ])

    REPORT_PATH.write_text("\n".join(sections), encoding="utf-8")
    print(f"Wrote CI report to {REPORT_PATH.relative_to(ROOT)}")
    if failures:
        print(f"Agent KB CI failed: {failures} check(s) failed")
        return 1
    print("Agent KB CI passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
