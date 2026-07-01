# Module 06 Planning Checklist

## Planning Gate

- [ ] Source module is identified
- [ ] Runtime baseline is documented
- [ ] Deployment prerequisites are listed
- [ ] Cost boundaries are explicit
- [ ] IAM review points are listed
- [ ] API review points are listed
- [ ] Rollback path is documented
- [ ] Evidence plan is separated from deployment path
- [ ] No deploy, billing, or IAM changes are included
- [ ] No secrets or private URLs are exposed

## Decision Split

- Deployment path: build, container, deploy, rollback
- Evidence plan: Network, Console, Performance, Cloud logs

## Stop Conditions

- Missing cost boundary
- Missing approval gate
- Missing rollback path
- Any attempt to move from planning into live deployment without manual review

