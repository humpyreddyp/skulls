# Excel export of filtered reports

## What and why
Operations wants Excel exports of the same filtered reports requested by Support for CSV export.

## Expected outcome
Operations can obtain an Excel export whose rows match the active report filters.

## Constraints
Keep this need in the inbox for later selection and definition. Carry forward the shared requirement that exported rows match active filters. The shared reports' export columns remain undecided, and export implementation has not been selected.

The [CSV export request](../work-001-csv-report-export/request.md) shares the reporting outcome. Keep the requests linked and distinct until the user decides whether to define and ship them together.

## Acceptance criteria
- Operations can export the same reports as Excel files.
- Exported rows match the report's active filters.

## Open questions
- Should Excel export ship with CSV or separately? This determines whether later definition covers both requests or separate scopes.
- Which columns should the shared report exports contain? This determines the information Operations receives; resolve this alongside the related CSV column decision.

## Sources
- User conversation: Operations requests Excel exports of the same reports, whether it ships with CSV is undecided, and all three needs must remain in the inbox.
- [CSV request](../work-001-csv-report-export/request.md): preserves the explicitly shared active-filter requirement and undecided export columns from the conversation.
- [Product context](../../context/product.md): identifies filterable reports and CSV and Excel as requested additions.
- [Engineering context](../../context/engineering.md): confirms support for active row filters and that export implementation is unselected. No implementation code is available in the supplied project to verify additional behavior.
