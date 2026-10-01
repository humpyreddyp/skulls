# CSV export for filtered reports

## What and why
Customers need to export filtered reports as comma-separated values (CSV). The customer and support requests describe the same outcome and are captured together here.

## Expected outcome
Users can download report data that matches the row filters visible when they export it.

## Constraints
Preserve visible row filters. Required export columns are undecided.

## Acceptance criteria
- Users can export reports as CSV.
- The exported rows match the visible row filters.

## Open questions
- Which columns must the CSV include?

## Sources
- [Customer call](../../intake/customer-notes.md): requests CSV export, preservation of visible filters, and leaves columns undecided.
- [Team notes](../../intake/team-notes.md): confirms that customer and support requests are duplicates.
- [Product context](../../context/product.md): establishes existing filterable reports and identifies CSV as a requested addition.
- [Engineering context](../../context/engineering.md): confirms that the reporting endpoint supports active row filters and that export implementation has not been selected.
