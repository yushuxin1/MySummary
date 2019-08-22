"""
功能描述
    输入：大学排名URL链接
    输出：大学排名信息的屏幕输出(排名，大学名称，总分)
    技术路线：requests-bs4
    定向爬虫：仅对输入URL进行爬取，不扩展爬取

程序的结构设计
    1) 从网络上获取大学排名网页内容
        getHTMLText()
    2) 提取网页内容中信息到合适的数据结构
        fillUnivList()
    3) 利用数据结构展示并输出结果
        printUnivList()
"""

import requests
from bs4 import BeautifulSoup
import bs4

def getHTMLText(url):
    try:
        r = requests.get(url, timeout=30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return ''

def fillUnivList(ulist, html):
    soup = BeautifulSoup(html, 'html.parser')
    for tr in soup.find('tbody').children:
        # 不是bs4库定义的Tag将会过滤掉
        if isinstance(tr, bs4.element.Tag):
            tds = tr('td')
            ulist.append([tds[0].string, tds[1].string, tds[2].string])

def printUnivList(ulist, num):
    tplt = '{0:^10}\t{1:{3}^10}\t{2:^10}'
    print(tplt.format('排名', '学校名称', '总分', chr(12288)))
    for i in range(num):
        u = ulist[i]
        print(tplt.format(u[0], u[1], u[2], chr(12288)))

def main():
    uinfo = []
    url = 'http://www.zuihaodaxue.cn/zuihaodaxuepaiming2016.html'
    html = getHTMLText(url)
    fillUnivList(uinfo, html)
    printUnivList(uinfo, 20)  # 20 univs

main()