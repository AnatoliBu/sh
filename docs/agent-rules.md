---
title: Agent Rules
---

# Agent Rules

These rules define how an assistant should work with this repository.

## Default behavior

Before suggesting a command, identify:

- target system or service;
- distribution and version, when relevant;
- package or daemon version, when relevant;
- whether the operation is diagnostic, mitigative, or destructive;
- expected output or success condition;
- rollback path for state-changing commands.

## Command safety levels

### Safe read-only commands

Examples:

```shell
systemctl status nginx
journalctl -u nginx --since "1 hour ago"
ss -tulpn
ip addr
ip route
```

These can usually be suggested directly, but still explain what the user should look for.

### Low-risk state-changing commands

Examples:

```shell
systemctl reload nginx
systemctl restart my-service
```

Before suggesting them, include:

- why the command is needed;
- how to validate the result;
- what to do if it fails.

### Dangerous commands

Examples:

```shell
rm -rf /path
chmod -R 777 /path
iptables -F
ufw reset
systemctl disable ssh
```

Do not suggest these as a first-line fix. Provide safer alternatives, backups, dry-runs, and rollback guidance.

## Troubleshooting shape

Use this sequence:

1. State the symptom clearly.
2. List the most likely layers involved.
3. Gather read-only evidence.
4. Narrow the cause.
5. Apply the smallest safe change.
6. Validate.
7. Record the permanent fix.

## Evidence discipline

Do not treat command output as proof unless it directly supports the claim.

Bad:

> NGINX is fine because `systemctl status nginx` is active.

Better:

> The daemon is running, but that does not prove routing, TLS, upstream, or application health. Check listener, logs, and HTTP response next.

## Source discipline

Use `docs/source-of-truth.md` before turning a claim into a rule.

When sources disagree:

- say which source is closer to the implementation;
- mention distro or version differences;
- avoid universal claims unless the source supports them.
