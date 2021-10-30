import sys

from src.controller.music_terminal_controller import MusicTerminalController
from src.exception.music_exception import InputParameterError, CrawlerFailedError


def main():
    tmp_argv = sys.argv
    tmp_argv.pop(0)

    song_input = None
    song_type = None

    music_source = ['netease', 'kugou', ]

    # 对命令行参数进行读取，判断合法性
    for single in tmp_argv:
        if single[0] == ':':
            if single[1:] in music_source:
                song_type = single[1:]
        else:
            song_input = single

    # 捕获各种可能出现的异常，并做相应处理
    try:
        MusicTerminalController(song_input=song_input, song_type=song_type)
    except CrawlerFailedError:
        try:
            MusicTerminalController(song_input=song_input, song_type=song_type)
        except CrawlerFailedError:
            print('似乎出了点问题，请重新点歌吧')
            song_input = None
            MusicTerminalController(song_input=song_input, song_type=song_type)
        except InputParameterError:
            print('似乎出了点问题，请重新点歌吧')
            song_input = None
            MusicTerminalController(song_input=song_input, song_type=song_type)
        except KeyboardInterrupt:
            print('您关闭了上一首歌，请重新点首歌吧')
            song_input = None
            MusicTerminalController(song_input=song_input, song_type=song_type)
    except InputParameterError:
        print('似乎出了点问题，请重新点歌吧')
        song_input = None
        MusicTerminalController(song_input=song_input, song_type=song_type)
    except KeyboardInterrupt:
        print('您关闭了上一首歌，请重新点首歌吧')
        song_input = None
        MusicTerminalController(song_input=song_input, song_type=song_type)


if __name__ == '__main__':
    main()
