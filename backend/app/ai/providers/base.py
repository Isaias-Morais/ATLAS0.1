from abc import ABC, abstractmethod


# Classe molde que obriga toda IA a seguir o mesmo padrão
class BaseAIProvider(ABC):

    # Obriga quem herdar dessa classe a criar a função "generate"
    @abstractmethod
    async def generate(self, prompt: str) -> str:
        pass