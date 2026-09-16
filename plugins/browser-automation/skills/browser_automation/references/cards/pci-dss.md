# PCI DSS

Official source: https://www.pcisecuritystandards.org/standards/pci-dss/

Use this authority for the baseline security requirements around systems that store, process,
transmit, or can impact the security of payment account data.

## Agent rules

- Minimize systems that can see or influence cardholder data.
- Never put PAN/CVV in logs, traces, screenshots, recordings, prompts, analytics, or general DB rows.
- Prefer hosted/tokenized payment surfaces and dedicated secret boundaries.
- Treat recordings capable of capturing payment secrets as sensitive infrastructure.
