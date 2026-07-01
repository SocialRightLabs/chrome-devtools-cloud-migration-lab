# Module 06 Approval Matrix

| Operation | Allowed in Planning | Requires Live Approval |
|---|---:|---:|
| Source code review | Yes | No |
| Local test execution | Yes | No |
| Container build | No | Yes |
| API enablement | No | Yes |
| IAM changes | No | Yes |
| Cloud Run deploy | No | Yes |
| Public endpoint exposure | No | Separate approval |
| Billing or budget changes | No | Separate approval |
| Screenshot or evidence capture | Planned only | After deploy |

## Decision Rule

If an action changes live cloud state, it is outside planning and requires explicit human approval.

## Notes

- Planning docs may describe commands.
- Planning docs must not execute commands.
- The matrix is intentionally conservative to avoid accidental live changes.
