import os
from dotenv import load_dotenv

# Carrega as variáveis do arquivo .env (como a chave da API)
load_dotenv()

from google import genai
from backend.app.ai.providers.base import BaseAIProvider


# Classe que conecta o sistema à API real do Gemini
class GeminiAIProvider(BaseAIProvider):

    # Prepara a conexão assim que a classe é criada
    def __init__(self):
        # Pega a chave da API salva nas variáveis de ambiente
        api_key = os.getenv("GEMINI_API_KEY")

        # Para tudo e avisa se a chave não existir
        if not api_key:
            raise ValueError("GEMINI_API_KEY não configurada.")

        # Cria o cliente oficial do Google usando a chave
        self.client = genai.Client(api_key=api_key)
        # Define qual versão do modelo será usada
        self.model = "gemini-3.8-flash"

    # Envia o prompt para o Gemini de forma assíncrona e devolve o texto
    async def generate(self, prompt: str) -> str:
        # Faz a chamada na API do Google (aio = versão assíncrona)
        response = await self.client.aio.models.generate_content(
            model=self.model,
            contents=prompt
        )

        # Garante que a IA não devolveu uma resposta em branco
        if not response.text:
            raise ValueError("O Gemini retornou uma resposta vazia.")

        # Retorna apenas o texto gerado pela IA
        return response.text