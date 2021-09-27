# https://www.runoob.com/w3cnote/page/109
# post-intro

"""
<div class="post-intro">
                        <h2>
                        <a target="_blank" href="/w3cnote/python-locals-globals.html" rel="bookmark"
                               title="Python 两个内置函数: locals 和 globals">Python 两个内置函数: locals 和 globals</a> <i
                                class="fa fa-external-link"></i></h2>
                    </div>
"""
import os
from urllib import request
from urllib.error import HTTPError
from urllib.parse import parse_qs, urlparse
import requests
from lxml import etree

titles = []
links=[]
for i in range(1, 110):
    url = "http://www.runoob.com/w3cnote/page/" + str(i)
    print(url)
    # parse_html = etree.parse("./html/notes.html", etree.HTMLParser())
    r=requests.get(url)
    r.encoding="utf-8"
    parse_html = etree.HTML(r.text)
    title = parse_html.xpath("//div[@class='post-intro']//a/@title")
    link=parse_html.xpath("//a[@class='focus']/@href")
    for item in title:
        titles.append(item)
    for item in link:
        links.append(item)
print(links)
#
# print(titles)
# with open("目录.txt", 'w') as fout:
#     for item in titles:
#         fout.writelines(item+"\n")
with open("链接.txt", 'w') as fout:
    for item in links:
        fout.writelines(item+"\n")