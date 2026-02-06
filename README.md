# Project Chimera

Project Chimera is an autonomous influencer factory: a governed, spec-driven system that spawns and manages AI influencers to research trends, create content, and engage audiences with economic agency. The goal is to provide a repeatable, auditable pipeline where Planner, Worker, and Judge roles enforce quality, safety, and brand integrity while MCP adapters handle external integrations.

At the core is a hierarchical swarm. Planners orchestrate the OODA loop, Workers execute stateless tasks with strict input/output schemas, and Judges validate outputs against each influencer's Digital Soul. This separation keeps behavior predictable, traceable, and aligned with the governing specs.

Project Chimera is designed to support multiple business models, from a Digital Talent Agency (operating influencer portfolios for clients) to a PaaS platform where customers configure their own personas and budgets. The system emphasizes safety and oversight via human-in-the-loop escalation when Judge confidence is low.

Key goals include:
- Reproducible, containerized development and testing to preserve TDD discipline.
- MCP-only external access for security, observability, and modular integrations.
- Persistent multimodal metadata storage for long-term relevance and ranking.
- Economic autonomy via non-custodial wallets with full audit trails.

## User Guide

### 1) Review the specs
- Start with the active spec in specs/ and confirm the feature scope, contracts, and constraints.
- The system is spec-driven; implementations must align to functional and technical specs.

### 2) Understand the roles
- Planners orchestrate tasks, Workers execute stateless skills, and Judges validate outputs.
- Skills and schemas are defined in skills/README.md.

### 3) Run the checks
- Use Makefile targets to build and test the containerized environment.
- Tests are expected to fail until Worker skills are implemented (TDD flow).

### 4) Iterate safely
- Use MCP adapters for all external access.
- Ensure new logic stays consistent with each influencer's Digital Soul.

