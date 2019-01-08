# -*- coding: UTF-8 -*-

import os
import os.path
from GPSPhoto import gpsphoto
import exifread
from urllib.request import urlopen

import shutil

filePaths = []
fileContents = []
sourcePath = '/work/accordion/abc/20170329/';
dstPath = '/work/test/abca';
limit_size = 31*1024  #图片大小限制，30K


def main():
    for root, dirs, files in os.walk(sourcePath):
        for name in files:
            if not name.lower().endswith(('.jpg', '.png', '.jpeg')):
                continue
            filePath = os.path.join(root, name)
            filesize = os.path.getsize(filePath)
            if (filesize <= limit_size):
                # print(filePath)
                continue
            filePaths.append(filePath)
    copyFiles(filePaths)


def copyFiles(files):
    try:
        if not os.path.exists(dstPath):
            os.makedirs(dstPath)
        for name in files:
            print(name)
            shutil.copy(name, dstPath)
    except ValueError:
        print(ValueError)


main()
