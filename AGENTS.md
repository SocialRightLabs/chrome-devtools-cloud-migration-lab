# AGENTS.md

Rules for Claude, Gemini, Codex, Copilot, and other AI agents working on this repository.

## Read first

Agents must read:

1. `docs/HEALTH_ECOSYSTEM_BOUNDARIES.md`
2. `docs/GUARDRAILS.md`
3. `MODULE_INDEX.md`
4. `ROADMAP.md`

## Hard rules

- Do not modify `main` directly.
- Use branch + PR workflow.
- Do not request PHI.
- Do not request e-Nabız exports.
- Do not request `.env` files.
- Do not request tokens, PATs, credentials, or secrets.
- Do not create direct runtime integration with sensitive health repositories.
- Do not copy private implementation details from sensitive repositories.
- Do not expose full live endpoints in public-facing docs.
- Do not auto-merge PRs.

## Cross-repo classification

Every cross-repository idea must be classified as exactly one of:

1. Allowed public-safe documentation/checklist pattern
2. Needs manual review
3. Forbidden sensitive-data coupling

## Before PR

Agents must provide:

- changed file list
- risk list
- validation commands and output
- safety boundary confirmation
- manual review checklist
