import json
from backend.app.ai.providers.base import BaseAIProvider

class FakeAIProvider(BaseAIProvider):

    async def generate(self, prompt: str) -> str:
        if not prompt:
            return "Please enter a valid prompt"
        reponse = json.dumps({
            "type":"conversation",
            "message":"Olá! Como posso ajudar?",
            'command': None
        })
        return reponse

