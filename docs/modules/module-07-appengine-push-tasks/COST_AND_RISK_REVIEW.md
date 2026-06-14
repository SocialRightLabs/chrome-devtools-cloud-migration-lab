# Module 07 — Cost and Risk Review

## Status

Planning only.

This PR has no cloud cost because it creates documentation only.

## Future Cost Posture

Future implementation should remain near-zero cost:

- App Engine Standard only for short verification windows
- `max_instances: 1`
- no min instances
- no scheduled recurring tasks
- one queue
- synthetic guestbook entries only
- app disabled or left idle after verification

## Cost-Control Checklist

Before any future deploy:

- confirm project: `trustable-ai-100mph`
- confirm region and service scope
- confirm `max_instances: 1`
- confirm no periodic task source
- confirm retry caps in `queue.yaml`
- confirm no load test
- confirm no real data
- confirm no health repo runtime coupling

## Risk Register

### Retry amplification

Risk:

A failing `/trim` handler could trigger repeated retries.

Mitigation:

- make `/trim` idempotent
- cap `task_retry_limit`
- cap `task_age_limit`
- monitor Cloud Logging during verification

### Open handler exposure

Risk:

`/trim` is a URL endpoint.

Mitigation:

- require App Engine task headers
- reject requests without task headers
- keep payload synthetic
- do not expose sensitive data

### Re-activating App Engine

Risk:

Module 04 and 05 moved toward Cloud Run, but Module 07 returns to App Engine to create the taskqueue baseline.

Mitigation:

- clearly document this as a codelab baseline needed for Module 08
- use short verification windows
- keep cost controls
- do not treat this as production architecture

### Bundled-services dependency

Risk:

Bundled services are App Engine-specific and not portable to Cloud Run.

Mitigation:

- keep code isolated to Module 07
- document Cloud Tasks migration path in Module 08
- do not reuse `taskqueue` code in Cloud Run modules

## Safety Guardrails

Never include:

- PHI
- real health data
- e-Nabız exports
- TCKN
- medical documents
- OCR output
- credentials
- `.env`
- API keys
- secrets

Allowed data:

- synthetic guestbook names
- synthetic greeting text
- timestamps
- public-safe screenshots with sensitive values redacted
