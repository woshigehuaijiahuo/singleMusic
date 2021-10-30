"""主控制器

根据主视图的选择调用不同的其他的控制器
"""
import re

from src.controller.music_terminal_controller import MusicTerminalController
from src.exception.music_exception import CrawlerFailedError, InputParameterError
from src.view.music_main_view import MusicMainView
from docs.conf import Pattern
from docs.conf import MusicSource
from utils.tools import color_output


def is_exit(output=''):
    """使用正则对输入数据的合法性判断"""
    flag = re.compile(r'^[Y|y][e|E]?[S|s]?$')
    is_play = input(
        color_output(output, text_color=2, is_return=True))
    is_play = flag.match(is_play)
    if not is_play:
        return True
    else:
        return False


class MusicMainController(object):
    """主控制器"""

    def __init__(self):
        """数据初始化"""
        self.song_type = MusicSource.NETEASE
        self.song_input = None

        self.music_main_view = MusicMainView()
        self.music_main_view.show_pattern()
        self.pattern_select = self.music_main_view.get_select()

    def match_view(self):
        """根据 主视图的值选择不同的视图 """
        # 选择点歌模式
        if self.pattern_select == Pattern.PLAY:
            # 捕获各种可能出现的异常，并做相应处理
            while True:

                try:
                    MusicTerminalController(song_input=self.song_input, song_type=self.song_type)
                # 捕获爬虫失败异常
                except CrawlerFailedError:
                    if not is_exit('\t\t\t\t**--------------------->似乎出了点问题，重新点歌? y|n: '):
                        self.song_input = None
                        MusicTerminalController(song_input=self.song_input, song_type=self.song_type)
                    else:
                        exit()
                # 捕获输入参数异常
                except InputParameterError:
                    if not is_exit('\t\t\t\t**--------------------->似乎出了点问题，重新点歌? y|n: '):
                        self.song_input = None
                        MusicTerminalController(song_input=self.song_input, song_type=self.song_type)
                    else:
                        exit()
                # 捕获键中断异常
                except KeyboardInterrupt:
                    if not is_exit('\t\t\t\t**--------------------->您关闭了一首歌，重新点歌? y|n: '):
                        self.song_input = None
                        MusicTerminalController(song_input=self.song_input, song_type=self.song_type)
                    else:
                        exit()

        # 选择下载模式
        if self.pattern_select == Pattern.DOWNLOAD:
            print('此功能暂未开放')

        # 选择音乐源模式
        if self.pattern_select == Pattern.SOURCE:
            print('此功能暂未开放')
