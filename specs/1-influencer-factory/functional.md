# Functional Specification: Autonomous Influencer Factory

## User Stories (Agent Roles)

### Planner Agent

- **Story**: As a Planner Agent, I need to discover trends for a given niche and platform, so that I can prioritize content opportunities.
	- **Acceptance Criteria**:
		- Trend discovery returns a ranked list of trends with velocity scores.
		- Each trend includes a keyword/tag and a numeric velocity score.
		- The result is associated with the requested niche and platform.

- **Story**: As a Planner Agent, I need to orchestrate tasks with clear inputs and deadlines, so that Workers can execute reliably.
	- **Acceptance Criteria**:
		- Tasks include `spec_id`, `task_id`, and required inputs.
		- Tasks can be routed to the correct Worker skill.

### Worker Agent

- **Story**: As a Worker Agent, I need to execute tasks statelessly using MCP tools, so that operations are auditable and secure.
	- **Acceptance Criteria**:
		- External interactions are routed through MCP adapters only.
		- Worker outputs adhere to the skill schemas defined in skills/README.md.

- **Story**: As a Worker Agent, I need to return structured outputs for content generation, so that Judges can validate results.
	- **Acceptance Criteria**:
		- Outputs include expected keys for each skill (e.g., `local_path`, `metadata`).
		- Errors are returned in a consistent, machine-readable format.

### Judge Agent

- **Story**: As a Judge Agent, I need to validate Worker outputs against `SOUL.md`, so that influencer behavior remains compliant.
	- **Acceptance Criteria**:
		- Outputs violating the Digital Soul are rejected with specific reasons.
		- Accepted outputs include a verdict and confidence score.

- **Story**: As a Judge Agent, I need to enforce schema compliance, so that invalid outputs never propagate.
	- **Acceptance Criteria**:
		- Missing required fields result in rejection.
		- Data types are validated (e.g., velocity score is numeric).

### Human Reviewer (HITL)

- **Story**: As a Human Reviewer, I need to review low-confidence outputs, so that high-risk decisions are verified.
	- **Acceptance Criteria**:
		- Review tasks include context, diff, and reason for escalation.
		- Feedback from the reviewer is captured and returned to the Planner.
