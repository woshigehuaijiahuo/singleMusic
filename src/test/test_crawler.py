import unittest
from src.crawler.music_crawler import MusicBaseDataCrawler, MusicFileCrawler


class TestMusicCrawler(unittest.TestCase):
    def test_music_basic_data_crawler(self):
        music_basic_data = MusicBaseDataCrawler(song_input='走天涯')
        music_basic_data.crawler()
        data = music_basic_data.get_data()
        print(data)

    def test_music_file_crawler(self):
        music_file = MusicFileCrawler(down_url='http://music.163.com/song/media/outer/url?id=128082.mp3')
        status_code = music_file.crawler()
        print(status_code)


if __name__ == '__main__':
    unittest.main()
