# _*_ coding: utf8 _*_
import os
import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web
from tornado.options import define, options

from abase.basehandler.handlers import Applications


def runserver(host, port):
    define("port", default=port, help="run on the given port", type=int)
    define("host", default=host, help="run on the given host", type=int)
    tornado.options.parse_command_line()
    app = Applications()

    http_server = tornado.httpserver.HTTPServer(app)

    http_server.listen(options.port)
    print(f'run {options.host}:{options.port}')
    tornado.ioloop.IOLoop.current().start()
