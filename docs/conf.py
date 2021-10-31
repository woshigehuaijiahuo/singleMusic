"""这里是一些全局配置设置，为了便于修改"""

from enum import Enum

# 音乐数据接口 URL
# 快速的接口和备用的接口
MUSIC_URL_QUICK = 'http://music.9q4.cn'
MUSIC_URL_BACKUP = 'https://bukaivip.com/music/'

# 爬虫请求延时设置
TIME_OUT = 20


# 音乐源选择
class MusicSource(object):
    NETEASE = 'netease'
    KUGOU = 'kugou'
    MUSIC_SOURCE_LIST = ['netease', 'kugou', ]


# 视图模式枚举
class Pattern(Enum):
    PLAY = 1
    DOWNLOAD = 2
    SOURCE = 3


# 视图布局的固定样式
LAYOUT_HEAD = '\t\t\t\t**--------------------------------------------------------------------------------------------------------**'
