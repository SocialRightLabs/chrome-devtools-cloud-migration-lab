# Module 06 Risk Register

| Risk | Impact | Mitigation |
|---|---|---|
| Billing exposure from always-on Cloud Run settings | Medium to high | Use explicit caps in the planning docs before any deploy step |
| IAM over-permission | High | Require least-privilege service account review |
| Secret leakage into build or runtime | High | Keep secrets out of repo and out of public docs |
| Public endpoint exposure | Medium | Require deployment approval gate and restricted access review |
| Evidence and deployment confusion | Medium | Separate deployment path from evidence plan |
| Roadmap drift | Low to medium | Keep Module 06 planning scoped and isolated from other modules |

## Notes

- This is a planning artifact only.
- No live cloud action is authorized by this document.

