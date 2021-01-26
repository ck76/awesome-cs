# http://jxz1.j9p.com/pc/

# !/usr/bin/python
# -*- coding: UTF-8 -*-

from urllib.error import HTTPError

import pinyin
import os
import urllib.request


# save_to_path = "/Users/chengkun/workspace/j9p.com/"


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
    result = pinyin.get_initial(bookname, delimiter="")+"dzs"

    return result


# number = 1
# book_name = "ck"
# postfix = ".pdf"

# fail_files = []
#
# count = 1
# dir_files = os.listdir(save_to_path)
# num_dir_files = []
# mulu = open("儿童类.txt")
# lines = mulu.readlines()
# print(lines)
# print(type(lines))
# print(dir_files)
#
# for item in dir_files:
#     split = item.split("：", 1)
#     item = split[0]
#     num_dir_files.append(item)
# print(num_dir_files)
#
# for line in lines:
#     line = line.replace("\n", "")
#     result_name = save_to_path + str(line) + ".pdf"
#     num = line.split("：", 1)
#     if num[0] in num_dir_files:
#         print("yes")
#         continue
#     # print(line)
#     # count = count + 1
#     # if count > 30:
#     #     break
#     print(line)
#     url = "http://ds.addsxz.com/" + get_num_and_name(line) + ".pdf"
#     try:
#         f = urllib.request.urlopen(url)
#         data = f.read()
#         # 存储位置可自定义
#         with open(result_name, 'wb') as code:
#             code.write(data)
#     except HTTPError:
#         print(url)
#         fail_files.append(line)
#     except  UnicodeEncodeError:
#         print(url)
#         fail_files.append(line)
#
# with open(save_to_path + "儿童类失败的.txt", 'w') as code:
#     for line in fail_files:
#         code.write(str(line) + "\n")
#     code.close()
#     # code.write(data)


# for i in (1,10):

def download_pdf(save_to_path, mulu_name):
    fail_files = []

    count = 1
    dir_files = os.listdir(save_to_path)
    num_dir_files = []
    mulu = open("./目录/带序号/" + mulu_name + ".txt")
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
        result_name = save_to_path + str(line) + ".pdf"
        num = line.split("：", 1)
        if num[0] in num_dir_files:
            print("yes")
            continue
        # print(line)
        # count = count + 1
        # if count > 30:
        #     break
        print(line)
        url = "http://jxz1.j9p.com/pc/" + get_num_and_name(line) + ".pdf"
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

    with open(save_to_path + mulu_name + "失败.txt", 'w') as code:
        for line in fail_files:
            code.write(str(line) + "\n")
        code.close()
        # code.write(data)
    with open(save_to_path + "带序号" + mulu_name + "失败.txt", 'w') as code:
        for line in fail_files:
            code.write(str(line) + "\n")
        code.close()


download_pdf("/Users/chengkun/workspace/j9p.com/互联网科技/", "带序号互联网科技目录")
download_pdf("/Users/chengkun/workspace/j9p.com/教程资料/", "带序号教程资料目录")
download_pdf("/Users/chengkun/workspace/j9p.com/教育相关/", "带序号教育相关目录")
download_pdf("/Users/chengkun/workspace/j9p.com/文化历史/", "带序号文化历史目录")
download_pdf("/Users/chengkun/workspace/j9p.com/文学艺术/", "带序号文学艺术目录")
download_pdf("/Users/chengkun/workspace/j9p.com/生活百科/", "带序号生活百科目录")
download_pdf("/Users/chengkun/workspace/j9p.com/社会科学/", "带序号社会科学目录")
download_pdf("/Users/chengkun/workspace/j9p.com/经济管理/", "带序号经济管理目录")
