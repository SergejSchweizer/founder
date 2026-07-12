# Risks

Last reviewed: 2026-07-12

This file tracks active operational, data correctness, and architecture risks. Keep it aligned with `AGENTS.md` and project history when commits introduce or retire meaningful risks.

## R001. Exchange API Reliability Can Silently Reduce Historical Completeness

Status: Active

Signal: Deribit route errors, retry behavior, and long-running trade backfills appear repeatedly in project history.

Mitigation: Keep debug logs, checkpoint keys, deterministic windows, and completeness reports aligned before changing fetch execution.

## R002. Dataset Naming Drift Can Break Bronze, Silver, and Gold Joins

Status: Active

Signal: Dataset names have changed over time, including volatility cleanup and explicit OHLCV dataset naming.

Mitigation: Rename work must update registry specs, lake paths, contracts, CLI choices, manifests, tests, and docs in one change.

## R003. Large Refactors Can Blur Architecture Boundaries

Status: Active

Signal: Project history includes extraction work across loader, lake, Silver, and Gold services.

Mitigation: Keep dependency direction and side effects explicit; verify with architecture/import checks and focused regression tests.

## R004. Coverage and Strict Typing Can Drift After Broad Edits

Status: Active

Signal: Quality-gate commits show type coverage and test coverage are active project risks.

Mitigation: Run focused tests first, then full pytest, Ruff, and type checks before merging behavior or boundary changes.

## R005. Documentation Snapshots Can Become Stale Relative to the Lake

Status: Active

Signal: README coverage statistics and missing-day details have been refreshed several times.

Mitigation: Regenerate or explicitly date coverage snapshots when lake content, dataset names, or coverage reporting changes.

## Update Rules

Update this file whenever:

- A risk becomes newly active, retired, or materially changed.
- A mitigation changes because tests, logging, contracts, or docs changed.
- A release or migration changes operational behavior.

If project history tooling is available, regenerate or review risk evidence with:

```bash
uv run python scripts/update_project_history_docs.py
```