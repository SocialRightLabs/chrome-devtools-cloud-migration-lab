# Module 06 Runtime Baseline

## Purpose

This document records the runtime baseline that Module 06 planning depends on.

## Baseline Fields

| Field | Value |
|---|---|
| Python/runtime version | Python 3.12 / Flask runtime used by the guestbook sample |
| Entry point | `main.py` |
| Dependency file | `requirements.txt` |
| Local start command | `PORT=8080 gunicorn -b :8080 main:app` |
| Expected port | `8080` |
| Health endpoint | `GET /` |
| Environment variables | `PORT` for local or container execution |
| Secret-free local configuration | No `.env`; local demo uses checked-in sample configuration only |
| Known tests | Flask route smoke tests and local request verification from Module 05 evidence |
| Source module commit | `6dea081` |

## Baseline Notes

- The runtime baseline is derived from the already completed Cloud Run buildpacks path.
- This document does not authorise deployment or build execution.
- Any later implementation must re-validate the runtime before live Cloud Run work.
