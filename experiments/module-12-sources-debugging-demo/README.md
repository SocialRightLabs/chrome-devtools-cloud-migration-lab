# Module 12 Sources Debugging Demo

## Purpose

This folder contains a safe local JavaScript debugging demo for Chrome DevTools Sources practice.

## Safety

This demo is intentionally synthetic and local-only.

- No deploy
- No cloud resource
- No API request
- No real user data
- No PHI
- No e-Nabiz data
- No TCKN
- No secrets

## How To Run Locally

Option 1:

```powershell
Start-Process .\experiments\module-12-sources-debugging-demo\index.html
```

Option 2:

```powershell
python -m http.server 8089 --directory experiments\module-12-sources-debugging-demo
```

Then open:

```text
http://localhost:8089
```

## Sample Inputs

- Price: `100`
- Quantity: `2`
- Discount: `10`

## Expected Debugging Behavior

The demo intentionally contains a logic bug in the discount calculation:

```javascript
return subtotal * (discountPercent / 10);
```

The correct implementation will be fixed later in the module:

```javascript
return subtotal * (discountPercent / 100);
```

## Buggy Output

With the sample inputs above, the buggy result should be:

- Subtotal: `200`
- Discount: `200`
- Final total: `0`

## Correct Output

After the bug is fixed, the correct result should be:

- Subtotal: `200`
- Discount: `20`
- Final total: `180`

## What To Inspect

- Sources panel breakpoints
- Call stack
- Local variables and scope
- Watch expressions
- Console output
- The calculation function in `app.js`

## No Cloud Boundary

This demo does not use cloud resources, APIs, authentication, deploy infrastructure, public endpoints, or secrets.

