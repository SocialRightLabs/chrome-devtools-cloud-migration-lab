# Module 06 Cost Boundary

## Purpose

Define planning-time cost boundaries before any live Cloud Run action.

## Planning Decisions

- Minimum instances: `0`
- Maximum instances: must be explicitly defined before deploy
- CPU allocation: request-based preference should be evaluated before deploy
- Concurrency: default must not be assumed; review separately
- Region: must be selected with cost and latency review before deploy
- Budget alert: must not be created or changed without explicit human approval
- Public ingress: must not be assumed by default

## Cost Rules

- Do not publish live pricing values in public documentation.
- Verify cloud prices separately before any deployment decision.
- Treat any always-on setting as a cost risk until reviewed.

## Stop Conditions

- No explicit instance cap
- No region review
- No budget approval
- No public ingress approval

