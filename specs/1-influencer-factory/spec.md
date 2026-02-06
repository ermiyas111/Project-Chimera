# Feature Specification: Autonomous Influencer Factory

**Feature Branch**: `1-influencer-factory`  
**Created**: 2026-02-06  
**Status**: Draft  
**Input**: Architect a robust Factory system for spawning and managing Autonomous AI Influencers

## User Scenarios & Testing *(mandatory)*

### User Story 1 - Trend Research & Signal Collection (Priority: P1)

Product managers and Planners need automated trend signals to inform content strategies.

**Why this priority**: Foundation for content relevance and for the Perpetual Relevance Machine.

**Independent Test**: `trend_fetcher` returns time-series signals and top-10 trends for a given topic within 60s.

**Acceptance Scenarios**:
1. **Given** a topic and time window, **When** Planner requests trends, **Then** Worker returns a ranked list of trends (id, score, source, vector) and persistence metadata.
2. **Given** an unreachable source, **When** Worker fails, **Then** Planner receives a structured error and schedules a retry.

---

### User Story 2 - Persona-Consistent Content Generation (Priority: P1)

Planners request short-form content for an influencer; Workers generate drafts that Judges validate against `SOUL.md`.

**Independent Test**: `skills_interface` produces content drafts and a Judge run yields accept/reject with reasons.

**Acceptance Scenarios**:
1. **Given** a `SOUL.md` and prompt, **When** Worker generates content, **Then** Judge accepts when content adheres to allowed tones and does not trigger forbidden rules.

---

### User Story 3 - Autonomous Engagement & Economic Actions (Priority: P2)

Influencer may autonomously execute budgeted promotions or tip creators via an agent wallet.

**Independent Test**: Wallet provisioning via Coinbase AgentKit completes; a test transfer emits a Sense flight-record entry.

**Acceptance Scenarios**:
1. **Given** an influencer wallet with funds, **When** Planner schedules a promotion, **Then** Worker requests transaction via MCP wallet adapter and Sense records the event.

---

### Edge Cases

- Rate limits from source APIs (handled by MCP adapter with backoff).  
- Judge indeterminate result: fallback to human HITL review.  
- Wallet provisioning failure: mark influencer Disabled and alert maintainers.

## Requirements *(mandatory)*

### Functional Requirements

- **FR-001**: System MUST decompose tasks (Planner) and assign to stateless Workers.
- **FR-002**: Workers MUST emit structured outputs with `spec_id`, `task_id`, `trace_id` and `vector` metadata when applicable.
- **FR-003**: Judges MUST validate outputs against `SOUL.md` and return machine-readable accept/reject reasons.
- **FR-004**: All external interactions MUST be routed via MCP adapters (no direct API calls in Workers).
- **FR-005**: Each influencer MUST have a non-custodial wallet provisioned (Coinbase AgentKit) when economic actions are enabled.
- **FR-006**: All economic events MUST be recorded to the MCP Sense flight recorder with immutable timestamps.
- **FR-007**: Persistence: multimodal asset metadata MUST conform to the schema in `technical.md` and be stored in PostgreSQL (JSONB + vectors).

### Key Entities

- **Influencer**: id, `soul_id` (SOUL.md), wallet_id, status, metadata
- **Task**: id, spec_id, planner_id, worker_role, input, output, status, trace_id
- **Asset**: id, influencer_id, type (text/audio/video), storage_ref, metadata (JSONB), vector
- **WalletEvent**: id, wallet_id, type, amount, currency, trace, mcp_record_id

## Success Criteria *(mandatory)*

- **SC-001**: `trend_fetcher` returns top-10 trends with vectors for 95% of requests within 60s.
- **SC-002**: Judges accept > 90% of generated drafts for P1 scenarios without human escalations over a 7-day test window.
- **SC-003**: Wallet provisioning completes for 98% of influencer signups in staging.
- **SC-004**: All external calls in Worker logs reference an MCP adapter (100% coverage in CI linting).

## Constitution Compliance (MANDATORY)

- `SOUL.md` is included with persona rules and Judge acceptance criteria.  
- All described integrations reference MCP adapters (see `technical.md` adapter contracts).  
- Wallet provisioning uses Coinbase AgentKit; Sense flight recorder events are described in `technical.md`.  
- Persistence schema is provided in `technical.md`.

## Tests (TDD - mandatory for initial slices)

- **T-001 (trend_fetcher)**: fail-first test asserting `trend_fetcher(topic)` returns non-empty list and vectors; implement Worker until pass.
- **T-002 (skills_interface)**: fail-first test asserting `skills_interface(prompt, soul)` returns content and Judge accepts or provides deterministic rejection reasons.

## Notes

- This spec uses PostgreSQL (JSONB + pgvector) for metadata and semantic search.  
- OpenClaw status publishing is handled by a dedicated MCP adapter (openclaw-adapter) described in `openclaw_integration.md`.
