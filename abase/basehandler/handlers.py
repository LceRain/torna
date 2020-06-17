
import tornado.web

from abase.basehandler.handlertools import localhandlers
from tornas import settings
template_path=settings.TEMPLATES_PATH,
static_path=settings.STATIC_PATH


class Applications(tornado.web.Application):

    def __init__(self):
        handlers = localhandlers()
        settings = dict(
            template_path=template_path,
            static_path=static_path
        )

        tornado.web.Application.__init__(self, handlers, **settings)




