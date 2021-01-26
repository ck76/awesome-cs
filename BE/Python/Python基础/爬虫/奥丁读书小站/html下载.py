# http://www.addsxz.com/cms/
# http://www.addsxz.com/News/
# http://www.addsxz.com/chunyingwenxilie/
# http://www.addsxz.com/zhexuelizhixinlixue/
# http://www.addsxz.com/xiaoshoushangyelei/
# http://www.addsxz.com/ertonglei/

# http://www.addsxz.com/cms/list_8_18.html【股票金融投资财务】
# http://www.addsxz.com/News/list_1_11.html【科技互联网计算机】
# http://www.addsxz.com/chunyingwenxilie/list_9_10.html【纯英文系列】
# http://www.addsxz.com/zhexuelizhixinlixue/list_11_65.html【哲学励志心理学】
# http://www.addsxz.com/xiaoshoushangyelei/list_12_41.html【销售商业类】
# http://www.addsxz.com/ertonglei/list_13_5.html【儿童类】
# http://www.addsxz.com/gongjulei/list_10_38.html【工具类】
import os

import requests
from lxml import etree

aoding_path = "/Users/chengkun/workspace/奥丁html/"

path_cms = aoding_path + "股票金融投资财务"
enter_command = "\n"


def cms():
    path_yuan = path_cms + " copy"
    os.chdir(path_yuan)
    for page in range(1, 19):
        url = "http://www.addsxz.com/cms/list_8_" + str(page) + ".html"
        print(url)
        r = requests.get(url)
        r.encoding = 'UTF-8'
        with open("list_8_" + str(page) + ".html", "w") as file:
            file.write(r.text)
    del_firstline(path_yuan, path_cms)
    os.chdir(path_cms)
    result = []
    for html in os.listdir(path_cms):
        if html == ".DS_Store":
            continue
        print(html)
        parse_html = etree.parse(html, etree.HTMLParser())
        title = parse_html.xpath("//div[@class='block']/h2/a/text()")
        for line in title:
            result.append(str(line))
        print(str(title))
    with open("股票金融投资财务.txt", 'w') as fout:
        for item in result:
            fout.writelines(item)
            fout.writelines(enter_command)


path_News = aoding_path + "科技互联网计算机"


def News():
    path_yuan = path_News + " copy"
    os.chdir(path_yuan)
    for page in range(1, 12):
        url = "http://www.addsxz.com/News/list_1_" + str(page) + ".html"
        print(url)
        r = requests.get(url)
        r.encoding = 'UTF-8'
        with open("list_1_" + str(page) + ".html", "w") as file:
            file.write(r.text)
    del_firstline(path_yuan, path_News)
    os.chdir(path_News)
    result = []
    for html in os.listdir(path_News):
        if html == ".DS_Store":
            continue
        print(html)
        parse_html = etree.parse(html, etree.HTMLParser())
        title = parse_html.xpath("//div[@class='block']/h2/a/text()")
        for line in title:
            result.append(str(line))
        print(str(title))
    with open("科技互联网计算机.txt", 'w') as fout:
        for item in result:
            fout.writelines(item)
            fout.writelines(enter_command)


path_chunyingwenxilie = aoding_path + "纯英文系列"


def chunyingwenxilie():
    path_yuan = path_chunyingwenxilie + " copy"
    os.chdir(path_yuan)
    for page in range(1, 11):
        url = "http://www.addsxz.com/chunyingwenxilie/list_9_" + str(page) + ".html"
        print(url)
        r = requests.get(url)
        r.encoding = 'UTF-8'
        with open("list_9_" + str(page) + ".html", "w") as file:
            file.write(r.text)
    del_firstline(path_yuan, path_chunyingwenxilie)
    os.chdir(path_chunyingwenxilie)
    result = []
    for html in os.listdir(path_chunyingwenxilie):
        if html == ".DS_Store":
            continue
        print(html)
        parse_html = etree.parse(html, etree.HTMLParser())
        title = parse_html.xpath("//div[@class='block']/h2/a/text()")
        for line in title:
            result.append(str(line))
        print(str(title))
    with open("纯英文系列.txt", 'w') as fout:
        for item in result:
            fout.writelines(item)
            fout.writelines(enter_command)


path_zhexuelizhixinlixue = aoding_path + "哲学励志心理学"


def zhexuelizhixinlixue():
    path_yuan = path_zhexuelizhixinlixue + " copy"
    os.chdir(path_yuan)
    # for page in range(1, 66):
    #     url = "http://www.addsxz.com/zhexuelizhixinlixue/list_11_" + str(page) + ".html"
    #     print(url)
    #     r = requests.get(url)
    #     r.encoding = 'UTF-8'
    #     with open("list_11_" + str(page) + ".html", "w") as file:
    #         file.write(r.text)
    del_firstline(path_yuan, path_zhexuelizhixinlixue)
    os.chdir(path_zhexuelizhixinlixue)
    result = []
    for html in os.listdir(path_zhexuelizhixinlixue):
        if html == ".DS_Store":
            continue
        print(html)
        parse_html = etree.parse(html, etree.HTMLParser())
        title = parse_html.xpath("//div[@class='block']/h2/a/text()")
        for line in title:
            result.append(str(line))
        print(str(title))
    with open("哲学励志心理学.txt", 'w') as fout:
        for item in result:
            fout.writelines(item)
            fout.writelines(enter_command)


path_xiaoshoushangyelei = aoding_path + "销售商业类"


def xiaoshoushangyelei():
    path_yuan = path_xiaoshoushangyelei + " copy"
    os.chdir(path_yuan)
    for page in range(1, 19):
        url = "http://www.addsxz.com/xiaoshoushangyelei/list_12_" + str(page) + ".html"
        print(url)
        r = requests.get(url)
        r.encoding = 'UTF-8'
        with open("list_12_" + str(page) + ".html", "w") as file:
            file.write(r.text)
    del_firstline(path_yuan, path_xiaoshoushangyelei)
    os.chdir(path_xiaoshoushangyelei)
    result = []
    for html in os.listdir(path_xiaoshoushangyelei):
        if html == ".DS_Store":
            continue
        print(html)
        parse_html = etree.parse(html, etree.HTMLParser())
        title = parse_html.xpath("//div[@class='block']/h2/a/text()")
        for line in title:
            result.append(str(line))
        print(str(title))
    with open("销售商业类.txt", 'w') as fout:
        for item in result:
            fout.writelines(item)
            fout.writelines(enter_command)


path_ertonglei = aoding_path + "儿童类"


def ertonglei():
    path_yuan = path_ertonglei + " copy"
    os.chdir(path_yuan)
    # for page in range(1, 6):
    #     url = "http://www.addsxz.com/ertonglei/list_13_" + str(page) + ".html"
    #     print(url)
    #     r = requests.get(url)
    #     r.encoding = 'UTF-8'
    #     with open("list_13_" + str(page) + ".html", "w") as file:
    #         file.write(r.text)
    del_firstline(path_yuan, path_ertonglei)
    os.chdir(path_ertonglei)
    result = []
    for html in os.listdir(path_ertonglei):
        if html == ".DS_Store":
            continue
        print(html)
        parse_html = etree.parse(html, etree.HTMLParser())
        title = parse_html.xpath("//div[@class='block']/h2/a/text()")
        for line in title:
            result.append(str(line))
        print(str(title))
    with open("儿童类.txt", 'w') as fout:
        for item in result:
            fout.writelines(item)
            fout.writelines(enter_command)


path_gongjulei = aoding_path + "工具类"


def gongjulei():
    path_yuan = path_gongjulei + " copy"
    os.chdir(path_yuan)
    for page in range(1, 39):
        url = "http://www.addsxz.com/gongjulei/list_10_" + str(page) + ".html"
        print(url)
        r = requests.get(url)
        r.encoding = 'UTF-8'
        with open("list_10_" + str(page) + ".html", "w") as file:
            file.write(r.text)
    del_firstline(path_yuan, path_gongjulei)
    os.chdir(path_gongjulei)
    result = []
    for html in os.listdir(path_gongjulei):
        if html == ".DS_Store":
            continue
        print(html)
        parse_html = etree.parse(html, etree.HTMLParser())
        title = parse_html.xpath("//div[@class='block']/h2/a/text()")
        for line in title:
            result.append(str(line))
        print(str(title))
    with open("工具类.txt", 'w') as fout:
        for item in result:
            fout.writelines(item)
            fout.writelines(enter_command)


"""删除第一行"""


def del_firstline(path_yuan, path_save):
    os.chdir(path_yuan)
    files = os.listdir()
    for file in files:
        if file == ".DS_Store":
            continue
        os.chdir(path_yuan)
        with open(file, 'r') as fin:
            data = fin.read().splitlines(True)
        os.chdir(path_save)
        with open(file, 'w') as fout:
            fout.writelines(data[1:])
        os.chdir(path_yuan)


# cms()
# News()
# chunyingwenxilie()
# zhexuelizhixinlixue()
# xiaoshoushangyelei()
# ertonglei()
gongjulei()
