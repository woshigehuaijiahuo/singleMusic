import re
import sys

from src.controller.music_terminal_controller import MusicTerminalController
from src.exception.music_exception import InputParameterError, CrawlerFailedError
from utils.tools import color_output
from docs.conf import MusicSource


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


def main():
    # 从命令行读取参数，保存在缓存中
    tmp_argv = sys.argv
    tmp_argv.pop(0)

    song_input = None
    song_type = None

    # 对命令行参数进行读取，判断合法性
    for single in tmp_argv:
        if single[0] == ':':
            if single[1:] in MusicSource.MUSIC_SOURCE_LIST:
                song_type = single[1:]
        else:
            song_input = single

    # 捕获各种可能出现的异常，并做相应处理
    while True:

        try:
            MusicTerminalController(song_input=song_input, song_type=song_type)
        # 捕获爬虫失败异常
        except CrawlerFailedError:
            if not is_exit('\t\t\t\t**--------------------->似乎出了点问题，退出或重新点歌 y|n: '):
                song_input = None
                MusicTerminalController(song_input=song_input, song_type=song_type)
            else:
                exit()
        # 捕获输入参数异常
        except InputParameterError:
            if not is_exit('\t\t\t\t**--------------------->似乎出了点问题，退出或重新点歌 y|n: '):
                song_input = None
                MusicTerminalController(song_input=song_input, song_type=song_type)
            else:
                exit()
        # 捕获键中断异常
        except KeyboardInterrupt:
            if not is_exit('\t\t\t\t**--------------------->您关闭了一首歌，退出或重新点歌 y|n: '):
                song_input = None
                MusicTerminalController(song_input=song_input, song_type=song_type)
            else:
                exit()
