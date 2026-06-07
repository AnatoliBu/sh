#!/usr/bin/env python3
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
LINK_RE = re.compile(r'(?<!!)\[[^\]]+\]\(([^)]+)\)')
FM_RE = re.compile(r'^---\n(.*?)\n---\n', re.DOTALL)
AGENT_ROOTS = {'sysadmin', 'analytics', 'java-qa', 'shared'}
SKIP_ROOTS = {'research', 'site', 'generated', 'public', 'agents', 'rules', 'skills'}
SKIP_PREFIXES = ('references/sysadmin/', 'references/analytics/', 'references/tooling/')


def rel(p: Path) -> str:
    return p.relative_to(ROOT).as_posix()


def fm(text: str) -> dict[str, str]:
    m = FM_RE.match(text)
    if not m:
        return {}
    data = {}
    for line in m.group(1).splitlines():
        if ':' in line:
            k, v = line.split(':', 1)
            data[k.strip()] = v.strip().strip('"')
    return data


def local_target(src: Path, raw: str) -> Path | None:
    raw = raw.strip().split('?', 1)[0].split('#', 1)[0]
    if not raw or raw.startswith('http') or raw.startswith('mailto:'):
        return None
    return (src.parent / raw).resolve()


def is_agent_artifact(path: Path, data: dict[str, str]) -> bool:
    parts = path.relative_to(ROOT).parts
    if not parts or parts[0] not in AGENT_ROOTS:
        return False
    return data.get('artifact_type') in {'agent', 'skill', 'rule', 'workflow', 'eval'}


def main() -> int:
    errors = []
    for p in sorted(ROOT.rglob('*.md')):
        r = rel(p)
        parts = p.relative_to(ROOT).parts
        if not parts or parts[0] in SKIP_ROOTS or r.startswith(SKIP_PREFIXES):
            continue
        text = p.read_text(encoding='utf-8')
        data = fm(text)
        if is_agent_artifact(p, data):
            links = LINK_RE.findall(text)
            flat_ref = False
            for link in links:
                if 'references/sysadmin/' in link or 'references/analytics/' in link:
                    errors.append(f'{r}: old reference link: {link}')
                dst = local_target(p, link)
                if dst and dst.parent == ROOT / 'references' and dst.suffix == '.md' and dst.exists():
                    flat_ref = True
            if not flat_ref and r != 'sysadmin/skills/incident-triage.md':
                errors.append(f'{r}: missing flat references/*.md link')
    if errors:
        print('Structure validation failed:', file=sys.stderr)
        for e in errors:
            print('- ' + e, file=sys.stderr)
        return 1
    print('Structure validation passed')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
