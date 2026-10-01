# CSV report download fails despite documented support

## What and why
Support reports that CSV report download fails and sees only PDF, although the product guide says CSV is supported. Account managers use reports. Capture the discrepancy so the intended report download behavior can be clarified and the support problem addressed.

## Expected outcome
Account managers and support can rely on an agreed, accurately documented set of report download formats. Restoring CSV download is a proposed interpretation of the request; the conflict between product context and implementation still requires a product decision.

## Constraints
This intake is limited to recording the request and unresolved questions. No implementation or downstream definition is requested. Other constraints are unknown.

## Acceptance criteria
Confirmed acceptance criteria: Unknown.

Proposed: After the intended formats are agreed, report download behavior and product guidance match that decision, and support can verify the reported problem is resolved. If CSV is intended to remain supported, an account manager can download a CSV report successfully.

## Open questions
- Should CSV be supported as the product guide states, or does the PDF-only implementation reflect an intended product change? The available sources conflict; neither establishes which behavior is authoritative.
- What report, interface, and deployed version did support use, and does “only PDF” describe available choices or successful downloads? No reproduction steps or production error evidence were supplied. The inspected function rejects CSV, but the exact support flow is unverified.
- If CSV is required, what report contents and CSV output requirements should later acceptance criteria cover? No CSV schema or sample is available in the supplied project.

## Sources
- User conversation: “the CSV report download fails. The product guide says CSV is supported, but support sees only PDF.” Requested investigation and intake capture only.
- [Product context](../../context/product.md): states reports support PDF and CSV downloads and identifies account managers as report users.
- [Engineering context](../../context/engineering.md): identifies the report implementation and says its format allowlist determines accepted formats.
- [Report implementation](../../../src/reports.py): the allowlist contains only PDF; download rejects formats outside it with an unsupported-format error. This directly conflicts with documented CSV support. This finding comes from code inspection, not a reproduction of support’s deployed environment.
