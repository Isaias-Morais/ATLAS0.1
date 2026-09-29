import requests


class YouTubeProvider:

    def __init__(self, youtube_api_key):
        self.api_key = youtube_api_key


    def busca_musica(self, musica:str, cantor:str|None=None):

        if not(cantor):
            pesquisar = f"{musica}"
        else:
            pesquisar = f'{musica} de {cantor}'

        params = {
            "key": self.api_key,
            "q": pesquisar,
            "type": "video"
        }

        musica_id = requests.get('https://www.googleapis.com/youtube/v3/search',params=params)

        musica_id = musica_id.json()

        musica_id = musica_id["items"][0]["id"]["videoId"]

        return {
            "video_id":musica_id
        }

