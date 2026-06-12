# Contributing

This repository uses branch + PR workflow only.

## Branch workflow

1. Start from current `main`.
2. Create a focused branch.
3. Make one logical change set.
4. Run validation.
5. Open a PR.
6. Do not merge without review.

Example branch names:

- `docs/bootstrap-repo-system`
- `module/03-cloud-tasks`
- `docs/devtools-evidence-guide`
- `ci/repo-guardrails`

## Commit style

Use conventional commits:

- `docs: ...`
- `ci: ...`
- `chore: ...`
- `test: ...`
- `feat: ...`

## Pre-PR checklist

Before opening a PR:

- `git status -sb`
- `git diff --check`
- blocked path check
- required docs exist
- no `.env`
- no `.venv`
- no `__pycache__`
- no nested repositories
- no `python-docs-samples`
- no accidental `package-lock.json`
- no PHI
- no e-Nabız export
- no secrets
- no raw health data
- no private screenshots

## PR body should include

- purpose
- changed files
- safety boundary
- validation output
- manual review checklist
- explicit note if roadmap item is research candidate
