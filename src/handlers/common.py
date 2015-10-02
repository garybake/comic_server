#!/usr/bin/env python2

import os
from Comics import *
import shutil
import itertools

image_list = []
current_image = 0

comics = Comic_Library()
comic_static_folder = os.path.dirname(os.path.realpath(__file__)) + '/../static/comic'
comic_archive_folder = os.path.dirname(os.path.realpath(__file__)) + '/../../comics'


def get_comics():
    comics.clear()
    for directory in os.listdir(comic_static_folder):
        print 'Found comic ' + directory
        comics.add_comic(id=directory, folder=comic_static_folder + '/' + directory)


def flatten_folder(destination):
    all_files = []
    for root, _dirs, files in itertools.islice(os.walk(destination), 1, None):
        for filename in files:
            all_files.append(os.path.join(root, filename))
    for filename in all_files:
        # TODO: handle matching filenames
        shutil.move(filename, destination)
