import pytest

from backend.app.ai.providers.fake import FakeAIProvider
from backend.app.services.ai_service import AIService


@pytest.mark.asyncio
async def test_ai_service():
    fake = FakeAIProvider()
    ai = AIService(provider=fake)
    resultado = await ai.generate('oi')

    assert resultado == "Resposta simulada da IA"