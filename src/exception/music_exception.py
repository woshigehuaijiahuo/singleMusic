"""异常处理模块

底层的相关代码在可能出现异常的地方抛出异常， 然后在最顶层做出捕获进行处理
这里 view 和 model 以及 crawler 抛出异常， 在 controller 或者 主函数中捕获异常

"""


class CrawlerFailedError(Exception):
    """爬虫爬取过程异常

    """
    def __init__(self, value=None):
        self.value = value

    def __str__(self):
        if self.value is not None:
            return f'{self.value} Crawler failed!'
        return 'Crawler failed!'


class InputParameterError(Exception):
    """输入参数异常

    """
    def __init__(self, value=None):
        self.value = value

    def __str__(self):
        if self.value is not None:
            return self.value
        return 'Incorrect input parameters!'
