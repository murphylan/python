# -*- coding: UTF-8 -*-
import urllib3

http = urllib3.PoolManager()
try:
    http.request('GET', 'nx.example.com', retries=False)
except urllib3.exceptions.NewConnectionError:
    print('Connection failed.')


print r.status
