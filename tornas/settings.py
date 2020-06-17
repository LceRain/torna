import os



BASEDIR = os.path.join(os.path.dirname(__file__))

DATABASES = {
    'default': 'mysql+pymysql://root:12345678@localhost:3306/spark'
}


APPS = [
    'apps.index',
    'apps.index2'
]

TEMPLATES_PATH = os.path.join(os.path.dirname(__file__), "templates"),
STATIC_PATH = os.path.join(os.path.dirname(__file__), "static")

