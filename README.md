# RexBot Codex Skill Library v0.6

**RexBot / Rex Hub community release for Codex.**

This is the Codex-specific port of the RexBot generalist skill library. It keeps the same deep playbooks, profiles, and category coverage as the OpenClaw release, but the docs, install paths, examples, and packaging are rewritten for Codex.

## What is in this pack

- **185 skills**
- **22 curated profiles**
- **21 internal orchestration or safety skills**
- **76 skills intended for model-side discovery**
- **109 slash-first specialist skills**
- **619.4 average words per skill**

## Platform fit

- Codex reads skills from `.agents/skills` in repositories and from `~/.agents/skills` for user-wide skills.
- Codex can invoke skills explicitly with `$skill-name` or by selecting them from `/skills`, and it can invoke them implicitly from the skill description.
- Codex skills use `SKILL.md` plus optional `agents/openai.yaml`; in this port, `openai.yaml` is generated when invocation policy metadata is needed.
- Always-on repo guidance belongs in `AGENTS.md`; skills should hold reusable workflows and longer playbooks that load on demand.

## Quick start

1. Put this library somewhere stable on disk.
2. Install a profile with `python scripts/install_profile.py minimal_core`.
3. Start with a narrow profile before you install the whole catalog.
4. Keep repo-wide standing guidance in `AGENTS.md` or an equivalent workspace note, and use skills for repeatable workflows.

## Invocation

- Explicit use: `$skill-name or /skills`
- Discovery: Type `$` to mention a skill, run `/skills`, or ask Codex to use a named skill.

## Recommended rollout

- Start with `minimal_core`
- Add one domain profile such as `builder_engineering`, `docs_support`, `research_operator`, or `security_quality`
- Treat `full_library` as a power-user profile, not a default

## Important files

- `START_HERE.md`
- `TRAINING_MANUAL.md`
- `SYSTEM_OVERVIEW.md`
- `DEPLOYMENT_GUIDE.md`
- `AGENT_INTEGRATION_GUIDE.md`
- `PROFILE_SELECTION_GUIDE.md`
- `SKILL_ROUTING_GUIDE.md`
- `AUTHORING_GUIDE.md`
- `CATALOG.md`
- `CATALOG_DETAILED.md`

## Attribution

- Publisher: **RexBot / Rex Hub**
- Homepage: `https://reggierexai-design.github.io/rexhub/`
- Status: community-maintained, not an official Codex bundle
