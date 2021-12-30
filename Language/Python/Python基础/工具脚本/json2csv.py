import json
import os

# https://konklone.io/json/


#获取目录下文件名清单
dir = "/Users/chengkun/Downloads/json/"
files = os.listdir(dir)
json_result = []
#对文件名清单里的每一个文件名进行处理
for filename in files:
    # portion = os.path.splitext(filename)#portion为名称和后缀分离后的列表
    portion = filename.split('.')
    print(filename)#打印出要更改的文件名
    id = portion[0]

    with open(dir+filename, 'r') as load_f:
        json_content = json.load(load_f)
        json_content["labels"][0]["id"] = id
        print(json_content)
        json_result.append(json_content["labels"][0])

with open("/Users/chengkun/Downloads/jsonResult/result.json", "w+") as fout:
    fout.write(str(json_result))
    fout.close()