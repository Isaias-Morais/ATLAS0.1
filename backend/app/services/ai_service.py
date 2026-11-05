from backend.app.ai.providers.base import BaseAIProvider


class AIService():

    def __init__(self,provider: BaseAIProvider):
        self.provider = provider


    async def generate(self,prompt: str) -> str:
        resultado = await self.provider.generate(prompt)
        return resultado