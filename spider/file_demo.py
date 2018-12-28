# -*- coding: UTF-8 -*-

import urllib3
import json

http = urllib3.PoolManager()
with open('README.md') as fp:
    file_data = fp.read()

# 'text/plain' 即元数组的第3个参数
r = http.request(
    'POST',
    'http://httpbin.org/post',
    fields={
        'filefield': ('example.txt', file_data, 'text/plain'),
    })
print json.loads(r.data.decode('utf-8'))['files']



