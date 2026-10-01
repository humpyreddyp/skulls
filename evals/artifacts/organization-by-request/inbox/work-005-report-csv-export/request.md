# Report CSV export

## What and why
Support needs downloadable report data, and Operations requests the same CSV export. This canonical request combines their requirements while preserving the unresolved disagreement about export size.

Grouped with [Audit exports](../work-003-audit-exports/request.md): together these requests support downloading report data and recording who exported it. They remain distinct requests for joint definition; this grouping does not commit either request to implementation or a schedule.

## Expected outcome
Support and Operations can download filtered report data in CSV format.

## Constraints
The source requirements conflict: Support specifies a maximum of 1,000 rows per export; Operations requires support for at least 10,000 rows per export. Neither limit has been selected or reconciled.

The existing reporting endpoint supports active row filters. Export implementation has not been selected.

## Acceptance criteria
- Export respects active report filters.
- Export dates use Coordinated Universal Time (UTC).

## Open questions
- What export-size requirement should apply, given the conflicting 1,000-row maximum and minimum capacity of 10,000 rows? This decision determines how much report data users can download in one export.
- Which columns should the CSV contain? This determines the report data available in the download.
- Who may export reports? This determines export access.

## Sources
- [Original CSV export request](../work-001-csv-export/request.md), citing support-ticket-17: Preserves Support's need, the 1,000-row maximum, active-filter requirement, and unresolved column selection. The underlying ticket is not available in this project and was not read.
- [Original report download request](../work-002-report-download/request.md), citing ops-meeting-22: Preserves Operations' need for the same CSV export, capacity of at least 10,000 rows, UTC dates, and unresolved export permissions. The underlying meeting record is not available in this project and was not read.
- [Product context](../../context/product.md): Identifies CSV export as a requested addition to the filterable reporting product.
- [Engineering context](../../context/engineering.md): Establishes endpoint support for active row filters and that export implementation remains undecided.
- User follow-up: Requests merging work-001 and work-002, preserving conflicts, grouping the merged request with work-003, and keeping the login request separate.
