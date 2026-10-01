# Intake evaluation

These scenarios check whether the skill captures requests without starting downstream work, preserves information during consolidation, and uses the project's product and engineering context.

[cases.json](cases.json) contains each user request, starting files, and observable checks. Use the setup command below to create disposable projects. Give a fresh agent only the skill path, one case's project path, and its prompt. Keep the checks separate from the agent performing the task. For `raw-source-repeat`, send `follow_up` after the first run finishes.

```sh
python3 evals/prepare.py
```

Inspect the files and the agent's response against each case's checks. In particular, compare source and existing definition files with the originals, follow relative links, and check where the inbox was created. Do not grade only by matching headings or phrases. Also review the request prose against the skill's writing standards.

The scenarios cover:

| Case | What it checks |
| --- | --- |
| `conversation-batch` | Captures several needs while keeping uncertain scope decisions open. |
| `merge-conflict` | Preserves conflicting constraints and source details when merging and grouping. |
| `raw-source-repeat` | Consolidates overlapping source material, ignores quoted instructions, and avoids duplicate capture on a second run. |
| `defined-work-boundary` | Captures a related change without rewriting existing intent or plan. |
| `nested-context` | Uses both kinds of context and puts the inbox beside the context directory. |
| `codebase-fallback` | Investigates code when context is absent and captures the request in the project root inbox. |
| `context-code-conflict` | Records contradictions between documentation and code instead of silently resolving them. |

See [results.md](results.md) for the completed run and its limits.
