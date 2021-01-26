import json
import urllib
from urllib.error import HTTPError
import certifi
import cryptography
# import 用户个人页视频下载
import requests

s = '''
install_id=2374555398325096; ttreq=1$5e844322393483f3a1d4e2d0944a149cc9273d6f; d_ticket=5f8fc87635be7acc88e9a5708a3f046607d02; odin_tt=086849e00d3f955d5541126c9a7dec7ec2db27557fdff128f543fda2466a825f2b1ee2b9585686725c960c1e409df588c405e4b8b8be5754b445f00e4af92c8d; sessionid=158c6ffe4aa1c03f4d8eef9c7487c6a0; sessionid_ss=158c6ffe4aa1c03f4d8eef9c7487c6a0; sid_guard=158c6ffe4aa1c03f4d8eef9c7487c6a0%7C1599353104%7C5184000%7CThu%2C+05-Nov-2020+00%3A45%3A04+GMT; sid_tt=158c6ffe4aa1c03f4d8eef9c7487c6a0; uid_tt=0b8e14f094b02cee966fad4d20de14af; uid_tt_ss=0b8e14f094b02cee966fad4d20de14af
odin_tt=086849e00d3f955d5541126c9a7dec7ec2db27557fdff128f543fda2466a825f2b1ee2b9585686725c960c1e409df588c405e4b8b8be5754b445f00e4af92c8d; d_ticket=5f8fc87635be7acc88e9a5708a3f046607d02; sid_guard=158c6ffe4aa1c03f4d8eef9c7487c6a0%7C1599353104%7C5184000%7CThu%2C+05-Nov-2020+00%3A45%3A04+GMT; uid_tt=0b8e14f094b02cee966fad4d20de14af; uid_tt_ss=0b8e14f094b02cee966fad4d20de14af; sid_tt=158c6ffe4aa1c03f4d8eef9c7487c6a0; sessionid=158c6ffe4aa1c03f4d8eef9c7487c6a0; sessionid_ss=158c6ffe4aa1c03f4d8eef9c7487c6a0; install_id=2374555398325096; ttreq=1$5e844322393483f3a1d4e2d0944a149cc9273d6f
'''
headers = {
    # TODO 变四样，两样时间可猜
    "Host": "lf.snssdk.com",
    "Cookie": "odin_tt=086849e00d3f955d5541126c9a7dec7ec2db27557fdff128f543fda2466a825f2b1ee2b9585686725c960c1e409df588c405e4b8b8be5754b445f00e4af92c8d; d_ticket=5f8fc87635be7acc88e9a5708a3f046607d02; sid_guard=158c6ffe4aa1c03f4d8eef9c7487c6a0%7C1599353104%7C5184000%7CThu%2C+05-Nov-2020+00%3A45%3A04+GMT; uid_tt=0b8e14f094b02cee966fad4d20de14af; uid_tt_ss=0b8e14f094b02cee966fad4d20de14af; sid_tt=158c6ffe4aa1c03f4d8eef9c7487c6a0; sessionid=158c6ffe4aa1c03f4d8eef9c7487c6a0; sessionid_ss=158c6ffe4aa1c03f4d8eef9c7487c6a0; install_id=2374555398325096; ttreq=1$5e844322393483f3a1d4e2d0944a149cc9273d6f",
    "x-tt-token": "00158c6ffe4aa1c03f4d8eef9c7487c6a06e3c8a43680206e28de7a4277c8847ec1489eef72ab80aa4b50a96f145a84a558",
    "x-ss-cookie": "install_id=2374555398325096; ttreq=1$5e844322393483f3a1d4e2d0944a149cc9273d6f; d_ticket=5f8fc87635be7acc88e9a5708a3f046607d02; odin_tt=086849e00d3f955d5541126c9a7dec7ec2db27557fdff128f543fda2466a825f2b1ee2b9585686725c960c1e409df588c405e4b8b8be5754b445f00e4af92c8d; sessionid=158c6ffe4aa1c03f4d8eef9c7487c6a0; sessionid_ss=158c6ffe4aa1c03f4d8eef9c7487c6a0; sid_guard=158c6ffe4aa1c03f4d8eef9c7487c6a0%7C1599353104%7C5184000%7CThu%2C+05-Nov-2020+00%3A45%3A04+GMT; sid_tt=158c6ffe4aa1c03f4d8eef9c7487c6a0; uid_tt=0b8e14f094b02cee966fad4d20de14af; uid_tt_ss=0b8e14f094b02cee966fad4d20de14af",
    # TODO
    "tt-request-time": "1601112363818",
    "user-agent": "Super 3.0.6 rv:3.0.6.80 (iPhone; iOS 13.5.1; zh_CN) Cronet",
    "sdk-version": "2",
    "passport-sdk-version": "5.12.0",
    "x-ss-dp": "1319",
    # TODO
    # "x-tt-trace-id": "00-c97b7d2c0d97fa12ce819a77d4ac0527-c97b7d2c0d97fa12-01",
    # TODO
    "x-khronos": "1601112362",
    # TODO  必须有
    "x-gorgon": "84024064000067ae9b0331c1ecbb6f5a9576a384016abd608d78"
}

headers2 = {
    "Host": "api.ribaoapi.com",
    "Cookie": "d_ticket=a706138bd0b723461a61380db690e82a07d02; odin_tt=b8c25a7ca2d6230a0d921425e4d4753477ad0590b016d2508a67e834af32ae445fd6aff17b737783a3ae3f3d0e3e259282a1634fff3009101bc62b51931ced92; sid_guard=2701e191636e1853e1785b4648783c3c%7C1601115548%7C5184000%7CWed%2C+25-Nov-2020+10%3A19%3A08+GMT; uid_tt=f249d37500a1aa64e439a06cdb719b66; sid_tt=2701e191636e1853e1785b4648783c3c; sessionid=2701e191636e1853e1785b4648783c3c",
    "x-ss-cookie": "d_ticket=a706138bd0b723461a61380db690e82a07d02; odin_tt=b8c25a7ca2d6230a0d921425e4d4753477ad0590b016d2508a67e834af32ae445fd6aff17b737783a3ae3f3d0e3e259282a1634fff3009101bc62b51931ced92; sessionid=2701e191636e1853e1785b4648783c3c; sid_guard=2701e191636e1853e1785b4648783c3c%7C1601115548%7C5184000%7CWed%2C+25-Nov-2020+10%3A19%3A08+GMT; sid_tt=2701e191636e1853e1785b4648783c3c; uid_tt=f249d37500a1aa64e439a06cdb719b66",
    "tt-request-time": "1601115636352",
    "user-agent": "Super 1.1.0 rv:1.1.0.6 (iPhone; iOS 13.5.1; zh_CN) Cronet",
}

熟人志 = "https://is.snssdk.com/bds/user/publish_list/?iid=2374555398325096&resolution=1242*2208&os_version=13.5.1&app_name=super&channel=App%20Store&idfa=1ABF0A44-4CBE-4191-B8E6-154836171658&device_platform=iphone&mac_address=02:00:00:00:00:00&vid=86A0335D-BB60-42CC-A461-72D1D67C6DE1&openudid=01942689b4d6f20e58ba3abb334a86fcf32d187c&device_type=iPhone%207%20Plus&idfv=86A0335D-BB60-42CC-A461-72D1D67C6DE1&version_code=3.0.6&ac=WIFI&device_id=2673605010266535&aid=1319&update_version_code=30680&count=20&user_id=1947990820141172&api_version=1&direction=1"
ss = "https://is.snssdk.com/bds/user/user_profile/?iid=2374555398325096&resolution=1242*2208&os_version=13.5.1&app_name=super&channel=App%20Store&idfa=1ABF0A44-4CBE-4191-B8E6-154836171658&device_platform=iphone&mac_address=02:00:00:00:00:00&vid=86A0335D-BB60-42CC-A461-72D1D67C6DE1&openudid=01942689b4d6f20e58ba3abb334a86fcf32d187c&device_type=iPhone%207%20Plus&idfv=86A0335D-BB60-42CC-A461-72D1D67C6DE1&version_code=3.0.6&ac=WIFI&device_id=2673605010266535&aid=1319&update_version_code=30680&user_id=1226655901687588"
url2 = "https://is.snssdk.com/bds/ward/list/?iid=2374555398325096&resolution=1242*2208&os_version=13.5.1&app_name=super&channel=App%20Store&idfa=1ABF0A44-4CBE-4191-B8E6-154836171658&device_platform=iphone&mac_address=02:00:00:00:00:00&vid=86A0335D-BB60-42CC-A461-72D1D67C6DE1&openudid=01942689b4d6f20e58ba3abb334a86fcf32d187c&device_type=iPhone%207%20Plus&idfv=86A0335D-BB60-42CC-A461-72D1D67C6DE1&version_code=3.0.6&ac=WIFI&device_id=2673605010266535&aid=1319&update_version_code=30680&user_id=179942927110947&count=20"
loadmore = "https://is.snssdk.com/bds/user/publish_list/?iid=2374555398325096&resolution=1242*2208&os_version=13.5.1&app_name=super&channel=App%20Store&idfa=1ABF0A44-4CBE-4191-B8E6-154836171658&device_platform=iphone&mac_address=02:00:00:00:00:00&vid=86A0335D-BB60-42CC-A461-72D1D67C6DE1&openudid=01942689b4d6f20e58ba3abb334a86fcf32d187c&device_type=iPhone%207%20Plus&idfv=86A0335D-BB60-42CC-A461-72D1D67C6DE1&version_code=3.0.6&ac=WIFI&device_id=2673605010266535&aid=1319&update_version_code=30680&count=20&user_id=1947990820141172&api_version=1&direction=2&cursor=1600863792251060"

chayan="https://is.snssdk.com/bds/ward/list/?iid=2374555398325096&resolution=1242*2208&os_version=13.5.1&app_name=super&channel=App%20Store&idfa=1ABF0A44-4CBE-4191-B8E6-154836171658&device_platform=iphone&mac_address=02:00:00:00:00:00&vid=86A0335D-BB60-42CC-A461-72D1D67C6DE1&openudid=01942689b4d6f20e58ba3abb334a86fcf32d187c&device_type=iPhone%207%20Plus&idfv=86A0335D-BB60-42CC-A461-72D1D67C6DE1&version_code=3.0.6&ac=WIFI&device_id=2673605010266535&aid=1319&update_version_code=30680&user_id=179942927110947&count=20"

熟人志_ruibao="https://api.ribaoapi.com/bds/user/userfeed/?iid=3993043734112957&resolution=1242*2208&app_name=super&channel=App%20Store&device_platform=iphone&idfa=1ABF0A44-4CBE-4191-B8E6-154836171658&vid=16669D53-CE1F-4081-991A-1EDCD1888DE8&openudid=be5d560c284b36c0aedb650d91fcc14095e13e7e&device_type=iPhone%207%20Plus&idfv=16669D53-CE1F-4081-991A-1EDCD1888DE8&device_id=2673605010266535&ac=WIFI&version_code=1.1.0&os_version=13.5.1&aid=1319&user_id=1947990820141172&direction=1&list_type=0&mas=006b9eea5975a8c0fe6f58723f45299caf0e3dce0d1eb24f98e792&as=a2b522b715b70fad601880&ts=1601187189"
健康观察_ruibao="https://api.ribaoapi.com/bds/user/userfeed/?iid=3993043734112957&resolution=1242*2208&app_name=super&channel=App%20Store&device_platform=iphone&idfa=1ABF0A44-4CBE-4191-B8E6-154836171658&vid=16669D53-CE1F-4081-991A-1EDCD1888DE8&openudid=be5d560c284b36c0aedb650d91fcc14095e13e7e&device_type=iPhone%207%20Plus&idfv=16669D53-CE1F-4081-991A-1EDCD1888DE8&device_id=2673605010266535&ac=WIFI&version_code=1.1.0&os_version=13.5.1&aid=1319&user_id=1226655901687588&direction=1&list_type=0&mas=009bae225a491d2a97e5ee57918909e84278b086c933e9db0729af&as=a205724747e20f8ec03339&ts=1601187367"
class RequestSpider(object):
    def __init__(self):
        url = 健康观察_ruibao
        self.response = requests.get(url, headers=headers2)

    def run(self):
        print("text" + self.response.text)
        data = self.response.content
        print(data)

        # 1.获取请求头
        request_headers = self.response.request.headers
        print(request_headers)

        # 2.获取相应头
        coderesponse_headers = self.response.headers
        print(coderesponse_headers)

        # 3.响应状态码
        code = self.response.status_code
        print(code)

        # 4. 请求的cookie 注意写法
        request_cookie = self.response.request._cookies
        print(request_cookie)

        # 5. 响应的cookie
        response_cookie = self.response.cookies
        print(response_cookie)


RequestSpider().run()
