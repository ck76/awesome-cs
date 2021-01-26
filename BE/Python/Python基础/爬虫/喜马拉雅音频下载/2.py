# https://blog.csdn.net/weixin_44000328/article/details/84868703
import json
import os
import re
import requests


def xima():
    # 模拟浏览器
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36"
    }
    # 拿到XX排行榜的所有关键字的url
    url_1 = "https://www.ximalaya.com/revision/getRankCluster"
    # 利用requests解析来得到源代码, 得到一个JSON类型的字符串
    json_1 = requests.get(url_1, headers=headers).content.decode()
    # 通过json模块来转换成Python的字典
    dict_1 = json.loads(json_1)
    # 从字典里面把上面写的XX排行的的关键字拿出来
    name_1 = dict_1['data']['list']
    for i in name_1:
        name = i['name']  # 终于拿到了
        print(name)
        # 就可以跟这个url拼接, 得到的url里面有所有书的id, 和名字
        url_2 = "https://www.ximalaya.com/revision/getRankList?code=" + name
        # 还是一样解析得到一个JSON数据
        json_2 = requests.get(url_2, headers=headers).content.decode()
        # 依然通过转换得到字典
        dict_2 = json.loads(json_2)
        # 从字典里面取到一个个的id和对应的名字
        for j in dict_2['data']['albums']:
            id_2 = j['id']
            title = j['albumTitle']
            title = re.sub('\?|"|\|', '', title)  # 因为有的名字里面有通配符, 所以得换成空
            if not os.path.exists(title):
                os.mkdir(title)  # 创建文件夹, 方便待会把这本书的所有音频存在进去
            # 有了id我们就可以进行拼接了, 这个链接里面就有每个音频的url. 但是有很多页, 所以我们得使用格式化点位符拼接得到每一页的url
            url_3 = "https://www.ximalaya.com/revision/play/album?albumId=" + str(
                id_2) + "&pageNum={}&sort=-1&pageSize=30"
            for i in range(50):
                url = url_3.format(i + 1)  # 循环拼接成不同页的url
                try:
                    # 得到每一次的源代码, JSON类型
                    json_3 = requests.get(url, headers=headers).content.decode()
                except Exception as e:
                    print(e)  # 因为我们循环了50次, 而有的书根本没有那么多页, 所有得try一下跳出循环
                    continue
                # 又一次进行转换得到字典
                dict_3 = json.loads(json_3)
                n = 1
                # 终于可以从字典里面拿到音频的url了, 还有对应的名字
                for k in dict_3['data']['tracksAudioPlay']:
                    src = k['src']
                    name = k['trackName']
                    print(src, name)
                    name = re.sub('\?|"|\|', '', name)  # 因为有的名字里面有通配符, 所以得换成空
                    # 给每一个音频拼接名字,
                    with open(title + '/' + str(i * 30 + n) + '%s.m4a' % name, 'ab') as f:
                        r = requests.get(src, headers=headers)
                        ret = r.content
                        # 获取到音频的二进制文件保存起来才是音频文件
                        f.write(ret)
                    n += 1


if __name__ == '__main__':
    xima()


