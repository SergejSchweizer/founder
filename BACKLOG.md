# Backlog

Last reviewed: 2026-07-12

This backlog captures known work that should stay visible across sessions. Keep entries short, actionable, and tied to risks or decisions where possible.

## Now

- Confirm the repository layout and restore or scaffold expected project files beyond the current documentation baseline.
- Add dependency and run instructions once the package structure is present.
- Define how EODHD EOD historical data will be fetched, stored, and validated without committing secrets.

## Next

- Add tests or smoke checks for any EODHD ingestion path before relying on it for historical completeness.
- Document dataset names, lake paths, and schema contracts when the first EODHD dataset is introduced.
- Add a repeatable quality gate command once test, lint, and type tools are present.

## Later

- Automate documentation refreshes for architecture, risks, decisions, and generated project-history summaries.
- Add completeness reporting for historical market data coverage.
- Add release or migration notes for dataset renames and contract changes.

## Update Rules

Update this file whenever:

- Work is completed, deferred, split, or superseded.
- `RISKS.md` introduces a mitigation that requires follow-up work.
- `DECISIONS.md` records a decision with implementation tasks.
- A new dataset, external API, or quality gate is added.