import requests
import pprint

r = requests.get('http://www.baidu.com')
print(r.status_code)
print(type(r))
pprint.pprint(r.headers)
print(r.encoding)
print(r.apparent_encoding)
print(r.text)
r.encoding = r.apparent_encoding
pprint.pprint(r.text)