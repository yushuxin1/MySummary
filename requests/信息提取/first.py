import requests
from bs4 import BeautifulSoup
import re


r = requests.get('https://python123.io/ws/demo.html')
demo = r.text
soup = BeautifulSoup(demo, 'html.parser')
for link in soup.find_all('a'):
    print(link.get('href'))
print(soup.find_all(['a', 'b']))

for tag in soup.find_all(re.compile('b')):
    print(tag.name)