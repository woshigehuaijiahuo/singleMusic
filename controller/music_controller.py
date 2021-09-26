"""负责将 model 和 view 结合起来

此控制器将 model 和 命令行版 view 结合起来

"""

from model.music_model import MusicBaseDataModel, MusicFileModel
from view.music_terminal_view import MusicTerminalView
from exception.music_exception import InputParameterError, CrawlerFailedError


class MusicTerminalController(object):
    def __init__(self, song_input=None, song_type=None):
        self.music_terminal_view = MusicTerminalView()

        if song_input is None:
            self.song_input = self.music_terminal_view.user_input()
        else:
            self.song_input = song_input

        if song_type is None:
            self.song_type = 'netease'
        else:
            self.song_type = song_type

        # 捕获异常，继续上层抛出
        try:
            self.music_base_data_model = MusicBaseDataModel(song_input=self.song_input, song_type=self.song_type)
        except CrawlerFailedError as crawler_failed_error:
            raise crawler_failed_error

        music_basic_data = self.music_base_data_model.get_data()

        self.music_terminal_view.show_select(music_basic_data)

        self.music_file_model = MusicFileModel(self.music_terminal_view.get_user_select().get("url"))

        self.music_terminal_view.music_play(self.music_file_model.get_music_file())
        try:
            self.music_terminal_view.show_lyric(self.music_terminal_view.get_user_select().get('lrc'))
        except InputParameterError:
            self.music_terminal_view.music_play(self.music_file_model.get_music_file())
