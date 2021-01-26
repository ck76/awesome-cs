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

dengji = {"n1": {"伴随・非伴随": []}}
leibie = {"伴随・非伴随": {"n1": []}}

n1_json = open("./json/" + "n5.json").read()
n1 = json.loads(n1_json)
print(n1)
print(n1.get("data")[17].get("grammerList")[0].get("grammar_link"))
parse_html = etree.parse("html/" + str(792) + ".html", etree.HTMLParser())
span_s = parse_html.xpath("//span/text()")
p_s = parse_html.xpath("//p/text()")
print(span_s)
print(p_s)

for item in p_s:
    text = item.replace("    ", "").replace("                ", "").replace("            ", "")
    print(text)
# all_ele = parse_html.xpath("//div[@class='grammar-content']//*")
# print(len(all_ele))
# count = 0
# lenth = len(all_ele)
# haha = {}
# for i in range(0, len(all_ele)):
#     item = all_ele[i]
#     print(item.tag)
#     content = []
#     if item.text == "相关文法":
#         break
#     if item.tag == "span":
#         current = i + 1
#         if current>=len(all_ele):
#             continue
#         while all_ele[current].tag != "span":
#             if current >= len(all_ele)-1:
#                 break
#             print()
#             if all_ele[current].tag=="p":
#                 text=all_ele[current].text
#                 content.append(text)
#             current=current+1
#         haha[item.text] = content
#
#     # print(str(count)+"   "+str(item.tag)+"   "+item.text)
#     count = count + 1
#
# print(haha)
# print(len(all_ele))
