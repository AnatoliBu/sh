#!/usr/bin/env python3
from pathlib import Path
import html
import json
import re
import shutil

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / 'public'
BASE_PATH = '/sh/'
LINK_RE = re.compile(r'(?<!!)\[([^\]]+)\]\(([^)]+)\)')


def rel(path):
    return path.relative_to(ROOT).as_posix()


def site_href(path):
    return BASE_PATH + path.lstrip('/')


def page_path(md_path):
    r = rel(md_path)
    if r == 'README.md':
        return 'index.html'
    if r.endswith('/README.md'):
        return r[:-len('README.md')] + 'index.html'
    return r[:-3] + '.html'


def markdown_links_to_html(line, current_md):
    def repl(match):
        label = html.escape(match.group(1))
        target = match.group(2).strip()
        if target.startswith('http://') or target.startswith('https://') or target.startswith('mailto:'):
            return f'<a href="{html.escape(target)}">{label}</a>'
        anchor = ''
        if '#' in target:
            target, frag = target.split('#', 1)
            anchor = '#' + frag
        if target.endswith('.md'):
            dst = (current_md.parent / target).resolve()
            try:
                dst.relative_to(ROOT)
                href = site_href(page_path(dst)) + anchor
            except ValueError:
                href = target + anchor
        elif target == '' and anchor:
            href = anchor
        else:
            href = target + anchor
        return f'<a href="{html.escape(href)}">{label}</a>'
    return LINK_RE.sub(repl, line)


def md_to_html(text, current_md):
    lines = text.splitlines()
    out = []
    in_code = False
    list_open = False
    for raw in lines:
        line = raw.rstrip('\n')
        if line.startswith('```'):
            if not in_code:
                if list_open:
                    out.append('</ul>')
                    list_open = False
                out.append('<pre><code>')
                in_code = True
            else:
                out.append('</code></pre>')
                in_code = False
            continue
        if in_code:
            out.append(html.escape(line))
            continue
        if not line.strip():
            if list_open:
                out.append('</ul>')
                list_open = False
            continue
        m = re.match(r'^(#{1,6})\s+(.*)$', line)
        if m:
            if list_open:
                out.append('</ul>')
                list_open = False
            level = len(m.group(1))
            title = markdown_links_to_html(m.group(2), current_md)
            slug = re.sub(r'[^a-z0-9 -]', '', m.group(2).lower())
            slug = re.sub(r'\s+', '-', slug).strip('-')
            out.append(f'<h{level} id="{html.escape(slug)}">{title}</h{level}>')
            continue
        if line.startswith('- '):
            if not list_open:
                out.append('<ul>')
                list_open = True
            item = markdown_links_to_html(html.escape(line[2:]), current_md)
            out.append(f'<li>{item}</li>')
            continue
        if list_open:
            out.append('</ul>')
            list_open = False
        out.append('<p>' + markdown_links_to_html(html.escape(line), current_md) + '</p>')
    if list_open:
        out.append('</ul>')
    if in_code:
        out.append('</code></pre>')
    return '\n'.join(out)


def title_for(md_path, text):
    for line in text.splitlines():
        if line.startswith('# '):
            return line[2:].strip()
    return rel(md_path)


def build_nav(pages):
    rows = []
    for md_path, title, href in pages:
        rows.append(f'<li><a href="{site_href(html.escape(href))}">{html.escape(title)}</a> <small>{html.escape(rel(md_path))}</small></li>')
    return '<ul>' + '\n'.join(rows) + '</ul>'


def wrap(title, body, nav):
    home = site_href('index.html')
    graph_json = site_href('generated/link-graph.json')
    graph_dot = site_href('generated/link-graph.dot')
    return f'''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{html.escape(title)}</title>
<style>
body {{ font-family: system-ui, sans-serif; margin: 0; line-height: 1.55; color: #1f2328; }}
.layout {{ display: grid; grid-template-columns: 320px minmax(0, 1fr); min-height: 100vh; }}
nav {{ padding: 24px; background: #f6f8fa; border-right: 1px solid #d0d7de; overflow: auto; }}
main {{ padding: 32px; max-width: 980px; }}
a {{ color: #0969da; }}
pre {{ background: #f6f8fa; padding: 16px; overflow: auto; border-radius: 8px; }}
code {{ font-family: ui-monospace, SFMono-Regular, Menlo, monospace; }}
small {{ color: #6e7781; display: block; }}
@media (max-width: 900px) {{ .layout {{ display: block; }} nav {{ border-right: 0; border-bottom: 1px solid #d0d7de; }} }}
</style>
</head>
<body>
<div class="layout">
<nav><h2>Agent KB</h2><p><a href="{home}">Home</a> · <a href="{graph_json}">Graph JSON</a> · <a href="{graph_dot}">Graph DOT</a></p>{nav}</nav>
<main>{body}</main>
</div>
</body>
</html>
'''


def main():
    if OUT.exists():
        shutil.rmtree(OUT)
    OUT.mkdir(parents=True)

    pages = []
    for md_path in sorted(ROOT.rglob('*.md')):
        if any(part in {'public', 'generated'} for part in md_path.relative_to(ROOT).parts):
            continue
        text = md_path.read_text(encoding='utf-8')
        title = title_for(md_path, text)
        href = page_path(md_path)
        pages.append((md_path, title, href))

    nav = build_nav(pages)
    for md_path, title, href in pages:
        text = md_path.read_text(encoding='utf-8')
        body = md_to_html(text, md_path)
        out_path = OUT / href
        out_path.parent.mkdir(parents=True, exist_ok=True)
        out_path.write_text(wrap(title, body, nav), encoding='utf-8')

    generated = ROOT / 'generated'
    if generated.exists():
        shutil.copytree(generated, OUT / 'generated', dirs_exist_ok=True)
    (OUT / '.nojekyll').write_text('', encoding='utf-8')
    (OUT / 'site-manifest.json').write_text(json.dumps({'pages': [p[2] for p in pages]}, indent=2) + '\n', encoding='utf-8')
    print(f'Built {len(pages)} pages into {OUT}')


if __name__ == '__main__':
    main()
