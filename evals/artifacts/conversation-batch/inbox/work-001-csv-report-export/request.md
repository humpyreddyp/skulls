# CSV export of filtered reports

## What and why
Support wants to export filtered reports as comma-separated values (CSV) files from the internal reporting product.

## Expected outcome
Support can obtain a CSV export whose rows match the active report filters.

## Constraints
Keep this need in the inbox for later selection and definition. Export columns are undecided. Export implementation has not been selected.

The [Excel export request](../work-002-excel-report-export/request.md) concerns the same reports and shares the filter requirement. Keep both needs distinct pending a decision on whether they should ship together.

## Acceptance criteria
- Support can export a filtered report as CSV.
- Exported rows match the report's active filters.

## Open questions
- Which report columns should the export contain? This determines the information Support receives in the file.
- Should CSV and Excel export ship together or separately? This determines the scope of later definition; the related Excel request preserves the same unresolved decision.

## Sources
- User conversation: Support requests CSV exports, rows must match active filters, columns are undecided, and all three needs must remain in the inbox.
- [Product context](../../context/product.md): identifies the internal reporting product, filterable reports, and CSV and Excel as requested additions.
- [Engineering context](../../context/engineering.md): confirms that the reporting endpoint supports active row filters and export implementation is unselected. No implementation code is available in the supplied project to verify additional behavior.
