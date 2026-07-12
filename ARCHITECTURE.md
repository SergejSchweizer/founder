# Architecture

Last reviewed: 2026-07-12

## Purpose

This project analyzes EODHD end-of-day ETF quotes and builds minimum-risk fund portfolio weights. The architecture should keep instrument discovery, quote ingestion, storage contracts, transformation logic, optimization, and validation gates separated so changes can be tested locally and reviewed safely.

## Current Shape

- **Discovery**: EODHD search and exchange symbol-list enumeration identify ETF and fund universes by ticker, name, ISIN, exchange, and type.
- **Bronze**: Raw EODHD API responses and quote ingestion outputs.
- **Silver**: Normalized ETF quote and instrument datasets with stable identifiers, schema checks, and coverage metadata.
- **Gold**: Portfolio-ready return, covariance, risk, and optimized-weight datasets derived from validated Silver inputs.
- **Validation**: Focused tests first, followed by full quality gates for behavior, typing, formatting, architecture boundaries, and coverage.
- **Configuration**: Secrets and local credentials live in ignored local environment files such as `.env.local`.

## Boundaries

- Discovery, fetch planning, checkpointing, retries, and completeness reporting belong near ingestion code.
- Dataset names, lake paths, contracts, manifests, CLI choices, and tests must move together.
- Transformation code should depend on explicit inputs and contracts, not hidden global state.
- Optimization code should consume validated quote history and explicit constraints, not raw API responses.
- Documentation snapshots must state their review date or be regenerated from source data.

## Update Rules

Update this file whenever a change alters one of these items:

- A layer boundary or dependency direction.
- Dataset ownership, naming, contracts, or lake paths.
- Validation gates, architecture checks, or required release commands.
- Local configuration conventions that affect reproducibility.

Before merging architecture changes, update `RISKS.md`, `DECISIONS.md`, and `BACKLOG.md` when the change creates, resolves, or reprioritizes work.