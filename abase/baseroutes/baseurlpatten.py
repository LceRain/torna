# _*_ coding: utf8 _*_
import functools
import os
from importlib import import_module




def path(path, urls):
    '''
    处理各个app内的urlpatten
    :param path:
    :param urls:
    :return: 各个app的urlpattens的处理结果
    '''

    urls = __import__(urls, globals(), locals(), ['urls'])
    urlpatten = getattr(urls, 'urlpatten')

    appurlpatten = []
    for i in urlpatten:
        url = path + i[0]
        view = i[1]
        uu = (url, view)

        appurlpatten.append(uu)

    return appurlpatten














