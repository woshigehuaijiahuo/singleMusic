"""对歌词进行分割

"""
import re

from exception.music_exception import InputParameterError


def lyric_filter(lyric=None) -> bool:
    if lyric is None:
        return True
    if re.search('id|ar|ti|by|hash|al|sign|qq|total|offset', lyric) is not None:
        return False
    return True


class LyricSplit(object):
    """接收一个音乐歌词格式字符串，将其分割成时间与歌词的字典

    """

    @staticmethod
    def __is_qualified(value=None) -> bool:
        """函数实现对输入数据的合法性判断

        数据校验

        :param value: 传入值
        :return: 返回 bool
        """

        if value is None:
            return False
        if not isinstance(value, str):
            return False
        if value == '':
            return False
        return True

    def __init__(self, lyric=None):
        if not self.__is_qualified(lyric):
            raise InputParameterError()

        self.__lyric = lyric

    def get_time_list(self) -> list:
        lyric_time_list = self.get_lyric_dict().keys()
        return list(lyric_time_list)

    def get_lyric_dict(self) -> dict:
        lyric_dict = {}
        lyric_list = self.__lyric.splitlines()
        for lyric_single in lyric_list:
            if not lyric_filter(lyric_single):
                continue
            lyric_split = lyric_single.split(']')
            lyric_left = lyric_split[0].strip()[1:].split(':')
            if lyric_left[0] == '':
                continue

            key = float(lyric_left[0]) * 60 + float(lyric_left[1])
            value = lyric_split[1].strip()
            lyric_dict[key] = value

        return lyric_dict
