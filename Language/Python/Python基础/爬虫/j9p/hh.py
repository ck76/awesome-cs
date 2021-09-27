# http://www.j9p.com/class/182_11.html【互联网科技】
# http://www.j9p.com/class/183_35.html【文学艺术】
# http://www.j9p.com/class/184_19.html【经济管理】
# http://www.j9p.com/class/185_13.html【社会科学】
# http://www.j9p.com/class/187_12.html【文化历史】
# http://www.j9p.com/class/188_21.html【教程资料】
# http://www.j9p.com/class/189_34.html【生活百科】
# http://www.j9p.com/class/190_8.html【教育相关】
#
import os
from urllib import request
from urllib.error import HTTPError
from urllib.parse import parse_qs, urlparse

from lxml import etree

disk_url = "/Users/chengkun/workspace/j9p.com/"

base_addr = "http://www.j9p.com/class/"
enter_command = "\n"


def download_catalog(leibie, page_count, category):
    herf_result = []
    address_result = []
    fail_result = []
    for page in range(1, page_count + 1):
        url = base_addr + str(leibie) + "_" + str(page) + ".html"
        print(url)
        parse_html = etree.parse(url, etree.HTMLParser())
        herf = parse_html.xpath("//ul[@class='slist tabcon']//li[@class='item']/a/@href")
        print(herf)
        # print(type(herf))
        for item in herf:
            herf_result.append(item)

    for herf_item in herf_result:
        link = "http://www.j9p.com/" + herf_item
        parse_html = etree.parse(link, etree.HTMLParser())
        # TODO 链接 <ul class="ul_Address"><script type="text/javascript" src="/inc/downLoad.asp?Address=tetjsxnx%2Ezip&TypeID=1&SoftLinkID=15732&SoftID=524538"></script></ul>
        ul_Address = parse_html.xpath("//ul[@class='ul_Address']/script/@src")
        book_name = parse_html.xpath("//h1/text()")

        if len(book_name) < 1:
            print("失败" + "link:" + link)
            fail_result.append(link)
            continue
        if len(ul_Address) < 1:
            print("失败" + "link:" + link)
            fail_result.append(link)
            continue
        print(ul_Address[0])
        query_result = urlparse(ul_Address[0]).query
        query_address = parse_qs(query_result).get("Address")
        pdf_Address = "http://jxz1.j9p.com/pc/" + query_address[0]
        zip_or_pdf = pdf_Address.split(".")[3] == "zip"
        print(pdf_Address)
        address_result.append(book_name[0] + "#" + pdf_Address)

        save_to_dic = disk_url + str(category) + "/"
        save_to_dic_lists = os.listdir(save_to_dic)
        save_to_dic_names = []
        for item in save_to_dic_lists:
            file_name = item.split(".")[0]
            save_to_dic_names.append(file_name)
        result_book_name = save_to_dic + book_name[0]
        # TODO 下载
        if book_name[0] in save_to_dic_names:
            print("  已存在" + book_name[0])
            continue
        try:
            f = request.urlopen(pdf_Address)
            data = f.read()
            # 存储位置可自定义
            if zip_or_pdf:
                with open(result_book_name + ".zip", 'wb') as code:
                    code.write(data)
            else:
                with open(result_book_name + ".pdf", 'wb') as code:
                    code.write(data)
        except HTTPError:
            print("HTTPError")
            print("失败" + "link:" + link)
            fail_result.append(link)
        except FileNotFoundError:
            print("FileNotFoundError")
            print("失败" + "link:" + link)
            fail_result.append(link)


    with open(str(category) + "目录.txt", 'w') as fout:
        for item in address_result:
            fout.writelines(item)
            fout.writelines(enter_command)
    with open(str(category) + "失败目录.txt", 'w') as fout:
        for item in fail_result:
            fout.writelines(item)
            fout.writelines(enter_command)


# download_catalog(182, 11, "互联网科技")
# download_catalog(183, 35, "文学艺术")
# download_catalog(184, 19, "经济管理")
# download_catalog(185, 13, "社会科学")
# download_catalog(187, 12, "文化历史")
# download_catalog(188, 21, "教程资料")
# download_catalog(189, 34, "生活百科")
# download_catalog(190, 8, "教育相关")
