import pytest

from backend.app.ai.router import AIRouter


def test_ai_router():
    modelos_texto = {
    }

    router = AIRouter(modelos_texto)
    resultado = router.select_provider("Mistral AI")

    print(resultado)

    assert resultado

