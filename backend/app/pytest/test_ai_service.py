import pytest
from backend.app.ai.providers.fake import FakeAIProvider
from backend.app.services.ai_service import AIService
from backend.app.ai.providers.parser import IAResponseParser

@pytest.mark.asyncio
async def test_ai_service():
    fake = FakeAIProvider()
    parser = IAResponseParser()

    ai = AIService(provider=fake, paser=parser)
    resultado = await ai.generate('oi')

    assert resultado.type == "conversation"
    assert resultado.message == "Olá! Como posso ajudar?"
    assert resultado.command is None