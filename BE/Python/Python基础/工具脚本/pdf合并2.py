# 更改python的当前工作路径
import os

# 显示当前脚本所在目录
print(os.getcwd())
# 将脚本所在目录设为工作目录
os.chdir(os.getcwd())

import sys
from PyPDF2 import PdfFileWriter, PdfFileReader,PdfFileMerger

filenames = os.listdir()
print("---------------------------------------------")
merger = PdfFileMerger()

outputPages = 0

# 主程序，合成目录内所有PDF文件
for filename in filenames:
    # 跳过此脚本文件
    if (filename[-3:] == ".py"):
        continue
    if (filename == '.DS_Store'):
        continue
    if (filename[-3:] == '.md'):
        continue
    print(filename)
    try:
        input = PdfFileReader(open(filename, "rb"))
    except:
        print(filename + '错误')
    merger.append(input)

merger.write(open("merge.pdf", "wb"))
