# Module 05 — Cloud Run Buildpacks Migration

## Purpose

This module documents the migration of the Google App Engine Flask guestbook sample to Cloud Run using Cloud Buildpacks.

Unlike Module 04, this module does not use a Dockerfile. The application is deployed from source with a Procfile-based runtime command.

## Source Module

Source folder:

`gae-flask-module-1/mod3-cloud-datastore/`

Module 03 already contains the Cloud Datastore client migration. Module 05 reuses the same app logic and demonstrates a second Cloud Run migration path.

- Module 04: Dockerfile-based Cloud Run deployment
- Module 05: Buildpacks + Procfile-based Cloud Run deployment

## Key Changes

- Removed App Engine runtime files from the Module 05 working copy.
- Did not use a Dockerfile.
- Added `Procfile`.
- Added `gunicorn` to `requirements.txt`.
- Updated `main.py` for Cloud Run runtime compatibility:
  - `host="0.0.0.0"`
  - `port=int(os.environ.get("PORT", 8080))`
  - `debug=False`
  - `threaded=True`

## Procfile

`web: gunicorn -b :$PORT main:app`

## Local Verification

Local Gunicorn test:

`PORT=8080 gunicorn -b :8080 main:app`

Results:

- `GET /` -> `HTTP/1.1 200 OK`
- `POST /sign` -> `HTTP/1.1 302 FOUND`
- Redirect location -> `/?guestbook_name=mod5`

## Cloud Run Deployment

Deploy command:

`gcloud run deploy mod5-cloud-run-buildpacks --source . --region europe-west1 --allow-unauthenticated --min-instances 0 --max-instances 1 --project trustable-ai-100mph`

Cloud Run service:

`mod5-cloud-run-buildpacks`

Live service URL:

`https://mod5-cloud-run-buildpacks-oi5mbdh6lq-ew.a.run.app`

Deployment result:

- Revision: `mod5-cloud-run-buildpacks-00001-ff6`
- Traffic: `100 percent`

## Live Verification

Live HTTP verification:

- `GET /` -> `HTTP/2 200`
- `POST /sign` -> `HTTP/2 302`
- Redirect location -> `/?guestbook_name=mod5`

## Cost Controls

Configured with:

- `--min-instances 0`
- `--max-instances 1`

Observed Cloud Run settings:

- `maxScale: 1`
- `minScale: default scale-to-zero behavior`

## Chrome DevTools Verification Checklist

Use the live Cloud Run URL in Chrome.

Network:

- Verify `GET /` returns `200`.
- Verify `POST /sign` returns `302`.
- Verify redirect location is `/?guestbook_name=mod5`.
- Verify there are no unexpected external requests.

Console:

- Verify there are no critical JavaScript errors.
- Verify no sensitive values are printed.

Application:

- Check Local Storage, Session Storage, Cookies, Cache Storage, and IndexedDB.
- Verify there is no unexpected sensitive data.

Security:

- Verify HTTPS is enabled.
- Verify the connection is secure.
- Verify there are no mixed content warnings.

## Safety Boundary

This module uses only the synthetic/demo Google guestbook sample.

It does not include:

- PHI
- real health data
- e-Nabız exports
- medical PDFs
- OCR output
- secrets or API keys

## Portfolio Evidence

This module demonstrates:

- Cloud Run source-based deployment
- Cloud Buildpacks usage
- Procfile-based runtime configuration
- Flask app runtime modernization
- Gunicorn production server usage
- Low-cost serverless deployment settings
- Chrome DevTools live endpoint verification
- Public-safe documentation discipline

## CV Note

Completed a Google Cloud migration module by deploying a Flask and Cloud Datastore application to Cloud Run using Cloud Buildpacks and a Procfile-based Gunicorn runtime, validating live GET/POST behavior with Chrome DevTools and preserving public-safe repository guardrails.
