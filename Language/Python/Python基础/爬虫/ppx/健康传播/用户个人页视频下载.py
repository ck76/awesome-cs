import json
import time
import urllib
from urllib.error import HTTPError
import certifi
import cryptography

import requests

# (origin)video_download
# 0插眼
# 1健康传播
# 2找春风
# 3绿色观察
# 4长寿秘籍
# 5健康观察(分身)
# 6健康观察
# 7熟人志
# 8妖妖灵
# 9解忧颜值推荐+关注
# 10
# 11
# 12
# 13
# 14
switch_s = [False,
            True,
            True,
            True,
            True,
            True,
            True,
            True,
            True,
            True,
            True,
            True,
            True,
            True,
            True,
            True,
            True, ]
# TODO 更新模式下只拉取最近几次请求
mode_update = True
mode_update_flag = False

path_save_0 = "/Volumes/TOSHIBA/ppx/【0】插眼/"
path_save_1 = "/Volumes/TOSHIBA/ppx/【1】COSPLAY专场/"
path_save_2 = "/Volumes/TOSHIBA/ppx/【2】找春风/"
path_save_3 = "/Volumes/TOSHIBA/ppx/【3】绿色观察/"
path_save_4 = "/Volumes/TOSHIBA/ppx/【4】长寿秘籍/"
path_save_5 = "/Volumes/TOSHIBA/ppx/【5】健康观察(分身)/"
path_save_6 = "/Volumes/TOSHIBA/ppx/【6】健康观察/"
path_save_7 = "/Volumes/TOSHIBA/ppx/【7】熟人志/"
path_save_8 = "/Volumes/TOSHIBA/ppx/【8】妖妖灵/"
path_save_9 = "/Volumes/TOSHIBA/ppx/【9】解忧颜值推荐+关注/"
path_save_10 = "/Volumes/TOSHIBA/ppx/【10】汤姆猫/"
path_save_11 = ""
path_save_12 = ""
path_save_13 = ""
path_save_14 = ""
path_save_15 = ""
path_save_16 = ""
# 目标视频存储位置
path_save_s = [path_save_0, path_save_1, path_save_2, path_save_3, path_save_4, path_save_5, path_save_6, path_save_7,
               path_save_8, path_save_9, path_save_10, path_save_11, path_save_12, path_save_13, path_save_14,
               path_save_15, path_save_16, ]

init_url_0 = "https://is.snssdk.com/bds/ward/list/?iid=2374555398325096&resolution=1242*2208&os_version=13.5.1&app_name=super&channel=App%20Store&idfa=1ABF0A44-4CBE-4191-B8E6-154836171658&device_platform=iphone&mac_address=02:00:00:00:00:00&vid=86A0335D-BB60-42CC-A461-72D1D67C6DE1&openudid=01942689b4d6f20e58ba3abb334a86fcf32d187c&device_type=iPhone%207%20Plus&idfv=86A0335D-BB60-42CC-A461-72D1D67C6DE1&version_code=3.0.6&ac=WIFI&device_id=2673605010266535&aid=1319&update_version_code=30680&user_id=179942927110947&count=20"
init_url_1 = "https://api.ribaoapi.com/bds/user/userfeed/?iid=3993043734112957&resolution=1242*2208&app_name=super&channel=App%20Store&device_platform=iphone&idfa=1ABF0A44-4CBE-4191-B8E6-154836171658&vid=16669D53-CE1F-4081-991A-1EDCD1888DE8&openudid=be5d560c284b36c0aedb650d91fcc14095e13e7e&device_type=iPhone%207%20Plus&idfv=16669D53-CE1F-4081-991A-1EDCD1888DE8&device_id=2673605010266535&ac=WIFI&version_code=1.1.0&os_version=13.5.1&aid=1319&user_id=89008532810&direction=1&list_type=0&mas=00fb9bd826eb322495de39ff822116989ac55b44cbbb1e26903122&as=a2b563b7f545df90709335&ts=1601187925"
init_url_2 = "https://api.ribaoapi.com/bds/user/userfeed/?iid=3993043734112957&resolution=1242*2208&app_name=super&channel=App%20Store&device_platform=iphone&idfa=1ABF0A44-4CBE-4191-B8E6-154836171658&vid=16669D53-CE1F-4081-991A-1EDCD1888DE8&openudid=be5d560c284b36c0aedb650d91fcc14095e13e7e&device_type=iPhone%207%20Plus&idfv=16669D53-CE1F-4081-991A-1EDCD1888DE8&device_id=2673605010266535&ac=WIFI&version_code=1.1.0&os_version=13.5.1&aid=1319&user_id=4358067917166531&direction=1&list_type=0&mas=00386a858b4f04fc7e683d22cb007b98b7189ede29962103157477&as=a22533366a40efa1bf5764&ts=1601122570"
init_url_3 = "http://api.ribaoapi.com/bds/user/userfeed/?iid=3993043734112957&resolution=1242*2208&app_name=super&channel=App%20Store&device_platform=iphone&idfa=1ABF0A44-4CBE-4191-B8E6-154836171658&vid=16669D53-CE1F-4081-991A-1EDCD1888DE8&openudid=be5d560c284b36c0aedb650d91fcc14095e13e7e&device_type=iPhone%207%20Plus&idfv=16669D53-CE1F-4081-991A-1EDCD1888DE8&device_id=2673605010266535&ac=WIFI&version_code=1.1.0&os_version=13.5.1&aid=1319&user_id=6058032285&direction=1&list_type=0&mas=008733d3f9ab46e918d7ad84c132f4cc997689393bda592cfc3122&as=a2b521c605655fdcbf5635&ts=1601117269"
init_url_4 = "http://api.ribaoapi.com/bds/user/userfeed/?iid=3993043734112957&resolution=1242*2208&app_name=super&channel=App%20Store&device_platform=iphone&idfa=1ABF0A44-4CBE-4191-B8E6-154836171658&vid=16669D53-CE1F-4081-991A-1EDCD1888DE8&openudid=be5d560c284b36c0aedb650d91fcc14095e13e7e&device_type=iPhone%207%20Plus&idfv=16669D53-CE1F-4081-991A-1EDCD1888DE8&device_id=2673605010266535&ac=WIFI&version_code=1.1.0&os_version=13.5.1&aid=1319&user_id=1591688795264663&direction=1&list_type=0&mas=003f0dcfc2e9233eb1b41e46116b59ce0c373cb1d6afae1d90ef1a&as=a25581a644a36fecaf9788&ts=1601117236"
init_url_5 = "http://api.ribaoapi.com/bds/user/userfeed/?iid=3993043734112957&resolution=1242*2208&app_name=super&channel=App%20Store&device_platform=iphone&idfa=1ABF0A44-4CBE-4191-B8E6-154836171658&vid=16669D53-CE1F-4081-991A-1EDCD1888DE8&openudid=be5d560c284b36c0aedb650d91fcc14095e13e7e&device_type=iPhone%207%20Plus&idfv=16669D53-CE1F-4081-991A-1EDCD1888DE8&device_id=2673605010266535&ac=WIFI&version_code=1.1.0&os_version=13.5.1&aid=1319&user_id=2334989129615431&direction=1&list_type=0&mas=00729a41dc9afb6c5121cae50ea4987d7dbccc98a403a9b8eb2717&as=a2f5f1d6d6dfbf1baf4001&ts=1601117174"
init_url_6 = "http://api.ribaoapi.com/bds/user/userfeed/?iid=3993043734112957&resolution=1242*2208&app_name=super&channel=App%20Store&device_platform=iphone&idfa=1ABF0A44-4CBE-4191-B8E6-154836171658&vid=16669D53-CE1F-4081-991A-1EDCD1888DE8&openudid=be5d560c284b36c0aedb650d91fcc14095e13e7e&device_type=iPhone%207%20Plus&idfv=16669D53-CE1F-4081-991A-1EDCD1888DE8&device_id=2673605010266535&ac=WIFI&version_code=1.1.0&os_version=13.5.1&aid=1319&user_id=1226655901687588&direction=1&list_type=0&mas=00e80c5d415925a28e9578cb602502b42f7988184ac40c282b1712&as=a2c5e1466cfc3f7c6f9407&ts=1601117388"
init_url_7 = "http://api.ribaoapi.com/bds/user/userfeed/?iid=3993043734112957&resolution=1242*2208&app_name=super&channel=App%20Store&device_platform=iphone&idfa=1ABF0A44-4CBE-4191-B8E6-154836171658&vid=16669D53-CE1F-4081-991A-1EDCD1888DE8&openudid=be5d560c284b36c0aedb650d91fcc14095e13e7e&device_type=iPhone%207%20Plus&idfv=16669D53-CE1F-4081-991A-1EDCD1888DE8&device_id=2673605010266535&ac=WIFI&version_code=1.1.0&os_version=13.5.1&aid=1319&user_id=1947990820141172&direction=1&list_type=0&mas=0024adcc397162480d2cae14d1b4e16f36cd525bb5d38477d32067&as=a2a5b1d60f8fbf48af1871&ts=1601116415"
init_url_8 = "https://api.ribaoapi.com/bds/user/userfeed/?iid=3993043734112957&resolution=1242*2208&app_name=super&channel=App%20Store&device_platform=iphone&idfa=1ABF0A44-4CBE-4191-B8E6-154836171658&vid=16669D53-CE1F-4081-991A-1EDCD1888DE8&openudid=be5d560c284b36c0aedb650d91fcc14095e13e7e&device_type=iPhone%207%20Plus&idfv=16669D53-CE1F-4081-991A-1EDCD1888DE8&device_id=2673605010266535&ac=WIFI&version_code=1.1.0&os_version=13.5.1&aid=1319&user_id=4100484672&direction=1&list_type=0&mas=00fa892d3f1c1fe679b471c94625f5208d74f6a69e96e768083302&as=a2951347118bffb0c07515&ts=1601188017"
init_url_9 = "https://api.ribaoapi.com/bds/user/userfeed/?iid=3993043734112957&resolution=1242*2208&app_name=super&channel=App%20Store&device_platform=iphone&idfa=1ABF0A44-4CBE-4191-B8E6-154836171658&vid=16669D53-CE1F-4081-991A-1EDCD1888DE8&openudid=be5d560c284b36c0aedb650d91fcc14095e13e7e&device_type=iPhone%207%20Plus&idfv=16669D53-CE1F-4081-991A-1EDCD1888DE8&device_id=2673605010266535&ac=WIFI&version_code=1.1.0&os_version=13.5.1&aid=1319&user_id=54796283715&direction=1&list_type=0&mas=00312aef9ae5ce8e07155ed97dac869731a7567711fb439fee9792&as=a2a50307c5d16f51c01687&ts=1601188117"
init_url_10 = ""
init_url_11 = ""
init_url_12 = ""
init_url_13 = ""
init_url_14 = ""
init_url_15 = ""
init_url_16 = ""
# url
init_url_s = [init_url_0, init_url_1, init_url_2, init_url_3, init_url_4, init_url_5, init_url_6, init_url_7,
              init_url_8, init_url_9, init_url_10, init_url_11, init_url_12, init_url_13, init_url_14, init_url_15,
              init_url_16, ]

path_yixiazai_0 = "/Volumes/TOSHIBA/ppx/插眼.txt"
path_yixiazai_1 = "/Volumes/TOSHIBA/ppx/COSPLAY专场.txt"
# 因为【找春天】被永久封禁了，长寿秘籍原名健康传播
path_yixiazai_2 = "/Volumes/TOSHIBA/ppx/找春风.txt"
path_yixiazai_3 = "/Volumes/TOSHIBA/ppx/绿色观察.txt"
path_yixiazai_4 = "/Volumes/TOSHIBA/ppx/长寿秘籍.txt"
path_yixiazai_5 = "/Volumes/TOSHIBA/ppx/健康观察(分身).txt"
path_yixiazai_6 = "/Volumes/TOSHIBA/ppx/健康观察.txt"
path_yixiazai_7 = "/Volumes/TOSHIBA/ppx/熟人志.txt"
path_yixiazai_8 = "/Volumes/TOSHIBA/ppx/妖妖灵.txt"
path_yixiazai_9 = "/Volumes/TOSHIBA/ppx/解忧颜值推荐+关注.txt"
path_yixiazai_10 = "/Volumes/TOSHIBA/ppx/汤姆猫.txt"
path_yixiazai_11 = ""
path_yixiazai_12 = ""
path_yixiazai_13 = ""
path_yixiazai_14 = ""
path_yixiazai_15 = ""
path_yixiazai_16 = ""

# 已下载的目录文件
path_yixiazai_s = [path_yixiazai_0, path_yixiazai_1, path_yixiazai_2, path_yixiazai_3, path_yixiazai_4, path_yixiazai_5,
                   path_yixiazai_6, path_yixiazai_7, path_yixiazai_8, path_yixiazai_9, path_yixiazai_10,
                   path_yixiazai_11, path_yixiazai_12, path_yixiazai_13,
                   path_yixiazai_14, path_yixiazai_15, path_yixiazai_16, ]

headers = {
    "Host": "api.ribaoapi.com",
    "Cookie": "d_ticket=a706138bd0b723461a61380db690e82a07d02; odin_tt=b8c25a7ca2d6230a0d921425e4d4753477ad0590b016d2508a67e834af32ae445fd6aff17b737783a3ae3f3d0e3e259282a1634fff3009101bc62b51931ced92; sid_guard=2701e191636e1853e1785b4648783c3c%7C1601115548%7C5184000%7CWed%2C+25-Nov-2020+10%3A19%3A08+GMT; uid_tt=f249d37500a1aa64e439a06cdb719b66; sid_tt=2701e191636e1853e1785b4648783c3c; sessionid=2701e191636e1853e1785b4648783c3c",
    "x-ss-cookie": "d_ticket=a706138bd0b723461a61380db690e82a07d02; odin_tt=b8c25a7ca2d6230a0d921425e4d4753477ad0590b016d2508a67e834af32ae445fd6aff17b737783a3ae3f3d0e3e259282a1634fff3009101bc62b51931ced92; sessionid=2701e191636e1853e1785b4648783c3c; sid_guard=2701e191636e1853e1785b4648783c3c%7C1601115548%7C5184000%7CWed%2C+25-Nov-2020+10%3A19%3A08+GMT; sid_tt=2701e191636e1853e1785b4648783c3c; uid_tt=f249d37500a1aa64e439a06cdb719b66",
    "tt-request-time": "1601115636352",
    "user-agent": "Super 1.1.0 rv:1.1.0.6 (iPhone; iOS 13.5.1; zh_CN) Cronet",
}


def get_download_urls(path_save, init_url, cursor_url, yixiazai, origin_video_download_urls, origin_video_id_s):
    print("path_save: " + path_save)
    print(cursor_url)
    requests.packages.urllib3.disable_warnings()
    time.time()
    request_time = str(round(time.time() * 1000))
    headers["tt-request-time"] = request_time
    # TODO 就是这出的bug……
    r = requests.get(cursor_url, headers=headers)
    # 加一次
    global mode_update_flag
    print("mode_update_flag: " + str(mode_update_flag))
    if mode_update == True and mode_update_flag == True:
        return

    r.encoding = "utf-8"
    print("text: " + r.text)
    r_json = json.loads(r.text)
    data_s = r_json.get("data").get("data")
    for cell in data_s:
        temp1 = cell.get("item")
        if temp1 == None:
            continue
        temp2 = temp1.get("origin_video_download")
        if temp2 == None:
            continue
        temp3 = temp2.get("url_list")[0]
        if temp3 == None:
            continue
        temp4 = temp3.get("url")
        if temp4 == None:
            continue
        # origin_video_download = cell.get("item").get("origin_video_download").get("url_list")[0].get("url")
        origin_video_download = temp4

        if origin_video_download == "":
            continue
        print(origin_video_download)
        origin_video_id = cell.get("item").get("origin_video_id")
        # 【带水印】
        # video_download = cell.get("item").get("video").get("video_download").get("url_list")[0].get("url")
        origin_video_download_urls.append(origin_video_download)
        origin_video_id_s.append(origin_video_id)
        try:
            if yixiazai.__contains__(str(origin_video_id)):
                print("已存在：" + origin_video_id)
                mode_update_flag = True
                continue
            f = urllib.request.urlopen(origin_video_download)
            data = f.read()
            # 存储位置可自定义
            with open(path_save + str(origin_video_id) + ".mp4", 'wb') as code:
                code.write(data)
        except HTTPError:
            print(origin_video_download)
    cursor = r_json["data"].get("cursor")
    if cursor.get("has_more") == True:
        cursor = cursor.get("loadmore_cursor")
        cursor_url = init_url.replace("direction=1", "direction=2") + "&cursor=" + str(cursor)
        print("cursor -----------  cursor=" + str(cursor))
        print("cursor_url -----------  cursor_url=" + cursor_url)
        get_download_urls(path_save, init_url, cursor_url, yixiazai, origin_video_download_urls, origin_video_id_s)


def start():
    origin_video_download_urls = []
    origin_video_id_s = []
    yixiazai = []
    path_yixiazai = ""
    try:
        for index in range(0, len(switch_s)):
            # 清除上一个循环的影响
            global mode_update_flag
            mode_update_flag = False

            origin_video_download_urls = []
            origin_video_id_s = []
            yixiazai = []
            path_yixiazai = ""

            if not switch_s[index]:
                print("当前第" + str(index) + "任务不需要下载。")
                continue

            path_save = path_save_s[index]
            path_yixiazai = path_yixiazai_s[index]
            init_url = init_url_s[index]
            if path_save == "" or init_url == "" or path_yixiazai == "":
                continue
            temp = open(path_yixiazai).readlines()
            for item in temp:
                yixiazai.append(item.split("--")[0])

            get_download_urls(path_save, init_url, init_url, yixiazai, origin_video_download_urls, origin_video_id_s)

            # 保存
            with open(path_yixiazai, "w+") as file:
                for i in range(0, len(origin_video_id_s)):
                    file.writelines(origin_video_id_s[i] + "--" + origin_video_download_urls[i] + "\n")
                file.close()
            print("上一次ok！")
    finally:
        # 保存
        print("finally:xxxxxxx")
        with open(path_yixiazai, "w+") as file:
            for i in range(0, len(origin_video_id_s)):
                file.writelines(origin_video_id_s[i] + "--" + origin_video_download_urls[i] + "\n")
            file.close()


start()
