# Module 08-G - Gated Deploy-Readiness Review Plan

## Purpose

This document defines the gated deploy-readiness review plan for Module 08 Cloud Tasks migration work.

The goal is to prepare the project for a future controlled deployment review without performing any deployment, API enablement, queue creation, IAM change, billing-impacting configuration, or public endpoint exposure in this step.

## Scope

This is a documentation-only review plan.

This step does not change:

```text
application code
tests
deployment configuration
Cloud Tasks API state
Cloud Tasks queues
IAM policies
billing-impacting settings
public endpoints
secrets
.env files
```

## Current Baseline

The Module 08 chain is currently documented through:

```text
08-A reconciliation
08-B implementation design
08-C implementation planning
08-D Cloud Tasks code baseline
08-E readiness / evidence checklist
08-F local DevTools evidence note
```

The current baseline HEAD before this task is expected to be:

```text
b3b705c docs(module08): add local DevTools evidence note (#20)
```

## Gated Deployment Principle

Deployment is not a default next step.

A future deploy phase must be explicitly approved and must pass readiness gates before any cloud-side action is attempted.

The following actions remain gated:

```text
deploy
gcloud services enable
Cloud Tasks API enablement
Cloud Tasks queue creation
IAM changes
billing-impacting configuration
public endpoint exposure
live URL sharing
secret creation
.env creation
```

## Required Approval Gates

Before any future deploy attempt, the following approvals must be explicitly confirmed:

| Gate | Required Confirmation |
| --- | --- |
| Deploy approval | Explicit approval to deploy the Module 08 app |
| API enablement approval | Explicit approval before enabling Cloud Tasks API |
| Queue creation approval | Explicit approval before creating or modifying any queue |
| IAM approval | Explicit approval before changing service account permissions |
| Billing-impacting approval | Explicit approval before changing settings that may affect cost |
| Public endpoint approval | Explicit approval before exposing or sharing any live URL |
| Logging review approval | Explicit approval to inspect Cloud Logging evidence |
| Rollback approval | Explicit rollback decision criteria agreed before deployment |

## Pre-Deploy Technical Checks

Before a future gated deploy, the following local checks should be completed:

```text
git status -sb
git branch --show-current
git log --oneline -5
python -m pytest -q
python main_test.py
```

Expected local result:

```text
clean working tree
branch main or approved deploy branch
expected HEAD confirmed
local tests passing
no blocked files staged
no secrets or PHI present
```

## Pre-Deploy Repository Safety Checks

Before deployment, confirm that no blocked paths or sensitive files are tracked or staged.

Blocked paths:

```text
.env
.venv
__pycache__
.pytest_cache
.git
package-lock.json
python-docs-samples
```

Sensitive content that must not appear:

```text
API keys
tokens
private keys
passwords
TCKN
PHI
real patient data
e-Nabiz export data
medical PDFs
OCR output from real health data
```

## Cloud Tasks Readiness Checks

Before a future Cloud Tasks deploy, confirm the following design expectations:

```text
Cloud Tasks API status is known before any enablement attempt
queue name is documented
queue region is documented
service account behavior is understood
task payload is minimal and non-sensitive
handler endpoint is documented
retry behavior is understood
dispatch evidence plan exists
failure evidence plan exists
rollback plan exists
```

Important boundary:

```text
Cloud Tasks server-side dispatch is not visible in Chrome DevTools Network.
```

Browser DevTools can verify user-originated requests such as:

```text
GET /
POST /sign
POST /trim when manually triggered
```

Server-side dispatch requires Cloud Logging or Cloud Console evidence after a gated deploy phase.

## Chrome DevTools Evidence Plan

A future gated deployment should collect DevTools evidence from the browser for:

```text
Network
Console
Application
Security
```

### Network Panel

Verify:

```text
GET / status
POST /sign status
request payload shape
response behavior
headers
timing
initiator
unexpected external requests
```

Do not claim that Cloud Tasks dispatch appears in browser Network.

### Console Panel

Verify:

```text
no critical browser-side errors
no sensitive values printed
no task payload leakage
no unexpected client-side warnings
```

### Application Panel

Verify:

```text
Local Storage
Session Storage
Cookies
IndexedDB
Cache Storage
Service Workers
```

Expected:

```text
no PHI
no secrets
no task payloads
no queue identifiers stored unnecessarily
no unexpected persistent browser storage
```

### Security Panel

Verify:

```text
HTTPS status if live endpoint is used
certificate status
mixed content warnings
insecure request warnings
```

## Cloud Logging Evidence Plan

A future gated deployment should collect Cloud Logging evidence for server-side behavior.

Required evidence categories:

```text
task creation attempt
task creation success or failure
handler invocation
handler status code
retry behavior if applicable
trim behavior
error logs
permission errors
queue not found errors
```

Cloud Logging evidence must not include:

```text
secrets
tokens
PHI
real patient data
TCKN
raw sensitive payloads
```

## Failure Modes To Review

Before future deployment, explicitly review these failure modes:

| Failure Mode | Expected Handling |
| --- | --- |
| Cloud Tasks API disabled | Stop and request explicit approval before enablement |
| Queue missing | Stop and request explicit approval before queue creation |
| IAM permission denied | Stop and review least-privilege IAM plan |
| Handler returns non-2xx | Inspect logs, do not retry blindly |
| Unexpected public exposure | Stop and review endpoint policy |
| Sensitive data in logs | Stop and treat as safety incident |
| Browser stores unexpected data | Stop and fix before proceeding |
| Tests fail | Stop and do not deploy |

## Rollback Readiness

A future deploy phase must define rollback before deployment.

Rollback plan should include:

```text
known previous commit
known previous deployed version if applicable
how to stop traffic
how to disable or pause queue dispatch if applicable
how to inspect failed tasks
how to confirm recovery
who approves rollback
```

## Cost Boundary

This review does not create cost.

Future deploy-related actions may create cost or quota usage through:

```text
Cloud Build
App Engine or Cloud Run runtime
Cloud Tasks
Cloud Logging
Artifact storage
network usage
```

Any billing-impacting action requires explicit approval.

## Go / No-Go Checklist

A future gated deploy may proceed only if all of the following are true:

```text
explicit deploy approval exists
working tree is clean
expected branch and HEAD are confirmed
tests pass
blocked paths are absent
secret / PHI scan is clean
Cloud Tasks API decision is approved
queue decision is approved
IAM decision is approved
DevTools evidence plan is ready
Cloud Logging evidence plan is ready
rollback plan is ready
cost boundary is acknowledged
```

If any item is not true:

```text
No deploy.
No API enablement.
No queue creation.
No IAM change.
No public endpoint exposure.
```

## Evidence Summary

| Evidence Area | Status In This Step | Future Gated Phase |
| --- | ---: | --- |
| Local tests | Planned only | Run before deploy |
| DevTools Network | Planned only | Collect browser request evidence |
| DevTools Console | Planned only | Confirm no client-side errors or leaks |
| DevTools Application | Planned only | Confirm no unexpected storage |
| DevTools Security | Planned only | Confirm HTTPS / mixed content status |
| Cloud Logging | Planned only | Collect server-side dispatch evidence |
| Cloud Tasks API | Not changed | Requires explicit approval |
| Queue creation | Not changed | Requires explicit approval |
| IAM | Not changed | Requires explicit approval |
| Deploy | Not performed | Requires explicit approval |

## Portfolio Note

This module documents a professional release-readiness pattern for asynchronous cloud migration work:

```text
Local DevTools evidence validates browser-originated behavior, while Cloud Logging evidence is required for backend-to-backend Cloud Tasks dispatch. Deployment must remain gated until API, queue, IAM, cost, logging, and rollback controls are explicitly approved.
```

## Next Safe Step

Open a docs-only PR for this review plan.

Suggested branch:

```text
docs/module-08g-gated-deploy-readiness-review
```

Suggested commit:

```text
docs(module08): add gated deploy-readiness review plan
```

Suggested PR title:

```text
docs(module08): add gated deploy-readiness review plan
```
