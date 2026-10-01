# Export filtered reports as CSV

Status: draft

## What and why
Let account managers export filtered reports as comma-separated values (CSV) files. Reports currently support PDF downloads only; the request adds a CSV option for filtered report data.

## Expected outcome
Users can download report data as CSV with their selected date and region filters applied.

## Constraints
Exports must preserve tenant isolation: users can export only data belonging to their current tenant. Date and region filters are already available in the backend. This capture leaves product decisions open for later definition.

## Acceptance criteria

- Users can export a filtered report as a CSV file.
- Exported data matches the selected date and region filters.
- Exported data contains no records from another tenant.

## Open questions

- Which report fields should the CSV include? The available context does not define report fields or an export column set, and this determines the data users receive.

## Sources

- User conversation: requested CSV export of filtered reports and asked to keep open decisions for later.
- [Product context](../../context/product.md): identifies account managers as report users, date and region filtering, and existing PDF-only downloads.
- [Engineering context](../../context/engineering.md): establishes current-tenant access, the tenant isolation requirement for exports, and existing backend date and region filters. No application code or tests were available to establish report fields.
