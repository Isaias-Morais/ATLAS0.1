from backend.app.ai.providers.base import BaseAIProvider
from backend.app.ai.providers.parser import IAResponseParser


class AIService():

    def __init__(self,provider: BaseAIProvider,paser:IAResponseParser):
        self.provider = provider
        self.paser = paser


    async def generate(self,prompt: str):
        respostar_bruta = await self.provider.generate(prompt)
        intepretacao = self.paser.parse(respostar_bruta)
        return intepretacao