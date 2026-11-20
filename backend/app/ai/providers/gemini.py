
import os
from dotenv import load_dotenv

load_dotenv()

from google import genai

from backend.app.ai.providers.base import BaseAIProvider


class GeminiAIProvider(BaseAIProvider):

    def __init__(self):
        api_key = os.getenv("GEMINI_API_KEY")

        if not api_key:
            raise ValueError("GEMINI_API_KEY não configurada.")

        self.client = genai.Client(api_key=api_key)
        self.model = "gemini-3.8-flash"

    async def generate(self, prompt: str) -> str:
        response = await self.client.aio.models.generate_content(
            model=self.model,
            contents=prompt
        )

        if not response.text:
            raise ValueError("O Gemini retornou uma resposta vazia.")

        return response.text
