"""负责将 model 和 view 结合起来

此控制器将结合 model 和 MusicTerminalView

"""

from src.model.music_model import MusicBaseDataModel, MusicFileModel
from src.view.music_play_view import MusicPlayView
from src.exception.music_exception import InputParameterError, CrawlerFailedError


class MusicPlayController(object):
    """终端控制器实现"""
    def __init__(self, song_input=None, song_type=None):
        self.music_terminal_view = MusicPlayView()

        if song_input is None:
            self.song_input = self.music_terminal_view.user_input()
        else:
            self.song_input = song_input

        if song_type is None:
            self.song_type = 'netease'
        else:
            self.song_type = song_type

        # 初始化音乐基础数据模型，并捕获异常，继续上层抛出
        try:
            self.music_base_data_model = MusicBaseDataModel(song_input=self.song_input, song_type=self.song_type)
        except CrawlerFailedError as crawler_failed_error:
            raise crawler_failed_error
        except InputParameterError as input_parameter_error:
            raise input_parameter_error

        # 得到音乐基础数据, 使用音乐基础数据展示音乐选择视图
        music_basic_data = self.music_base_data_model.get_data()
        self.music_terminal_view.show_select(music_basic_data)

        # 初始化音乐文件模型，输入音乐下载链接，模型调用爬虫将MP3文件保存在缓存中, 捕获并处理响应异常
        try:
            self.music_file_model = MusicFileModel(self.music_terminal_view.get_user_select().get("url"))
        except CrawlerFailedError as crawler_failed_error:
            raise crawler_failed_error
        except InputParameterError as input_parameter_error:
            raise input_parameter_error

        # 异步播放音乐并打印歌词，捕获并处理对应异常
        try:
            try:
                self.music_terminal_view.music_play(self.music_file_model.get_music_file())
            except InputParameterError as input_parameter_error:
                raise input_parameter_error
            try:
                self.music_terminal_view.show_lyric(self.music_terminal_view.get_user_select().get('lrc'))
            except InputParameterError:
                self.music_terminal_view.music_stop()
                self.music_terminal_view.music_play(self.music_file_model.get_music_file())
        except KeyboardInterrupt as keyboard_interrupt:
            self.music_terminal_view.music_stop()
            raise keyboard_interrupt

    def music_stop(self):
        if self.music_terminal_view is not None:
            self.music_terminal_view.music_stop()
