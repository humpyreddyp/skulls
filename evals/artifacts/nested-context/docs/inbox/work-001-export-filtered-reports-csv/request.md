# Export filtered reports as CSV

## What and why
Account managers need to export filtered reports as comma-separated values (CSV). Reports currently support PDF downloads only; users already filter reports by date and region.

## Expected outcome
Users can download report data as CSV with their selected date and region filters applied.

## Constraints
Exports must preserve tenant isolation: downloaded data must belong to the current tenant. Capture this as draft intent and leave unresolved decisions for later definition.

## Acceptance criteria
- Users can export filtered report data as CSV.
- CSV results respect the selected date and region filters.
- CSV exports contain no data from other tenants.

## Open questions
Which report fields should the CSV contain? The available context does not describe report fields, so the exported content remains to be defined.

## Sources
- User conversation: requested CSV export of filtered reports and deferred open decisions.
- [Product context](../../context/product.md): identifies account managers, date and region filters, and existing PDF-only downloads.
- [Engineering context](../../context/engineering.md): establishes tenant isolation and existing backend date and region filters.
