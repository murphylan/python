# -*- coding: UTF-8 -*-

import urllib3

http = urllib3.PoolManager(timeout=3.0)
http = urllib3.PoolManager(timeout=urllib3.Timeout(connect=1.0, read=2.0))


r1 = http.request(
    'GET', 'http://httpbin.org/delay/3', timeout=urllib3.Timeout(connect=1.0))
print r1.status

r2 = http.request(
    'GET', 'http://httpbin.org/delay/3', timeout=urllib3.Timeout(connect=1.0, read=2.0))
print r2.status



