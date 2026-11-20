
import pytest

from backend.app.ai.providers.gemini import GeminiAIProvider


@pytest.mark.asyncio
async def test_gemini_responde():
    provider = GeminiAIProvider()

    resposta = await provider.generate(
        "Responda em português: diga apenas Olá, Atlas!"
    )

    print("RESPOSTA DO GEMINI:", resposta)

    assert resposta is not None
    assert isinstance(resposta, str)
    assert len(resposta.strip()) > 0
