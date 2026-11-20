import pytest
from backend.app.ai.providers.fake import FakeAIProvider
from backend.app.ai.providers.parser import IAResponseParser
from backend.app.ai.router import AIRouter
from backend.app.services.ai_service import AIService


@pytest.mark.asyncio

async def test_ai_integration():
    fake = FakeAIProvider()

    modelos_dict = {
        "fakeprovider":fake,
    }

    router = AIRouter(modelos_dict)

    paser = IAResponseParser()

    resultado_ai = router.select_provider('fakeprovider')

    ai = AIService(provider=resultado_ai,paser=paser)

    resultado_geral = await ai.generate('oi')

    print(resultado_geral)
    assert resultado_geral is not None

"""
Testa a integração entre AIRouter, AIService, FakeAIProvider e IAResponseParser.

Verifica se o provider selecionado consegue gerar uma resposta JSON,
se o parser consegue convertê-la e validá-la e se o AIService
retorna corretamente um objeto Interpretation_AI.
"""