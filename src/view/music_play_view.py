"""这是 view， 从用户获取输入交付给 controller , 并展现数据给用户

视图有三种
1. 从用户接收输入，这个可以用命令行参数代替，显得更优雅一些
2. 展现选择给用户，提供必要的信息，让用户选择播放哪首歌
3. 当用户提供选择之后，展现歌词和播放歌曲

"""

import time
from io import BytesIO

import pygame
from pydub import AudioSegment

from src.exception.music_exception import InputParameterError
from src.view.lyric_split import LyricSplit
from utils.tools import color_output


class MusicPlayView(object):
    """
    view 之一, 命令行版
    """

    def __init__(self):
        self.song_input = None
        self.music_data = None
        self.song_select = None
        self.music = None

    def user_input(self) -> str:
        song_input = input(color_output('\t\t\t\t**--------------------->点首歌吧: ', is_return=True))
        self.song_input = song_input
        return song_input

    def show_select(self, music_data=None):
        """用户选择视图

        把拿到的音乐数据展现给用户，用户选择播放哪一个

        """
        if music_data is None:
            raise InputParameterError()
        self.music_data = music_data
        music_id_list = list(self.music_data.keys())

        # 使用 for 循环 展现数据给用户

        color = 1
        count = 0
        layout_head = '\t\t\t\t**--------------------------------------------------------------------------------------------------------**'
        color_output('\t\t\t\t\t\t\t\t\t\t音乐列表')
        color_output(layout_head, text_color=2)
        color_output(layout_head, text_color=3)
        color_output('\t\t\t\t**--------------------->\t歌手\t\t\t歌名')
        for single in music_id_list:
            if color > 6:
                color = 1
            tmp_data = self.music_data.get(single)
            color_output(
                f'\t\t\t\t{count + 1}.--------------------->\t{tmp_data.get("author")}\t\t\t{tmp_data.get("title")}',
                text_color=color)
            color += 1
            count += 1

        #
        flag = True
        while flag:
            select = input('\t\t\t\t请选择你喜欢的作者：')
            if select == "":
                color_output('\t\t\t\t输入有误，请重新输入：')
            try:
                select = int(select)
            except ValueError:
                color_output('\t\t\t\t输入有误，请重新输入：')
            self.song_select = self.music_data.get(music_id_list[int(select) - 1])
            flag = False

    def show_lyric(self, lyric):
        """
        拿到歌词，按照时间打印出来
        :param lyric: 歌词
        :return:
        """
        lrc = LyricSplit(lyric=lyric)
        time_list = lrc.get_time_list()
        color = 1
        layout_head = '\t\t\t\t**--------------------------------------------------------------------------------------------------------**'
        print('\n\n')

        color_output(f'\t\t\t\t\t\t\t\t\t\tmusic: {self.song_select.get("title")}', text_color=2)
        color_output(layout_head, text_color=1)
        color_output(layout_head, text_color=2)
        for i in range(len(time_list)):
            if i > 0:
                time.sleep(time_list[i] - time_list[i - 1])
                color_output(f'\t\t\t\t---------------->\t\t\t\t{lrc.get_lyric_dict().get(time_list[i])}',
                             text_color=color)
                color_output('\t\t\t\t---------------->')
                color += 1
                if color > 6:
                    color = 1
            else:
                time.sleep(time_list[i])
                color_output(f'\t\t\t\t---------------->\t\t\t\t{lrc.get_lyric_dict().get(time_list[i])}',
                             text_color=color)
                color_output('\t\t\t\t---------------->')

    def music_play(self, music_file=None):
        if music_file is None:
            raise InputParameterError()

        print(f'\t\t\t\t正在为您初始化歌曲 {self.song_select.get("title")}，请稍等。。。')

        music_mp3 = BytesIO(music_file)
        pygame.mixer.init()

        # music_ogg = AudioSegment.from_mp3(music_mp3).export(format='ogg')

        try:
            # 在 windows 平台上似乎是好的
            self.music = pygame.mixer.Sound(music_mp3)
        except pygame.error:
            # 在 linux 平台上必须转码才能播放
            music_ogg = AudioSegment.from_mp3(music_mp3).export(format='ogg')
            self.music = pygame.mixer.Sound(music_ogg)

        self.music.play()

    # 返回的是一个字典，字典数据中携带者基础数据
    def get_user_select(self) -> dict:
        return self.song_select

    # 停止当前音乐播放
    def music_stop(self):
        if self.music is not None:
            self.music.stop()
