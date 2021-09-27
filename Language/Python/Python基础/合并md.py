import os

os.chdir("/Users/chengkun/workspace/iBook/李笑来/regular-investing-in-box/Translations/English")
files = os.listdir()
contents = []
for filename in sorted(files):
    portion = os.path.splitext(filename)  # portion为名称和后缀分离后的列表
    print(portion)
    if portion[1] != ".md":  # 如果为JPG则更改名字
        continue
    with open(filename, 'r') as f:
        contents.append(f.read() + "\n")

with open("result.md", "w") as f:
    f.writelines(contents)


