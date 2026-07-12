# Architecture

Last reviewed: 2026-07-12

## Purpose

This project collects, transforms, and validates market data across Bronze, Silver, and Gold layers. The architecture should keep data ingestion, storage contracts, transformation logic, and validation gates separated so changes can be tested locally and reviewed safely.

## Current Shape

- **Bronze**: Raw exchange/API ingestion and lake persistence.
- **Silver**: Normalized datasets with registry-backed names, schemas, and contracts.
- **Gold**: Feature-ready datasets and regime/analytics outputs derived from Silver inputs.
- **Validation**: Focused tests first, followed by full quality gates for behavior, typing, formatting, architecture boundaries, and coverage.
- **Configuration**: Secrets and local credentials live in ignored local environment files such as `.env.local`.

## Boundaries

- Fetch planning, checkpointing, retries, and completeness reporting belong near ingestion code.
- Dataset names, lake paths, contracts, manifests, CLI choices, and tests must move together.
- Transformation code should depend on explicit inputs and contracts, not hidden global state.
- Documentation snapshots must state their review date or be regenerated from source data.

## Update Rules

Update this file whenever a change alters one of these items:

- A layer boundary or dependency direction.
- Dataset ownership, naming, contracts, or lake paths.
- Validation gates, architecture checks, or required release commands.
- Local configuration conventions that affect reproducibility.

Before merging architecture changes, update `RISKS.md`, `DECISIONS.md`, and `BACKLOG.md` when the change creates, resolves, or reprioritizes work.