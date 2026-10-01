# Manager report access

Status: draft

## What and why
Let managers view reports too. This is a requested change related to the accepted [work-007 report-permissions intent](../work-007-report-permissions/intent.md), which requires administrator-only access and denies managers access. The reason for expanding access is unknown.

## Expected outcome
Managers can view reports alongside administrators.

## Constraints
Keep this request ready for later discussion. Work-007's accepted definition and existing plan remain unchanged; this draft does not authorize implementation. No code or tests are available in this project to establish the current implementation of report access.

## Acceptance criteria
Managers can view reports. Administrators retain report access.

## Open questions
Should managers view all reports available to administrators, or only a subset? This determines the scope of manager access. If this request is accepted later, work-007's manager-denial requirement and plan will need reconciliation with the new access rule.

## Sources
- User conversation: “let managers view reports too,” related to work-007, and keep the request ready for later discussion.
- [Work-007 intent](../work-007-report-permissions/intent.md) and [plan](../work-007-report-permissions/plan.md): accepted administrator-only access and planned manager denial; evidence of the conflicting existing definition, not evidence of deployed behavior.
- [Product context](../../context/product.md): internal reporting product with filterable reports.
- [Engineering context](../../context/engineering.md): existing reporting endpoint supports active row filters; it does not document report authorization behavior.
