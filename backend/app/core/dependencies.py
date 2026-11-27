from backend.app.config.config import YOUTUBE_API_KEY
from backend.app.providers.youtube_provider import YouTubeProvider

from backend.app.services.music_service import MusicService

def get_music_service():
    provider = YouTubeProvider(YOUTUBE_API_KEY)

    music = MusicService(provider)

    return music