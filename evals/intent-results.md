# Draft intent evaluation

Four focused scenarios passed after intake changed its capture document from request.md to intent.md. These runs exercised the draft status, updates to an existing draft, inbox placement, requested organization, and the boundary around accepted work.

Fresh Codex agents received the skill, each disposable project, and its user prompt without the grading checks. The maintainer reviewed the resulting documents against [the scenario checks](cases.json), compared preserved files with the fixtures, and checked relative Markdown links. The saved projects below contain the evaluated outputs.

| Scenario | Result and evidence |
| --- | --- |
| [Nested context](intent-artifacts/nested-context/docs/inbox/work-001-filtered-report-csv-export/intent.md) | Passed. Created a draft under docs/inbox; incorporated account-manager users, existing PDF behavior, date and region filters, and tenant isolation. Referenced both unchanged context files. |
| [Draft update](intent-artifacts/draft-intent-update/inbox/work-001-csv-export/intent.md) | Passed. Updated the existing draft with account ID and revenue columns, resolved the column question, and preserved filters and tenant isolation. Created no additional files. |
| [Accepted-work boundary](intent-artifacts/defined-work-boundary/inbox/work-008-manager-report-access/intent.md) | Passed. Captured a separate draft linked to accepted work and recorded the access-policy conflict. The accepted intent and its plan remained byte-for-byte unchanged. |
| [Requested merge and group](intent-artifacts/merge-conflict/inbox/work-004-report-export/intent.md) | Passed. Preserved source references, filters, UTC dates, unanswered questions, and conflicting row limits. Retained the absorbed entries with links to the canonical draft and kept the audit request distinct with group links. |

All newly created files were intent documents marked Status: draft. Context files remained unchanged, and relative Markdown links resolved. No scenario created a specification, implementation plan, or application code.

These are four focused runs, not a rerun of every current scenario. The earlier [evaluation results](results.md) apply to the previous request document format. Claude Code behavior was not evaluated by these runs; its plugin packaging is validated separately.
