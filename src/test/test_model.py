import unittest
from src.model.music_model import MusicBaseDataModel, MusicFileModel


class TestMusicModel(unittest.TestCase):
    def test_music_basic_data_model(self):
        music_basic_data = MusicBaseDataModel(song_input='走天涯')
        data = music_basic_data.get_data()
        print(data)

    def test_music_file_model(self):
        music_file = MusicFileModel('http://music.163.com/song/media/outer/url?id=128082.mp3')
        file = music_file.get_music_file()
        with open('./music.mp3', 'wb') as f:
            f.write(file)


if __name__ == '__main__':
    unittest.main()
