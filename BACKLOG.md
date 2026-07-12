# Backlog

Last reviewed: 2026-07-12

This backlog captures known work that should stay visible across sessions. Keep entries short, actionable, and tied to risks or decisions where possible.

## Now

- Scaffold the Python package layout for EODHD discovery, quote ingestion, validation, and portfolio optimization.
- Turn the manual `UCITS ETF` exchange enumeration into a repeatable command that writes token-free outputs.
- Define how EODHD EOD historical quotes will be fetched, stored, and validated without committing secrets.
- Add dependency and run instructions once the package structure is present.

## Next

- Add tests or smoke checks for EODHD discovery and quote ingestion before relying on historical completeness.
- Define portfolio constraints for the first minimum-risk optimization run.
- Document dataset names, lake paths, and schema contracts for instruments, quotes, returns, covariance, and weights.
- Add a repeatable quality gate command once test, lint, and type tools are present.

## Later

- Add completeness reporting for ETF quote-history coverage.
- Add duplicate ISIN/listing, currency, and survivorship-bias handling.
- Automate documentation refreshes for architecture, risks, decisions, README facts, and generated project-history summaries.
- Add release or migration notes for dataset renames and contract changes.

## Update Rules

Update this file whenever:

- Work is completed, deferred, split, or superseded.
- `RISKS.md` introduces a mitigation that requires follow-up work.
- `DECISIONS.md` records a decision with implementation tasks.
- A new dataset, external API, or quality gate is added.