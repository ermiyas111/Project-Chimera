<!--
Sync Impact Report

- Version change: 1.0.0 -> 1.0.1
- Modified principles: none
- Added sections: none
- Removed sections: none
- Templates checked: ✅ .specify/templates/plan-template.md
					 ✅ .specify/templates/spec-template.md
					 ✅ .specify/templates/tasks-template.md
- Follow-up TODOs: RATIFICATION_DATE needs confirmation (TODO)
-->

# Project Chimera Factory Constitution

## Core Principles

### SPEC-CENTRICITY (NON-NEGOTIABLE)
All functional behavior, acceptance criteria, data models and technical constraints MUST be defined in `/specs/*/functional.md` and
`/specs/*/technical.md`. No agent or implementer SHALL add features, logic, or behaviors that are not explicitly specified in those files.
Rationale: single source of truth prevents drift between design and implementation and preserves auditability.

### SWARM TOPOLOGY (NON-NEGOTIABLE)
The system MUST follow a strict Planner → Worker → Judge topology:
- Planner: Orchestrates the OODA loop (Observe, Orient, Decide, Act), composes tasks from specs, and assigns jobs to Workers.
- Worker: Stateless executor that performs a single, well-scoped task and emits structured output and diagnostics.
- Judge: Deterministic validator that verifies Worker outputs against the target influencer's `SOUL.md` and other contractual artifacts; Judges
	MUST accept or reject outputs and provide deterministic, machine-readable reasons for rework.
Rationale: separation of concerns enforces predictable behavior and enables safe automation.

### ARCHITECTURAL ABSTRACTION (NON-NEGOTIABLE)
All external platform interactions (e.g., X, YouTube, TikTok, payments, wallets) MUST be performed through Model Context Protocol (MCP)
servers. Worker logic MUST NOT make direct API calls to external platforms. Rationale: MCP abstraction centralizes credentials, auditing,
retries, and rate-limiting while enabling pluggable platform adapters.

### ECONOMIC GOVERNANCE (MANDATORY)
Every generated influencer entity MUST have a non-custodial wallet provisioned via Coinbase AgentKit or an approved equivalent. Financial
autonomy is mandatory. All economic events (payments, transfers, fees) MUST be recorded in the MCP "Sense" flight recorder with immutable
timestamps and transaction metadata. Rationale: protect user funds, ensure traceability, and separate execution from custody.

### PERSONA INTEGRITY (NON-NEGOTIABLE)
Each influencer's behavior and tone MUST conform to the constraints and rules in its `SOUL.md`. Judges MUST reject any output that violates
the Digital Soul. Any rejection MUST emit canonical reasons and remediation actions. Rationale: guardrails for ethics, brand, and legal
compliance.

### PERSISTENCE & PERPETUAL RELEVANCE (REQUIRED)
All metadata about multimodal assets (text, audio, video, prompts, model outputs) MUST be stored in the structured schema defined in
`/specs/*/technical.md`. The system MUST support a feedback loop—the "Perpetual Relevance Machine"—to update metadata, lifecycle state,
and re-ranking signals based on engagement and Judge outcomes.

## Definitions


## Operational Constraints

- All agents MUST log structured telemetry to MCP-observed channels; logs MUST include `spec_id`, `task_id`, `agent_role`, and `trace_id`.
- Tests: Every spec for an influencer MUST include acceptance tests mapping to `SOUL.md` rules and Judge criteria.
- No direct secrets in Worker code; secrets and credentials MUST be provisioned via MCP secrets or vault-backed MCP adapters.
- Privacy: Personal data MUST be minimized and stored with explicit retention in `technical.md`.

## Governance

Amendments to this constitution follow semantic versioning and an explicit approval flow:
- PATCH (x.y.z → x.y.(z+1)) for clarifications, wording fixes, non-functional edits.
- MINOR (x.y.z → x.(y+1).0) for adding new Principles or materially expanding guidance.
- MAJOR ((x.y.z) → (x+1).0.0) for removing or redefining Principles in a backward-incompatible way.

Amendment process:
- Propose change in `/docs/constitution/amendment-<short>.md` linking affected specs and templates.
- Run an impact analysis (automated checks + Planner simulation using a sample spec).
- Approval: 2 maintainers or a governance board; merge and update `Last Amended` date.

Compliance reviews:
- All feature plans (see `.specify/templates/plan-template.md`) MUST include a "Constitution Check" section referencing the gates in this file.

**Version**: 1.0.1 | **Ratified**: TODO(RATIFICATION_DATE) | **Last Amended**: 2026-02-04
