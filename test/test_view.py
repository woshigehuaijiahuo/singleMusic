import unittest

from model.music_model import MusicBaseDataModel, MusicFileModel
from view.music_terminal_view import MusicTerminalView


class TestMusicView(unittest.TestCase):
    def test_music_terminal_view(self):
        terminal_view = MusicTerminalView()
        song_input = terminal_view.user_input()
        base_data_model = MusicBaseDataModel(song_input=song_input)
        base_data = base_data_model.get_data()
        terminal_view.show_select(base_data)
        music_file_model = MusicFileModel(terminal_view.get_user_select().get('url'))
        terminal_view.music_play(music_file=music_file_model.get_music_file())
        terminal_view.show_lyric(terminal_view.get_user_select().get('lrc'))


if __name__ == '__main__':
    unittest.main()
