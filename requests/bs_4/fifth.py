from bs4 import BeautifulSoup
import requests

r = requests.get('https://python123.io/ws/demo.html')
demo = r.text

soup = BeautifulSoup(demo, 'html.parser')

# print(soup.head)
# print(soup.head.contents)
# print(soup.body.contents)
# print(len(soup.body.contents))
# print(soup.body.contents[0])

print(soup.title.parent)
print(soup.html.parent)
