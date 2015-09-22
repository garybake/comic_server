#!/usr/bin/env python2

import os

DEBUG = True
DIRNAME = os.path.dirname(__file__)
STATIC_URL = '/static/(.*)'
STATIC_PATH = os.path.join(DIRNAME, 'static')
TEMPLATE_PATH = os.path.join(DIRNAME, 'templates')
gzip = True
