# -*- coding: UTF-8 -*-
from urllib import request
import ssl
import chardet

if __name__ == "__main__":
    ssl._create_default_https_context = ssl._create_unverified_context
    
    req = request.Request("http://fanyi.baidu.com/")
    response = request.urlopen(req)
    html = response.read()

    charset = chardet.detect(html)
    print(charset)
    html = html.decode(charset.get('encoding'))
    print(html)
