"""和爬虫进行交互。

给爬虫提供数据，并得到爬虫数据
对数据进行进一步封装

"""

from src.crawler.music_crawler import MusicBaseDataCrawler, MusicFileCrawler
from src.exception.music_exception import CrawlerFailedError, InputParameterError
from docs.conf import MUSIC_URL_QUICK, MUSIC_URL_BACKUP


class MusicBaseDataModel(object):
    """这里封装了对爬虫数据的操作，根据输入提供爬虫数据

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

    def __init__(self,
                 song_input=None,
                 song_url=MUSIC_URL_QUICK,
                 song_filter='name',
                 song_type='netease',
                 song_page='1'):
        """ 初始化

        :param song_url:
        :param song_input:
        :param song_filter:
        :param song_type:
        :param song_page:
        """

        if not (self.__is_qualified(song_url) and self.__is_qualified(song_input) and
                self.__is_qualified(song_filter) and self.__is_qualified(song_type) and
                self.__is_qualified(song_page)):
            raise InputParameterError()

        self.music_base_data_crawler = MusicBaseDataCrawler(song_url=song_url,
                                                            song_input=song_input,
                                                            song_filter=song_filter,
                                                            song_type=song_type,
                                                            song_page=song_page)
        try:
            self.music_base_data_crawler.crawler()
        except CrawlerFailedError as crawler_failed_error:
            raise crawler_failed_error

    def get_data(self) -> dict:
        """返回所有的音乐数据 music_data """
        return self.music_base_data_crawler.get_data()

    def get_value_by_id(self, song_id=None) -> dict:
        """通过 dict 的 key 获取值"""
        if not self.__is_qualified(song_id):
            raise InputParameterError()
        return self.get_data().get(song_id)

    def get_value_by_name(self, song_id=None, name=None) -> str:
        """通过 song_id 和 name 获取一个精确的值"""
        if not (self.__is_qualified(song_id) and self.__is_qualified(name)):
            raise InputParameterError()
        return self.get_value_by_id(song_id).get(name)


class MusicFileModel(object):
    """

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
        """

        :param down_url:
        """
        if not self.__is_qualified(down_url):
            raise InputParameterError()
        self.music_file_crawler = MusicFileCrawler(down_url=down_url)

        try:
            self.music_file_crawler.crawler()
        except CrawlerFailedError as crawler_failed_error:
            raise crawler_failed_error

    def get_music_file(self) -> bytes:
        return self.music_file_crawler.get_music_file()
