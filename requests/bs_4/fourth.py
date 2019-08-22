import requests
from bs4 import BeautifulSoup

r = requests.get('https://python123.io/ws/demo.html')
# print(r.text)
demo = r.text
# 解析器
soup = BeautifulSoup(demo, 'html.parser')
print(soup.title)
# print(soup.prettify())
tag = soup.a
print(tag)
print(soup.a.name)
print(soup.a.parent.name)
print(soup.a.parent.parent.name)
tag1 = soup.a
print(tag1.attrs)
print(tag1.attrs['class'])
print(tag1.attrs['href'])
print(type(tag1.attrs))
print(type(tag1))
print(soup.a.string)
print(soup.p)
print(soup.p.string)
print(type(soup.p.string))

print('-----------------------------------------')

newsoup = BeautifulSoup('<b><!--This is a comment--></b><p>This is not a comment</p>', 'html.parser')
print(newsoup.b.string)
print(type(newsoup.b.string))
print(newsoup.p.string)
print(type(newsoup.p.string))
