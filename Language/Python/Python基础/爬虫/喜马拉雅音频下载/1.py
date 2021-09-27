
# https://www.jianshu.com/p/53e89ced9edf
import requests
import re
import json
# http://www.ximalaya.com/tracks/66104267.json   json 的 url 格式，不同的只是 ID
# TODO https://www.ximalaya.com/gerenchengzhang/16059951/
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36'
}
def get_id(url):
    req = requests.get(url, headers=headers)
    result = req.text
    id_number = re.findall('sound_id="([\d]*?)"',result)
    id_number = set(id_number)  # 由于页面上有重复的 ID，故利用集合的属性去掉其重复的 ID
    id = []
    for number in id_number:
        id.append('http://www.ximalaya.com/tracks/' + number + '.json')  # 这样构造url是不太严谨的，当然在这里是可以的，以后再探讨 url 的构造方法
    return id

def download(url):
    req = requests.get(url,headers = hd)  # hd 为 user-agent
    result = req.text
    result = json.loads(result)
    title = result['title']
    data_url = result['play_path_64']
    data = requests.get(data_url).content
    with open('%s.m4a'%title,'wb') as f:
        f.write(data)

for url in get_id('https://www.ximalaya.com/gerenchengzhang/16059951/'):
    download(url)