import pytest

from backend.app.ai.router import AIRouter

def test_ai_router():
    modelos_texto = {
        "Mistral AI": "provider_teste"
    }

    router = AIRouter(modelos_texto)
    resultado = router.select_provider("Mistral AI")

    assert resultado == "provider_teste"