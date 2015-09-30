#!/usr/bin/env python2

# import os
# import shutil
# import zipfile
# import re

import tornado.web
import tornado.gen

from common import *


class AdminInfoHandler(tornado.web.RequestHandler):

    def get(self):
        for comic in comics:
            self.write(comic.id)
