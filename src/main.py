import sys

from src.controller.music_controller import MusicTerminalController

if __name__ == '__main__':

    tmp_argv = sys.argv
    tmp_argv.pop(0)

    song_input = None
    song_type = None

    music_source = ['netease', 'kugou', 'kuwo', 'xiami', 'migu', 'qq']

    for single in tmp_argv:
        if single[0] == ':':
            if single[1:] in music_source:
                song_type = single[1:]
        else:
            song_input = single

    m = MusicTerminalController(song_input=song_input, song_type=song_type)

    # terminal_view = MusicTerminalView()
    # song_input = terminal_view.user_input()
    # base_data_model = MusicBaseDataModel(song_input=song_input)
    # base_data = base_data_model.get_data()
    # terminal_view.show_select(base_data)
    # music_file_model = MusicFileModel(terminal_view.get_user_select().get('url'))
    # terminal_view.music_play(music_file=music_file_model.get_music_file())
    # terminal_view.show_lyric(terminal_view.get_user_select().get('lrc'))
