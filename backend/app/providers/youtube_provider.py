import requests  # Biblioteca para fazer requisições HTTP na internet


class YouTubeProvider:

    # Inicializa a classe guardando a chave da API do YouTube
    def __init__(self, youtube_api_key):
        self.api_key = youtube_api_key

    def busca_musica(self, musica: str, cantor: str | None = None):
        # Monta o texto da pesquisa (inclui o cantor se ele for informado)
        if not(cantor):
            pesquisar = f"{musica}"
        else:
            pesquisar = f'{musica} de {cantor}'

        # Parâmetros enviados na URL para a API do YouTube
        params = {
            "key": self.api_key,
            "q": pesquisar,
            "type": "video"
        }

        # Faz a busca na API do YouTube e converte a resposta para JSON (dicionário)
        musica_id = requests.get('https://www.googleapis.com/youtube/v3/search', params=params,timeout=5).json()

        # Pega o ID do primeiro vídeo que apareceu nos resultados
        musica_id = musica_id["items"][0]["id"]["videoId"]

        # Retorna o ID encontrado
        return {
            "video_id": musica_id
        }