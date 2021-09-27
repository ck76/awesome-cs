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
# TODO 有问题
# html_path = "/Users/chengkun/workspace/iBook/语言学/日语/芥末语法1-792/"
html_path="/Users/chengkun/Downloads/托福/语言学/日语/芥末语法1-792/"
json_list = os.listdir("./json/")


def all():
    with open("jlpt.md", 'w') as code:
        count = 0
        print(json_list)
        for json_item in json_list:
            # if count == 1:
            #     break
            code.write("[TOC]")
            code.write("\n")
            n1_json = open("./json/" + json_item).read()
            n1 = json.loads(n1_json)
            print(n1)
            data = n1.get("data")
            print(data[0].get("level"))
            level = data[0].get("level")
            code.write("### " + level)
            code.write("\n")
            count = count + 1
            for item in data:
                # print(item.get("id"))
                title = item.get("title")
                code.write("#### " + title)
                code.write("\n")
                print(title)
                grammerList = item.get("grammerList")
                for grammer_item in grammerList:
                    grammar = grammer_item.get("grammar")
                    grammer_id = grammer_item.get("id")
                    print(grammer_id)
                    parse_html = etree.parse(html_path + str(grammer_id) + ".html", etree.HTMLParser())
                    span_s = parse_html.xpath("//span/text()")
                    p_s = parse_html.xpath("//p/text()")
                    # ['语法内容', '解说', '接続', '例文', '注意点', ' 相关文法']
                    print(span_s)

                    print(p_s)
                    print(len(span_s))
                    print(len(p_s))
                    for i in range(0, len(span_s) - 1):
                        if span_s[i] == "语法内容":
                            code.write("##### " + p_s[0]
                                       .replace("\n", "")
                                       .replace("    ", "")
                                       .replace("                ", "")
                                       .replace("            ", "") + "\n")
                            code.write("\n")
                            continue
                        code.write("```c")
                        code.write("\n")
                        code.write("//" + span_s[i])
                        code.write("\n")
                        if span_s[i] == "例文":

                            code.write(
                                p_s[i]
                                .replace("\n", "")
                                .replace("    ", "")
                                .replace("                ", "")
                                .replace("            ", "")
                                .replace("／", "\n//") + "\n")
                            code.write(
                                p_s[i + 1]
                                .replace("\n", "")
                                .replace("    ", "")
                                .replace("                ", "")
                                .replace("            ", "")
                                .replace("／", "\n//") + "\n")

                        elif span_s[i] == "注意点":

                            code.write(
                                p_s[i + 1]
                                .replace("\n", "")
                                .replace("    ", "")
                                .replace("                ", "")
                                .replace("            ", "")
                                .replace("／", "\n//") + "\n")

                        else:

                            code.write(
                                p_s[i]
                                .replace("\n", "")
                                .replace("    ", "")
                                .replace("                ", "")
                                .replace("            ", "") + "\n")

                        code.write("```")
                        code.write("\n")
                        code.write("\n")


def ck(files):
    print(files)
    for item in files:
        file_name = item.split(".")[0]
        with open(file_name + ".md", "w") as code:
            print()
            count = 0
            # if count == 1:
            #     break
            code.write("[TOC]")
            code.write("\n")
            n1_json = open("./json/" + item).read()
            n1 = json.loads(n1_json)
            print(n1)
            data = n1.get("data")
            print(data[0].get("level"))
            level = data[0].get("level")
            code.write("### " + level)
            code.write("\n")
            count = count + 1
            for item in data:
                # print(item.get("id"))
                title = item.get("title")
                code.write("#### " + title)
                code.write("\n")
                print(title)
                grammerList = item.get("grammerList")
                for grammer_item in grammerList:
                    grammar = grammer_item.get("grammar")
                    grammer_id = grammer_item.get("id")
                    print(grammer_id)
                    parse_html = etree.parse(html_path + str(grammer_id) + ".html", etree.HTMLParser())
                    span_s = parse_html.xpath("//span/text()")
                    p_s = parse_html.xpath("//p/text()")
                    # ['语法内容', '解说', '接続', '例文', '注意点', ' 相关文法']
                    print(span_s)

                    print(p_s)
                    print(len(span_s))
                    print(len(p_s))
                    for i in range(0, len(span_s) - 1):
                        if span_s[i] == "语法内容":
                            code.write("##### " + p_s[0]
                                       .replace("\n", "")
                                       .replace("    ", "")
                                       .replace("                ", "")
                                       .replace("            ", "") + "\n")
                            code.write("\n")
                            continue
                        code.write("```c")
                        code.write("\n")
                        code.write("//" + span_s[i])
                        code.write("\n")
                        if span_s[i] == "例文":

                            code.write(
                                p_s[i]
                                .replace("\n", "")
                                .replace("    ", "")
                                .replace("                ", "")
                                .replace("            ", "")
                                .replace("／", "\n//") + "\n")
                            code.write(
                                p_s[i + 1]
                                .replace("\n", "")
                                .replace("    ", "")
                                .replace("                ", "")
                                .replace("            ", "")
                                .replace("／", "\n//") + "\n")

                        elif span_s[i] == "注意点":

                            code.write(
                                p_s[i + 1]
                                .replace("\n", "")
                                .replace("    ", "")
                                .replace("                ", "")
                                .replace("            ", "")
                                .replace("／", "\n//") + "\n")

                        else:

                            code.write(
                                p_s[i]
                                .replace("\n", "")
                                .replace("    ", "")
                                .replace("                ", "")
                                .replace("            ", "") + "\n")

                        code.write("```")
                        code.write("\n")
                        code.write("\n")


def all_label():
    print()
    with open("label.md", 'w') as code:
        count = 0
        print(json_list)
        for json_item in json_list:
            # if count == 1:
            #     break
            code.write("[TOC]")
            code.write("\n")
            n1_json = open("./json/" + json_item).read()
            n1 = json.loads(n1_json)
            print(n1)
            data = n1.get("data")
            print(data[0].get("level"))
            level = data[0].get("level")
            code.write("### " + level)
            code.write("\n")
            count = count + 1
            for item in data:
                # print(item.get("id"))
                title = item.get("title")
                code.write("#### " + title)
                code.write("\n")
                print(title)
                grammerList = item.get("grammerList")
                for grammer_item in grammerList:
                    grammar = grammer_item.get("grammar")
                    grammer_id = grammer_item.get("id")
                    print(grammer_id)
                    parse_html = etree.parse(html_path + str(grammer_id) + ".html", etree.HTMLParser())
                    span_s = parse_html.xpath("//span/text()")
                    p_s = parse_html.xpath("//p/text()")
                    # ['语法内容', '解说', '接続', '例文', '注意点', ' 相关文法']



ck(json_list)
# all_label()

# all()
"""
### N1

#### 伴随、非伴随

##### **~かたがた**

```c
//接续
N+かたがた
```

```c
//解说
表示某行为兼具两个目的。“顺便……”。
```

```c
//例文
①散歩かたがた駅前の本屋に行きました。
  ／散步的时候顺便去了趟车站附近的书店。
②先生が引っ越したというので、挨拶かたがたお菓子を持ってお宅を訪問することにした。
  ／听说老师搬家了，我决定去问候一下老师，带了些点心去老师家拜访。
```

```c
//注意点
①是较为正式的表达，与「～を兼ねて」相同。
②通常与「お見舞い」「ご挨拶」「お礼」「お詫び」等词连用。
```
"""
