# syntax=docker/dockerfile:1

FROM python:3.11-slim AS base

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

WORKDIR /app

RUN apt-get update \
    && apt-get install -y --no-install-recommends git curl \
    && rm -rf /var/lib/apt/lists/*

FROM base AS builder

COPY requirements.txt /app/requirements.txt
RUN pip install --upgrade pip \
    && pip install --prefix=/install -r /app/requirements.txt

FROM base AS runtime

# Placeholder environment variables for MCP + Coinbase AgentKit
ENV COINBASE_AGENTKIT_API_KEY="YOUR_KEY" \
    COINBASE_AGENTKIT_API_SECRET="YOUR_SECRET" \
    MCP_FILESYSTEM_ROOT="/app" \
    MCP_GIT_REPO="/app" \
    MCP_POSTGRES_URL="postgres://readonly_user:password@localhost:5432/chimera" \
    MCP_PROXY_URL="https://mcppulse.10academy.org/proxy"

COPY --from=builder /install /usr/local
COPY . /app

CMD ["python", "-m", "pytest", "tests/"]
