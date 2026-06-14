# Module 07 — App Engine Push Task Queues Research

## Status

Planning only.

This document prepares the official Module 07 App Engine Push Task Queues work. It does not implement code, deploy services, enable APIs, or create queues.

## Purpose

Module 07 introduces an App Engine bundled Task Queue push task baseline. This is the predecessor that Module 08 will later migrate to Cloud Tasks.

This module should branch from the App Engine + Cloud NDB line:

`gae-flask-module-1/mod2-cloud-ndb/`

It should not branch from Cloud Run modules because bundled App Engine `taskqueue` APIs do not belong to Cloud Run.

## Source Module

Recommended source:

`gae-flask-module-1/mod2-cloud-ndb/`

Reason:

- App Engine Standard app
- Cloud NDB data layer
- Existing guestbook model
- Uses repo-actual `Greeting` entities under `Book`

## Entity Model Decision

Use the repo-actual model:

- `Book`
- `Greeting`

Do not use the canonical codelab `Visit` model in this repo.

Known discrepancy:

Some existing Module 08 research notes may reference `Visit`. That should be reconciled later in a separate docs cleanup so Module 07 and Module 08 consistently describe `Greeting` / `Book`.

## Verified Bundled Services Planning Facts

The future implementation should use the current bundled-services setup:

- `app_engine_bundled_services:`
  - `taskqueue`
- `threadsafe: true`
- `appengine-python-standard>=1.0.0`
- `wrap_wsgi_app`
- `taskqueue`

Legacy note:

Older codelab material may mention `app_engine_apis: true`. The planning baseline should prefer the current `app_engine_bundled_services` style.

## Expected Architecture

Expected future flow:

1. User submits guestbook entry.
2. App writes a `Greeting` under a `Book`.
3. App enqueues a push task.
4. App Engine dispatches the task to `POST /trim`.
5. `/trim` deletes old `Greeting` entities beyond the retention policy.

## Push Task Scope

In scope:

- App Engine bundled push tasks
- One queue
- One `/trim` handler
- Synthetic guestbook data only
- Cloud Logging evidence for server-side dispatch

Out of scope:

- Pull queues
- Pub/Sub
- Cloud Scheduler
- Cloud Tasks implementation
- Cloud Run implementation
- Real data
- Health data
- Secrets

## Handler Security Planning

Future `/trim` handler should validate task headers before doing work:

- `X-AppEngine-QueueName`
- `X-AppEngine-TaskName`
- `X-AppEngine-TaskRetryCount`

Requests without expected task headers should be rejected.

## Risks

Resolved:

- Runtime compatibility is not considered a blocker for the planning phase.
- Module 07 should use the App Engine line rather than Cloud Run.

Open:

- Exact retention count for trimming old `Greeting` entities
- Final App Engine deploy decision
- Module 08 `Visit` vs `Greeting` documentation reconciliation
- Sanitized Cloud Logging evidence format

## Safety Boundary

This planning package uses only public-safe demo guestbook context.

It does not include:

- PHI
- real health data
- e-Nabız exports
- TCKN
- medical PDFs
- OCR output
- secrets
- API keys
- `.env` files
