# Lake Contracts

Last reviewed: 2026-07-12

## Table Of Contents

- [Layers](#layers)
- [Core Tables](#core-tables)
- [How This Fits The Onboarding Flow](#how-this-fits-the-onboarding-flow)

Founder uses deterministic local lake artifacts under a `LakePaths` root. The current implementation keeps runtime dependencies small by writing table rows as newline-delimited JSON through `founder.table_io` while preserving the table-oriented paths and schema names used by the backlog.

Read this after [ARCHITECTURE.md](../ARCHITECTURE.md) and before changing Search, Fetch, Gold, or storage code. Read [docs/search_fetch_workflow.md](search_fetch_workflow.md) for executable examples that use these contracts.

## Layers

- Bronze stores raw or near-raw EODHD search, quote, and fundamentals payloads.
- Silver stores normalized search candidates, canonical universe rows, quote rows partitioned by year, and selected fundamentals profile rows.
- Gold stores adjusted-close returns, correlation, and covariance rows.
- Meta stores the active universe pointer, fetch plans, fetch runs, coverage, errors, and dry-run summaries.

Runtime logs are intentionally outside the lake under `.logs/`. They are operational diagnostics, not dataset artifacts.

## Core Tables

- `search_candidates`: normalized discovery rows with search run id, query, endpoint, instrument identifiers, type, country, currency, ISIN, name, normalized name, and discovery timestamp.
- `canonical_universe`: one selected listing per ISIN, including selection reason and `selected_for_fetch=true`.
- `fetch_plan`: run id, ISIN, code, exchange, derived EODHD symbol, start date, and end date.
- `quotes`: normalized OHLCV rows with adjusted close, currency, run id, and fetch timestamp.
- `fundamentals_profile`: selected profile fields from archived fundamentals payloads.
- `coverage`: first and last quote dates, observed rows, missing periods, and next incremental fetch start.
- `errors`: non-secret fetch error records.
- `returns`, `correlation`, and `covariance`: Gold risk-input tables built from validated Silver quote rows.

## How This Fits The Onboarding Flow

Use the deterministic mocked pipeline to see these contracts written end to end:

```bash
uv run founder dry-run --root data/dry-run
```

The dry run is safe to repeat and rewrites the same sample artifacts deterministically.