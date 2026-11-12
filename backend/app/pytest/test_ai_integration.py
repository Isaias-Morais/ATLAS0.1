import pytest
from backend.app.ai.providers.fake import FakeAIProvider
from backend.app.ai.router import AIRouter
from backend.app.services.ai_service import AIService


@pytest.mark.asyncio

async def test_ai_integration():
    fake = FakeAIProvider()

    modelos_dict = {
        "fakeprovider":fake,
    }

    router = AIRouter(modelos_dict)

    resultado_ai = router.select_provider('fakeprovider')

    ai = AIService(provider=resultado_ai)

    resultado_geral = await ai.generate('oi')

    assert resultado_geral == "Resposta simulada da IA"
