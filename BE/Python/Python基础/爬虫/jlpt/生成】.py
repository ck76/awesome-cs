file1 = open("/Users/chengkun/workspace/Blog/语言学/jlpt语法按类别的副本.md", "r")
lines = file1.readlines()
result = []
for item in lines:
    if item.startswith("#"):
        item = item.replace("\n", "") + "】" + "\n"
    result.append(item)

with open("/Users/chengkun/workspace/Blog/语言学/yy.md", "w") as file:
    for item in result:
        file.write(item)

# file1.writelines(lines)
