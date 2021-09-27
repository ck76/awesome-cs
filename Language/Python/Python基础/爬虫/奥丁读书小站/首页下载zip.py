#!/usr/bin/python
# -*- coding: UTF-8 -*-

from urllib.error import HTTPError

import pinyin
import os
import urllib.request

save_to_path = "/Users/chengkun/workspace/奥丁图书小站/首页/"


# TODO :和（ 先解决掉
# TODO 总共1162个
# str = "Line1-abcdef \nLine2-abc \nLine4-abcd";
# print(str.split())  # 以空格为分隔符，包含 \n
#
# print(str.split(' ', 1))  # 以空格为分隔符，分隔成两个
#
# filename = "836：那不勒斯四部曲NO.1：我的天才女友》"
# first_split = filename.split("：", 1)
# print(first_split)
# second_split = first_split[1].split("》")
# print(second_split)


def get_num_and_name(bookname):
    # filename = "1591：最寒冷的冬天：美国人眼中的朝鲜战争"
    first_split = bookname.split("：", 1)
    # print(first_split)
    number = first_split[0]
    second_split = first_split[1].split("（", 1)
    if len(second_split) == 1:
        second_split = first_split[1].split("：", 1)
    bookname = second_split[0]
    # print(number)
    # print(bookname)
    # print(str(number) + pinyin.get_initial(bookname, delimiter=""))
    result = str(number) + pinyin.get_initial(bookname, delimiter="")

    return result


# number = 1
# book_name = "ck"
# postfix = ".zip"

fail_files = []

count = 1
dir_files = os.listdir(save_to_path)
num_dir_files = []
mulu = open("首页目录.txt")
lines = mulu.readlines()
print(lines)
print(type(lines))
print(dir_files)

for item in dir_files:
    split = item.split("：", 1)
    item = split[0]
    num_dir_files.append(item)
print(num_dir_files)

for line in lines:
    line = line.replace("\n", "")
    result_name = save_to_path + str(line) + ".zip"
    num = line.split("：", 1)
    if num[0] in num_dir_files:
        print("yes")
        continue
    # print(line)
    # count = count + 1
    # if count > 30:
    #     break
    print(line)
    url = "http://ds.addsxz.com/" + get_num_and_name(line) + ".zip"
    try:
        f = urllib.request.urlopen(url)
        data = f.read()
        # 存储位置可自定义
        with open(result_name, 'wb') as code:
            code.write(data)
    except HTTPError:
        print(url)
        fail_files.append(line)
    except  UnicodeEncodeError:
        print(url)
        fail_files.append(line)

with open(save_to_path+"首页失败的zip.txt", 'w') as code:
    for line in fail_files:
        code.write(str(line) + "\n")
    code.close()
    # code.write(data)
# for i in (1,10):
