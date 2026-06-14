# Module 07 — Implementation Plan

## Status

Future code PR only.

This planning PR ships zero code and zero cloud changes.

## Future Code PR

Future branch:

`feat/module-07-gaetasks-baseline`

Future code folder:

`gae-flask-module-1/mod7-gaetasks-baseline/`

Source folder:

`gae-flask-module-1/mod2-cloud-ndb/`

## Future Scope

The future implementation should add an App Engine bundled push task baseline to the Cloud NDB guestbook app.

Planned behavior:

1. User submits a guestbook entry.
2. The app stores a `Greeting`.
3. The app enqueues a push task.
4. App Engine dispatches the task to `/trim`.
5. `/trim` deletes old `Greeting` entities idempotently.

## Expected Future File Changes

Future code PR may create or modify:

- `gae-flask-module-1/mod7-gaetasks-baseline/main.py`
- `gae-flask-module-1/mod7-gaetasks-baseline/app.yaml`
- `gae-flask-module-1/mod7-gaetasks-baseline/queue.yaml`
- `gae-flask-module-1/mod7-gaetasks-baseline/requirements.txt`
- `gae-flask-module-1/mod7-gaetasks-baseline/main_test.py`
- `gae-flask-module-1/mod7-gaetasks-baseline/README-module-07.md`
- `gae-flask-module-1/mod7-gaetasks-baseline/templates/index.html`
- `gae-flask-module-1/mod7-gaetasks-baseline/index.yaml`

## Expected Implementation Deltas

### requirements.txt

Add:

`appengine-python-standard>=1.0.0`

### main.py

Expected additions:

- import `wrap_wsgi_app`
- import `taskqueue`
- wrap Flask WSGI app
- enqueue push task on guestbook write
- add `POST /trim`
- validate App Engine task headers
- delete old `Greeting` entities idempotently

### app.yaml

Expected App Engine bundled-services settings:

`app_engine_bundled_services: [taskqueue]`

Also use:

`threadsafe: true`

Keep cost control:

`automatic_scaling: max_instances: 1`

### queue.yaml

Expected future purpose:

- define one push queue
- cap rate
- cap retry limit
- cap task age
- avoid retry amplification

### main_test.py

Expected tests:

- task enqueue path can be called with stubs
- `/trim` rejects missing task headers
- `/trim` accepts simulated task headers
- trimming is idempotent
- no live cloud calls in tests

## Local Verification Plan

Before any cloud deploy:

1. Run unit tests.
2. Run Flask locally if possible.
3. Manually call `/trim` with simulated task headers.
4. Confirm no unexpected Console output.
5. Confirm no secrets or sensitive values are logged.

## Deployment Decision Gates

Do not deploy until all gates pass:

- Planning PR merged
- Entity model confirmed as `Greeting` / `Book`
- Cost controls reviewed
- Queue retry controls reviewed
- Explicit human approval to deploy App Engine
- Project confirmed demo-only
- No runtime integration with sensitive health repos
- Guardrails green

## Rollback Plan

If future implementation causes issues:

- Revert implementation PR
- Purge or pause the queue
- Route traffic back to prior App Engine version if applicable
- Disable or stop the demo app after verification
