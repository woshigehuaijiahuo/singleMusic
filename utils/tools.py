"""常用的工具函数"""


def color_output(data='', text_color=1, is_return=False):
    """打印出带颜色的文本"""
    if is_return:
        return f'\033[3{text_color}m{data}\033[0m'
    print(f'\033[3{text_color}m{data}\033[0m')
