import ssl
import time

import requests
from lxml import etree

# https://gist.github.com/derhuerst/19e0844796fa3b62e1e9567a1dc0b5a3


ssl._create_default_https_context = ssl._create_unverified_context

first_url = "https://github.com/ck76?tab=stars"
headers = {
    # 'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36',
    # "cookie": "_octo=GH1.1.1956350209.1628238836; logged_in=yes; dotcom_user=ck76; color_mode=%7B%22color_mode%22%3A%22light%22%2C%22light_theme%22%3A%7B%22name%22%3A%22light%22%2C%22color_mode%22%3A%22light%22%7D%2C%22dark_theme%22%3A%7B%22name%22%3A%22dark_dimmed%22%2C%22color_mode%22%3A%22dark%22%7D%7D; tz=Asia%2FShanghai",
    # "accept-language": "zh-CN,zh;q=0.9",
    # "accept-encoding": "gzip, deflate, br",
    # "content-type:": "text/plain;charset=UTF-8",
    # "origin": "https://github.com",
    # "referer": "https://github.com",
}

count = 0

repository_urls_result = []
repository_result_prefix = "https://github.com"

page_urls = []
page_urls_result = []

file_name_page_urls = "file_name_page_urls.txt"
file_name_repository_urls = "file_name_repository_urls.txt"

last_request_url = ""


def init_page_urls():
    print("init_page_urls---------------------")
    with open(file_name_page_urls, 'r') as urls:
        for line in urls.readlines():
            line = line.replace("\n", "")
            page_urls.append(line)


def save_result():
    print("save_page_urls-----------------")
    with open(file_name_page_urls, "a+") as fout:
        for item in page_urls_result:
            fout.write(item + "\n")

    print("save_repository_urls-----------------")
    with open(file_name_repository_urls, "a+") as fout:
        for item in repository_urls_result:
            result = repository_result_prefix + item
            fout.write(result + "\n")


def add_last_request_url():
    print("last_request_url", last_request_url)
    all_page_urls = []
    with open(file_name_page_urls, 'r') as urls:
        for line in urls.readlines():
            line = line.replace("\n", "")
            all_page_urls.append(line)
    if not all_page_urls.__contains__(last_request_url):
        print("add_last_request_url------添加")
        with open(file_name_page_urls, "a+") as fout:
            fout.write(last_request_url + "\n")
    else:
        print("add_last_request_url------已经在了所以不添加")


def remove_duplicates():
    with open(file_name_repository_urls, "r") as fin:
        lines = fin.readlines()
        print("去重前仓库长度：", str(len(lines)))
        fin.close()

    r_repository_urls_result = []
    with open(file_name_repository_urls, "r") as fin:
        # print("去重前仓库长度：", str(len(fin.readlines())))
        for item in fin.readlines():
            item = item.replace("\n", "")
            if not r_repository_urls_result.__contains__(item):
                r_repository_urls_result.append(item)
        fin.close()
    print("去重后仓库长度：", str(len(r_repository_urls_result)))
    with open(file_name_repository_urls, "w+") as fout:
        for item in r_repository_urls_result:
            fout.write(item + "\n")
        fout.close()

    with open(file_name_page_urls, "r") as fin:
        lines = fin.readlines()
        print("去重前页面长度：", str(len(lines)))
        fin.close()
    r_page_urls_result = []
    with open(file_name_page_urls, "r") as fin:
        # print("去重前页面长度：", str(len(fin.readlines())))
        for item in fin.readlines():
            item = item.replace("\n", "")
            if not r_page_urls_result.__contains__(item):
                r_page_urls_result.append(item)
        fin.close()
    print("去重后页面长度：", str(len(r_page_urls_result)))
    with open(file_name_page_urls, "w+") as fout:
        for item in r_page_urls_result:
            fout.write(item + "\n")
        fout.close()


def get_stars():
    init_page_urls()
    try:
        global last_request_url
        first_page_key = page_urls[len(page_urls) - 1]
        print("请求开始：", first_page_key)
        last_request_url = first_page_key
        # r = requests.get(first_page_key, headers=headers, timeout=15)
        r = requests.get(first_page_key, headers=headers)
        #  r = requests.get(first_page_key,proxies={'http':'ip:port'})
        time.sleep(2)
        print("请求结束：", first_page_key)
        if r.status_code == 200:
            # 请求第一页返回第二页的key
            parse_html = etree.HTML(r.text)
            second_page_key_s = parse_html.xpath(
                "//div[@class='BtnGroup']//a[@class='btn btn-outline BtnGroup-item']/@href")
            content = parse_html.xpath(
                "//div[@class='BtnGroup']//a[@class='btn btn-outline BtnGroup-item']/text()")
            second_page_key = ""
            if len(second_page_key_s) == 1:
                print("长度1  ", second_page_key_s)
                second_page_key = second_page_key_s[0]
            elif len(second_page_key_s) == 2:
                print("长度2  ", second_page_key_s)
                print("second-content:", content)
                second_page_key = second_page_key_s[1]

            # TODO 仓库地址
            repository_urls = parse_html.xpath("//div[@class='d-inline-block mb-1']//a/@href")
            for item in repository_urls:
                repository_urls_result.append(item)
            print("添加仓库地址", repository_urls)

            # 请求第二页以后的页面直至最后
            print("请求开始：", second_page_key)
            last_request_url = second_page_key
            r = requests.get(second_page_key, headers=headers)
            time.sleep(2)
            print("请求结束：", second_page_key)

            if r.status_code == 200:
                page_urls_result.append(second_page_key)
                parse_html = etree.HTML(r.text)
                mid_page_key_s = parse_html.xpath(
                    "//div[@class='BtnGroup']//a[@class='btn btn-outline BtnGroup-item']/@href")
                content = parse_html.xpath(
                    "//div[@class='BtnGroup']//a[@class='btn btn-outline BtnGroup-item']/text()")
                print("mid-content:", content)
                # TODO 仓库地址
                repository_urls = parse_html.xpath("//div[@class='d-inline-block mb-1']//a/@href")
                for item in repository_urls:
                    repository_urls_result.append(item)
                print("添加仓库地址", repository_urls)

                while len(mid_page_key_s) > 1:
                    mid_page_key = mid_page_key_s[1]
                    print("请求开始：", mid_page_key)
                    last_request_url = mid_page_key
                    r = requests.get(mid_page_key, headers=headers)
                    time.sleep(2)
                    print("请求结束：", mid_page_key)

                    if r.status_code == 200:
                        page_urls_result.append(mid_page_key)
                        parse_html = etree.HTML(r.text)
                        mid_page_key_s = parse_html.xpath(
                            "//div[@class='BtnGroup']//a[@class='btn btn-outline BtnGroup-item']/@href")
                        # TODO 仓库地址
                        repository_urls = parse_html.xpath("//div[@class='d-inline-block mb-1']//a/@href")
                        for item in repository_urls:
                            repository_urls_result.append(item)
                        print("添加仓库地址", repository_urls)
                        # 11111111111
                        # global count
                        # count = count + 1
                        # if count == 2:
                        #     print("结束")
                        #     break

                # 请求最后一页
                last_page_key = mid_page_key_s[0]
                print("请求开始-最后一页：", last_page_key)
                last_request_url = last_page_key
                r = requests.get(last_page_key, headers=headers)
                print("请求结束-最后一页：", last_page_key)
                if r.status_code == 200:
                    page_urls_result.append(last_page_key)
                    parse_html = etree.HTML(r.text)
                    # TODO 仓库地址
                    repository_urls = parse_html.xpath("//div[@class='d-inline-block mb-1']//a/@href")
                    for item in repository_urls:
                        repository_urls_result.append(item)
                    print("添加仓库地址", repository_urls)
    except requests.exceptions.ConnectTimeout:
        print("卧槽！！！！！！！！  timeout llllll")
    except requests.exceptions.ReadTimeout:
        print("卧槽！！！！！！！！  read time out 11111")
    except requests.exceptions.ConnectionError:
        print("卧槽！！！！！！！！  connection Error 11111")
    except KeyboardInterrupt:
        print("卧槽！！！！！！！！  KeyboardInterrupt 11111")

    add_last_request_url()
    save_result()
    remove_duplicates()


get_stars()
