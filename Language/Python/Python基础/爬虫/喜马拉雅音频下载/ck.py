import os
import json
import urllib
from urllib.error import HTTPError

import requests
from lxml import etree
from urllib.parse import parse_qs

# http://www.ximalaya.com/tracks/95414554.json    二级页 正经
# A开头重新命名
# https://www.ximalaya.com/gerenchengzhang/16059951/p1(30)-p8(10)
pre_url = "https://www.ximalaya.com/youshengshu/14289577/p"
second_url = "http://www.ximalaya.com/tracks/"
result_mp4_json = []
result_mp4 = []
result_mp4_name = []
save_path = "/Users/chengkun/Downloads/喜马拉雅/道德经-白话版/"
categ = "renwenjp"
album_id = "2993623"
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36'
}
for i in range(1, 9):
    url = "https://www.ximalaya.com/" + categ + "/" + album_id + "/p" + str(i)
    r = requests.get(url, headers=headers)
    parse_html = etree.HTML(r.text)
    mp4s = parse_html.xpath("//div[@class='text _Vc']/a/@href")
    for item in mp4s:
        result_mp4_json.append(item.split("/")[3])

for item in result_mp4_json:
    url = second_url + str(item) + ".json"
    print(url)
    r = requests.get(url, headers=headers)
    result_mp4.append(r.json().get("play_path_32"))
    name = r.json().get("title")
    result_mp4_name.append(name)
for i in range(0, result_mp4.__len__()):
    print(result_mp4[i])
    try:
        f = urllib.request.urlopen(result_mp4[i])
        data = f.read()
        # 存储位置可自定义
        with open(save_path + result_mp4_name[i] + ".mp4", 'wb') as code:
            code.write(data)
    except AttributeError:
        print(result_mp4[i])
    except HTTPError:
        print(result_mp4[i])
