# Project Chimera Worker Skill Contracts

These skill contracts define the required input/output schemas for Worker agents. Workers are ephemeral, and Judges rely on these schemas for deterministic validation. All skills operate through MCP adapters and must respect the Digital Soul constraints defined in `SOUL.md` for the target influencer.

## skill_trend_fetcher

**Purpose**: Scan social data via MCP adapters and produce ranked trend signals for a specific niche and platform.

**Input Schema**:
```json
{
  "niche": "string",
  "platform": "string"
}
```

**Output Schema**:
```json
{
  "trend_list": [
    {
      "keyword": "string",
      "velocity_score": 0.0
    }
  ]
}
```

**Error States**:
- API_TIMEOUT
- SOURCE_UNAVAILABLE
- INVALID_PLATFORM

---

## skill_multimodal_generator

**Purpose**: Generate multimodal assets aligned with the Digital Soul using MCP-backed model adapters.

**Input Schema**:
```json
{
  "prompt_base": "string",
  "aspect_ratio": "string",
  "soul_id": "string"
}
```

**Output Schema**:
```json
{
  "local_path": "string",
  "metadata": {
    "soul_id": "string",
    "asset_type": "string",
    "created_at": "iso8601"
  }
}
```

**Error States**:
- MODEL_TIMEOUT
- POLICY_VIOLATION
- INVALID_ASPECT_RATIO

---

## skill_agentkit_manager

**Purpose**: Execute non-custodial economic actions using Coinbase AgentKit via an MCP wallet adapter, with traceable outcomes.

**Input Schema**:
```json
{
  "transaction_type": "send",
  "amount": 0.0,
  "destination": "string"
}
```

**Output Schema**:
```json
{
  "transaction_hash": "string",
  "network_status": "string"
}
```

**Error States**:
- INSUFFICIENT_FUNDS
- INVALID_DESTINATION
- NETWORK_TIMEOUT
- TX_REJECTED
