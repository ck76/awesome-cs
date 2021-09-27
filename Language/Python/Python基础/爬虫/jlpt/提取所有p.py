import json

# 1-207     1-31
# 208-362   32-64
# 363-521   65-90
# 522-640   91-119
# 641-793   120-137 666 -794-667

#
import os
import requests
import urllib
from lxml import etree
import os
# TODO 正解
from lxml.etree import Element

path = "/Users/chengkun/Downloads/托福/语言学/日语/芥末语法1-792++/"
mulu = ["语法内容", "解说", "接続", "例文", "注意点"]

all_p = dict()
all_p.keys()
result = []
for item in all_p:
    tag = ""
    if item in mulu:
        tag = item
for i in range(1, 795):
    all_p[i] = dict()

for i in range(1, 795):
    kari = dict()
    kari_texts = []
    current_title = ""
    current_p_text = []
    html_path = path + str(i) + ".html"
    # parse_html = etree.HTML(r.text)
    parse_html = etree.parse(html_path, etree.HTMLParser())
    element_s = parse_html.xpath("//div[@class='grammar-content']//*")
    # 进行一次循环，完成一个html页面的提取

    for element in element_s:
        if element.tag == "span":
            # 清空操作
            current_title = element.text
            current_p_text = []
            if current_title in kari.keys():
                pass
            else:
                kari[current_title] = []

        if element.tag == "p":
            kari[current_title].append(element.text
                                       .replace("\n                ", "")
                                       .replace("            ", "")
                                       .replace("    ", "")
                                       # .replace("／", "\n//")
                                       .replace("②", "\n②")
                                       .replace("③", "\n③")
                                       .replace("④", "\n④"))
    all_p[str(i)] = kari


# print(json.dumps(all_p, ensure_ascii=False, indent=4))
# print(all_p)


def an_N1_N5():
    json_list = os.listdir("./json/")
    with open("jlpt语法按等级.md", 'w') as code:
        count = 0
        for json_item in json_list:
            # if count == 1:
            #     break
            code.write("[TOC]")
            code.write("\n")
            n1_json = open("./json/" + json_item).read()
            n1 = json.loads(n1_json)
            data = n1.get("data")
            # print(data[0].get("level"))
            level = data[0].get("level")
            code.write("### " + level)
            code.write("\n")
            count = count + 1
            for item in data:
                # print(item.get("id"))
                title = item.get("title")
                code.write("#### " + title)
                code.write("\n")
                grammerList = item.get("grammerList")
                for grammer_item in grammerList:
                    grammar = grammer_item.get("grammar")
                    code.write("##### " + grammar + "\n")
                    code.write("```c\n")
                    grammer_id = grammer_item.get("id")
                    grammar_s = all_p[grammer_id]
                    for mulu_line in mulu:
                        if mulu_line in grammar_s.keys() and mulu_line!="语法内容":
                            code.write("【" + mulu_line + "】" + "\n")
                            content_s = grammar_s[mulu_line]
                            for haha in content_s:
                                if mulu_line == "例文":
                                    code.write(haha.replace("／", "\n//") + "\n")
                                else:
                                    code.write(haha + "\n")

                    code.write("```\n")
                    code.write("\n")


n1_n5 = ["N1", "N2", "N3", "N4", "N5"]
n1_n5_grammer = {"N1": [], "N2": [], "N3": [], "N4": [], "N5": []}  # TODO 根源处在这
all_leibie = {}

id_and_name = {}
json_list = os.listdir("./json/")
with open("jlpt语法按类别.md", 'w') as code:
    for json_item in json_list:
        n1_json = open("./json/" + json_item).read()
        n1 = json.loads(n1_json)
        data = n1.get("data")
        for data_item in data:
            grammerList = data_item.get("grammerList")
            for grammer_item in grammerList:
                id = grammer_item.get("id")
                grammer = grammer_item.get("grammar")
                id_and_name[id] = grammer

print(id_and_name)
def an_leibie():
    count = 0  # 137----73
    json_list = os.listdir("./json/")
    with open("jlpt语法按类别.md", 'w') as code:
        for json_item in json_list:
            n1_json = open("./json/" + json_item).read()
            n1 = json.loads(n1_json)
            data = n1.get("data")
            for data_item in data:
                grammerList = data_item.get("grammerList")
                for grammer_item in grammerList:
                    category = grammer_item["category"]
                    all_leibie[str(category)] = {}
                    haha = all_leibie[str(category)]
                    haha["N1"] = []
                    haha["N2"] = []
                    haha["N3"] = []
                    haha["N4"] = []
                    haha["N5"] = []

        for json_item in json_list:
            n1_json = open("./json/" + json_item).read()
            n1 = json.loads(n1_json)
            data = n1.get("data")
            for data_item in data:
                grammerList = data_item.get("grammerList")
                for grammer_item in grammerList:
                    id = grammer_item.get("id")
                    level = grammer_item.get("level")
                    category = grammer_item["category"]
                    # TODO 为什么dict会复用？？？？？？？
                    grammer_dict = all_leibie[category]
                    grammer_list = grammer_dict[level]
                    grammer_list.append(id)

        code.write("[TOC]\n")
        for title in all_leibie.keys():
            code.write("### " + title + "\n")
            for level in all_leibie[title]:  # 比较・程度
                if len(all_leibie[title][level]) == 0:
                    continue
                code.write("#### " + level + "\n")  # N1
                for grammer_id in all_leibie[title][level]:
                    grammer_name=id_and_name[grammer_id]
                    code.write("##### " + grammer_name + "\n")
                    code.write("```c\n")
                    grammar_s = all_p[grammer_id]
                    for mulu_line in mulu:
                        if mulu_line in grammar_s.keys() and mulu_line != "语法内容":
                            code.write("【" + mulu_line + "】" + "\n")
                            content_s = grammar_s[mulu_line]
                            for haha in content_s:
                                if mulu_line == "例文":
                                    code.write(haha.replace("／", "\n//") + "\n")
                                else:
                                    code.write(haha + "\n")

                    code.write("```\n")
                    code.write("\n")


an_N1_N5()

an_leibie()
# print(json.dumps(all_leibie, ensure_ascii=False, indent=4))
# print(all_leibie)
# print(all_leibie.keys().__len__())
