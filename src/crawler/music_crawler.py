"""这个模块是爬虫模块，用以提供数据

相当于 MVC 模式中的数据库，不过这个数据库是源自于爬虫，数据来自于互联网
这里将定义两个类：
一个类实现 music 基础数据的爬取， 一个类实现 music MP3 文件的下载

"""
import json.decoder

import httpx
from src.exception.music_exception import CrawlerFailedError, InputParameterError


class MusicBaseDataCrawler(object):
    """这个类实现对音乐基础数据的爬取

    通过输入数据爬取基本数据，将数据封装成 list
    获取数据可以通过 generator 函数 get_next() 获取

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

    def __init__(
            self,
            song_input=None,
            song_url='http://music.9q4.cn',
            # song_url='https://bukaivip.com/music/',
            song_filter='name',
            song_type='netease',
            song_page='1'
    ):
        """初始化类成员变量

        :param song_url: 从哪个网站爬取音乐
        :param song_input: 歌曲的名字
        :param song_filter: 过滤器， 默认为 name
        :param song_type: 歌曲来源， 默认为 netease
        :param song_page: 第几页， 默认为 1

        """

        if not (self.__is_qualified(song_url) and self.__is_qualified(song_input) and
                self.__is_qualified(song_filter) and self.__is_qualified(song_type) and
                self.__is_qualified(song_page)):
            raise InputParameterError()

        self.__url = song_url

        self.__form_data = {
            'input': song_input,
            'filter': song_filter,
            'type': song_type,
            'page': song_page,
        }

        self.__headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36',
            'X-Requested-With': 'XMLHttpRequest'
        }

        self.__data = {}

    def crawler(self) -> int:
        """开始爬虫

        :return:
        """
        try:
            response = httpx.post(url=self.__url, data=self.__form_data, headers=self.__headers, timeout=100)
        except httpx.ConnectError:
            raise CrawlerFailedError(self.__class__.__name__)
        except httpx.HTTPError:
            raise CrawlerFailedError(self.__class__.__name__)

        try:
            json_data = response.json()
        except json.decoder.JSONDecodeError:
            try:
                json_data = json.loads(response.content)
            except json.decoder.JSONDecodeError as json_error:
                raise json_error

        for single in json_data['data']:
            self.__data[str(dict(single)['songid'])] = dict(single)

        return response.status_code

    def get_data(self) -> dict:
        """
        返回整个数据字典
        :return: 返回一个 dict
        """

        return self.__data

    def get_value_by_id(self, song_id=None) -> dict:
        """通过 dict 的 key 获取值"""
        if not self.__is_qualified(song_id):
            raise InputParameterError()
        return self.__data.get(key=song_id, default="No Value!")


class MusicFileCrawler(object):
    """这个爬虫是为了下载音乐文件为了在本地播放

    这个类实现音乐文件的下载

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

    def __init__(self, down_url=None):
        """初始化成员变量

        :param down_url: 音乐文件 url
        """
        if not self.__is_qualified(down_url):
            raise InputParameterError()

        self.__down_url = down_url
        self.__music_file = None

    def crawler(self) -> int:
        try:
            response = httpx.get(url=self.__down_url, timeout=10)
        except httpx.ConnectError:
            raise CrawlerFailedError(self.__class__.__name__)
        except httpx.HTTPError:
            raise CrawlerFailedError(self.__class__.__name__)

        else:
            self.__music_file = response.content
            return response.status_code

    def get_music_file(self) -> bytes:
        return self.__music_file
