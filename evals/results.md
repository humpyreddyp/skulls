# Intake evaluation results

Evaluated on October 1, 2026 using independent Codex agents. Each agent received the skill, a user request, and a disposable project. A separate reviewer inspected the resulting files against the [scenario checks](cases.json). Claude Code's own validator checked its plugin and marketplace manifests; no Claude model session ran the behavioral scenarios.

## Observed behavior

| Scenario | Result and evidence |
| --- | --- |
| Conversation batch | [Three requests](artifacts/conversation-batch/inbox/) capture CSV export, Excel export, and login investigation separately. The export requests preserve shared filters and link to each other while leaving joint delivery undecided. |
| Merge and group | [Merged requests](artifacts/merge-conflict/inbox/) preserve both row-limit requirements as a conflict, retain the absorbed request, and link the audit request without merging its identity. |
| Source intake and repeat | [Two requests](artifacts/raw-source-repeat/inbox/) consolidate duplicate export material and keep login separate. Raw sources are unchanged, and quoted instructions did not produce implementation or definition artifacts. The executor reported no changes on repeat; no first-run snapshot was saved, so temporal claims are only partially verified. |
| Existing defined work | [Manager-access request](artifacts/defined-work-boundary/inbox/) records the conflict with existing administrator-only access. The existing intent and plan remain byte-for-byte unchanged. |
| Nested context | [Request beside the context directory](artifacts/nested-context/docs/inbox/) uses the product's users and filters and the engineering requirement for tenant isolation. No root-level inbox was created. |
| Codebase fallback | [Code-grounded request](artifacts/codebase-fallback/inbox/) preserves the columns, filters, permissions, and existing format established by code. It does not demand context documents or change the implementation. |
| Context and code conflict | [Support request](artifacts/context-code-conflict/docs/inbox/) records that documentation promises CSV while the code accepts only PDF. The intended behavior remains a product question. |

## Improvement from evaluation

The first review found unnecessary generic acceptance questions and questions about routine CSV formatting. The skill now requires each question to identify a specific consequential decision, derives acceptance criteria from stated outcomes, and carries shared requirements across related requests. Fresh agents reran the batch and nested-context scenarios. Their requests retain only the relevant open decisions and preserve the shared filtering requirement.

## Verification limits

All final relative links resolve. Code, context, raw material, and existing definitions were preserved; only authorized request artifacts changed. Accurate references establish that outputs are grounded in the supplied evidence, but artifact inspection alone does not prove every tool read or every conversational step.

The source-repeat executor reported a second pass with no changes. Without a first-pass snapshot, the independent reviewer verified the final absence of duplicates and preservation of information, not the exact before-and-after history.

These are focused scenario evaluations, not a statistical success-rate estimate or a runtime comparison between Codex and Claude. [The detailed grades](grades.json) record each check and its evidence. [Saved projects](artifacts/) let reviewers inspect the outputs alongside their original context and sources; [the scenario definitions](cases.json) retain the original fixture contents for comparison.
