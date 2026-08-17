---
artifact_type: reference
authority_tier: Tier A
status: foundation
source_type: specification
topics:
  - mcp
  - tools
  - resources
  - agent-safety
domains:
  - agent-tooling
owner: Model Context Protocol project
last_checked: 2026-08-17
source_url: https://modelcontextprotocol.io/specification/2025-06-18
---

# Reference: Model Context Protocol Specification

## Authority tier

Tier A

## Status

foundation

## Owner / maintainer

Model Context Protocol project (specification revision 2025-06-18, normative schema in
`schema/2025-06-18/schema.ts`).

## URL

https://modelcontextprotocol.io/specification/2025-06-18

## Last checked

2026-08-17

## Scope

Authoritative for the protocol itself: host/client/server roles over JSON-RPC 2.0, the three
server-side primitive families, the client-side ones, and the trust-and-safety requirements
that govern exposing anything to a model.

## Why trusted

The normative specification, with RFC 2119 keywords, backed by a machine-readable schema.

## Caveats

Revision-dated: capability sets move between revisions, so pin the revision when citing.
The specification defines the protocol, not whether a given surface is *usable* by a model —
that question is answered by measurement, not by conformance.

## Extracted rules

- Three server-offered families, and they are not interchangeable:
  **Resources** — context and data for the user or the model; **Prompts** — templated
  messages and workflows for users; **Tools** — functions the model executes.
  Mapping every readable endpoint to a Tool ignores this split.
- Clients may offer **Sampling**, **Roots**, and **Elicitation** back to servers.
- Capability negotiation is explicit; connections are stateful.
- Trust and safety, stated as requirements:
  - users must explicitly consent to and understand data access and operations, and retain
    control over what is shared;
  - hosts must obtain explicit user consent before invoking any tool;
  - tools are arbitrary code execution and must be treated with caution;
  - **descriptions of tool behavior, including annotations, must be considered untrusted
    unless they come from a trusted server**;
  - users must explicitly approve sampling requests, and the protocol deliberately limits
    server visibility into prompts.
- MCP cannot enforce these at the protocol level: implementors SHOULD build consent flows,
  access controls, and documentation of security implications.

## Do not use this source for

CLI surface design, exit-code taxonomies, or claims about how many tools a model can
handle before its accuracy degrades — none of that is in the specification.

## Related references

- [Command Line Interface Guidelines (clig.dev)](./cli-guidelines-clig.md)
- [Claude Code Plugin and Marketplace Format](./claude-code-plugin-format.md)

## Notes

The "annotations are untrusted" clause is the specification's own admission that a tool's
self-description is not evidence — which is the protocol-level counterpart to measuring a
tool surface on a weak agent instead of believing its docstring.
