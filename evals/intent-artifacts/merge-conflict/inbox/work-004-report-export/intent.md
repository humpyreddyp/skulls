# Report export

Status: draft

## What and why
Support needs downloadable report data, and Operations needs the same CSV export. This request combines work-001 and work-002 while retaining their distinct requirements and source details.

## Expected outcome
Support and Operations can download filtered report data as CSV.

## Constraints
The source requirements conflict: work-001 specifies a maximum of 1,000 rows per export, while work-002 requires at least 10,000 rows per export. Neither limit has been selected. Export implementation has not been selected in the engineering context.

Grouped for later definition with [work-003 audit exports](../work-003-audit-exports/intent.md): downloadable reports and a record of who exported them support a shared report-export workflow. Work-003 retains its separate identity and requirements. This grouping does not authorize implementation or set a delivery schedule.

## Acceptance criteria
- Export report data as CSV and respect active filters (work-001, with filtered downloads also requested by work-002).
- Export dates use UTC (work-002).
- Row-count acceptance remains unresolved because the source constraints conflict.

## Open questions
- What row limit should apply: the 1,000-row maximum from Support, the ability to export at least 10,000 rows from Operations, or a clarified requirement? This determines export scope and resolves the incompatible source constraints.
- Which columns should be exported? Carried forward from work-001; this determines the downloaded data.
- Who can export? Carried forward from work-002; this determines permitted users.

## Sources
- User conversation: merge work-001 and work-002 into one report-export request, preserve source details, and group the result with work-003 for later definition while keeping work-003 separate.
- [Original work-001 CSV export](../work-001-csv-export/intent.md), source support-ticket-17: Support's need for CSV, maximum 1,000 rows, active-filter acceptance, and column question. The ticket itself is not supplied and was not read.
- [Original work-002 report download](../work-002-report-download/intent.md), source ops-meeting-22: Operations' need for the same CSV export, filtered downloads, at least 10,000 rows, UTC dates, and exporter-permission question. The meeting source itself is not supplied and was not read.
- [Product context](../../context/product.md): filterable internal reports; CSV and Excel are requested additions. Excel is outside this merged CSV request.
- [Engineering context](../../context/engineering.md): the reporting endpoint supports active row filters and export implementation is undecided. No code or tests are available to investigate further.
