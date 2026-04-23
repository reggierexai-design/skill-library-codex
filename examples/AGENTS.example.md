# AGENTS.md

## Repo rules
- Read nearby tests and docs before editing.
- Prefer minimal diffs and targeted verification.
- Keep risky workflows explicit and reviewable.

## Skill usage
- Use installed skills from `.agents/skills` when the request matches a named workflow.
- Prefer explicit `$skill-name` invocation for high-impact or side-effecting workflows.
- Keep reusable methods in skills and persistent repo facts here.
