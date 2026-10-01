# Report export

## What and why
Support and Operations need to download report data as comma-separated values (CSV). This request combines work-001 and [work-002](../work-002-report-download/request.md), preserving each team's requirements below.

Grouped for later joint definition with [work-003: Audit exports](../work-003-audit-exports/request.md): users need to export reports, and Compliance needs to know who exported them. Work-003 retains its separate identity; grouping leaves eventual implementation scope open.

## Expected outcome
Support and Operations can download filtered report data as CSV.

## Constraints
- support-ticket-17 requires a maximum of 1,000 rows per export.
- ops-meeting-22 requires support for at least 10,000 rows per export.
These requirements conflict. Neither has been selected or superseded.

## Acceptance criteria
- When a user exports a filtered report, the export respects the active filters (support-ticket-17).
- Exported dates use Coordinated Universal Time (UTC) (ops-meeting-22).

## Open questions
- Which columns should users export? (support-ticket-17)
- Who can export? (ops-meeting-22)
- How should the maximum of 1,000 rows and minimum capacity of 10,000 rows be reconciled?

## Sources
- support-ticket-17, as recorded in the original work-001 request, supplies Support's need, row maximum, filter criterion, and column question above. The underlying ticket was not supplied.
- ops-meeting-22, as recorded in the [preserved work-002 request](../work-002-report-download/request.md), supplies Operations' need, minimum capacity, UTC criterion, and permissions question above. The underlying meeting record was not supplied.
- [Product context](../../context/product.md) establishes that the internal product has filterable reports and that CSV and Excel exports are requested additions. It does not supply Excel requirements for this merged CSV request.
- [Engineering context](../../context/engineering.md) confirms that the existing reporting endpoint supports active row filters and that export implementation has not been selected.
- User conversation authorizes merging work-001 and work-002, preserving source details, and grouping with work-003 for later definition while retaining its separate identity.
