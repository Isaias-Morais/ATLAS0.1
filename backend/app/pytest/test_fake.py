import pytest
import json

from backend.app.ai.providers.fake import FakeAIProvider


@pytest.mark.asyncio
async def test_fake_provider():
    fake = FakeAIProvider()
    resultado = await fake.generate('oi')

    dados = json.loads(resultado)

    assert dados["type"] == "conversation"
    assert dados["message"] == "Olá! Como posso ajudar?"
    assert dados["command"] is None