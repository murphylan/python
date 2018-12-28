import urllib3
import json

http = urllib3.PoolManager()
r = http.request(
    'POST',
    'http://httpbin.org/post',
    fields={'field': 'value'})

print json.loads(r.data.decode('utf-8'))['form']


