# Module 12-B - Safe Local JavaScript Debugging Demo

## Purpose

This document records the safe local JavaScript debugging demo created for Module 12 Sources panel practice.

## Scope

This step creates a small static demo with one deliberate logic bug for later debugging evidence collection.

## Demo Files

- `experiments/module-12-sources-debugging-demo/index.html`
- `experiments/module-12-sources-debugging-demo/app.js`
- `experiments/module-12-sources-debugging-demo/README.md`

## Local-Only Boundary

```text
No deploy.
No public endpoint.
No cloud resource.
No API enablement.
No IAM change.
No billing impact.
No real user data.
No PHI.
No e-Nabiz export.
No TCKN.
No secrets.
No .env.
No external API.
```

## Planned Inputs

```text
price = 100
quantity = 2
discount = 10
```

## Buggy Result

```text
Subtotal: 200
Discount: 200
Final total: 0
```

## Expected Correct Result

```text
Subtotal: 200
Discount: 20
Final total: 180
```

## Console Behavior

```text
The demo logs a structured calculation object to the console to support later Sources and Console inspection.
```

## Next Step

Next step: Module 12-C should use Chrome DevTools Sources panel to collect before/after debugging evidence and identify the root cause.
