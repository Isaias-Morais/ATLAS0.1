import pytest

from backend.app.ai.router import AIRouter


def test_ai_router():
    modelos_texto = {
        "Google": ["Gemini 1.5 Pro", "Gemini 1.5 Flash"],
        "OpenAI": ["GPT-4o", "GPT-4o mini", "GPT-4 Turbo"],
        "Anthropic": ["Claude 3.5 Sonnet", "Claude 3.5 Haiku", "Claude 3 Opus"],
        "Meta": ["Llama 3.1", "Llama 3.2"],
        "Mistral AI": ["Mistral Large", "Mixtral 8x22B"]
    }

    router = AIRouter(modelos_texto)
    resultado = router.select_provider("Mistral AI")

    print(resultado)

    assert resultado is not None

