# -*- coding: UTF-8 -*-
from urllib import request, parse, error
import json

if __name__ == "__main__":
    # 对应上图的Request URL
    Request_URL = 'http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule&smartresult=ugc'
    # 创建Form_Data字典，存储上图的Form Data
    Form_Data = {}
    Form_Data['type'] = 'AUTO'
    Form_Data['i'] = 'Hello world'
    Form_Data['doctype'] = 'json'
    Form_Data['version'] = '2.1'
    Form_Data['keyfrom'] = 'fanyi.web'
    Form_Data['ue'] = 'UTF-8'
    # 使用urlencode方法转换标准格式
    data = parse.urlencode(Form_Data).encode('utf-8')
    try:
        # 传递Request对象和转换完格式的数据
        response = request.urlopen(Request_URL, data)
        # 读取信息并解码
        html = response.read().decode('utf-8')
        # 使用JSON
        translate_results = json.loads(html)
    except error.URLError as e:
        if hasattr(e, 'code'):
            print("HTTPError")
            print(e.code)
        elif hasattr(e, 'reason'):
            print("URLError")
            print(e.reason)
    # 找到翻译结果
    translate_results = translate_results['translateResult'][0][0]['tgt']
    # 打印翻译信息
    print("翻译的结果是：%s" % translate_results)
