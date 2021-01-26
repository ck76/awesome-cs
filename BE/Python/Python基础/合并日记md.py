import os
import re

daliy_path = "/Users/chengkun/Documents/Blog/生活/Daily/"
os.chdir(daliy_path)
dirs = os.listdir()
print(str(len(dirs)) + " " + str(dirs))
dirs.remove(".DS_Store")
dirs.sort()
print(str(len(dirs)) + " " + str(dirs))
contents = []
for year in range(0, len(dirs)):
    dir_name = dirs[year]
    dir_path = daliy_path + dir_name
    portion = os.path.splitext(dir_name)
    if portion[1] != "":
        continue
    print(year)
    os.chdir(dir_path)
    files = os.listdir()
    for filename in sorted(files):
        portion = os.path.splitext(filename)  # portion为名称和后缀分离后的列表
        print(portion)
        if portion[1] != ".md":  # 如果为JPG则更改名字
            continue
        with open(filename, 'r') as f:
            contents.append(f.read() + "\n")

#              替换掉其中的[TOC]
os.chdir(daliy_path)

# contents_lines=str(contents).splitlines("\n")
# contents_lines.remove("[TOC]")
# print(contents_lines)
with open("result.md", "w") as f:
    content=re.sub(r'[TOC]', "", str(contents))
    f.writelines(content)


# lineList = []
# matchPattern = re.compile(r'[TOC]')
# file = open('result.md', 'r', encoding='UTF-8')
# while 1:
#     line = file.readline()
#     if not line:
#         print("Read file End or Error")
#         break
#     elif matchPattern.search(line):
#         pass
#     else:
#         lineList.append(line)
# file.close()
# file = open(r'result.md', 'w', encoding='UTF-8')
# for i in lineList:
#     file.write(i)

