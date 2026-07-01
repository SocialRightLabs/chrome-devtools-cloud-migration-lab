# Module 06 Evidence Plan

## Objective

Capture the minimum evidence needed to prove Cloud Run readiness and post-deploy behavior without mixing it with deployment instructions.

## Evidence Categories

### Local Readiness

- app starts locally
- container or buildpack path is reproducible
- local config does not rely on secrets

### Deployment Readiness

- billing cap is defined
- API enablement is reviewed
- IAM service account is reviewed
- rollback path is documented

### DevTools Evidence

- Network: request and response status
- Console: no critical runtime errors
- Performance: cold start or load timing when applicable
- Application: storage and cookie review

### Cloud Evidence

- service status
- logs
- revision or rollout state

## Evidence Rules

- keep screenshots free of secrets and private URLs
- avoid exporting sensitive data
- store only public-safe notes in this repository

