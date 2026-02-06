from unittest import mock

import pytest


# These tests act as the "Judge": strict schema validation for Worker outputs.

def test_multimodal_generator_validation_and_output_schema():
    try:
        from skills.multimodal_generator import skill_multimodal_generator
        from skills.exceptions import ValidationError
    except ImportError as exc:
        raise exc

    with pytest.raises(ValidationError):
        skill_multimodal_generator(prompt_base="hi", aspect_ratio=123, soul_id="nova")

    mocked_output = {
        "local_path": "C:/tmp/asset.png",
        "metadata": {"soul_id": "nova", "asset_type": "image", "created_at": "2026-02-06T00:00:00Z"},
    }

    with mock.patch("skills.multimodal_generator.generate_multimodal_asset", return_value=mocked_output):
        result = skill_multimodal_generator(prompt_base="hi", aspect_ratio="1:1", soul_id="nova")

    assert set(result.keys()) == {"local_path", "metadata"}
    assert "soul_id" in result["metadata"]


def test_agentkit_manager_validation_and_output_schema():
    try:
        from skills.agentkit_manager import skill_agentkit_manager
        from skills.exceptions import ValidationError
    except ImportError as exc:
        raise exc

    with pytest.raises(ValidationError):
        skill_agentkit_manager(transaction_type="send", amount="ten", destination="addr")

    mocked_output = {"transaction_hash": "0xabc", "network_status": "confirmed"}

    with mock.patch("skills.agentkit_manager.submit_transaction", return_value=mocked_output):
        result = skill_agentkit_manager(transaction_type="send", amount=1.0, destination="addr")

    assert set(result.keys()) == {"transaction_hash", "network_status"}
