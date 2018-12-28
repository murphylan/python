import urllib3
import json

http = urllib3.PoolManager()
data = {'attribute': 'value'}
encoded_data = json.dumps(data).encode('utf-8')
r = http.request(
    'POST',
    'http://httpbin.org/post',
    body=encoded_data,
    headers={'Content-Type': 'application/json'})

print json.loads(r.data.decode('utf-8'))['json']



