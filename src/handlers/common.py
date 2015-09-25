#!/usr/bin/env python2

import os
from Comics import *

image_list = []
current_image = 0

comics = Comic_Library()
comic_static_folder = os.path.dirname(os.path.realpath(__file__)) + '/../static/comic'
comic_archive_folder = os.path.dirname(os.path.realpath(__file__)) + '/../../comics'

def get_comics():
    for directory in os.listdir(comic_static_folder):
        print 'Found comic ' + directory
        comics.add_comic(id=directory, folder=comic_static_folder + '/' + directory)
