# -*- coding: UTF-8 -*-

import pandas
import os
import os.path
import codecs
import json
from GPSPhoto import gpsphoto
import exifread
from urllib.request import urlopen

import shutil

filePaths = []
fileContents = []


def main():
    # response = urlopen("http://api.rethumb.com/v1/exif/all/http://images.rethumb.com/image_exif_1.jpg")
    # json_data = json.loads(response.read().decode("utf-8"))
    # print(parseGPSCoordinates(json_data))
    for root, dirs, files in os.walk('/work/accordion/abc/20170329/'):
        for name in files:
            if not name.lower().endswith(('.jpg', '.png', '.jpeg')):
                continue
            filePath = os.path.join(root, name)
            filePaths.append(filePath)
            print()
            # f = codecs.open(filePath, 'r', 'utf-8')
            # fileContent = f.read()
            # f.close()
            # fileContents.append(fileContent)
    parseImagesData(filePaths)


def parseImagesData(files):
    dst = os.mkdir('/work/test/abca')
    try:
        for name in files:
            print(name)
            shutil.copy(name, '/work/test/abca/')
            # f = open(name, 'rb')
            # # Return Exif tags
            # tags = exifread.process_file(f)
            # print(tags);
            # for tag in tags.keys():
            #     if tag not in ('JPEGThumbnail', 'TIFFThumbnail', 'Filename', 'EXIF MakerNote'):
            #         print("Key: %s, value %s", (tag, tags[tag]))
    except ValueError:
        print(ValueError)

# filePaths = []
# fileContents = []


# data = gpsphoto.getGPSData('/work/accordion/abc/20170329/身份证/IMG_0606.JPG')
# if data is None:
#     return


def parseGPSCoordinates(data):
    if (data['GPS'] is None):
        return 'GPS Coordinates not found'

    values = {}

    values['LAT'] = data['GPS']['GPSLatitudeRef']
    values['LONG'] = data['GPS']['GPSLongitudeRef']
    values['LAT_DEG'] = applyDivision(data['GPS']['GPSLatitude'][0])
    values['LAT_MIN'] = applyDivision(data['GPS']['GPSLatitude'][1])
    values['LAT_SEC'] = applyDivision(data['GPS']['GPSLatitude'][2])
    values['LONG_DEG'] = applyDivision(data['GPS']['GPSLongitude'][0])
    values['LONG_MIN'] = applyDivision(data['GPS']['GPSLongitude'][1])
    values['LONG_SEC'] = applyDivision(data['GPS']['GPSLongitude'][2])

    return format("{LAT} {LAT_DEG}° {LAT_MIN}' {LAT_SEC}'' {LONG} {LONG_DEG}° {LONG_MIN}' {LONG_SEC}''", values)


def applyDivision(value):
    tokens = value.split('/')
    return trim(int(tokens[0]) / float(tokens[1]))


def trim(f):
    if f.is_integer():
        return int(f)
    return f


def format(s, values):
    for key in values:
        s = s.replace('{' + key + '}', str(values[key]))

    return s


main()
