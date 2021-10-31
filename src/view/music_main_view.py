"""主视图

展示功能给用户，提供模式选择
*** 1. 点歌模式
*** 2. 下载模式
*** 3. 音乐源选择

"""

from utils.tools import color_output
from docs.conf import Pattern, LAYOUT_HEAD


class MusicMainView(object):
    """主视图"""

    def __init__(self):
        """
        模式选择，默认为点歌模式
        """
        self.__pattern_select = Pattern.PLAY

    def show_pattern(self):
        color_output(LAYOUT_HEAD, text_color=1)
        color_output(LAYOUT_HEAD, text_color=4)
        color_output('\t\t\t\t**--------------------->1. 点歌模式', text_color=1)
        color_output('\t\t\t\t**--------------------->2. 下载模式', text_color=2)
        color_output('\t\t\t\t**--------------------->3. 音乐源选择', text_color=3)
        select = int(input('\t\t\t\t**--------------------->你的选择： '))

        self.__pattern_select = Pattern(select)

    def get_select(self):
        return self.__pattern_select
