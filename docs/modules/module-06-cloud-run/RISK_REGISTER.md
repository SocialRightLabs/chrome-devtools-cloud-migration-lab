# Module 06 Risk Register

| Risk | Impact | Likelihood | Mitigation | Trigger | Stop condition | Evidence required | Status |
|---|---|---|---|---|---|---|---|
| Billing exposure from always-on Cloud Run settings | High | Medium | Use explicit caps in the planning docs before any deploy step | Deployment planning starts without caps | Cost cap is undefined | Planning docs with cap fields | Open |
| IAM over-permission | High | Medium | Require least-privilege service account review | IAM roles are proposed without review | Service account roles are not documented | IAM review note | Open |
| Secret leakage into build or runtime | High | Low | Keep secrets out of repo and out of public docs | Secret references appear in docs or commands | Secret or private URL is present | Secret scan note | Open |
| Public endpoint exposure | High | Medium | Require deployment approval gate and restricted access review | Public ingress is implied without approval | Public access is not separately approved | Approval matrix entry | Open |
| Evidence and deployment confusion | Medium | Medium | Separate deployment path from evidence plan | Evidence steps include live mutation commands | Deployment and evidence are mixed | Evidence plan doc | Open |
| Roadmap drift | Low | Medium | Keep Module 06 planning scoped and isolated from other modules | ROADMAP is modified in this branch | ROADMAP change is introduced here | Branch diff review | Open |

## Notes

- This is a planning artifact only.
- No live cloud action is authorized by this document.
- The register intentionally avoids exact cloud pricing because cost values change.

