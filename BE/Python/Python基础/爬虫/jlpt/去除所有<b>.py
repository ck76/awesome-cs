import os

path = "/Users/chengkun/workspace/iBook/语言学/日语/芥末语法1-792+"
os.chdir(path)
files = os.listdir()
for file in files:
    print(file)
    content = []
    for line in open(file).readlines():
        line_no_b = line.replace("<br>", "")
        content.append(line_no_b)
    with open("/Users/chengkun/workspace/iBook/语言学/日语/芥末语法1-792++/" + file, "w") as out:
        print("/Users/chengkun/workspace/iBook/语言学/日语/芥末语法1-792++/" + file)
        for line in content:
            # print(line)
            out.writelines(line)
