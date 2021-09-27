# 更改python的当前工作路径
import os

# 显示当前脚本所在目录
print(os.getcwd())
# 将脚本所在目录设为工作目录
os.chdir(os.getcwd())

import sys
from PyPDF2 import PdfFileWriter, PdfFileReader

filenames = os.listdir()
filenames.sort()
print("---------------------------------------------")
output = PdfFileWriter()

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
    pageCount = input.getNumPages()
    outputPages += pageCount
    for iPage in range(0, pageCount):
        output.addPage(input.getPage(iPage))

output.write(open("merge.pdf", "wb"))
