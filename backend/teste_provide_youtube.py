import pprint

from backend.app.providers.youtube_provider import YouTubeProvider
from backend.app.config.config import YOUTUBE_API_KEY

youtubeprovider = YouTubeProvider(YOUTUBE_API_KEY)

# print(youtubeprovider.api_key)

print(youtubeprovider.busca_musica('poesia acustica 2','pineple'))