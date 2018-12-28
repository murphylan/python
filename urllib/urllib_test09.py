# -*- coding: UTF-8 -*-
from urllib import request

if __name__ == "__main__":
    # 以CSDN为例，CSDN不更改User Agent是无法访问的
    url = 'http://393355173.ax.nofollow.51wyfl.com/index.php/toupiao/h5/detail?id=762786&vid=393355173'
    head = {}
    # 写入User Agent信息
    head['User-Agent'] = 'Mozilla/5.0 (iPad; CPU OS 5_0 like Mac OS X) AppleWebKit/534.46 (KHTML, like Gecko) Version/5.1 Mobile/9A334 Safari/7534.48.3'
    # 创建Request对象
    req = request.Request(url, headers=head)
    # 传入创建好的Request对象
    response = request.urlopen(req)
    # 读取响应信息并解码
    html = response.read().decode('utf-8')
    # 打印信息
    print(html)
