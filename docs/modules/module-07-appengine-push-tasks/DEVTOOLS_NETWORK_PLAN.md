# Module 07 — Chrome DevTools and Cloud Logging Evidence Plan

## Core Principle

Push task dispatch is server-to-server.

That means the queue-to-`/trim` request is not fully visible from the browser Network panel. Evidence must be split:

- Browser-visible behavior: Chrome DevTools
- Server-side enqueue and dispatch: Cloud Logging

## Browser-Visible DevTools Evidence

Use Chrome DevTools against the future Module 07 app.

### Network Panel

Verify:

- `GET /` returns `200`
- `POST /sign` returns `302`
- redirect goes to `/?guestbook_name=...`
- direct manual `POST /trim` test returns expected status
- no unexpected external browser requests

### Console Panel

Verify:

- no critical JavaScript errors
- no raw sensitive values
- no noisy debug output that could become portfolio evidence

### Application Panel

Verify:

- Local Storage has no unexpected data
- Session Storage has no unexpected data
- Cookies have no sensitive data
- Cache Storage has no sensitive content
- IndexedDB has no unexpected data

### Security Panel

Verify:

- HTTPS enabled on deployed App Engine URL
- secure connection
- no mixed content warnings

## Server-Side Evidence

Use Cloud Logging for:

- task enqueue evidence
- task dispatch to `/trim`
- task retry count
- handler status code
- sanitized request metadata

Expected task headers to observe in server-side context:

- `X-AppEngine-QueueName`
- `X-AppEngine-TaskName`
- `X-AppEngine-TaskRetryCount`

## Evidence Mapping

| Claim | Evidence Tool |
|---|---|
| Page loads | DevTools Network |
| Form submit redirects | DevTools Network |
| Browser stays clean | Console / Application / Security |
| Task enqueued | Cloud Logging |
| Queue dispatched to `/trim` | Cloud Logging |
| Retry behavior controlled | Cloud Logging + `queue.yaml` |

## Sanitization Rules

Do not publish:

- secrets
- raw tokens
- private project metadata beyond approved public demo context
- health data
- personal data
- real user payloads

Allowed:

- synthetic guestbook text
- sanitized status codes
- sanitized request path
- redacted logs
