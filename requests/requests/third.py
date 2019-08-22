import requests

#  params
kv = {'key1': 'value1', 'key2': 'value2'}
r = requests.request('GTE', 'http://python123.io/ws', params=kv)
print(r.url)

# data
kv1 = {'key1': 'value1', 'key2': 'value2'}
r1 = requests.request('POST', 'http://python123.io/ws', data=kv1)
body = '主体内容'
r2 = requests.request('POST', 'http://python123.io/ws', data=body)
