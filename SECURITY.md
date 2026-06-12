# Security Policy

## Scope

This is a private-first, public-safe Chrome DevTools and Google Cloud migration lab.

It must not process health data, PHI, e-Nabız exports, patient records, medical PDFs, OCR clinical text, or clinical free text.

## Forbidden content

Do not commit:

- `.env`
- API keys
- tokens
- credentials
- private keys
- service account JSON
- real health data
- PHI
- e-Nabız exports
- patient-level records
- medical PDFs
- OCR clinical text
- private screenshots
- database dumps

## Reporting

If you find a secret or sensitive file:

1. Do not paste it into chat.
2. Do not print it in logs.
3. Stop work.
4. Rotate/revoke the credential if applicable.
5. Open a private security note or issue in the organization workflow.

## Public-readiness

This repo is not public-ready until a final review confirms:

- no secrets
- no PHI
- no live endpoint exposure
- no private screenshots
- no medical data
- no unsupported badge or recognition claims
