# Module 07 — Safe Reuse Notes

## Reuse Classification

Public-safe to reuse:

- documentation structure
- DevTools evidence checklist
- Cloud Logging evidence split
- retry-risk checklist
- header-validation concept
- queue configuration checklist

Use with caution:

- bundled App Engine `taskqueue` code
- `wrap_wsgi_app`
- App Engine-specific queue handlers

Do not reuse directly in Cloud Run modules.

## Portability Notes

The bundled `taskqueue` API is App Engine-specific.

The portable migration path is Module 08:

- App Engine Push Task Queues
- Cloud Tasks migration
- explicit queue/location/client setup

## Safe Patterns

Safe to copy into other public demo repos:

- `/trim` handler validation checklist
- queue retry cap checklist
- DevTools + Cloud Logging evidence split
- public-safe README wording
- synthetic-only test payload rules

## Unsafe Patterns

Do not copy:

- real payloads
- credentials
- `.env` files
- project secrets
- health data
- e-Nabız exports
- patient data
- TCKN
- medical documents
- OCR output

## Related Modules

- Module 02: Cloud NDB baseline
- Module 07: App Engine Push Task Queues baseline
- Module 08: Cloud Tasks migration plan

## Known Follow-Up

Reconcile older Module 08 docs if they refer to `Visit` entities. The current repo model is `Greeting` under `Book`.
