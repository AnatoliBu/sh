# Source Review: cc-devops-skills

## Claimed purpose

DevOps-oriented skills for generating and validating infrastructure configuration.

## Authority level

Useful after audit.

## Strengths

- Good pattern: generator followed by validator.
- Emphasizes dry-run / lint / security checks.
- Useful taxonomy for IaC, Kubernetes, CI/CD review.

## Weaknesses / caveats

- Community project, not official documentation.
- Must audit dependencies, wrappers, and GitHub Actions before use.
- Do not trust generated configs without official validation tools.

## What can be reused

- Generate → validate → patch → revalidate loop.
- Skill split between creation and review.
- Validator-first thinking.

## What must not be reused blindly

- CI wrappers.
- Generated YAML/Terraform patterns.
- Security assumptions.
- Any direct production automation.

## Verdict

Useful scaffold. Convert into narrower, auditable skills backed by official docs and tool validations.
