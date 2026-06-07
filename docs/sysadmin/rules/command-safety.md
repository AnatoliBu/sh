---
title: Command Safety Rules
---

# Command Safety Rules

## Default behavior

Before suggesting a command, identify:

- target system or service;
- distribution and version, when relevant;
- package or daemon version, when relevant;
- whether the operation is diagnostic, mitigative, or destructive;
- expected output or success condition;
- rollback path for state-changing commands.

## Safe read-only commands

```shell
systemctl status nginx
journalctl -u nginx --since "1 hour ago"
ss -tulpn
ip addr
ip route
```

These can usually be suggested directly, but still explain what the user should look for.

## Low-risk state-changing commands

```shell
systemctl reload nginx
systemctl restart my-service
```

Before suggesting them, include:

- why the command is needed;
- how to validate the result;
- what to do if it fails.

## Dangerous commands

```shell
rm -rf /path
chmod -R 777 /path
iptables -F
ufw reset
systemctl disable ssh
```

Do not suggest these as first-line fixes. Provide safer alternatives, backups, dry-runs, and rollback guidance.

## Troubleshooting shape

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
