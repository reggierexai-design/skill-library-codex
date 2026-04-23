# Compatibility

This pack targets **Codex**.

## Assumptions

- Skills are discovered from `.agents/skills` and `~/.agents/skills`
- `SKILL.md` uses `name` and `description` frontmatter
- Codex-specific appearance or invocation policy can live in `agents/openai.yaml`
- Project-wide standing guidance belongs in `AGENTS.md`

## Port notes

This port rewrites each skill to Codex-compatible frontmatter and generates `agents/openai.yaml` for display metadata and manual-only invocation policy where relevant.
