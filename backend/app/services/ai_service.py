from backend.app.ai.prompt_builder import PromptBuilder
from backend.app.ai.providers.base import BaseAIProvider
from backend.app.ai.providers.parser import IAResponseParser


class AIService:
    """Orquestra a geração de resposta da IA e o tratamento do retorno."""

    def __init__(self, provider: BaseAIProvider, paser: IAResponseParser,prompt_builder:PromptBuilder):
        # Define o provedor de IA (ex: Gemini, OpenAI) e o formatador de resposta
        self.provider = provider
        self.paser = paser
        self.prompt_builder = prompt_builder

    async def generate(self, prompt: str):
        # Envia o prompt para a IA e aguarda a resposta em texto puro
        respostar_bruta = await self.provider.generate(prompt)

        # Converte/interpreta a resposta bruta para o formato esperado pelo sistema
        intepretacao = self.paser.parse(respostar_bruta)

        return intepretacao