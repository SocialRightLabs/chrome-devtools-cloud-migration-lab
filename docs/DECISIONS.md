# Architecture Decisions

## ADR-001 — Private-first repository

This repository remains private-first until final public-readiness review. The lab may contain live endpoint references, cloud project details, or draft research notes that require review before publication.

## ADR-002 — Modules 00–02 are baseline

Modules 00, 01, and 02 are retained as the initial App Engine modernization baseline. They provide the migration story from legacy App Engine concepts toward Python 3 and Cloud NDB.

## ADR-003 — Health repositories are conceptual/documentation relationships only

Related health repositories are sensitive. This lab may document public-safe patterns, checklists, and guardrails, but must not connect directly to raw health data systems.

## ADR-004 — Branch + PR workflow is mandatory

All changes must use a branch and pull request. This supports review, diff inspection, safety checks, and durable project history.

## ADR-005 — Research stays under docs/research until validated

Gemini and other research outputs are stored under `docs/research/`. They are inputs, not canonical project decisions, until reviewed and promoted into `ROADMAP.md` or module docs.

## ADR-006 — Every module requires DevTools evidence

A module is not complete until it has DevTools verification notes or a reason why a specific panel is not applicable.

## ADR-007 — GitHub Actions guardrails are conservative

The guardrail workflow uses low permissions and avoids untrusted PR text in shell or agent prompts. It is designed to detect repository hygiene issues without exposing matched secret values.
