#!/usr/bin/env python2

import os

class Comic_Library(list):

    def add_comic(self, id, folder):
        comic = Comic(id=id, folder=folder)
        comic.import_data()
        self.append(comic)

    def get_comic(self, id):
        for comic in self:
            if comic.id == id:
                return comic
        return None


class Comic:

    def __init__(self, id, folder):
        self.id = id
        self.folder = folder
        self.images = []
        self.folder_image = '/static/comic/' + self.id + '/folder.jpg'

    def import_data(self):
        image_list = []
        for file in os.listdir(self.folder):
            if file.endswith(".jpg"):
                image_list.append(file)
            image_list.sort()

        self.images = image_list
