# -*- coding: UTF-8 -*-

import urllib3
import json

http = urllib3.PoolManager()
with open('example.jpg', 'rb') as fp:
    binary_data = fp.read()
r = http.request(
    'POST',
    'http://httpbin.org/post',
    body=binary_data,
    headers={'Content-Type': 'image/jpeg'})

print json.loads(r.data.decode('utf-8'))['data']



