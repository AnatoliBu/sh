---
artifact_type: reference
authority_tier: Tier A
status: foundation
domain: network
owner: NetBox Labs / NetBox open-source community
last_checked: 2026-06-06
source_url: https://netboxlabs.com/docs/netbox/
---

# Reference: NetBox

## Authority tier

Tier A

## Status

foundation

## Owner / maintainer

NetBox Labs / NetBox open-source community

## URL

https://netboxlabs.com/docs/netbox/

## Last checked

2026-06-06

## Scope

Authoritative reference for NetBox as a network source of truth: IPAM, DCIM, device inventory, topology metadata, circuits, VLANs, VRFs, racks, sites, and automation inputs.

## Why trusted

NetBox is a mature and widely used network source-of-truth platform. Its documentation defines the data model and APIs used to drive network automation and inventory workflows.

## Caveats

NetBox is only as accurate as the data maintained in it. The agent must distinguish intended state in NetBox from observed state collected from devices/cloud/Kubernetes.

## Skills that may consume this reference

- future: netbox-drift-analysis
- future: network-path-debug
- future: dns-debug
- future: inventory-review

## Agents that may consume this reference

- [Sysadmin / SRE / Network Assistant](../../agents/sysadmin-agent.md)

## Extracted rules

- The agent must not invent network topology.
- Intended state should come from NetBox or another approved source of truth.
- Observed state should be compared against intended state and reported as drift.
- Mutations to source-of-truth records require approval and audit trail.

## Do not use this source for

- Real-time device telemetry.
- Packet-level forwarding analysis.
- Cloud-provider-specific inventory unless integrated.
- Security policy validation by itself.

## Related references

- future: Nautobot
- future: Batfish
- future: Infrahub

## Notes

All future network automation skills should link to this or another approved SoT reference.
