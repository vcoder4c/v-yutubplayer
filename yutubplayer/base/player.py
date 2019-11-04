import pafy
import vlc

from .exceptions import NotExistVideo
from .youtube_client import search_video


class Video:
    def __init__(self, video_id, title) -> None:
        self.video_id = video_id
        self.title = title

    def __str__(self) -> str:
        return self.title


class YutubPlayer:
    def __init__(self) -> None:
        self.videos = []
        self.vlc = vlc.Instance()
        self.player = self.vlc.media_player_new()

    def search(self, query):
        search_results = search_video(query)
        for result in search_results:
            self.videos.append(Video(video_id=result['id'], title=result['title']))

    def list(self):
        for idx, video in enumerate(self.videos):
            print(f'Video {idx}: {video}')

    def _get(self, idx):
        try:
            return self.videos[idx]
        except IndexError:
            raise NotExistVideo()

    @classmethod
    def _playable_url(cls, video_id):
        video = pafy.new(f'https://www.youtube.com/watch?v={video_id}')
        best = video.getbestaudio()
        return best.url

    def play(self, idx):
        video = self._get(idx)
        print(f'Playing {video.title}')
        play_url = self._playable_url(video.video_id)
        if self.player.is_playing():
            self.player.stop()
        media = self.vlc.media_new(play_url)
        media.get_mrl()
        self.player.set_media(media)
        self.player.play()

    def pause(self):
        self.player.pause()

    def resume(self):
        self.player.play()

    def clear(self):
        self.videos = []
