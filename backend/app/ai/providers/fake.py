from backend.app.ai.providers.base import BaseAIProvider

class FakeAIProvider(BaseAIProvider):

    async def generate(self, prompt: str) -> str:
        if not prompt:
            return "Please enter a valid prompt"
        return "Resposta simulada da IA"
