import urllib3
from urllib import urlencode
import json

http = urllib3.PoolManager()
encoded_args = urlencode({'arg': 'value'})
url = 'http://httpbin.org/post?' + encoded_args
r = http.request('POST', url)

print json.loads(r.data.decode('utf-8'))['args']



