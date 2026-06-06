#!/usr/bin/env python3
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
BASE_REQUIRED = {'artifact_type', 'status'}
REFERENCE_REQUIRED = {
    'artifact_type',
    'authority_tier',
    'status',
    'source_type',
    'topics',
    'domains',
    'owner',
    'last_checked',
    'source_url',
}
AGENT_REQUIRED = {'artifact_type', 'status', 'domain'}
STRICT_ROOTS = {'sysadmin', 'analytics', 'shared', 'references'}
EXCLUDED_PARTS = {'research', 'site', 'generated', 'public', 'tooling'}
TEMPORARY_EXCLUDED = {'sysadmin/skills/incident-triage.md'}
FRONTMATTER_RE = re.compile(r'^---\n(.*?)\n---\n', re.DOTALL)
KEY_RE = re.compile(r'^([A-Za-z0-9_-]+):\s*(.*)$')


def rel(path):
    return path.relative_to(ROOT).as_posix()


def is_strict_artifact(path):
    if path.suffix != '.md' or path.name in {'TEMPLATE.md'}:
        return False
    r = rel(path)
    if r in TEMPORARY_EXCLUDED:
        return False
    parts = path.relative_to(ROOT).parts
    if not parts or parts[0] not in STRICT_ROOTS:
        return False
    if set(parts) & EXCLUDED_PARTS:
        return False
    if parts[0] == 'references' and len(parts) != 2:
        return False
    return True


def parse_frontmatter(text):
    match = FRONTMATTER_RE.match(text)
    if not match:
        return None
    data = {}
    for line in match.group(1).splitlines():
        m = KEY_RE.match(line.strip())
        if m:
            data[m.group(1)] = m.group(2).strip().strip('"')
    return data


def required_for(path, data):
    if path.parent == ROOT / 'references' and path.name != 'README.md':
        return REFERENCE_REQUIRED
    artifact_type = data.get('artifact_type') if data else None
    if artifact_type in {'agent', 'skill', 'rule', 'workflow', 'eval'}:
        return AGENT_REQUIRED
    return BASE_REQUIRED


def main():
    errors = []
    for path in sorted(ROOT.rglob('*.md')):
        if not is_strict_artifact(path):
            continue
        text = path.read_text(encoding='utf-8')
        data = parse_frontmatter(text)
        if data is None:
            errors.append(f'{rel(path)}: missing YAML frontmatter')
            continue
        missing = sorted(required_for(path, data) - set(data.keys()))
        if missing:
            errors.append(f'{rel(path)}: missing frontmatter keys: {", ".join(missing)}')
        if data.get('artifact_type') not in {'reference', 'skill', 'agent', 'rule', 'workflow', 'eval', 'index'}:
            errors.append(f'{rel(path)}: invalid artifact_type: {data.get("artifact_type")}')

    if errors:
        print('Frontmatter validation failed:', file=sys.stderr)
        for error in errors:
            print('- ' + error, file=sys.stderr)
        return 1
    print('Frontmatter validation passed')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
