#!/usr/bin/env python2

import os
import shutil
import zipfile
import rarfile
import re

import tornado.web
import tornado.gen

from common import *


class AdminRefreshHandler(tornado.web.RequestHandler):

    def get(self):
        self.clear_comics_folder(comic_static_folder)

        for file in os.listdir(comic_archive_folder):

            full_file = comic_archive_folder + '/' + file
            if file.endswith(".cbz"):

                clean_file = re.sub('[^0-9a-zA-Z]+', '_', file[:-4])
                clean_file_folder = comic_static_folder + '/' + clean_file

                if not os.path.exists(clean_file_folder):
                    os.makedirs(clean_file_folder)

                self.write(clean_file)
                self.extract_zip(zip_file=full_file, output_folder=clean_file_folder)

            elif file.endswith(".cbr"):

                clean_file = re.sub('[^0-9a-zA-Z]+', '_', file[:-4])
                clean_file_folder = comic_static_folder + '/' + clean_file

                if not os.path.exists(clean_file_folder):
                    os.makedirs(clean_file_folder)

                self.write(clean_file)
                rar = rarfile.RarFile(full_file)
                rar.extractall(path=clean_file_folder)
                # self.extract_zip(zip_file=full_file, output_folder=clean_file_folder)

                print 'a rar file: ' + full_file
            else:
                # TODO - rarfile
                # Are there any other cbx formats?
                print 'not a zip: ' + full_file

        get_comics()

    def clear_comics_folder(self, folder):
        for file in os.listdir(folder):
            file_path = os.path.join(folder, file)
            try:
                if os.path.isfile(file_path):
                    print 'removing file ' + file_path
                    os.unlink(file_path)
                if os.path.isdir(file_path):
                    print 'removing directory ' + file_path
                    shutil.rmtree(file_path)
            except Exception, e:
                print e

    def extract_zip(self, zip_file, output_folder):

        if zipfile.is_zipfile(zip_file):
            with zipfile.ZipFile(zip_file, "r") as z:
                z.extractall(output_folder)
