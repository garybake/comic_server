#!/usr/bin/env python2

import tornado.ioloop
import tornado.options
import tornado.web

import settings

from handlers.RootHandler import *
from handlers.ComicPageHandler import *
from handlers.AdminRefreshHandler import *
from handlers.AdminInfoHandler import *
from handlers.common import *

from tornado.options import define, options
define("port", default=9000, help="run on the given port", type=int)

class Application(tornado.web.Application):
    def __init__(self, settings):

        get_comics()

        handlers = [
            (r"/", RootHandler),
            (r"/comic_page", ComicPageHandler),
            (r"/admin/refresh", AdminRefreshHandler),
            (r"/admin/info", AdminInfoHandler)
        ]
        settings = {
            "template_path": settings.TEMPLATE_PATH,
            "static_path": settings.STATIC_PATH,
            "static_url": settings.STATIC_URL,
            "debug": settings.DEBUG,
            "gzip": settings.gzip
        }
        tornado.web.Application.__init__(self, handlers, **settings)


def main():
    tornado.options.parse_command_line()
    app = Application(settings)
    app.listen(options.port)
    print 'Now serving on port ' + str(options.port)
    tornado.ioloop.IOLoop.instance().start()

if __name__ == "__main__":
    main()
