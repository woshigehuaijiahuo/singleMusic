"""音乐下载视图

这个视图给用户提供下载位置选择，默认下载到当前位置

"""


class MusicDownloadView(object):
    def __init__(self):
        self.save_path = './'

