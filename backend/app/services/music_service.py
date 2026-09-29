from backend.app.config.config import YOUTUBE_API_KEY
from backend.app.providers.youtube_provider import YouTubeProvider

def tocar_musica_service(musica:str,cantor:str|None=None):

    busca = YouTubeProvider(YOUTUBE_API_KEY)

    if not busca.api_key:
        raise Exception("API key not provided")

    musica_id = busca.busca_musica(musica,cantor)

    return musica_id