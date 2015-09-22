#!/usr/bin/env python
# -*- coding: utf-8 -*-

import tornado.web
import tornado.gen

from common import *

class RootHandler(tornado.web.RequestHandler):
    def get(self):
        self.render('index.html', comics=comics)
