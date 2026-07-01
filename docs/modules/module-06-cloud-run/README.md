# Module 06 — Cloud Run Planning Foundation

## Purpose

This directory contains the planning foundation for Module 06.

The goal is to separate Cloud Run planning from execution and evidence gathering so the repository stays deterministic, cost-aware, and reviewable.

## Scope

This planning set covers:

- deployment prerequisites
- billing and cost boundaries
- API and IAM review points
- approval gates
- rollback planning
- DevTools and Cloud Run evidence planning

## Out of Scope

This planning increment does not include:

- deploy commands
- API enablement
- IAM changes
- billing operations
- container builds
- ROADMAP updates
- cherry-picks from other branches

## Related Module 06 Docs

Existing Module 06 evidence and gate documents remain available in this folder:

- `MODULE_06A_CLOUD_RUN_READINESS_PLAN.md`
- `MODULE_06B_CLOUD_RUN_RUNBOOK_APPROVAL.md`
- `MODULE_06C_PRE_DEPLOY_APPROVAL_GATE.md`
- `MODULE_06D_FINAL_LOCAL_PREFLIGHT_REPORT.md`

## Safety Boundary

This module is docs-only.

It must remain public-safe and avoid secrets, private URLs, service account material, or any direct runtime coupling to sensitive repositories.

