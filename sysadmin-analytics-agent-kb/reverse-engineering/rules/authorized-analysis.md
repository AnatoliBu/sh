---
artifact_type: rule
status: foundation
domain: reverse-engineering
---

# Rule: Authorized Reverse Engineering

## Reference links

- [leanrea upstream scope and caveats](../../references/leanrea-repo.md)

## Safety and evidence

- Inspect only user-owned or explicitly authorized targets. For uncertain scope,
  limit investigation to static artifacts the user provides.
- Work on a copy, in a newly created directory. Do not delete old extraction trees,
  overwrite originals, or execute unknown binaries to discover what they do.
- Decompilers, `npx`, package managers, dynamic instrumentation and debugging hooks
  may execute downloaded code or affect a running process. Ask before installs,
  remote downloads, attachment or state-changing steps.
- Do not collect or print credentials, tokens, private keys, personal records
  or unrelated private data. Redact logs and traces.
- A byte string or static call site does not prove the feature executed. Cite
  `file:offset`, `path:line`, a symbol or an authorized runtime trace. Use
  **seen**, **inferred** and **unknown**, not unsupported certainty.
- Stop once requested questions have evidence. Escalate from inventories to
  decompilation only when needed.

## Detailed methods

- [CLI investigation playbook](../skills/cli-recon.md)
