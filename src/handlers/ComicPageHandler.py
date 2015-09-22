#!/usr/bin/env python2

import os

import tornado.web
import tornado.gen

from common import *


class ComicPageHandler(tornado.web.RequestHandler):

    def get(self):
        comic_name = self.get_argument('comic_name', 'unknown')
        pg = self.get_argument('page', 0)
        pg_index = int(pg)
        comic = comics.get_comic(comic_name)

        if pg_index >= len(comic.images):
            pg_index = len(comic.images) - 1

        if pg_index <= 0:
            pg_index = 0

        filename = comic.images[pg_index]

        pic_file = tornado.escape.url_escape(filename, plus=False)
        self.render('comic_page.html', title=filename, pic_file=pic_file, comic_name=comic_name, back=pg_index-1, forward=pg_index+1)
