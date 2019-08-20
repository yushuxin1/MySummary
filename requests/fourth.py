import requests
from bs4 import BeautifulSoup

r = requests.get('https://python123.io/ws/demo.html')
print(r.text)
demo = r.text
# 解析器
soup = BeautifulSoup(demo, 'html.parser')
print(soup.prettify())