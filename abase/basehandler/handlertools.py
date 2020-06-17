
from tornas import urls
def localhandlers():
    '''
    初始化路由和views
    :return: 路由和view的映射列表
    '''
    urlpattens = urls.urlpattens
    handlers = []
    for urlpatten in urlpattens:
        handlers.extend(urlpatten)

    return handlers


if __name__ == '__main__':
    handlers = localhandlers()
    print(handlers)