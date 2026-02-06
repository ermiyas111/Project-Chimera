# MCP Tooling Strategy (Project Chimera)

## Purpose
Configure and document the MCP (Model Context Protocol) layer that powers tooling for the Project Chimera Factory. This ensures Workers use approved adapters, maintain traceability, and stay scoped to the project root.

## Repository MCP Configuration

**Detected local MCP config**: .vscode/mcp.json

This file currently contains a single HTTP proxy. The configuration below extends it with additional local MCP servers while enforcing root scoping.

## MCP Server Roles (Factory Architecture)

### 1) mcp-server-filesystem
- **Role**: Controlled filesystem access for Spec Kit and code manipulation.
- **Why it matters**: Enables Workers to read/write within the repo while preserving the Safety Layer.
- **Scope**: Must be restricted to the project root only.

### 2) mcp-server-git
- **Role**: Branch management, diff inspection, and repository history for controlled implementation.
- **Why it matters**: Supports Planner/Worker pipelines with version-aware task execution.
- **Scope**: Limited to the repo root; no access outside the working tree.

### 3) mcp-server-postgres
- **Role**: Query high-velocity video metadata and vector memory (pgvector) for retrieval and evaluation.
- **Why it matters**: Powers semantic memory and trend indexing for the Factory.
- **Scope**: Restrict to read-only role and to project-owned DB resources.

### 4) mcp-server-sequential-thinking
- **Role**: Enforces architectural discipline during complex tasks (reasoning scaffold).
- **Why it matters**: Helps keep Worker execution aligned with the Constitution and spec constraints.

## Configuration JSON (example)

> Replace placeholder paths and connection strings. All filesystem access is restricted to the repo root.

```json
{
  "servers": {
    "filesystem": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-filesystem", "/path/to/project-root"],
      "env": {}
    },
    "git": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-github", "--repo", "/path/to/project-root"],
      "env": {}
    },
    "postgres": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-postgres", "postgresql://readonly_user:password@localhost:5432/chimera"],
      "env": {}
    },
    "sequential-thinking": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-sequential-thinking"],
      "env": {}
    }
  }
}
```

## Installation & Run Commands

### Node-based servers (recommended)
- **filesystem**:
  - Install: `npm i -g @modelcontextprotocol/server-filesystem`
  - Run: `npx @modelcontextprotocol/server-filesystem /path/to/project-root`
- **git**:
  - Install: `npm i -g @modelcontextprotocol/server-github`
  - Run: `npx @modelcontextprotocol/server-github --repo /path/to/project-root`
- **postgres**:
  - Install: `npm i -g @modelcontextprotocol/server-postgres`
  - Run: `npx @modelcontextprotocol/server-postgres postgresql://readonly_user:password@localhost:5432/chimera`
- **sequential-thinking**:
  - Install: `npm i -g @modelcontextprotocol/server-sequential-thinking`
  - Run: `npx @modelcontextprotocol/server-sequential-thinking`

## Safety & Alignment with Constitution

- **Worker access**: Workers can use MCP servers only; direct external APIs are disallowed.
- **Root restrictions**: Filesystem and git servers are limited to `/path/to/project-root`.
- **Data access**: Postgres access uses read-only credentials unless elevated by Planner approval.
- **Traceability**: All Worker actions must include `spec_id`, `task_id`, `agent_role`, and `trace_id` in MCP-observed logs.

## Automated Governance (CI + AI Review)

The Autonomous Oversight layer enforces a "Judge" gate before changes can be trusted:

- **CI Gate**: GitHub Actions runs `make build` and `make test` on push and pull_request to `main`. CI fails if tests fail.
- **AI Review Gate**: Code review policies require spec alignment against `specs/` and `skills/README.md`, security checks for
  hardcoded API keys (especially Coinbase AgentKit), and Digital Soul consistency against `specs/core/spec.md`.

## Open Items

- Replace `/path/to/project-root` with the actual repository root.
- Set a read-only Postgres user and rotate credentials before production use.
