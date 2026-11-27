from backend.app.config.config import YOUTUBE_API_KEY
from backend.app.providers.youtube_provider import YouTubeProvider
from backend.app.schemas.command_scherma import MusicCommandData


class MusicService:
    def __init__(self,provider):
        self.provider=provider


    def tocar_musica_service(self,musica:str,cantor:str):

       return self.busca_musica(musica=musica,cantor=cantor)



    def busca_musica(self,musica,cantor):

        musica_id = self.provider.busca_musica(musica, cantor)

        if not musica_id:
            raise ValueError("Nenhuma música encontrada.")

        return musica_id


