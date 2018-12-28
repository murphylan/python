# -*- coding: UTF-8 -*-

import certifi
import urllib3
http = urllib3.PoolManager(
    cert_reqs='CERT_REQUIRED',
    ca_certs=certifi.where())

r1 = http.request('GET', 'https://google.com')
print r1.status

r2 = http.request('GET', 'https://expired.badssl.com')
print r2.status


