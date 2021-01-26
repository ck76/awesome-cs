from _elementtree import Element

import requests
# https://xueqiu.com/1803026560/151658213
import os
import urllib
from urllib import request
from urllib.error import HTTPError
# TODO https://blog.csdn.net/qq_22592457/article/details/95490976
import requests
from lxml import etree
from urllib.parse import parse_qs, urlparse

url = "https://xueqiu.com/1803026560/151658213"

# def download_catalog(leibie, page_count, category):
#     herf_result = []
#     address_result = []
#     fail_result = []
#     for page in range(1, page_count + 1):
#         url = base_addr + str(leibie) + "_" + str(page) + ".html"
#         print(url)
#         parse_html = etree.parse(url, etree.HTMLParser())
#         herf = parse_html.xpath("//ul[@class='slist tabcon']//li[@class='item']/a/@href")
#         print(herf)
#         # print(type(herf))
#         for item in herf:
#             herf_result.append(item)

r = requests.get(url)

html = etree.parse("./雪球.html", etree.HTMLParser())
p_s = html.xpath('//div[@class="article__bd__detail"]//*')
print(dir(Element))
print(help(Element.tag))
for res in p_s:
    # print(res.tag)
    print(res.attrib)
    # print(res.text)

""""
method 一定是 function
function 不一定是 method
"""


class ck:
    name = []

    def ck_fangfa(self):
        print()


print(ck.name)
