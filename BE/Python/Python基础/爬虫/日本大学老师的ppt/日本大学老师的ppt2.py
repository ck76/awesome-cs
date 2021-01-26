import urllib
from urllib.error import HTTPError
import  os
import  sys
import requests
from lxml import etree
import ssl
ssl._create_default_https_context = ssl._create_unverified_context
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36', }

# base_url = "http://www.akita-pu.ac.jp/system/elect/ins/kusakari/japanese/teaching/InfoTheo/2006/"
# https://www-alg.ist.hokudai.ac.jp/~thomas/ToC/SLIDES/
# base_url="https://www-alg.ist.hokudai.ac.jp/~thomas/ToC/SLIDES/"
base_url="https://www.jaist.ac.jp/~uehara/course/2009/ti118/"
r = requests.get(base_url)
parse_html = etree.HTML(r.text)
title_s = parse_html.xpath("//a/@href")
ok_s = []
print (os.getcwd()) #获取当前工作目录路径
# print os.path.abspath('.') #获取当前工作目录路径
# print os.path.abspath('test.txt') #获取当前目录文件下的工作目录路径
# print os.path.abspath('..') #获取当前工作的父目录 ！注意是父目录路径
# print os.path.abspath(os.curdir) #获取当前工作目录路径
with open("result.txt", 'r') as code:
    ok_s=code.readlines()
    # print(ok_s)

for item in title_s:
    url = base_url + item
    if url+"\n" in ok_s:
        print(url+"已存在")
        continue
    print(url)

    try:
        f = urllib.request.urlopen(url)
        data = f.read()
        # 存储位置可自定义
        with open("/Users/chengkun/Downloads/" + item, 'wb') as code:
            code.write(data)
        ok_s.append(url)
    except PermissionError:
        print(url)
    except HTTPError:
        print("exception:" + url)
    except UnicodeEncodeError:
        print("exception:" + url)
    except FileNotFoundError:
        print("exception:" + url)
    finally:
        with open("result.txt", 'w') as code:
            for item in ok_s:
                code.writelines(item+"\n")
