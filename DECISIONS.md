# Decisions

Last reviewed: 2026-07-12

Record durable technical decisions here. Use short entries with context, decision, consequences, and update triggers.

## D001. Keep Local Secrets Out of Git

Date: 2026-07-12

Context: The project needs local API credentials for EODHD EOD historical data.

Decision: Store local credentials in ignored environment files such as `.env.local`. Track only examples or documentation, never real tokens.

Consequences: Any code that needs credentials should read from environment variables or local config loaders. `.gitignore` must continue excluding `.env` and `.env.*` while allowing `.env.example`.

Update trigger: Revisit if the project adopts a dedicated secret manager, encrypted local config, or deployment-specific credential flow.

## D002. Track Architecture, Risks, Backlog, and Decisions as First-Class Docs

Date: 2026-07-12

Context: The workspace needs persistent project memory that survives coding sessions and gives future changes a review checklist.

Decision: Maintain `ARCHITECTURE.md`, `RISKS.md`, `BACKLOG.md`, and `DECISIONS.md` at the repository root and stage them in Git.

Consequences: Changes that affect architecture, risk, planned work, or durable technical direction must update the corresponding document in the same change.

Update trigger: Revisit if these docs move into generated documentation or a different project governance system.

## Update Rules

Add or update a decision when:

- A choice changes data contracts, external APIs, deployment, storage, or quality gates.
- A decision explains why a non-obvious approach was selected.
- A previous decision is replaced or retired.

Do not rewrite old decisions silently. Add a superseding entry and mark the old decision as superseded.