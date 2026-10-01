# Add CSV report export

## What and why
Add comma-separated values (CSV) report export alongside the existing PDF export format so administrators can export reports as CSV. The user's broader reason for needing CSV is unknown.

## Expected outcome
Administrators can choose CSV or the existing PDF format when exporting reports, with the same report columns, filters, and access rules.

## Constraints
Preserve the existing export format. Keep the export columns account_id and revenue, the date and region filters, and the administrator-only access rule. The current implementation evidence is described in Sources.

## Acceptance criteria

- CSV is accepted alongside PDF for report export.
- CSV exports contain the existing account_id and revenue columns in their existing order.
- Exported rows continue to match both the selected date and region.
- Only administrators can export reports; non-administrators remain denied.
- Existing PDF export behavior remains available.

## Open questions
The supplied implementation accepts PDF as a format but returns filtered row dictionaries rather than a serialized file. It does not establish a file delivery mechanism or CSV serialization conventions, such as header handling or encoding. Those details remain unknown.

## Sources

- User conversation: requested CSV report export alongside the existing export format, preserving existing columns, filters, and access rules.
- [Report export implementation](../../src/reports.py): declares PDF as the only supported format, defaults to PDF, selects account_id and revenue in that order, filters rows by exact date and region matches, and rejects users whose role is not admin. The function returns row dictionaries. No product or engineering context directory, additional project documentation, or tests were present; the relevant code was inspected directly.
