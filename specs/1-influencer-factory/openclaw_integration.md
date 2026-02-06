# OpenClaw Integration Plan

Purpose: Publish influencer status and public assets to the OpenClaw social network via an MCP adapter.

## Flow

1. Planner marks an asset for publication.
2. Worker prepares a signed content package and stores asset metadata.
3. Worker calls `mcp-adapter-openclaw.publish(asset_ref, metadata)`.
4. Adapter returns `mcp_record_id` and post URL; adapter must handle rate limits and retries.
5. Persist `mcp_record_id` in `assets.metadata.published_records`.

## Adapter contract

- Input: `{ "asset_ref": "string", "metadata": { ... }, "visibility": "public|followers" }`
- Output: `{ "status":"ok|error", "mcp_record_id":"string", "url":"string" }`

## Safety

- Adapter MUST validate content against provided `SOUL.md` accept rules before publishing; if adapter cannot validate, it must return `human_review`.
