import datetime
from unittest import mock

import pytest


# These tests act as the "Judge": strict schema validation for Worker outputs.

def test_trend_fetcher_schema_with_mocked_response():
    try:
        from skills.trend_fetcher import trend_fetcher
    except ImportError as exc:
        raise exc

    mocked_response = {
        "trends": [
            {"tag": "ai", "velocity": 1.23},
            {"tag": "robotics", "velocity": 0.87},
        ],
        "timestamp": "2026-02-06T00:00:00Z",
    }

    with mock.patch("skills.trend_fetcher.fetch_trends_from_mcp", return_value=mocked_response):
        result = trend_fetcher(niche="ai", platform="x")

    assert "trends" in result
    assert "timestamp" in result

    assert isinstance(result["timestamp"], str)
    datetime.datetime.fromisoformat(result["timestamp"].replace("Z", "+00:00"))

    assert isinstance(result["trends"], list)
    for item in result["trends"]:
        assert set(item.keys()) == {"tag", "velocity"}
        assert isinstance(item["tag"], str)
        assert isinstance(item["velocity"], float)


@pytest.mark.xfail(reason="Skill not implemented yet; expected to fail until Worker is built")
def test_trend_fetcher_not_implemented():
    try:
        from skills.trend_fetcher import trend_fetcher
    except ImportError:
        raise

    with pytest.raises(NotImplementedError):
        trend_fetcher(niche="ai", platform="x")
