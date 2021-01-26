
import os
#获取目录下文件名清单
files = os.listdir("/Users/chengkun/Downloads/2020-06-08")
#对文件名清单里的每一个文件名进行处理
for filename in files:
    portion = os.path.splitext(filename)#portion为名称和后缀分离后的列表
    if portion[1] ==".m4s":#如果为JPG则更改名字
        newname = portion[0]+".mp3"#要改的新后缀#改好的新名字
        print(filename)#打印出要更改的文件名
        os.chdir("/Users/chengkun/Downloads/2020-06-08")#修改工作路径
        os.rename(filename,newname)
