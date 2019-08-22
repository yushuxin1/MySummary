# 百度/360关键词搜索提交

import requests

keyword = 'python'
try:
    kv = {
        'wd': keyword
    }
    # kv = {
    #     'q': keyword
    # }
    r = requests.get('http://www.baidu.com/s', params=kv)
    print(r.request.url)
    r.raise_for_status()
    print(len(r.text))
except:
    print('爬取失败')