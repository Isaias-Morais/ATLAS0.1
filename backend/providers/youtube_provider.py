from backend.config.config import YOUTUBE_API_KEY


class YouTubeProvider:

    def __init__(self, youtube_api_key):
        self.api_key = youtube_api_key


    def busca_musica(self, musica:str, cantor:str|None=None):
        pass
