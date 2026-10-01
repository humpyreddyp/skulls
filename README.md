# Skulls

Small software-delivery skills for Codex and Claude Code. The first skill is **intake**: investigate incoming requests, capture draft intent documents, and record unresolved questions.

## Install

### Claude Code

Run inside Claude Code:

```text
/plugin marketplace add humpyreddyp/skulls
/plugin install skulls@skulls
```

Then use:

```text
/skulls:intake Capture these requests in the project inbox. Leave unresolved questions for later.
```

For a local development checkout, launch `claude --plugin-dir ./plugins/skulls` from this repository.

### Codex

```sh
codex plugin marketplace add humpyreddyp/skulls
codex plugin add skulls@skulls
```

Start a new chat after installation and select the plugin's `intake` skill, or ask: "Use Skulls intake to capture these requests in the project inbox."

For local development, register this repository with `codex plugin marketplace add /absolute/path/to/skulls`, then install `skulls@skulls`.

## What intake does

- Accepts conversations, `intake/` material, or explicitly identified sources.
- Uses product and engineering context when available; inspects relevant code and tests when context is missing or incomplete.
- Creates `inbox/` beside the directory containing that context: `docs/context/` produces `docs/inbox/work-NNN-short-summary/intent.md`. Without a context directory, uses the target project's root inbox.
- Records questions for gaps, contradictions, and ambiguities that the available evidence cannot resolve.
- Writes intent.md with Status: draft, recording what/why, expected outcome, constraints, known acceptance criteria, open questions, and sources. Missing answers can stay unknown. Later work refines the same file; the filename does not indicate approval to implement.
- Handles batches without requiring every request to be defined first.
- Uses multiple sources for one request when they describe the same need, preserving each source reference.
- Merges, groups, or splits existing inbox requests only when the user asks. Ordinary intake leaves related requests separate.
- Stops at the inbox. It does not automatically design, plan, implement, or approve captured work.

The same [SKILL.md](plugins/skulls/skills/intake/SKILL.md) serves both tools. Each plugin manifest points to the shared skill directory; `agents/openai.yaml` supplies optional Codex UI metadata. There are no hooks, MCP servers, or runtime dependencies.

## Evaluation

See [evals](evals/README.md) for reproducible behavioral scenarios and results. Plugin packaging and behavioral evaluation are checked separately.

## Format references

- [Claude Code skills](https://code.claude.com/docs/en/skills)
- [Claude Code plugins](https://code.claude.com/docs/en/plugins-reference)
- [Codex plugins](https://developers.openai.com/plugins/build/plugins)
