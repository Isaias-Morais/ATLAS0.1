class AIRouter:
    """Gerencia e seleciona provedores de IA registrados."""

    def __init__(self, providers: dict):
        # Armazena o dicionário de provedores disponíveis (ex: {"gemini": instancia})
        self.providers = providers

    def select_provider(self, provider_name: str):
        """Busca e retorna o provedor pelo nome, ou None se não existir."""
        # Tenta obter a instância do provedor sem gerar KeyError caso não exista
        provider = self.providers.get(provider_name)

        if provider is None:
            return None

        print(provider)  # Log de depuração do provedor selecionado
        return provider