# coding: gb2312
# !/usr/bin/env python

# http://www.j9p.com/down/525808.html
# http://www.j9p.com/down/517525.html
# /Users/chengkun/workspace/iBook/爬虫/
import os
import requests
import urllib
from lxml import etree

aoding_path = "/Users/chengkun/workspace/奥丁html/"

enter_command = "\r\n"
# os.chdir("/Users/chengkun/workspace/iBook/爬虫/奥丁html/")
os.chdir(aoding_path)
htmls = os.listdir()
htmls.sort()
print(htmls)
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.116 Safari/537.36'
}
# 共163页
result = []
for html in htmls:
    if html == ".DS_Store":
        continue
    print(html)
    # r = requests.get("http://www.addsxz.com/html/list_6_" + str(page) + ".html", headers=headers)
    # r.encoding = 'UTF-8'
    # with open("list_6_" + str(page) + ".html","w") as file:
    #     file.write(r.text)

    parse_html = etree.parse(html, etree.HTMLParser())
    title = parse_html.xpath("//div[@class='block']/h2/a/text()")
    for line in title:
        result.append(str(line))
    print(str(title))
with open("奥丁所有书籍.txt", 'w') as fout:
    for item in result:
        fout.writelines(item)
        fout.writelines(enter_command)


# r = requests.get('http://www.addsxz.com/html/list_6_2.html',headers=headers)
# r.encoding='UTF-8'
# print(r.text)


def xiazai_html_list():
    for i in range(1, 19):
        # http://www.addsxz.com/cms/list_8_18.html【股票金融投资财务】
        # http://www.addsxz.com/News/list_1_11.html【科技互联网计算机】
        # http://www.addsxz.com/chunyingwenxilie/list_9_10.html【纯英文系列】
        # http://www.addsxz.com/zhexuelizhixinlixue/list_11_65.html【哲学励志心理学】
        # http://www.addsxz.com/xiaoshoushangyelei/list_12_41.html【销售商业类】
        # http://www.addsxz.com/ertonglei/list_13_5.html【儿童类】
        url = "http://www.addsxz.com/cms/list_8_" + str(i) + ".html"
        print(url)
        f = urllib.request.urlopen(url)
        data = f.read()
        # 存储位置可自定义
        with open("sss.pdf", 'wb') as code:
            code.write(data)




"""删除第一行"""


def del_firstline():
    files = os.listdir()
    for file in files:
        os.chdir(aoding_path)
        with open(file, 'r') as fin:
            data = fin.read().splitlines(True)
        os.chdir("/Users/chengkun/workspace/iBook/爬虫/奥丁html/")
        with open(file, 'w') as fout:
            fout.writelines(data[1:])
        os.chdir(aoding_path)

