#!/usr/bin/env python3
from pathlib import Path
import json
import re

ROOT = Path(__file__).resolve().parents[1]
LINK_RE = re.compile(r'(?<!!)\[([^\]]+)\]\(([^)]+)\)')
FENCE_RE = re.compile(r'```.*?```', re.DOTALL)


def clean(text):
    return FENCE_RE.sub('', text)


def rel(path):
    return path.relative_to(ROOT).as_posix()


def split_target(raw):
    raw = raw.strip().split('?', 1)[0]
    if raw.startswith('http') or raw.startswith('mailto:'):
        return None
    if raw.startswith('#'):
        return None
    if '#' in raw:
        raw = raw.split('#', 1)[0]
    if not raw:
        return None
    return raw


def local_target(src, raw):
    target = split_target(raw)
    if not target:
        return None
    dst = (src.parent / target).resolve()
    try:
        dst.relative_to(ROOT)
    except ValueError:
        return None
    if dst.is_dir():
        dst = dst / 'README.md'
    if not dst.exists() or dst.suffix != '.md':
        return None
    return dst


def main():
    edges = []
    nodes = set()
    for src in sorted(ROOT.rglob('*.md')):
        src_rel = rel(src)
        nodes.add(src_rel)
        text = clean(src.read_text(encoding='utf-8'))
        for label, raw in LINK_RE.findall(text):
            dst = local_target(src, raw)
            if not dst:
                continue
            dst_rel = rel(dst)
            nodes.add(dst_rel)
            edges.append({'source': src_rel, 'target': dst_rel, 'label': label.strip()})

    out_dir = ROOT / 'generated'
    out_dir.mkdir(exist_ok=True)

    graph = {'nodes': sorted(nodes), 'edges': edges}
    (out_dir / 'link-graph.json').write_text(json.dumps(graph, indent=2, ensure_ascii=False) + '\n', encoding='utf-8')

    lines = ['digraph docs {', '  rankdir=LR;', '  node [shape=box];']
    for node in sorted(nodes):
        lines.append(f'  {json.dumps(node)};')
    for edge in edges:
        lines.append(f'  {json.dumps(edge["source"])} -> {json.dumps(edge["target"])};')
    lines.append('}')
    (out_dir / 'link-graph.dot').write_text('\n'.join(lines) + '\n', encoding='utf-8')

    print(f'Generated {len(nodes)} nodes and {len(edges)} edges')


if __name__ == '__main__':
    main()
