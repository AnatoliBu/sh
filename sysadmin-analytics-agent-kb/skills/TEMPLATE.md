# Skill Template

Use this template for every skill. Keep skills narrow and procedural. A skill is not an expert brain; it is a workflow contract.

## Purpose

What exact task this skill handles.

## When to use

Trigger conditions and examples.

## Required context

List the facts, files, tools, credentials, environment data, and source-of-truth references required before execution.

## Authority chain

Rank sources the agent must consult, for example:

1. internal source of truth;
2. official vendor/project docs;
3. validated internal runbooks;
4. audited community references;
5. unaudited examples only.

## Allowed read-only actions

Commands/API calls that inspect state only.

## Allowed write actions

Only list write actions if the skill is explicitly intended to mutate state. Most skills should have none.

## Forbidden actions

Commands/actions the agent must never run in this skill without explicit escalation.

## Validation steps

Lint, dry-run, schema validation, policy checks, cross-checks, tests, or peer review gates.

## Risk classification

Define low/medium/high risk conditions.

## Human approval requirement

State when a human must approve and what evidence the agent must present.

## Output format

Define the exact structure of the skill result.

## Assumptions log

List all assumptions. The agent must mark unknowns clearly instead of guessing.

## Rollback / recovery

If this skill can lead to a change, describe rollback requirements before execution.
