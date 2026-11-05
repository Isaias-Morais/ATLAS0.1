import pytest

from backend.app.ai.providers.fake import FakeAIProvider


@pytest.mark.asyncio
async def test_fake_provider():
    fake = FakeAIProvider()
    resultado = await fake.generate('oi')

    assert resultado == "Resposta simulada da IA"