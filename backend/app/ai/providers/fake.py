import json
from backend.app.ai.providers.base import BaseAIProvider
import hashlib


# IA falsa usada para testes sem gastar créditos de API real
class FakeAIProvider(BaseAIProvider):

    # Recebe o texto do usuário e devolve uma resposta simulada
    async def generate(self, prompt: str) -> str:
        # Se o texto vier vazio, avisa o erro
        if not prompt:
            return "Please enter a valid prompt"

        # Transforma o dicionário Python em texto JSON válido
        reponse = json.dumps({
            "type": "conversation",
            "message": "Olá! Como posso ajudar?",
            "command": None
        })

        # Devolve a resposta pronta
        return reponse