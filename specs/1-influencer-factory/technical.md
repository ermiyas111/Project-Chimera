# Technical Specification: Autonomous Influencer Factory

## API Contracts: Planner → Worker → Judge

Planner assigns tasks to Workers using the following JSON envelope:

```json
{
  "task_id": "string",
  "spec_id": "string",
  "planner_id": "string",
  "role": "string", // worker role
  "input": { },
  "meta": { "trace_id": "string", "deadline": "iso8601" }
}
```

Worker output schema:

```json
{
  "task_id":"string",
  "status":"success|error",
  "output": { },
  "vectors": [ [0.0, ...] ],
  "metadata": { "spec_id":"string", "agent_role":"worker", "duration_ms":0 }
}
```

Judge result schema:

```json
{
  "task_id":"string",
  "verdict":"accept|reject|human_review",
  "reasons":["string"],
  "confidence":0.0
}
```

## Persistence: PostgreSQL + pgvector

- Table `assets`:
  - `id` UUID PK
  - `influencer_id` UUID
  - `type` TEXT
  - `metadata` JSONB
  - `vector` VECTOR (pgvector)
  - `created_at` TIMESTAMP

- Table `tasks`:
  - `id` UUID PK
  - `spec_id` TEXT
  - `task_id` TEXT
  - `planner_id` TEXT
  - `status` TEXT
  - `payload` JSONB
  - `trace_id` TEXT

## MCP Adapter Contracts

- `mcp-adapter-openclaw`: Publish status updates and post content to OpenClaw network. Accepts signed `asset` references and returns `mcp_record_id`.
- `mcp-adapter-wallet`: Wallet provisioning and transactions via Coinbase AgentKit. Methods: `provision_wallet(influencer_id)`, `prepare_tx(wallet_id, tx)`, `submit_tx(signed_tx)`.
- `mcp-adapter-search`: External trend sources ingestion with rate-limiting and backoff; returns vectors and source metadata.

## Observability & Traceability

- All agents MUST emit structured logs (JSON) to MCP-observed channels including `spec_id`, `task_id`, `agent_role`, `trace_id`.
- Sense flight recorder MUST receive all wallet events with `mcp_record_id`.

## Security & Secrets

- No secrets in Worker code. MCP secrets/vault adapters provide credentials to adapters only. Workers call adapters over internal mTLS channels.
