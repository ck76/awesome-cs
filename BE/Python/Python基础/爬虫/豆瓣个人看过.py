# -*-coding=UTF-8 -*-

import requests
from bs4 import BeautifulSoup

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36',
    'Host': 'movie.douban.com'}
movie_list = {}

for i in range(0, 4):
    link = 'https://movie.douban.com/top250?start=' + str(i * 25) + '&filter='
    r = requests.get(link, headers=headers, timeout=10)
    print(str(i + 1), 'states:', r.status_code)
    # print(r.text)
    soup = BeautifulSoup(r.text, "lxml")
    div_list = soup.find_all('div', class_="info")

    for each in div_list:
        name = each.div.a.span.text.strip()
        info = each.p.text.strip()

        movie_list[name] = info

return movie_list

movies = get_movies()

with open('douban.txt', 'w', encoding='utf-8') as f:
    for k in movies:
        f.write(str('\n' + k + ' :: ' + movies[k] + '\n\n' + '-------------------------' + '\n\n'))
    f.close()
    print('Finished!!!')
