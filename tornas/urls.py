from abase.baseroutes.baseurlpatten import path

urlpattens = [
    path('/index', 'apps.index.urls'),
    path('/index2', 'apps.index2.urls')

]

if __name__ == '__main__':
    print(urlpattens)
