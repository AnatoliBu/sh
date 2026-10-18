---
name: leanrea
description: >
  Use when reverse engineering or auditing authorized shipped software: Electron app.asar,
  minified JS and source maps, Mach-O/ELF/PE binaries, native addons, Go/Rust/.NET/Flutter,
  Android APK, WASM, SQLite, firmware, pcap/HAR, plist and websites. Используй, когда
  нужно разобраться, как устроена функция приложения, найти IPC, экспорты, сборочные
  зависимости, версии, сравнить бинарники и подтвердить выводы доказательствами.
---

# leanrea — reverse engineering with CLI tools

Choose the smallest, fastest read-only probe for an authorized artifact.
No MCP server is needed; use installed command-line tools.

## Choose the route

| Target | First probe |
|---|---|
| Unknown binary | `file`, magic bytes, `strings` |
| Electron and JavaScript | asar inventory, `package.json`, `rg -uu` |
| Mach-O / ELF / PE | `otool`, `nm`, `readelf`, imports and exports |
| Go / Rust / .NET / APK / Flutter / WASM | format-specific build metadata |
| SQLite / plist / pcap / firmware | schema, headers, capture or image inventory |
| Website / running app | authorized static assets or read-only tracing |

## Process

1. Verify permission to inspect this target and identify its file format.
2. Copy the artifact or create a unique extraction directory.
3. Batch inexpensive read-only metadata probes; limit output.
4. Slice relevant symbols, source-map modules or string neighborhoods.
5. Decompile or inspect runtime behavior only when necessary and authorized.
6. Distinguish **seen**, **inferred** and **unknown**. Cite line/offset, symbol
   or trace evidence, and state what was not verified.

## Read next

- [CLI recon recipes by format](references/cli-recon.md) — first moves,
  router, common pitfalls and speed patterns.
- [Authorized analysis rules](references/safety.md) — copies, downloads,
  credentials, runtime attachment and evidence levels.
- [Upstream provenance](references/cards/leanrea-repo.md) — original source,
  MIT terms and limitations of the reported benchmark.

Do not auto-install dependencies with `npx` or package managers. If a
tool is missing, use an installed fallback or ask before installing.
