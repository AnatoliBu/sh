# OWASP Session Management Cheat Sheet

Official source: https://cheatsheetseries.owasp.org/cheatsheets/Session_Management_Cheat_Sheet.html

Use this authority for session identifiers, cookies, lifecycle, timeout, transport protection,
storage, fixation, and authenticated-session security.

## Agent rules

- Treat authenticated browser state as a bearer credential.
- Restrict access, lifetime, logging, and persistence of session state.
- Prefer ephemeral state when reuse is unnecessary.
- Revoke/destroy temporary sessions promptly at terminal workflow states.
