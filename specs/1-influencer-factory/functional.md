# Functional Specification: Autonomous Influencer Factory

## High-level workflow

1. Planner observes signals (trend_fetcher) → composes tasks with `spec_id` and requirements.
2. Planner schedules tasks to Workers via the task queue (MCP-observed).  
3. Worker executes stateless task (e.g., fetch trends, generate draft, create asset metadata) and emits structured output.
4. Judge validates Worker output against `SOUL.md` and either accepts, rejects with reasons, or escalates to HITL.
5. Accepted outputs are persisted; Planner may schedule downstream tasks (publish, promote).

## Agent Roles

- Planner: responsible for OODA orchestration, task decomposition, budget allocation, and retry/backoff policies.
- Worker: stateless micro-tasks with strict input/output JSON schema; MUST not call external APIs directly (use MCP adapters).
- Judge: deterministic rules engine and policy checker that evaluates outputs against `SOUL.md` and constitutional gates.

## Key workflows (examples)

- Trend Fetching: Planner → Worker(trend_fetcher) → MCP adapters fetch sources → Worker returns ranked list + vectors → Judge (sanity) → Persist
- Content Generation: Planner → Worker(prompt/template) → Model via MCP → Draft → Judge(SOUL) → Persist/Publish
- Wallet Action: Planner → Worker(prepare_tx) → Wallet MCP adapter → Sense records event → Confirm

## Human-in-the-Loop (HITL)

- Judges provide confidence scores. Below threshold → create HITL review task assigned to human reviewer; include task context and diffs.
