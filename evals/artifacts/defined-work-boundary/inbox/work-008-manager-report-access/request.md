# Allow managers to view reports

## What and why
The user wants managers to view reports too. This request relates to work-007 report permissions and conflicts with its defined administrator-only policy, which explicitly denies managers access. The business reason for expanding access is unspecified.

## Expected outcome
Managers can view reports in addition to administrators.

## Constraints
Keep this request ready for later discussion. Work-007 already has an intent and plan; capture this proposed change separately and leave those definitions unchanged.

## Acceptance criteria
- Managers can view reports.

## Open questions
- Should this request revise work-007's policy or become later related work?
- Which reports should managers be allowed to view, and are any access boundaries needed?
- Has work-007 been implemented? The supplied context, intent, and plan do not establish deployment status.

## Sources
- User conversation: requests “let managers view reports too,” identifies work-007 as related, and asks to retain the request for later discussion.
- [Work-007 intent](../work-007-report-permissions/intent.md): defines administrator-only viewing and requires managers to be denied access.
- [Work-007 plan](../work-007-report-permissions/plan.md): directs implementation and verification of that policy.
- [Product context](../../context/product.md): identifies the product as an internal reporting system with filterable reports.
- [Engineering context](../../context/engineering.md): confirms that the existing reporting endpoint supports active row filters; it does not describe implemented report permissions.
