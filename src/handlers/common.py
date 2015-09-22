#!/usr/bin/env python2

import os
from Comics import *

image_list = []
current_image = 0

comics = Comic_Library()
comic_static_folder = './static/comic'

def get_comics():
    for directory in os.listdir(comic_static_folder):
        print directory
        comics.add_comic(id=directory, folder=comic_static_folder + '/' + directory)
