# coding: gb2312
# !/usr/bin/env python

# http://www.j9p.com/down/525808.html
# http://www.j9p.com/down/517525.html
# /Users/chengkun/workspace/iBook/����/
import os
import requests
import urllib
from lxml import etree

aoding_path = "/Users/chengkun/workspace/�¶�html/"

enter_command = "\r\n"
# os.chdir("/Users/chengkun/workspace/iBook/����/�¶�html/")
os.chdir(aoding_path)
htmls = os.listdir()
htmls.sort()
print(htmls)
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.116 Safari/537.36'
}
# ��163ҳ
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
with open("�¶������鼮.txt", 'w') as fout:
    for item in result:
        fout.writelines(item)
        fout.writelines(enter_command)


# r = requests.get('http://www.addsxz.com/html/list_6_2.html',headers=headers)
# r.encoding='UTF-8'
# print(r.text)


def xiazai_html_list():
    for i in range(1, 19):
        # http://www.addsxz.com/cms/list_8_18.html����Ʊ����Ͷ�ʲ���
        # http://www.addsxz.com/News/list_1_11.html���Ƽ��������������
        # http://www.addsxz.com/chunyingwenxilie/list_9_10.html����Ӣ��ϵ�С�
        # http://www.addsxz.com/zhexuelizhixinlixue/list_11_65.html����ѧ��־����ѧ��
        # http://www.addsxz.com/xiaoshoushangyelei/list_12_41.html��������ҵ�ࡿ
        # http://www.addsxz.com/ertonglei/list_13_5.html����ͯ�ࡿ
        url = "http://www.addsxz.com/cms/list_8_" + str(i) + ".html"
        print(url)
        f = urllib.request.urlopen(url)
        data = f.read()
        # �洢λ�ÿ��Զ���
        with open("sss.pdf", 'wb') as code:
            code.write(data)




"""ɾ����һ��"""


def del_firstline():
    files = os.listdir()
    for file in files:
        os.chdir(aoding_path)
        with open(file, 'r') as fin:
            data = fin.read().splitlines(True)
        os.chdir("/Users/chengkun/workspace/iBook/����/�¶�html/")
        with open(file, 'w') as fout:
            fout.writelines(data[1:])
        os.chdir(aoding_path)

