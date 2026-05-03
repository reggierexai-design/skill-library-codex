#!/usr/bin/env python3
"""
Convert upgraded OpenClaw v1.0 skills to Codex format.
Key differences:
- "OpenClaw tool pattern" → "Codex tool pattern"
- Tool references adapted for Codex (shell commands, file operations)
- Codex uses a more shell-centric approach
"""

import os, re

SRC_DIR = r"E:\rexhub-repos\skill-library-openclaw\skills"
DEST_DIR = r"E:\rexhub-repos\skill-library-codex\skills"

CODEX_TOOL_PATTERNS = {
    "att": [
        "- Use `shell` with `curl` to research competitor content and current platform conventions.",
        "- Read existing site copy, product pages, and proof assets before drafting so output fits the real product truth.",
        "- When external claims appear, verify before publishing with `safe_external_claims`.",
        "- After drafting, run `att_proof_mining` to verify every claim has backing.",
    ],
    "core": [
        "- Use file read operations to load relevant files and context before planning.",
        "- Use `shell` to check workspace state (git status, file structure) before and after actions.",
        "- After execution, use `core_verify_done` to confirm the result meets the stated objective.",
    ],
    "eng": [
        "- Use `shell` to run diagnostic commands, read logs, and check system state.",
        "- Use file read operations to inspect source files, configs, and error output directly.",
        "- Use file edit/write operations for targeted code changes. Prefer `eng_minimal_patch` scope discipline.",
        "- After changes, use `eng_test_strategy` to verify the fix works and nothing else broke.",
    ],
    "prod": [
        "- Use `shell` with `curl` to review competitor products and user feedback on review sites.",
        "- Use file read operations to load analytics data, user research files, and product specs.",
        "- After design work, run `core_review_changes` to check for scope creep.",
    ],
    "data": [
        "- Use `shell` to run data queries and analysis scripts (python, sql, etc.).",
        "- Use file read operations to load data exports, schema files, and query results.",
        "- After analysis, use `data_quality_checks` to validate findings before presenting.",
    ],
    "ops": [
        "- Use `shell` to check system status, run deployments, and verify infrastructure state.",
        "- Use file read operations to load runbooks, config files, and incident history.",
        "- After operational changes, use `ops_change_management` to document what changed and why.",
    ],
    "pm": [
        "- Use file read operations to load project plans, roadmaps, and stakeholder communications.",
        "- Use `shell` to check project status (git logs, CI results, milestone tracking).",
        "- After planning, use `pm_scope_tradeoffs` to pressure-test scope decisions.",
    ],
    "qa": [
        "- Use `shell` to run test suites, check CI results, and verify deployment state.",
        "- Use file read operations to load test plans, bug reports, and acceptance criteria.",
        "- After testing, use `qa_release_smoke_test` to confirm release readiness.",
    ],
    "sec": [
        "- Use `shell` to run security scanning tools, check dependency vulnerabilities, and audit configs.",
        "- Use file read operations to load security policies, auth configurations, and access control files.",
        "- After security review, use `sec_threat_model` to assess residual risk.",
    ],
    "sales": [
        "- Use `shell` with `curl` to research prospect companies, news, and relevant context before outreach.",
        "- Use file read operations to load CRM data, call notes, and deal history.",
        "- After sales planning, use `att_proof_mining` to ensure every claim in materials is backed.",
    ],
    "res": [
        "- Use `shell` with `curl` to gather competitor data, market reports, and source material.",
        "- Use file read operations to load interview transcripts, survey data, and research notes.",
        "- After research, use `core_evidence_research` to rate source quality and confidence.",
    ],
    "safe": [
        "- Use file read operations to load configs, credentials, and access control files for auditing.",
        "- Use `shell` to verify system state, check permissions, and test security controls.",
        "- After safety review, use `core_risk_gate` to assess whether the change can proceed.",
    ],
    "doc": [
        "- Use file read operations to load existing docs, code comments, and API definitions.",
        "- Use `shell` to check code structure and generate API schemas when needed.",
        "- After writing docs, use `doc_docs_feedback_loop` to plan for ongoing accuracy.",
    ],
    "des": [
        "- Use file read operations to load design specs, component libraries, and existing UI copy.",
        "- Use `shell` with `curl` to review competitor designs and accessibility standards.",
        "- After design work, use `des_accessibility_review` to verify compliance.",
    ],
    "solo": [
        "- Use `shell` to check current project status, deadlines, and shipping readiness.",
        "- Use file read operations to load personal productivity notes, goals, and rhythm files.",
        "- Pair with `solo_scope_guard` to prevent scope expansion during execution.",
    ],
    "vibe": [
        "- Use `shell` to run AI-assisted code generation, debugging, and deployment commands.",
        "- Use file read operations to load prompts, code templates, and AI tool configurations.",
        "- After building, use `vibe_debug_no_code` to test without deep technical knowledge.",
    ],
    "comm": [
        "- Use platform APIs via `shell` to check community channels, respond to members, and manage discussions.",
        "- Use file read operations to load community guidelines, feedback data, and engagement metrics.",
        "- After community actions, use `comm_retention_audit` to check member retention trends.",
    ],
    "legal": [
        "- Use `shell` with `curl` to look up regulation references and compliance requirements.",
        "- Use file read operations to load existing legal documents, terms, and privacy policies.",
        "- After legal review, flag anything that needs actual attorney review. This skill assists, not replaces counsel.",
    ],
    "finance": [
        "- Use file read operations to load financial data, pricing spreadsheets, and revenue reports.",
        "- Use `shell` to run calculations and financial models (python, etc.).",
        "- After financial analysis, use `finance_burn_rate` to cross-check sustainability.",
    ],
    "ai": [
        "- Use `shell` to run model evaluations, prompt tests, and benchmarking scripts.",
        "- Use file read operations to load prompt templates, eval datasets, and model configurations.",
        "- After AI system design, use `ai_eval_harness` to validate performance claims.",
    ],
}

DEFAULT_TOOL_PATTERN = [
    "- Use file read operations to load relevant context files before starting.",
    "- Use `shell` to verify current state before and after changes.",
    "- After completing, verify the result meets the stated objective.",
]

converted = 0

for skill_name in sorted(os.listdir(SRC_DIR)):
    src_path = os.path.join(SRC_DIR, skill_name, "SKILL.md")
    if not os.path.exists(src_path):
        continue
    
    with open(src_path, "r", encoding="utf-8") as f:
        content = f.read()
    
    # Replace section header
    content = content.replace("## OpenClaw tool pattern", "## Codex tool pattern")
    content = content.replace("## Claude Code tool pattern", "## Codex tool pattern")
    
    # Replace tool names in the tool pattern section
    cat = skill_name.split("_")[0] if "_" in skill_name else "other"
    
    # Replace inline tool references
    replacements = {
        "`exec`": "`shell`",
        "`read`": "file read operations",
        "`write`": "file write operations",
        "`edit`": "file edit operations",
        "`web_fetch`": "`shell` with `curl`",
        # Claude Code specific
        "`Bash`": "`shell`",
        "`Read`": "file read operations",
        "`Write`": "file write operations",
        "`Edit`": "file edit operations",
        "`WebFetch`": "`shell` with `curl`",
    }
    
    # Only replace in the tool pattern section
    pattern = r'(## Codex tool pattern\s*\n)((?:- .*\n)+)'
    match = re.search(pattern, content)
    if match:
        section = match.group(2)
        for old, new in replacements.items():
            section = section.replace(old, new)
        content = content[:match.start(2)] + section + content[match.end(2):]
    
    # Remove disable-model-invocation
    content = re.sub(r'\ndisable-model-invocation: [^\n]+', '', content)
    
    # Write
    dest_skill_dir = os.path.join(DEST_DIR, skill_name)
    os.makedirs(dest_skill_dir, exist_ok=True)
    dest_path = os.path.join(dest_skill_dir, "SKILL.md")
    
    with open(dest_path, "w", encoding="utf-8") as f:
        f.write(content)
    
    converted += 1

print(f"Converted: {converted} skills from OpenClaw v1.0 to Codex format")
