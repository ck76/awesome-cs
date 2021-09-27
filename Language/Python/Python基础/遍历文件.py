
import os
#获取目录下文件名清单
from PyPDF2 import PdfFileMerger

merger = PdfFileMerger()

files = os.listdir("/Users/chengkun/workspace/iBook/pdf课件/语言学/语言学概论_北京联合大学")
#对文件名清单里的每一个文件名进行处理
for filename in files:
    # portion = os.path.splitext(filename)#portion为名称和后缀分离后的列表
    # if portion[1] ==".m4s":#如果为JPG则更改名字
    #     newname = portion[0]+".mp3"#要改的新后缀#改好的新名字
    #     print(filename)#打印出要更改的文件名
    #     os.chdir("/Users/chengkun/Downloads/2020-06-08")#修改工作路径
    #     os.rename(filename,newname)
    print(filename)

files.sort()
for filename in files:
    # portion = os.path.splitext(filename)#portion为名称和后缀分离后的列表
    # if portion[1] ==".m4s":#如果为JPG则更改名字
    #     newname = portion[0]+".mp3"#要改的新后缀#改好的新名字
    #     print(filename)#打印出要更改的文件名
    #     os.chdir("/Users/chengkun/Downloads/2020-06-08")#修改工作路径
    #     os.rename(filename,newname)
    print(filename)
    print(type(filename))
    # merger.append(filename)
    file = open(filename, "rb")
    merger.append(file)

# Write to an output PDF document
output = open("/Users/chengkun/workspace/iBook/pdf课件/语言学/语言学概论_北京联合大学/document-output.pdf", "wb")
merger.write(output)



