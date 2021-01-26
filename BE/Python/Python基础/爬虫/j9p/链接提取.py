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

import requests
from lxml import etree
from urllib.parse import parse_qs

base_addr = "http://www.j9p.com/class/"
enter_command = "\n"


def download_catalog(leibie, page_count, name):
    herf_result = []
    address_result = []
    for page in range(1, page_count + 1):
        url = base_addr + str(leibie) + "_" + str(page) + ".html"
        print(url)
        parse_html = etree.parse(url, etree.HTMLParser())
        herf = parse_html.xpath("//ul[@class='slist tabcon']//li[@class='item']/a/@href")
        print(herf)
        for item in herf:
            herf_result.append(item)

    for herf_item in herf_result:
        link = "http://www.j9p.com/down/" + herf_item
        parse_html = etree.parse(link, etree.HTMLParser())
        # TODO 链接 <ul class="ul_Address"><script type="text/javascript" src="/inc/downLoad.asp?Address=tetjsxnx%2Ezip&TypeID=1&SoftLinkID=15732&SoftID=524538"></script></ul>
        ul_Address = parse_html.xpath("//ul[@class='ul_Address']/script/@src")
        pdf_Address = "http://jxz1.j9p.com/pc/" + parse_qs(ul_Address.query).get("Address")
        print(pdf_Address)
        address_result.append(pdf_Address)

    with open(str(name) + "目录.txt", 'w') as fout:
        for item in address_result:
            fout.writelines(item)
            fout.writelines(enter_command)


# download_catalog(182, 11, "互联网科技")
download_catalog(183, 35, "文学艺术")
download_catalog(184, 19, "经济管理")
download_catalog(185, 13, "社会科学")
download_catalog(187, 12, "文化历史")
download_catalog(188, 21, "教程资料")
download_catalog(189, 34, "生活百科")
download_catalog(190, 8, "教育相关")
